# Blueprint Generator Agent - Template 1.4 METODOLOGÍA COMPLETA

## Nuevo Template Estándar
**IMPORTANTE**: A partir de ahora, usar siempre `Blueprint_1.4_vuoto.docx` como template base para todas las generaciones futuras.

### Ubicación Template
```
Template Path: C:\Users\A405260\Enel Spa\AI Scale Up Accelerator - Canale Grids e EGP TGX\Template Blueprint\Blueprint_1.4_vuoto.docx
```

### Estructura Template 1.4 - COMPLETA

El template 1.4 incluye las siguientes secciones mejoradas vs versiones anteriores:

#### 1. Sección Contextual Mejorada
- **1.1 Scopo**: Definición clara del objetivo del proceso
- **1.2 Finalità**: Lista de objetivos específicos (4-5 bullets)  
- **1.3 Perimetro**: IN SCOPE / OUT OF SCOPE claramente separados
- **1.4 Vincoli Chiave**: Categorías NORMATIVI / TECNICI / ORGANIZZATIVI

#### 2. Process Cards DETALLADAS - OBLIGATORIAS
**SIEMPRE incluir estas secciones después de las tablas:**

```
3.1 PROCESO ACTUAL (AS-IS) - [NOMBRE PROCESO]

MACROATTIVITÀ A: [NOMBRE MACRO-ACTIVIDAD]
Input: • [elementos input específicos]
Attività AS-IS: [lista numerada 1-N actividades]
Output: • [deliverables específicos]
Pain Point: [limitaciones proceso actual]
HITL / Note: N/A — proceso manual AS-IS

MACROATTIVITÀ B: [SEGUNDA MACRO-ACTIVIDAD]
[mismo formato]

4.1 PROCESO FUTURO (TO-BE) - [NOMBRE PROCESO CON IA]

MACROATTIVITÀ A: [NOMBRE MEJORADO]
Input: • [elementos input, alcuni unchanged]
Attività TO-BE: [actividades optimizadas con IA]
Output: • [deliverables mejorados]
Sistemi: [sistemas involucrados]
HITL: [intervención humana requerida]
```

#### 3. Tablas Estandarizadas (13 tablas totales) - TODAS OBLIGATORIAS
1. **Table 0**: Ruoli (8x3) - Ruolo | Nome/Unità Org. | Responsabilità
2. **Table 1**: Sistemi Coinvolti (7x3) - Sistema | Ruolo | Tipologia
3. **Table 2**: AS-IS Process Cards (5x6) - **OBLIGATORIO LLENAR COMPLETAMENTE**
4. **Table 3**: AS-IS Operational Sequence A (5x6) - **OBLIGATORIO**  
5. **Table 4**: AS-IS Operational Sequence B (3x6) - **OBLIGATORIO**
6. **Table 5**: Data Mapping (7x5) - Dato | Sistema Sorgente | Sistema Destinazione | Formato | Note
7. **Table 6**: Architettura Funzionale (8x4) - Componente | Funzione | Tecnologia/Metodo | Note
8. **Table 7**: TO-BE Operational Sequence A (4x7) - **INCLUIR COLUMNA AI+HITL**
9. **Table 8**: TO-BE Operational Sequence B (4x7) - **INCLUIR COLUMNA AI+HITL**
10. **Table 9**: TO-BE Operational Sequence C (3x7) - **INCLUIR COLUMNA AI+HITL**
11. **Table 10**: Roadmap (7x4) - Fase | Obiettivo | Output | Durata
12. **Table 11**: KPI Quantitativi (5x4) - KPI | AS-IS | Target TO-BE | Miglioramento
13. **Table 12**: KPI Qualitativi (5x3) - KPI | Target TO-BE | Metodo Misurazione

