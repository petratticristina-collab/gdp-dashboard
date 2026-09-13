# Capítulo 6 · Plan del ARQUITECTO, con las decisiones del ORQUESTADOR (13-09-2026)

> Punto de partida: entrada del capítulo 6 en `indice.md` (v1, aprobada por la autora), la regla 14 de `biblia.md` (el caso de la etiqueta nutricional, ya revisado por los cuatro agentes en el ciclo del capítulo 2, se integra aquí) y los solapamientos con lo ya escrito: la hoja "¿Por qué recupero el peso?" en tres niveles es el caso 5 del capítulo 1; el mensaje de refuerzo entre visitas es el caso 6 del capítulo 4; el audio con ElevenLabs es el caso 2 del capítulo 9. El capítulo 5 fue aprobado por la autora el 13-09-2026; el 4 sigue pendiente de su aprobación, con sus preguntas en la biblia.

## Ficha

- **Título:** Capítulo 6 · Educar a la persona con obesidad
- **Subtítulo:** Materiales que se entienden, en su idioma y sin culpa.
- **Parte:** II · Usar. **Dependencias:** capítulos 1 (hoja en tres niveles, caso 5; adaptación metabólica, caso 2), 3 (disclaimers, datos, diez preguntas), 4 (cinco piezas, regla 19, mensaje entre visitas) y 5 (borrador y firma; SAIP; criterios de aviso de enfermería). Prepara el 9 (audio, vídeo e infografía) y el 13 (estigma en salidas; la hoja sin revisar que llega a la persona equivocada).
- **Extensión objetivo:** 6.400-6.800 palabras en v1, contando el caso de la etiqueta (unas 1.100). Tope 8.000 (regla 20; siete prompts, uno de ellos ya revisado).
- **Formato obligatorio:** el de la biblia (decisión 2), con la frase introductoria a los casos de los capítulos 4 y 5 como modelo.

## Gancho

El del índice: "Le di una hoja de recomendaciones de tres páginas. Volvió a los tres meses y me dijo que no la había entendido. Tenía razón: la había escrito para mí." Se cierra con la frase de composición ("Como todas las escenas de consulta de este libro…").

## Los tres aprendizajes clave

1. Alfabetización en salud: no basta con "nivel de lectura de 12 años" en el prompt. Se comprueba: frases cortas, una idea por párrafo, palabras que la persona usa, y la pregunta de vuelta ("¿cómo se lo contaría a su hija?") que dice si se ha entendido. Las hojas del capítulo 1 pasan aquí su examen.
2. Multiidioma con red: traducir es fácil; saber si la traducción dice lo mismo, no. Retraducción en conversación nueva, un hablante que lo lea, y la honestidad de que el idioma escrito no siempre es el hablado (quien habla dariya o amazige no siempre lee árabe estándar). Nunca se entrega sin revisar.
3. Todo lo que llega a la persona lleva validación clínica, las tres líneas de la regla 19 y el disclaimer en su variante (regla 11). Sin excepciones, tampoco con prisa, tampoco en otro idioma, tampoco en un cartel.

## Tesis del capítulo en una frase

Un material educativo no es lo que yo escribo: es lo que la persona entiende. La máquina escribe rápido y en cualquier idioma; comprobar que se entiende, sin culpa y sin error, sigue siendo mío.

## Los siete casos (con las decisiones del ORQUESTADOR)

