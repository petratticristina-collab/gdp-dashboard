# Revisión PROMPTS · Capítulo 4 · v1

> Agente: PROMPTS (ingeniero de prompts) · Fecha: 2026-09-12 · Ámbito: exclusivamente los bloques de código que el capítulo ofrece al lector: el prompt pobre y el estructurado del Caso 1 (con la salida del pobre citada en la Tercera parte, porque es el otro término de la comparación), el prompt del Caso 2, los cuatro eslabones del Caso 3, el prompt del Caso 4, los prompts de los Casos 5 y 6 y la plantilla Markdown del Caso 7 (revisada como ficha, igual que el inventario del Caso 6 del capítulo 2). En las tres primeras partes no hay ningún bloque de código: los prompts sueltos ("antes de responder, escribe tu razonamiento paso a paso", "pensemos paso a paso") van entrecomillados en el texto y son correctos tal cual. No se revisa el texto expositivo ni las referencias.
> Versión revisada: `capitulos/cap04_v1.md` tal como quedó tras el recorte del REDACTOR de las 12:12 UTC (6.977 palabras). Se ha releído entero después del aviso del ORQUESTADOR; las diferencias con la versión anterior que afectan a los prompts son tres: el Caso 2 gana la lista POR ACLARAR, el Caso 3 pierde colesterol total y HDL en el contexto del eslabón 1, y la frase introductoria añade "cuando escribo esto: comprueba la versión vigente". Ninguna cambia los veredictos.
> Método: el de los capítulos 1 a 3. Para cada prompt: rol · contexto · tarea · formato · restricciones; anonimización y comprobación humana previa (decisión 7 de `biblia.md`); variables entre corchetes con ejemplo por defecto; salidas cerradas, etiqueta antes que contenido (T2 del capítulo 1, T4 del capítulo 2, T1 del capítulo 3); portabilidad Gemini / ChatGPT / Claude; realismo del ejemplo; riesgo. Cada prompt se ha ejecutado mentalmente con un caso sintético y la salida se ha leído con la rúbrica del propio capítulo (fidelidad · priorización · calibración · confusores · acción segura). Escala de certeza, marcadores [FALTA: …] y POR ACLARAR, y reglas 7, 11, 16 y 17 de `biblia.md` aplicadas como norma.

## Resumen de veredictos

| Caso | Título | Bloques | Veredicto | Motivo principal |
|---|---|---|---|---|
| 1 | Prompt pobre frente a prompt estructurado | 2 prompts + 1 salida citada | **mejorar** (el estructurado, listo con retoques; la comparación, no) | La salida del prompt pobre que se lee con la rúbrica ("Presenta claramente un síndrome metabólico… necesitará mucha disciplina") no es lo que devuelve un modelo de 2026 a "Plan de ejercicio para una persona con obesidad y artrosis de rodilla": no hay caso al que ser infiel, ningún modelo actual diagnostica un síndrome sin datos ni escribe "disciplina". Es un hombre de paja, y además contradice el gancho, que describe la salida real (folleto, "consulte con su médico", 5-10 %). La comparación honesta es más útil: el prompt pobre no está mal, está vacío, y el modelo lo rellena con lo más probable (kilos, calorías, 150 minutos, "consulte con su médico"). El estructurado es bueno; le sobra [FALTA: …] dentro de una hoja para el paciente, le falta prohibir el "consulte con su médico antes de empezar" (inútil en una hoja que entrega la médica) y conviene alinear su contexto con el del Caso 3 (mismo hombre, misma metformina). |
| 2 | Que escriba como yo | 1 prompt | **mejorar (leve)** | Bien construido, con la etiqueta (0) antes que el contenido. Pero la tarea pide "una hoja sobre qué traer y de qué vamos a hablar" y la restricción prohíbe "contenido clínico que no esté en los ejemplos o en la tarea": el modelo tiene que inventar el contenido (venga en ayunas, traiga la medicación) porque nadie se lo ha dado. Los tres modelos lo hacen. Falta la variable de contenido. Y el pie va en usted aunque el trato sea tú (regla 11). |
| 3 | La cadena de cuatro prompts | 4 prompts | **mejorar** (eslabones 2 y 4 reescritos; 1 y 3, retoques) | "No propongas tratamientos" no impide lo que más hacen los modelos con HbA1c 7,6 % y obesidad de grado II: un dilema titulado "intensificación del tratamiento hipoglucemiante" con la clase de fármaco dentro, y "LDL por encima del objetivo en persona con diabetes (ALTA)", que es una indicación de estatina con otro nombre. La nota al pie promete que "ninguno para la obesidad" aparece; el prompt no lo garantiza. Y el texto (B) para la persona lleva el aviso de IA, pero no lleva red de seguridad ni cómo contactar, en un texto que manda a moverse a un hombre con rodillas, diabetes y una tensión de 146/88. |
| 4 | "No cierres diagnóstico" | 1 prompt | **listo (retoque)** | El mejor prompt del capítulo y el ejemplo más realista. "No lo sé" existe pero no es un valor de la escala: el modelo lo escribe como comentario y el recuento final no sabe qué contar. Se convierte en cuarto valor definido. El tope de ocho puntos en HECHOS obliga a fusionar hechos (el caso tiene doce) y rompe la numeración que las inferencias necesitan. Y la línea de rescate para quien no tiene razonador está en el capítulo 2; conviene que viaje con el prompt. |
| 5 | El consejo breve de siete minutos | 1 prompt | **listo (retoque)** | Sale bien en los tres. Retoques: valor por defecto en [usted / tú]; que la primera frase pida permiso para hablar del peso (la entrevista motivacional lo pone antes de nombrar); definir qué es "palabra prohibida" con derivados ("esforzarse", "disciplinado"). |
| 6 | Mensaje entre visitas | 1 prompt | **mejorar (leve)** | Aviso en usted correcto y la línea de seguridad de la regla 17 literal y entera: bien. Pero "diga cómo contactar si hay dudas" hace que ChatGPT y Gemini inventen un teléfono o "responda a este mensaje" (que en muchos portales no existe); "máximo 90 palabras" sin decir si el aviso al pie cuenta hace que el modelo recorte la línea de seguridad para caber; "FRASES QUE EVALÚAN" no está definido; y el mensaje (2) admite consejos de comida y dosis con otras palabras. |
| 7 | Mi biblioteca de prompts en Markdown | 1 plantilla | **listo (retoque)** | Usable tal cual y coherente con la ficha del Anexo A en lo esencial. Le faltan cuatro líneas que el propio capítulo exige y la plantilla no tiene sitio para ellas: "Probada por" (la mitigación del riesgo habla de "la firma de quien la probó"), "Por qué esta herramienta" (el Anexo A lo lleva), "Variables" (qué poner en cada corchete) e "Higiene" (conversación nueva, memoria, borrado). |

Ningún prompt es peligroso tal como está; dos producen algo que no debe salir sin cambios: el eslabón 2 del Caso 3 (fármacos por clase) y el eslabón 4 (texto para la persona sin red de seguridad). Ninguno hay que rehacer de arriba abajo. La portabilidad es limpia: nada depende de búsqueda ni de archivos; solo el Caso 4 depende del razonador, y tiene rescate.

---

## Hallazgos transversales (afectan a varios casos)

**T1 · El prompt pobre tiene que perder con honestidad.** El capítulo dice, con razón, que "un prompt pobre no es erróneo: deja todas las decisiones a la estadística". La salida que luego lee con la rúbrica no es eso: es una salida errónea, con un diagnóstico inventado y una palabra de regañina, que ningún modelo de consumo escribe hoy a esa línea. Ejecución mental del prompt pobre tal cual, en los tres modelos: un plan genérico en cuatro o cinco bloques (calentamiento, aeróbico de bajo impacto, fuerza de cuádriceps, flexibilidad, progresión a 150 minutos semanales), en tono de folleto, con "consulte con su médico antes de comenzar", casi siempre una línea de "una pérdida del 5-10 % del peso reduce la carga sobre la rodilla" y, en Gemini y ChatGPT, una mención a "dieta hipocalórica" o a "déficit calórico"; a veces "puede tomar paracetamol antes del ejercicio". Ni "síndrome metabólico" ni "disciplina". Lo que de verdad falla es más interesante y es la tesis del capítulo: el plan no sabe que la marcha se agota a los veinte minutos (propone 30-45 minutos desde la primera semana), no está escrito para la persona (está escrito para quien pregunta, en tú o en infinitivo), no tiene regla de dolor ni señales para parar, trae kilos y calorías, y remata con "consulte con su médico", que es inútil en una hoja que entrega la médica. Eso es lo que hay que leer con la rúbrica, y la rúbrica sigue diciendo "no sale": fidelidad no aplica (no hay caso), priorización falla (el peso antes que la rodilla), calibración falla ("los pacientes con obesidad deben…" en general), confusores faltan (nada de dolor, sueño, fármacos), acción segura falla (45 minutos con una marcha de veinte). Con eso, el gancho, la rúbrica, el "Hazlo hoy" ("subraya cada kilo, cada caloría y cada 'consulte con su médico'") y el Caso 1 cuentan la misma historia. Hoy no.

**T2 · "No propongas tratamientos" no basta: la correa va por nombre, por clase y por juicio sobre lo que ya toma.** Con una HbA1c de 7,6 %, obesidad de grado II, LDL 131 y triglicéridos 210, los tres modelos tienden a producir, en el eslabón 2 del Caso 3, un dilema del tipo "necesidad de intensificar el tratamiento; los fármacos con beneficio ponderal y cardiovascular (agonistas del receptor de GLP-1, inhibidores de SGLT2) serían de elección (ALTA)" y otro del tipo "LDL por encima del objetivo en diabetes (ALTA)". Claude lo evita más; Gemini casi nunca. Lo hacen porque "no propongas tratamientos" lo leen como "no pautes", y nombrar una clase les parece analizar. El capítulo promete en la nota al pie que "ninguno para la obesidad" aparece: hoy no depende del prompt, depende de la suerte. Regla, en una línea, para los eslabones 2, 3 y 4: "No nombres ningún fármaco ni clase de fármacos, ni el que ya toma ni otros; no digas si el tratamiento actual basta, sobra o debe cambiarse; si un dilema es 'qué hacer con el tratamiento', escríbelo solo como 'DECISIÓN TERAPÉUTICA: la toma la médica', sin desarrollarlo; y no digas si hay que derivar". Y una salida cerrada que lo haga visible: "FÁRMACOS O CLASES NOMBRADOS: [n]", que la lectora comprueba con el texto delante. Afecta al Caso 3 (los cuatro eslabones) y, por la misma lógica, al Caso 4 ("sin tratamientos" ya está; se añade "ni clases").

