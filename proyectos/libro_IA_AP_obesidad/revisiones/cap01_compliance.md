# Revisión COMPLIANCE · Capítulo 1 · v1

> Agente: COMPLIANCE (Módulo 3 + RGPD/LOPDGDD + AI Act + Código de Deontología OMC 2022) · Fecha: 2026-09-11 · Capítulo revisado: `capitulos/cap01_v1.md` (v1, REDACTOR, 2026-09-11).
> **Estado: BLOQUEADO** (un hallazgo de gravedad alta: Caso 1). El capítulo vuelve al REDACTOR aunque los demás revisores digan "ok".

---

## Resumen de la auditoría por criterio

| # | Criterio | Resultado |
|---|---|---|
| 1 | Nombres comerciales de medicamentos de prescripción (RD 1416/1994) | **OK.** No aparece ninguno. "GLP-1" (l. 39) se cita como hormona intestinal, no como fármaco. Los prompts de los casos 2, 3, 4 y 6 prohíben expresamente nombrar medicamentos. |
| 2 | Prompts sin datos identificables · distinción consumo / acuerdo de tratamiento | **BLOQUEADO.** La sección "Dos herramientas, dos reglas" (l. 83-87) hace bien la distinción, pero el Caso 1 la contradice: exporta microdatos de la historia clínica y los sube a herramientas de consumo (H1, H2, H3, H4). Caso 5: revisión humana previa insuficiente (H5). Casos 2, 3, 4 y 6: correctos. |
| 3 | Viñeta clínica: regla "una sola persona", tres checks, etiqueta | **OK con matiz.** Etiqueta correcta ("Caso ilustrativo, no real: arquetipo compuesto"), declaración de rasgos combinados y modificados, rangos en lugar de cifras exactas. Check 1 (reconocible por alguien cercano): no. Check 2 (frame): no aplica, texto. Check 3 (disociación): sí. Matiz: el gancho de las 12:40 y la continuidad hacia el capítulo 14 presentan la figura como una paciente real seguida en el tiempo (H7). |
| 4 | Disclaimer estándar en material dirigido al paciente | **OK.** Caso 6 lo incluye literalmente en el prompt (l. 256) y en la salida (l. 264), y "Qué revisar" exige comprobarlo en las tres versiones. Caso 3 es explicación oral: no procede el disclaimer escrito, pero falta la advertencia de qué pasa si se imprime o se envía (H9, baja). |
| 5 | Transparencia (herramientas / formaciones patrocinadas) | **OK con matiz.** No se menciona ninguna herramienta ni formación patrocinada por su nombre. Pero el capítulo usa lenguaje del programa potencIA (patrocinado por Novo Nordisk) y cita GLP-1 en un libro cuya autora declara vínculo con Novo Nordisk: procede una remisión a la declaración de transparencia del inicio del libro (H8, baja). |
| 6 | AI Act: IA no decisora, supervisión humana explícita | **OK.** "No atiende pacientes, no diagnostica y no decide … Tú verificas y tú firmas" (l. 79); Caso 1 "No hagas recomendaciones clínicas" (l. 112); Caso 5 "No propongas automatizar nada que implique decisión clínica" (l. 227); Caso 4 verificación cita a cita (l. 208); "En 60 segundos" 4 y 5 (l. 295-296). Ningún uso descrito entra en alto riesgo del AI Act (anexo III); el material para pacientes lleva declaración de generación con IA (art. 50). |
| 7 | Propiedad intelectual | **REVISAR.** Reproducción casi literal de la "regla de oro" del Módulo 2 de potencIA, material cuyo aviso dice "cualquier obra derivada debe ser elaboración propia, no reproducción" (H6, media). Caso 4: cargar PDFs de guías en NotebookLM, matiz de licencia (H10, baja). |
| 8 | Lenguaje sin estigma · "persona con obesidad" | **OK.** "Persona con obesidad" en todo el texto; "obesa" y "el diabético de la tres" solo como contraejemplos explícitos (l. 55). Prompts de los casos 3 y 6 prohíben "obeso/a", "fracaso", "recaída", "culpa". Un matiz de redacción en l. 29 (H11, baja). |

---

## Hallazgos

