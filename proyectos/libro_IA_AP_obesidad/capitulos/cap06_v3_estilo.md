# Capítulo 6 · Educar a la persona con obesidad

**Materiales que se entienden, en su idioma y sin culpa.**

Le di una hoja de recomendaciones de tres páginas. Volvió a los tres meses: no la había entendido. Tenía razón; la había escrito para mí.

Estaba bien escrita: fisiología, guía debajo, mi nombre. Le faltaba quien iba a leerla: frases de treinta palabras, tres ideas por párrafo, un "debe" en cada línea. Asintió, se la llevó doblada y la guardó en un cajón.

Lo que aprendí no fue a escribir más corto: fue a preguntar de vuelta. Un material educativo no es lo que yo escribo; es lo que la persona entiende. La máquina escribe rápido y en cualquier idioma. Comprobar que se entiende, sin culpa y sin error, sigue siendo mío.

*Como todas las escenas de consulta de este libro, es una composición de varias personas.*

## Lo que te vas a llevar

- Un examen para cualquier hoja tuya y tres preguntas de vuelta para saber, en consulta, si se ha entendido.
- Una traducción con red: retraducción, comparación y un hablante antes de entregar nada.
- Siete prompts, de la hoja al cartel y a la etiqueta; lo que llega a la persona lleva las tres líneas y tu revisión.

---

## Primera parte · La hoja que escribí para mí

Casi la mitad de la población de los ocho países de la primera encuesta europea de alfabetización en salud tenía dificultades para entender y usar información de salud; en España, casi seis de cada diez (Sørensen 2015 [VERIFICAR cifra española en la figura 2]). No es solo un problema de estudios: es de cómo escribimos. En obesidad se suma otra cosa: años de hojas que regañan.

Las hojas de los centros fallan como la mía: frases largas, tres ideas por párrafo, tono de instrucción, y además las palabras que solo usamos nosotros. La persona asiente, se la lleva y no vuelve.

Y el asentir engaña: quien no ha entendido no lo dice, por vergüenza, por prisa o por un idioma a medias. Solo se sabe pidiendo que lo cuente con sus palabras. En un estudio de visitas grabadas, en diabetes, los médicos que comprobaban así lo explicado tenían pacientes con mejor control, y solo lo hacían en una de cada cinco visitas (Schillinger 2003). Se llama teach-back; yo lo llamo pregunta de vuelta.

---

## Segunda parte · Lo que la máquina hace bien con la comprensión y lo que no

Con un texto para pacientes, un modelo de lenguaje hace cinco cosas bien: **acortar** frases, **reescribir** a un nivel de lectura, **cambiar** de registro, **traducir** y **proponer** preguntas de vuelta. En segundos, y sin cansarse a la décima hoja.

Lo que no hace: saber qué entiende esta persona, si la traducción dice lo mismo o qué palabra hiere en esta consulta. "Nivel de lectura de 12 años" no es una garantía: es un encargo, y se comprueba. En español, el índice de Flesch-Szigriszt cuenta sílabas por palabra y palabras por frase, y la escala INFLESZ lo interpreta (Barrio-Cantalejo 2008); el caso 1 pide lo mismo y te manda contar una muestra a mano.

La regla del capítulo: lo que sale de la máquina se comprueba con la persona y, en otro idioma, también con un hablante. Adaptar materiales a la alfabetización y al idioma con pasos comprobables lo traigo de mi formación en IA; las hojas son de esta consulta.

---

## Tercera parte · Las tres líneas y el disclaimer, también en otro idioma

Todo texto que llega a la persona termina igual (capítulos 3 y 4): el contacto, como hueco "[FALTA: contacto del centro]"; cuándo no esperar, con "urgencias o 112", solo si toca síntomas o tratamiento; y el aviso de material informativo, en usted si se imprime o se envía. Lo nuevo es el idioma: las tres líneas no se improvisan en cada hoja; se validan una vez y se pegan (caso 2). Una hoja en árabe con la línea de urgencias mal traducida es peor que ninguna.

Los casos 1, 2 y 4 llegan a la persona: tres líneas. El 7, cuando se entrega, dos: no toca síntomas. Los guiones que dices tú (3 y 5) y el cartel (6) quedan fuera. Ninguna hoja lleva datos de nadie: ninguna necesita contrato de tratamiento de datos (capítulo 3).

---

## Siete casos para que se entienda

Mismo molde que en los capítulos 4 y 5; ninguno admite datos identificables. POR ACLARAR la contestas tú fuera del chat; [FALTA: …] lo rellenas tú fuera de la IA (capítulo 3). El modelo no rellena ninguno.

Conversación nueva, memoria apagada; el 7 se borra al terminar, por la imagen. Hoy se pegan igual en Gemini, ChatGPT y Claude; comprueba la versión vigente. Ninguno pide razonador (capítulo 2); el 7 necesita que la herramienta lea imágenes. Ficha del capítulo 4, caso 7, con "Higiene: sí" en el 7 y "Probada por" con fecha.

### Caso 1 · La hoja pasa el examen: legibilidad y pregunta de vuelta

**Momento:** consulta. **Herramienta:** consumo, sobre una hoja genérica tuya.

**Situación.** La hoja "¿Por qué recupero el peso?" del capítulo 1 (caso 5) no se vuelve a escribir: se examina. Entra su versión A, o cualquier hoja tuya sin datos; el prompt cuenta lo que yo no tengo tiempo de contar y devuelve tres preguntas de vuelta. Antes de pegar una hoja tuya, quítale tu nombre, el del centro y el teléfono, y deja el hueco: la línea (0) para si los ve, y hace bien; el contacto vuelve a entrar en tu sistema, no en el chat.

