# Capítulo 7 · Plan del ARQUITECTO, con las decisiones del ORQUESTADOR (15-09-2026)

> Punto de partida: entrada del capítulo 7 en `indice.md` (v1, aprobada por la autora), la biblia (decisiones 1-9, reglas 10-30) y los solapamientos con lo ya escrito: la caza de referencias inventadas es el caso 2 del capítulo 2; buscar un dato en una guía con página es el caso 3 del capítulo 2; la sesión del centro con NotebookLM es el caso 3 del capítulo 1; el mapa del cupo con recuentos es el caso 6 del capítulo 1; el asistente propio con guías es el caso 2 del capítulo 8. Estado: capítulos 1-3 y 5 aprobados; 4 y 6 terminados, pendientes de aprobación; la autora ha pedido seguir.

## Decisión provisional del ORQUESTADOR sobre la longitud de los prompts

La autora no ha elegido aún entre las tres opciones de la regla 20 (biblia). Para el capítulo 7 se aplica la recomendada, la (c), como decisión provisional y reversible: **ningún prompt supera las 350 palabras**; el REDACTOR escribe correas por diseño (etiqueta antes que contenido, recuentos definidos, huecos de línea entera, líneas literales) sin frases redundantes, y el ingeniero de prompts, cuando añada una correa, quita otra o la funde. Objetivo del capítulo: 6.400-6.800; tope 8.000 (regla 20). Si la autora elige (a) o (b), el capítulo 7 no cambia: un prompt corto vale en las tres.

## Ficha

- **Título:** Capítulo 7 · Buscar y leer evidencia sin ahogarte
- **Subtítulo:** Deep Research, NotebookLM y lectura crítica en el tiempo que de verdad tienes.
- **Parte:** II · Usar. **Dependencias:** capítulos 2 (alucinación, caso 2; guía con página, caso 3; chat frente a razonador) y 4 (cinco piezas, rúbrica, ficha). Prepara el 8 (asistente propio con guías; decisiones) y el 12 (validación del proyecto).
- **Extensión objetivo:** 6.400-6.800 palabras. Tope 8.000. Siete prompts de ≤ 350 palabras.
- **Formato obligatorio:** el de la biblia (decisión 2), con la frase introductoria a los casos de los capítulos 4-6 como modelo.

## Gancho

El del índice: "Un paciente me preguntó por un estudio que había salido en el telediario. No lo había leído. Tardé dos minutos en tenerlo delante y diez en saber qué opinar." Cierra con la frase de composición.

## Los tres aprendizajes clave (corregidos)

1. Qué herramienta para qué pregunta: buscadores con IA (Perplexity y los modos de búsqueda profunda de Gemini, ChatGPT y Claude) para orientarse en minutos; buscadores de evidencia (Consensus, Elicit, Scite, OpenEvidence) para encontrar y clasificar estudios; NotebookLM o el asistente con archivos para tus propias fuentes. Ninguna sustituye a PubMed, la ficha técnica en CIMA y la guía en PDF para verificar. Todas cambian de nombre y de versión: "cuando escribo esto".
2. Lectura crítica asistida: el modelo estructura (diseño, población, comparador, desenlace principal, tamaño del efecto con su intervalo, pérdidas, financiación) y tú juzgas. La pregunta que decide: "¿esto cambia lo que hago el lunes con las personas de mi cupo?".
3. Cada cita se comprueba; una referencia con aspecto real que no existe es el error más caro de una sesión, de un artículo y de este libro. El capítulo 2 enseñó a cazarla; este enseña el protocolo para no dejar pasar ninguna.

## Tesis del capítulo en una frase

La evidencia no está más lejos que antes: está más enterrada. La máquina desentierra en minutos; decidir qué vale y qué cambia en tu consulta sigue costando lo mismo, y es tuyo.

## Los siete casos (con las decisiones del ORQUESTADOR)

