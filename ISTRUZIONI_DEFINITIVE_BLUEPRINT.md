# BlueprintGenerator Agent - ISTRUZIONI DEFINITIVE

## Template Standard Obbligatorio  
**SEMPRE utilizzare**: `Blueprint_1.4_vuoto.docx`

### Ubicazione Template
```
Template Path: C:\Users\A405260\Enel Spa\AI Scale Up Accelerator - Canale Grids e EGP TGX\Template Blueprint\Blueprint_1.4_vuoto.docx
```

## WORKFLOW COMPLETO OBBLIGATORIO

### Phase 1 — Environment Setup  
```python
# Verificare sempre Python e librerie
python --version  # Python 3.14+
python -c "import docx; import fitz; import pptx; print('All OK')"
```

### Phase 2 — Template Analysis
```python  
def find_para(doc, text_fragment, style=None, start=0):
    """OBBLIGATORIO - usare sempre invece di indici fissi"""
    
def set_para_text(para, new_text):
    """FORMATO CORRETTO - preserva formatting"""
    try:
        if para.runs:
            first_run = para.runs[0]
            font_name = first_run.font.name
            font_size = first_run.font.size
            font_bold = first_run.font.bold
            font_italic = first_run.font.italic
            
            para.clear()
            new_run = para.add_run(new_text)
            
            if font_name: new_run.font.name = font_name
            if font_size: new_run.font.size = font_size  
            if font_bold: new_run.font.bold = font_bold
            if font_italic: new_run.font.italic = font_italic
        else:
            para.text = new_text
    except:
        para.text = new_text
```

### Phase 3 — Content Extraction & Synthesis
- **Extractar TUTTO il contenuto** dalle fonti disponibili
- **Sintetizzare per ogni sezione** specifica del template
- **Non lasciare mai tabelle vuote** o sezioni incomplete

### Phase 4 — Document Generation COMPLETO

#### SEZIONI OBBLIGATORIE in ESPAÑOL:

**1. Título Principal**: 
```
"Blueprint – BTP – [Nombre Proyecto] con Inteligencia Artificial"
```

**2. Resumen Ejecutivo (4 paragrafi)**:
- Situación Actual (AS-IS) con limitaciones específicas
- Solución Propuesta (TO-BE) con tecnología IA
- Beneficios Cuantificables con métricas precisas  
- Inversión y Retorno con timeframes realistas

**3. Contexto y Finalidad**:
- **1.1 Alcance**: 1-2 frases objetivo proceso
- **1.2 Finalidad**: 4-5 bullets objetivos específicos
- **1.3 Perímetro**: IN SCOPE (3 items) + OUT OF SCOPE (2 items)  
- **1.4 Restricciones Clave**: NORMATIVAS / TÉCNICAS / ORGANIZATIVAS

#### TABLAS OBLIGATORIAS (13 totales) - TUTTE DA RIEMPIRE:

**Tabla 0 - Roles**: Business Owner, Data Owner, IT Owner, Product Owner + specifici progetto

**Tabla 1 - Sistemas**: Core Platform, Integration Layer, External Systems

**Tabla 2 - AS-IS Process Cards**: 4 Macroactividades con Input/Actividades/Salida/Punto Crítico/Intervención Humana

**Tablas 3,4 - AS-IS Sequences**: Subprocesos detallados paso-paso  

**Tabla 5 - Data Mapping**: ≥6 flussi dati con Sistema Origen → Sistema Destino

**Tabla 6 - Arquitectura Funcional**: ≥7 componenti técnicos con Función + Tecnología  

**Tablas 7,8,9 - TO-BE Sequences**: Con columna **"IA+Intervención Humana"** OBLIGATORIA

**Tabla 10 - Roadmap**: 6 fases M1-M12+ con Objetivos + Entregables + Duración

**Tabla 11 - KPIs Cuantitativos**: 4 KPIs con AS-IS + Target TO-BE + % Mejora

**Tabla 12 - KPIs Cualitativos**: 4 KPIs con Target + Método Medición

#### PROCESS CARDS DETALLADAS - OBLIGATORIAS:

```
3.1 PROCESO ACTUAL (AS-IS) - [NOMBRE]

MACROACTIVIDAD A: [NOMBRE]
Entrada: • [elementos input específicos]
Actividades AS-IS: [lista numerada 1-N]  
Salida: • [deliverables específicos]
Punto Crítico: [limitación específica proceso actual]
Intervención Humana / Nota: N/A — proceso manual AS-IS

[Repetir per 3-4 Macroactividades]

4.1 PROCESO FUTURO (TO-BE) - [NOMBRE CON IA]

MACROACTIVIDAD A: [NOMBRE MEJORADO]  
Entrada: • [input, algunos unchanged]
Actividades TO-BE: [actividades optimizadas con IA]
Salida: • [deliverables mejorados] 
Sistemas: [plataformas involucradas]
Intervención Humana: [donde require expertise humana]

[Repetir per 3-4 Macroactividades]
```

