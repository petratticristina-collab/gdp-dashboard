# Capítulo 4 · Hablar con la IA

**Rol, contexto, tarea, formato: la gramática que cambia el resultado.**

Son las 11:20. Acaba de salir un hombre de sesenta y pocos años, jubilado desde la primavera, con obesidad de grado II, diabetes tipo 2 y las dos rodillas gastadas. "Ahora tengo tiempo, doctora, pero no sé por dónde empezar." Le he prometido una hoja con ejercicio para la próxima visita. Tengo tres minutos.

Escribo en el chat: "plan de ejercicio para obesidad y artrosis de rodilla". Me devuelve lo mismo que un folleto de gasolinera: camine treinta minutos, evite el sedentarismo, consulte con su médico. Y una línea que no pedí: "un objetivo realista es perder el 5-10 % del peso". Borro. Escribo otra vez, ahora con quién quiero que sea, para quién es, qué necesito, cómo lo quiero y qué no puede decir. Tarda lo mismo. Lo que vuelve es algo que puedo corregir y darle esa tarde.

La diferencia no estaba en la máquina. Estaba en lo que le pedí. Este capítulo es esa diferencia.

*Como todas las escenas de consulta de este libro, es una composición de varias personas.*

## Lo que te vas a llevar

- Una gramática de cinco piezas (rol, contexto, tarea, formato, restricciones) y el mismo encargo escrito mal y bien, lado a lado.
- Tres técnicas que bastan: tus textos como ejemplo, pedir los pasos por escrito y encadenar cuatro prompts en vez de pedir uno imposible.
- Cinco preguntas para leer cualquier respuesta antes de fiarte de ella, y siete casos sin datos identificables.

---

## Primera parte · La gramática: cinco piezas

### Un prompt es una interconsulta

Cuando escribes a un compañero de segundo nivel no pones "paciente con obesidad, ¿qué hago?". Pones quién eres, qué sabes, qué necesitas y para cuándo. Con la máquina pasa lo mismo, con una diferencia. El compañero rellena los huecos con experiencia y te llama si duda. El modelo los rellena con lo más probable y no llama a nadie: es la máquina de completar frases del capítulo 2.

Por eso "dieta para adelgazar" devuelve un folleto. Un prompt pobre no es un prompt erróneo. Es un prompt que deja todas las decisiones a la estadística. Y la estadística de internet, en obesidad, está llena de culpa, de kilos objetivo y de marcas.

### Las cinco piezas

Los prompts de este libro siguen siempre el mismo molde:

- **ROL.** Quién quieres que sea: "médica de familia con experiencia en obesidad", "redactora de textos para pacientes". Cambia el vocabulario y lo que da por supuesto. Nunca "el médico que trata a este paciente": el rol es de quien escribe, no de quien decide.
- **CONTEXTO.** Lo que el modelo no sabe de ti y no puede adivinar: Atención Primaria, España, siete minutos, herramienta de consumo, a quién va el texto. Aquí vive casi toda la calidad. Y aquí no entra nunca un dato identificable.
- **TAREA.** El verbo. Uno, o varios numerados y en orden: "ordena", "reescribe", "compara". No "ayúdame con". Si hay una decisión clínica detrás, no está en la tarea. Está en tu cabeza.
- **FORMATO.** Cómo quieres verlo: tabla, lista de cinco puntos, unas 150 palabras, trato de usted, una línea final literal con un recuento. El formato cerrado hace comparable una respuesta con la siguiente. Lo que protege va en la primera línea del formato, no en la última: el modelo lee de arriba abajo y decide pronto.
- **RESTRICCIONES.** Lo que no puede hacer: inventar lo que falta, nombrar marcas, dar objetivos de peso, culpar, decidir. Y siempre la misma frase final: "No incluyas ni pidas datos de personas".

Una prueba para el contexto, que es la pieza que más se escatima: ¿qué sabría de ti un residente recién llegado que leyera tu prompt? Si "nada", el modelo tampoco.

### Dónde ponerlo en la mesa

Como vimos en el capítulo 2, la mesa es grande pero se lee mal por el medio (Liu 2024). Lo que no puede fallar va al principio (rol, contexto) y al final (restricciones). Lo largo que pegas va en medio y con etiqueta: "TEXTO:", "EJEMPLO 1:". Y si quieres que mire algo concreto, díselo.

Lo que no va en ningún prompt lo explicó el capítulo 3 (nada identificable, casos sintéticos, textos propios anonimizados, la decisión clínica fuera) y lo doy por puesto de aquí en adelante.

---

## Segunda parte · Tres técnicas que bastan

Hay decenas de técnicas con nombre en inglés. Para una consulta de siete minutos bastan tres.

### Ejemplos propios: que escriba como yo

Un modelo aprende más de tres ejemplos que de diez adjetivos. "Escribe cercano pero profesional" no le dice nada; tres cartas tuyas, sí. Con unos pocos ejemplos en el propio prompt, el modelo adopta el patrón sin reentrenarlo (Brown 2020). En la práctica: tus tres mejores hojas, anonimizadas en papel primero, y el encargo nuevo debajo. Copia la estructura, el trato, hasta tus muletillas. Lo que no copia es tu criterio (caso 2).

### Pedir los pasos

Lo segundo es viejo y funciona: "antes de responder, escribe tu razonamiento paso a paso". Con lo intermedio escrito, acierta más (Wei 2022); incluso "pensemos paso a paso", sin más, mejora el resultado (Kojima 2022). Los razonadores lo traen de fábrica, como vimos en el capítulo 2. En modo chat, se lo pides tú.

Dos advertencias. Razonar más no es verificar: puede llegar con más pasos a una conclusión falsa. Y los pasos que muestra son un texto plausible, no una grabación de lo que pasa dentro: sirven para que veas dónde se tuerce, no como prueba.

### Encadenar: estructurar, analizar, criticar, comunicar

