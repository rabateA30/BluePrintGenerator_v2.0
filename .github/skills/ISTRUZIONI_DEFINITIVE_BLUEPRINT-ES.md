# BlueprintGenerator Agent — ISTRUZIONI DEFINITIVE (Español)

> **Attivazione**: queste istruzioni si applicano **ogni volta che l'utente richiede un Blueprint in lingua Spagnola**.

---

## Regola Lingua — DOPPIO CHECK OBBLIGATORIO

Tutto il contenuto generato deve essere in **Español correcto** con accenti ortografici precisi.

### Accenti obbligatori — parole frequenti nel dominio Blueprint

| Errato | Corretto |
|---|---|
| proceso | proceso ✓ |
| analisis | análisis ✓ |
| informacion | información ✓ |
| gestion | gestión ✓ |
| solucion | solución ✓ |
| comunicacion | comunicación ✓ |
| validacion | validación ✓ |
| automatizacion | automatización ✓ |
| optimizacion | optimización ✓ |
| configuracion | configuración ✓ |
| integracion | integración ✓ |
| clasificacion | clasificación ✓ |
| implementacion | implementación ✓ |
| generacion | generación ✓ |
| documentacion | documentación ✓ |
| evaluacion | evaluación ✓ |
| operacion | operación ✓ |
| visualizacion | visualización ✓ |
| prediccion | predicción ✓ |
| actualizacion | actualización ✓ |
| notificacion | notificación ✓ |
| planificacion | planificación ✓ |
| verificacion | verificación ✓ |
| extracion | extracción ✓ |
| revision | revisión ✓ |
| tecnico | técnico ✓ |
| metodo | método ✓ |
| calidad | calidad ✓ |
| estandar | estándar ✓ |
| numero | número ✓ |
| area | área ✓ |
| critico | crítico ✓ |
| especifico | específico ✓ |
| diagnostico | diagnóstico ✓ |
| automatico | automático ✓ |
| periodico | periódico ✓ |
| historico | histórico ✓ |

### Regole tilde obbligatorie

- **Parole acute** (acento en la última sílaba): terminano in vocale, -n, -s → acento: `también`, `según`, `después`
- **Parole piane** (acento en la penúltima): terminano in consonante diversa da -n, -s → acento: `fácil`, `útil`
- **Parole interrogative/esclamative**: sempre accentate → `¿qué?`, `¿cómo?`, `¿cuándo?`, `¿dónde?`, `¿por qué?`
- **Distinzioni semantiche**: `sí` (sì) vs `si` (se) · `él` (lui) vs `el` (il) · `más` (più) vs `mas` (ma) · `sólo/solo` (verificare contesto)

### Checklist Lingua prima del salvataggio

```
□ Nessuna parola con accento mancante
□ Tutti i titoli di sezione con accenti corretti
□ Intestazioni tabelle in español corretto
□ Testo delle Fichas de Proceso con accenti
□ Puntos Críticos, KPI e Roadmap con accenti
□ Nessun termine italiano o inglese mescolato al testo spagnolo
□ Punteggiatura interrogativa/esclamativa con apertura: ¿ / ¡
```

---

## Template Standard Obbligatorio

**SEMPRE utilizzare**: `Blueprint_Template_1.5_vacio-ES.docx`

```
Template Path: BluePrintGenerator_v2.0/TEMPLATE/Blueprint_Template_1.5_vacio-ES.docx
```

---

## Struttura Documento — Template 1.5 ES

### Titolo principale
```
Blueprint – [NOMBRE PROYECTO]
```

---

### 1. Resumen Ejecutivo
Sezione testuale introduttiva a livello documento:

| Campo | Contenuto |
|---|---|
| Procesos Identificados | Elenco processi coperti |
| Contexto General | Contesto aziendale/operativo |

---

### Per ogni Proceso (ripetibile)

#### 1. Contexto e Finalidad

