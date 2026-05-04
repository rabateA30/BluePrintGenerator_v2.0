# Blueprint – ES · GRIDS · Gestión de Reclamaciones (Claims) v2.0

> **Template base**: `Blueprint_Template_1.5_vacio-ES.docx`
> **Versión**: 2.0 — Integración CJX (Customer Journeys: Red · Contadores · Contratos · Interrupciones)
> **Idioma de salida**: Español
> **Última actualización**: mayo 2026

---

## Resumen Ejecutivo

| Campo | Contenido |
|---|---|
| **Procesos Identificados** | 1. Clasificación y Routing de Reclamaciones · 2. Gestión Operativa por Dominio (Red / Contadores / Contratos / Interrupciones) · 3. Cierre y Comunicación |
| **Contexto General** | El área GRIDS ES gestiona reclamaciones de clientes relativas a la red de distribución eléctrica en España. El volumen actual supera las 120.000 reclamaciones anuales, procesadas mayoritariamente de forma manual con routing basado en sólo tres rutas genéricas. Los Customer Journeys (CJ) incorporados en esta versión revelan sub-tipologías específicas por dominio que el modelo AS-IS no contempla. |
| **Objetivo de la Solución** | Ampliar el modelo de clasificación IA para cubrir todos los sub-tipos de reclamación identificados en los CJ; extender el routing de 3 a 8 rutas con lógica paramétrica; añadir ramificaciones de flujo específicas por dominio operativo; gestionar automáticamente las excepciones al cierre según las "Necesidades generales"; actualizar el mapa de integración de sistemas incluyendo WART y PUC; implementar templates de comunicación diferenciados por sub-tipo. |
| **Impacto Esperado** | Reducción del tiempo medio de resolución de reclamaciones en un 45 %; aumento de la tasa de cierre automático del 28 % al 65 %; reducción de escaladas manuales en un 50 %; mejora de la satisfacción del cliente (NPS +12 puntos). |

---

## Proceso 1 — Clasificación y Routing de Reclamaciones

### 1. Contexto y Finalidad

| Sección | Contenido |
|---|---|
| **1.1 Alcance** | Recepción multicanal de reclamaciones de red (IVR, portal web, app, oficina presencial, email), clasificación automática mediante IA en tipología y sub-tipo, routing inteligente al dominio operativo competente, y cierre con comunicación al cliente. El modelo de clasificación IA se extiende a todos los sub-tipos definidos en los CJ de Red, Contadores, Contratos e Interrupciones. |
| **1.2 Finalidad** | • Clasificar automáticamente el 100 % de las reclamaciones entrantes en tipología principal y sub-tipo específico · • Enrutar cada caso al dominio operativo correcto con información contextual completa · • Reducir el tiempo de primera respuesta a < 24 h · • Garantizar el tratamiento específico de casos que no pueden cerrarse automáticamente · • Proporcionar comunicaciones personalizadas por sub-tipo de reclamación |
| **1.3 Perímetro** | **EN ALCANCE**: Reclamaciones de suministro eléctrico (cortes, averías, calidad, contadores, contratos, interrupciones programadas/no programadas) · Canales: IVR, portal web, app móvil, email, atención presencial · Dominios: Red, Contadores, Contratos, Interrupciones · Gestión de excepciones y casos no cerrables automáticamente · Comunicaciones diferenciadas por sub-tipo **FUERA DE ALCANCE**: Reclamaciones tarifarias reguladas (CNMC directo) · Fraude eléctrico (acometida a proceso penal) · Reclamaciones de distribuidoras terceras · Consultas de facturación sin incidencia técnica |
| **1.4 Restricciones Clave** | **Normativas**: Real Decreto 1955/2000 (calidad suministro), Orden ETU/1282/2017 (interrupciones), Ley 24/2013 (sector eléctrico) · **Técnicas**: Integración obligatoria con SAP CRM, SAP IS-U, WART, PUC, GIS, SCADA, RECORE · **Organizativas**: SLA de resolución: 15 días hábiles (estándar), 5 días (corte de suministro) · **Datos**: Cumplimiento RGPD en tratamiento de datos de consumo y domicilio del cliente |

---

### Stakeholders y Participantes

**Tabla 0** (10×3) — Roles:

| Rol | Nombre / Unidad Organizativa | Responsabilidad |
|---|---|---|
| Business Owner | Gestión de Reclamaciones, GRIDS ES | Valida requisitos funcionales y aprueba el Blueprint |
| Data Owner | CRM & Analytics Team, GRIDS ES | Garantiza calidad y accesibilidad de los datos de reclamaciones |
| IT Owner | Arquitectura Digital, GICT Spain | Supervisa la arquitectura técnica e integración de sistemas |
| Product Owner | AISA Factory, Enel | Gestiona el backlog y coordina las iteraciones de desarrollo |
| Process Owner | Operaciones Red, GRIDS ES | Valida los flujos operativos por dominio (Red / Contadores / Contratos / Interrupciones) |
| Legal & Compliance | Asesoría Jurídica, Enel España | Garantiza cumplimiento normativo y gestión de casos con implicaciones legales |
| Customer Experience | CX Team, GRIDS ES | Valida templates de comunicación y experiencia de cliente |
| Integrations Lead | GICT Integrations, Spain | Gestiona las integraciones con WART, PUC, RECORE y sistemas legacy |
| Field Operations | Centro de Control, GRIDS ES | Responsable de la resolución técnica en campo (averías, cortes, instalaciones) |
| Regulatory Affairs | Departamento Regulatorio, Enel España | Gestiona relación con CNMC y coordinación de reportes regulatorios |

---

### 2. Proceso AS-IS — Descripción Estructurada

#### 2.1 Sistemas Involucrados (AS-IS)

**Tabla 1** (8×3):

| Herramienta AS-IS | Descripción / Rol | Tipología |
|---|---|---|
| SAP CRM | Sistema core de registro y seguimiento de reclamaciones | Core Platform |
| SAP IS-U | Gestión de contratos, tarifas y medición de consumo | Core Platform |
| WART (Work Assignment & Resolution Tool) | Asignación y seguimiento de órdenes de trabajo en campo | Integration Layer |
| PUC (Platform for Utilities & Contracts) | Gestión de accesos, contratos y puntos de suministro | Core Platform |
| GIS (Geographic Information System) | Topología de red e identificación de afectados | Integration Layer |
| SCADA | Supervisión y control en tiempo real de la red de distribución | External System |
| IVR / Plataforma Omnicanal | Entrada de reclamaciones por voz, web, app y email | Integration Layer |
| RECORE | Sistema de reconexión automática de suministro | External System |

---

#### 2.2 AS-IS — Secuencia Operativa

**Tabla 2** (6×6) — AS-IS Secuencia A: Recepción y Registro

