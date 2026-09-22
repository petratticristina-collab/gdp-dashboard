# Capítulo 4 · Hablar con la IA

**Rol, contexto, tarea, formato: la gramática que cambia el resultado.**

Son las 11:20. Acaba de salir un hombre de sesenta y pocos años, jubilado hace unos meses, con obesidad de grado II, diabetes tipo 2 y artrosis en las dos rodillas. "Ahora tengo tiempo, doctora, pero no sé por dónde empezar." Le he prometido una hoja de ejercicio para la próxima visita. Tengo tres minutos.

Escribo en el chat: "plan de ejercicio para obesidad y artrosis de rodilla". Vuelve un folleto de gasolinera: camine treinta minutos, consulte con su médico. Y una línea que no pedí ni va en una hoja: "un objetivo realista es perder el 5-10 % del peso". Escribo otra vez, ahora con las cinco piezas de este capítulo. Tarda lo mismo. Lo que vuelve puedo corregirlo y dárselo esa tarde.

La diferencia no estaba en la máquina. Estaba en lo que le pedí. Este capítulo es esa diferencia.

*Como todas las escenas de consulta de este libro, es una composición de varias personas.*

## Lo que te vas a llevar

- Una gramática de cinco piezas y el mismo encargo escrito mal y bien, lado a lado.
- Tres técnicas: tus textos como ejemplo, pedir los pasos y encadenar cuatro prompts.
- Cinco preguntas para leer cualquier respuesta y siete casos sin datos identificables.

---

## Primera parte · La gramática: cinco piezas

### Un prompt es una interconsulta

A un compañero de segundo nivel no le escribes "paciente con obesidad, ¿qué hago?". Le dices quién eres, qué sabes, qué necesitas y para cuándo. Con la máquina, lo mismo, con una diferencia: el compañero rellena los huecos con experiencia y te llama si duda; el modelo los rellena con lo más probable y no llama a nadie (capítulo 2).

Un prompt pobre deja las decisiones a la estadística de internet, que en obesidad está llena de culpa, de kilos objetivo y de marcas: "dieta para adelgazar" devuelve un folleto.

### Las cinco piezas

Los prompts del libro siguen el mismo molde:

- **ROL.** Quién quieres que sea: "médica de familia con experiencia en obesidad". Nunca "el médico que trata a este paciente": el rol es de quien escribe, no de quien decide.
- **CONTEXTO.** Lo que el modelo no sabe de ti: Atención Primaria, España, siete minutos, herramienta de consumo, a quién va el texto. Aquí vive la calidad; aquí no entra nunca un dato identificable.
- **TAREA.** El verbo: "ordena", "reescribe", "compara"; uno, o varios numerados. No "ayúdame con". La decisión clínica no está en la tarea: está en tu cabeza.
- **FORMATO.** Cómo quieres verlo: tabla, cinco puntos, unas 150 palabras, trato de usted, una línea final con un recuento. Lo que protege va en su primera línea, no en la última.
- **RESTRICCIONES.** Lo que no puede hacer: inventar lo que falta, nombrar marcas, dar objetivos de peso, culpar, decidir. Y siempre la misma frase final: "No incluyas ni pidas datos de personas".

Prueba para el contexto, la pieza que más se escatima: ¿qué sabría de ti un residente recién llegado que leyera tu prompt? Si "nada", el modelo tampoco.

### Dónde ponerlo en la mesa

La mesa del capítulo 2 se lee mal por el medio: el modelo pesa más lo que está al principio y al final (Liu 2024). Rol y contexto, arriba; restricciones, abajo; lo largo que pegas, en medio y con etiqueta: "TEXTO:", "EJEMPLO 1:".

---

## Segunda parte · Tres técnicas que bastan

Técnicas con nombre en inglés hay decenas. Para siete minutos bastan tres.

### Ejemplos propios: que escriba como yo

Un modelo aprende más de tres ejemplos que de diez adjetivos. "Escribe cercano pero profesional" no le dice nada; tres cartas tuyas, sí: con pocos ejemplos adopta el patrón (Brown 2020). Tus tres mejores hojas, anonimizadas en papel primero, y el encargo nuevo debajo. Lo que no copia es tu criterio (caso 2).

### Pedir los pasos

Lo segundo funciona: "antes de responder, escribe tu razonamiento paso a paso". Con lo intermedio escrito acierta más (Wei 2022); incluso "pensemos paso a paso", sin más, mejora (Kojima 2022). Los razonadores lo traen de fábrica (capítulo 2); en modo chat, se lo pides tú.

Dos advertencias. Razonar más no es verificar: puede llegar con más pasos a una conclusión falsa. Y los pasos que muestra son texto plausible, no una grabación de lo que pasa dentro.

### Encadenar: estructurar, analizar, criticar, comunicar

Lo tercero es lo que más ha cambiado mi manera de trabajar. "Analiza este caso y escribe la nota y la hoja" pide cuatro cosas que fallan de cuatro maneras, y el error de la primera contamina las demás. Sepáralas en cuatro mensajes de la misma conversación:

- **Estructurar.** Solo ordenar lo que hay, sin una opinión y con los huecos marcados.
- **Analizar.** Qué se deduce, de qué hecho y con qué confianza: ALTA, MEDIA o BAJA.
- **Criticar.** Que relea: qué dio por supuesto, qué sonó demasiado seguro, qué otra explicación cabe, qué omitió.
- **Comunicar, dos veces.** Una nota para el equipo y un texto para la persona: los mismos hechos, dos registros. La nota es un borrador, no una anotación en la historia.

El tercer paso es el que nadie da: pedirle a la máquina que se revise, como tú al releer una nota al día siguiente. El caso 3 corre la cadena entera.

---

## Tercera parte · Leer la respuesta con rúbrica

### Cinco preguntas a cada salida

La respuesta llega bien escrita. Ese es el problema: lo bien escrito se lee rápido y se cree pronto. Cinco preguntas, en este orden:

- **Fidelidad.** ¿Dice solo lo que le di? Un dato, un antecedente, un "ya ha probado" que no estaba en tu prompt: lo ha inventado.
- **Priorización.** ¿Lo importante va primero? Si la señal de alarma está en el punto siete, no ha priorizado. Ha enumerado.
- **Calibración.** ¿La seguridad es proporcional a la evidencia? "Claramente", "sin duda" delante de algo que tú pondrías en MEDIA.
- **Confusores.** ¿Qué otra explicación cabe y no la nombra? Lo que el capítulo 1 pide mirar antes de atribuirlo todo al peso.
- **Acción segura.** ¿Qué pasa si esto está mal y actúo igual? Si "nada grave", corriges y sigues. Si "alguien sale perjudicado", no sale de tu pantalla.

La rúbrica y su lema, la cadena de cuatro pasos y el ejercicio de no cerrar diagnóstico los traigo de mi formación en IA y los he hecho míos en consulta: si suena demasiado segura, probablemente lo es.

---

## Siete casos para hablar mejor con la máquina

Sustituye lo que va entre corchetes; ninguno de los siete casos admite datos identificables. Valen las dos salidas del capítulo 3: POR ACLARAR, pregunta que contestas tú; [FALTA: …], hueco que rellenas tú fuera de la IA. El modelo no rellena ninguno.

Todo se hace con herramientas de consumo, sin acuerdo de tratamiento de datos: solo casos sintéticos, textos anonimizados a mano y plantillas. Un contrato futuro cambiará lo que puede entrar, no la gramática.

Los casos 1 a 4 van en conversación nueva con la memoria apagada ("chat temporal" o "incógnito") y se borran al terminar; el 5 y el 6 no llevan dato alguno, y aun así conviene la costumbre. Los seis prompts se pegan igual en Gemini, ChatGPT y Claude cuando escribo esto; comprueba la versión vigente. El 4 pide razonador y trae una línea de rescate por si tu plan no lo tiene; el 3 va entero en la misma conversación y con el mismo modelo; el 7 no usa IA.

### Caso 1 · Prompt pobre frente a prompt estructurado

**Momento:** consulta. **Herramienta:** cualquier asistente conversacional.

**Situación.** La hoja de las 11:20, con un caso sintético. El ejercicio es tratamiento de la artrosis y de la diabetes, no una forma de quemar calorías: las guías lo ponen en primera línea (Bannuru 2019; Moseng 2024; Colberg 2016). El peso sí cuenta en esa rodilla, y lo hablo yo con él; en una hoja de ejercicio no va una cifra objetivo.

Prompt pobre:

```
Plan de ejercicio para una persona con obesidad y artrosis de rodilla.
```

Prompt estructurado:

```
ROL: Eres médica de familia con formación en ejercicio terapéutico y en la obesidad como enfermedad crónica.

CONTEXTO: Atención Primaria en España, consultas de siete minutos. Caso sintético, sin ninguna persona real detrás: hombre de 60-65 años, obesidad de grado II, diabetes tipo 2 tratada con metformina, artrosis de ambas rodillas con dolor mecánico que limita la marcha a unos veinte minutos, jubilado hace poco, sin cardiopatía conocida y sin síntomas con el esfuerzo, sensibilidad de los pies [FALTA: exploración] (no lo menciones en la hoja), con un parque y una piscina municipal cerca. Quiero una hoja para entregarle y comentar en la próxima visita. No pidas ni supongas más datos: si necesitas algo que no está, no lo inventes ni lo pongas en la hoja; escríbelo al final en una lista "POR ACLARAR", que resuelvo yo.

TAREA: (1) Plan de actividad física de cuatro semanas, progresivo, que trate el ejercicio como parte del tratamiento de la artrosis y de la diabetes, no como forma de quemar calorías. (2) Tres tipos: caminar por tiempo y no por distancia, fuerza de piernas con el propio cuerpo o apoyado en una silla, y una opción en el agua. (3) Una regla de dolor sencilla: cuándo seguir, cuándo bajar, cuándo parar. (4) Señales para parar, en dos grupos: las que son de urgencias o 112 (dolor u opresión en el pecho, falta de aire que no corresponde al esfuerzo, mareo o desmayo) y las que son de pedir cita (rodilla hinchada y caliente, dolor que no cede en 24-48 horas, bloqueo o fallo de la rodilla). (5) Una línea sobre calzado cerrado y mirar los pies al terminar, por la diabetes.

FORMATO: Título de máximo ocho palabras. Tabla de cuatro filas (semanas) y tres columnas (caminar, fuerza, agua), con tiempos y repeticiones en rangos. Debajo, la regla de dolor en tres líneas; las señales para parar en dos bloques, "Pare y llame al 112 si" y "Pare y pida cita si", con un máximo de tres señales cada uno; y la línea de calzado y pies. Trato de usted, nivel de lectura de 12 años, unas 300 palabras sin contar las líneas literales, sin emoticonos. Al pie, en este orden y literal: "Si tiene dudas o algo no va bien, [FALTA: contacto del centro]." "Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112." "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Después de la hoja, la lista "POR ACLARAR" si la hay. Última línea, literal: "CIFRAS DE PESO O CALORÍAS EN EL TEXTO: [n]".

RESTRICCIONES: Ningún objetivo de peso, ninguna cifra de kilos ni de calorías, ninguna dieta. Sin fármacos ni nombres comerciales. Sin "debería", sin culpa, sin "esfuerzo" ni "disciplina", sin frases de ánimo ("la constancia es clave", "usted puede"). No escribas "consulte con su médico antes de empezar": esta hoja se la da su médica. No digas que el ejercicio "cura" ni prometas resultados. Cada ejercicio tiene que poder hacerse con dolor de rodilla leve; si alguno no, no lo incluyas; sin sentadillas profundas ni escaleras en las dos primeras semanas. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> **Mover las rodillas para que duelan menos**
> | Semana | Caminar | Fuerza | Agua |
> |---|---|---|---|
> | 1 | 2 tramos de 8-10 min, llano | Sentarse y levantarse de una silla, 2 series de 5-8 | Caminar en el agua 10-15 min |
> **Regla del dolor.** Molestia que se va al parar o al día siguiente: siga. Dolor que sube mientras lo hace: baje. Dolor que dura más de 24 horas o le despierta: pare y consúltelo.
> **Pare y llame al 112 si:** dolor u opresión en el pecho, falta de aire, mareo o desmayo.
> **Pare y pida cita si:** la rodilla se hincha y está caliente, se bloquea o el dolor no cede en dos días.
> Calzado cerrado y cómodo; al terminar, mírese los pies. […]
> Si tiene dudas o algo no va bien, [FALTA: contacto del centro].
> Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112.
> Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> POR ACLARAR: ¿sabe nadar o solo caminar en el agua?
> CIFRAS DE PESO O CALORÍAS EN EL TEXTO: 0

**Qué revisar antes de usarla.** El pobre devuelve, en los tres modelos, algo así:

> "Un programa de ejercicio para personas con obesidad y artrosis de rodilla debe combinar actividad aeróbica de bajo impacto (caminar, bicicleta estática, natación) 30-45 minutos al día, cinco días por semana, con ejercicios de fortalecimiento del cuádriceps. Una pérdida de peso del 5-10 % reduce de forma significativa la carga sobre la articulación, por lo que conviene combinarlo con una dieta hipocalórica. Consulte con su médico antes de comenzar cualquier programa de ejercicio."

Leído con las cinco:

- **Fidelidad.** Sin caso no puede ser infiel; lo que hay es relleno: "5-10 %", "dieta hipocalórica", "cinco días por semana".
- **Priorización.** Primero el peso y la dieta. Lo que pedí era el ejercicio con esas rodillas.
- **Calibración.** "Debe", "de forma significativa": la seguridad de quien no conoce a nadie.
- **Confusores.** Nada sobre el dolor, la marcha ni qué toma; tampoco deja el hueco.
- **Acción segura.** Cuarenta y cinco minutos diarios con una marcha de veinte: deja de caminar a la semana. Y "consulte con su médico" en una hoja que le da su médica.

Veredicto: no sale; se rehace. El pobre habla de kilos; el estructurado, de rodillas y de tiempo. En el estructurado, el cero lo cuentas tú: el recuento del modelo es una afirmación, no una prueba. La regla del dolor es orientativa; el matiz, con la rodilla delante. Que no diga "desgaste": esa rodilla se mueve para doler menos. La línea del 112, literal: el modelo tiende a suavizarla. Con insulina o sulfonilurea haría falta una línea sobre hipoglucemia; con metformina sola, no. Y las diez preguntas del anexo B.

**Riesgo principal y mitigación.** Que la hoja sustituya la conversación: le duele al tercer día y no vuelve. Mitigación: se entrega y se comenta, con fecha de revisión; hinchazón, calor, bloqueo o un síntoma con el esfuerzo se exploran antes de seguir.

### Caso 2 · Que escriba como yo

**Momento:** administración. **Herramienta:** asistente conversacional con tres textos propios como ejemplo.

**Situación.** Tres textos tuyos bastan para que la máquina imite tu tono. Pero fueron de personas reales, y el trabajo grande va antes de abrir el chat:

- **Copia el texto plano, no el archivo.** Un Word lleva dentro el autor y el servicio de salud; un PDF, la cabecera del centro. Lo que no ves, entra.
- **Sustituye por marcadores:** [NOMBRE], [FECHA], [CENTRO], [CIFRA]; profesión y municipio, fuera.
- **Lee cada ejemplo** como en la sala de espera: si alguien podría reconocerse, no está listo.
- **Elige textos de lo frecuente y distintos entre sí.** Lo que en tu cupo tiene una sola persona sigue siendo suyo sin el nombre (capítulo 3).

```
ROL: Eres una redactora que imita el estilo de otra persona a partir de ejemplos, sin inventar contenido.