| Sezione | Contenuto |
|---|---|
| **1.1 Alcance** | Objetivo claro del proceso |
| **1.2 Finalidad** | Lista objetivos específicos |
| **1.3 Perimetro** | EN ALCANCE / FUERA DE ALCANCE |
| **1.4 Restricciones Clave** | Normativos / Tecnicos / Organizativos |

---

#### Stakeholders y Participantes

**Tabla 0** (10x3) — Roles:

| Rolo | Nombre / Unità Org. | Responsabilidad |
|---|---|---|
| … | … | … |

*(9 righe dati — includere Business Owner, Data Owner, IT Owner, Product Owner + specifici progetto)*

---

#### 2. Proceso AS-IS — Descripción Estructurada

##### 2.1 Sistemas Involucrados (AS-IS)

**Tabla 1** (8x3):

| Herramienta AS-IS | Descripción / Rol | Tipología |
|---|---|---|
| … | … | … |

*(7 righe dati)*

---

##### 2.2 AS-IS — Secuencia Operativa

**Tabla 2** (6x6) — AS-IS Secuencia A *(prefilled Paso A1–A5)*:

| Paso | Actividad | Actor | Entrada | Salida | Sistemas |
|---|---|---|---|---|---|
| A1 | … | … | … | … | … |

**Tabla 3** (5x6) — AS-IS Secuencia B:

| Paso | Actividad | Actor | Entrada | Salida | Sistemas |
|---|---|---|---|---|---|
| … | … | … | … | … | … |

**Tabla 4** (5x6) — AS-IS Secuencia C:

| Paso | Actividad | Actor | Entrada | Salida | Sistemas |
|---|---|---|---|---|---|
| … | … | … | … | … | … |

---

##### 2.3 Fichas de Proceso AS-IS (sezione testuale — OBBLIGATORIA)

Compilare **almeno 3 Fichas**. Formato per ciascuna:

```
Ficha N: [NOMBRE SUBPROCESO]
Entrada: [elementos input específicos]
Actividades:
  1. [actividad específica]
  2. ...
Salida: [deliverables]
Punto Crítico: [limitación específica del proceso actual]
```

---

##### 2.4 Puntos Críticos Principales (AS-IS)

```
Puntos Críticos Generales:
• [punto crítico específico 1]
• [punto crítico específico 2]
• [punto crítico específico N]
```

---

#### 3. Proceso TO-BE

##### 3.1 Arquitectura Funcional IA

**Tabla 5** (7x5):

| Componente | Función | Tecnología/Método | Agente Común | Note |
|---|---|---|---|---|
| … | … | … | … | … |

*(6 righe dati — min 5 componenti compilati)*

---

##### 3.2 Mapeo de Datos-Sistemas TO-BE (AI-ENABLED)

**Tabla 6** (3x5):

| Dato | Sistema Origen | Sistema Destino | Formato | Nota |
|---|---|---|---|---|
| … | … | … | … | … |