| Paso | Actividad | Actor | Entrada | Salida | Sistemas |
|---|---|---|---|---|---|
| A1 | Recepción de reclamación por canal (IVR, web, app, presencial) | Cliente / Agente | Llamada / formulario web / email | Caso abierto en cola | IVR · Omnicanal |
| A2 | Identificación del cliente y punto de suministro (CUPS) | Agente / Sistema | NIF · Dirección · CUPS | Cliente validado · CUPS vinculado | SAP CRM · SAP IS-U |
| A3 | Categorización manual del tipo de reclamación (sólo 3 categorías genéricas) | Agente | Descripción verbal del problema | Categoría: Corte / Facturación / Otro | SAP CRM |
| A4 | Asignación a Ruta 1, 2 o 3 según categoría | Agente / Regla fija | Categoría asignada | Ruta de gestión asignada | SAP CRM |
| A5 | Apertura de expediente y envío de acuse de recibo genérico | Sistema | Datos del caso | Expediente SAP CRM · Email acuse al cliente | SAP CRM |

**Tabla 3** (5×6) — AS-IS Secuencia B: Gestión y Resolución

| Paso | Actividad | Actor | Entrada | Salida | Sistemas |
|---|---|---|---|---|---|
| B1 | Revisión del expediente por el equipo de gestión de ruta | Gestor | Expediente SAP CRM | Análisis manual del caso | SAP CRM |
| B2 | Consulta manual a sistemas auxiliares (GIS, SCADA, IS-U) para obtener contexto | Gestor | CUPS · Fecha del evento | Datos técnicos de la incidencia | GIS · SCADA · SAP IS-U |
| B3 | Escalada a campo o a especialista según criterio del gestor | Gestor | Análisis del caso | Orden de trabajo (si aplica) | WART · SAP CRM |
| B4 | Resolución y cierre manual del expediente | Gestor | Resultado técnico / respuesta | Expediente cerrado | SAP CRM |
| B5 | Comunicación al cliente con respuesta genérica | Gestor | Resolución | Email / SMS genérico al cliente | SAP CRM |

**Tabla 4** (5×6) — AS-IS Secuencia C: Excepciones y Re-procesos

| Paso | Actividad | Actor | Entrada | Salida | Sistemas |
|---|---|---|---|---|---|
| C1 | Detección de reclamación mal clasificada (routing erróneo) | Gestor receptor | Expediente recibido | Reclasificación manual | SAP CRM |
| C2 | Re-routing manual a la unidad correcta | Supervisor | Expediente reclasificado | Nuevo gestor asignado | SAP CRM |
| C3 | Duplicados y reclamaciones repetidas tratadas de forma independiente | Gestor | Nueva reclamación | Expediente duplicado (no vinculado al original) | SAP CRM |
| C4 | Casos con implicación legal gestionados sin protocolo específico | Gestor / Supervisor | Solicitud cliente / requerimiento externo | Derivación ad hoc a Asesoría | SAP CRM · Email |
| C5 | Cierre sin respaldo de acción técnica verificada | Gestor | Transcurso del plazo | Expediente cerrado sin evidencia | SAP CRM |

---

#### 2.3 Fichas de Proceso AS-IS

```
Ficha 1: Clasificación y Routing Genérico
Entrada: Reclamación entrante por cualquier canal
Actividades:
  1. El agente escucha/lee la descripción del cliente
  2. Selecciona manualmente una de 3 categorías disponibles (Corte / Facturación / Otro)
  3. El sistema asigna automáticamente la ruta correspondiente (Ruta 1, 2 o 3)
  4. Se genera acuse genérico sin información específica de gestión
Salida: Caso categorizado y asignado a ruta
Punto Crítico: Sólo 3 categorías no cubren la diversidad de sub-tipos reales (al menos 18 sub-tipos identificados en los CJ); hasta un 35 % de los casos se clasifican en "Otro" y requieren re-routing manual posterior

Ficha 2: Gestión de Incidencia de Red (Ruta 1 AS-IS)
Entrada: Reclamación de corte o avería de red
Actividades:
  1. El gestor consulta manualmente GIS para identificar la zona afectada
  2. Verifica en SCADA si hay incidencia activa registrada
  3. Si hay incidencia conocida, informa al cliente con respuesta estándar
  4. Si no hay incidencia en SCADA, crea orden de trabajo en WART manualmente
  5. Hace seguimiento telefónico con campo
Salida: Orden de trabajo creada en WART / Caso cerrado con información de incidencia
Punto Crítico: La consulta manual a GIS y SCADA no está integrada en el flujo de CRM; el gestor tarda entre 15 y 40 minutos en recopilar el contexto técnico necesario; no se detectan automáticamente los clientes afectados por la misma incidencia

Ficha 3: Gestión de Reclamación de Facturación/Contador (Ruta 2 AS-IS)
Entrada: Reclamación de error en factura o contador defectuoso
Actividades:
  1. El gestor accede manualmente a SAP IS-U para revisar el historial de consumo
  2. Verifica lectura del contador (manual o telemedida si disponible)
  3. Si detecta anomalía, abre proceso de verificación de contador (puede requerir visita técnica)
  4. Emite factura correctiva o acuerdo de pago si confirma el error
  5. Comunica al cliente por email con resultado
Salida: Corrección de factura / Verificación de contador / Cierre sin acción
Punto Crítico: El acceso a SAP IS-U y PUC se realiza en sesiones separadas sin traspaso automático del contexto del caso; los casos de autoconsumo no tienen flujo específico y se gestionan como "Otro"
```

---

#### 2.4 Puntos Críticos Principales (AS-IS)

```
Puntos Críticos Generales:
• Modelo de clasificación insuficiente: sólo 3 categorías para más de 18 sub-tipos reales de reclamación identificados en los CJ, provocando un 35 % de re-routing y una pérdida media de 2,3 días de gestión
• Routing estático sin lógica paramétrica: las Rutas 1/2/3 no tienen en cuenta factores como zona geográfica, tipo de cliente, historial, sistemas afectados ni urgencia del caso
• Ausencia de detección automática de clientes coafectados: los cortes masivos generan decenas de expedientes independientes que no se agrupan, multiplicando el trabajo del gestor
• Falta de integración en tiempo real entre SAP CRM y los sistemas técnicos (GIS, SCADA, WART, PUC): el gestor debe navegar manualmente entre 4-6 aplicaciones por caso
• Gestión de excepciones al cierre no estructurada: no existen estados intermedios formalizados (suspensión pendiente verificación técnica, pendiente documentación cliente, etc.); los casos se mantienen abiertos sin criterio claro
• Ausencia de templates de comunicación diferenciados: se usa un único email genérico para todos los tipos de reclamación, con impacto negativo en la satisfacción del cliente y en el cumplimiento de los requisitos regulatorios de información
• Sistemas WART y PUC no contemplados en el flujo CRM: las órdenes de trabajo y la gestión contractual se gestionan fuera del expediente de reclamación, sin trazabilidad integrada
```