| # | Caso | Momento | Herramienta | Decisiones |
|---|---|---|---|---|
| 1 | **De la duda a la pregunta PICO** | consulta | asistente de consumo → buscador de evidencia (Consensus, Elicit u otro) | Una duda de consulta ("¿se pierde músculo con el tratamiento farmacológico y qué lo evita?") convertida en pregunta PICO (población, intervención, comparador, desenlace), tres cadenas de búsqueda (una para PubMed con términos MeSH, una en lenguaje natural para un buscador de evidencia, una en español para orientarse), y una lista de "lo que la pregunta no cubre". Sin datos de nadie. El prompt exige separar "lo que sé" de "lo que busco" y no responder la pregunta clínica: solo formularla. Fármacos por mecanismo si aparecen; el ejemplo de masa muscular no nombra ninguno (regla 12 solo si el REDACTOR nombra fármacos para la obesidad: mejor no). |
| 2 | **Tres guías, una pregunta: coincidencias y discrepancias con cita [AP]** | consulta | NotebookLM o asistente con archivos, con guías públicas | **Reformulado**: el índice decía "Mis guías, con citas" y eso ya está (capítulo 1, caso 3; capítulo 2, caso 3; capítulo 8, caso 2). Aquí: la misma pregunta (por ejemplo, "¿qué criterios de derivación desde Atención Primaria a una unidad de obesidad?") a tres guías cargadas (GIRO 2024; una europea o canadiense, Wharton 2020; NICE si el REDACTOR la conoce con certeza), y una tabla de tres columnas con cita literal y página o número de cita por guía, más las filas "COINCIDEN", "DISCREPAN" y "NO LO DICE NINGUNA". La decisión sobre a quién derivar no la toma la tabla: capítulo 8 (regla 13). Solo documentos públicos de su web oficial, uso personal. |
| 3 | **Un ensayo en diez minutos** | docencia | asistente con carga de documento (PDF de acceso abierto o resumen) | Plantilla de lectura crítica de un ensayo de un fármaco para la obesidad, por principio activo o clase: diseño, población (¿se parece a mi cupo?), comparador, desenlace principal y secundarios, tamaño del efecto con intervalo de confianza, pérdidas y análisis, efectos adversos con cifras absolutas, financiación y conflictos, y "lo que el resumen no dice". Salida cerrada con "DATOS QUE NO ESTÁN EN EL DOCUMENTO: [n]". El ejemplo usa un ensayo real de acceso abierto que EVIDENCIA pueda verificar (por ejemplo, un ensayo de semaglutida 2,4 mg o de tirzepatida en obesidad, citado por principio activo y con su registro), o un ensayo sintético declarado si no hay acceso abierto. **Nota al pie de transparencia obligatoria (regla 12)**: el capítulo trata fármacos para la obesidad. Sin nombres comerciales; sin decir a quién se indica. |
| 4 | **Del titular al artículo [AP]** | divulgación y consulta | buscador con IA (Perplexity o modo de búsqueda de un asistente) → PubMed | "He visto en la tele que…": en dos minutos, localizar el estudio original (no la noticia), y en diez, la respuesta en dos frases para la persona, con la fuente y con lo que la noticia exageró. El prompt pide primero la cadena de búsqueda y el estudio con DOI, y solo después la lectura; la respuesta para la persona lleva las tres líneas de la regla 19 si se entrega por escrito (normalmente es oral: se dice). Regla 27: sin culpa. |
| 5 | **Mis datos, agregados: el antes y después del programa del centro [AP]** | seguimiento de crónicos | asistente que ejecute código, con tablas agregadas construidas en el ordenador del centro | Continúa el caso 6 del capítulo 1 (recuentos, nunca filas, "<5"). Aquí entran medias y medianas por trimestre de las personas del programa (peso en rango de categoría, HbA1c media, tensión), calculadas en la hoja de cálculo del centro, y la máquina hace dos cosas: la lectura descriptiva y, sobre todo, la lista de lo que NO se puede concluir (sin grupo de comparación, regresión a la media, pérdidas de seguimiento, quién falta en el numerador). Lección del capítulo 5 (caso 6): la máquina inventa tendencias y causas. Sin identificadores; decisión 8. |
| 6 | **La alerta mensual de evidencia para el equipo [AP]** | docencia | alertas de PubMed (MyNCBI) como fuente; asistente para resumir los resúmenes; búsqueda programada si la herramienta la ofrece | Honestidad: la alerta fiable y gratuita es la de PubMed; la IA resume lo que la alerta trae y clasifica por relevancia para Atención Primaria con una regla explícita ("cambia lo que hago / conviene saberlo / no aplica"). Una página al mes para la sesión del centro, con cada estudio citado por DOI y la advertencia de que resumir un resumen no es leer el artículo. Si el REDACTOR menciona búsquedas programadas de una herramienta, con "cuando escribo esto". |
| 7 | **Verificar las referencias de mi sesión: el protocolo** | docencia | asistente + PubMed + navegador | Continúa el caso 2 del capítulo 2 (cazar una alucinación) y lo convierte en protocolo: la lista de referencias de una sesión, artículo o capítulo pasa por (1) el prompt, que la convierte en tabla con los campos que hay que comprobar y marca lo que tiene aspecto sospechoso (DOI con formato raro, año y volumen que no cuadran, revista inexistente, autores que no coinciden con el tema); (2) la comprobación manual, una por una, en PubMed por título y en el navegador por DOI; (3) la etiqueta final de cada una (EXISTE Y COINCIDE / EXISTE CON ERRORES / TRATA DE OTRA COSA / NO EXISTE). El prompt no verifica: prepara la verificación. Es el método que este libro usa (el agente de evidencia): el REDACTOR puede decirlo en una frase sin nombrar el orquestador. |