| # | Caso | Momento | Herramienta | Decisiones |
|---|---|---|---|---|
| 1 | **La hoja pasa el examen: legibilidad y pregunta de vuelta** | consulta | asistente de consumo, sobre la hoja del capítulo 1 (versión A) o cualquier hoja propia sin datos | **Sustituye a "Hoja 'por qué recupero el peso'" del índice**, que ya se escribió en el capítulo 1 (caso 5). Aquí la hoja entra como texto y el prompt la audita: longitud media de frase, palabras de más de tres sílabas o técnicas, ideas por párrafo, culpa o moralización, cifras; devuelve la hoja reescrita a nivel de 12 años si hace falta, y tres preguntas de vuelta (teach-back) para comprobar en consulta que se ha entendido, formuladas sin examen ("para que yo sepa si me he explicado bien…"). Referencias: método teach-back (AHRQ Health Literacy Universal Precautions Toolkit; Schillinger 2003 [VERIFICAR]); legibilidad en español (INFLESZ, Barrio-Cantalejo 2008 [VERIFICAR]). Sin datos de nadie: la hoja es genérica. |
| 2 | **La misma hoja en árabe, rumano e inglés, con retraducción [AP]** | consulta | asistente de consumo, dos conversaciones | Se mantiene. La hoja validada (caso 1) se traduce; en una conversación nueva, otro modelo o el mismo sin memoria retraduce al español; se comparan las dos versiones en español y se marcan las diferencias de sentido. Después, un hablante nativo (mediador intercultural del centro, si lo hay; nunca un familiar menor) la lee. Honestidad: para muchas personas del Magreb el árabe escrito no es el idioma hablado; para algunas, ninguna hoja escrita sirve y el material tiene que ser oral (capítulo 9). Las tres líneas de la regla 19 y el disclaimer, traducidos y comprobados igual. Referencia: la Ley 41/2002 (art. 4) exige información comprensible; guías sobre traducción en salud [VERIFICAR: por ejemplo, la guía de traducción y adaptación de la OMS o un estudio sobre traducción automática en salud]. |
| 3 | **Qué esperar del tratamiento: guion de primera visita** | consulta | asistente de consumo | Guion oral (no entregable) para la visita en la que se empieza un tratamiento farmacológico de la obesidad: objetivos realistas sin cifras objetivo, la enfermedad crónica y el tratamiento como puerta ("la medicación puede abrir una puerta…", frase de la autora), principio activo y mecanismo (por ejemplo, agonistas del receptor de GLP-1: "imita una hormona del intestino que avisa de saciedad"), efectos adversos frecuentes al empezar, cuándo llamar y cuándo no esperar (regla 17 literal), qué pasa si se deja. Sin nombres comerciales, sin dosis, sin decir a quién se le indica (eso es el capítulo 8). **Nota al pie de transparencia obligatoria (regla 12).** Referencias: GIRO 2024; Wharton 2020; ficha técnica por principio activo (AEMPS/CIMA) [VERIFICAR]. |
| 4 | **Preguntas frecuentes sobre náuseas y otros efectos digestivos** | seguimiento de crónicos | asistente de consumo | Hoja de manejo en casa de las molestias digestivas frecuentes al empezar un tratamiento (náuseas, estreñimiento, reflujo, saciedad precoz): raciones pequeñas, despacio, qué evitar, hidratación; y las señales que no esperan, con la frase de la regla 17 literal y entera; las tres líneas de la regla 19 en usted. Sin nombrar el tratamiento (vale para cualquier fármaco que dé molestias digestivas al empezar); sin dosis ni "no se preocupe"; sin consejos que no sean generales. Remite al mensaje (2) del capítulo 4 (caso 6) y a la farmacovigilancia del 3 (si la persona contesta con un efecto adverso, notificar). Nota al pie compartida con el caso 3. Referencias: GIRO 2024; Wharton 2020; ficha técnica por principio activo [VERIFICAR]. |
| 5 | **Llamar a quien no vuelve [AP]** | seguimiento de crónicos | asistente de consumo | **Sustituye a "Mensaje de refuerzo para la consulta telefónica"**, que ya es el caso 6 del capítulo 4. Guion oral para la llamada, propia o de enfermería, a una persona con obesidad que no ha acudido a dos citas seguidas (criterio de aviso del capítulo 5, caso 5): sin reproche, sin "se ha perdido", con una pregunta abierta sobre qué se lo pone difícil, una oferta concreta (cita, hora, alternativa) y una salida digna si no quiere seguir. Tres variantes: "no tengo tiempo", "no ha servido de nada", "me da vergüenza volver". Es oral: sin disclaimer impreso; el registro de la llamada lo escribe la médica (capítulo 5). Longitudinalidad como argumento (Starfield 2005 [VERIFICAR] o la evidencia de continuidad en AP). Entrevista motivacional (Miller 2013, ya verificada). |
| 6 | **Cartel de sala de espera [AP]** | divulgación | asistente de consumo para el texto; el diseño, en el capítulo 9 | "La obesidad es una enfermedad crónica. Aquí se trata." Texto de máximo 25 palabras, tres variantes, sin cifras, sin culpa, sin imágenes de cuerpos (eso va al capítulo 9, caso 6), con la frase de contacto del centro como hueco y sin disclaimer de material informativo (un cartel no es material clínico individual: COMPLIANCE se pronuncia; en el capítulo 3 el texto de sala de espera sobre IA sí llevaba revisión de jurídico). Sin patrocinio: si el cartel lo paga alguien, no es este cartel (capítulo 3). Rubino 2020 y Kyle 2014 para el lenguaje. |
| 7 | **Leer una etiqueta nutricional** | docencia (educación grupal y preparación de material) | asistente multimodal | **Sustituye a "De hoja a audio"** (el audio con ElevenLabs es el caso 2 del capítulo 9, con la viñeta de la cuidadora que escucha mientras cocina). Se integra íntegro el texto de `capitulos/cap06_caso_etiqueta_reservado.md`, ya revisado por los cuatro agentes: renumerado como caso 7; sus dos referencias (Reglamento 1169/2011, Reglamento 1924/2006 [VERIFICAR]) van a la lista del capítulo; la higiene de la herramienta se remite al capítulo 3 (en el reservado dice capítulo 1: corregir) en vez de repetirse; el disclaimer final de las tres frases pasa a la forma de la regla 19 solo si el material se entrega (contacto como hueco; sin línea de urgencias porque no toca síntomas). Los revisores solo comprueban la integración, no lo reabren. |