---

### 3. Proceso TO-BE

#### 3.1 Arquitectura Funcional IA

**Tabla 5** (7×5):

| Componente | Función | Tecnología / Método | Agente Común | Nota |
|---|---|---|---|---|
| Motor de Clasificación IA (extendido) | Clasificación multiclase de reclamaciones en tipología principal + sub-tipo específico por dominio CJ | NLP multiclase · Modelo fine-tuned sobre corpus histórico de reclamaciones GRIDS ES · Confianza por umbral | BluePrintGenerator Agent | Cubre 18 sub-tipos identificados en los CJ de Red, Contadores, Contratos e Interrupciones |
| Motor de Routing Paramétrico | Enrutamiento inteligente a una de 8 rutas según sub-tipo, zona, urgencia, historial y sistemas afectados | Motor de reglas + scoring paramétrico · Tablas de routing configurables | BluePrintGenerator Agent | Sustituye las Rutas 1/2/3 estáticas; parámetros editables sin redeploy |
| Módulo de Contexto Técnico Enriquecido | Recuperación automática de información técnica de GIS, SCADA y WART al crear el expediente | API REST · Integración en tiempo real · Cache TTL=5 min | Integraciones GICT | Elimina la consulta manual del gestor a sistemas auxiliares |
| Módulo de Agrupación de Casos Masivos | Detección y agrupación de reclamaciones correspondientes a la misma incidencia de red | Clusterización geoespacial (GIS) + correlación temporal | BluePrintGenerator Agent | Reduce duplicados; genera un único expediente maestro por incidencia |
| Gestor de Excepciones al Cierre | Identificación de casos no cerrables automáticamente y gestión de estados intermedios de suspensión | Motor de reglas de cierre · Catálogo de excepciones · Workflow de suspensión | BluePrintGenerator Agent | Implementa "Necesidades generales" — ver sección 3.5 |
| Motor de Comunicación Diferenciada | Generación y envío de comunicaciones personalizadas por sub-tipo de reclamación | Templates LLM-augmented · Selección por sub-tipo · Multicanal (email, SMS, app, carta) | BluePrintGenerator Agent | 14 templates diferenciados — ver módulo "Cierre y Comunicación" |
| Panel de Monitorización y Alertas | Dashboard en tiempo real de KPIs de reclamaciones, alertas de SLA en riesgo, y trazabilidad de integraciones | Power BI Embedded · Alertas Microsoft Teams | GICT Integrations | — |

---

#### 3.2 Mapeo de Datos — Sistemas TO-BE (AI-ENABLED)

**Tabla 6** (3×5):

| Dato | Sistema Origen | Sistema Destino | Formato | Nota |
|---|---|---|---|---|
| Expediente de reclamación enriquecido (CUPS + sub-tipo IA + contexto técnico) | SAP CRM + GIS + SCADA + WART | Motor de Routing Paramétrico | JSON estructurado | Creado en tiempo real al registrar la reclamación |
| Estado de orden de trabajo en campo | WART | SAP CRM · Portal Cliente | Webhook REST | Actualización automática del expediente al cambiar estado en WART |

---

#### 3.2b Secuencia Operativa Detallada (TO-BE)

**Tabla 7** (7×7) — TO-BE Subproceso A: Recepción, Clasificación y Routing

| Paso | Actividad | Actor | Entrada | Salida | Sistemas | IA + Intervención Humana |
|---|---|---|---|---|---|---|
| A1 | Recepción omnicanal y extracción de información | Sistema | Llamada / formulario / email / chat | Texto estructurado del caso | IVR · Omnicanal · NLP | **IA**: Extracción automática de entidades (CUPS, fecha, descripción del problema) · **HITL**: Agente corrige si IVR no reconoce el CUPS |
| A2 | Identificación y validación del cliente | Sistema | NIF · CUPS · Dirección | Cliente validado · Datos contractuales | SAP CRM · SAP IS-U · PUC | **IA**: Validación automática con SAP IS-U y PUC · **HITL**: Intervención si hay ambigüedad en la identidad (< 2 % de casos) |
| A3 | Clasificación IA extendida: tipología + sub-tipo | Motor IA | Texto del caso · Contexto cliente | Tipología principal + sub-tipo CJ + score de confianza | Motor Clasificación IA | **IA**: Clasificación automática en 18 sub-tipos (ver Tabla Paramétrica de Sub-tipos) · **HITL**: Revisión humana si score < 0,75 |
| A4 | Recuperación de contexto técnico enriquecido | Sistema | CUPS · Sub-tipo clasificado | Datos GIS (zona, afectados) · Estado SCADA · Historial WART · Datos PUC | GIS · SCADA · WART · PUC | **IA**: Recuperación automática y enriquecimiento del expediente · **HITL**: ninguna |
| A5 | Detección de agrupación: ¿incidencia masiva? | Motor IA | Datos GIS · Reclamaciones recientes | Caso individual / Caso agrupado a incidencia maestra | Motor Agrupación | **IA**: Clusterización geoespacial automática · **HITL**: Supervisor valida agrupaciones con > 50 afectados |
| A6 | Routing paramétrico a una de las 8 rutas | Motor Routing | Sub-tipo + contexto técnico + parámetros | Ruta asignada + unidad operativa receptora + SLA calculado | Motor Routing Paramétrico | **IA**: Selección automática de ruta según tabla paramétrica · **HITL**: Override manual disponible para supervisores |
| A7 | Apertura de expediente y comunicación de acuse personalizado | Sistema | Ruta asignada · Sub-tipo · Datos cliente | Expediente SAP CRM · Acuse personalizado por sub-tipo | SAP CRM · Motor Comunicación | **IA**: Generación automática del acuse con template específico del sub-tipo · **HITL**: ninguna |

**Tabla 8** (4×7) — TO-BE Subproceso B: Gestión Operativa por Dominio