**T3 · Todo texto que va a una persona lleva tres líneas fijas, no una.** El aviso de IA en usted está en los Casos 1, 2, 3 (B) y 6: bien (regla 11). Pero la regla 17 pide red de seguridad cuando el texto toca síntomas o tratamientos, y el texto (B) del Caso 3 manda a caminar a un hombre con diabetes, artrosis y una toma de 146/88, sin decir qué hacer si algo va mal ni cómo contactar. En el Caso 6 sí está la línea de seguridad, pero "cómo contactar" queda abierto y el modelo lo inventa. Propuesta única para el libro, que el REDACTOR puede fijar en `biblia.md` si el ORQUESTADOR lo acepta: cualquier texto para la persona termina con (1) cómo contactar, siempre como marcador "[FALTA: cómo contactar con la consulta]", nunca un teléfono ni "responda a este mensaje"; (2) cuándo no esperar, con la fórmula de la regla 17 si hay tratamiento nuevo o, si hay movimiento o síntomas, "Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112"; (3) el aviso de IA en la variante que corresponda al trato. En ese orden, y las tres literales en el prompt, porque "el modelo tiende a suavizarla" (lo dice el propio Caso 6, y es verdad: Gemini convierte "no espere: urgencias o 112" en "acuda a un servicio de urgencias si lo considera necesario").

**T4 · Lo que no le das, lo inventa: tres variables que faltan.** (a) Caso 2: el contenido de la hoja nueva ("qué traer y de qué vamos a hablar"): el modelo escribe "venga en ayunas", "traiga su medicación y las últimas analíticas", "hablaremos de sus hábitos" sin que nadie se lo haya dado, y la restricción "no añadas contenido clínico" no puede cumplirse porque la tarea lo exige; hace falta un corchete con los puntos que la hoja debe contener. (b) Caso 6: el canal de contacto; ChatGPT escribe "llame al 900 000 000 o responda a este mensaje", Gemini "a través de la app del centro"; hace falta el marcador. (c) Caso 3, eslabón 1: "TSH 2,4" sin unidad en un prompt que exige "cada cifra con su unidad, tal como te la di": el modelo añade "mUI/l" y ya ha añadido un dato. Regla de los capítulos anteriores, aplicada aquí: si el prompt exige algo del contexto, el contexto lo trae; si no lo trae, va como [FALTA: …] o como corchete que rellena la lectora.

**T5 · Recuentos finales: útiles, pero solo si se dice qué se cuenta.** El capítulo hereda bien la salida cerrada con recuento ("CIFRAS DE PESO O CALORÍAS: [n]", "HECHOS: [n] · HUECOS: [n]", "ALTA: [n] · MEDIA: [n] · BAJA: [n]", "MARCADORES SIN RELLENAR: [n]", "PALABRAS PROHIBIDAS ENCONTRADAS: [n]") y dice lo justo: "el cero lo cuentas tú". Dos recuentos no están definidos y cada modelo cuenta una cosa: "NO LO SÉ: [n]" en el Caso 4 (¿hipótesis sin certeza?, ¿datos ausentes?, ¿veces que aparece la frase?) y "FRASES QUE EVALÚAN: [n]" en el Caso 6 (¿"enhorabuena"?, ¿"bien"?, ¿"lo ha hecho fenomenal"?). Definir cada recuento en la misma línea en que se pide. Y una precisión que conviene mantener: en los Casos 1, 5 y 6 el recuento es de lo que el propio modelo acaba de escribir (autoauditoría); es una afirmación, no una prueba, como dice el capítulo, y por eso "qué revisar" debe seguir mandando contarlo a mano.

**T6 · Trato y aviso tienen que ir juntos.** El Caso 2 ofrece "trato de [usted (hoja impresa) / tú]" y un pie fijo en usted. Si la lectora elige tú, la hoja queda con "te propongo" arriba y "su profesional sanitario" abajo (T6 del capítulo 1, resuelto en `biblia.md` con la regla 11). La solución es pedir en el prompt "el aviso en el trato elegido" y dar las dos variantes literales. Caso 5: "trato de [usted / tú]" sin valor por defecto; para hablar en consulta a una persona a la que no se ha abordado el peso, usted por defecto.

**T7 · Lo que ya está bien y hay que conservar.** La etiqueta antes que el contenido en el Caso 2 (línea (0) "EJEMPLOS LIMPIOS / EJEMPLOS CON DATOS: BORRA ESTA CONVERSACIÓN" y "para"): aplicado T1 del capítulo 3 sin que hubiera que pedirlo. La escala ALTA / MEDIA / BAJA definida dentro de cada prompt que la usa, con las palabras de `biblia.md`. POR ACLARAR y [FALTA: …] definidos una vez en la frase introductoria y usados con su sentido. Rol en femenino en todos los prompts. "Unas 120 / 150 / 250 palabras" y no recuentos exactos. Los eslabones 2, 3 y 4 del Caso 3 sin rol ni contexto propios: es correcto, son mensajes de la misma conversación, y el capítulo lo dice ("una sola conversación nueva"). El ejemplo de salida del Caso 4, que es lo que devuelven los razonadores, incluido el "no lo sé cuál es" y la conclusión prematura sobre "el antidepresivo". La frase "cuando escribo esto: comprueba la versión vigente". Y la ficha del Caso 7 con "Historial" y "Datos que admite": es el mismo criterio que el inventario del capítulo 2.

**Frase introductoria** (sustituye desde "Cada caso trae situación" hasta "Las cifras son inventadas"; cambia lo justo):

> Cada caso trae situación, prompt literal (rol · contexto · tarea · formato · restricciones), ejemplo abreviado de salida, qué revisar y riesgo. Sustituye lo que va entre corchetes; ninguno admite datos identificables. Siguen las dos salidas del capítulo 3: POR ACLARAR, pregunta que contestas tú fuera del chat; [FALTA: …], hueco que rellenas tú fuera de la IA. Nunca dejes que el modelo rellene ninguno de los dos. Los casos 1 a 4 se hacen en conversación nueva, con la memoria desactivada ("chat temporal" o "incógnito") y se borran al terminar: el 2 porque tus textos nacen de cartas reales; el 3 porque su caso sintético nace de alguien que se sentó en tu silla; los demás porque el hábito de pegar casos tiene que nacer con la higiene puesta. Los seis prompts se pegan igual en Gemini, ChatGPT y Claude, cuando escribo esto: comprueba la versión vigente. El 4 pide razonador y trae la línea de rescate si tu plan no lo tiene; el 3 se hace entero en la misma conversación y con el mismo modelo, sin cambiar de desplegable a mitad de cadena; el 7 no usa IA. Las cifras son inventadas.

---

## Caso 1 · Prompt pobre frente a prompt estructurado · veredicto: MEJORAR (la comparación) · LISTO con retoques (el estructurado)

### Respuesta a la atención especial del ORQUESTADOR
¿Es honesta la comparación? El prompt pobre, sí: "Plan de ejercicio para una persona con obesidad y artrosis de rodilla" es exactamente lo que escribe una médica con tres minutos, y el gancho lo describe bien. La salida que se le atribuye en la Tercera parte, no. A esa línea ningún modelo de consumo de 2026 responde "Presenta claramente un síndrome metabólico con alto riesgo cardiovascular… necesitará mucha disciplina": no hay ningún caso ("presenta" ¿quién?), no hay datos que interpretar, y "disciplina" como regañina ha desaparecido casi por completo del registro de los tres modelos para obesidad. Peor: la rúbrica reprocha a esa salida "'ya ha fracasado con dietas previas' no estaba en el caso", pero en el prompt pobre no hay caso al que ser fiel. La lectora que haga el "Hazlo hoy" (paso 1) verá un folleto correcto y aburrido, no el texto del libro, y la primera vez que el libro le haya dicho algo comprobable le habrá mentido. Es el fallo más importante del capítulo, y no está en un prompt sino en el ejemplo de salida del prompt pobre, que es el otro término de la comparación. La comparación honesta es más útil (T1): el pobre no está mal, está vacío, y el modelo lo rellena con lo más probable.

### Checklist
| Criterio | Estructurado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco, en orden y con lo que protege al principio del formato y al final de las restricciones. |
| Anonimización | Caso sintético declarado dos veces; "no incluyas ni pidas datos de personas". Suficiente: no entra ningún dato. |
| Variables | No hay corchetes que rellenar salvo "[FALTA: …]" y "[n]": el caso es fijo. Correcto para un caso de demostración; conviene decir en "qué revisar" cómo se cambia el contexto para otra persona (en rangos, sin nombre). |
| Salidas cerradas | Tabla 4 × 3, regla en tres líneas, señales (máximo seis), pie literal, recuento final. Bien. El "[FALTA: …]" dentro de una hoja para el paciente es un cuerpo extraño: la hoja no debe llevar huecos; lo que el modelo necesite y no tenga va en POR ACLARAR, fuera de la hoja. |
| Portabilidad | Sin cambios. Gemini adorna la tabla con negritas y a veces emoticonos (hay que prohibirlos); ChatGPT y Claude, limpios. Al copiar la tabla a un Word, a veces se pierde: si pasa, pedir "en lista, no en tabla". |
| Ejemplo de salida | Realista: título, fila 1 con rangos, regla de las 24 horas, señales. Es lo que devuelven los tres. |
| Riesgo | Bien identificado (la hoja sustituye la conversación) y bien mitigado. Falta el paso previo obvio: la hoja va a una persona, luego pasa la lista del Anexo B. |

