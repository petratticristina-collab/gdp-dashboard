# Capítulo 5 · Plan del ARQUITECTO, con las decisiones del ORQUESTADOR (13-09-2026)

> Punto de partida: entrada del capítulo 5 en `indice.md` (v1, aprobada por la autora) ajustada a las decisiones tomadas después de redactar el índice: decisión 8 (la autora no dispone de ninguna herramienta con acuerdo de tratamiento de datos; el libro se escribe desde ese supuesto), reglas 13, 16, 19, 21 y 22 de `biblia.md`, y los compromisos que los capítulos 2, 3 y 4 dejaron para este. Estado del ciclo: la autora ha pedido "seguir con el libro" con el capítulo 4 terminado y pendiente de su aprobación; el ORQUESTADOR abre el ciclo del 5 sin cerrar el 4 (sus diez preguntas abiertas siguen en la biblia).

## Ficha

- **Título:** Capítulo 5 · Documentar mejor y más rápido
- **Subtítulo:** Notas, interconsultas, informes y cartas sin perder la tarde.
- **Parte:** II · Usar. **Dependencias:** capítulos 3 (datos, anonimización, caso 7 "preparar una consulta a un compañero", disclaimers, diez preguntas) y 4 (cinco piezas, ejemplos propios, cadena de cuatro pasos, rúbrica, ficha de biblioteca, regla 19). Prepara el 8 (criterios de derivación y tratamiento) y el 13 (la nota es borrador; documentos clínicos no salen de la máquina).
- **Extensión objetivo:** 6.400-6.800 palabras en v1. Tope ad hoc 8.000 (regla 20: ocho prompts literales) si la v2 lo necesita; la v3 no lo supera.
- **Formato obligatorio:** el de la biblia (decisión 2), con la frase introductoria a los casos del capítulo 4 como modelo (POR ACLARAR y [FALTA: …], higiene de conversación, portabilidad, "comprueba la versión vigente").

## Gancho (primera persona, desde la consulta)

El del índice, corregido para que no sugiera que la historia clínica entró en una herramienta de consumo: "A las tres me quedaban once historias por cerrar y una interconsulta que llevaba dos semanas posponiendo. La interconsulta salió en cuatro minutos [con un perfil en rangos, capítulo 3]. Las historias, en veinte, [con una plantilla de nota que había preparado la semana anterior; la máquina no vio ninguna]. Antes eran la tarde entera." El REDACTOR decide la redacción; lo que no puede decir es que la IA leyó las once historias. Cierra con la frase de composición ("Como todas las escenas de consulta de este libro…").

## Los tres aprendizajes clave (corregidos)

1. De notas sueltas a nota estructurada: el modelo ordena y, si le dejas, inventa. Todo hueco se marca [FALTA: …] y lo rellenas tú. (El índice decía "ordena, no inventa": es falso y lo contradice el caso 7 del capítulo 3.)
2. La interconsulta que se lee: motivo, pregunta concreta, lo hecho ya en Atención Primaria y el criterio de derivación que cumple, escrito por ti con la guía delante (los criterios van en el capítulo 8; regla 13).
3. Dónde se hace cada cosa: la historia clínica real no entra en una herramienta de consumo. Hoy trabajas con plantillas, casos sintéticos construidos de cero (regla 22) y texto anonimizado a mano (capítulo 3, caso 1); el día que tu servicio de salud te dé una herramienta con contrato, los mismos prompts sirven con datos reales (decisión 8: escenario futuro, no punto de partida).

## Tesis del capítulo en una frase

Documentar con IA no es que la máquina lea tu historia clínica: es que tú tengas, antes de sentarte, la plantilla, la pregunta y la lista de huecos. Lo que se documenta es tuyo y lo firmas tú.

## Los ocho casos (con las decisiones del ORQUESTADOR)