Lo tercero es lo que más ha cambiado mi manera de trabajar. Un prompt que pide "analiza este caso y escribe la nota y la hoja para el paciente" pide cuatro cosas que fallan de cuatro maneras distintas. Juntas, el error de la primera contamina las demás. Sepáralas en cuatro mensajes de la misma conversación:

- **Estructurar, sin opinar.** Solo ordenar lo que hay, con los huecos marcados. Ni una inferencia.
- **Analizar, con nivel de certeza.** Qué se deduce, de qué hecho y con qué confianza: ALTA, MEDIA o BAJA, con la escala única del libro.
- **Criticar la propia respuesta.** Qué dio por supuesto, qué sonó demasiado seguro, qué otra explicación cabe, qué omitió.
- **Comunicar, en doble salida.** Una nota para el equipo y un texto para la persona. Dos registros, los mismos hechos.

El tercero es el que nadie hace: pedirle a la máquina que se revise. La segunda pasada encuentra lo que la primera soltó por inercia, como tú cuando relees una nota al día siguiente. El caso 3 corre la cadena entera.

---

## Tercera parte · Leer la respuesta con rúbrica

### Cinco preguntas a cada salida

La respuesta llega bien escrita. Ese es el problema: lo bien escrito se lee rápido y se cree pronto. Cinco preguntas, en este orden:

- **Fidelidad.** ¿Dice solo lo que le di? Busca lo que no estaba en tu prompt: un dato, un antecedente, un "ya ha probado". Si lo hay, lo ha inventado.
- **Priorización.** ¿Lo importante va primero? Si la señal de alarma está en el punto siete, no ha priorizado. Ha enumerado.
- **Calibración.** ¿La seguridad del texto es proporcional a la evidencia? "Claramente", "sin duda" delante de algo que tú pondrías en MEDIA.
- **Confusores.** ¿Qué otra explicación cabe y no la nombra? Lo que el capítulo 1 pide mirar antes de atribuirlo todo al peso.
- **Acción segura.** ¿Qué pasa si esto está mal y actúo igual? Si "nada grave", corriges y sigues. Si "alguien sale perjudicado", no sale de tu pantalla.

La rúbrica y su lema los traigo de mi formación en IA y los he hecho míos: si suena demasiado segura, probablemente lo es.

### Una respuesta, leída con las cinco

El folleto de las 11:20, salida del prompt pobre del caso 1, decía:

> "Presenta claramente un síndrome metabólico con alto riesgo cardiovascular. Lo prioritario es una pérdida de peso del 5-10 % mediante dieta hipocalórica y 45 minutos diarios de ejercicio aeróbico. Probablemente ya ha fracasado con dietas previas, por lo que necesitará mucha disciplina."

- **Fidelidad.** "Ya ha fracasado con dietas previas" no estaba en el caso. "Síndrome metabólico": no le di lípidos ni tensión.
- **Priorización.** Lo primero es el peso. Lo que pedí era el ejercicio con las rodillas que tiene.
- **Calibración.** "Claramente" sobre datos que no existen: una BAJA vestida de ALTA.
- **Confusores.** Ni una palabra sobre dolor, sueño, ánimo ni fármacos.
- **Acción segura.** Cuarenta y cinco minutos diarios con una marcha limitada a veinte: deja de caminar a la semana. Y "disciplina" es culpa con otro nombre.

Veredicto: no sale. No se corrige, se rehace. Con el prompt del caso 1.

---

## Siete casos para hablar mejor con la máquina

Cada caso trae situación, prompt literal, ejemplo abreviado de salida, qué revisar y riesgo. Sustituye lo que va entre corchetes; ninguno admite datos identificables. Siguen las dos salidas del capítulo 3: POR ACLARAR es una pregunta que contestas tú fuera del chat; [FALTA: …], un hueco que rellenas tú fuera de la IA. Los casos 1 a 4 se hacen en conversación nueva, con la memoria desactivada (busca "chat temporal" o "incógnito") y se borran al terminar: el 2 porque tus textos nacen de cartas reales; los demás porque el hábito de pegar casos tiene que nacer con la higiene puesta. Los prompts se pegan igual en Gemini, ChatGPT y Claude; el 4 pide razonador. El 7 no usa IA. Las cifras son inventadas.

### Caso 1 · Prompt pobre frente a prompt estructurado

**Momento:** consulta. **Herramienta:** cualquier asistente conversacional.

**Situación.** La hoja de las 11:20. Caso sintético: nadie detrás, aunque se parezca a muchos. Pega el pobre; en otra conversación, el estructurado; compara. El ejercicio es tratamiento de la artrosis y de la diabetes, no una forma de quemar lo que se come: las guías lo ponen en primera línea para la rodilla (Bannuru 2019; Moseng 2024), también en personas con obesidad (Messier 2013).

Prompt pobre (su salida es la que leímos con la rúbrica):

```
Plan de ejercicio para una persona con obesidad y artrosis de rodilla.
```

Prompt estructurado:

```
ROL: Eres médica de familia con formación en ejercicio terapéutico y en la obesidad como enfermedad crónica.

CONTEXTO: Atención Primaria en España, consultas de siete minutos. Caso sintético, sin ninguna persona real detrás: hombre de 60-65 años, obesidad de grado II, diabetes tipo 2, artrosis de ambas rodillas con dolor mecánico que limita la marcha a unos veinte minutos, jubilado hace poco, sin hábito de ejercicio en años, sin cardiopatía conocida, con un parque y una piscina municipal cerca. Quiero una hoja para entregarle y comentar en la próxima visita. No pidas ni supongas más datos: lo que no esté aquí va como [FALTA: …].

TAREA: (1) Plan de actividad física de cuatro semanas, progresivo, que trate el ejercicio como parte del tratamiento de la artrosis y de la diabetes, no como forma de quemar calorías. (2) Tres tipos: caminar por tiempo y no por distancia, fuerza de piernas con el propio cuerpo o apoyado en una silla, y una opción en el agua. (3) Una regla de dolor sencilla: cuándo seguir, cuándo bajar, cuándo parar. (4) Señales para dejarlo y consultar.

FORMATO: Título de máximo ocho palabras. Tabla de cuatro filas (semanas) y tres columnas (caminar, fuerza, agua), con tiempos y repeticiones en rangos. Debajo, la regla de dolor en tres líneas, las señales para parar (máximo seis) y una línea de cierre. Trato de usted, nivel de lectura de 12 años, unas 250 palabras. Al pie, literal: "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "CIFRAS DE PESO O CALORÍAS EN EL TEXTO: [n]".

RESTRICCIONES: Ningún objetivo de peso, ninguna cifra de kilos ni de calorías, ninguna dieta. Sin fármacos ni nombres comerciales. Sin "debería", sin culpa, sin "esfuerzo" ni "disciplina". No digas que el ejercicio "cura" ni prometas resultados. Cada ejercicio tiene que poder hacerse con dolor de rodilla leve; si alguno no, no lo incluyas. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> **Mover las rodillas para que duelan menos**
> | Semana | Caminar | Fuerza | Agua |
> |---|---|---|---|
> | 1 | 2 tramos de 8-10 min, llano | Sentarse y levantarse de una silla, 2 series de 5-8 | Caminar en el agua 10-15 min |
> **Regla del dolor.** Molestia que se va al parar o al día siguiente: siga. Dolor que sube mientras lo hace: baje. Dolor que dura más de 24 horas o le despierta: pare y consúltelo.
> **Deje de hacerlo y consulte si:** la rodilla se hincha y está caliente; dolor en el pecho o falta de aire desproporcionada; mareo […]
> CIFRAS DE PESO O CALORÍAS EN EL TEXTO: 0

**Qué revisar antes de usarla.** Lado a lado: el pobre habla de kilos; el estructurado, de rodillas y de tiempo. El cero lo cuentas tú: el recuento del modelo es una afirmación, no una prueba. Que no haya sentadillas profundas ni escaleras en la semana 1. La regla del dolor es orientativa: el matiz lo pones con la rodilla delante. La condición física se mide en el capítulo 8.

**Riesgo principal y mitigación.** Que la hoja sustituya la conversación: le duele al tercer día y no vuelve. Mitigación: se entrega y se comenta, con fecha de revisión; si hay hinchazón, calor o bloqueo, la rodilla se explora antes de seguir.

### Caso 2 · Que escriba como yo

**Momento:** administración. **Herramienta:** asistente conversacional con tres textos propios como ejemplo.

**Situación.** Tú escribes de una manera; la máquina, como internet. Tres textos tuyos bastan para que imite tu tono. Pero fueron de personas reales, y el trabajo grande va antes de abrir el chat:

- **Copia el texto plano, no el archivo.** Un Word "sin nombre" lleva dentro el autor, el servicio de salud, la fecha y el control de cambios; un PDF, la cabecera del centro. Es la trampa de los metadatos: lo que no ves, entra. Pega texto, nunca adjuntes.
- **Sustituye por marcadores:** [NOMBRE], [FECHA], [CENTRO], [CIFRA]; profesión y municipio, fuera.
- **Lee en voz alta** cada ejemplo como si estuvieras en la sala de espera. Si alguien podría reconocerse, no está listo. Y elige textos distintos entre sí: así aprende tu voz y no un formato.

```
ROL: Eres una redactora que imita el estilo de otra persona a partir de ejemplos, sin inventar contenido.

CONTEXTO: Soy médica de familia en Atención Primaria en España. Te doy tres textos míos, anonimizados a mano: nombres, fechas, centro y cifras sustituidos por marcadores entre corchetes. No corresponden a ninguna persona concreta. Quiero un texto nuevo que suene a mí.

EJEMPLO 1 (carta con resultados):
[pega aquí el texto anonimizado]
EJEMPLO 2 (hoja de recomendaciones):
[pega aquí el texto anonimizado]
EJEMPLO 3 (mensaje breve):
[pega aquí el texto anonimizado]

TAREA: (1) Describe en máximo seis líneas cómo escribo: longitud de frase, trato, cómo empiezo y cierro, palabras que repito, qué no hago nunca. (2) Con ese estilo, escribe [tipo de texto, por ejemplo: una hoja para la primera visita de obesidad] sobre [tema genérico, por ejemplo: qué traer y de qué vamos a hablar], sin ninguna persona detrás. Todo dato que no te haya dado va como [FALTA: …].

FORMATO, en este orden:
(0) Una línea: "EJEMPLOS LIMPIOS" o "EJEMPLOS CON DATOS: BORRA ESTA CONVERSACIÓN". Es la segunda si en los ejemplos queda un nombre o apellido, una fecha completa, un municipio, un centro, un número que parezca de historia o una cifra con decimales; en ese caso, para.
(1) Bloque "ASÍ ESCRIBES".
(2) Bloque "TEXTO NUEVO", de unas [150] palabras, trato de [usted (hoja impresa) / tú], con la estructura del ejemplo más parecido. Al pie, literal: "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."
(3) Última línea, literal: "MARCADORES SIN RELLENAR: [n]".

RESTRICCIONES: No añadas contenido clínico que no esté en los ejemplos o en la tarea. No rellenes ningún marcador. Sin nombres comerciales, sin objetivos de peso, sin "obeso/a". Imita la forma, no los datos. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> EJEMPLOS LIMPIOS
> **ASÍ ESCRIBES.** Frases de 8-14 palabras. Empiezas por lo que la persona ha hecho, no por lo que falta. Usted; "le propongo" dos veces; cierras con un paso con fecha. Nunca "debe".
> **TEXTO NUEVO.** Antes de la primera visita, le propongo tres cosas sencillas. […] Nos veremos el [FALTA: fecha]. Hasta entonces, nada de balanzas.
> MARCADORES SIN RELLENAR: 1

