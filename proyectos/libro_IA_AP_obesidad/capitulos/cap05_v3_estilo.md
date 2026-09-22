# Capítulo 5 · Documentar mejor y más rápido

**Notas, interconsultas, informes y cartas sin perder la tarde.**

Son las tres. Me quedan once historias por cerrar y una interconsulta pospuesta dos semanas. La interconsulta sale en cuatro minutos: el perfil en rangos y la pregunta ya los tenía del capítulo 3; la máquina pone orden y huecos, yo pongo datos y firma. Las once historias, en veinte, con una plantilla mía; ninguna pasó por la máquina. Antes era la tarde entera; estimación mía, no un estudio.

Lo que importa no lo hago más deprisa: qué queda escrito lo decido yo. Lo que ya no hago es empezar en blanco.

*Como todas las escenas de consulta de este libro, es una composición de varias personas.*

## Lo que te vas a llevar

- Una plantilla que convierte tus apuntes en un borrador con huecos, y la interconsulta que se contesta.
- Ocho prompts, de la nota de consulta a la respuesta a una queja.
- Un cuadro con lo que entra hoy y lo que entraría con contrato. Lo que se documenta lo firmas tú.

---

## Primera parte · Lo que documentar te cuesta y por qué

Documentar es la parte de la consulta que nadie ve. En Estados Unidos, la mitad de la jornada de consulta va a la pantalla y al escritorio (Sinsky 2016); en Atención Primaria, casi seis horas de una jornada de once y media van a la historia clínica electrónica (Arndt 2017). En dos centros de Madrid, casi cuatro de cada diez minutos de la visita se iban mirando la pantalla (Pérez-Santonja 2017); mide otra cosa, la mirada en la visita, no el tiempo de documentar, y por eso no la comparo.

La tarde la conozco: la nota que dice "seguimiento, bien, cita" y no qué se acordó, la interconsulta sin pregunta, el informe a petición, la queja. Escribir no es lo difícil: lo difícil es decidir qué queda escrito.

---

## Segunda parte · Tres cosas que la máquina hace bien con texto y una que no

Con texto, un modelo de lenguaje hace tres cosas bien: **ordenar** (notas telegráficas en cuatro apartados), **resumir** (dos años en una cronología) y **cambiar de registro** (de nota a carta). No sabe qué pasó en la consulta y lo rellena con lo probable: "se realizó consejo dietético", "buena adherencia", "mejoría progresiva". Nada de eso sale de tus notas: sale de miles ajenas.

De ahí las dos reglas de todos los prompts del capítulo: lo que no está va como [FALTA: …], y ordenar no es interpretar. Pedir documentos así, con plantilla, huecos y firma, lo traigo de mi formación en IA; los documentos son de esta consulta.

---

## Tercera parte · Dónde se hace cada cosa

No dispongo de ninguna herramienta con acuerdo de tratamiento de datos, como casi nadie en Atención Primaria (capítulo 3). Todo se hace con herramientas de consumo, y la pregunta de cada documento no es "qué le pido", sino "qué entra":

| Documento | Hoy, en herramienta de consumo | Con contrato |
|---|---|---|
| Nota de consulta (1) | Notas de un caso sintético de cero | Tus notas; sigue siendo borrador |
| Interconsulta (2) | Perfil en rangos (capítulo 3, caso 7) y tu pregunta | Perfil con cifras y fechas |
| Informe a petición de la persona (3) | Plantilla sobre caso sintético | La plantilla con los datos |
| Informe hospitalario (4) | Un informe sintético | El informe real |
| Plan con enfermería (5) | Todo: no lleva datos de nadie | Igual |
| Resumen de evolución (6) | Tabla sintética; nunca la de una persona, ni "anonimizada" | La tabla real |
| Carta de resultados (7) | Plantilla y tu contexto de voz | La carta con la analítica |
| Respuesta a una queja (8) | El hecho en una línea, sin nombres | La queja, si el contrato lo cubre |

La anonimización a mano (capítulo 3, caso 1) no la sustituye nada de lo que aquí se pega. Con contrato, los mismos ocho prompts sirven con datos reales: cambia la columna, no la gramática. Los sistemas que escuchan la consulta y escriben la nota (Tierney 2024) llegarán con contrato y consentimiento; hoy, grabar la visita en una herramienta de consumo mete en ella a la persona y a ti.

---

## Ocho casos para documentar sin empezar en blanco

Mismo molde que en el capítulo 4; ninguno admite datos identificables. Dos salidas del capítulo 3: POR ACLARAR la contestas tú fuera del chat; [FALTA: …] lo rellenas tú fuera de la IA. Nunca dejes que el modelo rellene ninguno.

Los casos 2, 3 y 8 son documentos que firmas tú: sin línea de "generado con IA" ni el pie de las hojas para pacientes. Interconsulta e informe van entre profesionales; la respuesta a una queja llega a la persona por el circuito de atención al paciente, con su contacto, y no es material informativo. Tu firma es la responsabilidad (capítulo 3); si tu servicio de salud exige que conste la herramienta, consta.

Conversación nueva, memoria apagada, y se borran al terminar; el 2 y el 8 con más razón: el perfil nace de una persona y la queja fue de alguien. Hoy se pegan igual en Gemini, ChatGPT y Claude; comprueba la versión vigente. Ninguno pide razonador (capítulo 2). Ficha del capítulo 4, caso 7, con "Higiene: sí" en el 2 y el 8 y "Probada por" con fecha.

### Caso 1 · Notas sueltas → nota estructurada con [FALTA]

**Momento:** consulta. **Herramienta:** consumo, con notas de un caso sintético.

**Situación.** Lo que escribo en la visita no son frases: abreviaturas, cifras y flechas. Aquí entra ese desorden, con notas inventadas; a los diez casos, tus apuntes nacen ya ordenados. La salida es un borrador; la nota de tu historia la escribes tú (capítulo 10).