### Ejecución mental
- **Prompt pobre, los tres:** ver T1. Plan genérico de 5 bloques, 300-500 palabras, "consulte con su médico", 150 minutos semanales, "pérdida del 5-10 %", a veces paracetamol. Gemini lo empieza con "¡Claro! Aquí tienes…". Nada de "síndrome metabólico" ni "disciplina".
- **Estructurado, ChatGPT:** título de 6-8 palabras; tabla correcta con rangos ("2 × 8-10 min", "2 × 6-8 rep."); semana 4 con 2 × 15 min o 1 × 25 min; fuerza con silla, elevación de talones, extensión de rodilla sentado; agua de 10 a 25 min. Regla del dolor casi literal a la del ejemplo. Señales: hinchazón con calor, bloqueo, dolor torácico, mareo, falta de aire, dolor que no cede en 48 h. Unas 320 palabras (pide 250). Recuento 0, y es verdad. Añade a veces "consulte con su médico antes de empezar" al principio, que es lo que hay que prohibir.
- **Estructurado, Gemini:** igual, con negritas, un emoticono en el título en una de cada tres ejecuciones, y una frase "recuerde que la constancia es clave", que no está prohibida y suena a lo que el capítulo no quiere. En la semana 4 puede meter "subir y bajar un escalón" (aceptable) o "sentadillas" (no).
- **Estructurado, Claude:** el más pegado al formato y al recuento; escribe la hoja entera en usted; en la semana 1 pone "[FALTA: tolerancia al agua]" dentro de la tabla porque el contexto se lo permite: es el cuerpo extraño.
- Rúbrica sobre el estructurado: fidelidad alta; priorización correcta (rodilla y tiempo primero); calibración correcta (rangos, "suele", nada de "cura"); confusores: la hoja no los necesita; acción segura alta con la regla del dolor y las señales.

### Problemas
1. Salida del prompt pobre inventada; contradice el gancho y el "Hazlo hoy" (T1). Se sustituye por una salida realista y se reescribe la lectura con la rúbrica (cinco líneas; es texto expositivo, lo dejo redactado para el REDACTOR).
2. "[FALTA: …]" dentro de una hoja para la persona: sustituir por POR ACLARAR fuera de la hoja.
3. Falta prohibir "consulte con su médico antes de empezar" y las frases de ánimo ("la constancia es clave"), y prohibir emoticonos.
4. Contexto desalineado con el Caso 3 (mismo hombre): allí toma metformina; aquí "diabetes tipo 2" sin tratamiento. Con un tratamiento que no baja el azúcar de golpe, el modelo no necesita avisar de hipoglucemias; sin saberlo, algunos escriben "si toma insulina, lleve azúcar". Poner "con metformina" (la restricción "sin fármacos" sigue valiendo para la hoja) y que CLÍNICO confirme si quiere una señal de bajada de azúcar entre las de parar.
5. "Unas 250 palabras" con tabla, regla, señales y pie: los tres pasan de 300. "Unas 300" o "que quepa en una cara".
6. "Qué revisar" no manda la hoja por el Anexo B ni dice cómo se adapta el contexto a otra persona.

### Versión corregida

**Salida del prompt pobre** (sustituye la cita de la Tercera parte, "Una respuesta, leída con las cinco"; es lo que devuelven los tres modelos, abreviado):

> "Un programa de ejercicio para personas con obesidad y artrosis de rodilla debe combinar actividad aeróbica de bajo impacto (caminar, bicicleta estática, natación) 30-45 minutos al día, cinco días por semana, con ejercicios de fortalecimiento del cuádriceps. Una pérdida de peso del 5-10 % reduce de forma significativa la carga sobre la articulación, por lo que conviene combinarlo con una dieta hipocalórica. Consulte con su médico antes de comenzar cualquier programa de ejercicio."

Lectura con las cinco (sustituye las cinco viñetas):

> - **Fidelidad.** No hay caso, así que no puede ser infiel. Lo que hay es relleno: "5-10 %", "dieta hipocalórica", "cinco días por semana". Nadie se lo pidió; es lo más probable en internet.
> - **Priorización.** Lo primero es el peso y la dieta. Lo que pedí era el ejercicio con esas rodillas.
> - **Calibración.** "Debe", "de forma significativa", para todas las personas con obesidad y artrosis a la vez. Un texto sin nadie delante habla con la seguridad de quien no conoce a nadie.
> - **Confusores.** Nada sobre el dolor, ni cuánto aguanta caminando, ni qué toma. No lo sabe; tampoco lo pregunta ni deja el hueco.
> - **Acción segura.** Treinta a cuarenta y cinco minutos diarios con una marcha de veinte: deja de caminar a la semana. Y "consulte con su médico" en una hoja que le da su médica: la responsabilidad devuelta a quien ya la tiene.
>
> Veredicto: no sale. No se corrige, se rehace. No porque esté mal, sino porque no sabe nada. Con el prompt del caso 1.

**Prompt estructurado** (cambios: contexto alineado con el Caso 3; POR ACLARAR en vez de [FALTA] dentro de la hoja; sin "consulte con su médico", sin frases de ánimo, sin emoticonos; "unas 300 palabras"):

```
ROL: Eres médica de familia con formación en ejercicio terapéutico y en la obesidad como enfermedad crónica.

CONTEXTO: Atención Primaria en España, consultas de siete minutos. Caso sintético, sin ninguna persona real detrás: hombre de 60-65 años, obesidad de grado II, diabetes tipo 2 tratada con metformina, artrosis de ambas rodillas con dolor mecánico que limita la marcha a unos veinte minutos, jubilado hace poco, sin cardiopatía conocida, con un parque y una piscina municipal cerca. Quiero una hoja para entregarle y comentar en la próxima visita. No pidas ni supongas más datos: si necesitas algo que no está, no lo inventes ni lo pongas en la hoja; escríbelo al final en una lista "POR ACLARAR", que resuelvo yo.

TAREA: (1) Plan de actividad física de cuatro semanas, progresivo, que trate el ejercicio como parte del tratamiento de la artrosis y de la diabetes, no como forma de quemar calorías. (2) Tres tipos: caminar por tiempo y no por distancia, fuerza de piernas con el propio cuerpo o apoyado en una silla, y una opción en el agua. (3) Una regla de dolor sencilla: cuándo seguir, cuándo bajar, cuándo parar. (4) Señales para dejarlo y consultar.

FORMATO: Título de máximo ocho palabras. Tabla de cuatro filas (semanas) y tres columnas (caminar, fuerza, agua), con tiempos y repeticiones en rangos. Debajo, la regla de dolor en tres líneas y las señales para parar (máximo seis). Trato de usted, nivel de lectura de 12 años, unas 300 palabras, sin emoticonos. Al pie, en este orden y literal: "Si tiene dudas o algo no va bien, [FALTA: cómo contactar con la consulta]." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Después de la hoja, la lista "POR ACLARAR" si la hay. Última línea, literal: "CIFRAS DE PESO O CALORÍAS EN EL TEXTO: [n]".

RESTRICCIONES: Ningún objetivo de peso, ninguna cifra de kilos ni de calorías, ninguna dieta. Sin fármacos ni nombres comerciales. Sin "debería", sin culpa, sin "esfuerzo" ni "disciplina", sin frases de ánimo ("la constancia es clave", "usted puede"). No escribas "consulte con su médico antes de empezar": esta hoja se la da su médica. No digas que el ejercicio "cura" ni prometas resultados. Cada ejercicio tiene que poder hacerse con dolor de rodilla leve; si alguno no, no lo incluyas; sin sentadillas profundas ni escaleras en las dos primeras semanas. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale; añadir antes del recuento las dos líneas del pie:

> Si tiene dudas o algo no va bien, [FALTA: cómo contactar con la consulta].
> Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> POR ACLARAR: ¿sabe nadar o solo caminar en el agua?
> CIFRAS DE PESO O CALORÍAS EN EL TEXTO: 0

Añadir a "qué revisar" (una frase cada una): "La hoja va a una persona: pasa las diez preguntas del anexo B antes de imprimirla. Y para otra persona, cambia el contexto en rangos y sin nombre; si al escribirlo te viene una cara con apellidos, escribe el rango más ancho."

---

## Caso 2 · Que escriba como yo · veredicto: MEJORAR (leve)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Los ejemplos van en medio y etiquetados (EJEMPLO 1, 2, 3), que es donde deben ir. |
| Anonimización y comprobación humana previa | La mejor Situación del capítulo: texto plano y no archivo (metadatos), marcadores, lectura en voz alta, textos distintos entre sí. La línea (0) del formato comprueba y para. Higiene explícita en la frase introductoria (conversación temporal, borrado). |
| Variables con ejemplo por defecto | [tipo de texto] y [tema genérico] con ejemplo; [150] palabras; [usted (hoja impresa) / tú] con valor por defecto implícito. Falta la variable de contenido (T4). |
| Salidas cerradas | (0) etiqueta antes que contenido, ASÍ ESCRIBES, TEXTO NUEVO, POR ACLARAR, recuento de marcadores. Muy bien. |
| Portabilidad | Sin cambios. Tres textos de 150-300 palabras caben de sobra en los tres. Claude y ChatGPT devuelven ASÍ ESCRIBES más fino; Gemini tiende a describir "tono cálido y profesional" (adjetivos, no rasgos), que es justo lo que el capítulo dice que no sirve; pedir rasgos medibles ayuda. |
| Ejemplo de salida | Realista. "Frases de 8-14 palabras. Empiezas por lo que la persona ha hecho…" es lo que devuelven Claude y ChatGPT. |
| Riesgo | Bien identificado (el Word con propiedades) y bien mitigado. |

### Ejecución mental (tres textos anonimizados, hoja de primera visita, usted)
- **ChatGPT:** (0) correcta si los ejemplos están limpios; con un "[NOMBRE]" y una fecha "el 12 de marzo" escribe la segunda línea y para, en dos de tres ejecuciones; en la tercera para y aun así resume el estilo. ASÍ ESCRIBES en seis líneas, con rasgos concretos. TEXTO NUEVO: inventa el contenido ("Traiga la medicación que toma y sus últimas analíticas. Venga en ayunas por si hacemos analítica"). Recuento correcto.
- **Gemini:** ASÍ ESCRIBES con adjetivos ("cercano, empático, claro"); TEXTO NUEVO más largo (200 palabras) y con una despedida que no es de la lectora ("¡Estoy aquí para acompañarle!"); a veces rellena [FALTA: fecha] con "en las próximas semanas".
- **Claude:** el más fiel a la forma; deja [FALTA: …] donde toca; también inventa "venga en ayunas" porque la tarea lo pide y nadie le ha dado el contenido.
- Rúbrica: fidelidad media (contenido inventado por diseño); priorización no aplica; acción segura media-alta: "venga en ayunas" en una hoja de primera visita es un consejo individual que la lectora no dio (pregunta 6 del checklist, eliminatoria).

### Problemas
1. Contradicción entre TAREA (2) ("escribe una hoja sobre qué traer y de qué vamos a hablar") y RESTRICCIONES ("no añadas contenido clínico que no esté en los ejemplos o en la tarea"): el contenido no está en ninguno de los dos. Los tres inventan. Añadir un corchete con los puntos que la hoja debe contener (T4).
2. Aviso al pie fijo en usted con trato variable (T6). Pedir el aviso en el trato elegido, con las dos variantes.
3. Lista de (0) incompleta: añadir profesión concreta, DNI, teléfono, correo y dirección (los que el capítulo 3 ya enumera).
4. ASÍ ESCRIBES: pedir rasgos observables y prohibir adjetivos de tono, para que sirva de contexto reutilizable.
5. Gemini rellena marcadores con vaguedades ("en las próximas semanas"): la restricción "no rellenes ningún marcador" debe añadir "ni con aproximaciones".
6. "Qué revisar" dice que ASÍ ESCRIBES sirve de contexto para prompts futuros: decir dónde se guarda (la ficha del Caso 7, como bloque "CONTEXTO DE VOZ"), que es el puente natural entre los dos casos.

### Versión corregida

```
ROL: Eres una redactora que imita el estilo de otra persona a partir de ejemplos, sin inventar contenido.