#### SECCIÓN DELTA OBLIGATORIA:

```
5. COMPARATIVA AS-IS vs TO-BE

SITUACIÓN ACTUAL (AS-IS) - LIMITACIONES:  
• [5-6 limitaciones específicas con métricas]

5.1 IMPACTOS OPERATIVOS TO-BE:
• [5-6 mejoras operativas específicas]

5.2 INVARIANTES (NO CAMBIA):  
• [4-5 elementos que se mantienen]

5.3 NUEVOS REQUISITOS HABILITANTES:
• [4-5 requirements nuevos para TO-BE]

SITUACIÓN OBJETIVO (TO-BE) - BENEFICIOS:
• [5-6 beneficios específicos con impacto]
```

### TRADUCCIÓN COMPLETA AL ESPAÑOL - OBLIGATORIA

**Dictionary Traducciones**:
```python
translations = {
    # Títulos principales
    "Sommario Esecutivo": "Resumen Ejecutivo",
    "Contesto e finalità": "Contexto y Finalidad",
    "Scopo": "Alcance", 
    "Finalità": "Finalidad",
    "Perimetro": "Perímetro",
    "Vincoli chiave": "Restricciones Clave",
    
    # Headers tablas  
    "Ruolo": "Rol",
    "Nome / Unità Org.": "Nombre / Unidad Organizativa",
    "Responsabilità": "Responsabilidades",
    "Sistema": "Sistema",
    "Tipologia": "Tipología", 
    "Data Mapping": "Mapeo de Datos",
    "Dato": "Dato",
    "Sistema Sorgente": "Sistema Origen",
    "Sistema Destinazione": "Sistema Destino",
    "Architettura Funzionale": "Arquitectura Funcional",
    "Componente": "Componente",
    "Funzione": "Función",  
    "Tecnologia/Metodo": "Tecnología/Método",
    "Roadmap": "Hoja de Ruta",
    "Fase": "Fase",
    "Obiettivo": "Objetivo",
    "Output": "Entregable", 
    "Durata": "Duración",
    "AS-IS": "Situación Actual",
    "Target TO-BE": "Objetivo Futuro",
    "Miglioramento": "Mejora",
    
    # Proceso
    "Step": "Paso",
    "Attività": "Actividad",
    "Attore": "Actor", 
    "Input": "Entrada",
    "Sistemi": "Sistemas",
    "AI+HITL": "IA+Intervención Humana"
}
```

## EXECUTION COMMAND  

**Per OGNI generazione Blueprint**:

```python
def generate_complete_spanish_blueprint():
    # 1. Load Template 1.4 OBBLIGATORIO
    template_path = r"...\Blueprint_1.4_vuoto.docx"
    
    # 2. Fill ALL sections ESPAÑOL  
    # - Título principal
    # - Resumen Ejecutivo (4 paragrafi)
    # - Contexto y Finalidad (1.1-1.4)
    
    # 3. Fill ALL 13 tables COMPLETAMENTE
    # - NO lasciare tabelle vuote
    # - Específico per domain del progetto
    
    # 4. Add Process Cards DETALLADAS
    # - AS-IS: ≥3 Macroactividades  
    # - TO-BE: ≥3 Macroactividades
    # - Con Input/Actividades/Salida/Sistemas/HITL
    
    # 5. Add Delta Section ESTRUTURADA  
    # - AS-IS limitations
    # - TO-BE impacts + Invariantes + Requirements
    # - TO-BE benefits
    
    # 6. Translate ALL títulos español
    
    # 7. Save as Blueprint_[ProjectName]_ES_FINAL.docx
```

## VALIDATION CHECKLIST OBBLIGATORIA

Before saving, VERIFICARE:
- [ ] Template 1.4 utilizzato
- [ ] Título principal in español  
- [ ] Resumen Ejecutivo 4 paragraphs específicos
- [ ] Secciones 1.1-1.4 complete in español
- [ ] 13/13 tablas filled >90%  
- [ ] Process Cards AS-IS + TO-BE detalladas
- [ ] Sección Delta estruturada 5.1/5.2/5.3  
- [ ] ALL títulos translated español
- [ ] Content específico per domain progetto
- [ ] KPIs con métricas quantitative precisas
- [ ] Columna "IA+Intervención Humana" in TO-BE tables

## RISULTATO FINALE

**Output File**: `Blueprint_[ProjectName]_ES_FINAL.docx`

**Contenuto**:  
✅ 100% ESPAÑOL (títulos + contenuto)  
✅ Template 1.4 con ALL secciones filled
✅ Process Cards detallate con macroactividades  
✅ 13 tabelle completamente filled 
✅ Delta AS-IS vs TO-BE ben strutturato
✅ Domain-specific content estratto da fonti
✅ KPIs quantitativi + qualitativi realistici

**Quality Standard**: ≥95% completeness + 100% español + domain accuracy

Esta metodología è DEFINITIVA per ALL future Blueprint generations.