```
ROL: Eres una redactora de materiales para pacientes, experta en alfabetización en salud y en lenguaje llano en español de España.

CONTEXTO: Soy médica de familia en España. Te pego una hoja GENÉRICA que entrego a personas con obesidad; no lleva ningún dato de nadie. Quiero saber si se entiende y, si no, una versión que se entienda sin cambiar lo que dice. TRATO: [usted por defecto / tú]. LÍNEA DE URGENCIAS, la elijo yo: [ninguna]. Si no es "ninguna", será una de estas dos, literal: "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo." (en tú: "Si no toleras líquidos, tienes dolor fuerte de tripa, te mareas o te encuentras mal, no esperes: urgencias o 112. Y ante cualquier molestia, pide cita y lo vemos, o te llamo yo.") o "Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112." (en tú: "Si notas dolor en el pecho, falta de aire o mareo, no esperes: urgencias o 112.").

HOJA: [pega la hoja sin su línea de "Revisado por" ni de fecha; por ejemplo, la versión A de "¿Por qué recupero el peso?" del capítulo 1]

TAREA, en este orden:
(1) EXAMEN de la hoja tal cual, sin contar sus líneas finales de contacto, urgencias o aviso si las trae: número de frases (una frase termina en punto, interrogación o exclamación); palabras por frase, de media; palabras largas (más de tres sílabas), listadas; palabras técnicas (nombres de hormonas, órganos, pruebas o fármacos y términos que solo usa el personal sanitario; "biología", "enfermedad crónica", "tratamiento" y "seguimiento" no lo son), listadas; cifras y porcentajes; frases con más de una idea; y las palabras de esta lista que aparezcan: "debe", "tiene que", "no debería", "culpa", "fracaso", "esfuerzo", "voluntad", "disciplina", "obeso", "obesa". Las frases "No es culpa suya" (o "no es culpa tuya") y "No es falta de voluntad" se conservan tal cual y no cuentan.
(2) HOJA REESCRITA solo si el examen encuentra algo: mismas ideas, sin añadir ni quitar contenido, frases de 15 palabras como máximo, una idea por párrafo, sin palabras técnicas, sin cifras y sin las palabras de la lista salvo en las dos frases que las niegan. Si ya cumple, escribe "NO HACE FALTA REESCRIBIR".
(3) TRES PREGUNTAS DE VUELTA, para elegir yo una en consulta, sobre lo que más importa de la hoja, cada una empezando por "Para saber si me he explicado bien," y pidiendo que la persona lo cuente con sus palabras a alguien de su confianza; ninguna con "¿ha entendido?", "qué ha entendido", "repítame" ni "resúmame".

FORMATO, en este orden:
(0) Una línea: "HOJA SIN DATOS" o "HOJA CON DATOS: BORRA ESTA CONVERSACIÓN" si contiene nombre, fecha, centro, teléfono o cualquier dato individual; en ese caso, para.
(1) El examen, en siete líneas.
(2) La hoja reescrita, máximo 120 palabras sin contar las líneas literales, sin negritas ni emoticonos, terminada, en este orden y literal, con: "Si tiene dudas, [FALTA: contacto del centro]." (en tú, "Si tienes dudas"); la LÍNEA DE URGENCIAS que te he dado, solo si no es "ninguna"; y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." (en tú, "tu profesional sanitario"). Si la LÍNEA DE URGENCIAS es "ninguna", no añadas ninguna línea de urgencias, de síntomas ni de "consulte con su médico", aunque te parezca prudente.
(3) Las tres preguntas.
(4) Última línea, literal: "FRASES: [n] · PALABRAS POR FRASE: [n] · PALABRAS LARGAS: [n] · PALABRAS TÉCNICAS: [n] · PALABRAS DE LA LISTA: [n]", contadas sobre la hoja reescrita sin sus líneas literales, o sobre la original si no hizo falta; las dos últimas tienen que ser 0.

RESTRICCIONES: No añadas consejos, síntomas, tratamientos ni frases de ánimo que no estén en la hoja. Sin nombres de fármacos, ni comerciales ni por principio activo ni por clase; sin objetivos de peso. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida (versión A del capítulo 1, en usted, sin línea de urgencias).**

> HOJA SIN DATOS
> EXAMEN. 10 frases; 7 palabras por frase; largas: biología, energía, enfermedad, tratamiento, seguimiento; técnicas: ninguna; cifras: ninguna; frases con más de una idea: 1; palabras de la lista: ninguna fuera de "No es culpa suya" y "no es falta de voluntad".
> HOJA REESCRITA. Por qué vuelve el peso. Su cuerpo defiende su peso. Cuando baja kilos, le da más hambre y gasta menos energía. No es culpa suya. Es biología. […] Si tiene dudas, [FALTA: contacto del centro]. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> PREGUNTAS. Para saber si me he explicado bien, ¿cómo le contaría a alguien de su confianza por qué vuelve el peso después de una dieta? […]
> FRASES: 10 · PALABRAS POR FRASE: 7 · PALABRAS LARGAS: 5 · PALABRAS TÉCNICAS: 0 · PALABRAS DE LA LISTA: 0

**Qué revisar antes de usarla.** Cuenta tú una muestra: tres frases, palabras con el dedo; el modelo cuenta mal y redondea bien. Las dos frases que niegan la culpa se quedan; si aparecen "no depende de usted", "no está en su mano", "no puede hacer nada" o "usted no ha hecho nada mal", no dicen lo mismo: así niega la culpa la máquina, quitándole a la persona lo que sí es suyo, y esa frase la escribes tú.

Las palabras largas no son un fallo: la persona tiene que poder leerlas; más de cinco por cada cien, y la hoja pesa. Con LÍNEA DE URGENCIAS "ninguna", busca "consulte" y "112": si están, la máquina ha decidido por ti que la hoja toca síntomas. Si la persona no sabe contarlo, la que se explicó mal fui yo: se repite con otras palabras, no más alto, y se vuelve a preguntar. Una pregunta por visita, la que toca lo que hay que hacer.

**Riesgo principal y mitigación.** Que la hoja "apta" sustituya a la pregunta de vuelta. Mitigación: el examen dice si se puede leer; solo la persona dice si se ha entendido.

### Caso 2 · La misma hoja en árabe, rumano e inglés, con retraducción [AP]

**Momento:** consulta. **Herramienta:** consumo, dos conversaciones: la segunda con otro modelo, o el mismo sin memoria.

**Situación.** Traducir es fácil. Saber si la traducción dice lo mismo, no: yo no leo árabe ni rumano, y un error en la línea del 112 no lo vería nunca. Tres nudos: se traduce (A); en conversación nueva y sin el original, se retraduce al español (B); se comparan las dos versiones. Es la retraducción de toda la vida (Brislin 1970), con la máquina haciendo los dos viajes. Después la lee un hablante nativo: el mediador intercultural, si lo hay; nunca un familiar menor.

```
ROL: Eres una traductora sanitaria profesional de español a [IDIOMA; por ejemplo: árabe estándar moderno / rumano / inglés], para personas sin estudios sanitarios.

CONTEXTO: Soy médica de familia en España. Te pego una hoja GENÉRICA para personas con obesidad, ya revisada por mí, sin ningún dato de nadie. Un hablante nativo la leerá antes de entregarse. TRATO: [usted; en el idioma, su forma de respeto]. LÍNEAS FINALES EN [IDIOMA]: [pega aquí las tres líneas ya traducidas y validadas por un hablante o por la versión oficial de tu servicio de salud; si aún no las tienes, escribe TRADÚCELAS].

HOJA: [pega la hoja que pasó el caso 1, con sus líneas finales]