| # | Caso | Momento | Herramienta | Decisiones |
|---|---|---|---|---|
| 1 | **Notas sueltas → nota estructurada con [FALTA]** | consulta | asistente de consumo, caso sintético | Notas telegráficas, como las escribe una médica con prisa (abreviaturas, cifras sueltas, sin verbos), de un caso construido de cero. La tarea es ordenar en S/O/A/P "o la estructura de tu sistema", sin interpretar (hereda el eslabón 1 del capítulo 4: sin "sugiere", "compatible con", sin rótulos que agrupen cifras). Diferencia con el capítulo 4: allí entraba un caso ordenado; aquí entra el desorden real. La salida es un borrador, nunca una anotación en la historia (compromiso con el capítulo 13). Escenario futuro: con contrato, las mismas notas reales. Recuento final: "HECHOS: [n] · HUECOS: [n] · FRASES QUE INTERPRETAN: [n]". |
| 2 | **Interconsulta a la unidad de obesidad o Endocrinología [AP]** | seguimiento de crónicos | asistente de consumo, perfil en rangos | Continúa el caso 7 del capítulo 3 (perfil apto, pregunta, huecos) y cumple el compromiso del capítulo 2 ("la plantilla de interconsulta se escribe en el capítulo 5, con caso sintético; los datos de la persona los pones tú, fuera de la IA"). Estructura de la carta: motivo; pregunta concreta; situación actual; lo hecho ya en AP (todo como [FALTA] si no está en el perfil); criterio de derivación que cumple, como hueco "[FALTA: criterio que cumple según la guía; lo escribo yo]" (regla 13: el modelo no cita criterios). Sin fármacos ni cirugía en la carta. Máximo 200 palabras. El REDACTOR explica en "Situación" qué hace que una interconsulta se lea y se conteste (pregunta respondible, lo ya hecho, lo que se pide). Sirve para la viñeta. |
| 3 | **Informes a petición de la persona: incapacidad temporal, inspección, discapacidad, servicio de prevención [AP]** | administración | asistente de consumo, plantilla con caso sintético | Un solo prompt con variable [destinatario] y [finalidad]. Lenguaje funcional (qué puede y qué no puede hacer, con qué limitación, desde cuándo, qué tratamiento sigue, qué se espera), nunca moral ni de estilo de vida; sin "obeso/a"; la obesidad como enfermedad crónica codificada. Estructura y tono son de la máquina; datos, diagnóstico, fechas y firma son de la médica, fuera de la IA. Marco legal solo si el REDACTOR lo conoce con certeza y marcado [VERIFICAR]: derecho de la persona a certificados e informes (Ley 41/2002, art. 22), certificados en el Código de Deontología 2022, RD 625/2014 para la IT, baremo de discapacidad RD 888/2022. EVIDENCIA lo comprobará; en la duda, [VERIFICAR]. Cubre el "informe para su empresa" de la viñeta (que en realidad es un informe para el servicio de prevención, a petición de ella). |
| 4 | **Del informe hospitalario a mi lista de tareas [AP]** | seguimiento de crónicos | asistente de consumo con informe sintético; escenario futuro con contrato | El gancho del capítulo 3 fue exactamente pegar un informe de alta real en un chat gratuito: aquí no se hace. El caso construye y prueba el prompt con un informe de alta sintético de cirugía bariátrica (o de consulta externa de la unidad), y lo que el lector se lleva hoy es doble: el prompt probado, listo para el día del contrato, y la lista genérica de "lo que suele quedar para AP" que aplica a mano al informe real. Salida: TAREAS PARA AP (qué, cuándo, quién), SEÑALES DE ALARMA que el informe nombra, LO QUE EL INFORME NO DICE ([FALTA]). Contenido clínico (suplementación, analíticas, señales tras cirugía bariátrica) solo por principio activo/nutriente y remitido a la guía (GIRO 2024; guías internacionales de seguimiento tras cirugía bariátrica, [VERIFICAR] si no se conocen con certeza). Nota al pie de transparencia (regla 12) si aparecen fármacos para la obesidad; mejor que no aparezcan: el informe sintético no los lleva. |
| 5 | **Plan de cuidados compartido con enfermería [AP]** | seguimiento de crónicos | asistente de consumo, sin datos | Quién hace qué en el seguimiento de la persona con obesidad en el centro: primera visita, hoja informativa, cita a los 15-20 días o al mes, seguimientos mensuales, analítica cuando toca (circuito real de la autora, biblia). La tarea: convertir ese circuito en una tabla de dos columnas (medicina / enfermería) con frecuencia, qué se registra y cuándo enfermería avisa a medicina. Sin ningún dato de persona: es un documento de organización. Es el caso más [AP] del capítulo. Riesgo: que la tabla la escriba la máquina sin que enfermería la haya discutido; mitigación: el prompt produce una propuesta para la reunión, no el plan. |
| 6 | **Resumen de dos años de evolución** | seguimiento de crónicos | hoy: caso sintético; mañana: solo con contrato | Índice: "exclusivamente herramienta con contrato". Con la decisión 8 se reescribe como escenario futuro: el prompt que tendrás listo el día que llegue el contrato, probado hoy con una tabla sintética de dos años (fechas relativas, peso en rangos, HbA1c, tensión, tratamientos por principio activo, visitas). Lo que se aprende probándolo: que el modelo inventa tendencias ("mejoría progresiva") y causas ("tras el cambio de tratamiento"); la tarea exige cronología sin causalidad, y "LO QUE NO SE PUEDE SABER CON ESTOS DATOS". Lo que la médica hace hoy sin IA: sus seis líneas de evolución en la historia y los contadores de la historia clínica electrónica (biblia). Explícito: nunca en una herramienta de consumo con datos reales, ni "anonimizados": dos años de una persona son esa persona (capítulo 3). |
| 7 | **La carta de resultados que no alarma [AP]** | consulta | asistente de consumo, plantilla | **Decisión del ORQUESTADOR:** sustituye a "Recomendación escrita de actividad física" del índice, porque la hoja de ejercicio ya se escribió en el capítulo 4 (caso 1) y el material educativo va al capítulo 6. La carta de resultados es documentación, es de Atención Primaria y usa el "CONTEXTO DE VOZ" del capítulo 4 (caso 2). Plantilla con un caso sintético: qué se dice por escrito de una analítica (en general, sin diagnósticos nuevos por carta), qué se deja para la visita y cómo se cita. Tres líneas de la regla 19 al pie, en usted. Se plantea a la autora como pregunta (¿mantiene la sustitución?). |
| 8 | **Respuesta a una reclamación con calma** | administración | asistente de consumo, hechos resumidos por la médica en una línea, sin nombres | La reclamación la escribió la persona y lleva su nombre: no se pega. La médica resume el hecho en una línea neutra y sin identificadores ("una persona se queja de que en la visita se habló de su peso sin que lo pidiera"), y pide estructura y tono: hechos, lo que se hizo, lo que se ofrece, sin justificarse ni disculparse en exceso ni culpar. Destinatario: el servicio de atención al paciente del centro o del departamento ([VERIFICAR: nombre del circuito de reclamaciones en la sanidad valenciana]). Este caso conecta con el estigma (capítulo 13): la reclamación más frecuente sobre obesidad es haber hablado del peso sin permiso, y el capítulo 4 (caso 5) ya pide permiso. |