### H1 · ALTA · Caso 1 "Mapa de mi cupo" · exportación de la historia clínica a herramientas de consumo
- **Ubicación:** l. 95-122 (cabecera, "Antes de nada", prompt, mitigación).
- **Cita literal:** "**Herramienta:** asistente con intérprete de código (Gemini, ChatGPT o Claude) sobre una hoja de cálculo exportada sin identificadores." · "Exporta solo variables categóricas: grupo de edad por décadas, sexo, categoría de IMC, sí/no para hipertensión, diabetes tipo 2 y dislipemia, y meses desde la última visita en tramos." · "Te adjunto una hoja de cálculo exportada de un sistema de historia clínica."
- **Problema:** (a) Un archivo con una fila por paciente (1.480 registros en el ejemplo) y siete variables de salud es **microdato seudonimizado, no dato anonimizado ni agregado**: con 8 décadas × 2 sexos × 5 categorías de IMC × 8 combinaciones de comorbilidad × 3 tramos hay más combinaciones posibles que filas, así que muchas filas son únicas. Según el considerando 26 y el art. 4.5 del RGPD, los datos seudonimizados siguen siendo datos personales, y aquí son de categoría especial (art. 9). El propio texto "sin municipio" no resuelve nada: el cupo es, por definición, una zona básica de salud, y la cuenta desde la que se sube el archivo es la de la médica. (b) El médico de familia no es responsable del tratamiento: lo es el servicio de salud (art. 4.7 RGPD). Exportar un listado de la historia clínica y subirlo a un servicio externo sin contrato de encargo (art. 28) excede las instrucciones del responsable (art. 29 y 32 RGPD; art. 5 LOPDGDD deber de confidencialidad; medidas del Esquema Nacional de Seguridad que aplican a los sistemas del SNS) y contradice la decisión editorial 5 de la biblia y la propia regla del capítulo (l. 85: en herramientas de consumo "solo entran datos sintéticos, anonimizados o agregados"). (c) En las versiones gratuitas o personales de las tres herramientas nombradas, por defecto los archivos subidos pueden usarse para entrenar y ser revisados por personas; la política cambia cada pocos meses. (d) La cabecera nombra herramientas de consumo para una tarea que, tal como está descrita, solo cabe en una herramienta con acuerdo de tratamiento de datos o en procesamiento local.
- **Norma afectada:** RGPD arts. 4.5, 4.7, 9, 28, 29, 32 y considerando 26 · LOPDGDD art. 5 · Código de Deontología OMC 2022 (secreto profesional, cap. V) · Módulo 3, checklist ítem 03 · biblia, decisiones 5 y 7.
- **Corrección literal (sustituir cabecera, "Antes de nada" y primera línea del CONTEXTO):**

  > **Momento:** administración. **Herramienta:** (a) una herramienta con acuerdo de tratamiento de datos que te ofrezca tu servicio de salud, o (b) si solo tienes una herramienta de consumo, **nunca el listado fila a fila**: solo una tabla de recuentos ya agregada que construyes tú antes de subir nada.
  >
  > **Antes de nada.** Un listado de tu cupo con una fila por persona es un dato de salud aunque no lleve nombre: la combinación de edad, sexo, IMC y enfermedades identifica a mucha gente en un cupo de 1.500. Por eso este caso tiene dos caminos. **Camino A (herramienta con acuerdo de tratamiento de datos):** pide a tu servicio de salud o a informática la extracción y confirma con el delegado de protección de datos que el uso está autorizado; solo entonces sube el archivo, con estas variables: grupo de edad por décadas, sexo, categoría de IMC, sí/no para hipertensión, diabetes tipo 2 y dislipemia, y meses desde la última visita en tramos. **Camino B (herramienta de consumo):** haz tú los recuentos con las tablas dinámicas de la hoja de cálculo (o con el módulo de explotación de tu historia clínica) y sube **solo la tabla de recuentos**, sin ninguna fila individual, con las celdas de menos de 5 personas sustituidas por "<5". Revisa el archivo con tus ojos antes de subirlo: sin nombres, sin CIP, sin fechas, sin municipio, sin texto libre. Y desactiva en la cuenta el uso de tus datos para entrenamiento antes de empezar.
  >
  > CONTEXTO: Te adjunto una tabla de recuentos agregados (no hay filas individuales) con estas dimensiones: grupo_edad (décadas), sexo, categoria_imc (…), hta (si/no), dm2 (si/no), dislipemia (si/no), ultima_visita (0-6 meses / 7-12 / más de 12), y la columna n (número de personas; "<5" cuando son menos de cinco). No contiene identificadores ni datos individuales.

  Ajustar la TAREA (2)-(4) a "suma y cruza los recuentos" y el ejemplo de salida ("He verificado que la tabla es de recuentos agregados y no contiene identificadores…").