CONTEXTO: Soy médica de familia en Atención Primaria en España. Te doy tres textos míos, anonimizados a mano: nombres, fechas, centro y cifras sustituidos por marcadores entre corchetes. No corresponden a ninguna persona concreta. Quiero un texto nuevo que suene a mí.

EJEMPLO 1 (carta con resultados):
[pega aquí el texto anonimizado]
EJEMPLO 2 (hoja de recomendaciones):
[pega aquí el texto anonimizado]
EJEMPLO 3 (mensaje breve):
[pega aquí el texto anonimizado]

TAREA: (1) Describe en máximo seis líneas cómo escribo, con rasgos que se puedan comprobar: longitud de frase, trato, cómo empiezo y cómo cierro, palabras y giros que repito, qué no hago nunca. Sin adjetivos de tono ("cercano", "empático"). (2) Con ese estilo, escribe [tipo de texto, por ejemplo: una hoja para la primera visita de obesidad] sobre [tema genérico, por ejemplo: qué traer y de qué vamos a hablar], sin ninguna persona detrás. El contenido es solo este, y no más: [puntos que debe contener, por ejemplo: traer la medicación que toma y las analíticas del último año; no hace falta venir en ayunas; hablaremos de su historia con el peso, de cómo duerme y de qué espera de la consulta; la visita dura unos veinte minutos]. Todo dato que no te haya dado va como [FALTA: …].

FORMATO, en este orden:
(0) Una línea: "EJEMPLOS LIMPIOS" o "EJEMPLOS CON DATOS: BORRA ESTA CONVERSACIÓN". Es la segunda si en los ejemplos queda un nombre o apellido, una fecha completa, un municipio, un centro, una profesión concreta, un DNI, un teléfono, un correo, una dirección o un número que parezca de historia; en ese caso, para: no escribas nada más.
(1) Bloque "ASÍ ESCRIBES".
(2) Bloque "TEXTO NUEVO", de unas [150] palabras, trato de [usted (por defecto en hojas impresas o enviadas) / tú], con la estructura del ejemplo más parecido. Al pie, literal y en el trato elegido: en usted, "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."; en tú, "Material informativo generado con apoyo de IA y revisado por tu profesional sanitario. No sustituye la valoración clínica individual."
(3) Lista "POR ACLARAR" con lo que no puedas deducir de los ejemplos; lo contesto yo fuera del chat.
(4) Última línea, literal: "MARCADORES SIN RELLENAR: [n]".

RESTRICCIONES: No añadas contenido clínico ni consejos que no estén en los puntos de la tarea: si un punto te parece incompleto, no lo completes; ponlo en POR ACLARAR. No rellenes ningún marcador, ni con aproximaciones ("en las próximas semanas"). Sin nombres comerciales, sin objetivos de peso, sin "obeso/a", sin frases de ánimo ni despedidas que no estén en los ejemplos. Imita la forma, no los datos. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale; en ASÍ ESCRIBES ya son rasgos comprobables. Añadir una línea a "qué revisar": "Copia ASÍ ESCRIBES a un bloque 'CONTEXTO DE VOZ' en tu biblioteca (caso 7): pegado al principio de cualquier prompt, te ahorra volver a pegar cartas. Y en el texto nuevo, cualquier consejo que no esté en tus puntos (un 'venga en ayunas' que tú no diste) se borra: es la pregunta 6 del anexo B."

---

## Caso 3 · La cadena de cuatro prompts · veredicto: MEJORAR (eslabones 2 y 4 reescritos; 1 y 3, retoques)

### Respuesta a la atención especial del ORQUESTADOR
**¿Impide la cadena que el eslabón 2 opine sobre fármacos concretos?** No. "No propongas tratamientos: la decisión es mía" es la frase correcta para una persona y la insuficiente para un modelo. En la ejecución mental con el caso del prompt 1, ChatGPT y Gemini escriben casi siempre un dilema del tipo "Control glucémico subóptimo con obesidad: la intensificación con fármacos que además reducen peso (agonistas del receptor de GLP-1) o con beneficio cardiorrenal (iSGLT2) sería la opción preferente según las guías (ALTA)", y otro "Perfil lipídico aterogénico en persona con diabetes; LDL por encima del objetivo (ALTA)", que es una indicación de estatina sin decir estatina. Claude lo evita en dos de tres ejecuciones y en la tercera escribe "sin proponer tratamiento, cabe señalar que las guías priorizan fármacos con beneficio ponderal". El modelo no lo vive como "proponer": lo vive como analizar. La nota al pie del caso promete "ninguno para la obesidad": hoy depende de la suerte. Y hay un segundo agujero: aunque no nombre nada, el modelo juzga el tratamiento que ya toma ("metformina en monoterapia insuficiente"), que es la decisión sobre la metformina que el capítulo dice que es de la lectora. La correa tiene que ir por nombre, por clase y por juicio sobre lo actual (T2), en los eslabones 2, 3 y 4, con un recuento que lo haga visible. Con esa regla, los tres modelos escriben "DECISIÓN TERAPÉUTICA: la toma la médica" y siguen; Gemini a veces añade "(ver guías)", que es inocuo.

**¿Impide que el eslabón 4 produzca un texto para la persona sin disclaimer ni red de seguridad?** El aviso de IA en usted está, literal, y los tres lo respetan. La red de seguridad no está (T3). El texto (B) manda a caminar dos ratos al día a un hombre con diabetes, dos rodillas con artrosis, una toma de 146/88 y sin segunda toma, y no dice qué hacer si le duele el pecho, se marea o la rodilla se hincha, ni cómo contactar antes de la próxima visita. Los modelos no lo añaden solos: ninguno de los tres pone una línea de alarma en (B) si no se le pide. Además, (B) nombra hallazgos que la médica aún no ha valorado ("el hígado y la tensión merecen una segunda mirada"): es aceptable si ella lo revisa, pero el prompt debería impedir que (B) nombre diagnósticos ("hígado graso", "hipertensión") o pruebas concretas, y limitar a "lo miraremos en la próxima visita". La viñeta del capítulo entrega ese texto (B) al hombre real, en usted y con firma: razón de más para que salga con las tres líneas fijas.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Eslabón 1: los cinco. Eslabones 2, 3, 4: solo tarea y formato, porque heredan rol, contexto y restricciones de la conversación: correcto, y es lo que enseña el caso. Falta decir en la Situación que no se cambia de modelo a mitad de cadena y qué hacer si la conversación se corta (volver a empezar por el 1). |
| Anonimización | Caso sintético declarado en cada eslabón que lo necesita; higiene en la frase introductoria (casos 1 a 4). Cifras en rangos ("en torno a 37", "60-65"). Nace de una persona real convertida en arquetipo: es lo que la regla 16 y la Situación exigen. |
| Variables | Ninguna: el caso es fijo. Adecuado para una demostración; "qué revisar" debería decir cómo se cambia (misma estructura, cifras en rangos o inventadas). |
| Salidas cerradas | Numeración continua, "HECHOS · HUECOS", "ALTA · MEDIA · BAJA", "CAMBIOS", "DATOS EN (A) QUE NO ESTÁN EN LOS HECHOS": es la mejor cadena de recuentos del libro. Falta el recuento de fármacos (T2) y una lista revisada al final del eslabón 3 para que el 4 tenga una sola fuente. |
| Portabilidad | Sin cambios de texto. Diferencias: ChatGPT puede activar el razonador en un eslabón y no en otro (más ruido); Gemini en conversación larga "olvida" la prohibición de "sugiere / indica" en el eslabón 1 si el contexto es muy largo (no es el caso). Los tres mantienen la numeración de hechos entre eslabones. |
| Ejemplo de salida | Realista en los cuatro. En el eslabón 2, "control glucémico por encima del objetivo habitual (ALTA)": es lo que escriben, y CLÍNICO puede querer matizar que el objetivo se individualiza a esa edad; sirve para "qué revisar". |
| Riesgo | Bien identificado (el rigor aparente de cuatro pasos). Falta el segundo: los fármacos por clase en el eslabón 2. |