Orden de los casos en el texto: 1, 2, 3, 4, 5, 6, 7, 8 (del documento más frecuente al menos frecuente; los tres de la viñeta son 2, 3 y 5).

## Estructura del desarrollo (antes de los casos)

- **Primera parte · Lo que documentar te cuesta y por qué.** Tiempo de documentación en AP (cifras solo con referencia verificable; si no, sin cifras). La nota que nadie lee y la interconsulta que vuelve sin respuesta. Documentar es decidir qué queda escrito: eso no lo hace la máquina.
- **Segunda parte · Tres cosas que la máquina hace bien con texto y una que no.** Ordenar, resumir, cambiar de registro (de nota a carta, de carta a informe). Lo que no hace: saber qué pasó en la consulta. De ahí [FALTA] y "sin interpretar".
- **Tercera parte · Dónde se hace cada cosa.** Cuadro de tres columnas: documento · qué entra hoy (consumo: plantilla / sintético / anonimizado a mano) · qué entraría con contrato. Una sola vez la distinción consumo/contrato (decisión del capítulo 4). Remisión al capítulo 3 para la anonimización y al 13 para "la nota es borrador".
- **Ocho casos.**
- **Viñeta.**
- **En 60 segundos · Hazlo hoy · Referencias.**

## Viñeta clínica (arquetipo compuesto, declarado)