| Paso | Actividad | Actor | Entrada | Salida | Sistemas | IA + Intervención Humana |
|---|---|---|---|---|---|---|
| B1 | Recepción del expediente enriquecido por el dominio competente (Red / Contadores / Contratos / Interrupciones) | Gestor de dominio | Expediente SAP CRM con contexto técnico completo | Caso asignado con toda la información disponible | SAP CRM | **IA**: El gestor recibe el expediente pre-analizado · **HITL**: El gestor revisa y confirma el contexto |
| B2 | Aplicación de la lógica de flujo específica del dominio (ver ramificaciones de flujo por dominio — sección 3.6) | Gestor / Sistema | Sub-tipo + datos técnicos | Acciones específicas por dominio (creación OT en WART, verificación IS-U, revisión PUC, etc.) | WART · SAP IS-U · PUC · SCADA | **IA**: Propuesta de acciones automáticas según sub-tipo · **HITL**: El gestor aprueba o modifica las acciones propuestas |
| B3 | Verificación del criterio de cierre (¿es cerrable automáticamente?) | Motor Excepciones | Resultado acciones + criterios "Necesidades generales" | Caso cerrable / Caso con excepción → estado intermedio de suspensión | Motor Excepciones al Cierre | **IA**: Evaluación automática contra catálogo de excepciones · **HITL**: Supervisor decide en casos límite |
| B4 | Cierre y generación de comunicación diferenciada, o activación de estado de suspensión con comunicación de seguimiento | Sistema / Gestor | Resultado resolución / Estado suspensión | Expediente cerrado + comunicación final · o Expediente en suspensión + comunicación de seguimiento | SAP CRM · Motor Comunicación | **IA**: Generación automática del template de cierre o suspensión por sub-tipo · **HITL**: Revisión obligatoria antes del envío para sub-tipos con implicaciones legales o compensaciones |

**Tabla 9** (4×7) — TO-BE Subproceso C: Escalación y Casos Especiales

| Paso | Actividad | Actor | Entrada | Salida | Sistemas | IA + Intervención Humana |
|---|---|---|---|---|---|---|
| C1 | Detección de necesidad de escalación a operador humano (ver criterios sección 3.5.2) | Motor IA / Monitor SLA | Estado del caso · Score IA · Historial cliente · Umbrales SLA | Flag de escalación + motivo | Motor Excepciones · SAP CRM | **IA**: Detección automática de cualquiera de los 6 criterios de escalación · **HITL**: Supervisor recibe alerta en Teams con contexto completo |
| C2 | Gestión humana del caso escalado con acceso a toda la trazabilidad | Supervisor / Especialista | Expediente completo + motivo escalación | Resolución supervisada | SAP CRM · WART · PUC · GIS | **IA**: asistencia IA para síntesis del historial · **HITL**: Decisión final siempre humana en casos escalados |
| C3 | Gestión de casos con demanda regulatoria (CNMC) o implicaciones legales | Gestor Regulatorio / Asesoría Jurídica | Requerimiento externo + expediente | Respuesta regulatoria / Acción legal | SAP CRM · Herramientas legales | **IA**: ninguna en la decisión regulatoria · **HITL**: 100 % humano; IA sólo proporciona el resumen del expediente |
| C4 | Revisión periódica de casos en estados intermedios de suspensión | Sistema / Gestor | Lista casos en suspensión + fecha de expiración | Renovación de suspensión o activación de resolución | SAP CRM · Motor Excepciones | **IA**: Alerta automática 48 h antes de vencer el plazo de suspensión · **HITL**: El gestor decide renovar, cerrar o escalar |

---

#### 3.3 Fichas de Proceso TO-BE

```
Ficha 1 TO-BE: Clasificación IA Extendida con Sub-tipos CJ
Entrada:
  • Texto libre de reclamación (IVR transcrito / formulario web / email)
  • Datos del cliente identificado (CUPS, contrato, historial)
Actividades:
  1. El Motor de Clasificación IA analiza el texto mediante NLP multiclase
  2. Asigna tipología principal: Red / Contador / Contrato / Interrupción / Daños / Autoconsumo
  3. Asigna sub-tipo específico del CJ correspondiente (ver Tabla Paramétrica de Sub-tipos y Routing)
  4. Calcula score de confianza; si < 0,75, activa revisión humana
  5. El expediente se enriquece automáticamente con contexto técnico (GIS + SCADA + WART + PUC)
Salida:
  • Expediente clasificado con tipología + sub-tipo + score de confianza + contexto técnico
Punto Crítico TO-BE: Mantener el modelo actualizado con nuevos sub-tipos; proceso de retraining trimestral requerido

Ficha 2 TO-BE: Routing Paramétrico a 8 Rutas
Entrada:
  • Expediente clasificado con sub-tipo + contexto técnico
  • Parámetros de routing (configurados en tabla paramétrica editable)
Actividades:
  1. El Motor de Routing evalúa el sub-tipo contra la tabla paramétrica de routing
  2. Aplica factores secundarios: urgencia (corte activo sí/no), zona geográfica, tipo de cliente (vulnerable/estándar), historial (reclamaciones previas)
  3. Selecciona la ruta óptima entre las 8 disponibles
  4. Calcula el SLA aplicable según la ruta y el sub-tipo
  5. Asigna el expediente a la unidad operativa receptora con toda la información de contexto
Salida:
  • Expediente asignado a ruta y unidad operativa + SLA calculado + acuse personalizado enviado al cliente
Punto Crítico TO-BE: Los parámetros de la tabla de routing deben revisarse trimestralmente con los Process Owners de cada dominio

Ficha 3 TO-BE: Gestión de Excepciones al Cierre
Entrada:
  • Expediente con resolución técnica disponible
  • Resultado de acciones del dominio
Actividades:
  1. El Motor de Excepciones evalúa el caso contra el catálogo de excepciones al cierre
  2. Si el caso no es cerrable automáticamente, asigna el estado intermedio de suspensión correspondiente
  3. Genera comunicación de suspensión personalizada por sub-tipo
  4. Programa revisión automática al vencer el plazo de suspensión
  5. Si el caso es cerrable, genera el template de cierre específico del sub-tipo y lo envía
Salida:
  • Expediente cerrado con comunicación diferenciada · o Expediente en estado de suspensión con comunicación de seguimiento y revisión programada
```

---

#### 3.4 Qué NO hace la IA

```
• No toma decisiones sobre indemnizaciones o compensaciones económicas — requiere validación humana y criterio jurídico
• No gestiona directamente los expedientes con requerimiento formal de CNMC o tribunal — todo el proceso regulatorio/legal es 100 % humano
• No cierra automáticamente casos con score de confianza de clasificación < 0,75 — requiere revisión del gestor
• No aprueba de forma autónoma órdenes de trabajo en campo con impacto en más de 100 clientes — requiere validación del supervisor de Red
• No modifica contratos ni tarifas directamente en SAP IS-U o PUC — el gestor humano ejecuta la acción tras la propuesta de la IA
• No toma decisiones sobre la vulnerabilidad del cliente (activación de protocolos de clientes vulnerables) — requiere validación humana
```

---

### 3.5 Excepciones al Cierre — "Necesidades Generales"

#### 3.5.1 Casos No Cerrables Automáticamente

Los siguientes casos **no pueden cerrarse de forma automática** y requieren intervención humana antes del cierre definitivo:

| Código Excepción | Descripción del Caso | Motivo | Acción Requerida |
|---|---|---|---|
| EXC-01 | Reclamación con daños a terceros o bienes del cliente | Implicaciones legales / seguro | Derivación a Asesoría Jurídica + peritaje antes de cierre |
| EXC-02 | Reclamación con requerimiento formal de CNMC | Obligación regulatoria | Gestión regulatoria completa antes de cierre; plazo CNMC prevalece |
| EXC-03 | Corte de suministro de larga duración (> 24 h continuas) | Obligación de informe técnico + posible compensación automática RD 1955/2000 | Informe técnico validado por Field Operations + cálculo de compensación |
| EXC-04 | Disputa de medición activa (contador en auditoría) | No es posible determinar la resolución correcta hasta el resultado de la auditoría | Esperar resultado de auditoría de contador antes de cerrar |
| EXC-05 | Cliente en colectivo vulnerable (código en SAP IS-U) | Obligación de protocolo especial de atención | Revisión por el gestor especialista en clientes vulnerables antes de cierre |
| EXC-06 | Reclamación repetida sobre la misma incidencia (≥ 3 reclamaciones del mismo CUPS en 30 días) | Patrón de problema no resuelto | Escalación a supervisor + investigación de causa raíz antes de cierre |
| EXC-07 | Caso con intervención judicial o expediente sancionador activo | Riesgo legal | Coordinación obligatoria con Asesoría Jurídica; no cerrar hasta resolución judicial |
| EXC-08 | Incidencia masiva activa (> 50 clientes afectados misma zona) | Gestión centralizada por Centro de Control | El cierre individual se bloquea hasta que el Centro de Control cierre la incidencia maestra |

---

#### 3.5.2 Criterios de Escalación a Operador Humano

La IA activa la escalación automática a un operador humano si se cumple **al menos uno** de los siguientes criterios:

| Criterio | Umbral / Condición | Motivo |
|---|---|---|
| Score de confianza IA bajo | Score clasificación < 0,75 | La IA no tiene suficiente certeza sobre el sub-tipo; riesgo de routing incorrecto |
| Historial de reclamaciones elevado | ≥ 3 reclamaciones del mismo CUPS en los últimos 12 meses | Cliente con problema crónico no resuelto; requiere análisis de causa raíz |
| Daño económico declarado alto | Importe declarado por el cliente > 1.000 € | Riesgo económico y reputacional; requiere validación humana |
| Incidencia masiva en zona | > 10 reclamaciones en la misma zona geográfica en < 2 h | Posible evento de red no registrado en SCADA |
| Sub-tipo EXC-01 a EXC-08 detectado | Cualquier excepción al cierre activada | Ver tabla de excepciones sección 3.5.1 |
| SLA en riesgo crítico | < 20 % del tiempo SLA restante y caso aún sin resolución | Prevención de incumplimiento de SLA regulatorio |

---

#### 3.5.3 Estados Intermedios de Suspensión

Los expedientes que no pueden avanzar a resolución ni cerrarse se gestionan mediante los siguientes **estados intermedios de suspensión**:

| Código Estado | Nombre Estado | Descripción | Plazo Máximo | Condición de Salida |
|---|---|---|---|---|
| SUS-01 | Pendiente Verificación Técnica | El caso requiere visita o inspección técnica en campo antes de poder resolverse | 15 días hábiles | Resultado de inspección recibido en WART |
| SUS-02 | Pendiente Documentación Cliente | El cliente debe aportar documentación adicional (denuncia, presupuesto daños, etc.) | 10 días hábiles | Documentación recibida y validada |
| SUS-03 | Pendiente Resolución CNMC | El caso está sujeto a revisión o resolución por parte de la CNMC | Sin plazo propio (plazo CNMC) | Recepción de resolución CNMC |
| SUS-04 | Pendiente Resultado Auditoría Contador | La medición del contador está siendo auditada en laboratorio o en campo | 20 días hábiles | Resultado de auditoría disponible en SAP IS-U / PUC |
| SUS-05 | En Revisión Legal | El caso está siendo revisado por Asesoría Jurídica (daños, demandas, expedientes sancionadores) | 30 días hábiles | Informe legal emitido |
| SUS-06 | Agrupado a Incidencia Maestra | El expediente individual está vinculado a una incidencia masiva activa gestionada por Centro de Control | Duración de la incidencia maestra | Cierre de la incidencia maestra en WART |

> **Comportamiento del sistema en suspensión**: El Motor de Excepciones genera automáticamente una comunicación de seguimiento al cliente informando del estado de suspensión y el motivo. Se programa una alerta automática 48 h antes de vencer el plazo máximo de cada estado. Si el plazo expira sin condición de salida, el caso se escala al supervisor responsable.

---

### 3.6 Ramificaciones de Flujo por Dominio Operativo

#### CJ RED — Flujo Específico (Cortes, Averías, Calidad de Suministro, Acometidas)

```
[Entrada: sub-tipos Red]
  ↓
¿Corte de suministro activo en CUPS?
  SÍ → ¿Corte asociado a incidencia conocida en SCADA?
        SÍ → Agrupación a incidencia maestra + comunicación con ETA de reposición
        NO → Ruta 2 (WART orden urgente) + detección de nuevo evento en SCADA
  NO → ¿Sub-tipo = Baja Tensión?
        SÍ → Consulta medición GIS (niveles de tensión zona) → Ruta 2 con prioridad media
       ¿Sub-tipo = Daños por Falta de Calidad?
        SÍ → Activar EXC-01 (posibles daños) + Ruta 7 (Gestión Siniestros)
       ¿Sub-tipo = Instalación Defectuosa / Acometida?
        SÍ → Verificar titularidad (red pública vs instalación privada en PUC)
             Red pública → Ruta 2 (WART)
             Instalación privada → Ruta 4 (Contratos/PUC + indicación al cliente)
```

#### CJ CONTADORES — Flujo Específico (Contador Defectuoso, Error Facturación, Autoconsumo, TUP/Telemedida)

```
[Entrada: sub-tipos Contadores]
  ↓
¿Sub-tipo = Contador Defectuoso?
  SÍ → Verificar lecturas históricas en SAP IS-U
        Anomalía confirmada → Activar SUS-04 (auditoría contador) + Ruta 3
        Sin anomalía → Información al cliente + cierre
¿Sub-tipo = Error Facturación por Contador?
  SÍ → Comparar lecturas reales vs facturadas en SAP IS-U
        Discrepancia > umbral → Regularización automática + comunicación Template CONTADOR
        Sin discrepancia → Explicación de factura + cierre
¿Sub-tipo = Autoconsumo (Medición / Compensación)?
  SÍ → Consultar configuración en Portal Autoconsumo + PUC
        Ruta 7 (Autoconsumo/Renovables) + especialista autoconsumo
¿Sub-tipo = TUP / Telemedida?
  SÍ → Verificar conectividad del contador inteligente en sistema telemedida
        Sin comunicación → Orden de verificación en WART + SUS-01
        Con comunicación → Revisión de datos en SAP IS-U
```