Orden: 1 a 7. La viñeta usa los casos 1, 4 y 7 (o 3).

## Estructura del desarrollo (antes de los casos)

- **Primera parte · Enterrada, no lejos.** Volumen de publicaciones (cifra solo con referencia verificable; por ejemplo, el crecimiento de PubMed; si no, sin cifra); la pregunta del paciente que llega antes que el artículo; lo que hacía antes (nada, o el resumen) y lo que hago ahora.
- **Segunda parte · Cuatro tipos de herramienta y para qué sirve cada una.** Cuadro: buscador con IA (orientarse; cita fuentes web, no siempre científicas), buscador de evidencia (encuentra y clasifica estudios; algunos dan "consenso" que no es metaanálisis), asistente con archivos o NotebookLM (lo tuyo, con cita), PubMed y CIMA (verificar; sin IA). Para cada uno: qué entra (nada de nadie), qué devuelve, cuándo miente. "Cuando escribo esto; comprueba la versión vigente."
- **Tercera parte · Leer con rúbrica también un artículo.** La rúbrica del capítulo 4 aplicada a un resumen estructurado: fidelidad (¿dice lo que dice el artículo?), priorización (¿el desenlace principal primero?), calibración (¿el efecto con su intervalo?), confusores (¿población, comparador, financiación?), acción segura (¿cambia lo que hago el lunes?). Una sola frase de atribución a "mi formación en IA" (regla 21): el itinerario de herramientas y "hagamos un paper" vienen del programa; se reformulan.
- **Siete casos.**
- **Viñeta.**
- **En 60 segundos · Hazlo hoy · Referencias.**

## Viñeta clínica (arquetipo compuesto, declarado)

Mujer de 30-35 años, obesidad de grado II, en tratamiento farmacológico de la obesidad (por mecanismo, sin nombre), que planifica un embarazo y pregunta si sigue o lo deja, y desde cuándo. Se combinan varias consultas preconcepcionales; se modifican edad, paridad y tratamiento; sin municipio, fechas ni cifras. **Reglas:** el capítulo 6 ya dijo "avíseme antes de nada"; aquí se muestra cómo se busca bien y rápido: primero la ficha técnica en CIMA (fuente primaria: contraindicación y antelación para suspender según principio activo), después la guía (GIRO 2024), después PubMed para la pregunta concreta (exposición inadvertida en el primer trimestre: qué se sabe y qué no), con el caso 1 (PICO) y el caso 4 (del titular al artículo) si ella trae algo leído. La viñeta no decide la anticoncepción ni el plan (capítulo 8); muestra que la respuesta "se suspende antes de buscar el embarazo, con la antelación que dice la ficha de su fármaco, y lo planificamos juntas" sale de la fuente y no de la máquina, y que lo que no se sabe se dice. Frase suya entrecomillada; promesa de datos (regla 16); nota de transparencia (regla 12) en el caso 3 y remitida aquí; estribillo si encaja.

