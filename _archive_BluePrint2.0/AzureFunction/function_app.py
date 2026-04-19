import azure.functions as func
import json
import os
import uuid
import threading
import logging
from datetime import datetime, timezone
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError
from azure.storage.blob import BlobServiceClient

from blueprint_engine import run_blueprint_pipeline, list_sharepoint_folders

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


class _PersistentJobRecord(dict):
    def __init__(self, initial: dict, persist_callback):
        super().__init__(initial)
        self._persist_callback = persist_callback

    def _persist(self) -> None:
        self._persist_callback(dict(self))

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._persist()

    def __delitem__(self, key):
        super().__delitem__(key)
        self._persist()

    def clear(self):
        super().clear()
        self._persist()

    def pop(self, key, default=None):
        result = super().pop(key, default)
        self._persist()
        return result

    def popitem(self):
        result = super().popitem()
        self._persist()
        return result

    def setdefault(self, key, default=None):
        result = super().setdefault(key, default)
        self._persist()
        return result

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._persist()


class _PersistentJobStore(dict):
    def __init__(self):
        self._cache = {}
        connection_string = (
            os.environ.get("BLUEPRINT_JOBS_STORAGE_CONNECTION_STRING")
            or os.environ.get("AzureWebJobsStorage", "")
        )
        container_name = os.environ.get("BLUEPRINT_JOBS_CONTAINER", "blueprint-jobs")
        self._container_client = None

        if connection_string:
            blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            self._container_client = blob_service_client.get_container_client(container_name)
            try:
                self._container_client.create_container()
            except ResourceExistsError:
                pass
        else:
            logging.warning(
                "No persistent storage connection string configured for jobs; "
                "falling back to in-memory cache only."
            )

    def _blob_name(self, job_id: str) -> str:
        return f"jobs/{job_id}.json"

    def _wrap(self, job_id: str, data: dict):
        return _PersistentJobRecord(data, lambda updated: self._save(job_id, updated))

    def _save(self, job_id: str, data: dict) -> None:
        normalized = dict(data)
        self._cache[job_id] = normalized
        if self._container_client is not None:
            self._container_client.upload_blob(
                name=self._blob_name(job_id),
                data=json.dumps(normalized),
                overwrite=True
            )

    def _load(self, job_id: str):
        if job_id in self._cache:
            return self._wrap(job_id, self._cache[job_id])

        if self._container_client is None:
            return None

        try:
            blob_client = self._container_client.get_blob_client(self._blob_name(job_id))
            payload = blob_client.download_blob().readall()
        except ResourceNotFoundError:
            return None

        if isinstance(payload, bytes):
            payload = payload.decode("utf-8")

        data = json.loads(payload)
        self._cache[job_id] = data
        return self._wrap(job_id, data)

    def get(self, key, default=None):
        job = self._load(key)
        return default if job is None else job

    def __getitem__(self, key):
        job = self._load(key)
        if job is None:
            raise KeyError(key)
        return job

    def __setitem__(self, key, value):
        self._save(key, dict(value))

    def __contains__(self, key):
        return self._load(key) is not None

    def pop(self, key, default=None):
        existing = self._load(key)
        if existing is None:
            return default

        self._cache.pop(key, None)
        if self._container_client is not None:
            try:
                self._container_client.delete_blob(self._blob_name(key))
            except ResourceNotFoundError:
                pass
        return dict(existing)


# ── Persistent job store ───────────────────────────────────────────────────────
JOBS: dict = _PersistentJobStore()
JOBS_LOCK = threading.Lock()

API_KEY = os.environ.get("BLUEPRINT_API_KEY", "")
TEAMSFX_ENV = (os.environ.get("TEAMSFX_ENV", "") or "").strip().lower()
ALLOW_MISSING_API_KEY = (os.environ.get("BLUEPRINT_ALLOW_MISSING_API_KEY", "") or "").strip().lower() in {
    "1", "true", "yes", "on"
}


def _verify_api_key(req: func.HttpRequest) -> bool:
    if not API_KEY:
        if TEAMSFX_ENV in {"local", "dev"} or ALLOW_MISSING_API_KEY:
            logging.warning(
                "BLUEPRINT_API_KEY not set — allowing access only because local/dev mode or explicit bypass is enabled"
            )
            return True
        logging.error("BLUEPRINT_API_KEY not set — denying access outside local/dev mode")
        return False
    return req.headers.get("X-API-Key") == API_KEY