```
ROL: Eres médica de familia con experiencia en obesidad y en documentación clínica. Ejercicio con notas inventadas; no hay ninguna persona real.

CONTEXTO: Atención Primaria en España. Te pego las notas telegráficas de una visita de seguimiento de un caso sintético construido de cero, escritas como las escribo yo con prisa: abreviaturas, cifras sueltas, sin verbos. No son de ninguna visita real. Quiero un borrador ordenado que después completo yo; tú no escribes en ninguna historia. ESTRUCTURA DE LA NOTA: [S/O/A/P por defecto; o la de tu sistema, por ejemplo: motivo / exploración / juicio / plan].

NOTAS: [pega las notas del caso inventado; hoy, nunca las de una visita real, aunque no lleven nombre; por ejemplo: "seg obes gII. 3 sem caminando 20 min x4-5/sem. duerme mal, ronca, somnol tarde (dice pareja). TA 138/86. cint 104. no atrac. metformina ok. pdte analit. pregunta x rodilla. cita 1 m"]

TAREA: Ordena las notas en la estructura dada; en S/O/A/P: S (lo que cuenta la persona, con sus palabras; lo que "pregunta" se transcribe como pregunta, no como síntoma), O (exploración y cifras, exactamente como las escribí, sin añadir unidades ni marcarlas como hueco), A (solo lo que yo haya escrito como valoración; si no hay, "A: [FALTA: valoración de la médica]") y P (lo acordado y lo pendiente). Desarrolla cada abreviatura solo si es inequívoca; si no lo es, o si una palabra puede significar varias cosas ("ok", "bien", "±"), déjala tal cual seguida de "[FALTA: qué significa]". Un hueco es solo lo que mis notas anuncian y no completan ("pdte analit" → "[FALTA: cuál]"); no pidas lo que una nota ideal tendría y la mía no menciona. No interpretes: ni "sugiere", "compatible con" o "probable", ni diagnósticos nuevos, ni calificativos sobre cifras ("alta") o sobre conductas ("buena tolerancia", "regular", "adecuada", "sin incidencias", "cumple"), ni rótulos que agrupen datos ("sospecha de apnea").

FORMATO, en este orden:
(0) Una línea: "NOTAS SIN DATOS DIRECTOS" o "NOTAS CON DATOS DIRECTOS: BORRA ESTA CONVERSACIÓN" si hay nombre, fecha completa, número de historia, teléfono, municipio, centro o profesión; en ese caso, para.
(1) Los apartados, frases cortas, máximo 150 palabras, sin introducción ni comentario, sin negritas ni emoticonos.
(2) Lista "HUECOS", numerada.
(3) Última línea, literal: "HECHOS: [n] · HUECOS: [n] · FRASES QUE INTERPRETAN: [n]": un hecho es cada anotación de mis notas separada por punto; un hueco, cada [FALTA: …]; una frase que interpreta, cualquiera que deduzca lo que no estaba escrito (diagnóstico, causa, tendencia o calificativo); la tercera cifra tiene que ser 0.

RESTRICCIONES: No añadas datos, unidades, fechas ni tratamientos que no estén; no rellenes ningún hueco con lo "habitual". Sin nombres comerciales, sin objetivos de peso. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> NOTAS SIN DATOS DIRECTOS
> S. […] Pregunta por la rodilla [FALTA: qué pregunta]. O. TA 138/86. Cintura 104. A. [FALTA: valoración de la médica]. P. Metformina ok [FALTA: qué significa]. Pendiente analítica [FALTA: cuál]. Cita en 1 mes.
> HECHOS: 10 · HUECOS: 4 · FRASES QUE INTERPRETAN: 0

**Qué revisar antes de usarla.** Cuenta los hechos, uno por punto: doce con diez anotaciones es que partió o añadió. Busca "buena", "regular", "adecuada" y "tolerancia": si están, la máquina decidió lo que tu "ok" no decía. "Ronca" y "somnolencia" son tuyas; "sospecha de apnea", no: el cribado lo haces tú (STOP-Bang, Chung 2008; capítulo 8). "NOTAS SIN DATOS DIRECTOS" lo dice el modelo de lo que ve: unas notas reales sin nombre pasan el filtro y siguen siendo de alguien.

**Riesgo principal y mitigación.** Pegar las notas de alguien real "porque no llevan nombre": llevan a la persona. Mitigación: la columna del cuadro.

### Caso 2 · Interconsulta a la unidad de obesidad o a Endocrinología [AP]

**Momento:** seguimiento de crónicos. **Herramienta:** consumo, con el perfil en rangos del capítulo 3.

**Situación.** Se contesta la interconsulta que en veinte segundos dice qué pregunto, qué he hecho y qué pido; la que vuelve con "sigue control en su centro" no tenía pregunta. Continúa el caso 7 del capítulo 3: primera interconsulta; si la unidad ya la sigue, el prompt lo sabe.

```
ROL: Eres médica de familia con experiencia en obesidad y en redactar interconsultas que se leen y se contestan.

CONTEXTO: Atención Primaria en España. Te doy un perfil en rangos que ya pasó la revisión de privacidad y una pregunta formulada por mí. PERFIL: [por ejemplo: mujer de 40-50 años, obesidad de grado III, apnea del sueño tratada, tensión arterial tratada, varios intentos previos de tratamiento, candidata a valoración por la unidad, aún sin derivar]. PREGUNTA: [por ejemplo: si cumple criterios para valoración en la unidad y qué debe quedar hecho y documentado desde Atención Primaria antes]. DESTINATARIO: [unidad de obesidad / Endocrinología]. Quiero un BORRADOR que completaré, firmaré y registraré en mi sistema.

TAREA: Escribe la interconsulta con cinco apartados, en este orden: MOTIVO (una frase); PREGUNTA (la mía, literal); SITUACIÓN ACTUAL (solo lo que está en el perfil, en rangos y con sus palabras: los tratamientos y el seguimiento que el perfil nombra van aquí, sin dosis ni fechas); LO HECHO YA EN ATENCIÓN PRIMARIA (solo huecos: cada línea entera como "[FALTA: …]" con lo que la unidad querría saber, por ejemplo intervenciones y fechas, tratamientos con dosis, analítica reciente, cribados hechos; no escribas ninguna frase que afirme que algo se hizo, ni con un corchete al final); CRITERIO DE DERIVACIÓN, solo si es la primera interconsulta, exactamente así y nada más: "[FALTA: criterio que cumple según la guía; lo escribo yo]"; si la unidad ya la sigue, escribe "No procede: ya valorada por la unidad".

FORMATO, en este orden:
(0) Una línea: "PERFIL APTO" o "PERFIL NO APTO: BORRA ESTA CONVERSACIÓN" si hay nombre, fecha completa, municipio, centro, profesión, hospital de referencia, cifras con decimales o cualquier dato que no sea rango o categoría; en ese caso, para.
(1) La carta, máximo 200 palabras contando los huecos, sin encabezado, fecha, firma ni despedida.
(2) Lista "LO QUE AÑADIRÉ YO FUERA DE LA IA", numerada.
(3) Última línea, literal: "HUECOS: [n] · FÁRMACOS, CLASES O TÉCNICAS NOMBRADOS: [n]": el primero cuenta los [FALTA: …] de la carta; el segundo, cualquier fármaco o clase de fármacos y cualquier técnica quirúrgica concreta (bypass, gastrectomía vertical, balón); "cirugía bariátrica" como motivo y los tratamientos que el perfil nombra sin fármaco ("tratada", "presión positiva") no cuentan; tiene que ser 0.

RESTRICCIONES: No propongas fármacos ni cirugía; no cites criterios de derivación ni guías, tampoco entre paréntesis ni como ejemplo: los escribo yo. No traduzcas el grado de obesidad a cifras de IMC ni añadas ninguna cifra que el perfil no traiga. No rellenes ningún hueco, tampoco con acciones "habituales" ("se ha realizado consejo dietético"). No escribas en el documento ninguna línea de "generado con IA": lo firmo yo. Sin nombres comerciales. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> PERFIL APTO
> **MOTIVO.** Persona con obesidad de grado III y varios intentos previos de tratamiento; se solicita valoración en la unidad. […] **LO HECHO YA EN ATENCIÓN PRIMARIA.** [FALTA: intervenciones y fechas] · [FALTA: tratamientos con dosis] · [FALTA: analítica reciente] · [FALTA: cribados hechos]. **CRITERIO DE DERIVACIÓN.** [FALTA: criterio que cumple según la guía; lo escribo yo]
> HUECOS: 5 · FÁRMACOS, CLASES O TÉCNICAS NOMBRADOS: 0