#### CJ CONTRATOS — Flujo Específico (Modificación, Cambio Titular, Alta/Baja, Conexión Ilegal)

```
[Entrada: sub-tipos Contratos]
  ↓
¿Sub-tipo = Modificación de Contrato (potencia, tarifa)?
  SÍ → Verificar viabilidad técnica en PUC (potencia disponible, instalación)
        Viable → Tramitación en PUC + SAP IS-U + comunicación Template CONTRATO
        No viable → Explicación técnica al cliente + alternativas
¿Sub-tipo = Cambio de Titular?
  SÍ → Verificar documentación en PUC
        Completa → Tramitación automática en PUC + SAP IS-U
        Incompleta → Activar SUS-02 (pendiente documentación cliente)
¿Sub-tipo = Alta/Baja de Suministro?
  SÍ → Ruta 4 (PUC + SAP CRM) + verificación técnica red disponible
¿Sub-tipo = Enganche/Conexión Ilegal sospechada?
  SÍ → Activar EXC-07 (implicaciones legales) + derivación a Asesoría + Inspección WART
```

#### CJ INTERRUPCIONES — Flujo Específico (Programada, No Programada, Larga Duración, RECORE)

```
[Entrada: sub-tipos Interrupciones]
  ↓
¿Sub-tipo = Interrupción Programada?
  SÍ → Verificar aviso previo enviado en SCADA/GIS (72 h antes por normativa)
        Aviso enviado → Información al cliente + cierre con Template INTERRUPCIÓN PROGRAMADA
        Aviso NO enviado → Activar EXC-02 potencial (incumplimiento normativo) + revisión proceso
¿Sub-tipo = Interrupción No Programada?
  SÍ → Consultar incidencia en SCADA + RECORE
        RECORE actuó (reconexión automática realizada) → Confirmar reconexión + comunicación
        RECORE no actuó / fallo → Ruta 5 (WART urgente + SCADA) + comunicación inmediata
¿Sub-tipo = Larga Duración (> 24 h)?
  SÍ → Activar EXC-03 (informe técnico obligatorio + cálculo compensación)
        Activar SUS-01 (pendiente verificación técnica)
        Notificar Centro de Control
        Calcular compensación según RD 1955/2000
¿Sub-tipo = Fallo RECORE / Reconexión Automática?
  SÍ → Verificar estado RECORE en SCADA
        Fallo técnico RECORE → Ruta 2 (WART mantenimiento RECORE) + escalación técnica
        Fallo de datos → Verificar telemetría + SUS-01
```

---

### 3.7 Tabla Paramétrica de Sub-tipos y Routing

Esta tabla define el **mapping completo** entre sub-tipo de reclamación (identificado por el Motor de Clasificación IA) y la ruta de gestión correspondiente. Los parámetros son **editables por los Process Owners** sin necesidad de redeploy del sistema.

| Dominio CJ | Sub-tipo | Código Sub-tipo | Ruta Asignada | Sistemas Clave | SLA (días hábiles) | EXC Posible | Template Comunicación |
|---|---|---|---|---|---|---|---|
| Red | Corte de suministro activo | RED-01 | Ruta 2 | WART · GIS · SCADA | 1 | EXC-08 | TPL-CORTE |
| Red | Baja tensión / Calidad deficiente | RED-02 | Ruta 2 | WART · GIS · SCADA | 5 | — | TPL-AVERÍA |
| Red | Daños a bienes del cliente por falta de calidad | RED-03 | Ruta 7 | SAP CRM · WART | 10 | EXC-01 | TPL-DAÑOS |
| Red | Instalación defectuosa / Acometida | RED-04 | Ruta 2 / Ruta 4 | WART · PUC | 10 | — | TPL-AVERÍA |
| Red | Extensión o nueva acometida de red | RED-05 | Ruta 4 | PUC · WART | 15 | — | TPL-CONTRATO |
| Contadores | Contador defectuoso (lectura anómala) | CNT-01 | Ruta 3 | SAP IS-U · PUC | 10 | SUS-04 | TPL-CONTADOR |
| Contadores | Error de facturación por lectura incorrecta | CNT-02 | Ruta 3 | SAP IS-U | 5 | — | TPL-CONTADOR |
| Contadores | Autoconsumo — error en medición/compensación | CNT-03 | Ruta 7 | PUC · Portal Autoconsumo · SAP IS-U | 10 | — | TPL-AUTOCONSUMO |
| Contadores | TUP / Telemedida — fallo de comunicación | CNT-04 | Ruta 3 | SAP IS-U · WART | 5 | SUS-01 | TPL-CONTADOR |
| Contratos | Modificación de contrato (potencia/tarifa) | CTR-01 | Ruta 4 | PUC · SAP IS-U | 5 | — | TPL-CONTRATO |
| Contratos | Cambio de titular | CTR-02 | Ruta 4 | PUC · SAP CRM | 5 | SUS-02 | TPL-CONTRATO |
| Contratos | Alta / Baja de suministro | CTR-03 | Ruta 4 | PUC · SAP IS-U | 10 | — | TPL-CONTRATO |
| Contratos | Enganche ilegal / Conexión no autorizada | CTR-04 | Ruta 8 | SAP CRM · WART | N/A | EXC-07 | TPL-LEGAL |
| Interrupciones | Interrupción programada | INT-01 | Ruta 5 | WART · SCADA | 5 | EXC-02 potencial | TPL-INT-PROG |
| Interrupciones | Interrupción no programada | INT-02 | Ruta 5 | WART · SCADA · RECORE | 2 | EXC-08 | TPL-INT-NOPROG |
| Interrupciones | Larga duración (> 24 h) | INT-03 | Ruta 6 | WART · SCADA · RECORE | 1 (urgente) | EXC-03 | TPL-INT-LARGA |
| Interrupciones | Fallo RECORE / Reconexión automática | INT-04 | Ruta 6 | WART · SCADA · RECORE | 2 | — | TPL-INT-NOPROG |
| Daños / Legal | Daños a terceros / infraestructura | DAÑ-01 | Ruta 7 | SAP CRM · WART | 15 | EXC-01 · EXC-07 | TPL-DAÑOS |

---

### 3.8 Mapa Actualizado de Integración de Sistemas

> **Versión**: TO-BE v2.0 — incluye WART, PUC, RECORE y Portal Autoconsumo identificados en los CJ