TAREA: Traduce la hoja entera, frase por frase, con el mismo orden y el mismo número de frases; sin resumir, sin unir frases, sin añadir explicaciones ni notas culturales, sin cambiar de registro. Las líneas finales ("Si tiene dudas, [FALTA: contacto del centro].", la de urgencias si la hay, y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.") no se traducen: se copian tal cual de LÍNEAS FINALES EN [IDIOMA]. Solo si he escrito TRADÚCELAS las traduces tú, con tres reglas: lo que va entre corchetes se copia en español, tal cual y entre corchetes, sin traducirlo; "urgencias o 112" conserva el número escrito con las cifras 112, no con otras cifras ni en letras; y "no espere" se traduce como una orden de no demorarse, no como una cortesía. Si una palabra no tiene equivalente llano, elige la más corriente; como máximo en dos palabras puedes poner el español entre paréntesis, y dime cuáles en una línea aparte.

FORMATO, en este orden:
(0) Una línea: "HOJA SIN DATOS" o "HOJA CON DATOS: BORRA ESTA CONVERSACIÓN" si contiene nombre, fecha, centro, teléfono o cualquier dato individual; en ese caso, para.
(1) La traducción, sin el original al lado, sin negritas ni emoticonos.
(2) Última línea, literal: "FRASES EN ESPAÑOL: [n] · FRASES TRADUCIDAS: [n] · CORCHETES: [n] · '112': [n] · LÍNEAS FINALES: COPIADAS / TRADUCIDAS": una frase termina en punto, interrogación o exclamación y las líneas finales cuentan; corchetes y 112 se cuentan en la traducción, con la grafía 112, y tienen que coincidir con los del original.

RESTRICCIONES: No añadas ni quites contenido. Sin nombres de fármacos, sin cifras que no estén, sin consejos. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida (paso A, árabe; la hoja del caso 1: diez frases más las tres líneas).**

> FRASES EN ESPAÑOL: 13 · FRASES TRADUCIDAS: 13 · CORCHETES: 1 · '112': 0 · LÍNEAS FINALES: COPIADAS

En una conversación nueva, con otro modelo o con la memoria apagada:

```
ROL: Eres una traductora sanitaria profesional de [IDIOMA] a español de España.

CONTEXTO: Te pego un texto informativo genérico para pacientes, en [IDIOMA], sin datos de nadie. No conoces el original en español y no debes imaginarlo. Después, en otro mensaje, te pegaré ese original para compararlos.

TEXTO: [pega la traducción del paso A]

TAREA: (1) Tradúcelo al español, frase por frase, fiel al sentido: sin embellecer, sin corregir lo que te parezca raro, sin añadir nada; lo que va entre corchetes se copia tal cual. (2) Cuando te pegue el ORIGINAL, no cambies tu traducción: compara la que escribiste con el original, frase a frase, y lista solo las diferencias de sentido: una palabra que cambia lo que hay que hacer, una negación que desaparece, una cifra, un síntoma, una línea final distinta. Las de estilo no se listan.

FORMATO, en este orden:
(0) Una línea: "TEXTO SIN DATOS" o "TEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" si contiene nombre, fecha, centro, teléfono o cualquier dato individual; en ese caso, para.
(1) La retraducción, sin comentario.
(2) Tras el original: lista "DIFERENCIAS DE SENTIDO", numerada, con las dos frases enfrentadas; y la última línea, literal: "FRASES DE LA RETRADUCCIÓN: [n] · DIFERENCIAS DE SENTIDO: [n] · LÍNEAS FINALES: CONTACTO SÍ/NO · URGENCIAS SÍ/NO/NO APLICA · AVISO SÍ/NO": CONTACTO es SÍ si el corchete está, en español y tal cual; URGENCIAS es SÍ si está el 112 y una orden de no demorarse ("no espere" o equivalente; "no dude" no lo es), NO APLICA si el original no lleva esa línea; AVISO es SÍ si están sus tres ideas: hecho con apoyo de IA, revisado por su profesional sanitario, no sustituye la valoración individual. Los tres tienen que ser SÍ o NO APLICA.

RESTRICCIONES: No corrijas la traducción, ni la tuya ni la que te pegué, ni propongas otra: solo señala. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida (paso B, rumano; la hoja del caso 1 con la línea de tratamiento, que suma dos frases).**

> DIFERENCIAS DE SENTIDO. 1. Original: "gasta menos energía". Retraducción: "consume menos". 2. Original: "no espere". Retraducción: "no dude". […]
> FRASES DE LA RETRADUCCIÓN: 15 · DIFERENCIAS DE SENTIDO: 2 · LÍNEAS FINALES: CONTACTO SÍ · URGENCIAS NO · AVISO SÍ

**Qué revisar antes de usarla.** Un NO en CONTACTO, URGENCIAS o AVISO no se negocia: se rehace esa línea en A y se vuelve a retraducir. Las demás diferencias las decides tú con el hablante delante; la máquina señala, no arbitra. El original entra en el segundo mensaje, nunca en el primero; si el modelo "revisa" su retraducción al verlo, la comparación no vale: conversación nueva. El 112, con el buscador; si no aparece, está en otra grafía.

Las tres líneas se traducen y validan una sola vez por idioma (mediador, teléfono de interpretación o versión oficial de tu servicio de salud), van a la ficha del caso y desde entonces se pegan: la máquina no vuelve a tocar la del 112. Se guarda la hoja corregida a mano. "Revisado por su profesional sanitario" sigue siendo verdad en árabe si la revisión es esta: retraducción, hablante y tu nombre al pie. Respondes tú de la traducción (Ley 41/2002, art. 4.3); el mediador comprueba, no firma. Ningún aviso más: el que lleva ya dice que hubo máquina.

Lo que ninguna herramienta te dirá: para muchas personas del Magreb el árabe escrito no es el idioma de casa, y hay quien no lee en ninguno. Pregunta qué lee y en qué idioma antes de traducir; si es "nada", el material es oral (capítulo 9). La ley pide información comprensible y adecuada a la persona, no una hoja en su idioma (art. 4.2). Con instrucciones de alta traducidas por un traductor automático, la mayoría se entendía y unas pocas podían hacer daño (Khoong 2019).

**Riesgo principal y mitigación.** Entregar la traducción "porque la retraducción salió limpia". Mitigación: sin hablante no se entrega; sin mediador ni líneas finales validadas en ese idioma, no se entrega en papel: se lee juntos en español, frase corta y pregunta de vuelta, y el material es oral (capítulo 9).

### Caso 3 · Qué esperar del tratamiento: guion de primera visita

**Momento:** consulta. **Herramienta:** consumo. Guion oral; no se entrega.

**Situación.** La visita en la que decidimos empezar un tratamiento farmacológico de la obesidad tiene siete cosas que decir y siete minutos. El guion las ordena. El fármaco entra por su mecanismo, con mis palabras; el principio activo se lo digo yo con la caja delante, y el guion no lo lleva, para que sirva con cualquiera.¹

¹ Declaración de transparencia: mantengo vínculos con Novo Nordisk, detallados al inicio del libro. Aquí los fármacos aparecen solo por mecanismo y ninguno por su nombre; a quién se indican y cómo se sigue va en el capítulo 8.

```
ROL: Eres médica de familia especialista en obesidad, muy buena explicando en voz alta y sin jerga.

CONTEXTO: Atención Primaria en España. Quiero un GUION ORAL para decirlo yo en la visita en que una persona con obesidad y yo decidimos empezar un tratamiento farmacológico. Genérico: sin ninguna persona; a quién se le indica lo decido yo y no entra aquí. MECANISMO, con mis palabras: [por ejemplo: imita una hormona del intestino que avisa al cerebro de que hay saciedad y hace que el estómago se vacíe más despacio]. EFECTOS FRECUENTES AL EMPEZAR, con mis palabras y sin cifras: [por ejemplo: náuseas, diarrea, algún vómito, estreñimiento o notar el estómago lleno antes]. FRASE MÍA, literal: [por ejemplo: "La medicación puede abrir una puerta. Pero lo que realmente transforma la salud es lo que una persona construye después de cruzarla."]. LÍNEA DE AZÚCAR BAJO: [ninguna]. Si la persona toma medicación para la diabetes que puede bajar el azúcar, la línea es esta, literal: "Si toma medicación para la diabetes y nota temblor, sudor frío, hambre repentina o mareo, tome algo con azúcar y avísenos ese mismo día." (en tú: "Si tomas medicación para la diabetes y notas temblor, sudor frío, hambre repentina o mareo, toma algo con azúcar y avísanos ese mismo día."). Si es "ninguna", no añadas nada sobre el azúcar. TRATO: [usted por defecto / tú].

TAREA: Siete bloques cortos, en este orden y con estos títulos: QUÉ TRATAMOS (enfermedad crónica con biología detrás; no es falta de voluntad); QUÉ HACE EL TRATAMIENTO (solo el mecanismo que te he dado, con mis palabras, sin ampliarlo con otros efectos ni órganos y sin nombrar la hormona, y mi frase); QUÉ ESPERAR AL EMPEZAR (que al principio son frecuentes los EFECTOS que te he dado, solo esos, y suelen ir a menos, aunque pueden volver unos días cada vez que el tratamiento cambia; sin cifras de frecuencia ni plazos; y la LÍNEA DE AZÚCAR BAJO, si no es "ninguna"); QUÉ ES IR BIEN (menos hambre, más salud, poder hacer más; nunca kilos ni porcentajes; y que en unos meses vemos juntos si le está ayudando; si no, se cambia, y no es culpa de nadie); CUÁNDO LLAMAR Y CUÁNDO NO ESPERAR, con dos cosas: si puede quedarse embarazada, que si busca un embarazo, se queda embarazada o da el pecho me lo diga antes de nada, porque este tratamiento no se toma en esas etapas; y esta línea literal y entera, en usted: "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo." (en tú: "Si no toleras líquidos, tienes dolor fuerte de tripa, te mareas o te encuentras mal, no esperes: urgencias o 112. Y ante cualquier molestia, pide cita y lo vemos, o te llamo yo."); SI SE DEJA (es una enfermedad crónica, el cuerpo tiende a volver al peso anterior, y dejarlo se decide juntos y sin culpa); y PREGUNTA DE VUELTA, máximo 25 palabras: "Para saber si me he explicado bien, ¿qué le va a contar en casa de lo que hemos hablado, y cuándo tiene que llamar o ir a urgencias?".

FORMATO: Máximo 290 palabras sin contar las líneas literales, frases de 15 palabras como máximo, para decir en voz alta; sin negritas, sin emoticonos, sin pie de aviso: lo digo yo. Última línea, literal: "FÁRMACOS, CLASES O SIGLAS NOMBRADOS: [n] · DOSIS, VÍAS O PAUTAS: [n] · CIFRAS DE PESO, PORCENTAJES O PLAZOS: [n]": el primero cuenta cada nombre comercial, cada principio activo, cada clase o familia ("agonistas", "análogos", "esta familia de fármacos") y cada sigla de hormona; el segundo, cada cantidad con unidad, cada vía ("inyección", "pastilla") y cada frecuencia de administración; el tercero, cada kilo, porcentaje o plazo de resultado ("en pocas semanas notará", "en tres meses"); la cita de valoración de "qué es ir bien" no cuenta; los tres tienen que ser 0.

RESTRICCIONES: No nombres ningún fármaco, ni comercial, ni por principio activo, ni por clase o familia, ni la hormona por sus siglas; sin dosis, vía ni frecuencia; no digas a quién se le indica ni desde qué peso; no prometas resultados: sin "perderá", "bajará de peso", "la mayoría de las personas" ni plazos; sin dietas ni "comer menos". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> QUÉ TRATAMOS. La obesidad es una enfermedad crónica. Su cuerpo defiende el peso. No es falta de voluntad.
> QUÉ HACE EL TRATAMIENTO. Imita una hormona del intestino que avisa al cerebro de que hay saciedad. La medicación puede abrir una puerta. Pero lo que realmente transforma la salud es lo que una persona construye después de cruzarla. […]
> CUÁNDO LLAMAR Y CUÁNDO NO ESPERAR. […] Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo.
> FÁRMACOS, CLASES O SIGLAS NOMBRADOS: 0 · DOSIS, VÍAS O PAUTAS: 0 · CIFRAS DE PESO, PORCENTAJES O PLAZOS: 0

**Qué revisar antes de usarla.** El mecanismo, contra la ficha técnica del principio activo que vas a prescribir (CIMA, AEMPS): la máquina explica muy bien mecanismos que no son el de tu fármaco. Los efectos del ejemplo son los de los fármacos que imitan hormonas del intestino (GIRO 2024; Wharton 2020); con otro principio activo los sustituyes tú, ficha técnica delante: no los añades. Busca "kilos", "%", "perderá", "agonista", "familia", "inyección", cualquier sigla de hormona y "azúcar" fuera de la línea que le diste: si están, el recuento miente. "También regula el azúcar" lo dices tú o no se dice: en diabetes es una afirmación clínica, no una explicación.

Con medicación para la diabetes que puede bajar el azúcar, lo que haces con ella lo decides antes de la primera dosis (capítulo 8); el guion solo enseña a reconocer el azúcar bajo. Si la persona puede quedarse embarazada, esa frase no se salta; qué anticoncepción y con cuánta antelación se deja el fármaco, en la ficha técnica (capítulo 8). Si no sabe decir cuándo no esperar, la línea se repite. "Sin culpa" en el bloque de dejar no es adorno: quien se siente juzgado no vuelve a contarlo.

Dos cosas que el guion no dice: lo explicado de palabra consta en la historia (Ley 41/2002, art. 4.1), y estos bloques son lo que la ley pide antes de decidir juntos (art. 10.1). Si lo imprimes, deja de ser guion: pasa por el caso 1 y lleva las tres líneas.

**Riesgo principal y mitigación.** Que el guion prometa. Mitigación: "qué es ir bien" sin cifras y la valoración a los meses dicha el primer día; y tu frase de la puerta, que dice quién construye.

### Caso 4 · Preguntas frecuentes sobre náuseas y otros efectos digestivos

**Momento:** seguimiento de crónicos. **Herramienta:** consumo, sin ningún dato.

**Situación.** El mensaje corto entre visitas ya está en el capítulo 4 (caso 6, mensaje 2). Esta hoja es para cuando no basta: la persona ha empezado un tratamiento que da molestias digestivas los primeros días y quiere saber qué hacer en casa. No nombra el tratamiento, vale para cualquiera que las dé y no cambia ninguna pauta: eso es consulta (nota del caso 3).

```
ROL: Eres una redactora de materiales para pacientes de Atención Primaria, con conocimientos de lenguaje llano.

CONTEXTO: Soy médica de familia en España. Quiero una hoja GENÉRICA de preguntas y respuestas para personas que empiezan un tratamiento que puede dar molestias digestivas los primeros días, sin nombrar el tratamiento: vale para cualquiera. La entrego o la envío por el canal del centro. Sin ningún dato de nadie. LÍNEA DE AZÚCAR BAJO: [ninguna]. Si la persona toma medicación para la diabetes que puede bajar el azúcar, la línea es esta, literal: "Si toma medicación para la diabetes y nota temblor, sudor frío, hambre repentina o mareo, tome algo con azúcar y avísenos ese mismo día." Si es "ninguna", no añadas nada sobre el azúcar. TRATO: usted.

TAREA: Seis preguntas, con las palabras que usaría la persona, y su respuesta, sobre: náuseas o algún vómito; diarrea o deposiciones sueltas; estreñimiento; ardor o reflujo; sentirse lleno enseguida; y "¿cuánto dura esto?". Cada respuesta solo con medidas generales de casa, y nada más, de esta lista: raciones pequeñas; comer despacio y parar al notar el estómago lleno; evitar las comidas muy grasas y el alcohol mientras duren las molestias; beber a sorbos a lo largo del día; moverse un poco después de comer y no tumbarse justo después. Para la diarrea: beber más de lo habitual y a sorbos, mejor líquidos con algo de sal y azúcar (caldo, agua con limón y una pizca de sal); comidas blandas y pequeñas; no forzarse a comer; y que si no tolera líquidos vale la línea de urgencias del pie, sin repetirla. Para el estreñimiento: más fruta, verdura y legumbre, poco a poco; más agua de lo habitual; caminar cada día; no aguantarse las ganas; y si pasan más de tres o cuatro días sin deposición, o hay dolor o hinchazón, pida cita. En "sentirse lleno enseguida", además, la LÍNEA DE AZÚCAR BAJO si no es "ninguna". En la última, esto: "Suelen ir a menos con el tiempo, unas en días y otras en semanas, y pueden volver unos días cuando el tratamiento cambia. Si no mejoran, lo hablamos en consulta."

FORMATO: Máximo 220 palabras sin contar las líneas literales, frases de 15 palabras como máximo, nivel de lectura de 12 años, sin negritas ni emoticonos. La línea de urgencias va solo al pie, no dentro de las respuestas. Al pie, en este orden y literal: "Si tiene dudas, [FALTA: contacto del centro]."; "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo."; y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "PREGUNTAS: [n] · NOMBRES DE FÁRMACOS O 'FARMACIA': [n] · DOSIS O CAMBIOS DE PAUTA: [n] · 'NO SE PREOCUPE', 'ES NORMAL' O 'NO PASA NADA': [n]": la primera tiene que ser 6 y las otras 0; un cambio de pauta es cualquier "tome menos", "sáltese", "espere a la siguiente", "deje", "pare" o cantidad con unidad, y la LÍNEA DE AZÚCAR BAJO no cuenta; la última cuenta también "tranquilo" y "sin importancia".

RESTRICCIONES: No nombres el tratamiento ni ningún fármaco, tampoco para las náuseas o el estreñimiento ni de venta libre, ni remitas a la farmacia. No digas que se reduzca, se salte o se retrase una dosis, ni que se deje el tratamiento o se pare unos días: la pauta solo se cambia en consulta. No digas que las molestias son señal de que el tratamiento funciona. Sin infusiones, plantas ni remedios de herbolario. Sin "coma menos" ni "sáltese una comida". Sin "no se preocupe", "es normal", "tranquilo", "no pasa nada" ni "sin importancia". Sin más consejos de comida que los dados, sin dietas, sin peso ni cifras. No inventes teléfonos ni "responda a este mensaje". No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> ¿Qué hago si tengo náuseas o vomito? Coma raciones pequeñas y despacio. Pare cuando note el estómago lleno. […]
> ¿Y si tengo diarrea? Beba más de lo habitual, a sorbos: caldo, o agua con limón y una pizca de sal. […]
> ¿Cuánto dura esto? Suelen ir a menos con el tiempo, unas en días y otras en semanas, y pueden volver unos días cuando el tratamiento cambia. Si no mejoran, lo hablamos en consulta.
> Si tiene dudas, [FALTA: contacto del centro]. Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> PREGUNTAS: 6 · NOMBRES DE FÁRMACOS O 'FARMACIA': 0 · DOSIS O CAMBIOS DE PAUTA: 0 · 'NO SE PREOCUPE', 'ES NORMAL' O 'NO PASA NADA': 0

**Qué revisar antes de usarla.** Busca "dosis", "tome", "deje", "normal", "funciona", "jengibre" y "farmacia": los tres modelos los cuelan de vez en cuando y cuentan cero. Las medidas de casa son las de las recomendaciones prácticas para las molestias digestivas al empezar (Wharton 2022; GIRO 2024) y las de la ficha técnica de tu principio activo (CIMA, sección 4.8) [VERIFICAR en CIMA la duración de cada molestia para el principio activo que prescribas]; si el tuyo pide otra cosa (en ayunas o con la comida, por ejemplo), la pones tú y compruebas que la hoja no la contradice.

Con medicación para la diabetes que puede bajar el azúcar, lo que haces con ella lo decides antes de la primera dosis (capítulo 8); la hoja solo enseña a reconocer el azúcar bajo.

La línea de urgencias dice con palabras de casa lo que tú sabes que hay detrás: dolor fuerte que no cede o va a la espalda (páncreas), dolor bajo las costillas derechas (vesícula), no tolerar líquidos (deshidratación y riñón). Fiebre o piel amarilla no las dice: las dices tú en la visita del caso 3.

En quien vomita o no bebe, lo que se para esos días lo decides tú (capítulo 8). Cuando devuelva la hoja leída, pregunta lo que la hoja no pregunta: qué come de verdad, si vomita a diario, si bebe, si se salta comidas a propósito. Antes de imprimir, las diez preguntas del anexo B; el contacto, en tu sistema.

**Riesgo principal y mitigación.** Que la hoja "maneje" un efecto adverso que había que ver. Mitigación: la línea de urgencias y "pida cita y lo vemos" en cada hoja, y, si contesta contando un efecto adverso, la frase del capítulo 3 y tu notificación.

### Caso 5 · Llamar a quien no vuelve [AP]

**Momento:** seguimiento de crónicos. **Herramienta:** consumo, sin ningún dato. Guion oral; no se entrega.

**Situación.** "No acude a dos citas seguidas" es un criterio de aviso de enfermería del capítulo 5 (caso 5). Lo que pasa después suele ser nada, y en obesidad la nada se llama "abandono". La continuidad con el mismo médico se asocia a menos mortalidad (Pereira Gray 2018) y es la ventaja de Atención Primaria (Starfield 2005); una llamada de tres minutos la sostiene. El registro lo escribes tú (capítulo 5).

```
ROL: Eres médica de familia con experiencia en obesidad y en entrevista motivacional, y escribes guiones para llamadas breves.

CONTEXTO: Atención Primaria en España. Una persona con obesidad no ha acudido a dos citas seguidas; es un criterio de aviso que pacté con enfermería. Quiero un GUION ORAL para la llamada, que puede hacer enfermería o yo; quien llama se presenta como "[FALTA: quien llama], del centro de salud, de parte de su médica". Genérico: sin nombre, sin motivo de las citas, sin ningún dato. LO QUE PUEDO OFRECER de verdad: [por ejemplo: cita presencial conmigo, cita con enfermería o una llamada a la hora que le venga bien; las horas las pongo yo fuera de la IA]. CÓMO SE PIDE CITA en mi centro: [por ejemplo: por la aplicación del servicio de salud o en el mostrador]. TRATO: usted.

TAREA: (0) SI CONTESTA OTRA PERSONA O SALTA EL BUZÓN, una sola frase: que llamamos del centro de salud y que nos devuelva la llamada cuando pueda; sin motivo, sin nombrar ninguna enfermedad, sin citas pendientes, sin "su médica". (1) APERTURA, máximo 50 palabras: quién llama y por qué ("hace tiempo que no nos vemos y quería saber cómo está"), sin ninguna referencia a que faltó; una pregunta abierta sobre qué se lo está poniendo difícil; y "[escuchar]". (2) TRES RESPUESTAS, máximo 60 palabras cada una, a lo que la persona suele decir: "no tengo tiempo", "no ha servido de nada" y "me da vergüenza volver". Cada una: recoge lo que ha dicho con sus palabras, sin discutirlo y sin decirle que no debería sentirlo; una idea: la obesidad es una enfermedad crónica que va por épocas, no una nota de examen; y la oferta concreta, con las opciones que te he dado. (3) SALIDA DIGNA, máximo 40 palabras, si no quiere seguir ahora: la puerta sigue abierta, cómo pedir cita cuando quiera, y que su médica sigue siendo la misma. (4) SI CUENTA OTRA COSA, máximo 30 palabras, para quien llama, no para decir: si cuenta molestias con un tratamiento, ánimo bajo o ideas de muerte, la llamada deja de ser esta: cita con la médica hoy, y se anota; no se aconseja nada por teléfono.

FORMATO: Los siete textos con su título, para decir en voz alta: frases de 15 palabras como máximo, sin negritas, sin emoticonos, sin acotaciones salvo "[escuchar]", sin pie de aviso: es una llamada. Última línea, literal: "PALABRAS DE REPROCHE: [n] · FRASES QUE EVALÚAN: [n] · MENCIONES DE PESO, CIFRAS O FÁRMACOS: [n]": reproche es cada "faltó", "no vino", "no acudió", "abandonó", "se ha perdido", "debería", "tiene que"; una frase que evalúa califica a la persona o lo que hizo ("muy bien", "una pena", "es importante que", "valoramos su esfuerzo", "sus objetivos", "su compromiso"); las tres tienen que ser 0.

RESTRICCIONES: Sin reproche, tampoco disfrazado de preocupación ("nos tenía preocupados"). No le digas que no tiene por qué sentir lo que siente ("no tiene por qué avergonzarse", "no hay nada de qué"). Sin hablar de peso, kilos, balanza ni de lo que "tiene que" hacer. Sin fármacos ni nombres comerciales. Sin prometer resultados: ni "esta vez sí" ni "ahora hay más opciones". No inventes horarios, teléfonos ni nombres: las opciones son las que te he dado y el único hueco es quien llama. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> SI CONTESTA OTRA PERSONA O SALTA EL BUZÓN. Llamamos del centro de salud; que nos devuelva la llamada cuando pueda, por favor.
> APERTURA. Buenos días, soy [FALTA: quien llama], del centro de salud, de parte de su médica. Hace tiempo que no nos vemos y quería saber cómo está. ¿Qué se lo está poniendo difícil estos meses? [escuchar] […]
> SI CUENTA OTRA COSA. Molestias con un tratamiento, ánimo bajo o ideas de muerte: esta llamada se acaba y se pide cita con la médica hoy. Se anota.
> PALABRAS DE REPROCHE: 0 · FRASES QUE EVALÚAN: 0 · MENCIONES DE PESO, CIFRAS O FÁRMACOS: 0

**Qué revisar antes de usarla.** Busca "importante", "preocupados", "seguimiento", "avergonzarse" y "objetivos": los tres primeros son reproches que pasan el recuento; el cuarto discute lo que la persona siente; el quinto le pone nota. "No ha servido de nada" se contesta sin defender el tratamiento anterior: recoger, no discutir (Miller 2013). Las opciones que ofreces existen en tu agenda, o la llamada hace daño. El bloque "si cuenta otra cosa" es para quien llama, no se lee; con ideas de muerte, la cita es el mismo día (capítulo 5). Si contesta otra persona, una frase y ninguna más: el secreto también va por teléfono (capítulo 3).

Con quien entiende el español a medias, la llamada no explica: recoge, ofrece la cita y la confirma con una pregunta de vuelta ("¿me dice a qué hora viene?"); mediador o teléfono de interpretación si existen. El criterio son dos citas seguidas; con barrera idiomática puedes no esperar a la segunda, y lo anotas.

**Riesgo principal y mitigación.** Que la llamada suene a control de asistencia. Mitigación: la apertura sin "faltó" y la salida digna; quien cuelga sin sentirse juzgado vuelve antes que quien se disculpa.

### Caso 6 · Cartel de sala de espera [AP]

**Momento:** divulgación. **Herramienta:** consumo para el texto; el diseño, en el capítulo 9.

**Situación.** La sala de espera es el único sitio donde una persona con obesidad lee algo del centro sin que nadie se lo dé. Veinticinco palabras pueden decir lo que tres consultas no llegan a decir: que es una enfermedad y que aquí se trata. Lenguaje que pone a la persona primero (Kyle 2014), sin imágenes que estigmaticen (Rubino 2020) y sin cuerpos, por criterio mío: imágenes, en el capítulo 9. Si lo paga alguien, no es este cartel (capítulo 3).

```
ROL: Eres una redactora de textos breves para espacios de salud, con conocimientos de lenguaje centrado en la persona.

CONTEXTO: Soy médica de familia en España. Quiero el texto de un cartel para la sala de espera de mi centro que diga que la obesidad es una enfermedad crónica y que aquí se trata. Solo el texto; el diseño va aparte. Sin ningún dato. Sin patrocinio. IDEA que debe estar: "La obesidad es una enfermedad crónica. Aquí se trata."

TAREA: Tres variantes, de máximo 25 palabras cada una sin contar la línea de contacto, en forma impersonal (sin "usted" ni "tú" en el cuerpo), que digan: que es una enfermedad crónica; que no es falta de voluntad; y que en este centro se puede hablar de ello. Cada variante termina con esta línea literal, la única en usted: "Pregunte a su médica o enfermera, o en [FALTA: contacto del centro]."

FORMATO: Las tres variantes numeradas; nada más: sin titular, sin cuarta variante. Sin cifras, sin preguntas, sin imperativos fuera de la línea literal, sin exclamaciones, sin emoticonos, sin descripción de imágenes. Última línea, literal: "PALABRAS POR VARIANTE, SIN LA LÍNEA DE CONTACTO: [n] / [n] / [n] · CIFRAS: [n] · PALABRAS DE LA LISTA: [n]": la lista es "obeso", "obesa", "adelgazar", "kilos", "peso ideal", "dieta", "esfuerzo", "culpa", "lucha"; las dos últimas cifras tienen que ser 0.

RESTRICCIONES: Sin culpa, sin consejos ("coma", "muévase", "pida ayuda"), sin prometer resultados, sin fármacos ni nombres comerciales, sin marcas ni logotipos de ninguna entidad, sin ninguna línea de urgencias ni de "acuda". Usa "persona con obesidad" si nombras a alguien. No rellenes el marcador. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> 1. La obesidad es una enfermedad crónica. No es falta de voluntad. Aquí se trata, y se puede hablar de ello. Pregunte a su médica o enfermera, o en [FALTA: contacto del centro].
> 2. […]
> PALABRAS POR VARIANTE, SIN LA LÍNEA DE CONTACTO: 19 / 22 / 24 · CIFRAS: 0 · PALABRAS DE LA LISTA: 0

**Qué revisar antes de usarla.** Cuenta las palabras con el dedo, sin la línea de contacto: el modelo la cuenta la mitad de las veces y escribe 24 donde hay 29. Busca "lucha" y "¿": la primera está en la lista y pasa; la segunda es un titular que nadie pidió. Lee cada variante como quien no quiere que le hablen del peso: "aquí se trata" tiene que sonar a puerta, no a citación.

Un cartel no es material informativo para una persona: sin el pie de las hojas; con el contacto del centro, que es también su firma, y ninguna marca. Si tu consulta es privada, "aquí se trata" es publicidad sanitaria y tiene su norma en tu comunidad [VERIFICAR: normativa autonómica de publicidad sanitaria]; en un centro público lo autoriza quien autoriza lo demás, como la hoja sobre IA del capítulo 3.

**Riesgo principal y mitigación.** Que el cartel señale a quien está sentado debajo. Mitigación: sin cuerpos, sin cifras, sin "usted" en el cuerpo (el de la línea de contacto habla a quien quiera preguntar): habla de una enfermedad y de un sitio.

### Caso 7 · Leer una etiqueta nutricional

**Momento:** educación grupal y preparación de material (docencia). **Herramienta:** asistente multimodal, que lea imágenes.

**Situación.** "Esto es light, ¿no?" En la consulta, la etiqueta se lee juntos, con el dedo en la lista de ingredientes; ahí no hay móvil que valga. La IA sirve para preparar el taller o la hoja: diez etiquetas de letra diminuta en tablas, en una tarde. Y "light" no es una opinión: la ley exige al menos un 30 % menos de algo respecto a un producto similar y obliga a decir de qué (Reglamento 1924/2006); lo que no dice es qué lleva a cambio.

**Antes de la foto.** De frente, sin flash, la tabla ocupando la pantalla; dos tablas, dos fotos. Superficie lisa y neutra: sin manos, sin recetas, sin la pantalla del ordenador detrás y sin ninguna persona, menos aún en una sala con gente. Los envases brillantes reflejan caras: míralo en grande antes de subirlo.

La foto del móvil lleva dentro fecha, hora y, si se lo permites, dónde estabas; una captura de pantalla no las lleva: sube la captura. Al terminar, bórrala del carrete, de "eliminados recientemente" y de la nube; la conversación y el archivo, como en el capítulo 3. Borrar no deshace lo que el proveedor haya retenido: la imagen tiene que poder verla cualquiera sin dañar a nadie.

```
ROL: Eres una dietista-nutricionista que lee etiquetas de alimentos envasados y transcribe lo que ve, sin valorarlo.

CONTEXTO: Te adjunto la imagen de la etiqueta de un producto envasado, hecha por mí y revisada antes de subirla. En la imagen no hay personas, ni manos, ni documentos, ni datos personales, y no debes inferir nada sobre quién lo consume. Es una transcripción para uso educativo; no sustituye a la etiqueta.

TAREA, en este orden:
(0) Legibilidad. Antes de transcribir nada, escribe una línea: "Legibilidad: BUENA / REGULAR / MALA". Si es MALA (números borrosos, brillos sobre la tabla, tabla cortada), escribe "REPETIR FOTO" y para. Si en la imagen aparece cualquier persona, parte del cuerpo, texto manuscrito, ticket o dirección, escribe "IMAGEN NO APTA" y para.
(1) Idioma y tablas. Di en qué idiomas está la etiqueta y cuántas tablas o columnas distintas hay (por 100 g o 100 ml; por ración; producto tal cual o preparado; con o sin leche; sin cocinar o cocinado). Usa la versión en español si existe; si no, indica el idioma que usas.
(2) Transcripción, una tabla por cada columna del envase, con el título que le da el envase, sin mezclarlas ni elegir una: energía (kJ y kcal), grasas, de las cuales saturadas, hidratos de carbono, de los cuales azúcares, fibra, proteínas, sal, y cualquier otra fila que figure. Copia los números con el mismo decimal y la misma unidad que ves. Si el envase imprime la columna %IR, cópiala; no calcules ninguna. Si un número o una palabra no se lee con claridad, escribe ILEGIBLE en esa casilla: no lo estimes ni lo completes con los valores habituales de ese tipo de producto.
(3) Lista de ingredientes, en su orden y con su texto exacto; si está en otro idioma, tradúcela al español dejando el original entre paréntesis.
(4) Los tres primeros ingredientes. Después, en dos listas separadas, las fuentes de azúcares y los edulcorantes que aparecen, contados y nombrados, solo de esta lista. Fuentes de azúcares: azúcar, sacarosa, glucosa, dextrosa, fructosa, jarabe o sirope (de glucosa, de glucosa-fructosa, de maíz, de agave, de arroz), miel, melaza, azúcar invertido, maltodextrina, zumo o concentrado de fruta añadido. Edulcorantes: sucralosa, aspartamo, acesulfamo K, sacarina, ciclamato, glucósidos de esteviol, polialcoholes (sorbitol, maltitol, xilitol, eritritol) o cualquier E-950 a E-969. Si ves otro que creas que es una fuente de azúcar, ponlo aparte con un interrogante.
(5) Comprobación aritmética, por cada tabla por 100 g o 100 ml: los azúcares no pueden superar a los hidratos, las saturadas no pueden superar a las grasas, y 4 × hidratos + 4 × proteínas + 9 × grasas + 2 × fibra debe quedar a menos de un 10 % de las kcal. Escribe "COHERENTE" o "INCOHERENTE: [qué no cuadra]" y, si es INCOHERENTE, la casilla que crees mal leída.

FORMATO: Las líneas (0) y (1); las tablas; la lista de ingredientes; el punto (4); la línea (5); y al final tres frases descriptivas en lenguaje llano, trato de usted, que digan qué lleva el producto y en qué cantidad por ración, sin valorarlo. Cierra las tres frases, en este orden y literal, con: "Si tiene dudas, [FALTA: contacto del centro]." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."

RESTRICCIONES: No digas si el producto es "bueno", "malo", "sano" o "light", ni si conviene a alguien. Sin consejos individuales, sin necesidades diarias, sin mencionar peso ni dietas. Sin nombres de marca: llama al producto por su tipo ("galleta de cereales", "yogur de sabores"). No conviertas unidades (sodio a sal, kJ a kcal, onzas a gramos): copia lo impreso. No rellenes el marcador. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> Legibilidad: BUENA. Idiomas: español y portugués. Tablas: una (por 100 g y por ración de 30 g).
> Por 100 g: energía 1.890 kJ / 452 kcal; grasas 18 g, saturadas 8,2 g; hidratos 64 g, azúcares 23 g; fibra 3,1 g; proteínas 6,5 g; sal 0,9 g. Ración (30 g): azúcares 6,9 g.
> Ingredientes: harina de trigo, azúcar, aceite de palma […]. Fuentes de azúcares: azúcar, jarabe de glucosa (2). Edulcorantes: ninguno.
> Comprobación: 4×64 + 4×6,5 + 9×18 + 2×3,1 = 450 kcal frente a 452. COHERENTE.
> Una ración de 30 g de esta galleta de cereales lleva casi 7 g de azúcares […]. Si tiene dudas, [FALTA: contacto del centro]. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.

**Qué revisar antes de usarla.** Los números, con la etiqueta delante: un 4,5 se lee como 45 con facilidad. Con legibilidad REGULAR, cuenta los ILEGIBLE: más de tres, repite la foto. INCOHERENTE casi siempre es un decimal mal leído. Tantas tablas como tiene el envase: la que falta suele ser la que importa.

El orden de los ingredientes es lo que de verdad informa: la normativa europea obliga a listarlos de mayor a menor peso (Reglamento 1169/2011, art. 18). "Azúcares añadidos" no existe en la etiqueta europea (Reglamento 1169/2011, art. 30): lo deduces tú de la lista; por eso el prompt habla de fuentes de azúcares. Que las tres frases no se deslicen hacia "es poco saludable": eso lo hablas tú, en el taller. Si las dices tú, las dos líneas del final sobran; si se imprimen o se envían, van con el contacto rellenado en tu sistema y con tu nombre. Sin línea de urgencias: una etiqueta no toca síntomas.

**Riesgo principal y mitigación.** Tres: un decimal mal leído; una imagen con más de lo que querías; y el más difícil de ver: cuando no lee un número, el modelo pone el valor habitual de ese tipo de producto, y parece una transcripción. Mitigación: la puerta de legibilidad, la comprobación aritmética, la etiqueta delante y la imagen revisada por ti, ampliada, antes de subirla. Las tres grandes leen imágenes en sus versiones gratuitas, y las tres fallan con brillos. Si una dice BUENA y luego llena la tabla de ILEGIBLE, repite la foto.

---

## Caso ilustrativo, no real: arquetipo compuesto

> Esta viñeta combina rasgos de varias personas con barrera idiomática que he atendido en la zona. Se modifican el país de origen, el sector laboral y la composición familiar; no hay municipio, fechas ni cifras que permitan trazar a nadie. Los materiales son los de los casos 1, 2 y 5, y ninguno lleva un dato suyo.

Entre cincuenta y cincuenta y cinco años. Nació en el Magreb, lleva años en el campo y habla un español de trabajo: el que hace falta en el campo y en el mostrador, no para una hoja de dos caras. Obesidad de grado II y diabetes tipo 2 con tratamiento oral. Asiente a todo. No vuelve.

El "asiente a todo" no es carácter: es una jornada que empieza a las seis, un idioma en el que las preguntas se entienden a medias y la vergüenza de decir "no lo he entendido" delante de una médica. Lo destapó la hoja del caso 1. Le di la versión A y, antes de que la guardara: "Para saber si me he explicado bien, ¿cómo le contaría a su mujer por qué vuelve el peso después de una dieta?". Silencio. "Que hay que comer menos." No era lo que decía la hoja: era lo que había leído en todas las anteriores.

Antes de traducir, la pregunta que casi nunca hago: qué lee y en qué idioma. Árabe, "poco y despacio"; en casa hablan dariya. La hoja del caso 2 salió en árabe estándar, pasó la retraducción y esperó al día del mediador intercultural, que no viene a diario. La leyó con él, la corrigió en dos sitios y la explicó en su idioma; las dos correcciones fueron a la ficha del caso 2: se guarda la corregida.

Su hija de catorce años esperaba fuera y no entró a traducir: la información de salud de su padre es de su padre (Ley 41/2002, arts. 4.2 y 5.1), y una niña no es una intérprete.

Faltó a la segunda cita. El criterio son dos faltas seguidas; con él no esperé: con un idioma a medias y una campaña, una falta ya es perderlo. Enfermería llamó con el guion del caso 5 y no le explicó nada por teléfono. "No tengo tiempo, con la campaña." Sin reproche; la cita, a las dos y media, cuando baja del campo, y que la repitiera. La repitió. Vino.

La hoja no le cambió el tratamiento: lo que hacemos con su diabetes y con su peso es el capítulo 8, y se decide con él y con el mediador delante. Y la frase de siempre, que el mediador tradujo despacio: nada que permita saber quién es usted entra nunca en esas herramientas. Entraron dos hojas genéricas y un guion. Salió un hombre que, a la tercera visita, contó con sus palabras por qué vuelve el peso. No es falta de voluntad. Es biología, y es un idioma. Las dos cosas se pueden trabajar.

---

## En 60 segundos

1. Un material no es lo que escribes: es lo que la persona entiende. Se comprueba con la pregunta de vuelta, no con el asentimiento.
2. La máquina acorta, reescribe, traduce y propone preguntas; no sabe qué entiende esta persona ni qué palabra hiere. Cuentas tú.
3. Traducir sin retraducir y sin un hablante es entregar una hoja que no has leído.
4. Las tres líneas van en toda hoja, también en árabe, validadas una vez por idioma; guiones y cartel, fuera.
5. Fármacos por mecanismo, sin nombre, sin dosis y sin decir a quién: eso es el capítulo 8.

## Hazlo hoy · 10 minutos

1. **(3 min)** Pasa por el caso 1 la hoja que más entregas; cuenta tú tres frases con el dedo.
2. **(3 min)** Una sola pregunta de vuelta a la próxima persona a la que des una hoja: "Para saber si me he explicado bien…".
3. **(2 min)** Averigua si tu centro tiene mediador intercultural o teléfono de interpretación; apúntalo en la ficha del caso 2.
4. **(2 min)** Guarda los dos con la ficha del capítulo 4: v1, fecha, modelo, tus iniciales en "Probada por".

La hoja de tres páginas sigue en un cajón de alguien. La próxima cabe en media y, antes de salir de la consulta, la persona me la cuenta a mí.

---

## Referencias

**Alfabetización en salud, legibilidad y pregunta de vuelta**

1. Sørensen K, Pelikan JM, Röthlin F, Ganahl K, Slonska Z, Doyle G, et al. Health literacy in Europe: comparative results of the European health literacy survey (HLS-EU). Eur J Public Health. 2015;25(6):1053-8. doi:10.1093/eurpub/ckv043
2. Schillinger D, Piette J, Grumbach K, Wang F, Wilson C, Daher C, et al. Closing the loop: physician communication with diabetic patients who have low health literacy. Arch Intern Med. 2003;163(1):83-90. doi:10.1001/archinte.163.1.83
3. Barrio-Cantalejo IM, Simón-Lorda P, Melguizo M, Escalona I, Marijuán MI, Hernando P. Validación de la Escala INFLESZ para evaluar la legibilidad de los textos dirigidos a pacientes. An Sist Sanit Navar. 2008;31(2):135-52. doi:10.4321/S1137-66272008000300004

**Traducción e información comprensible**

4. Brislin RW. Back-translation for cross-cultural research. J Cross Cult Psychol. 1970;1(3):185-216. doi:10.1177/135910457000100301
5. Ley 41/2002, de 14 de noviembre, básica reguladora de la autonomía del paciente y de derechos y obligaciones en materia de información y documentación clínica. BOE núm. 274, de 15 de noviembre de 2002 (BOE-A-2002-22188). Arts. 4.1, 4.2, 4.3, 5.1 y 10.1.
6. Khoong EC, Steinbrook E, Brown C, Fernandez A. Assessing the use of Google Translate for Spanish and Chinese translations of emergency department discharge instructions. JAMA Intern Med. 2019;179(4):580-2. doi:10.1001/jamainternmed.2018.7653

**Obesidad, tratamiento farmacológico y efectos digestivos**

7. Agencia Española de Medicamentos y Productos Sanitarios. Centro de Información online de Medicamentos (CIMA) [Internet]. Madrid: AEMPS [consultado el 13 de septiembre de 2026]. Fichas técnicas autorizadas por principio activo, sección 4.8 (reacciones adversas). Disponible en: https://cima.aemps.es
8. Sociedad Española para el Estudio de la Obesidad (SEEDO). Guía Española GIRO: Guía española del manejo Integral y multidisciplinaR de la Obesidad en personas adultas. 2.ª ed. Lecube A, coordinador. Madrid: SEEDO; noviembre de 2024. Disponible en: https://www.seedo.es/images/site/giro/GUIA-GIRO-2a-edicin_26NOV2024.pdf [VERIFICAR ISBN en créditos del PDF; candidato 978-84-09-65969-2]
9. Wharton S, Lau DCW, Vallis M, Sharma AM, Biertho L, Campbell-Scherer D, et al. Obesity in adults: a clinical practice guideline. CMAJ. 2020;192(31):E875-E891. doi:10.1503/cmaj.191707
10. Wharton S, Davies M, Dicker D, Lingvay I, Mosenzon O, Rubino DM, et al. Managing the gastrointestinal side effects of GLP-1 receptor agonists in obesity: recommendations for clinical practice. Postgrad Med. 2022;134(1):14-9. doi:10.1080/00325481.2021.2002616

**Continuidad y entrevista motivacional**

11. Pereira Gray DJ, Sidaway-Lee K, White E, Thorne A, Evans PH. Continuity of care with doctors: a matter of life and death? A systematic review of continuity of care and mortality. BMJ Open. 2018;8(6):e021161. doi:10.1136/bmjopen-2018-021161
12. Starfield B, Shi L, Macinko J. Contribution of primary care to health systems and health. Milbank Q. 2005;83(3):457-502. doi:10.1111/j.1468-0009.2005.00409.x
13. Miller WR, Rollnick S. Motivational interviewing: helping people change. 3.ª ed. Nueva York: Guilford Press; 2013. ISBN 978-1-60918-227-4. Edición en español: La entrevista motivacional: ayudar a las personas a cambiar. 3.ª ed. Asensio Fernández M, traductora. Barcelona: Paidós; 2015. ISBN 978-84-493-3139-8.

**Estigma y lenguaje**

14. Kyle TK, Puhl RM. Putting people first in obesity. Obesity (Silver Spring). 2014;22(5):1211. doi:10.1002/oby.20727
15. Rubino F, Puhl RM, Cummings DE, Eckel RH, Ryan DH, Mechanick JI, et al. Joint international consensus statement for ending stigma of obesity. Nat Med. 2020;26(4):485-97. doi:10.1038/s41591-020-0803-x

**Etiquetado de alimentos**

16. Reglamento (CE) n.º 1924/2006 del Parlamento Europeo y del Consejo, de 20 de diciembre de 2006, relativo a las declaraciones nutricionales y de propiedades saludables en los alimentos. Diario Oficial de la Unión Europea L 404, 30 de diciembre de 2006, p. 9-25; corrección de errores en DO L 12, 18 de enero de 2007, p. 3-18. Anexo, declaraciones "contenido reducido" y "light/lite (ligero)". Disponible en: https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=celex%3A32006R1924
17. Reglamento (UE) n.º 1169/2011 del Parlamento Europeo y del Consejo, de 25 de octubre de 2011, sobre la información alimentaria facilitada al consumidor. Diario Oficial de la Unión Europea L 304, 22 de noviembre de 2011, p. 18-63. Arts. 18 y 30. Disponible en: https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=celex%3A32011R1169