*(2 righe dati — specificare flussi dati chiave abilitati dall'AI)*

---

##### 3.2b Secuencia Operativa Detallada (TO-BE)

**Tabla 7** (7x7) — TO-BE Subproceso A — **colonna IA+HITL OBBLIGATORIA**:

| Paso | Actividad | Actor | Entrada | Salida | Sistemas | IA + Intervención Humana |
|---|---|---|---|---|---|---|
| … | … | … | … | … | … | … |

**Tabla 8** (4x7) — TO-BE Subproceso B:

| Paso | Actividad | Actor | Entrada | Salida | Sistemas | IA + Intervención Humana |
|---|---|---|---|---|---|---|
| … | … | … | … | … | … | … |

**Tabla 9** (4x7) — TO-BE Subproceso C:

| Paso | Actividad | Actor | Entrada | Salida | Sistemas | IA + Intervención Humana |
|---|---|---|---|---|---|---|
| … | … | … | … | … | … | … |

---

##### 3.3 Fichas de Proceso TO-BE (sezione testuale — OBBLIGATORIA)

Compilare **almeno 3 Fichas**. Formato per ciascuna:

```
Ficha N: [NOMBRE SUBPROCESO CON IA]
Entrada:
  • [input específico]
Actividades:
  1. [actividad optimizada con IA]
  2. ...
Salida:
  • [deliverable mejorado]
```

---

##### 3.4 Que NO hace la IA (OBBLIGATORIA)

```
• [limitación IA 1 — decisiones que requieren criterio humano]
• [limitación IA 2]
• [limitación IA N]
```

---

#### 4. Delta AS-IS vs TO-BE

##### 4.1 Impactos Operativos

```
• [impacto operativo específico 1]
• [impacto operativo específico 2]
• [impacto operativo específico N]
```

##### 4.2 Invariantes (No Cambia)

```
• [elemento invariante 1]
• [elemento invariante 2]
• [elemento invariante N]
```

---

#### 5. Hoja de Ruta (Draft)

**Duración Total Estimada**: [XXX semanas/meses]

**Tabla 10** (3x4):

| Fase | Objetivo | Entregable | Duración Estimada |
|---|---|---|---|
| … | … | … | … |

*(2 righe dati — espandere se necessario)*

---

#### 6. KPI

**KPI Cuantitativos**

**Tabla 11** (7x4):

| KPI | AS-IS (Situación Actual) | Objetivo TO-BE | Método de Medición |
|---|---|---|---|
| … | … | … | … |

*(6 righe dati — inserire valori numerici baseline + target)*

**KPI Cualitativos**

**Tabla 12** (5x3):

| KPI | Objetivo TO-BE | Método de Medición |
|---|---|---|
| … | … | … |

*(4 righe dati)*

---

## Riepilogo Tabelle — Template 1.5 ES (13 tabelle totali)

| # | Nome | Dim. | Colonne |
|---|---|---|---|
| Tabla 0 | Roles | 10x3 | Rolo \| Nombre/Unità Org. \| Responsabilidad |
| Tabla 1 | Sistemas AS-IS | 8x3 | Herramienta AS-IS \| Descripción/Rol \| Tipología |
| Tabla 2 | AS-IS Secuencia A | 6x6 | Paso \| Actividad \| Actor \| Entrada \| Salida \| Sistemas |
| Tabla 3 | AS-IS Secuencia B | 5x6 | Paso \| Actividad \| Actor \| Entrada \| Salida \| Sistemas |
| Tabla 4 | AS-IS Secuencia C | 5x6 | Paso \| Actividad \| Actor \| Entrada \| Salida \| Sistemas |
| Tabla 5 | Arquitectura Funcional IA | 7x5 | Componente \| Función \| Tecnología/Método \| Agente Común \| Note |
| Tabla 6 | Mapeo Datos TO-BE | 3x5 | Dato \| Sistema Origen \| Sistema Destino \| Formato \| Nota |
| Tabla 7 | TO-BE Secuencia A | 7x7 | Paso \| Actividad \| Actor \| Entrada \| Salida \| Sistemas \| IA+HITL |
| Tabla 8 | TO-BE Secuencia B | 4x7 | idem |
| Tabla 9 | TO-BE Secuencia C | 4x7 | idem |
| Tabla 10 | Hoja de Ruta | 3x4 | Fase \| Objetivo \| Entregable \| Duración Estimada |
| Tabla 11 | KPI Cuantitativos | 7x4 | KPI \| AS-IS \| Objetivo TO-BE \| Método de Medición |
| Tabla 12 | KPI Cualitativos | 5x3 | KPI \| Objetivo TO-BE \| Método de Medición |

---

## Helper Functions Python — OBBLIGATORIE

```python
def find_para(doc, text_fragment, style=None, start=0):
    """Usare sempre invece di indici fissi."""
    if start < 0:
        raise ValueError("start must be >= 0")
    for para in doc.paragraphs[start:]:
        if text_fragment not in para.text:
            continue
        if style is not None:
            para_style = getattr(getattr(para, "style", None), "name", None)
            if para_style != style:
                continue
        return para
    raise ValueError(
        f"Paragraph not found: fragment={text_fragment!r}, style={style!r}, start={start}"
    )

def set_para_text(para, new_text):
    """Sostituisce testo preservando il formatting."""
    try:
        if para.runs:
            first_run = para.runs[0]
            font_name  = first_run.font.name
            font_size  = first_run.font.size
            font_bold  = first_run.font.bold
            font_italic = first_run.font.italic
            para.clear()
            new_run = para.add_run(new_text)
            if font_name:   new_run.font.name   = font_name
            if font_size:   new_run.font.size   = font_size
            if font_bold:   new_run.font.bold   = font_bold
            if font_italic: new_run.font.italic = font_italic
        else:
            para.text = new_text
    except Exception:
        para.text = new_text
```

---

## Sequenza di Generazione — OBBLIGATORIA

```python
def generate_spanish_blueprint_1_5():
    # 1. Caricare template 1.5 ES
    template_path = r"...\Blueprint_Template_1.5_vacio-ES.docx"

    # 2. Compilare Resumen Ejecutivo
    # 3. Compilare Contexto y Finalidad (1.1–1.4)
    # 4. Compilar Tabla 0 (Roles) — min 4 righe
    # 5. Compilar Tabla 1 (Sistemas AS-IS) — min 3 righe
    # 6. Compilar Tablas 2, 3, 4 (AS-IS Secuencias) — nessuna cella vuota
    # 7. Compilar Fichas AS-IS (2.3) — min 3 Fichas testuali
    # 8. Compilar Puntos Críticos (2.4)
    # 9. Compilar Tabla 5 (Arquitectura Funcional IA) — min 5 componenti
    # 10. Compilar Tabla 6 (Mapeo Datos TO-BE)
    # 11. Compilar Tablas 7, 8, 9 (TO-BE Secuencias) — colonna IA+HITL sempre compilata
    # 12. Compilar Fichas TO-BE (3.3) — min 3 Fichas testuali
    # 13. Compilar sección 3.4 "Que NO hace la IA"
    # 14. Compilar Delta 4.1 Impactos + 4.2 Invariantes
    # 15. Compilar Tabla 10 (Hoja de Ruta)
    # 16. Compilar Tabla 11 (KPI Cuantitativos) — valori numerici precisi
    # 17. Compilar Tabla 12 (KPI Cualitativos)
    # 18. Salvare come Blueprint_[NombreProyecto]_ES_FINAL.docx
```

---

## Validation Checklist

```
□ Template Blueprint_Template_1.5_vacio-ES.docx utilizzato
□ Resumen Ejecutivo compilato
□ Secciones 1.1–1.4 complete (Alcance/Finalidad/Perimetro/Restricciones)
□ Tabla 0 — Roles (min 4 righe)
□ Tabla 1 — Herramientas AS-IS (min 3 righe)
□ Tablas 2/3/4 — AS-IS Secuencias (tutte le celle compilate)
□ Fichas AS-IS 2.3 — min 3 Fichas con Entrada/Actividades/Salida/Punto Crítico
□ Puntos Críticos 2.4 — specifici del dominio
□ Tabla 5 — Arquitectura Funcional IA con colonna "Agente Común"
□ Tabla 6 — Mapeo Datos TO-BE compilata
□ Tablas 7/8/9 — TO-BE Secuencias con colonna "IA + Intervención Humana" compilata
□ Fichas TO-BE 3.3 — min 3 Fichas
□ Sección 3.4 "Que NO hace la IA" presente
□ Delta 4.1 Impactos Operativos
□ Delta 4.2 Invariantes (No Cambia)
□ Tabla 10 — Hoja de Ruta con Entregables
□ Tabla 11 — KPI Cuantitativos con baseline + objetivo TO-BE numerici
□ Tabla 12 — KPI Cualitativos con método de medición
□ Output: Blueprint_[NombreProyecto]_ES_FINAL.docx
```