CONTEXTO: Soy médica de familia en Atención Primaria en España. Te doy tres textos míos, anonimizados a mano: nombres, fechas, centro y cifras sustituidos por marcadores entre corchetes, y sin ningún dato clínico poco frecuente. Ya no corresponden a ninguna persona concreta. Quiero un texto nuevo que suene a mí.

EJEMPLO 1 (carta con resultados):
[pega aquí el texto anonimizado]
EJEMPLO 2 (hoja de recomendaciones):
[pega aquí el texto anonimizado]
EJEMPLO 3 (mensaje breve):
[pega aquí el texto anonimizado]

TAREA: (1) Describe en máximo seis líneas cómo escribo, con rasgos que se puedan comprobar: longitud de frase, trato, cómo empiezo y cómo cierro, palabras y giros que repito, qué no hago nunca. Sin adjetivos de tono ("cercano", "empático"). (2) Con ese estilo, escribe [tipo de texto, por ejemplo: una hoja para la primera visita de obesidad] sobre [tema genérico, por ejemplo: qué traer y de qué vamos a hablar], sin ninguna persona detrás. El contenido es solo este, y no más: [puntos que debe contener, por ejemplo: traer la medicación que toma y las analíticas del último año; no hace falta venir en ayunas; hablaremos de su historia con el peso, de cómo duerme y de qué espera de la consulta; la visita dura unos veinte minutos]. Todo dato que no te haya dado va como [FALTA: …].

FORMATO, en este orden:
(0) Una línea: "EJEMPLOS LIMPIOS" o "EJEMPLOS CON DATOS: BORRA ESTA CONVERSACIÓN". Es la segunda si en los ejemplos queda un nombre o apellido, una fecha completa, un municipio, un centro, una profesión concreta, un DNI, un teléfono, un correo, una dirección, un número que parezca de historia o un dato clínico tan poco frecuente que señale a una persona; en ese caso, para: no escribas nada más.
(1) Bloque "ASÍ ESCRIBES".
(2) Bloque "TEXTO NUEVO", de unas [150] palabras sin contar las líneas literales, trato de [usted (por defecto en hojas impresas o enviadas) / tú], con la estructura del ejemplo más parecido. Al pie, en este orden y literal: "Si tiene dudas, [FALTA: contacto del centro]." (en tú, "Si tienes dudas"); [solo si el texto habla de síntomas o de un tratamiento: pega aquí la línea de "no espere: urgencias o 112" del caso 1 o del caso 6]; y el aviso en el trato elegido: en usted, "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."; en tú, "Material informativo generado con apoyo de IA y revisado por tu profesional sanitario. No sustituye la valoración clínica individual."
(3) Lista "POR ACLARAR" con lo que no puedas deducir de los ejemplos; lo contesto yo fuera del chat.
(4) Última línea, literal: "MARCADORES SIN RELLENAR: [n]".