**Qué revisar antes de usarla.** "ASÍ ESCRIBES" es lo más útil del caso: tu voz descrita, que sirve de contexto para prompts futuros sin volver a pegar ejemplos. En el texto nuevo, busca lo que no es tuyo: una frase hecha, un "¡ánimo!", un consejo que no diste. Si salta "EJEMPLOS CON DATOS", el dato ya entró: protocolo del capítulo 3, el mismo día.

**Riesgo principal y mitigación.** El archivo: adjuntar el Word, que lleva tu servicio de salud en las propiedades aunque el cuerpo esté limpio. Mitigación: texto plano, papel antes, conversación temporal, borrado.

### Caso 3 · La cadena de cuatro prompts

**Momento:** seguimiento de crónicos. **Herramienta:** asistente conversacional, una sola conversación nueva.

**Situación.** El hombre de las 11:20, convertido en caso sintético: rasgos de varias personas, cifras verosímiles e inventadas, ninguna historia abierta. Cuatro mensajes, en este orden. El tratamiento farmacológico no entra: lo decides tú, con la guía delante, en el capítulo 8.¹

¹ Declaración de transparencia: mantengo vínculos con Novo Nordisk, detallados al inicio del libro. En este capítulo los fármacos aparecen solo por principio activo o clase y ninguno para la obesidad; ese tratamiento se aborda en el capítulo 8.

Prompt 1 · estructurar, sin opinar:

```
ROL: Eres médica de familia con experiencia en obesidad. Esto es un ejercicio sobre un caso sintético; no hay ninguna persona real y no debes tomar ni proponer decisiones para nadie.

CONTEXTO: Caso inventado, compuesto a partir de rasgos de varias personas, con cifras verosímiles pero no reales: hombre de 60-65 años, jubilado hace pocos meses, obesidad de grado II (IMC en torno a 37, cintura en torno a 119 cm), diabetes tipo 2 de varios años con metformina, artrosis de ambas rodillas que limita la marcha a unos veinte minutos, sin cardiopatía conocida. Desde la jubilación come a deshoras y picotea por las tardes; se describe "aburrido, no triste"; se levanta dos veces por la noche a orinar. Tensión en consulta 146/88 mmHg, sin diagnóstico previo de hipertensión. Analítica reciente: glucosa en ayunas 142 mg/dl, HbA1c 7,6 %, colesterol total 215, LDL 131, HDL 38, triglicéridos 210 mg/dl, creatinina 1,0 mg/dl con filtrado estimado por encima de 60, ALT 58 y GGT 64 U/l, TSH 2,4. No hay más datos.

TAREA: Ordena el caso sin interpretarlo. Cuatro apartados: ANTECEDENTES Y TRATAMIENTO; SITUACIÓN ACTUAL (lo que cuenta la persona); EXPLORACIÓN Y ANALÍTICA (cada cifra con su unidad, tal como te la di); LO QUE FALTA (lo que una médica de familia querría saber y no está, cada punto como [FALTA: …]).

FORMATO: Cuatro listas con numeración continua. Ni una frase con "sugiere", "indica", "compatible con", "probable" ni ningún diagnóstico nuevo. Última línea, literal: "HECHOS: [n] · HUECOS: [n]".

RESTRICCIONES: No opines, no agrupes cifras bajo el nombre de un síndrome, no añadas ni redondees datos. Sin nombres comerciales. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

> […] LO QUE FALTA: 14. [FALTA: consumo de alcohol]. 16. [FALTA: hipoglucemias, adherencia]. 17. [FALTA: segunda toma de tensión] […] HECHOS: 13 · HUECOS: 7

Prompt 2 · analizar, con nivel de certeza:

```
Ahora, y solo ahora, analiza. Lista de DILEMAS, máximo siete, cada uno con: qué se deduce; de qué hechos numerados sale; certeza ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, con explicaciones o estudios discrepantes) o BAJA (plausible, no lo afirmaría sin comprobarlo); y qué punto de LO QUE FALTA lo cambiaría. No propongas tratamientos: la decisión es mía. Última línea, literal: "ALTA: [n] · MEDIA: [n] · BAJA: [n]".
```

> 1. Control glucémico por encima del objetivo habitual (hechos 1, 2, 9, 10). ALTA. Lo cambiaría: hipoglucemias, adherencia [16]. 2. Transaminasas elevadas atribuibles a hígado graso asociado a disfunción metabólica (hechos 4, 12). MEDIA. Lo cambiaría: alcohol [14]. 3. Una toma de 146/88 es una cifra elevada (ALTA); que sea hipertensión, BAJA hasta la segunda toma [17]. […] ALTA: 3 · MEDIA: 1 · BAJA: 2

Prompt 3 · criticar la propia respuesta:

```
Revisa tu respuesta anterior como si la hubiera escrito otra persona. Cuatro listas: (1) SUPUESTOS: qué diste por hecho sin que estuviera en los hechos; (2) DEMASIADO SEGURO: qué certeza bajarías y por qué; (3) OTRA EXPLICACIÓN: para cada dilema, una alternativa que no nombraste; (4) OMITIDO: qué no miraste (ánimo, sueño, atracones, alcohol, fármacos, causas secundarias) y debería estar. Última línea, literal: "CAMBIOS QUE HARÍA EN LA LISTA DE DILEMAS: [n]".
```

> SUPUESTOS: di por hecho que el picoteo es por aburrimiento; el caso solo dice que coinciden. DEMASIADO SEGURO: el dilema 2 baja a BAJA sin alcohol ni serología. OTRA EXPLICACIÓN: el picoteo vespertino puede ser un patrón de atracón; la nicturia, apnea. OMITIDO: alcohol tras la jubilación; cribado de ánimo con preguntas, no con su adjetivo; ideas de muerte. CAMBIOS: 3

Prompt 4 · comunicar, en doble salida:

```
Escribe dos textos con los mismos hechos, sin añadir ninguno e incorporando los cambios de tu revisión. (A) NOTA PARA EL EQUIPO: máximo 120 palabras, en el orden problema, datos, pendiente; huecos como [FALTA: …]; certezas entre paréntesis; sin propuesta de tratamiento. (B) TEXTO PARA LA PERSONA: unas 120 palabras, trato de usted, nivel de lectura de 12 años: qué hemos visto, qué vamos a mirar en la próxima visita y una cosa concreta para esta semana sobre el movimiento y el horario de las comidas; sin cifras de peso ni de kilos, sin fármacos, sin culpa, sin "debería". Al pie de (B), literal: "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "DATOS EN (A) QUE NO ESTÁN EN LOS HECHOS: [n] · EN (B): [n]".
```

> **(A)** Persona con obesidad de grado II y diabetes tipo 2, HbA1c 7,6 % (ALTA). ALT 58, GGT 64 (causa por aclarar, BAJA) [FALTA: alcohol, serologías]. TA 146/88 en una toma [FALTA: segunda toma]. Pendiente: ánimo, atracones, sueño […]
> **(B)** Hemos visto que el azúcar está algo más alto de lo que nos gustaría y que el hígado y la tensión merecen una segunda mirada. En la próxima visita hablaremos de cómo duerme, de cómo anda de ánimo y de qué bebe. Esta semana le propongo dos cosas: caminar por tiempo, dos ratos cortos al día, y cenar a una hora fija. […]
> DATOS EN (A) QUE NO ESTÁN EN LOS HECHOS: 0 · EN (B): 0

**Qué revisar antes de usarla.** La nota (A), con los hechos del prompt 1 delante: lo que no esté allí, fuera. Los ceros los cuentas tú. En (B), busca kilos, "debería" y cualquier fármaco. La cadena te da orden y huecos; no te da la decisión sobre la metformina, sobre añadir algo ni sobre derivar. Eso es tuyo (capítulo 8).

**Riesgo principal y mitigación.** Que el rigor aparente de cuatro pasos te haga fiarte más que de uno. Mitigación: la rúbrica sobre la salida (2), y recordar que el paso 3 lo hace la misma máquina que escribió el 2. Si el caso sintético te trae una cara, cambia el caso.

### Caso 4 · "No cierres diagnóstico"

**Momento:** consulta (entrenar el criterio). **Herramienta:** modelo de razonamiento.

**Situación.** Una ganancia de peso reciente es de las pocas cosas en obesidad donde el error de omisión cuesta caro. Este caso entrena lo contrario del cierre prematuro: separar lo que hay, lo que deduzco, lo que falta y lo que escribiría con prisa. La estructura es la del caso 5 del capítulo 2, con razonador y una lista más. Caso sintético. El modelo lista hipótesis; tú decides qué explorar y cuándo derivar (capítulo 8).

```
ROL: Eres médica de familia. Esto es un ejercicio de razonamiento sobre un caso inventado; no hay ninguna persona real y no debes tomar ni proponer decisiones para nadie.