## Reglas de la biblia que este capítulo tiene que cumplir de forma visible

- **Regla 12:** nota al pie ¹ en el caso 3 (párrafo propio, formato de los capítulos 3, 4 y 6) y remisión en la viñeta.
- **Regla 19 y 11:** solo si algún texto se entrega por escrito (caso 4, variante escrita).
- **Regla 16:** promesa de datos en la viñeta.
- **Regla 21:** una sola atribución a "mi formación en IA".
- **Reglas 22-26:** sin datos de nadie; tablas agregadas construidas fuera de la IA (caso 5); documentos públicos (caso 2).
- **Regla 27:** listas cerradas exceptúan negaciones.
- **Decisión 5:** herramientas por nombre con "comprueba la versión vigente"; distinguir lo que busca en internet de lo que responde de memoria (capítulo 2, caso 2).
- **Tope de 350 palabras por prompt** (decisión provisional de arriba).
- Ficha del capítulo 4 para guardar los prompts.

## Lo que el REDACTOR no debe hacer

- No repetir los casos del capítulo 2 (cazar una alucinación; guía con página) ni el mapa del cupo del capítulo 1: remitir.
- No presentar el "consenso" de un buscador de evidencia como metaanálisis ni un resumen de resúmenes como lectura.
- No dar cifras de eficacia de fármacos como consejo; en el caso 3 las cifras son las del ensayo leído, citadas, y el texto dice "lo que decide a quién, el capítulo 8".
- No nombrar marcas; no decir a quién se indica; no inventar referencias ni ensayos: [VERIFICAR] con el tipo de fuente.
- No prometer que una herramienta hace algo que "cuando escribo esto" no se ha comprobado.

## Referencias que el REDACTOR puede usar si las conoce con certeza (EVIDENCIA las comprobará)

- Bhattacharyya 2023 (referencias inventadas por chat; ya citada en el capítulo 2, verificada allí) y otras sobre citas fabricadas [VERIFICAR].
- Un ensayo de acceso abierto de un fármaco para la obesidad para el caso 3 (por ejemplo, Wilding 2021 NEJM STEP 1, semaglutida 2,4 mg; Jastreboff 2022 NEJM SURMOUNT-1, tirzepatida) [VERIFICAR acceso y datos]; el REDACTOR cita por principio activo.
- Guías: GIRO 2024; Wharton 2020 (CMAJ); NICE NG246 u otra si se conoce con certeza [VERIFICAR].
- PICO y lectura crítica: Sackett/Straus (Evidence-based medicine) [VERIFICAR edición]; CASPe o las fichas de lectura crítica en español [VERIFICAR].
- Crecimiento de la literatura biomédica (Landhuis 2016 Nature "Scientific literature: information overload", u otra) [VERIFICAR].
- PubMed y MyNCBI (fuente oficial, NLM); CIMA (AEMPS).
- Evaluación de buscadores de evidencia con IA (estudios sobre Consensus/Elicit/Perplexity) [VERIFICAR: solo si se conoce con certeza].

## Preguntas para Cristina que el REDACTOR deja planteadas (máximo 5 al cierre; las recoge el ORQUESTADOR)

1. ¿Qué herramientas de búsqueda usa hoy de verdad (Perplexity, Consensus, Elicit, OpenEvidence, NotebookLM) y cuál pagaría?
2. ¿Qué pregunta de consulta le hizo buscar evidencia la última vez, y qué encontró?
3. ¿Su centro hace sesión mensual de evidencia? ¿Quién la prepara?
4. ¿Tiene datos agregados del programa de obesidad del centro (cuántas personas, desde cuándo, qué variables)?
5. ¿Cómo responde hoy a "he visto en la tele que…"?