RESTRICCIONES: No añadas contenido clínico ni consejos que no estén en los puntos de la tarea: si un punto te parece incompleto, no lo completes; ponlo en POR ACLARAR. No rellenes ningún marcador, ni con aproximaciones ("en las próximas semanas"). Sin nombres comerciales, sin objetivos de peso, sin "obeso/a", sin frases de ánimo ni despedidas que no estén en los ejemplos. Imita la forma, no los datos. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> EJEMPLOS LIMPIOS
> **ASÍ ESCRIBES.** Frases de 8-14 palabras. Empiezas por lo que la persona ha hecho. Usted; "le propongo" dos veces; cierras con un paso con fecha. Nunca "debe".
> **TEXTO NUEVO.** Antes de la primera visita, le propongo tres cosas sencillas. […] Nos veremos el [FALTA: fecha]. Hasta entonces, nada de balanzas. Si tiene dudas, [FALTA: contacto del centro]. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> POR ACLARAR: ¿firmas con nombre o con "tu médica"? Los ejemplos difieren.
> MARCADORES SIN RELLENAR: 2

**Qué revisar antes de usarla.** Copia "ASÍ ESCRIBES" a un bloque "CONTEXTO DE VOZ" en tu biblioteca (caso 7). Cualquier consejo que no esté en tus puntos (un "venga en ayunas" que tú no diste) se borra: pregunta 6 del anexo B. Si salta "EJEMPLOS CON DATOS", el dato ya entró: protocolo del capítulo 3, el mismo día. Y "EJEMPLOS LIMPIOS" lo dice el modelo; la limpieza la hiciste tú.

**Riesgo principal y mitigación.** Adjuntar el archivo en vez de pegar el texto. Mitigación: texto plano, papel antes, conversación temporal, borrado.

### Caso 3 · La cadena de cuatro prompts

**Momento:** seguimiento de crónicos. **Herramienta:** asistente conversacional, una sola conversación nueva.

**Situación.** Un caso construido de cero con el perfil del hombre de las 11:20; no es él con los datos cambiados, es otro, para entrenar. Cuatro mensajes en este orden, en la misma conversación y con el mismo modelo; si se corta, se empieza por el 1. El tratamiento farmacológico no entra: lo decides tú, con la guía delante (capítulo 8).¹

¹ Declaración de transparencia: mantengo vínculos con Novo Nordisk, detallados al inicio del libro. Aquí los fármacos aparecen solo por principio activo y ninguno para la obesidad por su nombre; el mensaje del caso 6 vale para cualquier tratamiento que dé molestias digestivas al empezar; ese tratamiento va en el capítulo 8.

Prompt 1 · estructurar:

```
ROL: Eres médica de familia con experiencia en obesidad. Esto es un ejercicio sobre un caso sintético; no hay ninguna persona real y no debes tomar ni proponer decisiones para nadie.

CONTEXTO: Caso inventado, con cifras verosímiles pero no reales: hombre de 60-65 años, jubilado hace pocos meses, obesidad de grado II (IMC en torno a 37, cintura en torno a 119 cm), diabetes tipo 2 de varios años con metformina, artrosis de ambas rodillas que limita la marcha a unos veinte minutos, sin cardiopatía conocida. Desde la jubilación come a deshoras y picotea por las tardes; se describe "aburrido, no triste"; se levanta dos veces por la noche a orinar. Tensión en consulta 146/88 mmHg, sin diagnóstico previo de hipertensión. Analítica reciente: glucosa en ayunas 142 mg/dl, HbA1c 7,6 %, LDL 131 mg/dl, triglicéridos 210 mg/dl, creatinina 1,0 mg/dl con filtrado estimado por encima de 60 ml/min, ALT 58 U/l, GGT 64 U/l, TSH 2,4 mU/l. No hay más datos.

TAREA: Ordena el caso sin interpretarlo. Cuatro apartados: ANTECEDENTES Y TRATAMIENTO; SITUACIÓN ACTUAL (lo que cuenta la persona, con sus palabras); EXPLORACIÓN Y ANALÍTICA (cada cifra con su unidad, tal como te la di); LO QUE FALTA (lo que una médica de familia querría saber y no está, máximo diez puntos, cada uno como [FALTA: …]).

FORMATO: Cuatro listas con numeración continua. Ni una frase con "sugiere", "indica", "compatible con", "probable", ni ningún diagnóstico nuevo, ni calificativos sobre las cifras ("elevada", "alta", "normal"), ni rótulos que las agrupen ("hipertransaminasemia", "dislipemia"). Última línea, literal: "HECHOS: [n] · HUECOS: [n]".

RESTRICCIONES: No opines, no agrupes cifras bajo el nombre de un síndrome, no añadas ni redondees datos ni unidades. Sin fármacos que no estén en el caso ni nombres comerciales. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Prompt 2 · analizar:

```
Ahora, y solo ahora, analiza. Lista de PUNTOS ABIERTOS, máximo siete, cada uno con: qué se deduce; de qué hechos numerados sale; certeza ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, con explicaciones o estudios discrepantes) o BAJA (plausible, no lo afirmaría sin comprobarlo); y qué punto de LO QUE FALTA lo cambiaría. Reglas: no nombres ningún fármaco ni clase de fármacos, ni el que ya toma ni otros; no digas si el tratamiento actual basta, sobra o debe cambiarse; no digas si hay que derivar. Si un punto es "qué hacer con el tratamiento" o "a quién derivar", escríbelo solo como "DECISIÓN TERAPÉUTICA: la toma la médica" o "DECISIÓN DE DERIVACIÓN: la toma la médica", sin desarrollarlo. Última línea, literal: "ALTA: [n] · MEDIA: [n] · BAJA: [n] · FÁRMACOS O CLASES NOMBRADOS: [n]".
```

Prompt 3 · criticar:

```
Revisa tu respuesta anterior como si la hubiera escrito otra persona. Cinco listas: (1) SUPUESTOS: qué diste por hecho sin que estuviera en los hechos; (2) DEMASIADO SEGURO: qué certeza bajarías y por qué; (3) OTRA EXPLICACIÓN: para cada punto abierto, una alternativa que no nombraste; (4) OMITIDO: qué no miraste (ánimo, ideas de muerte, sueño, atracones, alcohol, fármacos que ya toma y que cambian el peso, causas secundarias) y debería estar; (5) LISTA DE PUNTOS ABIERTOS REVISADA: la lista anterior con los cambios aplicados, mismas reglas de certeza y de fármacos. Última línea, literal: "CAMBIOS QUE HARÍA EN LA LISTA DE PUNTOS ABIERTOS: [n] · FÁRMACOS O CLASES NOMBRADOS: [n]".
```

Prompt 4 · comunicar, dos veces:

```
Escribe dos textos con los mismos hechos, sin añadir ninguno, a partir de la LISTA DE PUNTOS ABIERTOS REVISADA. (A) NOTA PARA EL EQUIPO: máximo 120 palabras, en el orden problema, datos, pendiente; huecos como [FALTA: …]; certezas entre paréntesis; sin propuesta ni valoración de tratamiento ni de derivación ("valorar ajuste" tampoco). (B) TEXTO PARA LA PERSONA: unas 120 palabras sin contar las líneas literales, trato de usted, nivel de lectura de 12 años: qué hemos visto en general (sin nombrar diagnósticos, órganos ni pruebas concretas: "hay un par de cosas que quiero mirar con calma"), qué vamos a hablar en la próxima visita y una cosa concreta para esta semana sobre el movimiento y el horario de las comidas; sin cifras de peso ni de kilos, sin fármacos, sin culpa, sin "debería", sin frases de ánimo. Al pie de (B), en este orden y literal: "Si tiene dudas o algo no va bien antes de vernos, [FALTA: contacto del centro]. Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "DATOS EN (A) QUE NO ESTÁN EN LOS HECHOS: [n] · EN (B): [n] · FÁRMACOS O CLASES NOMBRADOS: [n]".
```

**Ejemplo abreviado de salida (prompt 4).**

> **(A)** Persona con obesidad de grado II y diabetes tipo 2, HbA1c 7,6 % (ALTA). ALT 58, GGT 64 U/l (causa por aclarar, BAJA) [FALTA: alcohol, serologías]. TA 146/88 en una toma [FALTA: tomas repetidas o AMPA]. Pendiente: ánimo con cribado, atracones, sueño, alcohol. DECISIÓN TERAPÉUTICA: la médica […]
> **(B)** Hemos visto que el azúcar está algo más alto de lo que nos gustaría y hay un par de cosas que quiero mirar con calma en la próxima visita; también hablaremos de cómo duerme, de cómo anda de ánimo y de las tardes. Esta semana le propongo dos cosas: caminar por tiempo, dos ratos cortos al día, y cenar a una hora fija. […] Si tiene dudas o algo no va bien antes de vernos, [FALTA: contacto del centro]. Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> DATOS EN (A) QUE NO ESTÁN EN LOS HECHOS: 0 · EN (B): 0 · FÁRMACOS O CLASES NOMBRADOS: 0

**Qué revisar antes de usarla.** La nota (A), con los hechos del prompt 1 delante: lo que no esté allí, fuera. Y (A) no se pega en la historia: te dice qué preguntar. El recuento de fármacos, con el texto delante: "agonistas", "inhibidores", "estatina", "ajuste del tratamiento" son un 1 aunque el modelo escriba 0. El texto (B): pie entero, contacto en tu sistema, anexo B.

Mira lo que la máquina no echó en falta. Lo que un médico de familia pediría primero (tabaco, AST y plaquetas para el FIB-4, albúmina/creatinina en orina, tomas repetidas de tensión o AMPA, fondo de ojo y pies) lo completas tú con la guía (GIRO 2024; capítulo 8). Para la nicturia de un hombre de sesenta y pico propone apnea; la próstata va antes, y el azúcar también. Lo que la máquina no nombra lo nombras tú.

**Riesgo principal y mitigación.** Que el rigor aparente de cuatro pasos te haga fiarte más que de uno: el paso 3 lo hace la misma máquina que escribió el 2. Si el eslabón 2 nombra un fármaco, lo tachas y sigues: ha hecho lo que hace internet.

### Caso 4 · "No cierres diagnóstico"

**Momento:** consulta (entrenar el criterio). **Herramienta:** modelo de razonamiento.

**Situación.** Una ganancia de peso reciente es una de las cinco cosas del capítulo 1 donde omitir cuesta caro. Este caso sintético entrena lo contrario del cierre prematuro. El modelo lista hipótesis; tú decides qué explorar y cuándo derivar (capítulo 8).

```
[Si tu herramienta no tiene razonador, esta es la primera línea: "Antes de responder, escribe tu razonamiento paso a paso; solo después escribe las cuatro listas."]

ROL: Eres médica de familia. Esto es un ejercicio de razonamiento sobre un caso inventado; no hay ninguna persona real y no debes tomar ni proponer decisiones para nadie.

CONTEXTO: Caso sintético, sin correspondencia con nadie: mujer de 45-55 años, sin obesidad previa conocida, que ha ganado en torno a diez kilos en menos de un año sin identificar cambios claros en lo que come ni en lo que se mueve. Refiere cansancio, estreñimiento, piernas hinchadas al final del día, ánimo bajo "desde que pasó todo" (no concreta qué), reglas irregulares en el último año y un tratamiento nuevo desde hace unos meses cuyo nombre no consta. No hay exploración ni analítica. No hay más datos.

TAREA: No cierres ningún diagnóstico. Cuatro listas: (1) LO QUE HAY: lo que está en el caso, numerado, sin adjetivos, sin fusionar dos hechos en uno. (2) LO QUE SE DEDUCE: cada hipótesis que explicaría la ganancia de peso, con los hechos que la apoyan entre paréntesis y una certeza con uno de estos cuatro valores: ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, con explicaciones o estudios discrepantes), BAJA (plausible, no lo afirmaría sin comprobarlo) o NO LO SÉ (no puedo situarla ni en BAJA sin un dato; di cuál). Incluye las poco probables que una médica de familia no puede dejar de considerar, y di qué dato cambiaría cada una. (3) LO QUE FALTA: qué falta, ordenado por lo que más cambiaría el razonamiento, sin inventarlo y sin convertirlo en una petición de pruebas. (4) LO QUE ALGUIEN ESCRIBIRÍA CON PRISA: frases que alguien con prisa escribiría sobre este caso y que los hechos no sostienen, con una línea de por qué.