### H2 · MEDIA · Caso 1 · comprobación de identificadores delegada al modelo después de subir el archivo
- **Ubicación:** l. 108, prompt, TAREA (1).
- **Cita literal:** "Comprueba primero que ninguna columna contiene nombres, fechas completas, números de identificación o texto libre; si encuentras algo así, detente y avísame sin procesar el archivo."
- **Problema:** cuando el modelo comprueba, el archivo ya está en los servidores del proveedor. La instrucción crea una falsa sensación de seguridad: la comprobación válida es humana y previa. El mismo patrón se repite en el Caso 5 (l. 227).
- **Norma afectada:** RGPD art. 25 (protección de datos desde el diseño) y art. 32 · Módulo 3, regla del minuto y checklist ítem 03.
- **Corrección literal:** mantener la instrucción al modelo como segunda red, pero reescribirla y añadir la frase humana en "Antes de nada": "TAREA: (1) Como comprobación adicional a la que ya he hecho yo antes de subir el archivo, confirma que ninguna columna contiene nombres, fechas completas, números de identificación o texto libre; si encuentras algo así, detente, avísame y no continúes." Y en "Antes de nada": "Esa revisión la haces tú, con el archivo abierto, antes de subirlo. Lo que el modelo compruebe después no deshace lo que ya has subido."

### H3 · MEDIA · Caso 1 · "el archivo se borra de la herramienta al terminar" como mitigación
- **Ubicación:** l. 122.
- **Cita literal:** "Mitigación: décadas en vez de edad, sin municipio, celdas pequeñas suprimidas, y el archivo se borra de la herramienta al terminar."
- **Problema:** borrar la conversación no garantiza el borrado en los sistemas del proveedor ni evita que el archivo se haya usado para entrenamiento o revisión humana si esa opción estaba activa. Además "celdas pequeñas suprimidas" se aplica a la salida, no al archivo que entra.
- **Norma afectada:** RGPD art. 5.1.f (integridad y confidencialidad) y art. 17 · biblia, decisión 5 ("comprobar versión vigente y política de datos").
- **Corrección literal:** "Mitigación: solo tablas de recuentos, nunca filas individuales; décadas en vez de edad; sin municipio; celdas de menos de 5 sustituidas por '<5' **antes** de subir; uso de datos para entrenamiento desactivado en la cuenta; y al terminar borras la conversación y el archivo, sabiendo que eso no deshace lo que el proveedor haya retenido: por eso lo que subes tiene que poder leerlo cualquiera sin dañar a nadie."

### H4 · MEDIA · Afirmaciones generales que el Caso 1 contradice
- **Ubicación:** l. 19 y l. 87.
- **Cita literal:** "Seis usos concretos de la IA generativa para empezar esta semana, con sus prompts, **sin introducir datos de pacientes en ninguna herramienta**." · "Todos los prompts de este capítulo funcionan sin datos identificables."
- **Problema:** el Caso 1, tal como está, introduce datos de pacientes (seudonimizados). Aunque se corrija con H1 (camino A), seguirá siendo el único caso en el que entra información derivada de la historia clínica. La promesa de la l. 19 es falsa para ese caso.
- **Norma afectada:** coherencia interna · Módulo 3, prueba del comité deontológico imaginario (ítem 10).
- **Corrección literal:** l. 19 → "Seis usos concretos de la IA generativa para empezar esta semana, con sus prompts: cinco no tocan ningún dato de pacientes y el sexto solo usa recuentos agregados o una herramienta con acuerdo de tratamiento de datos." l. 87 → "Ninguno de los prompts de este capítulo admite datos identificables; el único que usa información derivada de la historia clínica (caso 1) explica cómo agregarla antes."

