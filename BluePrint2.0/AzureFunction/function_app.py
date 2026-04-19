import azure.functions as func
import json
import os
import uuid
import threading
import logging
from datetime import datetime, timezone

from blueprint_engine import run_blueprint_pipeline, list_sharepoint_folders

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# ── In-memory job store ────────────────────────────────────────────────────────
JOBS: dict = {}
JOBS_LOCK = threading.Lock()

API_KEY = os.environ.get("BLUEPRINT_API_KEY", "")


def _verify_api_key(req: func.HttpRequest) -> bool:
    if not API_KEY:
        logging.warning("BLUEPRINT_API_KEY not set — open access (dev mode)")
        return True
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