FORMATO: Cuatro listas; la 1 sin tope; las otras, máximo ocho puntos. Nada más que las cuatro listas. Última línea, literal: "HIPÓTESIS: [n] · EN ALTA: [n] · NO LO SÉ: [n]".

RESTRICCIONES: Sin diagnósticos cerrados, sin tratamientos ni clases de fármacos, sin nombres comerciales, sin plan de pruebas. No añadas datos al caso: si los necesitas, van en la lista 3. No atribuyas la ganancia a "hábitos" sin un hecho que lo sostenga. Usa "persona con obesidad" si procede. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida (listas 2 y 4).**

> LO QUE SE DEDUCE: 1. Hipotiroidismo (hechos 2, 3, 4, 7): MEDIA; lo cambiaría la TSH. 2. Efecto del tratamiento nuevo (hecho 8): NO LO SÉ; hace falta el nombre del fármaco. 3. Transición menopáusica (hechos 1, 7): MEDIA; explica parte, no diez kilos en un año. 4. Depresión (hecho 6): MEDIA. 5. Trastorno por atracón: BAJA; hay que preguntarlo. 6. Causa cardiaca o renal del edema (hecho 5): BAJA; disnea la subiría por el lado cardiaco; proteinuria, por el renal. 7. Hipercortisolismo (hechos 2, 5, 6): BAJA; estrías violáceas o debilidad proximal lo subirían.
> LO QUE ALGUIEN ESCRIBIRÍA CON PRISA: "Es la menopausia" (explica parte, no descarta el resto). "Algo habrá cambiado en sus hábitos" (ningún hecho). "El antidepresivo la ha hecho engordar" (no sabemos que sea un antidepresivo).
> HIPÓTESIS: 7 · EN ALTA: 0 · NO LO SÉ: 1

**Qué revisar antes de usarla.** Que nada esté en ALTA: aquí sería un error de calibración. Que el fármaco sea lo primero de LO QUE FALTA: es el dato más barato y el que más cambia (Wharton 2020; Wharton 2018).

Lo que no sale de esa consulta sin hacerse: nombre del fármaco, TSH, tensión, piernas y piel, tira de orina si hay edemas, y dos preguntas que pocos modelos hacen solos: atracones e ideas de muerte. La octava que casi nunca pone: con reglas irregulares a esa edad, el embarazo se descarta antes de pedir nada. Hipercortisolismo, edemas con falta de aire o una tiroides muy alterada se derivan (capítulo 8).

**Riesgo principal y mitigación.** Que el ejercicio se convierta en consulta y un día pegues a alguien real porque "es parecido". Mitigación: solo casos construidos de cero (capítulo 2). Y que siete hipótesis te anclen a siete y dejes de pensar en la octava.

### Caso 5 · El consejo breve de siete minutos [AP]

**Momento:** consulta. **Herramienta:** cualquier asistente conversacional.

**Situación.** Viene por otro motivo y al final queda un minuto. Treinta segundos bien dichos los aceptan cuatro de cada cinco personas y abren puertas si ofrecen algo concreto (Aveyard 2016): por eso el guion termina en un paso. El molde es el de la entrevista motivacional: pedir permiso, nombrar sin juzgar, preguntar y pactar (Miller 2013), con la persona primero (Kyle 2014).

```
ROL: Eres médica de familia con formación en entrevista motivacional y en lenguaje centrado en la persona.

CONTEXTO: Atención Primaria en España, consultas de siete minutos. Intervención para decir en voz alta al final de una visita por otro motivo, a una persona con obesidad a la que aún no he ofrecido abordar el peso. Hablo yo; no es un texto para entregar. Sin ninguna persona concreta detrás.

TAREA: Una intervención con exactamente tres partes: dos frases, la primera pide permiso para hablar del peso, con una salida digna si dice que no, y la segunda nombra la obesidad como enfermedad con biología detrás y sin culpa; una pregunta abierta que deje la decisión a la persona; y un siguiente paso pactado, pequeño, con fecha relativa ("en dos o tres semanas"). Después, tres variantes completas para cuando la persona responde: (a) "ya probé todo"; (b) "no tengo tiempo"; (c) "mi problema es la ansiedad".

FORMATO: Bloque BASE y bloques (a), (b), (c), cada uno con sus tres partes marcadas; máximo 60 palabras por bloque; trato de [usted (por defecto) / tú]; que pueda decirse en menos de treinta segundos. Nada más que los cuatro bloques. Última línea, literal: "PALABRAS PROHIBIDAS ENCONTRADAS: [n]".

RESTRICCIONES: Palabras prohibidas, incluidas sus variantes y derivados: "obeso/a", "gordo/a", "debería", "esfuerzo" (y "esforzarse"), "fuerza de voluntad", "disciplina" (y "disciplinado"), "solo tiene que", "fácil". Sin objetivos de peso, sin dietas, sin fármacos ni nombres comerciales, sin promesas de resultado. En (c), no des consejo sobre la ansiedad ni técnicas: reconócela y abre la puerta a valorarla. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> **BASE.** "¿Le parece si un día hablamos del peso? Si prefiere que no, lo dejamos aquí. No es una cuestión de voluntad: hay una biología detrás, y se trata." Pregunta: "¿Es algo que le preocupe a usted?" Paso: "Si quiere, pido una cita en dos o tres semanas solo para eso."
> **(a) "Ya probé todo".** "Lo creo. Y que todo funcionara un tiempo y luego no es justo lo que hace el cuerpo: no falló usted, falló el método." [POR ACLARAR: frase de la autora] […]
> PALABRAS PROHIBIDAS ENCONTRADAS: 0

**Qué revisar antes de usarla.** Léelo en voz alta: si no lo dirías con tu cara, no es tuyo. En (c), solo la puerta; si hay atracones, eso va antes que el peso (capítulo 8). No lleva disclaimer impreso: lo dices tú, en persona, y esa es la valoración clínica individual.

**Riesgo principal y mitigación.** Que el guion se recite; la persona lo nota. Mitigación: tres versiones, una elegida, y cambiarla cada pocos meses.

### Caso 6 · Mensaje entre visitas [AP]

**Momento:** seguimiento de crónicos. **Herramienta:** asistente conversacional, sin identificadores.

**Situación.** Entre dos visitas pasan semanas y la persona está sola con lo que pactó. Un mensaje corto sostiene más que un consejo largo.

```
ROL: Eres una redactora de mensajes breves para pacientes de Atención Primaria, con conocimientos de lenguaje centrado en la persona.