**Qué revisar antes de usarla.** Una acción que no escribiste la inventó la máquina, casi siempre como hueco a medias: "Cribado de atracones [FALTA: resultado]" dice que se hizo; cada línea de "lo hecho ya" empieza por [FALTA o no vale. Lo que la unidad pregunta siempre y la máquina no sabe: tabaco, intentos previos con fechas y resultado, cribado de atracones y ánimo, alcohol, deseo de embarazo, horas de uso de la presión positiva, analítica con micronutrientes. Lo escribes tú, guía en mano, y el criterio de derivación con la edición delante (GIRO 2024; capítulo 8).

**Riesgo principal y mitigación.** Enviar la carta con un hueco sin rellenar, o rellenarlo "en el chat". Mitigación: recuento a mano. Y la del capítulo 3: si en tu cupo solo hay una persona así, el perfil no es apto; ensánchalo o llama a la unidad.

### Caso 3 · Informes a petición de la persona: discapacidad, servicio de prevención, mutua [AP]

**Momento:** administración. **Herramienta:** consumo, con plantilla sobre caso sintético.

**Situación.** El informe es de la persona: tiene derecho a él y decide a quién lo entrega (Ley 41/2002, art. 22; Código de Deontología 2022, art. 17.1). Qué pasa por esta plantilla:

- **Pasa:** el que te pide para entregarlo a alguien: valoración de la discapacidad (RD 888/2022), servicio de prevención, mutua. Tú describes función y tratamiento; grado, aptitud o incapacidad permanente los deciden ellos.
- **No pasa:** la incapacidad temporal: partes e informe complementario son modelos oficiales de tu sistema (RD 625/2014, modificado por el RD 1060/2022); a la inspección le contestas tú.
- **Lo que sabe la empresa:** la vigilancia de la salud es voluntaria salvo excepciones tasadas y confidencial; recibe si es apta, no por qué (Ley 31/1995, art. 22.1, 22.2 y 22.4). Quien trabaja de noche tiene además evaluación periódica y, con problemas de salud reconocidos, derecho a un puesto de día si lo hay (Estatuto de los Trabajadores, art. 36.4 [VERIFICAR]).

```
ROL: Eres médica de familia con experiencia en obesidad y en redactar informes clínicos en lenguaje funcional para lectores no sanitarios.

CONTEXTO: Atención Primaria en España. Una persona me pide un informe sobre su salud para [destinatario; por ejemplo: el servicio de prevención de su empresa / el equipo de valoración de la discapacidad / la mutua] con la finalidad de [finalidad; por ejemplo: valorar la adaptación de su puesto por turnos de noche y somnolencia diurna]. Quiero una PLANTILLA de borrador sobre un caso sintético, sin ninguna persona real: [caso; por ejemplo: persona de 40-45 años con obesidad de grado III y apnea del sueño con presión positiva, en seguimiento en Atención Primaria y en espera de valoración por una unidad especializada]. DIAGNÓSTICOS QUE CONSTAN, decididos con la persona: [por ejemplo: apnea del sueño]. Datos, diagnósticos codificados, fechas y firma los pongo yo fuera de la IA; el informe se lo entrego a la persona.

TAREA: Escribe el borrador con estos apartados, en este orden: A QUIÉN SE DIRIGE Y POR QUÉ (a petición de la persona, con la finalidad dada); DIAGNÓSTICOS (solo los que yo indique como necesarios para la finalidad, cada uno como "[FALTA: diagnóstico codificado y fecha]"; si indico la obesidad, nómbrala como enfermedad crónica, sin grado ni cifras: el grado va con el código, y lo pongo yo); TRATAMIENTO Y SEGUIMIENTO ACTUALES (solo lo que está en el caso, sin calificar cómo lo sigue; lo demás, [FALTA: …]); SITUACIÓN FUNCIONAL, tres líneas: qué puede hacer, qué le cuesta o no puede y desde cuándo, cada una entera como "[FALTA: limitación concreta observada o referida]"; la finalidad no es un dato clínico: no conviertas lo que dice ("somnolencia") en algo que la persona presenta; LO QUE SE ESPERA (revisiones previstas, como "[FALTA: fecha o plazo]", sin pronóstico); y la línea literal "Se emite a petición de la persona interesada, para la finalidad indicada."

FORMATO, en este orden:
(0) Una línea: "CASO SINTÉTICO" o "CASO CON DATOS DIRECTOS: BORRA ESTA CONVERSACIÓN" si hay nombre, fecha completa, empresa, puesto concreto, municipio o centro; en ese caso, para.
(1) El borrador, máximo 180 palabras contando los huecos, en tercera persona, sin encabezado, fecha ni firma.
(2) Lista "POR ACLARAR" con lo que decido yo (por ejemplo, qué pruebas recientes citar).
(3) Última línea, literal: "HUECOS: [n] · PALABRAS SOBRE ESTILO DE VIDA, VOLUNTAD O CUMPLIMIENTO: [n]": el segundo cuenta "hábitos", "estilo de vida", "dieta", "sedentarismo", "adherencia", "cumple", "no cumple", "esfuerzo", "voluntad", "se recomienda", "se aconseja" y "obeso/a", y tiene que ser 0.

RESTRICCIONES: Lenguaje funcional, nunca moral: nada sobre lo que la persona come, hace o "debería" hacer. Sin cifras de peso ni de IMC salvo que las dé yo; sin pronósticos ("se espera mejoría"); sin recomendaciones sobre el puesto ni sobre la aptitud, que decide el destinatario; sin fármacos ni nombres comerciales. No rellenes ningún hueco, tampoco con plazos "habituales". No escribas en el documento ninguna línea de "generado con IA": lo firmo yo. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> CASO SINTÉTICO
> **Diagnósticos.** [FALTA: diagnóstico codificado y fecha] (apnea del sueño). **Tratamiento y seguimiento.** Presión positiva nocturna [FALTA: horas de uso registradas]. En espera de valoración por una unidad especializada [FALTA: fecha de solicitud]. **Situación funcional.** Puede: [FALTA: limitación concreta observada o referida]. Le cuesta o no puede: [FALTA: …]. Desde: [FALTA: …]. […]
> HUECOS: 7 · PALABRAS SOBRE ESTILO DE VIDA, VOLUNTAD O CUMPLIMIENTO: 0

**Qué revisar antes de usarla.** La situación funcional la escribes tú con lo visto o lo contado: "me quedo dormida en el descanso de las cuatro". Si la máquina puso la somnolencia porque estaba en la finalidad, nadie la observó: hueco. Busca "sedentaria", "adherencia" y "se recomienda". Léelo con ella antes de firmar; qué diagnósticos constan lo decide ella. Lo que la finalidad no necesita no consta (RGPD, art. 5.1.c); nada de lo que consta puede ser falso (Código de Deontología 2022, art. 17.1).

**Riesgo principal y mitigación.** Un informe que juzga, o que decide por el destinatario ("no apta para turnos de noche"). Mitigación: el recuento y la lectura con ella: lo que se escribe sobre alguien se escribe con alguien.

### Caso 4 · Del informe hospitalario a mi lista de tareas [AP]

**Momento:** seguimiento de crónicos. **Herramienta:** consumo, con un informe sintético.

**Situación.** El gancho del capítulo 3 fue un alta real en un chat gratuito; aquí, un alta inventada de cirugía bariátrica. La lista de lo que suele quedar para Atención Primaria, para aplicarla a mano al informe real: suplementación de por vida y adherencia; analítica de micronutrientes a intervalos y después cada año, de por vida; tratamientos que cambian cuando cambia el peso, y uno que se evita tras un bypass, los antiinflamatorios; anticoncepción eficaz durante 12-18 meses, y no oral si la técnica es malabsortiva; alcohol; ánimo, con la pregunta por ideas de muerte; atracones y picoteo; apnea que reevaluar.

Y las señales tardías que el alta no suele nombrar: vómitos que duran o síntomas neurológicos (tiamina; urgencias), hipoglucemias tras las comidas, dolor cólico que va y viene, cansancio con anemia. Analítica y suplementos, en O'Kane 2020; el resto, en Mechanick 2020; todo, en la GIRO 2024.

```
ROL: Eres médica de familia con experiencia en obesidad y en el seguimiento compartido con el hospital.

CONTEXTO: Atención Primaria en España. Te pego un informe de alta SINTÉTICO, construido de cero para este ejercicio, sin ninguna persona real. Quiero extraer lo que queda para Atención Primaria; no quiero que valores si lo que dice es correcto.

INFORME: "Alta tras cirugía bariátrica (técnica no especificada) sin complicaciones inmediatas. Dieta progresiva por fases, con hoja entregada. Suplementación diaria con multivitamínico específico, calcio con vitamina D y vitamina B12, según pauta de la hoja. Heparina de bajo peso molecular, una inyección diaria durante diez días, que la persona se administra en casa. Retirada de puntos o grapas en su centro de salud a los 10-12 días. Control analítico a los 3, 6 y 12 meses: hemograma, hierro y ferritina, vitamina B12, folato, vitamina D, calcio y proteínas totales. Revisión en la unidad a las 6 semanas. Continúa presión positiva nocturna hasta nueva valoración por Neumología. Se suspende uno de los dos antihipertensivos que tomaba, con control de tensión en su centro de salud. Ante vómitos persistentes, dolor abdominal intenso, fiebre o intolerancia a líquidos, acudir a urgencias."

TAREA: (1) TAREAS PARA ATENCIÓN PRIMARIA: tabla con cuatro columnas: qué / cuándo / quién (medicina, enfermería o la persona) / frase del informe que lo encarga, copiada literal. Solo lo que el informe encarga o deja al centro de salud o a la persona: si no puedes copiar una frase del informe en la cuarta columna, la fila no existe. Si el informe no dice cuándo o quién, "[FALTA: …]". (2) SEÑALES DE ALARMA: las que el informe nombra, literales, y nada más. (3) LO QUE EL INFORME NO DICE: lo que una médica de familia querría saber y no está, máximo ocho puntos, cada uno como "[FALTA: …]" sin cifras, plazos ni recomendaciones dentro del hueco, y sin proponer qué hacer con ello.

FORMATO, en este orden:
(0) Una línea: "INFORME SIN DATOS DIRECTOS" o "INFORME CON DATOS DIRECTOS: BORRA ESTA CONVERSACIÓN" si hay nombre, número de historia, fecha completa, hospital, servicio con nombre de médico o cualquier dato que no sea clínico; en ese caso, para.
(1) Las tres listas, sin introducción ni comentario. Última línea, literal: "TAREAS: [n] · SEÑALES: [n] · HUECOS: [n] · FILAS SIN FRASE DEL INFORME: [n]": una tarea es cada fila de la tabla; una señal, cada síntoma de la lista 2; un hueco, cada [FALTA: …] de las tres listas; la última cifra tiene que ser 0.

RESTRICCIONES: No añadas dosis, pautas, analíticas, suplementos ni plazos que no estén en el informe; copia las pautas tal como están, sin completarlas; no digas si la pauta es suficiente ni si le falta algo; no nombres qué antihipertensivo se suspendió ni ningún fármaco por nombre comercial; no valores la técnica ni el resultado. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> INFORME SIN DATOS DIRECTOS
> **TAREAS.** Analítica · 3, 6 y 12 meses · [FALTA: quién la pide] · "Control analítico a los 3, 6 y 12 meses…". […] **SEÑALES DE ALARMA.** Vómitos persistentes, dolor abdominal intenso, fiebre, intolerancia a líquidos: urgencias. **LO QUE EL INFORME NO DICE.** [FALTA: técnica] · [FALTA: seguimiento analítico después del mes 12] · [FALTA: hierro] · [FALTA: quién renueva los suplementos y si los paga la persona]. […]
> TAREAS: 7 · SEÑALES: 4 · HUECOS: 11 · FILAS SIN FRASE DEL INFORME: 0

**Qué revisar antes de usarla.** La cuarta columna es la prueba: si la frase citada no está en el informe, la fila la puso la máquina. Las señales del alta son las de las primeras semanas; las de después las pones tú, y con vómitos que no paran o síntomas neurológicos no se espera a la analítica: urgencias. La analítica del alta está incompleta a propósito; lo que falta (PTH, función renal y hepática, zinc y cobre según la técnica, tiamina si vomita, y cada año de por vida) lo dice la guía, no la máquina.

En el informe real, en mi experiencia, el hueco más frecuente es el tratamiento que hay que bajar cuando baja el peso: lo decides tú, con la persona delante (capítulo 8).

**Riesgo principal y mitigación.** Que el prompt funcione tan bien con el informe sintético que el real acabe en el chat "solo esta vez". Mitigación: el informe real se lee con la lista impresa al lado.

### Caso 5 · Plan de cuidados compartido con enfermería [AP]

**Momento:** seguimiento de crónicos. **Herramienta:** consumo, sin ningún dato.

**Situación.** Mi circuito de obesidad cabe en cinco líneas; lo que no cabe es quién hace qué: cuándo ve enfermería a la persona, qué registra y cuándo me avisa. El prompt no lleva ningún dato y produce una propuesta, no el plan: el plan se firma en equipo.

```
ROL: Eres médica de familia con experiencia en obesidad y en organizar el seguimiento de enfermedades crónicas en equipo con enfermería.

CONTEXTO: Centro de salud en España. Quiero llevar a la reunión con enfermería una PROPUESTA de reparto del seguimiento de la persona con obesidad, para discutirla; no el plan definitivo. Sin ninguna persona: es un documento de organización. Mi circuito actual: [circuito; por ejemplo: primera visita médica con historia clínica completa y hoja informativa; segunda visita a los 15-20 días o al mes; seguimientos mensuales; analítica cuando toca según el tratamiento]. Lo que hace enfermería hoy: [por ejemplo: toma tensión y cintura, y peso si la persona lo acepta; refuerza la hoja informativa]. Recursos: [por ejemplo: consulta de enfermería de 15 minutos; sin consulta telefónica programada].

TAREA: (1) Convierte el circuito en una tabla de cuatro columnas: momento del seguimiento; qué hace medicina; qué hace enfermería; qué se registra (el dato, por ejemplo "tensión y cintura") y dónde, como "[FALTA: campo de nuestro sistema]". (2) Debajo, la lista "ENFERMERÍA AVISA A MEDICINA CUANDO", solo con las situaciones que yo te doy, copiadas tal cual y sin añadir ninguna: [criterios de aviso; por ejemplo: tensión por encima de [FALTA: umbral que fijemos]; molestias con un tratamiento nuevo; la persona refiere atracones, vómitos provocados, ánimo bajo o ideas de muerte (estas, el mismo día); hipoglucemias si lleva insulina o sulfonilurea; no acude a dos citas seguidas]. (3) Lista "PREGUNTAS PARA LA REUNIÓN": lo que la tabla no puede decidir sola, máximo seis, como preguntas abiertas a enfermería.

FORMATO: Título "PROPUESTA PARA DISCUTIR CON ENFERMERÍA". Tabla de máximo siete filas y exactamente cuatro columnas, y las dos listas; nada más. Sin frases sobre lo que "debe" hacer la persona. Última línea, literal: "FILAS: [n] · CRITERIOS DE AVISO: [n] · FRECUENCIAS, UMBRALES O CRITERIOS QUE YO NO DI: [n]": el segundo tiene que coincidir con los que yo di; el tercero tiene que ser 0.

RESTRICCIONES: No inventes frecuencias, umbrales ni protocolos que no te haya dado; si el circuito no dice cada cuánto, escribe "[FALTA: frecuencia]"; si un criterio trae un hueco, cópialo con el hueco. Sin pesajes obligatorios: el peso se mide si la persona lo acepta. Ninguna tarea de "educación en hábitos", "adherencia", "cumplimiento" ni "estilo de vida": el refuerzo es el de la hoja informativa que yo doy. Sin objetivos de peso, sin fármacos ni nombres comerciales, sin "obeso/a". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> **PROPUESTA PARA DISCUTIR CON ENFERMERÍA.** A los 15-20 días o al mes: medicina, segunda visita; enfermería, tensión y cintura, peso si la persona lo acepta; se registra tensión y cintura en [FALTA: campo de nuestro sistema]. […] **ENFERMERÍA AVISA A MEDICINA CUANDO:** [los cinco criterios, con su hueco].
> FILAS: 5 · CRITERIOS DE AVISO: 5 · FRECUENCIAS, UMBRALES O CRITERIOS QUE YO NO DI: 0

**Qué revisar antes de usarla.** Que los criterios de aviso sean exactamente los tuyos: la máquina añade "ganancia de peso" y convierte la consulta de enfermería en una balanza. Busca "hábitos", "adherencia" y "educación" en su columna: si están, le ha dado el papel de vigilar. El peso, con permiso, explicando para qué sirve si hay tratamiento o cirugía en el horizonte (capítulo 8).

**Riesgo principal y mitigación.** Que la tabla la escriba la máquina y la firme el equipo sin discutirla. Mitigación: sin reunión, no hay plan.

### Caso 6 · Resumen de dos años de evolución

**Momento:** seguimiento de crónicos. **Herramienta:** consumo, con tabla sintética.

**Situación.** Dos años de visitas de una persona, con fechas, cifras y tratamientos, son esa persona aunque quites el nombre: no entran en una herramienta de consumo, ni "anonimizados" (capítulo 3). Hoy ese resumen lo hago sin IA: seis líneas en la historia. La tabla inventada enseña lo que la máquina hace con una serie temporal: inventa tendencias y causas.

```
ROL: Eres médica de familia con experiencia en obesidad. Ejercicio con una tabla inventada; no hay ninguna persona real y no debes proponer decisiones para nadie.

CONTEXTO: Atención Primaria en España. Tabla de dos años de seguimiento de un caso sintético, con fechas relativas y cifras verosímiles pero no reales. TABLA: hombre de 55-60 años. Mes 0: primera visita; peso en rango 105-110 kg; HbA1c 7,4 %; TA 148/90 mmHg; metformina 1.700 mg/día (ya la tomaba). Mes 1: TA 144/88 (media de tomas en casa); se inicia enalapril 10 mg/día. Mes 3: peso 103-108; TA 132/82. Mes 6: HbA1c 7,0 %; peso 100-105. Mes 9: no acude. Mes 12: peso 100-105; TA 130/80; HbA1c 6,8 %. Mes 15: refiere dolor de rodilla; peso 102-107. Mes 18: HbA1c 7,1 %; TA 136/84. Mes 24: peso 104-109; HbA1c 7,3 %; TA 138/86; metformina y enalapril sin cambios. No hay más datos.

TAREA: (1) CRONOLOGÍA: una línea por mes de la tabla, en orden, solo con lo que está en la tabla; "no acude" se escribe "no acude", sin más. (2) QUÉ HA CAMBIADO ENTRE EL MES 0 Y EL MES 24: cada variable con valor inicial y final, sin adjetivos, sin causas y sin calcular diferencias entre rangos. (3) LO QUE NO SE PUEDE SABER CON ESTOS DATOS: lo que la tabla no permite afirmar (causas, efecto de un tratamiento, qué pasó en el mes 9, alimentación, sueño, ánimo). (4) LO QUE FALTA para que el resumen sirva, cada punto como "[FALTA: …]", máximo seis.

FORMATO, en este orden:
(0) Una línea: "TABLA SINTÉTICA" o "TABLA CON DATOS REALES: BORRA ESTA CONVERSACIÓN" si hay fechas de calendario en vez de meses relativos, pesos en cifra exacta en vez de rangos, edad exacta, nombre o número de historia; en ese caso, para.
(1) Las cuatro listas, unas 250 palabras en total. Última línea, literal: "HITOS: [n] · PALABRAS DE CAUSA O TENDENCIA EN LAS LISTAS 1 Y 2: [n]": un hito es cada mes de la tabla; se cuenta, solo en las listas 1 y 2, cada aparición de "tras", "desde que", "debido a", "gracias a", "a causa de", "por efecto de", "en respuesta a", "mejoría", "empeoramiento", "progresiva", "estable", "evolución", "tendencia", "control", "respuesta", "adherencia", "abandono", "pérdida" o "ganancia"; tiene que ser 0.

RESTRICCIONES: No digas si el tratamiento funciona ni si hay que cambiarlo; no nombres fármacos ni clases que no estén en la tabla, ni nombres comerciales; no atribuyas nada al peso ni al comportamiento de la persona; no redondees, no conviertas los rangos en cifras ni digas que el peso "bajó" o "subió" cuando los rangos se solapan. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> TABLA SINTÉTICA
> **CRONOLOGÍA.** Mes 0: peso 105-110 kg; HbA1c 7,4 %; TA 148/90; metformina 1.700 mg/día. […] **QUÉ HA CAMBIADO.** Peso: 105-110 → 104-109. HbA1c: 7,4 → 7,3 %. TA: 148/90 → 138/86. **LO QUE NO SE PUEDE SABER.** Por qué cambió cada cifra; si el enalapril explica la tensión; qué ocurrió en el mes 9. […]
> HITOS: 9 · PALABRAS DE CAUSA O TENDENCIA EN LAS LISTAS 1 Y 2: 0

**Qué revisar antes de usarla.** Busca "mejoría", "tras" y "control" solo en las dos primeras listas: si están, el recuento miente; en la tercera tienen que estar. Y lo que la tabla me enseña a mí, que la máquina tiene prohibido decir: dos años sin tocar el tratamiento con esas cifras, ninguna analítica de riñón, lípidos ni orina, un mes 9 sin llamada y una rodilla sin plan. No es un resumen: es una decisión pendiente (capítulo 8). Otra tabla se construye de cero; nunca la de alguien con dos cifras cambiadas.

**Riesgo principal y mitigación.** El único rojo del capítulo: pegar la tabla real "porque solo son cifras". Mitigación: la columna del cuadro, sin excepciones; hasta el contrato, tus seis líneas.

### Caso 7 · La carta de resultados que no alarma [AP]

**Momento:** consulta. **Herramienta:** consumo, con plantilla y tu contexto de voz.

**Situación.** Vuelve una analítica de control y la persona no tiene cita hasta dentro de tres semanas. Si tu sistema la muestra en el portal, ella la verá antes que tu carta, con los valores marcados (Ley 41/2002, art. 18): la carta no es la primera noticia; es la que dice qué hacer con lo ya visto. El tono, tu "CONTEXTO DE VOZ" (capítulo 4, caso 2). No toca síntomas ni tratamiento: dos de las tres líneas fijas; si la tuya toca alguno, las tres.

```
ROL: Eres una redactora de cartas breves para pacientes de Atención Primaria, que imita el estilo de la médica a partir de su contexto de voz.

CONTEXTO: Soy médica de familia en España. CONTEXTO DE VOZ: [pega tu bloque "ASÍ ESCRIBES" del capítulo 4; por ejemplo: frases de 8-14 palabras; usted; empiezo por lo que la persona ha hecho; cierro con un paso con fecha; nunca "debe"]. Quiero una PLANTILLA de carta para comunicar por escrito una analítica de control a una persona con obesidad, con un caso sintético y sin ninguna persona real. Lo que quiero decir, y nada más: [por ejemplo: gracias por hacerse la analítica; los resultados no necesitan ninguna acción antes de que nos veamos; hay un dato que quiero comentar con calma en la visita]. Lo que se deja para la visita: [por ejemplo: todo lo demás]. Cómo se cita: [por ejemplo: pida cita en las próximas tres semanas].

TAREA: Escribe la carta con el contexto de voz, en tres párrafos cortos: lo que la persona hizo; lo que se dice de los resultados, sin nombrar cifras, pruebas ni diagnósticos; y la cita. Todo dato que no te haya dado va como "[FALTA: …]".

FORMATO: Unas 100 palabras sin contar las líneas literales, trato de usted, nivel de lectura de 12 años, sin negritas ni emoticonos, sin saludo con nombre ni despedida ni firma (los pongo yo). Al pie, en este orden y literal: "Si tiene dudas, [FALTA: contacto del centro]." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Después, lista "POR ACLARAR" si la hay. Última línea, literal: "CIFRAS, PRUEBAS O DIAGNÓSTICOS NOMBRADOS: [n] · PALABRAS DE ALARMA O DE VALORACIÓN: [n]": se cuenta cada "urgente", "grave", "preocupante", "preocupe", "anormal", "alterado", "mal", "malo", "bien", "bueno", "normal", "normalidad", "esperado" y "pequeño"; los dos tienen que ser 0.

RESTRICCIONES: No nombres cifras, pruebas, órganos ni diagnósticos, aunque el caso los tenga: eso va en la visita. No digas que los resultados están bien, normales o dentro de lo esperado, ni anticipes cuál es el dato ni por qué: solo lo que te he dado. No menciones síntomas ni tratamientos. Sin objetivos de peso, sin fármacos ni nombres comerciales, sin culpa, sin "debería", sin frases de ánimo. No inventes teléfonos, correos ni "responda a esta carta": el contacto es el marcador. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> Gracias por hacerse la analítica cuando lo acordamos. […] Hay un dato que quiero comentar con calma en la visita. Le propongo que pida cita en las próximas tres semanas.
> Si tiene dudas, [FALTA: contacto del centro]. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> CIFRAS, PRUEBAS O DIAGNÓSTICOS NOMBRADOS: 0 · PALABRAS DE ALARMA O DE VALORACIÓN: 0

**Qué revisar antes de usarla.** "Hay un dato que quiero comentar" tranquiliza a unas y desvela a otras: si va a dormir mal tres semanas, la llamas. Un asterisco que va a ver: o lo nombras sin cifra en la variable ("lo del colesterol lo vemos en la visita") o la llamas. Busca "normal", "bien" y "preocupe": si están, la máquina ha valorado la analítica por ti.

Si añades un tratamiento nuevo, entra la tercera línea, literal y entre las otras dos, la del capítulo 4: "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112." Si añades síntomas o movimiento, la otra: "Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112." Sale por el canal del centro, con el contacto rellenado en tu sistema; antes, las diez preguntas del anexo B.

**Riesgo principal y mitigación.** Dar por carta un diagnóstico nuevo. Mitigación: el recuento a cero, contado por ti; por carta se tranquiliza y se cita, no se diagnostica.

### Caso 8 · Respuesta a una reclamación con calma

**Momento:** administración. **Herramienta:** consumo, con el hecho resumido en una línea.

**Situación.** La queja la escribió la persona, lleva su nombre y no se pega. La más frecuente que conozco en obesidad: hablar del peso sin que la persona lo pidiera; por eso el capítulo 4 pide permiso antes, y el capítulo 10 vuelve sobre el estigma (Rubino 2020). En la sanidad valenciana entra por el Servicio de Atención e Información al Paciente (SAIP; Decreto 2/2002; Orden 6/2018 [VERIFICAR número del DOGV]) y se contesta en un mes, con un informe interno que firma la dirección o la respuesta que firmas tú: el prompt sirve para los dos.

```
ROL: Eres médica de familia con experiencia en obesidad y en responder por escrito a quejas con respeto y sin ponerte a la defensiva.

CONTEXTO: Atención Primaria en España. Una persona ha presentado una queja por escrito en el servicio de atención al paciente. No te la pego: lleva su nombre. HECHO, en una línea y sin identificadores: [por ejemplo: una persona se queja de que en una visita por otro motivo se habló de su peso sin que lo pidiera]. LO QUE OCURRIÓ según lo recuerdo y consta en la historia: [dos líneas sin datos; por ejemplo: al final de la visita ofrecí hablar del peso en otra cita; la persona lo vivió como un juicio]. LO QUE QUIERO DECIR DE CÓMO TRABAJO: [una línea; por ejemplo: que en esta consulta hablar del peso se ofrece y no se impone, y solo sigue si la persona lo acepta; que la pregunta llegara sin que la pidiera es lo que quiero corregir]. LO QUE OFREZCO: [por ejemplo: una cita en la que ella decide de qué se habla, y que su preferencia conste en la historia]. Quiero un BORRADOR que revisaré, firmaré y entregaré por el circuito del centro.

TAREA: Escribe la respuesta con esta estructura, en este orden: (1) agradecimiento por la queja, una frase, sin adjetivos; (2) HECHOS: lo que ocurrió, solo con lo que te he dado, sin calificar a nadie; (3) LO QUE SE HIZO Y POR QUÉ: solo mi línea, sin negar ni discutir el malestar de la persona y sin afirmar que "siempre" se hace bien ni que esta vez se hizo bien; (4) LO QUE SE OFRECE: literal, lo que yo he dado; (5) cierre en una frase, con disposición a escuchar.

FORMATO, en este orden:
(0) Una línea: "HECHO SIN IDENTIFICADORES" o "HECHO CON DATOS: BORRA ESTA CONVERSACIÓN" si en lo que te he dado hay nombre, fecha completa, número de queja o de expediente, motivo de consulta concreto que señale a alguien, centro, municipio o profesión; en ese caso, para.
(1) La respuesta, máximo 150 palabras, trato de usted, sin encabezado, fecha, firma ni despedida, sin negritas ni rótulos.
(2) Última línea, literal: "DISCULPAS: [n] · JUSTIFICACIONES: [n] · FRASES SOBRE LA PERSONA: [n]": disculpa es cada "lamento", "siento", "disculpe", "disculpas", "perdone" o "perdón"; justificación, cada frase que explique mi conducta por la presión asistencial, el tiempo de consulta, la agenda, mi intención o "por su bien"; frase sobre la persona, cualquiera que diga cómo es o qué debería hacer (contar lo que sintió, con las palabras que te he dado, no cuenta); tienen que ser como máximo 1, 0 y 0.

RESTRICCIONES: No niegues lo que la persona sintió ni lo discutas. No culpes a la persona, a la agenda ni al sistema. No menciones peso en cifras, diagnósticos ni tratamientos. Sin "obeso/a". Sin promesas que no te haya dado: ni "tomaré medidas", ni "mejoraremos", ni "no volverá a ocurrir", ni "le aseguro". Sin adverbios en la disculpa ("sinceramente", "profundamente"). Ninguna línea de "generado con IA": la respuesta la firmo yo. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> HECHO SIN IDENTIFICADORES
> Gracias por escribir esta queja. En la visita, al terminar el motivo por el que acudió, se le ofreció hablar del peso en otra cita. Usted lo vivió como un juicio. En esta consulta, hablar del peso se ofrece y solo sigue si la persona quiere. Que la pregunta llegara sin que la pidiera es lo que quiero corregir. […]
> DISCULPAS: 0 · JUSTIFICACIONES: 0 · FRASES SOBRE LA PERSONA: 0

**Qué revisar antes de usarla.** Léela con la queja delante: si se quejó de dos cosas, contesta a dos. Busca "intención", "siempre" y "aseguro", las tres defensas del borrador. Si dice que se pide permiso siempre, y esta vez no se pidió, la persona leerá que mientes: lo que se hizo mal se dice. "Lamento" una vez, si es tuyo; "por su bien", nunca. Ofrece solo lo que existe en tu agenda. Si el SAIP pide informe interno, tercera persona y sin cierre; si pide la respuesta a la persona, sale con tu firma por el circuito del centro.

**Riesgo principal y mitigación.** Pegar la queja, o pedir a la máquina que "encuentre argumentos". Mitigación: una línea sin nombres; si ese hecho lo reconocería alguien en la sala de espera, hazlo genérico o escribe la respuesta sin la máquina; con daño o recorrido legal, tu colegio o tu servicio jurídico, no un chat.

---

## Caso ilustrativo, no real: arquetipo compuesto

> Esta viñeta combina las trayectorias documentales de varias mujeres con obesidad de grado III y apnea del sueño que esperan una valoración de cirugía bariátrica. La edad es aproximada; no se dan profesión, hospital, tiempos de espera ni cifras que permitan trazar a nadie; el trabajo a turnos es un rasgo elegido para el ejercicio del informe, no de nadie en concreto. Los tres borradores son los de los casos 2, 3 y 5: el 2 con un perfil en rangos que no es el suyo, el 3 y el 5 con los casos sintéticos de este capítulo.

Entre cuarenta y cuarenta y cinco años; obesidad de grado III, presión positiva por apnea del sueño desde hace más de un año, tensión tratada, en lista de espera de la unidad. Un mes en el que todo el papel llega a la vez: la unidad, su empresa y enfermería.

La interconsulta es el caso 2, y no es la primera: la unidad ya la sigue. La máquina me dio los huecos, mi pregunta sin tocar y, en el criterio de derivación, "No procede: ya valorada por la unidad". Lo demás, yo, desde mi sistema: analítica con micronutrientes y fecha, tensión de tres meses, tabaco, intentos previos, cribados, horas de uso del equipo. Diez minutos, si no me engaño.

El informe es el caso 3, y es suyo antes que mío. "Doctora, en el trabajo solo quiero que sepan que me duermo, no por qué." Lo escribimos juntas. Antes, dos cosas que no son papel: cuántas horas marca el contador de su equipo y si alguna vez se ha dormido al volante volviendo del turno.

Una somnolencia con más de un año de presión positiva no se documenta sin mirarla: pido el registro del equipo, la vuelvo a mandar a la unidad de sueño y, hasta que lo veamos, conducir después de la noche, no; la apnea con somnolencia condiciona el permiso de conducir (RD 1055/2015, anexo IV [VERIFICAR]). Eso también queda escrito.

Del informe, a su empresa solo le llega si es apta o con qué límites, no el diagnóstico; aun así, ella decide qué consta: la apnea y su tratamiento, lo que la finalidad necesita; el porqué, no. Nada falso consta; nada que ella no quiera y no haga falta consta. Lo firmo, lo registro y se lo doy a ella: a quién se lo entrega es cosa suya.

El plan con enfermería es el caso 5, sin una línea de ella. Dos visitas de enfermería por cada una mía, lo que ese equipo puede darle este año, no un estándar; tensión y cintura cada vez, peso solo si ella lo acepta, y aviso si aparecen atracones, vómitos provocados o ánimo bajo mientras espera, el mismo día si hay ideas de muerte.

Tres veces no empecé en blanco; lo que ella iba a leer lo escribí yo. Y la frase de siempre: nada que permita saber quién es usted entra nunca en esas herramientas. La lista de espera no la acorta un prompt. Lo que sí puedo es que, cuando la llamen, todo esté escrito, y que la espera sea tratamiento y no cola (capítulo 8). No es falta de voluntad. Es biología, y es una espera; las dos cosas se acompañan.

---

## En 60 segundos

1. Documentar es decidir qué queda escrito; eso no lo hace la máquina: hace que no empieces en blanco.
2. Ordena, resume y cambia de registro; no sabe qué pasó. Todo hueco es [FALTA: …]; ordenar no es interpretar.
3. Una interconsulta se contesta si tiene pregunta, lo hecho y lo que pide.
4. Hoy entran plantillas, casos sintéticos de cero y texto anonimizado a mano; con contrato, datos reales.
5. Nota, carta, informe o respuesta: los completas, los firmas y los registras en tu sistema; el chat se borra.

## Hazlo hoy · 10 minutos

1. **(3 min)** Inventa diez líneas de notas de un caso que no existe y pásalas por el caso 1; cuenta los puntos tú.
2. **(3 min)** Corre el caso 2 con el perfil apto del capítulo 3; ningún hueco se rellena en el chat.
3. **(2 min)** Guarda los dos con la ficha del capítulo 4: v1, fecha, modelo, "Higiene: sí" en el 2, tus iniciales en "Probada por".
4. **(2 min)** Abre la interconsulta que llevas posponiendo y escribe solo la pregunta.

Mañana, a las tres, volverán a quedar once historias. La máquina no va a leer ninguna. Lo que quede escrito será tuyo, con tu firma debajo.

---

## Referencias

**Carga de documentación y tiempo de consulta**

1. Sinsky C, Colligan L, Li L, Prgomet M, Reynolds S, Goeders L, et al. Allocation of physician time in ambulatory practice: a time and motion study in 4 specialties. Ann Intern Med. 2016;165(11):753-60. doi:10.7326/M16-0961
2. Arndt BG, Beasley JW, Watkinson MD, Temte JL, Tuan WJ, Sinsky CA, et al. Tethered to the EHR: primary care physician workload assessment using EHR event log data and time-motion observations. Ann Fam Med. 2017;15(5):419-26. doi:10.1370/afm.2121
3. Pérez-Santonja T, Gómez-Paredes L, Álvarez-Montero S, Cabello-Ballesteros L, Mombiela-Muruzabal MT. Historia clínica electrónica: evolución de la relación médico-paciente en la consulta de Atención Primaria. Semergen. 2017;43(3):175-81. doi:10.1016/j.semerg.2016.03.022
4. Tierney AA, Gayre G, Hoberman B, Mattern B, Ballesca M, Kipnis P, et al. Ambient artificial intelligence scribes to alleviate the burden of clinical documentation. NEJM Catal Innov Care Deliv. 2024;5(3). doi:10.1056/CAT.23.0404

**Marco legal y deontológico de informes, certificados y quejas**

5. Ley 41/2002, de 14 de noviembre, básica reguladora de la autonomía del paciente y de derechos y obligaciones en materia de información y documentación clínica. BOE núm. 274, de 15 de noviembre de 2002. Arts. 18 y 22.
6. Ley 31/1995, de 8 de noviembre, de prevención de Riesgos Laborales. BOE núm. 269, de 10 de noviembre de 1995. Art. 22, apartados 1, 2 y 4.
7. Real Decreto Legislativo 2/2015, de 23 de octubre, por el que se aprueba el texto refundido de la Ley del Estatuto de los Trabajadores. BOE núm. 255, de 24 de octubre de 2015. Art. 36.4 [VERIFICAR].
8. Real Decreto 625/2014, de 18 de julio, por el que se regulan determinados aspectos de la gestión y control de los procesos por incapacidad temporal en los primeros trescientos sesenta y cinco días de su duración. BOE núm. 176, de 21 de julio de 2014. Modificado por el Real Decreto 1060/2022, de 27 de diciembre.
9. Real Decreto 888/2022, de 18 de octubre, por el que se establece el procedimiento para el reconocimiento, declaración y calificación del grado de discapacidad. BOE núm. 252, de 20 de octubre de 2022.
10. Real Decreto 1055/2015, de 20 de noviembre, por el que se modifica el Reglamento General de Conductores. BOE núm. 289, de 3 de diciembre de 2015. Anexo IV [VERIFICAR].
11. Reglamento (UE) 2016/679, general de protección de datos (RGPD). Art. 5.1.c.
12. Consejo General de Colegios Oficiales de Médicos. Código de Deontología Médica. Madrid: CGCOM; 2022. Arts. 17.1 y 17.2 (informes y certificados; certificados de complacencia) [VERIFICAR numeración en el PDF oficial].
13. Decreto 2/2002, de 8 de enero, del Gobierno Valenciano, por el que se crean los Servicios de Atención e Información al Paciente (SAIP). DOGV núm. 4167, de 14 de enero de 2002.
14. Orden 6/2018, de 13 de septiembre, de la Conselleria de Sanidad Universal y Salud Pública, por la que se regula el procedimiento de presentación y tramitación de las sugerencias, quejas y agradecimientos en el ámbito de las instituciones sanitarias dependientes de la conselleria con competencias en materia de sanidad. DOGV de 24 de septiembre de 2018 [VERIFICAR número de DOGV].

**Obesidad, cirugía bariátrica y apnea del sueño**

15. Sociedad Española para el Estudio de la Obesidad (SEEDO). Guía Española GIRO: Guía española del manejo Integral y multidisciplinaR de la Obesidad en personas adultas. 2.ª ed. Lecube A, coordinador. Madrid: SEEDO; noviembre de 2024. Disponible en: https://www.seedo.es/images/site/giro/GUIA-GIRO-2a-edicin_26NOV2024.pdf [VERIFICAR ISBN en créditos del PDF; candidato 978-84-09-65969-2]
16. Mechanick JI, Apovian C, Brethauer S, Garvey WT, Joffe AM, Kim J, et al. Clinical practice guidelines for the perioperative nutrition, metabolic, and nonsurgical support of patients undergoing bariatric procedures – 2019 update: cosponsored by American Association of Clinical Endocrinologists/American College of Endocrinology, The Obesity Society, American Society for Metabolic & Bariatric Surgery, Obesity Medicine Association, and American Society of Anesthesiologists. Surg Obes Relat Dis. 2020;16(2):175-247. doi:10.1016/j.soard.2019.10.025
17. O'Kane M, Parretti HM, Pinkney J, Welbourn R, Hughes CA, Mok J, et al. British Obesity and Metabolic Surgery Society guidelines on perioperative and postoperative biochemical monitoring and micronutrient replacement for patients undergoing bariatric surgery: 2020 update. Obes Rev. 2020;21(11):e13087. doi:10.1111/obr.13087
18. Chung F, Yegneswaran B, Liao P, Chung SA, Vairavanathan S, Islam S, et al. STOP questionnaire: a tool to screen patients for obstructive sleep apnea. Anesthesiology. 2008;108(5):812-21. doi:10.1097/ALN.0b013e31816d83e4

**Estigma**

19. Rubino F, Puhl RM, Cummings DE, Eckel RH, Ryan DH, Mechanick JI, et al. Joint international consensus statement for ending stigma of obesity. Nat Med. 2020;26(4):485-97. doi:10.1038/s41591-020-0803-x