CONTEXTO: Caso sintético, compuesto y sin correspondencia con nadie: mujer de 45-55 años, sin obesidad previa conocida, que ha ganado en torno a diez kilos en menos de un año sin identificar cambios claros en lo que come ni en lo que se mueve. Refiere cansancio, estreñimiento, piernas hinchadas al final del día, ánimo bajo "desde que pasó todo" (no concreta qué), reglas irregulares en el último año y un tratamiento nuevo desde hace unos meses cuyo nombre no consta. No hay exploración ni analítica. No hay más datos.

TAREA: No cierres ningún diagnóstico. Cuatro listas: (1) HECHOS: lo que está en el caso, numerado, sin adjetivos. (2) INFERENCIAS: cada hipótesis que explicaría la ganancia de peso, con los hechos que la apoyan entre paréntesis y la certeza ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, con explicaciones o estudios discrepantes) o BAJA (plausible, no lo afirmaría sin comprobarlo); incluye las que una médica de familia no puede dejar de considerar aunque sean poco probables, y di qué dato haría cada una más o menos probable. (3) DATOS AUSENTES: qué falta, ordenado por lo que más cambiaría el razonamiento, sin inventarlo. (4) CONCLUSIONES PREMATURAS: frases que alguien con prisa escribiría sobre este caso y que los hechos no sostienen, con una línea de por qué. Si algo no se puede saber con lo que hay, escribe "no lo sé" y qué haría falta.

FORMATO: Cuatro listas, máximo ocho puntos cada una. Última línea, literal: "HIPÓTESIS: [n] · EN ALTA: [n] · NO LO SÉ: [n]".