| Sistema | Tipología | Rol en el Proceso TO-BE | Protocolo de Integración | Nuevo / Existente |
|---|---|---|---|---|
| SAP CRM | Core Platform | Registro maestro de expedientes; tracking completo del ciclo de vida de la reclamación | API REST (OData) | Existente |
| SAP IS-U | Core Platform | Consulta y modificación de contratos, tarifas, lecturas y facturación | RFC / API REST | Existente |
| WART (Work Assignment & Resolution Tool) | Integration Layer | Creación, asignación y seguimiento de órdenes de trabajo en campo; integración de resultados de inspección en el expediente CRM | API REST (webhook) | **Nuevo en BP v2.0** |
| PUC (Platform for Utilities & Contracts) | Core Platform | Gestión de puntos de suministro, accesos contractuales, autoconsumo, potencias; verificación de titularidad | API REST | **Nuevo en BP v2.0** |
| GIS (Geographic Information System) | Integration Layer | Topología de red; identificación de clientes afectados por zona; soporte a clusterización de incidencias masivas | WFS / REST GeoServices | Existente |
| SCADA | External System | Supervisión en tiempo real del estado de la red; detección de incidencias activas; confirmación de reconexiones | SOAP / REST (sólo lectura) | Existente |
| RECORE | External System | Sistema de reconexión automática de suministro; verificación del estado de reconexión para sub-tipos INT-02 / INT-04 | API REST (sólo lectura) | **Nuevo en BP v2.0** |
| IVR / Plataforma Omnicanal | Integration Layer | Canal de entrada multicanal (IVR, web, app, email, presencial); entrega del texto de reclamación al Motor de Clasificación IA | Webhook / REST | Existente |
| Portal Autoconsumo | External System | Gestión de configuración y medición de instalaciones de autoconsumo; verificado para sub-tipo CNT-03 | API REST | **Nuevo en BP v2.0** |
| SAP PM (Plant Maintenance) | Integration Layer | Gestión de mantenimiento de activos de red; integración con WART para órdenes de mantenimiento preventivo/correctivo | RFC / API | Existente |
| Motor de Clasificación IA | AI Component | Clasificación multiclase de reclamaciones en 18 sub-tipos; integración con todos los sistemas de contexto | Servicio interno | **Nuevo en BP v2.0** |
| Motor de Routing Paramétrico | AI Component | Selección de ruta óptima entre 8 disponibles; parámetros configurables por Process Owner | Servicio interno | **Nuevo en BP v2.0** |
| Motor de Comunicación Diferenciada | AI Component | Generación de templates personalizados por sub-tipo; envío multicanal | Servicio interno + SMTP/SMS | **Nuevo en BP v2.0** |

---

### 3.9 Módulo "Cierre y Comunicación" — Templates Diferenciados por Sub-tipo

#### Estructura del Módulo

El módulo de Cierre y Comunicación gestiona el ciclo de vida de las comunicaciones al cliente desde el acuse hasta el cierre definitivo. Cada sub-tipo de reclamación dispone de un conjunto de templates específicos activados según el estado del expediente.

#### Catálogo de Templates de Comunicación

| Código Template | Nombre | Activación | Contenido Diferenciado |
|---|---|---|---|
| TPL-CORTE-ACK | Acuse — Corte de Suministro | Al registrar reclamación RED-01 | Número de expediente · CUPS · ETA estimada de reposición si disponible en SCADA · Contacto emergencias 24h |
| TPL-CORTE-RES | Resolución — Corte de Suministro | Al cerrar RED-01 | Confirmación de reposición · Duración total del corte · Compensación automática si > umbral RD 1955/2000 · Informe técnico adjunto si INT-03 |
| TPL-AVERÍA-ACK | Acuse — Avería / Baja Tensión | Al registrar RED-02 / RED-04 | Número de expediente · Equipo asignado en WART · SLA aplicable |
| TPL-AVERÍA-RES | Resolución — Avería Técnica | Al cerrar RED-02 / RED-04 | Descripción de la acción técnica realizada · Confirmación de normalización |
| TPL-DAÑOS-ACK | Acuse — Daños a Bienes del Cliente | Al registrar RED-03 / DAÑ-01 | Número de expediente · Proceso de peritaje activado · Documentación requerida al cliente · Plazos |
| TPL-DAÑOS-RES | Resolución — Daños (con/sin indemnización) | Al cerrar RED-03 / DAÑ-01 | Resultado del peritaje · Importe de indemnización (si aplica) · Instrucciones de pago |
| TPL-CONTADOR-ACK | Acuse — Reclamación de Contador | Al registrar CNT-01 / CNT-02 / CNT-04 | Número de expediente · Tipo de verificación activada · Plazo estimado |
| TPL-CONTADOR-RES | Resolución — Contador / Facturación | Al cerrar CNT-01 / CNT-02 | Resultado de la verificación · Regularización de facturación (si aplica) · Importe de la diferencia |
| TPL-AUTOCONSUMO-ACK | Acuse — Autoconsumo | Al registrar CNT-03 | Número de expediente · Especialista autoconsumo asignado · Datos del punto de autoconsumo |
| TPL-AUTOCONSUMO-RES | Resolución — Autoconsumo | Al cerrar CNT-03 | Resultado de la verificación de medición/compensación · Corrección aplicada |
| TPL-CONTRATO-ACK | Acuse — Reclamación Contractual | Al registrar CTR-01 / CTR-02 / CTR-03 | Número de expediente · Documentación requerida (si SUS-02) · Plazo de gestión |
| TPL-CONTRATO-RES | Resolución — Gestión Contractual | Al cerrar CTR-01 / CTR-02 / CTR-03 | Confirmación del cambio realizado · Nuevas condiciones del contrato · Fecha de efecto |
| TPL-INT-PROG-ACK | Acuse — Interrupción Programada | Al registrar INT-01 | Número de expediente · Información sobre el aviso previo emitido · Duración planificada |
| TPL-INT-PROG-RES | Resolución — Interrupción Programada | Al cerrar INT-01 | Confirmación de gestión · Información sobre el aviso y la normativa aplicable |
| TPL-INT-NOPROG-ACK | Acuse — Interrupción No Programada | Al registrar INT-02 / INT-04 | Número de expediente · Estado de RECORE · ETA de resolución si disponible |
| TPL-INT-NOPROG-RES | Resolución — Interrupción No Programada | Al cerrar INT-02 / INT-04 | Causa de la interrupción · Acciones realizadas · Compensación si aplica |
| TPL-INT-LARGA-ACK | Acuse — Interrupción Larga Duración | Al registrar INT-03 | Número de expediente · Equipo de crisis activado · Actualizaciones periódicas comprometidas |
| TPL-INT-LARGA-RES | Resolución — Interrupción Larga Duración | Al cerrar INT-03 | Informe técnico completo · Compensación calculada según RD 1955/2000 · Medidas preventivas |
| TPL-SUS-ACK | Comunicación — Estado de Suspensión | Al activar cualquier estado SUS-01 a SUS-06 | Motivo de la suspensión · Plazo estimado de resolución · Acción requerida (si SUS-02: documentación) · Canal de contacto para seguimiento |
| TPL-LEGAL-ACK | Acuse — Caso con Implicaciones Legales | Al registrar CTR-04 / EXC-07 | Número de expediente · Información sobre el proceso activado · Contacto de referencia en Asesoría Jurídica |