Orden en el texto: 1 a 7. Los casos 1, 2 y 5 son los de la viñeta.

## Estructura del desarrollo (antes de los casos)

- **Primera parte · La hoja que escribí para mí.** Alfabetización en salud en España: qué proporción de adultos tiene dificultades con textos de salud (cifra solo con referencia verificable: por ejemplo, la encuesta europea HLS-EU 2015 o la HLS19 [VERIFICAR]; si no, sin cifra). Por qué las hojas de los centros no se entienden: frases largas, jerga, tres ideas por párrafo, y el tono de instrucción que suena a regañina. La persona que asiente y no vuelve.
- **Segunda parte · Lo que la máquina hace bien con la comprensión y lo que no.** Bien: reescribir a un nivel, acortar frases, cambiar de registro, traducir, generar preguntas de vuelta. No: saber qué entiende esta persona, saber si la traducción dice lo mismo, saber qué palabra hiere. La regla: se comprueba con la persona (pregunta de vuelta) y con un hablante (traducción).
- **Tercera parte · Las tres líneas y el disclaimer, también en otro idioma.** Remisión a las reglas 11, 17 y 19 (ya explicadas en los capítulos 3 y 4): aquí solo lo nuevo: se traducen y se comprueban como el resto del texto; el contacto del centro sigue siendo hueco; una hoja en árabe con la línea del 112 mal traducida es peor que ninguna hoja. Una sola mención al escenario con contrato (decisión 8): nada de este capítulo lo necesita porque nada lleva datos de nadie.
- **Siete casos.**
- **Viñeta.**
- **En 60 segundos · Hazlo hoy · Referencias.**

## Viñeta clínica (arquetipo compuesto, declarado)

Hombre de 50-55 años, de origen magrebí, español funcional pero limitado, trabajador agrícola, obesidad de grado II y diabetes tipo 2, que asiente a todo y no vuelve. Nota de composición: se combinan rasgos de varias personas con barrera idiomática de la zona; se modifican país de origen, sector laboral y composición familiar; sin municipio, fechas ni cifras. **Reglas para la viñeta:** el "asiente a todo" se explica como barrera (idioma, vergüenza, jornada) y no como rasgo de carácter; sin estereotipos culturales ni alimentarios; el idioma escrito no se da por supuesto (se le pregunta qué lee y en qué idioma; si no lee, el material es oral y va al capítulo 9); el hijo o la hija no hace de intérprete de contenido clínico (mediador del centro o teléfono de interpretación, si existe; si no, frases cortas y pregunta de vuelta); el Ramadán no se menciona salvo que el REDACTOR sepa hacerlo con una fuente y sin tópicos (mejor no). Muestra: la hoja del caso 1 que no entendió; la pregunta de vuelta que lo destapa; la traducción del caso 2 comprobada por el mediador; la llamada del caso 5 cuando falta a la segunda cita; la frase de la persona entrecomillada; el cierre con la promesa de datos (regla 16) y, si encaja, el estribillo. Diabetes: la hoja no cambia el tratamiento; el ajuste va al capítulo 8.