CONTEXTO: Soy médica de familia en España. Quiero plantillas de mensaje de refuerzo entre dos visitas, para el canal del centro o para leer en una llamada. Son genéricas: sin nombre, fechas ni cifras de nadie. Solo se admiten tres marcadores, que relleno yo fuera de esta conversación: [FALTA: paso pactado], [FALTA: fecha de la próxima visita] y [FALTA: contacto del centro]. Sin saludo con nombre: el saludo lo pongo yo. Dos situaciones: (1) persona con obesidad que acordó empezar a caminar por tiempo y lleva dos o tres semanas; (2) persona que ha empezado un tratamiento nuevo que puede dar molestias digestivas los primeros días, sin nombrar el tratamiento.

TAREA: Un mensaje por situación que: reconozca lo hecho sin calificarlo de éxito ni de fracaso; recuerde el siguiente paso como [FALTA: paso pactado]; y remita a [FALTA: contacto del centro] si hay dudas. En (2), incluye literalmente y entera esta línea: "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo."

FORMATO: Dos mensajes de máximo 90 palabras cada uno sin contar las líneas literales, trato de usted, nivel de lectura de 12 años, sin emoticonos ni negritas. Al pie de cada uno, si se envía por escrito, literal: "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "MARCADORES: [n] · FRASES QUE EVALÚAN: [n]", donde una frase que evalúa es cualquiera que califique lo hecho o a la persona ("enhorabuena", "muy bien", "orgullosos", "fenomenal", "una pena").

RESTRICCIONES: Sin felicitaciones ni mención de peso, balanza o cifras. Sin "debería", sin "ánimo, usted puede", sin culpa si no se ha cumplido. Sin nombres de fármacos ni comerciales, sin consejo sobre dosis ni sobre qué comer: eso se dio en consulta. No inventes teléfonos, correos ni "responda a este mensaje": el contacto es el marcador. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> **(2)** Los primeros días de un tratamiento nuevo pueden traer molestias de estómago, que suelen ir a menos. Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo. Lo que acordamos: [FALTA: paso pactado]. Si tiene dudas, [FALTA: contacto del centro]. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> MARCADORES: 2 · FRASES QUE EVALÚAN: 0

**Qué revisar antes de usarla.** La línea de seguridad, literal y entera, como la del 112 en el caso 1. Las frases que evalúan las cuentas tú: el modelo escribió "enhorabuena" y contó cero más de una vez. Y si la persona contesta con un efecto adverso, el siguiente mensaje no lo escribe la máquina: es tu frase del capítulo 3, y notificas.

**Riesgo principal y mitigación.** Enviar la plantilla con el marcador sin rellenar, o rellenarlo en el chat "para que quede mejor". Mitigación: los huecos se rellenan en tu sistema.

### Caso 7 · Mi biblioteca de prompts en Markdown

**Momento:** administración. **Herramienta:** un editor de texto. Sin IA.

**Situación.** El tercer martes que reescribes el mismo prompt desde cero has perdido más tiempo del que la IA te ahorró. Los que funcionan se guardan, se versionan y se comparten. Yo los guardo en Markdown: texto plano con marcas mínimas (almohadilla para el título, tres acentos graves para el código) que leen igual una persona y el modelo. Un bloc de notas vale.

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

Tres reglas:

- **Versiona, no sobrescribas.** Si cambias una línea y la salida mejora, es v2 con fecha y por qué. Si la herramienta cambia de modelo, anótalo: el mismo prompt puede dejar de funcionar (capítulo 2).
- **Un nombre que diga lo que hace:** `consejo-breve-7min_v2.md`. Nada de "prompt final definitivo 3".
- **Comparte la ficha, nunca la conversación.** El prompt no lleva datos; la conversación puede llevarlos. Una carpeta del centro con las fichas es una biblioteca de equipo.

**Qué revisar antes de usarla.** Que cada ficha tenga "Datos que admite" y "Qué revisar" rellenos. Sin "Probada por" con fecha, no entra en la carpeta del centro. Una vez al trimestre, comprueba el modelo de las que más usas. Los setenta prompts del anexo A usan esta ficha.

**Riesgo principal y mitigación.** Que alguien use una ficha sin leer "Qué revisar", porque "si está en la carpeta, funciona". Mitigación: el riesgo en la cabecera y la firma de quien la probó.

---

## Caso ilustrativo, no real: arquetipo compuesto

> Esta viñeta combina rasgos de varios hombres con obesidad, diabetes tipo 2 y artrosis que llegan a la consulta tras jubilarse. No hay profesión, municipio, fechas ni cifras que permitan reconocer a nadie; las analíticas del caso 3 son inventadas. Es el mismo caso sintético que corre la cadena: lo construí para eso.

Tiene entre sesenta y sesenta y cinco años. Se jubiló hace unos meses. Obesidad de grado II, diabetes tipo 2 con metformina, las dos rodillas con artrosis. Viene a la segunda visita con la hoja del caso 1 doblada en cuatro y anotada a lápiz. "La piscina, los martes. Que está vacía."

Yo vengo con lo que la cadena del caso 3 me dejó semanas antes: no qué hacer, sino la lista de lo que suelo olvidar preguntar. Alcohol: una cerveza al mediodía, "a veces dos, que ahora hay tiempo". Duerme mal y se levanta dos veces. Ronca, dice su mujer, y se duerme después de comer: apunto el cribado de apnea, que con su tensión y su peso no se puede dejar pasar. Por la orina de noche, a su edad, antes que nada la próstata.

Por la tarde, "desde las seis hasta la cena, lo que pille". Las preguntas de ánimo, porque "aburrido, no triste" es un adjetivo suyo, no un cribado mío: hoy no hay más que un día demasiado largo. Segunda toma de tensión, alta otra vez: que se la tome en casa una semana, mañana y noche, y la traiga.

