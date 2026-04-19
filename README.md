# BluePrintGenerator v2.0

Agente Copilot (Declarative Agent) per la generazione automatica di documenti **Blueprint Enel-GICT** (.docx) a partire da materiali di progetto (PPTX, PDF, DOCX) presenti su SharePoint.

---

## Indice

1. [Prerequisiti](#prerequisiti)
2. [Struttura del repository](#struttura-del-repository)
3. [Variabili d'ambiente](#variabili-dambiente)
4. [Come fare il sideload in Teams / Copilot](#come-fare-il-sideload)
5. [Endpoint del backend (Azure Function)](#endpoint-del-backend)
6. [Configurare la chiave API (ApiKeyPluginVault)](#configurare-la-chiave-api)
7. [Sviluppo locale](#sviluppo-locale)
8. [CI / Validazione automatica](#ci--validazione-automatica)

---

## Prerequisiti

| Strumento | Versione minima | Note |
|-----------|----------------|------|
| Node.js | 18 LTS | Richiesto da `@microsoft/teamsapp-cli` |
| Teams App CLI | 3.x | `npm install -g @microsoft/teamsapp-cli` |
| Python | 3.11+ | Per l'Azure Function locale |
| Azure Functions Core Tools | 4.x | `npm install -g azure-functions-core-tools@4` |
| Azure CLI | 2.50+ | Per il deploy dell'Azure Function |
| Account Microsoft 365 | con permessi sideload | Developer tenant o tenant Enel abilitato |

---

## Struttura del repository

```
BluePrintGenerator_v2.0/
├── appPackage/                  # Pacchetto Teams/Copilot (cartella attiva)
│   ├── manifest.json            # Manifest Teams v1.25
│   ├── declarativeAgent.json    # Definizione agente dichiarativo v1.6
│   ├── instruction.txt          # Prompt di sistema dell'agente
│   ├── blueprintPlugin.json     # Plugin OpenAPI (API Actions)
│   └── openapi.yaml             # Specifica OpenAPI 3.0 del backend
├── agents/
│   └── ISTRUZIONI_DEFINITIVE_BLUEPRINT.md  # Logica dettagliata (riferimento)
├── env/                         # File .env per variabili locali (non committare)
├── .github/workflows/           # CI GitHub Actions
│   └── validate.yml
├── m365agents.yml               # Config Teams App CLI (produzione)
├── _archive_BluePrint2.0/       # Materiale legacy archiviato (non in produzione)
│   └── AzureFunction/           # Backend Python (archivio — function_app.py, blueprint_engine.py, …)
└── README.md
```

---

## Variabili d'ambiente

Creare un file `env/.env.dev` (non committare mai file con valori reali):

```dotenv
# ID dell'app Teams (generato da Teams Dev Portal o teamsapp provision)
TEAMS_APP_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

# URL base dell'Azure Function App (es. https://blueprint-fn.azurewebsites.net)
BLUEPRINT_API_BASE_URL=https://<your-function-app>.azurewebsites.net

# Reference ID del secret nel Teams Vault per la chiave API
# Vedere sezione "Configurare la chiave API" per il procedimento
BLUEPRINT_API_KEY_REFERENCE_ID=<vault-reference-id>
```

---

## Come fare il sideload

### Sideload locale (Teams desktop/web)

```bash
# 1. Installa le dipendenze CLI
npm install -g @microsoft/teamsapp-cli

# 2. Accedi al tenant Microsoft 365
teamsapp auth login m365

# 3. Provisioning (prima volta)
teamsapp provision --env dev

# 4. Deploy del pacchetto agente
teamsapp deploy --env dev

# 5. Avvia Teams e cerca "BlueprintGenerator" in Copilot
teamsapp preview --env dev
```

### Pacchetto .zip manuale

```bash
teamsapp package --env dev
# Output: appPackage/build/appPackage.dev.zip
```

Carica lo zip su [Teams Admin Center](https://admin.teams.microsoft.com) → App Teams → Carica app personalizzata.

---

## Endpoint del backend

Il backend è un'Azure Function App con i seguenti HTTP trigger:

| Metodo | Path | operationId | Descrizione |
|--------|------|-------------|-------------|
| POST | `/api/generate` | `generateBlueprint` | Avvia generazione async |
| GET | `/api/status/{job_id}` | `checkBlueprintStatus` | Poll stato job |
| GET | `/api/projects` | `listProjects` | Lista cartelle SharePoint |
| POST | `/api/section/{job_id}` | `regenerateSection` | Rigenera sezione singola |
| GET | `/api/log/{job_id}` | `getJobLog` | Log di esecuzione job |

Autenticazione: **API Key** nell'header `X-API-Key`.

Specifiche complete: [appPackage/openapi.yaml](appPackage/openapi.yaml)

---

## Configurare la chiave API (ApiKeyPluginVault)

Il plugin usa `ApiKeyPluginVault` per iniettare la chiave API senza esporla all'utente.

### Passaggi

1. **Generare una chiave API** nel portale Azure → Function App → Chiavi → Nuova chiave host.

2. **Registrare il secret nel Teams Developer Portal**:
   - Accedi a [Teams Developer Portal](https://dev.teams.microsoft.com)
   - Seleziona la tua app → *Configure* → *API key*
   - Inserisci la chiave e salva — il portale restituisce un `reference_id`

3. **Impostare la variabile d'ambiente**:
   ```dotenv
   BLUEPRINT_API_KEY_REFERENCE_ID=<reference_id_dal_portale>
   ```

4. **Non committare mai** la chiave API nel repository. Usare Azure Key Vault o GitHub Secrets per ambienti CI/CD.

---

## Sviluppo locale

### Azure Function locale

```bash
cd _archive_BluePrint2.0/AzureFunction
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
func start
# Function app avviata su http://localhost:7071
```

### Testare l'API localmente

```bash
# Lista progetti
curl http://localhost:7071/api/projects -H "X-API-Key: <chiave-locale>"

# Avvia generazione
curl -X POST http://localhost:7071/api/generate \
  -H "Content-Type: application/json" \
  -H "X-API-Key: <chiave-locale>" \
  -d '{"source_folder":"Test Project","project_name":"Test","output_language":"Italian"}'
```

Aggiornare `BLUEPRINT_API_BASE_URL=http://localhost:7071` nel file `.env.local` per il sideload locale.

---

## CI / Validazione automatica

Il workflow `.github/workflows/validate.yml` esegue automaticamente ad ogni PR verso `main`:

- Validazione di `manifest.json`, `declarativeAgent.json`, `blueprintPlugin.json` con `teamsapp validate`
- Lint di `openapi.yaml` con `spectral lint`
- Verifica delle variabili d'ambiente obbligatorie

Vedere [.github/workflows/validate.yml](.github/workflows/validate.yml) per i dettagli.

