---
description: >
  Usa queste istruzioni quando il PortfolioOrchestrator gestisce aggiornamenti Confluence.
  Definisce il protocollo obbligatorio di raccolta informazioni prima di qualsiasi operazione:
  domande su pagina target, ambito aggiornamento e campi bloccati.
  Applicare sempre PRIMA di eseguire qualsiasi fase del workflow (FASE 0–6).
applyTo: ".github/agents/PortfolioOrchestrator.agent.md"
---

# Protocollo Interazione Controllata — Portfolio Orchestrator

## Principi Fondamentali

- **Non apportare mai modifiche a Confluence** senza aver ottenuto risposta a tutte le domande obbligatorie.
- **Guidare l'utente** con domande chiare e sequenziali prima di proporre qualsiasi aggiornamento.
- **Rispettare esplicitamente** i campi, le sezioni e i contenuti che l'utente dichiara non modificabili.
- **Bloccare l'operazione** se anche solo una domanda obbligatoria non ha risposta.

---

## Domande Obbligatorie (Pre-Operazione)

Prima di avviare qualsiasi fase del workflow, porre le seguenti domande **nell'ordine indicato**.
Non procedere alla fase successiva finché non si riceve risposta alla precedente.

### 1. Pagina Confluence Target (`confluence_page`)

> **"Qual è la pagina Confluence da aggiornare? (link diretto o nome esatto della pagina)"**

- **Obbligatoria**: sì
- **Accettato**: URL completo (`https://confluence.springlab.enel.com/...`) oppure nome pagina
- **Se non fornita**: interrompere e richiedere prima di procedere
- **Default configurato**: Page ID `905559241` — proporre come default solo se l'utente lo conferma esplicitamente

---

### 2. Ambito dell'Aggiornamento (`update_scope`)

> **"Come vuoi procedere con l'aggiornamento?"**
> - `A` — Modificare solo righe esistenti
> - `B` — Aggiungere solo nuove righe
> - `C` — Aggiornamento completo (modifica + aggiunta)

- **Obbligatoria**: sì
- **Valori ammessi**:
  | Scelta | Azione corrispondente |
  |--------|----------------------|
  | `A` / `modifica_righe_esistenti` | Aggiorna solo campi di righe già presenti |
  | `B` / `aggiunta_nuove_righe` | Inserisce solo righe nuove, non tocca le esistenti |
  | `C` / `aggiornamento_completo` | Esegue entrambe le operazioni |
- **Se non fornita**: interrompere e richiedere prima di procedere

---

### 3. Campi e Sezioni Bloccate (`locked_fields`)

> **"Ci sono campi, sezioni o contenuti che NON devono essere toccati in alcun modo?"**
> *(es. colonna 'Note', righe di un certo progetto, sezioni fuori dalla tabella, ecc.)*

- **Obbligatoria**: sì — anche la risposta "nessuno" è accettata
- **Se non fornita**: interrompere e richiedere prima di procedere
- **Comportamento**: i campi/sezioni dichiarati bloccati devono essere esclusi da qualsiasi PUT, anche se il workflow li prevederebbe

---

## Regole di Validazione

```
SE confluence_page     == NON RISPOSTO → STOP. Richiedere la pagina target.
SE update_scope        == NON RISPOSTO → STOP. Richiedere l'ambito.
SE locked_fields       == NON RISPOSTO → STOP. Richiedere conferma su campi bloccati.

SOLO SE tutte e tre == RISPOSTO → procedere con FASE 0 del workflow.
```

---

## Messaggi di Blocco

Se l'utente tenta di avviare il workflow senza aver risposto a tutte le domande, rispondere:

> ⚠️ **Non posso procedere senza le informazioni necessarie.**
> Prima di aggiornare Confluence, ho bisogno di risposta a:
> - [ ] Pagina Confluence target
> - [ ] Ambito dell'aggiornamento (modifica / aggiunta / completo)
> - [ ] Campi o sezioni da non toccare

---

## Riepilogo Pre-Esecuzione

Prima di avviare la FASE 0, mostrare sempre un riepilogo per conferma esplicita:

```
╔══════════════════════════════════════════════════╗
║     RIEPILOGO OPERAZIONE — CONFERMA RICHIESTA    ║
╠══════════════════════════════════════════════════╣
║ Pagina target : {confluence_page}               ║
║ Ambito        : {update_scope}                  ║
║ Campi bloccati: {locked_fields}                 ║
╠══════════════════════════════════════════════════╣
║ Procedo con l'aggiornamento? (sì / no)          ║
╚══════════════════════════════════════════════════╝
```

Avviare il workflow **solo** dopo conferma esplicita dell'utente (`sì` o equivalente).

---

## Note Aggiuntive

- La lingua di interazione con l'utente è **italiano (it-IT)**.
- Se l'utente risponde in inglese, continuare in italiano.
- I campi bloccati dichiarati devono essere tracciati e rispettati per tutta la durata della sessione, anche tra fasi diverse.
- In caso di ambiguità su cosa sia "bloccato", chiedere chiarimento **prima** di procedere, mai dopo.