---

### 4. Delta AS-IS vs TO-BE

#### 4.1 Impactos Operativos

```
• Reducción del tiempo medio de clasificación de reclamaciones de 8 minutos (manual) a < 30 segundos (IA automática), con el 78 % de los casos clasificados con score de confianza ≥ 0,75
• Eliminación del re-routing manual: la tasa de re-clasificación disminuye del 35 % al 8 % gracias a los 18 sub-tipos del modelo extendido
• Reducción del tiempo de recopilación de contexto técnico por parte del gestor de 15-40 minutos a 0 minutos (recuperación automática de GIS, SCADA, WART, PUC)
• Reducción del volumen de expedientes duplicados por incidencias masivas en un 70 % gracias al módulo de agrupación geoespacial
• Tasa de cierre automático aumentada del 28 % al 65 % para casos estándar; el 35 % restante corresponde a excepciones gestionadas con estados de suspensión formalizados
• Los gestores pasan de gestionar 4-6 aplicaciones de forma manual a trabajar en una única interfaz unificada (SAP CRM enriquecido), con un ahorro estimado de 3 h/gestor/día
• Cumplimiento automatizado de los requisitos de comunicación regulatoria (RD 1955/2000) para interrupciones largas y compensaciones
```

#### 4.2 Invariantes (No Cambia)

```
• SAP CRM permanece como el sistema de registro maestro de todos los expedientes de reclamación
• El SLA regulatorio de 15 días hábiles (estándar) y 5 días (corte de suministro) sigue siendo el marco de referencia
• Las decisiones con implicaciones legales, regulatorias o económicas significativas siguen siendo 100 % humanas
• El Centro de Control (Field Operations) mantiene la responsabilidad operativa de las incidencias de red en campo
• El cumplimiento del RGPD para el tratamiento de datos de consumo y domicilio del cliente se mantiene inalterado
```

---

### 5. Hoja de Ruta (Draft)

**Duración Total Estimada**: 9 meses

**Tabla 10** (7×4):

| Fase | Objetivo | Entregable | Duración Estimada |
|---|---|---|---|
| F1 — Fundamentos IA y Datos | Preparar el dataset histórico de reclamaciones y entrenar el modelo de clasificación extendido (18 sub-tipos) | Modelo IA clasificación v1.0 validado · Dataset etiquetado con 18 sub-tipos | 6 semanas |
| F2 — Motor de Routing Paramétrico | Implementar el Motor de Routing con las 8 rutas y la tabla paramétrica configurable | Motor Routing Paramétrico deployado · Tabla de parámetros configurada y validada por Process Owners | 4 semanas |
| F3 — Integración WART, PUC y RECORE | Desarrollar y certificar las integraciones con los sistemas nuevos identificados en los CJ | APIs WART, PUC, RECORE integradas y testeadas · Módulo de Contexto Técnico Enriquecido operativo | 6 semanas |
| F4 — Excepciones y Estados de Suspensión | Implementar el catálogo de excepciones al cierre y los estados intermedios de suspensión | Motor de Excepciones operativo · 8 códigos EXC + 6 estados SUS implementados y configurados | 4 semanas |
| F5 — Módulo Cierre y Comunicación | Desarrollar los 20 templates diferenciados y el Motor de Comunicación Diferenciada | Templates TPL validados por CX Team · Motor de Comunicación integrado con SAP CRM | 4 semanas |
| F6 — Piloto y Validación | Piloto controlado con el 20 % del volumen de reclamaciones; ajuste del modelo y parámetros | Informe de piloto · Modelo IA ajustado · Parámetros de routing calibrados | 6 semanas |
| F7 — Despliegue Completo y Monitorización | Despliegue al 100 % del volumen; activación del Panel de Monitorización | Sistema en producción completa · Dashboard KPIs activo · Plan de mantenimiento del modelo | 6 semanas |

---

### 6. KPI

**KPI Cuantitativos**

**Tabla 11** (7×4):

| KPI | AS-IS (Situación Actual) | Objetivo TO-BE | Método de Medición |
|---|---|---|---|
| Tiempo medio de clasificación de reclamaciones | 8 minutos (manual) | < 30 segundos (automático) | Timestamp registro en SAP CRM vs timestamp clasificación IA |
| Tasa de re-routing / reclasificación | 35 % | < 8 % | % expedientes re-asignados post-clasificación inicial / total expedientes |
| Tasa de cierre automático | 28 % | 65 % | % expedientes cerrados sin intervención humana / total expedientes |
| Tiempo medio de resolución (todos los tipos) | 12,4 días hábiles | < 7 días hábiles | Fecha apertura vs fecha cierre en SAP CRM |
| Tiempo de recopilación de contexto técnico por gestor | 20 minutos (promedio) | 0 minutos | Eliminado por integración automática GIS/SCADA/WART/PUC |
| Volumen de expedientes duplicados por incidencias masivas | 100 % duplicados (sin agrupación) | < 30 % (agrupación automática) | % expedientes agrupados / total expedientes de incidencias masivas |
| Satisfacción del cliente (CSAT post-reclamación) | 3,2 / 5 | ≥ 4,0 / 5 | Encuesta automática post-cierre (NPS / CSAT) |

**KPI Cualitativos**

**Tabla 12** (5×3):

| KPI | Objetivo TO-BE | Método de Medición |
|---|---|---|
| Cobertura del modelo de clasificación IA | El modelo cubre el 100 % de los sub-tipos identificados en los CJ (18 sub-tipos) sin categoría "Otro" > 5 % | Monitorización mensual de la distribución de sub-tipos; revisión trimestral del modelo con Process Owners |
| Cumplimiento de los protocolos de excepciones al cierre | 100 % de los casos EXC-01 a EXC-08 gestionados según protocolo (ningún cierre automático indebido) | Auditoría mensual del 10 % de casos con excepción; revisión de alertas del Motor de Excepciones |
| Calidad de las comunicaciones diferenciadas | 95 % de los clientes reciben el template correcto correspondiente a su sub-tipo de reclamación | Muestreo mensual de 200 expedientes: verificación de template enviado vs sub-tipo del expediente |
| Integración y disponibilidad de sistemas nuevos (WART, PUC, RECORE) | SLA de disponibilidad ≥ 99,5 % para las APIs de WART, PUC y RECORE en horario operativo | Monitorización continua en Panel de Monitorización; alertas automáticas por caída de integración |
| Actualización del modelo IA | El modelo de clasificación se reentrena y valida al menos 1 vez por trimestre con nuevos datos de reclamaciones | Registro de versiones del modelo; informe de retraining trimestral aprobado por Business Owner y Data Owner |