RESTRICCIONES: Sin diagnósticos cerrados, sin tratamientos, sin nombres comerciales. No añadas datos al caso: si los necesitas, van en la lista 3. No atribuyas la ganancia a "hábitos" sin un hecho que lo sostenga. Usa "persona con obesidad" si procede. No incluyas ni pidas datos de personas.
```

Dónde está el razonador y qué hacer si tu plan no lo tiene: caso 5 del capítulo 2.

**Ejemplo abreviado de salida.**

> INFERENCIAS: 1. Hipotiroidismo (hechos 2, 3, 4, 7): MEDIA; lo cambiaría la TSH. 2. Efecto del tratamiento nuevo (hecho 8): MEDIA; no lo sé cuál es. 3. Transición menopáusica (hechos 1, 7): MEDIA; explica parte, no diez kilos en un año. 4. Depresión (hecho 6): MEDIA. 5. Trastorno por atracón: BAJA; hay que preguntarlo. 6. Retención de líquidos de causa cardiaca o renal (hecho 5): BAJA; disnea u ortopnea lo subirían. 7. Hipercortisolismo (hechos 2, 5, 6): BAJA; raro; hematomas fáciles, estrías violáceas o debilidad proximal lo subirían.
> DATOS AUSENTES: nombre del tratamiento; TSH; exploración (edemas, piel, tensión, cintura); preguntas de ánimo, incluidas ideas de muerte; preguntas de atracón; alcohol; sueño.
> CONCLUSIONES PREMATURAS: "Es la menopausia" (explica parte, no descarta el resto). "Algo habrá cambiado en sus hábitos" (no hay ningún hecho). "El antidepresivo la ha hecho engordar" (no sabemos que sea un antidepresivo).
> HIPÓTESIS: 7 · EN ALTA: 0 · NO LO SÉ: 2

**Qué revisar antes de usarla.** Que nada esté en ALTA: con este caso, una ALTA es un error de calibración. Que el fármaco sea lo primero de la lista 3: es el dato que más cambia el razonamiento y el más barato de conseguir. Que haya preguntado por atracones y por ideas de muerte; pocos modelos lo hacen solos. Lo raro, como el hipercortisolismo, está para que lo descartes en la exploración, no para pedirlo todo de entrada. Y la lista 4 es la más útil: son las frases que tú habrías escrito a las 13:50. Los fármacos que aumentan peso tienen listas publicadas (Wharton 2018; Wharton 2020).

**Riesgo principal y mitigación.** Que el ejercicio se convierta en consulta y un día pegues a alguien real porque "es parecido". Mitigación: solo casos compuestos; si la invención se parece a alguien, no es una invención. Y el anclaje inverso: que siete hipótesis te anclen a siete y dejes de pensar en la octava.

### Caso 5 · El consejo breve de siete minutos [AP]

**Momento:** consulta. **Herramienta:** cualquier asistente conversacional.

**Situación.** Viene por otro motivo y al final queda un minuto. Treinta segundos bien dichos son aceptables para la mayoría y abren puertas (Aveyard 2016). El molde es el de la entrevista motivacional: nombrar sin juzgar, preguntar y pactar (Miller 2013), con la persona primero (Kyle 2014).

```
ROL: Eres médica de familia con formación en entrevista motivacional y en lenguaje centrado en la persona.

CONTEXTO: Atención Primaria en España, consultas de siete minutos. Quiero una intervención breve para decir en voz alta, al final de una visita por otro motivo, a una persona con obesidad a la que aún no he ofrecido abordar el peso. Hablo yo, en persona; no es un texto para entregar. Sin ninguna persona concreta detrás.

TAREA: Una intervención con exactamente tres partes: dos frases que nombren la obesidad como enfermedad con biología detrás y sin culpa; una pregunta abierta que deje la decisión a la persona; y un siguiente paso pactado, pequeño, con fecha relativa ("en dos o tres semanas"). Después, tres variantes completas para cuando la persona responde: (a) "ya probé todo"; (b) "no tengo tiempo"; (c) "mi problema es la ansiedad".

FORMATO: Bloque BASE y bloques (a), (b), (c), cada uno con sus tres partes marcadas; máximo 60 palabras por bloque; trato de [usted / tú]; que pueda decirse en menos de treinta segundos. Última línea, literal: "PALABRAS PROHIBIDAS ENCONTRADAS: [n]".

RESTRICCIONES: Palabras prohibidas: "obeso/a", "debería", "esfuerzo", "fuerza de voluntad", "disciplina", "solo tiene que", "fácil". Sin objetivos de peso, sin dietas, sin fármacos ni nombres comerciales, sin promesas de resultado. En (c), no des consejo sobre la ansiedad: reconócela y abre la puerta a valorarla. No incluyas datos de personas.
```

**Ejemplo abreviado de salida.**

> **(a) "Ya probé todo".** "Lo creo. Y que todo funcionara un tiempo y luego no es justo lo que hace el cuerpo: no falló usted, falló el método." Pregunta: "¿Qué fue lo que más le costó mantener?" Paso: "En la próxima visita empezamos por ahí, no por una dieta."
> PALABRAS PROHIBIDAS ENCONTRADAS: 0

**Qué revisar antes de usarla.** Léelo en voz alta. Si no lo dirías con tu cara, no es tuyo: cámbialo hasta que lo sea. En (c), que no haya consejo sobre la ansiedad, solo la puerta; se valora en su propia visita y, si hay atracones, eso va antes que el peso (capítulo 8). No lleva disclaimer impreso: lo dices tú, en persona, y esa es la valoración clínica individual.

**Riesgo principal y mitigación.** Que el guion se recite; la persona nota la diferencia entre una frase pensada y una leída. Mitigación: tres versiones, una elegida, y cambiarla cada pocos meses.

### Caso 6 · Mensaje entre visitas [AP]

**Momento:** seguimiento de crónicos. **Herramienta:** asistente conversacional, sin identificadores.

**Situación.** Entre dos visitas pasan semanas y la persona está sola con lo que pactó. Un mensaje corto sostiene más que un consejo largo. El modelo escribe la plantilla; nombre, fecha y paso pactado los pones tú en tu sistema, fuera del chat. Si toca síntomas o un tratamiento nuevo, lleva red de seguridad (capítulo 3).

```
ROL: Eres una redactora de mensajes breves para pacientes de Atención Primaria, con conocimientos de lenguaje centrado en la persona.

CONTEXTO: Soy médica de familia en España. Quiero plantillas de mensaje de refuerzo entre dos visitas, para enviar por el canal del centro o leer en una llamada de seguimiento. Son genéricas: sin nombre, sin fechas, sin cifras de nadie; lo que cambie por persona va como [FALTA: …] y lo relleno yo en mi sistema, fuera de esta conversación. Dos situaciones: (1) persona con obesidad que acordó empezar a caminar por tiempo y lleva dos o tres semanas; (2) persona que ha empezado un tratamiento nuevo que puede dar molestias digestivas los primeros días, sin nombrar el tratamiento.

TAREA: Un mensaje por situación que: reconozca lo hecho sin calificarlo de éxito ni de fracaso; recuerde el siguiente paso como [FALTA: paso pactado]; y diga cómo contactar si hay dudas. En (2), incluye literalmente esta línea: "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo."