# ── POST /api/generate ─────────────────────────────────────────────────────────
@app.route(route="generate", methods=["POST"])
def generate_blueprint(req: func.HttpRequest) -> func.HttpResponse:
    if not _verify_api_key(req):
        return func.HttpResponse(
            json.dumps({"error": "Unauthorized"}),
            status_code=401, mimetype="application/json"
        )

    try:
        params = req.get_json()
    except Exception:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON body"}),
            status_code=400, mimetype="application/json"
        )

    source_folder = (params.get("source_folder") or "").strip()
    project_name  = (params.get("project_name")  or "").strip()

    if not source_folder:
        return func.HttpResponse(
            json.dumps({"error": "source_folder is required"}),
            status_code=400, mimetype="application/json"
        )
    if not project_name:
        return func.HttpResponse(
            json.dumps({"error": "project_name is required"}),
            status_code=400, mimetype="application/json"
        )

    output_language = params.get("output_language", "English")
    if output_language not in ("Italian", "English", "Spanish"):
        output_language = "English"

    output_filename = params.get("output_filename") or f"Blueprint_{project_name.replace(' ', '_')}.docx"

    job_id = str(uuid.uuid4())[:8]
    with JOBS_LOCK:
        JOBS[job_id] = {
            "status": "running",
            "started_at": datetime.now(timezone.utc).isoformat(),
            "finished_at": None,
            "output_url": None,
            "sections_filled": None,
            "open_questions": None,
            "error": None,
        }

    logging.info(f"[{job_id}] Job started: project={project_name}, lang={output_language}")

    try:
        result = run_blueprint_pipeline(
            source_folder=source_folder,
            project_name=project_name,
            output_language=output_language,
            output_filename=output_filename,
        )
        with JOBS_LOCK:
            JOBS[job_id].update({
                "status": "done",
                "finished_at": datetime.now(timezone.utc).isoformat(),
                "output_url": result["output_url"],
                "sections_filled": result["sections_filled"],
                "open_questions": result["open_questions"],
            })

        return func.HttpResponse(
            json.dumps({
                "job_id": job_id,
                "status": "done",
                "message": "Blueprint generation completed.",
                "poll_url": f"/api/status/{job_id}",
                "output_url": result["output_url"],
                "sections_filled": result["sections_filled"],
                "open_questions": result["open_questions"],
            }),
            status_code=200, mimetype="application/json"
        )
    except Exception as exc:
        logging.exception(f"[{job_id}] Pipeline error")
        with JOBS_LOCK:
            JOBS[job_id].update({
                "status": "error",
                "finished_at": datetime.now(timezone.utc).isoformat(),
                "error": str(exc),
            })

        return func.HttpResponse(
            json.dumps({
                "job_id": job_id,
                "status": "error",
                "error": str(exc),
                "poll_url": f"/api/status/{job_id}",
            }),
            status_code=500, mimetype="application/json"
        )
# ── GET /api/status/{job_id} ───────────────────────────────────────────────────
@app.route(route="status/{job_id}", methods=["GET"])
def check_status(req: func.HttpRequest) -> func.HttpResponse:
    if not _verify_api_key(req):
        return func.HttpResponse(
            json.dumps({"error": "Unauthorized"}),
            status_code=401, mimetype="application/json"
        )

    job_id = req.route_params.get("job_id", "")
    with JOBS_LOCK:
        job = JOBS.get(job_id)

    if not job:
        return func.HttpResponse(
            json.dumps({"error": f"Job '{job_id}' not found"}),
            status_code=404, mimetype="application/json"
        )

    return func.HttpResponse(
        json.dumps({"job_id": job_id, **job}),
        status_code=200, mimetype="application/json"
    )


# ── GET /api/projects ──────────────────────────────────────────────────────────
@app.route(route="projects", methods=["GET"])
def list_projects(req: func.HttpRequest) -> func.HttpResponse:
    if not _verify_api_key(req):
        return func.HttpResponse(
            json.dumps({"error": "Unauthorized"}),
            status_code=401, mimetype="application/json"
        )

    try:
        projects = list_sharepoint_folders()
        return func.HttpResponse(
            json.dumps({"projects": projects}),
            status_code=200, mimetype="application/json"
        )
    except Exception as exc:
        logging.exception("Error listing projects")
        return func.HttpResponse(
            json.dumps({"error": str(exc)}),
            status_code=500, mimetype="application/json"
        )