### Ejecución mental (caso tal cual, una conversación por modelo)
- **Eslabón 1, los tres:** cuatro listas bien hechas, 12-14 hechos, 6-9 huecos. Fallos repetidos: "TSH 2,4 mUI/L" (unidad añadida, T4); "tensión arterial 146/88 mmHg (elevada)" en Gemini y a veces ChatGPT, que es interpretar; "hipertransaminasemia" como rótulo en Gemini. Con "sin calificar ninguna cifra ni agruparlas bajo un rótulo" desaparece.
- **Eslabón 2, los tres:** ver arriba. Sin la correa: fármacos por clase en dos de tres modelos. Con ella: siete dilemas, tres o cuatro en ALTA (glucemia, cifra de tensión aislada como cifra, triglicéridos), dos en MEDIA (hígado graso metabólico, cambio de patrón alimentario tras la jubilación), dos en BAJA (hipertensión como diagnóstico, apnea por la nicturia). Recuento correcto.
- **Eslabón 3, los tres:** SUPUESTOS y DEMASIADO SEGURO son buenos y parecidos al ejemplo. OTRA EXPLICACIÓN para la nicturia: próstata, glucosuria, apnea (a veces solo apnea). OMITIDO: alcohol, ideas de muerte y atracones aparecen si se le nombran, como hace el prompt; sin la lista entre paréntesis, uno de cada dos los omite. Ninguno reescribe la lista de dilemas porque no se le pide, y el eslabón 4 parte de una lista sin revisar y de una crítica sueltas: la ambigüedad se resuelve pidiendo (5) LISTA DE DILEMAS REVISADA.
- **Eslabón 4, los tres:** (A) de 100-130 palabras, con [FALTA: …] y certezas entre paréntesis; ChatGPT añade "valorar ajuste terapéutico" en "pendiente" (T2). (B) en usted, sin kilos ni "debería"; Gemini añade "¡Ánimo!" en una de tres; ninguno pone red de seguridad ni contacto; los tres ponen el aviso. Recuentos "0 · 0": verdad en Claude; en ChatGPT (A) lleva un "valorar ajuste" que no es un hecho pero tampoco lo cuenta.
- Rúbrica sobre (B): fidelidad alta; priorización bien (dos cosas concretas); calibración bien; confusores no aplican; acción segura media hasta que lleve las tres líneas.

### Problemas
1. Eslabón 2 nombra clases de fármacos y juzga el tratamiento actual; la nota al pie promete lo contrario (T2).
2. Eslabón 4 (B) sin red de seguridad ni contacto (T3); (B) nombra órganos y hallazgos sin filtro.
3. Eslabón 1: unidad de TSH ausente; calificativos ("elevada") y rótulos ("hipertransaminasemia") no prohibidos por su nombre; sin tope en LO QUE FALTA (Gemini escribe quince).
4. Eslabón 3: no produce la lista revisada que el 4 dice incorporar.
5. Situación: no dice "mismo modelo toda la cadena" ni qué hacer si se corta.
6. "Qué revisar": no manda (B) por el anexo B ni dice cómo se construye otro caso.

### Versión corregida

Añadir a la Situación, tras "Cuatro mensajes, en este orden.": "En la misma conversación y con el mismo modelo del desplegable de principio a fin; si se corta, se empieza por el 1. El caso sintético lo escribes con la historia clínica cerrada, en rangos, y con al menos dos cosas cambiadas respecto a cualquiera que recuerdes."

Prompt 1 · estructurar, sin opinar (cambios: unidad de TSH; calificativos y rótulos prohibidos por su nombre; tope en LO QUE FALTA):

```
ROL: Eres médica de familia con experiencia en obesidad. Esto es un ejercicio sobre un caso sintético; no hay ninguna persona real y no debes tomar ni proponer decisiones para nadie.

CONTEXTO: Caso inventado, con cifras verosímiles pero no reales: hombre de 60-65 años, jubilado hace pocos meses, obesidad de grado II (IMC en torno a 37, cintura en torno a 119 cm), diabetes tipo 2 de varios años con metformina, artrosis de ambas rodillas que limita la marcha a unos veinte minutos, sin cardiopatía conocida. Desde la jubilación come a deshoras y picotea por las tardes; se describe "aburrido, no triste"; se levanta dos veces por la noche a orinar. Tensión en consulta 146/88 mmHg, sin diagnóstico previo de hipertensión. Analítica reciente: glucosa en ayunas 142 mg/dl, HbA1c 7,6 %, LDL 131 mg/dl, triglicéridos 210 mg/dl, creatinina 1,0 mg/dl con filtrado estimado por encima de 60 ml/min, ALT 58 U/l, GGT 64 U/l, TSH 2,4 mU/l. No hay más datos.

TAREA: Ordena el caso sin interpretarlo. Cuatro apartados: ANTECEDENTES Y TRATAMIENTO; SITUACIÓN ACTUAL (lo que cuenta la persona, con sus palabras); EXPLORACIÓN Y ANALÍTICA (cada cifra con su unidad, tal como te la di); LO QUE FALTA (lo que una médica de familia querría saber y no está, máximo diez puntos, cada uno como [FALTA: …]).

FORMATO: Cuatro listas con numeración continua. Ni una frase con "sugiere", "indica", "compatible con", "probable", ni ningún diagnóstico nuevo, ni calificativos sobre las cifras ("elevada", "alta", "normal"), ni rótulos que las agrupen ("hipertransaminasemia", "dislipemia"). Última línea, literal: "HECHOS: [n] · HUECOS: [n]".

RESTRICCIONES: No opines, no agrupes cifras bajo el nombre de un síndrome, no añadas ni redondees datos ni unidades. Sin fármacos que no estén en el caso ni nombres comerciales. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Prompt 2 · analizar, con nivel de certeza (reescrito: la correa de fármacos y derivación, y su recuento):

```
Ahora, y solo ahora, analiza. Lista de DILEMAS, máximo siete, cada uno con: qué se deduce; de qué hechos numerados sale; certeza ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, con explicaciones o estudios discrepantes) o BAJA (plausible, no lo afirmaría sin comprobarlo); y qué punto de LO QUE FALTA lo cambiaría. Reglas: no nombres ningún fármaco ni clase de fármacos, ni el que ya toma ni otros; no digas si el tratamiento actual basta, sobra o debe cambiarse; no digas si hay que derivar. Si un dilema es "qué hacer con el tratamiento" o "a quién derivar", escríbelo solo como "DECISIÓN TERAPÉUTICA: la toma la médica" o "DECISIÓN DE DERIVACIÓN: la toma la médica", sin desarrollarlo. Última línea, literal: "ALTA: [n] · MEDIA: [n] · BAJA: [n] · FÁRMACOS O CLASES NOMBRADOS: [n]".
```

Ejemplo de salida corregido (sustituye al actual):

> 1. Control glucémico por encima del objetivo habitual (hechos 1, 2, 9, 10). ALTA. Lo cambiaría: hipoglucemias, adherencia [16]. 2. Transaminasas por encima del rango, atribuibles a hígado graso asociado a disfunción metabólica (hechos 4, 12). MEDIA. Lo cambiaría: alcohol [14]. 3. Una toma de 146/88 es una cifra por encima del umbral (ALTA); que sea hipertensión, BAJA hasta la segunda toma [17]. […] 6. DECISIÓN TERAPÉUTICA: la toma la médica. […] ALTA: 3 · MEDIA: 1 · BAJA: 2 · FÁRMACOS O CLASES NOMBRADOS: 0

Prompt 3 · criticar la propia respuesta (cambio: lista revisada al final, mismas reglas):

```
Revisa tu respuesta anterior como si la hubiera escrito otra persona. Cinco listas: (1) SUPUESTOS: qué diste por hecho sin que estuviera en los hechos; (2) DEMASIADO SEGURO: qué certeza bajarías y por qué; (3) OTRA EXPLICACIÓN: para cada dilema, una alternativa que no nombraste; (4) OMITIDO: qué no miraste (ánimo, ideas de muerte, sueño, atracones, alcohol, fármacos que ya toma y que cambian el peso, causas secundarias) y debería estar; (5) LISTA DE DILEMAS REVISADA: la lista anterior con los cambios aplicados, mismas reglas de certeza y de fármacos. Última línea, literal: "CAMBIOS QUE HARÍA EN LA LISTA DE DILEMAS: [n] · FÁRMACOS O CLASES NOMBRADOS: [n]".
```

Prompt 4 · comunicar, en doble salida (reescrito: (B) con las tres líneas fijas y sin diagnósticos ni pruebas; (A) sin juicio sobre el tratamiento):

```
Escribe dos textos con los mismos hechos, sin añadir ninguno, a partir de la LISTA DE DILEMAS REVISADA. (A) NOTA PARA EL EQUIPO: máximo 120 palabras, en el orden problema, datos, pendiente; huecos como [FALTA: …]; certezas entre paréntesis; sin propuesta ni valoración de tratamiento ni de derivación ("valorar ajuste" tampoco). (B) TEXTO PARA LA PERSONA: unas 120 palabras, trato de usted, nivel de lectura de 12 años: qué hemos visto en general (sin nombrar diagnósticos, órganos ni pruebas concretas: "hay un par de cosas que quiero mirar con calma"), qué vamos a hablar en la próxima visita y una cosa concreta para esta semana sobre el movimiento y el horario de las comidas; sin cifras de peso ni de kilos, sin fármacos, sin culpa, sin "debería", sin frases de ánimo. Al pie de (B), en este orden y literal: "Si tiene dudas o algo no va bien antes de vernos, [FALTA: cómo contactar con la consulta]. Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "DATOS EN (A) QUE NO ESTÁN EN LOS HECHOS: [n] · EN (B): [n] · FÁRMACOS O CLASES NOMBRADOS: [n]".
```

Ejemplo de salida corregido (sustituye al actual):

> **(A)** Persona con obesidad de grado II y diabetes tipo 2, HbA1c 7,6 % (ALTA). ALT 58, GGT 64 U/l (causa por aclarar, BAJA) [FALTA: alcohol, serologías]. TA 146/88 en una toma [FALTA: segunda toma]. Pendiente: ánimo con cribado, atracones, sueño, alcohol. DECISIÓN TERAPÉUTICA: la médica […]
> **(B)** Hemos visto que el azúcar está algo más alto de lo que nos gustaría y hay un par de cosas que quiero mirar con calma en la próxima visita; también hablaremos de cómo duerme, de cómo anda de ánimo y de las tardes. Esta semana le propongo dos cosas: caminar por tiempo, dos ratos cortos al día, y cenar a una hora fija. […] Si tiene dudas o algo no va bien antes de vernos, [FALTA: cómo contactar con la consulta]. Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> DATOS EN (A) QUE NO ESTÁN EN LOS HECHOS: 0 · EN (B): 0 · FÁRMACOS O CLASES NOMBRADOS: 0

Añadir a "qué revisar": "El recuento de fármacos lo compruebas con el texto delante: 'agonistas', 'inhibidores', 'estatina', 'ajuste del tratamiento' son un 1 aunque el modelo escriba 0. Las dos líneas del pie de (B), literales y enteras; el contacto lo pones tú en tu sistema. Y (B) va a una persona: anexo B antes de imprimir."

Riesgo principal, añadir una frase: "Y que el eslabón 2 te diga, con nombre de clase y en ALTA, lo que a ti te toca decidir con la guía en la mano: si aparece un fármaco, la cadena no ha fallado; ha hecho lo que hace internet. Lo tachas y sigues."

---

## Caso 4 · "No cierres diagnóstico" · veredicto: LISTO (retoque)

### Respuesta a la atención especial del ORQUESTADOR
**¿Fuerza "no lo sé" y la escala, sin cerrar diagnóstico?** La escala sí: definida dentro del prompt con las palabras de `biblia.md`, ligada a hechos numerados y con recuento ("EN ALTA: [n]") que "qué revisar" convierte en criterio ("aquí una ALTA es un error de calibración"): es el mejor uso de la escala en todo el libro. El cierre de diagnóstico está bien impedido por tres vías (tarea, restricciones y la lista 4 de conclusiones prematuras). El "no lo sé" está pedido pero no forzado: es una frase al final de la tarea ("si algo no se puede saber con lo que hay, escribe 'no lo sé'") sin sitio en el formato, así que los modelos la usan como comentario ("no lo sé cuál es") y el recuento "NO LO SÉ: [n]" cuenta cosas distintas en cada modelo: Claude cuenta hipótesis a las que no puede dar certeza (2), ChatGPT cuenta veces que escribió la frase (1-3), Gemini cuenta datos ausentes (7). Se arregla convirtiendo "NO LO SÉ" en cuarto valor de la certeza, definido: "NO LO SÉ (no puedo situarla ni en BAJA sin un dato; digo cuál)". Con eso, "Efecto del tratamiento nuevo: NO LO SÉ; hace falta el nombre del fármaco" es exactamente lo que se quiere leer, y el recuento significa lo mismo en los tres.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. El rol lleva el marco ("ejercicio de razonamiento… no debes tomar ni proponer decisiones"). |
| Anonimización | Caso sintético declarado; "no incluyas ni pidas datos de personas"; higiene en la frase introductoria. Correcto. |
| Variables | Ninguna: caso fijo. Correcto para entrenar el criterio; "qué revisar" debería decir cómo se cambia el caso (arquetipo compuesto, capítulo 2). |
| Salidas cerradas | Cuatro listas y recuento final. "Máximo ocho puntos cada una" rompe HECHOS: el caso tiene doce hechos (franja de edad, sin obesidad previa, diez kilos, menos de un año, sin cambios en comida, sin cambios en movimiento, cansancio, estreñimiento, edemas vespertinos, ánimo bajo, "desde que pasó todo", reglas irregulares, tratamiento nuevo sin nombre, sin exploración, sin analítica); el modelo fusiona y las inferencias pierden precisión al citar hechos. Sin tope en HECHOS; ocho en las demás. |
| Portabilidad | Depende del razonador. Claude y Gemini lo tienen en el desplegable; ChatGPT decide solo cuándo razonar y con este prompt razona casi siempre, pero no siempre. La línea de rescate del capítulo 2 ("Antes de responder, escribe tu razonamiento paso a paso; solo después las cuatro listas") debe viajar con el prompt como primera línea opcional entre corchetes. |
| Ejemplo de salida | El más realista del capítulo: siete hipótesis, ninguna en ALTA, hipercortisolismo en BAJA con lo que lo subiría, la conclusión prematura del "antidepresivo". Es lo que devuelve un razonador. Lo que casi ningún modelo pone y la lectora debe añadir: embarazo (mujer de 45-55 con reglas irregulares; raro, pero "no puede dejar de considerarse"), y que "edemas + estreñimiento + cansancio" no descartan una causa cardiaca solo porque no haya disnea. Es la "octava" del riesgo, bien traída. |
| Riesgo | Bien identificado (pegar a alguien real "porque es parecido"; anclarse a siete). |

### Ejecución mental (razonador de los tres)
- **Claude:** cuatro listas, 12 hechos, 7 hipótesis (hipotiroidismo MEDIA; fármaco MEDIA "sin saber cuál"; menopausia MEDIA; depresión MEDIA; atracón BAJA; cardiaca o renal BAJA; Cushing BAJA); pregunta por ideas de muerte en DATOS AUSENTES sin que se le pida (dos de tres veces). Conclusiones prematuras muy parecidas al ejemplo. "NO LO SÉ: 2".
- **ChatGPT:** igual; a veces pone hipotiroidismo en ALTA ("cuadro muy sugestivo"), que es lo que "qué revisar" caza. Añade "pruebas recomendadas: TSH, hemograma, glucosa, perfil lipídico, cortisol" como quinta lista no pedida: no es tratamiento, pero es un plan; la restricción "sin pruebas ordenadas como plan; lo que falta va en la lista 3" lo evita.
- **Gemini:** más largo; fusiona hechos por el tope de ocho; hipotiroidismo en ALTA con frecuencia; "no lo sé" casi nunca (prefiere "no es posible determinar"); recuento inconsistente.
- Rúbrica: fidelidad alta; priorización buena (fármaco y TSH primero en DATOS AUSENTES); calibración buena en Claude, floja en Gemini (ALTA); confusores: es el objeto del ejercicio, y lo cumple; acción segura alta (no hay decisión).

### Problemas
1. "No lo sé" sin sitio en el formato ni definición; recuento incomparable (T5).
2. Tope de ocho en HECHOS fusiona hechos y estropea la numeración.
3. Línea de rescate sin razonador fuera del prompt.
4. Quinta lista de pruebas no pedida (ChatGPT): prohibir por su nombre.
5. "Sin tratamientos" sin "ni clases de fármacos" (T2, leve aquí).
6. "Qué revisar": añadir el embarazo como ejemplo de la octava y cómo se cambia el caso.

### Versión corregida

```
[Si tu herramienta no tiene razonador, esta es la primera línea: "Antes de responder, escribe tu razonamiento paso a paso; solo después escribe las cuatro listas."]