### H5 · MEDIA · Caso 5 "Inventario de mi tiempo" · revisión humana previa de la lista y datos de terceros
- **Ubicación:** l. 216, l. 221, l. 227-230.
- **Cita literal:** "Solo tareas, sin datos de nadie." · "Si detectas algún dato que parezca identificar a una persona, indícamelo y no lo proceses." · "LISTA: [pega aquí tu lista]"
- **Problema:** una lista de tareas anotada con prisa durante una semana contiene con facilidad nombres o apodos de pacientes ("llamar a la Sra. X"), de compañeros ("sesión con Pepe"), números de historia o descripciones que identifican ("informe de incapacidad del vecino del bar"). La única barrera es la petición al modelo, que actúa después de pegar (mismo patrón que H2). No hay instrucción de revisión humana antes de pegar. La herramienta es de consumo (correcto si la lista está limpia).
- **Norma afectada:** RGPD arts. 5.1.c y 25 · LOPDGDD art. 5 · Módulo 3, checklist ítem 03 · biblia, decisión 7.
- **Corrección literal:** en "Situación", sustituir "Solo tareas, sin datos de nadie." por "Solo tareas, sin datos de nadie: antes de pegar la lista, reléela y quita cualquier nombre, iniciales, número de historia o detalle que permita reconocer a un paciente o a un compañero. Escribe 'llamada de seguimiento', no a quién." En el prompt, TAREA/RESTRICCIONES: "Ya he revisado la lista y no contiene datos de personas; como comprobación adicional, si detectas algo que parezca identificar a alguien, indícamelo y no lo proceses."

### H6 · MEDIA · Propiedad intelectual · reproducción casi literal de la "regla de oro" del Módulo 2 de potencIA
- **Ubicación:** l. 77-79 (título de sección y primer párrafo).
- **Cita literal (capítulo):** "### Copiloto, no piloto … Razona en voz alta, estructura y redacta a partir de lo que tú le pides. Tú verificas y tú firmas. Si una salida parece demasiado segura, probablemente lo es."
- **Cita literal (fuente, `memoria/Curso_PotencIA_materiales_sesiones.md`, guía de laboratorio del Módulo 2, NCompany / Novo Nordisk 2026):** "La IA es copiloto, no piloto. El modelo razona, estructura y redacta; el clínico verifica y firma. Si una salida parece demasiado segura, probablemente lo es. (M2, regla de oro)". El aviso del material dice: "Cualquier obra derivada debe ser elaboración propia, no reproducción."
- **Problema:** tres frases seguidas reproducen casi palabra por palabra un material formativo ajeno, de uso restringido a profesionales sanitarios y patrocinado por la compañía con la que la autora declara vínculo. No es cita (no hay atribución) ni elaboración propia.
- **Norma afectada:** Real Decreto Legislativo 1/1996 (Ley de Propiedad Intelectual), arts. 10, 17 y 32 (cita con atribución) · condiciones de uso del material · Módulo 3, checklist ítem 05 · orquestador, criterio 7.
- **Corrección literal:** reescribir el párrafo con voz propia, por ejemplo: "Voy a ser muy clara desde la primera página. La IA generativa no atiende pacientes, no diagnostica y no decide. Ordena, redacta y te devuelve borradores a partir de lo que tú le pides. La responsabilidad no se mueve de sitio: la salida la lees tú, la corriges tú y la firmas tú. Y cuanto más segura suene una respuesta, más motivos tienes para comprobarla." Si Cristina quiere conservar el lema "copiloto, no piloto" como título, atribuirlo en una línea: "La imagen del copiloto la aprendí en mi formación en IA (programa AI-Powered Metabolic Medicine, 2026) y la he hecho mía." Ver pregunta 2.