FORMATO: Dos mensajes de máximo 90 palabras cada uno, trato de usted, nivel de lectura de 12 años, sin emoticonos. Al pie de cada uno, literal: "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "MARCADORES: [n] · FRASES QUE EVALÚAN: [n]".

RESTRICCIONES: Sin felicitaciones por kilos ni mención de peso, balanza o cifras. Sin "debería", sin "ánimo, usted puede", sin culpa si no se ha cumplido. Sin nombres de fármacos ni comerciales, sin consejo sobre dosis. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> **(2)** Los primeros días de un tratamiento nuevo pueden traer molestias de estómago, que suelen ir a menos. Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo. Lo que acordamos: [FALTA: paso pactado]. […]
> Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> MARCADORES: 2 · FRASES QUE EVALÚAN: 0

**Qué revisar antes de usarla.** Que la línea de seguridad esté literal y entera; el modelo tiende a suavizarla. Que no haya kilos ni "¡enhorabuena!". El canal: el portal del paciente es consulta registrada; el WhatsApp personal, no. Y si la persona contesta con un efecto adverso, el siguiente mensaje no lo escribe la máquina: es la frase del capítulo 3, y notificas.

**Riesgo principal y mitigación.** Enviar la plantilla con el marcador sin rellenar, o rellenarlo en el chat "para que quede mejor". Mitigación: los huecos se rellenan en tu sistema, nunca en la conversación; y un vistazo final antes de enviar, como a cualquier receta.

### Caso 7 · Mi biblioteca de prompts en Markdown

**Momento:** administración. **Herramienta:** un editor de texto. Sin IA.

**Situación.** El tercer martes que reescribes el mismo prompt desde cero has perdido más tiempo del que la IA te ahorró. Los prompts que funcionan se guardan, se versionan y se comparten. Yo los guardo en Markdown: texto plano con unas marcas mínimas (almohadilla para el título, asteriscos para la negrita, tres acentos graves para el código) que lee igual una persona y el propio modelo si se lo pegas como contexto. Un bloc de notas vale. No es magia: es una ficha.

````markdown
# [Nombre corto del prompt]

- **Versión:** v1 · **Fecha:** AAAA-MM-DD
- **Herramienta y modelo:** [por ejemplo: Claude, modelo X · ChatGPT, modelo Y], leído en el desplegable
- **Modo:** chat / razonador
- **Momento:** consulta / seguimiento / administración / docencia / divulgación
- **Para qué sirve:** una frase.
- **Datos que admite:** ninguno identificable; sintéticos / anonimizados / agregados.
- **Riesgo:** bajo / medio / alto, y por qué (qué pasa si se equivoca).

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

Tres reglas:

- **Versiona, no sobrescribas.** Si cambias una línea y la salida mejora, es v2 con fecha y una línea de por qué. Si la herramienta cambia de modelo, anótalo: el mismo prompt puede dejar de funcionar sin que hayas tocado nada (capítulo 2).
- **Un nombre de archivo que diga lo que hace:** `consejo-breve-7min_v2.md`. Nada de "prompt final definitivo 3".
- **Comparte la ficha, nunca la conversación.** El prompt no lleva datos; la conversación puede llevarlos. Una carpeta compartida del centro con las fichas, pasadas por las diez preguntas del capítulo 3, es una biblioteca de equipo.

**Qué revisar antes de usarla.** Que cada ficha tenga "Datos que admite" y "Qué revisar" rellenos: sin esas dos líneas no es una ficha, es un texto. Una vez al trimestre, abre las que más usas y comprueba el modelo. Los cincuenta prompts del anexo A usan esta misma ficha; los de este capítulo aparecen allí en su versión final.

**Riesgo principal y mitigación.** Que alguien use una ficha sin leer "Qué revisar", porque "si está en la carpeta, funciona". Mitigación: el riesgo en la cabecera, en mayúsculas si es alto; y que la firme quien la probó.

---

## Caso ilustrativo, no real: arquetipo compuesto

> Esta viñeta combina rasgos de varios hombres con obesidad, diabetes tipo 2 y artrosis que llegan a la consulta tras jubilarse. La franja de edad es amplia; no hay profesión, municipio, fechas ni cifras que permitan reconocer a nadie. Las analíticas del caso 3 son inventadas. Es el mismo caso sintético que corre la cadena: lo construí para eso.

Tiene entre sesenta y sesenta y cinco años. Se jubiló hace unos meses de un trabajo en el que se movía poco y comía a la hora que podía. Obesidad de grado II, diabetes tipo 2 con metformina, las dos rodillas con artrosis. Viene a la segunda visita con la hoja del caso 1 doblada en cuatro y anotada a lápiz. "La piscina, los martes. Que está vacía."

Yo vengo con cinco minutos de preparación. La cadena del caso 3 no me dijo qué hacer; me dijo qué no había preguntado. Pregunto. Alcohol: una cerveza al mediodía, "a veces dos, que ahora hay tiempo". Duerme mal y se levanta dos veces. Por la tarde, "desde las seis hasta la cena, lo que pille". Las preguntas de ánimo, porque "aburrido, no triste" es un adjetivo suyo, no un cribado mío: hoy no hay más que un día demasiado largo. Segunda toma de tensión, alta otra vez. Apunto la ecografía y la analítica que faltan; si hay que cambiar algo del tratamiento, lo decido con la guía en la mano (capítulo 8).

Lo que hablamos no es de kilos. Es de las seis de la tarde. El tiempo es lo que tiene y lo que le sobra a esa hora. Pactamos dos cosas: la piscina martes y jueves, y cenar a las nueve con algo preparado a las seis. Le doy el texto (B) del caso 3, en usted, con mi firma y la fecha de la próxima visita.

"¿Y lo del azúcar?", pregunta en la puerta. Va a mejorar si lo otro se mueve, le digo, y lo demás lo vemos con la analítica. No es falta de voluntad. Es biología, y es una agenda vacía a las seis de la tarde. Las dos cosas se tratan.