ROL: Eres médica de familia. Esto es un ejercicio de razonamiento sobre un caso inventado; no hay ninguna persona real y no debes tomar ni proponer decisiones para nadie.

CONTEXTO: Caso sintético, sin correspondencia con nadie: mujer de 45-55 años, sin obesidad previa conocida, que ha ganado en torno a diez kilos en menos de un año sin identificar cambios claros en lo que come ni en lo que se mueve. Refiere cansancio, estreñimiento, piernas hinchadas al final del día, ánimo bajo "desde que pasó todo" (no concreta qué), reglas irregulares en el último año y un tratamiento nuevo desde hace unos meses cuyo nombre no consta. No hay exploración ni analítica. No hay más datos.

TAREA: No cierres ningún diagnóstico. Cuatro listas: (1) HECHOS: lo que está en el caso, numerado, sin adjetivos, sin fusionar dos hechos en uno. (2) INFERENCIAS: cada hipótesis que explicaría la ganancia de peso, con los hechos que la apoyan entre paréntesis y una certeza con uno de estos cuatro valores: ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, con explicaciones o estudios discrepantes), BAJA (plausible, no lo afirmaría sin comprobarlo) o NO LO SÉ (no puedo situarla ni en BAJA sin un dato; di cuál). Incluye las poco probables que una médica de familia no puede dejar de considerar, y di qué dato cambiaría cada una. (3) DATOS AUSENTES: qué falta, ordenado por lo que más cambiaría el razonamiento, sin inventarlo y sin convertirlo en una petición de pruebas. (4) CONCLUSIONES PREMATURAS: frases que alguien con prisa escribiría sobre este caso y que los hechos no sostienen, con una línea de por qué.

FORMATO: Cuatro listas; la 1 sin tope; las otras, máximo ocho puntos. Nada más que las cuatro listas. Última línea, literal: "HIPÓTESIS: [n] · EN ALTA: [n] · NO LO SÉ: [n]".

RESTRICCIONES: Sin diagnósticos cerrados, sin tratamientos ni clases de fármacos, sin nombres comerciales, sin plan de pruebas. No añadas datos al caso: si los necesitas, van en la lista 3. No atribuyas la ganancia a "hábitos" sin un hecho que lo sostenga. Usa "persona con obesidad" si procede. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: cambiar solo la hipótesis 2: "2. Efecto del tratamiento nuevo (hecho 8): NO LO SÉ; hace falta el nombre del fármaco." El resto vale, y el recuento "HIPÓTESIS: 7 · EN ALTA: 0 · NO LO SÉ: 1".

Añadir a "qué revisar": "La octava que casi nunca pone: con reglas irregulares a esa edad, el embarazo se descarta antes de pedir nada. Y para otro caso, la receta del capítulo 2: rasgos de varias personas, dos cosas cambiadas, historia clínica cerrada."

---

## Caso 5 · El consejo breve de siete minutos · veredicto: LISTO (retoque)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "Hablo yo; no es un texto para entregar" es la línea que hace bien el resto: sin aviso impreso, y el capítulo explica por qué. |
| Anonimización | "Sin ninguna persona concreta detrás"; "no incluyas datos de personas". No entra ningún dato. |
| Variables | [usted / tú] sin valor por defecto (T6). |
| Salidas cerradas | BASE + (a), (b), (c), tres partes marcadas, tope de palabras, recuento de palabras prohibidas. Bien. "Palabra prohibida" no incluye derivados: "esforzarse", "disciplinado", "con voluntad" pasan. |
| Portabilidad | Sin cambios. Los tres cumplen los 60 palabras; Gemini añade un cuarto bloque "consejos para la médica" que no se pide (prohibir "nada más que los cuatro bloques"). |
| Ejemplo de salida | Realista: "no falló usted, falló el método" es lo que devuelven Claude y ChatGPT; y es una frase que la autora podría decir. |
| Riesgo | Bien identificado (recitar) y bien mitigado. |