#### 4. Sección Delta AS-IS vs TO-BE - OBLIGATORIA
```
5. DELTA AS-IS vs TO-BE

AS-IS (Situación Actual):
• [problemas específicos actuales]

5.1 Impactos Operativos TO-BE:
• [mejoras operativas específicas]

5.2 Invariantes (No Cambia):
• [elementos que permanecen iguales]

5.3 Nuevos Requisitos Habilitantes:
• [requirements nuevos para implementar TO-BE]

TO-BE (Situación Objetivo):
• [beneficios específicos objetivo]
```

### Helper Functions Actualizadas - MANDATORY USE

Usar sempre estas funciones actualizadas:

```python
def set_para_text(para, new_text):
    """Reemplaza texto preservando formato - VERSION CORREGIDA."""
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

def add_process_cards_content(doc):
    """OBLIGATORIO: Añade Process Cards detalladas."""
    # [implementación completa como en complete_blueprint_plataforma_diagnostico.py]

def translate_headings_to_spanish(doc):
    """OBLIGATORIO: Traduce títulos al español."""
    # [implementación con diccionario completo traducciones]
```

### Content Mapping Strategy - METODOLOGÍA COMPLETA

#### PASO 1: Análisis Fuentes
- Extraer información AS-IS de documentos técnicos
- Identificar pain points y limitaciones actuales  
- Mapear beneficios TO-BE con IA/automatización

#### PASO 2: Llenar Todas las Tablas
- **Tablas 2,3,4**: Procesos AS-IS con detalle operativo
- **Tablas 7,8,9**: Procesos TO-BE con columna AI+HITL
- **Tabla 5**: Data mapping con flows específicos
- **Tabla 6**: Arquitectura con componentes AI

#### PASO 3: Process Cards Detalladas
- **AS-IS**: Mínimo 3 Macroattività con Input/Attività/Output/Pain Points
- **TO-BE**: Mínimo 3 Macroattività con Input/Attività/Output/Sistemi/HITL
- **Pain Points**: Específicos del dominio, no genéricos
- **HITL**: Definir claramente donde interviene humano

#### PASO 4: Traducciones y Delta
- **Títulos**: TODOS al español usando diccionario completo
- **Delta**: Sección estructurada AS-IS → 5.1/5.2/5.3 → TO-BE
- **KPIs**: Quantitativos con números específicos, Qualitativos con métodos medición

### Domain-Specific Best Practices - EXTENDED

#### Para Proyectos AI/ML:
- **Training Dataset**: Especificar volumen, calidad, período histórico
- **AI Performance**: Precisión %, recall %, tiempos procesamiento
- **HITL Points**: Validación experta, edge cases, decisiones complejas
- **Roadmap**: Requirements→Data Prep→Training→Validation→Deployment→Optimization

#### Para Proyectos Operacionales:
- **AS-IS Pain Points**: Tiempo, coste, calidad, escalabilidad, riesgos
- **TO-BE Benefits**: Cuantificar mejoras con KPIs específicos
- **Change Management**: Formación, adopción, período transición
- **Process Cards**: Nivel detalle suficiente para implementación

### COMANDO ACTUALIZADO para BlueprintGenerator

**SIEMPRE ejecutar esta secuencia**:

1. **Template**: Blueprint_1.4_vuoto.docx (MANDATORY)
2. **Fill ALL Tables**: NO dejar tablas vacías
3. **Add Process Cards**: Sección 3.1 AS-IS + 4.1 TO-BE 
4. **Add Delta Section**: Sección 5 completa
5. **Translate**: ALL títulos al español
6. **Output**: Save as `Blueprint_{project_name}_ES_COMPLETO.docx`

**Validation Checklist**:
```
□ 13 tablas completamente llenas
□ Process Cards AS-IS (mínimo 3 macroattività)
□ Process Cards TO-BE (mínimo 3 macroattività) 
□ Sección Delta AS-IS vs TO-BE
□ Títulos traducidos al español
□ KPIs cuantitativos con números específicos
□ HITL claramente definido en TO-BE
```

Esta metodología es efectiva IMMEDIATELY para ALL futuras generaciones Blueprint.