### H7 · MEDIA · Viñeta y gancho · continuidad que sugiere una paciente real seguida en el tiempo
- **Ubicación:** l. 9-11 (gancho), l. 274 (etiqueta), l. 286 (cierre de la viñeta).
- **Cita literal:** "Son las 12:40. Llevo cuatro pacientes de retraso y entra una mujer que lleva veinte años oyendo que tiene que comer menos." · "Es la primera consulta en veinte años en la que no le han dicho que coma menos. Volverá a aparecer en el capítulo 14, porque lo que le pasa después es la mejor razón que tengo para haber escrito este libro."
- **Problema:** la viñeta está bien etiquetada y pasa los tres checks. Pero el gancho la presenta como una escena real y fechada (hora, retraso, "veinte años"), y el cierre la proyecta hacia el capítulo 14 con una frase que afirma una evolución real ("lo que le pasa después"). El lector, y una paciente concreta de la consulta de El Campello con esa historia, puede entender que hay una persona real detrás del arquetipo. El Módulo 3 exige que el arquetipo se declare como tal, y esa declaración queda debilitada si la narración lo trata como seguimiento longitudinal de una persona.
- **Norma afectada:** Módulo 3, regla "una sola persona" (check 1 y "declarar explícitamente que es un arquetipo compuesto") · Código de Deontología OMC 2022 (secreto profesional) · biblia, glosario "arquetipo compuesto".
- **Corrección literal:** (a) ampliar la etiqueta de la l. 274: "Esta viñeta, igual que la mujer de las 12:40 con la que abre el capítulo, combina rasgos de varias pacientes con recuperación ponderal tras dietas restrictivas. Se han modificado profesión, municipio, situación familiar y edad exacta. No contiene fechas ni cifras que permitan reconocer a nadie. Cuando reaparezca en el capítulo 14 seguirá siendo la misma figura compuesta." (b) l. 286: "Volverá a aparecer en el capítulo 14, porque lo que suele pasar después, en muchas personas como ella, es la mejor razón que tengo para haber escrito este libro." (c) Propuesta para la biblia: una "Nota sobre los casos" en los preliminares del libro que declare que todas las escenas de consulta son composiciones.

### H8 · BAJA · Transparencia · remisión a la declaración de conflictos de interés
- **Ubicación:** l. 39 (GLP-1) y l. 77-81 (lenguaje de la formación patrocinada).
- **Cita literal:** "recibe señales del tejido adiposo (leptina), del intestino (GLP-1, PYY, grelina)".
- **Problema:** no hay infracción: GLP-1 se cita como hormona y no se menciona ningún fármaco ni marca. Pero la guía de disclosure del Módulo 3 pide declarar "dentro del propio contenido aunque no sea patrocinado" cuando el contenido trata directamente un área en la que hay relación con un laboratorio. El capítulo entero (obesidad, fisiología GLP-1, método aprendido en un programa patrocinado) está en esa área, y la declaración vive en los preliminares, no en el capítulo.
- **Norma afectada:** Código de Deontología OMC 2022 (transparencia) · Código de Buenas Prácticas de Farmaindustria · Módulo 3, guía de disclosure, área 2 ("contenido específico") y test rápido de transparencia.
- **Corrección literal:** añadir una nota al pie en la primera mención de GLP-1 o al inicio de la tercera parte: "Declaración de transparencia: mantengo vínculos con Novo Nordisk, detallados al inicio del libro. En este capítulo no hablo de fármacos; cuando lo haga, lo recordaré." Y en la biblia, dejar como regla que todo capítulo que trate fisiología incretínica, tratamiento farmacológico o herramientas aprendidas en formaciones patrocinadas lleve esa remisión.

### H9 · BAJA · Caso 3 (y Caso 2) · salida oral sin advertencia sobre su uso escrito
- **Ubicación:** l. 156-180 (Caso 3), l. 124-154 (Caso 2).
- **Cita literal:** "Necesito una explicación oral para decir en consulta…" · "Qué revisar antes de usarla. Que no exagere (…) ni caiga en el nihilismo (…)."
- **Problema:** la salida está pensada para decirla en voz alta con palabras propias, así que el disclaimer escrito no procede. Pero es previsible que el lector la imprima, la pegue en la hoja de recomendaciones o la envíe por la app de mensajería del centro; en ese momento pasa a ser material dirigido al paciente y necesita el disclaimer (decisión 6 de la biblia) y la revisión firmada.
- **Norma afectada:** biblia, decisión 6 · AI Act art. 50 (transparencia de contenidos generados con IA) · Código de Deontología OMC 2022.
- **Corrección literal (añadir al final de "Qué revisar" del Caso 3):** "Y si en lugar de decirla la imprimes o la envías por escrito, deja de ser tu explicación oral y pasa a ser material para el paciente: añade la frase 'Material informativo generado con apoyo de IA y revisado por tu profesional sanitario. No sustituye la valoración clínica individual' y fírmala tú, como en el caso 6."