### Ejecución mental (usted)
- **Los tres:** BASE con dos frases del tipo "El peso no es una cuestión de voluntad: el cuerpo tiene mecanismos que lo defienden, y eso se puede tratar como cualquier otra enfermedad crónica"; pregunta abierta ("¿Le gustaría que lo habláramos con calma un día?"); paso ("Pido una cita en dos o tres semanas solo para esto"). (a), (b), (c) correctas; en (c), ChatGPT a veces desliza "hay técnicas de respiración que ayudan" pese a la restricción, en una de cuatro ejecuciones. Recuento 0 casi siempre, y es verdad; Gemini escribió "esforzándose" una vez y contó 0, porque no es la palabra exacta.
- Lo que falta en BASE, en los tres: pedir permiso. Nombran la enfermedad sin preguntar antes si la persona quiere hablar de eso, que es lo primero que enseña la entrevista motivacional y lo que evita que el consejo breve se viva como una emboscada al final de una visita por otro motivo. No lo hacen solos; hay que pedirlo. CLÍNICO puede confirmar la fórmula.
- Rúbrica: fidelidad alta; priorización correcta; calibración correcta ("puede", "muchas personas"); acción segura alta (lo dice la médica en persona).

### Problemas
1. Sin permiso antes de nombrar.
2. [usted / tú] sin valor por defecto.
3. Palabras prohibidas sin derivados ni "gordo/a"; el recuento se salta las variantes.
4. Bloques extra no pedidos (Gemini).

### Versión corregida (cambios mínimos, marcados en la tarea, el formato y las restricciones)

```
ROL: Eres médica de familia con formación en entrevista motivacional y en lenguaje centrado en la persona.

CONTEXTO: Atención Primaria en España, consultas de siete minutos. Intervención para decir en voz alta al final de una visita por otro motivo, a una persona con obesidad a la que aún no he ofrecido abordar el peso. Hablo yo; no es un texto para entregar. Sin ninguna persona concreta detrás.

TAREA: Una intervención con exactamente tres partes: dos frases, la primera pide permiso para hablar del peso y la segunda nombra la obesidad como enfermedad con biología detrás y sin culpa; una pregunta abierta que deje la decisión a la persona; y un siguiente paso pactado, pequeño, con fecha relativa ("en dos o tres semanas"). Después, tres variantes completas para cuando la persona responde: (a) "ya probé todo"; (b) "no tengo tiempo"; (c) "mi problema es la ansiedad".

FORMATO: Bloque BASE y bloques (a), (b), (c), cada uno con sus tres partes marcadas; máximo 60 palabras por bloque; trato de [usted (por defecto) / tú]; que pueda decirse en menos de treinta segundos. Nada más que los cuatro bloques. Última línea, literal: "PALABRAS PROHIBIDAS ENCONTRADAS: [n]".

RESTRICCIONES: Palabras prohibidas, incluidas sus variantes y derivados: "obeso/a", "gordo/a", "debería", "esfuerzo" (y "esforzarse"), "fuerza de voluntad" (y "voluntad"), "disciplina" (y "disciplinado"), "solo tiene que", "fácil". Sin objetivos de peso, sin dietas, sin fármacos ni nombres comerciales, sin promesas de resultado. En (c), no des consejo sobre la ansiedad ni técnicas: reconócela y abre la puerta a valorarla. No incluyas datos de personas.
```

Ejemplo de salida: el actual vale. Si el REDACTOR quiere mostrar BASE, una línea: "BASE. '¿Le parece si un día hablamos del peso? No es una cuestión de voluntad: hay una biología detrás, y se trata.' Pregunta: '¿Es algo que le preocupe a usted?' Paso: 'Si quiere, pido una cita en dos o tres semanas solo para eso.'"

---

## Caso 6 · Mensaje entre visitas · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿Salida sin identificadores?** Sí: el contexto dice "sin nombre, fechas ni cifras de nadie; lo que cambie por persona va como [FALTA: …]", la restricción "no rellenes ningún marcador" y "qué revisar" manda rellenar en el sistema. El ejemplo lo cumple. Lo que el prompt no cierra es qué marcadores se admiten: los modelos añaden "Hola, [FALTA: nombre]" y "[FALTA: fecha de la próxima visita]" (razonable) y, en "cómo contactar", inventan un teléfono o "responda a este mensaje" (T4). Lista cerrada de marcadores: paso pactado, fecha de la próxima visita, cómo contactar. El saludo, sin nombre: lo pone la lectora en su sistema.
**¿Variante usted del disclaimer?** Sí, literal y en usted (regla 11), y los tres modelos la ponen. La línea de seguridad de la regla 17 está literal, en usted y entera, con "o le llamo yo": es la primera vez que la red de seguridad del libro entra en un prompt tal cual, y está bien puesta. Dos grietas: "máximo 90 palabras" sin decir si el pie cuenta, así que ChatGPT y Gemini acortan la línea de seguridad para caber ("si se encuentra mal, acuda a urgencias"), justo lo que "qué revisar" avisa; y el mensaje (2) admite "coma poco y despacio, evite las grasas" y "no suba la dosis si no lo tolera" como "cómo contactar si hay dudas" ampliado: consejo sobre comida y dosis que la restricción solo cubre a medias ("sin consejo sobre dosis"; nada sobre comida).

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. |
| Anonimización | Correcta por diseño (plantillas genéricas). Marcadores no cerrados (T4). |
| Variables | Ninguna: dos situaciones fijas. Bien para el caso; "qué revisar" podría decir cómo se añade una tercera (misma estructura: reconocer, paso pactado, contacto, aviso). |
| Salidas cerradas | Dos mensajes, tope, pie literal, recuento doble. "FRASES QUE EVALÚAN" sin definir (T5). |
| Portabilidad | Sin cambios. Gemini pone emoticonos si no se le prohíbe (está prohibido) y negritas (no). |
| Ejemplo de salida | Realista, y muestra la línea de seguridad entera: bien elegido. "MARCADORES: 2": el segundo no se ve; con la lista cerrada, se sabe cuál es. |
| Riesgo | Bien identificado (enviar con el marcador; rellenarlo en el chat). |

### Ejecución mental (los tres)
- **(1) caminar:** "Han pasado dos o tres semanas desde que empezó a caminar por tiempo. Sea como haya ido, cuénteme cómo lo lleva en la próxima visita: [FALTA: paso pactado]…". ChatGPT añade "¡Enhorabuena por dar el paso!" (evalúa; y él cuenta 0). Gemini: "Estamos muy orgullosos de su compromiso" (evalúa y moraliza). Claude: limpio.
- **(2) tratamiento nuevo:** los tres ponen la línea; con el tope de 90 incluida la línea y el pie (unas 58 palabras entre las dos), les quedan 30 para el mensaje y dos de tres recortan la línea o el aviso. Consejos de comida en ChatGPT y Gemini ("coma despacio, porciones pequeñas"). Contacto inventado en los tres si no hay marcador.
- Rúbrica: fidelidad media (contacto inventado, consejos añadidos); priorización correcta (la línea de seguridad antes del paso pactado, como en el ejemplo); calibración correcta ("suelen ir a menos"); acción segura alta si la línea sale entera.

### Problemas
1. Contacto inventado: marcador cerrado (T4).
2. Tope de palabras que aplasta la línea de seguridad: "máximo 90 palabras sin contar las líneas literales".
3. "FRASES QUE EVALÚAN" sin definir (T5).
4. Consejos sobre comida y dosis en (2): prohibir los dos y decir por qué ("eso se dio en consulta").
5. Marcadores admitidos sin lista.
6. Negritas y saludos con nombre.

### Versión corregida