Lo que hablamos no es de kilos. Es de las seis de la tarde: el tiempo es lo que tiene y lo que le sobra. Pactamos la piscina martes y jueves, y cenar a las nueve con algo preparado a las seis. Le doy el texto (B) del caso 3, releído frase por frase contra lo que acabo de explorar y corregido donde no coincidía, en usted, con mi firma. Y, como siempre, una frase: nada que permita saber quién es él entra nunca en esas herramientas.

"¿Y lo del azúcar?", pregunta en la puerta. Lo de las seis ayuda, le digo, y no es lo único: con la analítica decidimos si hay que ajustar el tratamiento, guía en mano (GIRO 2024; capítulo 8), y eso no depende de lo que usted haga bien o mal. No es falta de voluntad. Es biología, y es una agenda vacía a las seis de la tarde. Las dos cosas se tratan.

---

## En 60 segundos

1. Un prompt pobre deja las decisiones a la estadística de internet: kilos objetivo, culpa y marcas.
2. Cinco piezas en el mismo orden: rol, contexto, tarea, formato, restricciones. En el contexto vive la calidad.
3. Tres técnicas: tus textos anonimizados como ejemplo, pedir los pasos y encadenar estructurar, analizar, criticar y comunicar.
4. Cada respuesta pasa por cinco preguntas: fidelidad, priorización, calibración, confusores y acción segura. Si suena demasiado segura, probablemente lo es.
5. Lo que funciona se guarda en una ficha con versión, fecha y modelo; se comparte la ficha, nunca la conversación.

## Hazlo hoy · 10 minutos

Te propongo cuatro pasos:

1. **(2 min)** Pega el prompt pobre del caso 1 en un asistente de consumo. Subraya cada kilo, cada caloría y cada "consulte con su médico".
2. **(4 min)** En una conversación nueva, pega el estructurado y pásale la rúbrica a las dos salidas.
3. **(3 min)** Guarda el estructurado con la ficha del caso 7, en v1, con fecha y modelo.
4. **(1 min)** Elige qué texto tuyo vas a anonimizar mañana para el caso 2. Solo elegirlo.

Mañana, a las 11:20, alguien te dirá que ahora tiene tiempo y no sabe por dónde empezar. Esto no lo hace la IA por ti: te da los minutos para hacerlo tú. Y las palabras que le pidas serán las tuyas, o serán las de un folleto.

---

## Referencias

**Modelos de lenguaje y técnicas de instrucción**

1. Brown TB, Mann B, Ryder N, Subbiah M, Kaplan J, Dhariwal P, et al. Language models are few-shot learners. En: Advances in Neural Information Processing Systems 33 (NeurIPS 2020); 2020. p. 1877-901. arXiv:2005.14165.
2. Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, et al. Chain-of-thought prompting elicits reasoning in large language models. En: Advances in Neural Information Processing Systems 35 (NeurIPS 2022); New Orleans (LA); 2022. p. 24824-37. arXiv:2201.11903.
3. Kojima T, Gu SS, Reid M, Matsuo Y, Iwasawa Y. Large language models are zero-shot reasoners. En: Advances in Neural Information Processing Systems 35 (NeurIPS 2022); New Orleans (LA); 2022. p. 22199-213. arXiv:2205.11916.
4. Liu NF, Lin K, Hewitt J, Paranjape A, Bevilacqua M, Petroni F, et al. Lost in the middle: how language models use long contexts. Trans Assoc Comput Linguist. 2024;12:157-73. doi:10.1162/tacl_a_00638

**Actividad física, artrosis de rodilla y diabetes**

5. Bannuru RR, Osani MC, Vaysbrot EE, Arden NK, Bennell K, Bierma-Zeinstra SMA, et al. OARSI guidelines for the non-surgical management of knee, hip, and polyarticular osteoarthritis. Osteoarthritis Cartilage. 2019;27(11):1578-89. doi:10.1016/j.joca.2019.06.011
6. Moseng T, Vliet Vlieland TPM, Battista S, Beckwée D, Boyadzhieva V, Conaghan PG, et al. EULAR recommendations for the non-pharmacological core management of hip and knee osteoarthritis: 2023 update. Ann Rheum Dis. 2024;83(6):730-40. doi:10.1136/ard-2023-225041
7. Colberg SR, Sigal RJ, Yardley JE, Riddell MC, Dunstan DW, Dempsey PC, et al. Physical activity/exercise and diabetes: a position statement of the American Diabetes Association. Diabetes Care. 2016;39(11):2065-79. doi:10.2337/dc16-1728

**Ganancia de peso, causas secundarias y fármacos**

8. Wharton S, Raiber L, Serodio KJ, Lee J, Christensen RA. Medications that cause weight gain and alternatives in Canada: a narrative review. Diabetes Metab Syndr Obes. 2018;11:427-38. doi:10.2147/DMSO.S171365
9. Wharton S, Lau DCW, Vallis M, Sharma AM, Biertho L, Campbell-Scherer D, et al. Obesity in adults: a clinical practice guideline. CMAJ. 2020;192(31):E875-E891. doi:10.1503/cmaj.191707
10. Sociedad Española para el Estudio de la Obesidad (SEEDO). Guía Española GIRO: Guía española del manejo Integral y multidisciplinaR de la Obesidad en personas adultas. 2.ª ed. Lecube A, coordinador. Madrid: SEEDO; noviembre de 2024. Disponible en: https://www.seedo.es/images/site/giro/GUIA-GIRO-2a-edicin_26NOV2024.pdf [VERIFICAR ISBN en créditos del PDF; candidato 978-84-09-65969-2]

**Comunicación y consejo breve**

11. Miller WR, Rollnick S. Motivational interviewing: helping people change. 3.ª ed. Nueva York: Guilford Press; 2013. ISBN 978-1-60918-227-4. Edición en español: La entrevista motivacional: ayudar a las personas a cambiar. 3.ª ed. Asensio Fernández M, traductora. Barcelona: Paidós; 2015. ISBN 978-84-493-3139-8.
12. Aveyard P, Lewis A, Tearne S, Hood K, Christian-Brown A, Adab P, et al. Screening and brief intervention for obesity in primary care: a parallel, two-arm, randomised trial. Lancet. 2016;388(10059):2492-500. doi:10.1016/S0140-6736(16)31893-1
13. Kyle TK, Puhl RM. Putting people first in obesity. Obesity (Silver Spring). 2014;22(5):1211. doi:10.1002/oby.20727