### H10 · BAJA · Caso 4 · carga de documentos de terceros en NotebookLM
- **Ubicación:** l. 184, l. 188.
- **Cita literal:** "Sube como fuentes solo documentos públicos: el posicionamiento de la SEEDO, la guía GIRO, el resumen de la Comisión de The Lancet 2025 y la hoja informativa de la OMS."
- **Problema:** "público" no equivale a "libre de derechos". Las guías y el artículo de The Lancet tienen copyright; cargarlos para uso personal y docente interno es un uso razonable, pero el guion resultante no debe reproducir fragmentos extensos ni distribuirse como si fuera el documento. Además, la versión de consumo de NotebookLM y la de Workspace tienen políticas de datos distintas.
- **Norma afectada:** Ley de Propiedad Intelectual, arts. 31 bis y 32 · Módulo 3, checklist ítem 05 · biblia, decisión 5.
- **Corrección literal:** "Sube como fuentes solo documentos de acceso público que hayas descargado de su web oficial (posicionamiento de la SEEDO, guía GIRO, resumen de la Comisión de The Lancet 2025, hoja informativa de la OMS). Son para tu uso personal: el guion que salga cita y resume, no copia párrafos. Nada interno del centro, nada con datos de pacientes. Y comprueba si tu cuenta de NotebookLM es personal o de tu organización: la política de datos no es la misma."

### H11 · BAJA · Lenguaje · fórmula antigua sin marcar como tal
- **Ubicación:** l. 29.
- **Cita literal:** "Durante décadas hemos tratado el exceso de peso como un resultado: comes más de lo que gastas, engordas."
- **Problema:** es una descripción crítica del modelo antiguo y se entiende así, pero "engordas" en segunda persona, sin comillas, es la única frase del capítulo que suena a la voz que el propio capítulo desmonta. Sin estigma real; matiz de redacción.
- **Norma afectada:** biblia, voz de la autora ("lo que nunca dice") · consenso Rubino 2020 sobre lenguaje.
- **Corrección literal:** "Durante décadas hemos tratado el exceso de peso como un resultado, con la fórmula de siempre: 'si comes más de lo que gastas, engordas'. La ecuación es cierta en física y falsa en clínica."

---

## Lo que está bien y conviene mantener
- Sección "Dos herramientas, dos reglas" (l. 83-87): formulación clara de la distinción consumo / acuerdo de tratamiento de datos y de la regla "si no sabes cuál tienes, asume que es de consumo".
- Prompts de los casos 2, 3, 4 y 6: instrucción explícita de no usar datos de personas, prohibición de nombres de medicamentos y de términos estigmatizantes, disclaimer literal en el caso 6.
- Supervisión humana en cada caso ("Qué revisar antes de usarla") y en "En 60 segundos" 4 y 5.
- Etiqueta y construcción de la viñeta (rangos de edad, número de intentos aproximado, sin fechas ni lugar).
- Ausencia total de nombres comerciales y de recomendaciones terapéuticas individualizadas (RD 1416/1994, checklist ítem 02).

## Puntuación orientativa (checklist Módulo 3, adaptada a capítulo de libro)
Ítems aplicables 01, 02, 03, 05, 09, 10: cumplidos 4 de 6 (fallan 03 por el Caso 1 y 05 por H6). Resultado: **no publicar esta versión; corregir Caso 1 y párrafo "Copiloto, no piloto" y volver a auditar.**

## Preguntas para Cristina
1. ¿Tu servicio de salud (Conselleria de Sanitat) permite exportar listados del cupo desde la historia clínica y te ofrece alguna herramienta de IA con acuerdo de tratamiento de datos? De la respuesta depende si el Caso 1 se reescribe con dos caminos (A y B) o solo con el camino de recuentos agregados.
2. ¿Quieres conservar "Copiloto, no piloto" como título de sección atribuyéndolo a tu formación, o prefieres una imagen propia (el timón, por ejemplo, que ya usas en *Obesidades sin culpa*)?