## Reglas de la biblia que este capítulo tiene que cumplir de forma visible

- **Regla 12:** nota al pie de transparencia en los casos 3 y 4 (fármacos para la obesidad por mecanismo).
- **Regla 17:** la frase real de la autora, literal y entera, en el caso 4, y la red de seguridad en el 3.
- **Regla 19:** tres líneas en todo texto para la persona (casos 1, 2, 4; el 7 si se entrega); el caso 6 (cartel) y los guiones orales (3 y 5) quedan fuera, y el capítulo lo dice.
- **Regla 11:** disclaimer en usted en hojas impresas o enviadas; en tú si la hoja tutea.
- **Regla 16:** la promesa de datos con su fórmula única, en la viñeta.
- **Regla 21:** una sola frase atribuye a "mi formación en IA" lo que venga del programa (materiales para pacientes adaptados a alfabetización y multiidioma).
- **Reglas 22-26:** casos de cero; documentos firmados; hueco de línea entera; historia clínica real nunca en consumo (aquí no hay datos de nadie: decirlo una vez).
- **Decisión 6 y regla 14:** disclaimer estándar; caso de la etiqueta integrado.
- Ficha del capítulo 4 (caso 7) para guardar los prompts, con "Higiene" y "Probada por".

## Lo que el REDACTOR no debe hacer

- No repetir la hoja del capítulo 1 ni el mensaje del capítulo 4: remitir.
- No dar cifras de alfabetización en salud sin referencia verificable.
- No presentar la traducción automática como suficiente: siempre retraducción y hablante.
- No nombrar marcas; no dar dosis; no decir a quién se indica un fármaco; no dar objetivos de peso.
- No caricaturizar a la persona de la viñeta ni a su cultura.
- No inventar referencias: [VERIFICAR] con el tipo de fuente.

## Referencias que el REDACTOR puede usar si las conoce con certeza (EVIDENCIA las comprobará)

- Ley 41/2002, art. 4 (información comprensible) y art. 5.
- GIRO 2024 (SEEDO); Wharton 2020 (CMAJ); Rubino 2020; Kyle y Puhl 2014; Miller y Rollnick 2013 (todas verificadas en capítulos anteriores).
- Teach-back: AHRQ Health Literacy Universal Precautions Toolkit; Schillinger 2003 (Arch Intern Med) [VERIFICAR].
- Legibilidad en español: Barrio-Cantalejo 2008 (INFLESZ) [VERIFICAR].
- Alfabetización en salud en Europa/España: Sørensen 2015 (HLS-EU) [VERIFICAR].
- Continuidad en AP: Starfield 2005 o Pereira Gray 2018 [VERIFICAR].
- Reglamento (UE) 1169/2011 y Reglamento (CE) 1924/2006 (caso 7).
- Ficha técnica por principio activo en CIMA (AEMPS) para los efectos adversos frecuentes [VERIFICAR].

## Preguntas para Cristina que el REDACTOR deja planteadas (máximo 5 al cierre; las recoge el ORQUESTADOR)

1. ¿Mantiene las tres sustituciones (caso 1 legibilidad y pregunta de vuelta; caso 5 llamada a quien no vuelve; caso 7 etiqueta en lugar del audio)?
2. ¿Qué recursos de interpretación tiene su centro (mediador intercultural, teléfono de interpretación) y qué idiomas necesita de verdad su cupo?
3. ¿Cómo explica hoy en la primera visita qué esperar de un tratamiento farmacológico, y qué frases suyas quiere en el guion del caso 3?
4. ¿Qué le dice a alguien que vuelve después de meses sin venir, y qué le dice enfermería cuando llama?
5. ¿Tiene un cartel en su sala de espera? ¿Qué dice?