Mujer de 40-45 años, obesidad de grado III, apnea del sueño en tratamiento con presión positiva, en lista de espera para valoración de cirugía bariátrica, que en el mismo mes necesita: una interconsulta a la unidad (pregunta concreta: qué prepara Atención Primaria mientras espera; caso 2), un informe para el servicio de prevención de su empresa a petición suya (turnos de noche y somnolencia; caso 3) y un plan de cuidados con enfermería (caso 5). Se combinan trayectorias documentales de varias pacientes; se modifican edad, profesión (no se da), hospital de referencia (no se da) y tiempos de espera (no se dan). Sin cifras que permitan trazar a nadie. La viñeta muestra lo que la máquina dio (tres borradores) y lo que la médica puso (los datos, el criterio de la guía, la firma) y una frase de la persona entrecomillada. Cierra con la promesa de datos en su fórmula única (regla 16).

## Reglas de la biblia que este capítulo tiene que cumplir de forma visible

- **Regla 19** en todo texto que llegue a la persona (caso 7; y si algún otro caso produce texto para la persona). Las cartas a un compañero (caso 2) y los informes (caso 3) no llevan disclaimer al paciente: son documentos entre profesionales que firma la médica; llevan, en cambio, la línea "borrador generado con apoyo de IA; datos y firma de la médica" solo en la conversación, nunca en el documento final (decidir en revisión: COMPLIANCE se pronuncia).
- **Regla 21:** una sola frase atribuye a "mi formación en IA" lo que venga del programa (documentación clínica: notas, interconsultas, informes, cartas).
- **Regla 22:** todos los casos sintéticos se construyen de cero; ninguno "cambiando dos datos".
- **Regla 16:** la promesa de datos con su fórmula única.
- **Regla 11:** disclaimer en usted en cartas y hojas enviadas.
- **Decisión 5:** herramientas por nombre con "comprueba la versión vigente".
- **Decisión 8:** consumo hoy, contrato como escenario futuro; una sola vez la distinción, y un cuadro.
- Ficha del caso 7 del capítulo 4 para los prompts que se guarden.

## Lo que el REDACTOR no debe hacer

- No describir la IA transcribiendo la consulta ("escribas ambientales") como algo que el lector pueda hacer hoy: grabar una consulta es dato identificable de la persona y de la médica, requiere herramienta con contrato y consentimiento; se menciona solo como escenario futuro, en dos líneas, sin marcas.
- No dar cifras de "tiempo ahorrado" propias sin decir que son estimación de la autora.
- No inventar referencias: [VERIFICAR] con el tipo de fuente que haría falta.
- No usar "obeso/a"; no nombrar marcas; no dar consejos individuales.

## Referencias que el REDACTOR puede usar si las conoce con certeza (EVIDENCIA las comprobará)

- Ley 41/2002, de autonomía del paciente (arts. 15, 17 y 22: historia clínica e informes/certificados).
- Código de Deontología Médica OMC 2022 (certificados e informes; historia clínica) [VERIFICAR apartados].
- GIRO 2024 (SEEDO), 2.ª ed.: seguimiento tras cirugía bariátrica en AP y criterios de derivación (solo remisión; los criterios van al capítulo 8).
- Guías de seguimiento tras cirugía bariátrica (AACE/TOS/ASMBS/OMA/ASA 2019; BOMSS 2020) [VERIFICAR].
- STOP-Bang (Chung 2008) para la apnea, si se cita.
- Evidencia sobre carga documental y tiempo de consulta en AP (solo si verificable; si no, sin cifra).
- Capítulo 4: Liu 2024 (posición en el contexto) si se reutiliza.

## Preguntas para Cristina que el REDACTOR deja planteadas (máximo 5 al cierre; las recoge el ORQUESTADOR)

1. ¿Mantiene la sustitución del caso 7 (carta de resultados en vez de hoja de actividad física)?
2. ¿Cuál es el circuito real de reclamaciones en su departamento y qué le piden que escriba?
3. ¿Cómo estructura sus notas hoy (S/O/A/P, texto libre, plantilla de su sistema) y qué campos exige su historia clínica electrónica en una interconsulta?
4. ¿Qué le pide la unidad de obesidad de referencia en una interconsulta para valoración de cirugía bariátrica (analítica, cribados, intentos previos documentados)?
5. ¿Cómo reparte hoy el seguimiento con enfermería en su centro (quién ve a quién y cada cuánto)?