```
ROL: Eres una redactora de mensajes breves para pacientes de Atención Primaria, con conocimientos de lenguaje centrado en la persona.

CONTEXTO: Soy médica de familia en España. Quiero plantillas de mensaje de refuerzo entre dos visitas, para el canal del centro o para leer en una llamada. Son genéricas: sin nombre, fechas ni cifras de nadie. Solo se admiten tres marcadores, que relleno yo fuera de esta conversación: [FALTA: paso pactado], [FALTA: fecha de la próxima visita] y [FALTA: cómo contactar con la consulta]. Sin saludo con nombre: el saludo lo pongo yo. Dos situaciones: (1) persona con obesidad que acordó empezar a caminar por tiempo y lleva dos o tres semanas; (2) persona que ha empezado un tratamiento nuevo que puede dar molestias digestivas los primeros días, sin nombrar el tratamiento.

TAREA: Un mensaje por situación que: reconozca lo hecho sin calificarlo de éxito ni de fracaso; recuerde el siguiente paso como [FALTA: paso pactado]; y remita a [FALTA: cómo contactar con la consulta] si hay dudas. En (2), incluye literalmente y entera esta línea: "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo."

FORMATO: Dos mensajes de máximo 90 palabras cada uno sin contar las líneas literales, trato de usted, nivel de lectura de 12 años, sin emoticonos ni negritas. Al pie de cada uno, literal: "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "MARCADORES: [n] · FRASES QUE EVALÚAN: [n]", donde una frase que evalúa es cualquiera que califique lo hecho o a la persona ("enhorabuena", "muy bien", "orgullosos", "fenomenal", "una pena").

RESTRICCIONES: Sin felicitaciones ni mención de peso, balanza o cifras. Sin "debería", sin "ánimo, usted puede", sin culpa si no se ha cumplido. Sin nombres de fármacos ni comerciales, sin consejo sobre dosis ni sobre qué comer: eso se dio en consulta. No inventes teléfonos, correos ni "responda a este mensaje": el contacto es el marcador. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale, cambiando el cierre: "Lo que acordamos: [FALTA: paso pactado]. Si tiene dudas, [FALTA: cómo contactar con la consulta]. […] MARCADORES: 2 · FRASES QUE EVALÚAN: 0".

Añadir a "qué revisar": "Cuenta tú las palabras que evalúan: el modelo escribió 'enhorabuena' y contó cero más de una vez. Y si el mensaje (2) trae un consejo sobre comida o dosis, se borra: no es que esté mal, es que no lo diste tú."

Nota de coherencia (regla 12 de `biblia.md`): el mensaje (2) es, sin nombrarlo, un fármaco con molestias digestivas los primeros días. La nota al pie de transparencia del capítulo está en el Caso 3; como la regla es por capítulo, basta. Si COMPLIANCE prefiere una llamada en el Caso 6, una línea: "(ver nota ¹)".

---

## Caso 7 · Mi biblioteca de prompts en Markdown · veredicto: LISTO (retoque)

No es un prompt: es una ficha. Se revisa como plantilla, igual que el inventario del Caso 6 del capítulo 2.

### Respuesta a la atención especial del ORQUESTADOR
**¿Usable tal cual?** Sí: se copia a un bloc de notas, se rellena y funciona; los corchetes dicen qué poner; las marcas Markdown son las tres que el texto explica; el bloque anidado (cuatro acentos graves fuera, tres dentro) se lee bien en pantalla y, si la lectora no sabe qué es, puede ignorarlo y el texto sigue siendo una ficha. Un detalle de imprenta: en el libro impreso, los cuatro acentos graves de apertura no deben verse; el REDACTOR o el maquetador deciden si el bloque va con las marcas o como caja.
**¿Coherente con el Anexo A?** En lo esencial, sí. El índice fija para el Anexo A: nombre, momento, herramienta recomendada y por qué, texto literal en bloque de código con rol · contexto · tarea · formato, variables entre corchetes, nivel de riesgo (bajo / medio / alto) y qué revisar antes de usar la salida, más la instrucción de anonimización. La ficha tiene nombre, momento, herramienta y modelo, modo, para qué sirve, datos que admite, riesgo, prompt, ejemplo, qué revisar e historial. Le faltan cuatro líneas: (1) "Por qué esta herramienta" (el Anexo A lo lleva; y es lo que justifica "razonador" en el Caso 4 o "cualquiera" en el 5); (2) "Variables" (qué poner en cada corchete y un ejemplo: el Anexo A las lista y la ficha no tiene sitio); (3) "Probada por" con fecha (la mitigación del riesgo del propio caso dice "la firma de quien la probó", y la ficha no tiene dónde firmar); (4) "Higiene" (conversación nueva, memoria apagada, borrar al terminar: lo que la frase introductoria exige a los casos 1 a 4 y que la ficha debería recordar en cada prompt que lo necesite). Con esas cuatro líneas, los cincuenta prompts del Anexo A y los del capítulo caben en la misma ficha sin traducir nada. Y una precisión: "Datos que admite" y "Riesgo" ya cumplen lo del Anexo ("todos incluyen la instrucción de anonimización"), porque la instrucción va dentro del prompt; la ficha solo recuerda qué entra.

### Checklist
| Criterio | Estado |
|---|---|
| Campos con ejemplo | Sí; "Herramienta y modelo: leído en el desplegable" enlaza con el inventario del capítulo 2. |
| Salidas cerradas | Riesgo con tres valores y "qué pasa si se equivoca"; Historial con fecha, motivo y modelo. Bien. |
| Coherencia interna | La regla "versiona, no sobrescribas" pone la versión en el nombre del archivo (`consejo-breve-7min_v2.md`) y en el Historial: son dos sitios para lo mismo; no es un error, pero conviene decir cuál manda (el Historial dentro del archivo; el nombre solo la última). |
| Ejemplo | No hay ejemplo rellenado. Con una ficha rellenada de tres líneas (el Caso 5 del propio capítulo) el lector ve el uso; el REDACTOR decide si cabe. |
| Riesgo | Bien identificado (usar sin leer "qué revisar") y bien mitigado, si la ficha tiene dónde firmar. |

### Versión corregida (cuatro líneas nuevas, marcadas; el resto igual)

````markdown
# [Nombre corto del prompt]

- **Versión:** v1 · **Fecha:** AAAA-MM-DD
- **Herramienta y modelo:** [por ejemplo: Claude, modelo X · ChatGPT, modelo Y], leído en el desplegable
- **Por qué esta herramienta:** [una frase: cualquiera vale / necesita razonador / necesita archivos]
- **Modo:** chat / razonador
- **Momento:** consulta / seguimiento / administración / docencia / divulgación
- **Para qué sirve:** una frase.
- **Datos que admite:** ninguno identificable; sintéticos / anonimizados / agregados.
- **Higiene:** conversación nueva y memoria apagada: sí / no hace falta · borrar al terminar: sí / no
- **Variables:** [corchete → qué poner, con un ejemplo]
- **Riesgo:** bajo / medio / alto, y qué pasa si se equivoca.
- **Probada por:** [iniciales] · **Última prueba:** AAAA-MM-DD, con [modelo]

## Prompt
```
[texto literal, con las variables entre corchetes]
```

## Ejemplo de salida
[abreviado, sin datos de nadie]

## Qué revisar antes de usar la salida
- 
- 

## Historial
- v1 (AAAA-MM-DD): primera versión.
- v2 (AAAA-MM-DD): qué cambió, por qué y con qué modelo se probó.
````

Añadir a "qué revisar", una frase: "Sin 'Probada por' con fecha, la ficha no entra en la carpeta del centro: la firma es la mitigación." Y si el REDACTOR quiere un ejemplo rellenado, tres líneas del Caso 5: "consejo-breve-7min · v1 · cualquiera vale · chat · consulta · Datos: ninguno · Higiene: no hace falta · Riesgo: bajo (si se equivoca, suena a folleto; no llega escrito a nadie) · Probada por: CP, 2026-09-12".

---

## Notas para el REDACTOR (integrar sin alargar)

El capítulo está en 6.977 palabras y el tope real del libro ronda 6.800. Todo lo que propongo cabe sin sumar más de unas 150 palabras netas si se hacen estos cambios por sustitución, no por adición:

1. **Caso 1 (T1), la más importante.** Sustituir la cita de la salida pobre y las cinco viñetas de "Una respuesta, leída con las cinco" por las de este informe: mismo tamaño. En el prompt estructurado, cambiar tres frases (contexto, formato, restricciones) por las corregidas. Añadir dos líneas del pie al ejemplo. El gancho, el "Hazlo hoy" y el Caso 1 quedan contando lo mismo.
2. **Caso 3 (T2 y T3).** Sustituir los eslabones 2 y 4 por los corregidos (unas 60 palabras más entre los dos) y quitar, para compensar, una de las dos frases del riesgo principal actual que ya dice "qué revisar". Eslabón 1: tres retoques de palabra. Eslabón 3: añadir la lista (5), una línea. Sustituir los dos ejemplos de salida (2 y 4) por los corregidos, que son igual de largos.
3. **Caso 2 (T4, T6).** Sustituir TAREA (2), FORMATO (0) y (2), y RESTRICCIONES por las corregidas. Añade unas 40 palabras al prompt; se compensa quitando de la Situación la frase "Tú escribes de una manera; la máquina, como internet", que ya está dicha en la Segunda parte.
4. **Caso 4.** Cuatro retoques de una línea (rescate entre corchetes, valor NO LO SÉ, "la 1 sin tope", "sin plan de pruebas"). Ejemplo: cambiar la hipótesis 2 y el recuento.
5. **Caso 5.** Tres retoques de palabra en tarea, formato y restricciones.
6. **Caso 6 (T3, T4, T5).** Sustituir CONTEXTO, FORMATO y RESTRICCIONES por los corregidos (unas 50 palabras más); compensar quitando del "qué revisar" la frase sobre el canal (portal frente a WhatsApp), que el capítulo 3 ya fijó y aquí se puede citar en cuatro palabras: "el canal, capítulo 3".
7. **Caso 7.** Cuatro líneas nuevas en la ficha; nada más.
8. **Frase introductoria:** la corregida, misma longitud.
9. Si el ORQUESTADOR acepta T3 como regla de libro (tres líneas fijas en todo texto para la persona), conviene añadirla a `biblia.md` como regla 19 y aplicarla hacia atrás en el capítulo 1 (hoja del Caso 6) cuando toque la v4; no lo hago yo.

## Notas para otros agentes (no las resuelvo yo)
- **CLÍNICO:** (a) Caso 1: con metformina en el contexto, ¿quiere una señal de bajada de azúcar entre las señales para parar, o basta con "mareo"? (b) Caso 3, ejemplo del eslabón 2: "control glucémico por encima del objetivo habitual (ALTA)": el objetivo se individualiza a los 60-65 años; ¿lo deja como está y lo usa en "qué revisar", o cambia la certeza en el ejemplo? (c) Caso 4: embarazo como "octava" en "qué revisar"; y la línea de red de seguridad para el movimiento en (B) del Caso 3 ("dolor en el pecho, falta de aire o mareo"), ¿la fórmula es la suya? (d) Caso 5: la frase de permiso antes de nombrar la enfermedad.
- **COMPLIANCE:** (a) T3 como regla de libro (contacto como marcador, cuándo no esperar, aviso de IA), y si el orden importa. (b) Caso 6: si la mención implícita a un fármaco con molestias digestivas necesita llamada a la nota ¹ dentro del caso. (c) Caso 2: el aviso de IA al pie de una hoja que imita el estilo de la lectora: sigue siendo "generado con apoyo de IA", aunque el estilo sea suyo; conviene que lo diga el "qué revisar" en cuatro palabras.
- **EVIDENCIA:** nada en los prompts depende de una cita. Las referencias que rodean a los Casos 1, 4 y 5 (Bannuru, Moseng, Wharton, Aveyard, Miller, Kyle) no son de mi ámbito.

## Preguntas para Cristina
1. Caso 1: la salida del prompt pobre que aparece en el libro ("síndrome metabólico… disciplina") no es lo que devuelven hoy los asistentes; propongo sustituirla por el folleto real (kilos, calorías, 150 minutos, "consulte con su médico"), que es lo que describe tu gancho. ¿Tienes guardada una salida real de aquel día, sin datos, para usarla tal cual? Sería mejor que la mía.
2. Caso 3 (B) y Caso 6: propongo que todo texto que llegue a la persona termine con tres líneas fijas: cómo contactar (hueco que rellenas tú), cuándo no esperar ("urgencias o 112", con la fórmula de la regla 17 si hay tratamiento nuevo, o "dolor en el pecho, falta de aire o mareo" si hay movimiento) y el aviso de IA. ¿Es así como lo escribes tú en tus hojas, o prefieres una fórmula más corta para el 112?