---

## En 60 segundos

1. Un prompt pobre no es un error: es dejar todas las decisiones a la estadística de internet, que en obesidad está llena de kilos objetivo, culpa y marcas.
2. Cinco piezas, siempre en el mismo orden: rol, contexto, tarea, formato, restricciones. El contexto es donde vive la calidad; lo que protege va en la primera línea del formato.
3. Tres técnicas bastan: tus textos anonimizados como ejemplo, pedir los pasos por escrito y encadenar estructurar, analizar, criticar y comunicar.
4. Cada respuesta se lee con cinco preguntas: fidelidad, priorización, calibración, confusores y acción segura. Si suena demasiado segura, probablemente lo es.
5. Lo que funciona se guarda en una ficha con versión, fecha y modelo; se comparte la ficha, nunca la conversación.

## Hazlo hoy · 10 minutos

Te propongo cuatro pasos:

1. **(2 min)** Pega el prompt pobre del caso 1 en un asistente de consumo. Subraya en la salida cada kilo, cada caloría y cada "consulte con su médico".
2. **(4 min)** En una conversación nueva, pega el estructurado. Pon las dos salidas lado a lado y pásales las cinco preguntas de la rúbrica.
3. **(3 min)** Crea una carpeta llamada "prompts" y guarda el estructurado con la ficha del caso 7, en v1, con la fecha de hoy y el modelo que has usado.
4. **(1 min)** Elige qué texto tuyo vas a anonimizar mañana para el caso 2. Solo elegirlo.

Mañana, a las 11:20, alguien te dirá que ahora tiene tiempo y no sabe por dónde empezar. Tendrás tres minutos y un chat abierto. Esto no lo hace la IA por ti: te da los minutos para hacerlo tú. Y las palabras que le pidas serán las tuyas, o serán las de un folleto.

---

## Referencias

**Modelos de lenguaje y técnicas de instrucción**

1. Brown TB, Mann B, Ryder N, Subbiah M, Kaplan J, Dhariwal P, et al. Language models are few-shot learners. En: Advances in Neural Information Processing Systems 33 (NeurIPS 2020); 2020. p. 1877-901. arXiv:2005.14165.
2. Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, et al. Chain-of-thought prompting elicits reasoning in large language models. En: Advances in Neural Information Processing Systems 35 (NeurIPS 2022); New Orleans (LA); 2022. p. 24824-37. arXiv:2201.11903.
3. Kojima T, Gu SS, Reid M, Matsuo Y, Iwasawa Y. Large language models are zero-shot reasoners. En: Advances in Neural Information Processing Systems 35 (NeurIPS 2022); New Orleans (LA); 2022. p. 22199-213. arXiv:2205.11916. [VERIFICAR páginas]
4. Liu NF, Lin K, Hewitt J, Paranjape A, Bevilacqua M, Petroni F, et al. Lost in the middle: how language models use long contexts. Trans Assoc Comput Linguist. 2024;12:157-73. doi:10.1162/tacl_a_00638
**Actividad física y artrosis de rodilla**

5. Bannuru RR, Osani MC, Vaysbrot EE, Arden NK, Bennell K, Bierma-Zeinstra SMA, et al. OARSI guidelines for the non-surgical management of knee, hip, and polyarticular osteoarthritis. Osteoarthritis Cartilage. 2019;27(11):1578-89. doi:10.1016/j.joca.2019.06.011
6. Moseng T, Vliet Vlieland TPM, Battista S, Beckwée D, Boyadzhieva V, Conaghan PG, et al. EULAR recommendations for the non-pharmacological core management of hip and knee osteoarthritis: 2023 update. Ann Rheum Dis. 2024;83(6):730-40. [VERIFICAR DOI]
7. Messier SP, Mihalko SL, Legault C, Miller GD, Nicklas BJ, DeVita P, et al. Effects of intensive diet and exercise on knee joint loads, inflammation, and clinical outcomes among overweight and obese adults with knee osteoarthritis: the IDEA randomized clinical trial. JAMA. 2013;310(12):1263-73. doi:10.1001/jama.2013.277669

**Ganancia de peso, causas secundarias y fármacos**

8. Wharton S, Raiber L, Serodio KJ, Lee J, Christensen RA. Medications that cause weight gain and alternatives in Canada: a narrative review. Diabetes Metab Syndr Obes. 2018;11:427-38. [VERIFICAR DOI]
9. Wharton S, Lau DCW, Vallis M, Sharma AM, Biertho L, Campbell-Scherer D, et al. Obesity in adults: a clinical practice guideline. CMAJ. 2020;192(31):E875-E891. doi:10.1503/cmaj.191707
10. Sociedad Española para el Estudio de la Obesidad (SEEDO). Guía Española GIRO: Guía española del manejo Integral y multidisciplinaR de la Obesidad en personas adultas. 2.ª ed. Lecube A, coordinador. Madrid: SEEDO; noviembre de 2024. Disponible en: https://www.seedo.es/images/site/giro/GUIA-GIRO-2a-edicin_26NOV2024.pdf [VERIFICAR ISBN 2.ª ed.: candidato 978-84-09-65969-2]

**Comunicación y consejo breve**

11. Miller WR, Rollnick S. Motivational interviewing: helping people change. 3.ª ed. Nueva York: Guilford Press; 2013. Edición en español: La entrevista motivacional: ayudar a las personas a cambiar. 3.ª ed. Barcelona: Paidós; 2015. [VERIFICAR edición española]
12. Aveyard P, Lewis A, Tearne S, Hood K, Christian-Brown A, Adab P, et al. Screening and brief intervention for obesity in primary care: a parallel, two-arm, randomised trial. Lancet. 2016;388(10059):2492-500. doi:10.1016/S0140-6736(16)31893-1
13. Kyle TK, Puhl RM. Putting people first in obesity. Obesity (Silver Spring). 2014;22(5):1211. doi:10.1002/oby.20727
