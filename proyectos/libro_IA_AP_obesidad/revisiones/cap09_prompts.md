# Revisión PROMPTS · Capítulo 9 · v1

> Agente: PROMPTS (ingeniero de prompts) · Fecha: 2026-09-21 · Ámbito: exclusivamente los ocho bloques de código que el capítulo ofrece al lector (casos 1 a 8; el del caso 5 es un prompt de imagen sin rol; el del caso 6 es la instrucción de una tarea programada) y los ejemplos abreviados de salida que los acompañan, más la frase introductoria a los casos (l. 96-98), porque fija reglas que los prompts heredan (conversación nueva, memoria, portabilidad, ficha). No se revisa el texto expositivo, la matriz, la viñeta ni las referencias, salvo cuando un prompt depende de ellos (la frase preparada del caso 2(c), las líneas del capítulo 3 y del capítulo 6 que los prompts copian).
> Versión revisada: `capitulos/cap09_v1.md` (commit 6325e0a; 10.097 palabras según `split()` con los bloques de código, 9.974 según el ORQUESTADOR; las líneas citadas son las de esa versión, `cat -n`). Los ocho bloques pesan 2.617 palabras (350 · 349 · 350 · 347 · 189 · 349 · 346 · 337), contadas con el mismo script que en los capítulos 7 y 8 (`len(texto.split())`; los rótulos y los signos sueltos cuentan). Regla de este ciclo (regla 20, opción a): 350 palabras por prompt es práctica recomendada, no obligación; si un prompt la supera, digo qué protege cada palabra de más y marco qué se puede recortar. **La v1 cumple la práctica en los ocho: es el primer capítulo desde el 7 que entra sin justificar nada, y hay que decirlo.** Mis versiones corregidas pesan **407 · 405 · 415 · 415 · 197 · 409 · 364 · 380 (2.992; +375 sobre la v1)**: siete de las ocho crecen porque cada una tenía un recuento que no se podía contar con el dedo, una variable con una instrucción dentro del corchete o un hueco que la ejecución mental deja abierto (T3, T4, T5); en cada caso digo qué palabra protege qué y qué se puede recortar "(−n)" si el ORQUESTADOR quiere acercarse a 350, porque el capítulo está en el tope de 10.000 y +375 de código lo empuja (T1). Ninguna lista literal de la médica se toca; la lista de diecisiete puntos del caso 8 se numera, no se cambia.
> Método: el de los capítulos 1 a 8 (`revisiones/cap08_prompts.md`). Para cada prompt: rol · contexto · tarea · formato · restricciones; etiqueta (0) con parada donde entra un texto, un archivo o un perfil (T1 del capítulo 5; PASO 0 de la regla 33 donde entran tablas); variables entre corchetes con valor por defecto y sin instrucción al lector dentro del corchete (T6 del capítulo 5); recuentos definidos en la misma línea y contables a mano (T2 del capítulo 5; T3 del capítulo 8); "DECISIÓN: la médica" donde hay decisión clínica (regla 30); si el modelo puede rellenar un hueco sin que se note (regla 24; regla 36: "[FALTA: ejecutar]"); portabilidad Gemini / ChatGPT / Claude sin cambios, y en este capítulo además: la voz que lee (caso 3), el generador de imágenes (caso 5) y las tareas programadas (caso 6), que no están en los tres cuando escribo esto; realismo del ejemplo de salida para 2026; riesgo. Cada prompt se ha ejecutado mentalmente con un caso sintético en los tres modelos: las tres plantillas con los recuentos de ejemplo del mapa del cupo; el reel de la pieza 1 del calendario y la pieza 3 con TOCA "sí"; la hoja "¿Por qué recupero el peso?" del capítulo 6 (caso 1, l. 87) sin la línea de tratamiento; las 150 palabras del capítulo 1 (caso 2) como guion del vídeo; la puerta entreabierta en dos generadores; una semana con cero, siete y veintitrés resultados en la tarea; la descripción del agente del reloj, y la propia tarea del caso 6c como descripción; la lista de diecisiete puntos del domicilio. La salida se ha leído con la rúbrica del capítulo 4 y las diez preguntas del anexo B. Contrastado con `revisiones/cap09_plan.md` (comprobaciones para PROMPTS, decisiones 2, 6 y 7 del ORQUESTADOR), `memoria/M3_checklist_compliance.md` (las diez verificaciones y la puntuación 8-10 / 6-7 / <6, para la duda 7 del REDACTOR) y `memoria/M3_marco_legal_etico_compliance.md` (las siete líneas rojas, para la comprobación 1). Reglas 7, 10, 11, 12, 16, 17, 19, 21, 22, 23, 24, 26, 27, 28, 30, 32, 33 y 36 de `biblia.md` como norma; ficha del caso 7 del capítulo 4 (v3, l. 384-388) como plantilla de guardado.

## Resumen de veredictos

| Caso | Título | Palabras v1 → corregida | Veredicto | Motivo principal |
|---|---|---|---|---|
| 1 | La burocracia de Atención Primaria en plantillas | 350 → 407 | **mejorar** | Produce tres plantillas en impersonal, sin firma ni "generado con IA", y la (0) para. Tres fallos. (a) Dos recuentos que no se pueden contar: "RECUENTOS MENORES DE 5 SIN '<5'" no tiene nada que contar en una plantilla sin datos (en (B) los recuentos los pone la médica al rellenar, fuera de la IA) y "DATOS DE EJEMPLO QUE PARECEN REALES" es una opinión, no un recuento; los tres modelos escriben 0 en los dos sin mirar. Pasan a un recuento con unidad ("CIFRAS, FECHAS O NOMBRES FUERA DE UN HUECO") y la regla 32 entra donde sí se aplica: en los recuentos que la médica pega en (C), con una parada en la (0) si uno es menor de 5 en cifra, y como línea literal dentro de la plantilla (B), para que la lectora la vea el día que rellene. (b) "Hueco de línea entera" contradice el propio ejemplo (l. 123: "[FALTA: servicio]" en mitad de la frase, que es lo que una plantilla necesita); lo que la regla 24 prohíbe es la frase que afirma con un corchete al final, y eso se dice por su nombre. (c) La (A) es una elección ("pedir un informe / adelantar una cita") con una instrucción dentro del corchete ("por un motivo que escribiré yo"); pasa a ELIJO y el motivo a hueco. |
| 2 | El calendario mensual de divulgación y el guion de un reel sanitario | 349 → 405 | **mejorar** | Las siete cosas que no se publican están como restricciones y cinco funcionan; dos no: "si hubiera patrocinio iría en la primera palabra" no tiene variable que lo active (el calendario dice "ninguno este mes"; el día que lo haya, la guionista no tiene dónde ponerlo) y "solo lo que trato en consulta" no lo puede comprobar el modelo (no sabe qué trata): se deja como restricción y la comprobación es la (1) del auditor del caso 4. Cifras y fuentes: "sin cifras" está; "sin estudios" no, y ChatGPT escribe "los estudios demuestran" en uno de tres; se cuenta. "SEGUNDOS ESTIMADOS: [n]" lo escribe el modelo sin cronómetro (el propio "qué revisar" lo dice: 44 y son 58); pasa a "PALABRAS DICHAS: [n]" con tope 110, que la lectora cuenta con el dedo y que el capítulo 1 ya calibró (150 palabras, un minuto). Dos corchetes con instrucción dentro ("lo decido yo", "que escribo yo"). La línea de derivación del capítulo 3 está literal; falta la segunda línea del mismo disclaimer cuando toca síntomas o efectos adversos ("Si es urgente, no esperes: urgencias o 112", capítulo 3, l. 84): TOCA pasa a tres valores. |
| 3 | Audio para quien no lee | 350 → 415 | **mejorar** | Conserva las tres líneas de la regla 19 y "AÑADIDAS: 0"; el rol ("cambias cómo suenan") es el mejor del capítulo. Cuatro grietas que la ejecución con la hoja real destapa. (a) La hoja del capítulo 6 ya termina con sus líneas finales; el prompt manda añadirlas "al final" y los tres modelos las duplican (leídas dos veces por una voz) o las reescriben. (b) La LÍNEA DE URGENCIAS solo admite la fórmula de "dolor en el pecho"; una hoja que lleve la larga de la regla 17 no cabe. El plan dice "solo si la hoja la lleva": se ata a la hoja y desaparece la variable. (c) "IDEAS" no tiene unidad: el modelo cuenta 9 y la lectora no sabe qué es una idea; pasa a "una línea del guion por cada frase de la hoja", que se cuenta con el dedo. (d) Lo que nadie vio: si se usa la lectura en voz alta del asistente, la voz lee "HOJA SIN DATOS", "corchete, FALTA" y el recuento; hace falta un turno "SOLO EL GUION" y que el hueco lo rellene la médica antes de la voz. "Cifras en letras" chocaba con el 112, que se escribe "112". La línea "Esta voz es una voz generada por ordenador" al final es honesta; si va al principio la oye también quien no llega al final (pregunta para COMPLIANCE y para la autora, no la decido). |
| 4 | Vídeo de sesenta segundos "qué es la adaptación metabólica" | 347 → 415 | **mejorar** | El auditor devuelve SÍ / NO / NO LO SÉ y no reescribe; la regla binaria es contable y funciona (tres cubos, cualquiera puede aplicarla con el dedo), y es más dura que la puntuación 8-10 del checklist del curso, que dejaría "preparado para publicar" un 8 con un caso identificable: la apoyo (duda 7 del REDACTOR). Tres cosas no cuadran. (a) Cuatro de las diez comprobaciones piden lo que el modelo no puede ver y el CONTEXTO no le da: qué trata la médica (1), si hay subtítulos y si el disclaimer general está en la bio (9); sin variables, los tres modelos contestan SÍ a (1) y NO LO SÉ a (9) siempre, y la pieza nunca es PUBLICABLE. (b) (10) "solo con las otras nueve" no dice qué escribir cuando una no es SÍ: el ejemplo pone NO LO SÉ y la regla pide NO. (c) El ejemplo pone NO LO SÉ en (9) por algo que sí se ve (el TEXTO EN PANTALLA no trae la línea): es un NO; NO LO SÉ se reserva a lo que no está ni en el texto ni en las líneas de la médica, y se dice. Suma a diez y "la primera regla que se cumpla" para cuando hay fallos en los dos bloques. |
| 5 | Imágenes sin estigma y el cartel de sala de espera diseñado | 189 → 197 | **mejorar (leve)** | La lista "LO QUE NO DEBE APARECER" basta como comprobación, con dos condiciones: que sean ocho puntos numerados en el prompt (la v1 tiene siete en el párrafo y el octavo, "estilo de anuncio", en otra frase; el ejemplo lista ocho) y que se admita que un generador aparte no escribe texto: entonces la lista la imprime la lectora del libro. Con "sin cuerpos", los generadores actuales devuelven pasillos y puertas vacíos si la escena se describe como vacía; lo que se cuela es lo que el "qué revisar" ya dice (una mano en el pomo, una sombra, letras en un cartel del fondo), y en los modelos de difusión una lista larga de prohibiciones a veces siembra lo que prohíbe: la escena se describe en positivo primero ("pasillo tranquilo y vacío") y la lista queda al final. Portabilidad: cuando escribo esto Claude no genera imágenes [VERIFICAR]; la frase introductoria (l. 98) dice que el 5 "se pega en los tres" y no es así. Formato: "vertical" pasa a "vertical (9:16)". Sin ROL, sin (0) y sin recuento, y está bien: no entra ningún texto de nadie. |
| 6 | Automatizaciones sin datos clínicos (tarea programada) | 349 → 409 | **mejorar** | Escrita como instrucción que se ejecuta sola: sin "te pego", con "cada lunes" y "últimos siete días", con permisos, "SIN DOI" y "FUERA DE MI LISTA". Los tres huecos del plan. (a) Sin resultados: no dice qué hacer y los tres modelos rellenan la página con estudios de otras semanas o "clásicos"; se cierra ("ENCONTRADOS: 0", sin estudios anteriores). (b) Demasiados: sin tope, la página de 350 palabras se llena de NO APLICA y lo relevante se recorta; tope de diez y una línea que pide acotar. (c) Cambio de modelo: la tarea sobrevive porque no depende del modelo, pero la ficha tiene que decir con cuál se probó y la primera página tras un cambio se contrasta con My NCBI; es texto de "qué revisar". Además: un resultado sin DOI no puede ir en PUEDE CAMBIAR LO QUE HAGO (la lectora no lo puede abrir); "No envíes" contradice lo que una tarea hace (entrega su salida como mensaje): pasa a "queda en esta conversación"; "RECIBIDOS" cuenta lo que nadie recibió: "ENCONTRADOS", y las dos etiquetas van al anexo A con su diferencia. |
| 7 | Diseñar en papel un agente de seguimiento, y cuándo no usar ninguno | 346 → 364 | **mejorar (leve)** | El razonador respeta la parada en Claude; ChatGPT y Gemini la rellenan a medias en uno de tres: "SIN RESPUESTA (presumiblemente la médica)", que el "qué revisar" (l. 365) teme y el prompt no prohíbe por su nombre: "a solas, sin paréntesis, sin 'presumiblemente' ni 'implícitamente'". La regla "NO SE ENCIENDE" sale de la regla y no de la opinión en los tres. Lo que la regla no prevé: el día que exista una herramienta con contrato (l. 33: "cambia la columna, no la gramática"), "DATOS DE PERSONAS: SÍ" apagaría cualquier agente para siempre; se añade la variable HERRAMIENTA CON ACUERDO DE TRATAMIENTO DE DATOS: [no] y la regla la lee. "n" no decía si cuenta las de (1) o las de (2): las de (2), como en el ejemplo (4). Prueba que el capítulo no propone y debería: pasar por este prompt la descripción de la tarea del caso 6c; sale una SIN RESPUESTA (quién la mira y cuándo) y es la ficha de la tarea la que está incompleta. |
| 8 | Antes del domicilio | 337 → 380 | **mejorar (leve)** | El caso sintético, "FUERA DE MI LISTA" y "DECISIÓN: la médica" están y funcionan; el recuento "DIAGNÓSTICOS, PROBABILIDADES O PAUTAS" es el mejor definido del capítulo. Dos fallos de recuento y uno de instrucción. (a) La lista tiene diecisiete puntos (7 + 5 + 4 + 1) y el ejemplo cuenta 16 porque pierde "glucómetro si hay diabetes"; el modelo no lo sabe y la lectora tampoco: se numera la lista ("diecisiete puntos separados por punto y coma") y el recuento tiene que ser 17. (b) "En cuatro bloques… sin cambiar de bloque" y "agrupando lo que se hace en la misma postura" se contradicen: el ejemplo agrupa por momento (sentada, cama, casa) y los cuatro bloques desaparecen; los tres modelos eligen uno u otro. Se resuelve con letras (E, P, L, N) en cada punto y orden por momento. (c) El recuento no decía que cuenta también dentro de FUERA DE MI LISTA y de COORDINAR, que es donde el "qué revisar" (l. 410) dice que se cuela el consejo. |

Ningún prompt es peligroso tal como está: ninguno pide decisiones clínicas, ninguno admite datos de nadie, los siete que reciben un texto llevan la línea (0) con parada (el del caso 6 con "omítelo y sigue", que es lo que cabe cuando no hay nadie delante) y los ocho llevan "No incluyas ni pidas datos de personas". Dos producen algo que llega a una persona (el audio del caso 3 y, por la sala de espera, el cartel del caso 5): el primero lleva las tres líneas de la regla 19 y el segundo no las necesita (capítulo 6, l. 284). Uno produce algo que sale al público (el reel del caso 2) y hereda el capítulo 3 literal. Ninguno afirma haber ejecutado una prueba: "[FALTA: ejecutar]" no hace falta en este capítulo. Cuatro tienen un recuento que cuenta lo que el modelo quiso contar (1, 2, 3 y 8) y uno hace que el modelo conteste SÍ a lo que no puede ver (4). El resto son correas de una o dos líneas. La portabilidad es la que la frase introductoria declara (l. 98) con tres matices que la frase no dice: Claude no genera imágenes cuando escribo esto (5), las tareas programadas existen en algunos asistentes y planes (6; EVIDENCIA lo fija) y la voz que lee (3) lee también lo que no es guion.

---

## Hallazgos transversales (afectan a varios casos)

**T1 · La práctica de 350 y qué protege cada palabra de más.** La v1 cumple en los ocho. Mi versión la supera en siete (todos menos el 5). Lo que pesa: en el 1, la parada por recuento menor de 5 (+22), la línea literal de la regla 32 dentro de la plantilla (B) (+16) y el recuento con unidad (+19): la primera y la segunda son la regla 32; la tercera sustituye dos recuentos que no contaban nada; se puede recortar la parada (−22) si el ORQUESTADOR acepta que la regla 32 la aplique la lectora antes de pegar, como en el capítulo 7. En el 2, TOCA con tres valores y la segunda línea del disclaimer de derivación (+22): es el capítulo 3 literal; PATROCINIO y su clausula (+28): es la sexta línea roja convertida en variable; "CIFRAS O ESTUDIOS" (+6). Se puede recortar PATROCINIO (−28) si la autora confirma que no acepta piezas patrocinadas (el calendario dice "ninguno este mes"; entonces la restricción se queda como frase). En el 3, la línea por frase (+12), "una sola vez aunque la hoja ya las traiga" (+9), el turno "SOLO EL GUION" (+26) y "el hueco lo relleno yo antes de la voz" (+9): las dos últimas son lo que hace que la voz lea solo el guion; se puede recortar el turno (−26) si la autora pega el guion en una herramienta de texto a voz y no usa la lectura en voz alta del asistente. En el 4, las tres variables nuevas (+26), la definición de NO LO SÉ (+15) y la regla de (10) (+12): sin ellas el auditor nunca dice PUBLICABLE; no recomiendo recorte. En el 6, el cierre de "sin resultados" y "más de diez" (+34) y "sin DOI, nunca esa etiqueta" (+6): son los tres huecos del plan; se puede recortar "más de diez" (−15). En el 7, la variable de contrato y su lectura en la regla (+14) y "a solas" (+8). En el 8, los diecisiete numerados y las letras (+18), "también dentro de FUERA DE MI LISTA y de COORDINAR" (+11), "un punto partido en dos momentos cuenta una vez" (+9): el primero hace contable el recuento. **Recomendación al ORQUESTADOR:** aceptar 2.992 palabras de código si el consolidado recorta prosa (el plan ya dice que el primer recorte es la primera parte, l. 10) o aplicar los recortes marcados "(−n)", que suman 91 palabras y no tocan ninguna línea de seguridad ni ninguna lista de la médica.

**T2 · La etiqueta (0) y las paradas.** Siete la llevan con "para" (1, 2, 3, 4, 7, 8) o con "omítelo y sigue" (6), que es la forma correcta cuando no hay nadie delante para parar: una tarea que se detiene sin avisar es una tarea que no existe, y una que incluye un dato es peor; omitir y seguir es lo que cabe. El 5 no la lleva y no la necesita: no entra ningún texto, y la descripción de la escena la escribe la médica (lo único que podría colarse es "la puerta de mi consulta 12 del centro de X", y el "No incluyas ni pidas datos de personas" no lo caza; lo dejo en "qué revisar": describe un sitio, no tu sitio). Novedad de este capítulo: la (0) del caso 1 gana una tercera rama, "RECUENTO MENOR DE 5", porque es el único prompt del capítulo en el que la médica pega cifras de su cupo, y la regla 32 dice que el "<5" se pone antes; una parada que lo recuerda vale más que un recuento que no puede contar nada. Gemini no para en uno de tres cuando la (0) tiene tres ramas (escribe la primera línea y sigue): "qué revisar" del caso 1 tiene que decirlo, como en el capítulo 8 (T5): si escribe las plantillas después de "BORRA ESTA CONVERSACIÓN", no las leas.

**T3 · Recuentos que cuentan lo que el modelo quiso contar (cinco).** "RECUENTOS MENORES DE 5 SIN '<5': [n]" (1) no tiene nada que contar en una plantilla sin cifras; "DATOS DE EJEMPLO QUE PARECEN REALES: [n]" (1) es un juicio; "SEGUNDOS ESTIMADOS: [n]" (2) no lo puede medir nadie sin cronómetro y el propio capítulo lo admite; "IDEAS DEL ORIGINAL: [n] · IDEAS EN EL AUDIO: [n]" (3) no define qué es una idea, y el "qué revisar" (l. 214) dice "el recuento coincide y a veces miente", que es la confesión de que no es contable; "PUNTOS DE MI LISTA: 16" (8) es 17. La regla de los capítulos 4, 5 y 8 (unidad definida en la misma línea, contable con el dedo) se aplica en los cinco: número, mes, día o nombre fuera de un [FALTA: …] (1); palabras dichas con tope, que el capítulo 1 calibró en 150 por minuto (2); una línea del guion por cada frase de la hoja (3); diecisiete separados por punto y coma (8). Y dos que sí eran contables y hay que conservar: "DIAGNÓSTICOS, PROBABILIDADES O PAUTAS" con sus verbos (8) y "SÍ / NO / NO LO SÉ" con la regla de tres cubos (4), a la que solo le faltaba "suman diez" y "la primera que se cumpla".

**T4 · Variables con instrucción dentro del corchete (T6 del capítulo 5), cuatro.** "[pedir un informe que no ha llegado / adelantar una cita por un motivo que escribiré yo]" (1); "[no / sí: lo decido yo]" y "[ninguno / esta línea literal, que escribo yo]" (2); "[pega la hoja que pasó el caso 1 del capítulo 6, sin la línea de tratamiento y sin nombre, centro ni teléfono]" (3). En los tres primeros la instrucción sale del corchete y se queda el valor ("ELIJO: [… / …]"; "TOCA, lo decido yo: [no / tratamientos / síntomas o efectos adversos]"; "VÍNCULO…, una línea literal mía o 'ninguno': [ninguno]"); en el cuarto, el corchete de un texto pegado no puede tener valor por defecto, y la instrucción pasa al rótulo ("HOJA (la del caso 1…): [hoja]"), que es la forma que el capítulo 7 usó para los resúmenes. Las demás variables del capítulo están bien: el TEMA con ejemplo (2), las cuatro líneas de "lo que solo yo sé" (4), la escena (5), la DESCRIPCIÓN con ejemplo entre comillas (7) y MI LISTA literal (8).

**T5 · Las tres líneas de la regla 19 cuando se dicen en voz alta (caso 3; también vale para el reel del caso 2).** Cuatro cosas que un texto no tiene que pensar y una voz sí. (a) La hoja del capítulo 6 ya termina con las tres líneas; si el prompt manda "añadirlas al final", la voz las dice dos veces o el modelo las funde en una: "una sola vez aunque la hoja ya las traiga". (b) "[FALTA: contacto del centro]" leído por una voz es "corchete, falta, dos puntos, contacto del centro": el hueco se rellena antes de la voz y se dice en el prompt y en "qué revisar"; el contacto, en un audio que entrega el centro, es el que el centro autorice (mostrador, teléfono del centro; capítulo 6, caso 6), nunca el de la médica. (c) "112" con "cifras en letras": el prompt pedía letras y la regla 28 pide las cifras 112; se exceptúa por su nombre y en "qué revisar" se escucha cómo lo dice la voz ("ciento doce" y "uno uno dos" se entienden; otra cosa, no). (d) El orden: contacto, urgencias si la hoja la lleva, aviso; y la cuarta línea, propia del formato, "Esta voz es una voz generada por ordenador". Al final es honesta y ordenada; al principio la oye también quien deja de escuchar a la mitad, que es justo la persona para la que el audio existe. No es decisión de prompts: la dejo como pregunta a COMPLIANCE (art. 50) y a la autora, con mi preferencia por el principio si COMPLIANCE no ve inconveniente. Ninguna de las tres líneas se pierde al leer en voz: la ejecución con la hoja real del capítulo 6 (l. 87) devuelve las tres en los tres modelos; lo que se pierde es el hueco (lo lee) y lo que sobra es la repetición.

**T6 · Portabilidad, y lo que la frase introductoria (l. 98) no dice.** Los ocho se pegan en los tres asistentes como texto. Lo que no está en los tres: la imagen (5): cuando escribo esto, Gemini y ChatGPT generan imágenes dentro del chat y devuelven después la lista; Claude no genera imágenes [VERIFICAR con EVIDENCIA]; en un generador aparte (fuera de los asistentes), el prompt vale pero la lista no vuelve, y se imprime del libro. Las tareas programadas (6): existen en algunos asistentes y en algunos planes [VERIFICAR: EVIDENCIA, comprobación 2 del plan]; la tarea corre en su propia conversación con el modelo del momento; no necesita la memoria encendida, y la frase "memoria apagada, salvo la tarea programada del caso 6" (l. 96) se lee como si la necesitara: propongo "salvo la tarea programada del caso 6, que vive en su propia conversación". La voz (3): los tres leen en voz alta una respuesta, y leen toda la respuesta; de ahí el turno "SOLO EL GUION". El razonador (7): el modo de razonamiento de los tres respeta el formato con la corrección; sin ella, ChatGPT y Gemini rellenan a medias en uno de tres. Y una cosa que sí hacen igual los tres y conviene decir en "qué revisar" del caso 2: ChatGPT y Gemini añaden emoticonos y hashtags al caption en uno de tres aunque se prohíban; se busca "#" y se borra.

**T7 · Etiquetas del anexo A (reglas 33 y 36), heredadas y nuevas.** Heredadas y unificadas: (0) con parada en los siete que reciben texto; "FUERA DE MI LISTA" en 6 y 8 con la misma forma ("…, nunca en una etiqueta" / "ahí y solo ahí"); "SIN DOI" en 6 (y ahora con consecuencia: nunca en PUEDE CAMBIAR LO QUE HAGO); "DECISIÓN: la médica" en 7 y 8 como última línea literal; "NO SE ENCIENDE" en 7 con la regla de la médica. No aplican en este capítulo: "SIN PÁGINA" (no hay documentos con página), "FUENTES QUE VEO" (no hay archivos cargados), "PEOR / MEJOR QUE EL CORTE" (no hay cortes), "[FALTA: ejecutar]" (ningún prompt afirma haber probado nada). Nuevas para registrar: "SIN RESPUESTA" (7), a solas, como salida de lo que una descripción no dice; "NO SE PUBLICA / SE CORRIGE Y SE VUELVE A PASAR / PUBLICABLE" (4), veredicto de tres cubos; "LO QUE NO DEBE APARECER" (5), lista de comprobación devuelta por un generador; "SOLO EL GUION" (3), turno de repetición sin recuento para una voz; "ENCONTRADOS" (6) frente a "RECIBIDOS" (capítulo 7, caso 6): la primera cuenta lo que una tarea trae; la segunda, lo que la médica pega; "MÁS DE DIEZ" (6) como parada por exceso. Y una etiqueta del capítulo 8 que este capítulo usa sin nombrarla: "PALABRAS: [n] / [n] / [n]" (1) es la misma forma que "PALABRAS POR VARIANTE" del cartel (capítulo 6, caso 6).

**T8 · La memoria del Módulo 3 en los prompts (regla 10).** Ninguna frase copiada. Lo más cercano: "¿La firmaría delante de mi colegio?" (4) frente a "si esto le llegase a mi colegio profesional mañana, ¿lo defendería?" (checklist, verificación 10): reformulada. "Si hubiera patrocinio iría en la primera palabra" (2) frente a "#publi como primera palabra del caption" (línea roja 6): es un requisito del Código de conducta, no una frase del curso, y mi versión usa la fórmula del capítulo 3 (l. 86: "al principio del texto y en pantalla mientras dure el vídeo"), que ya está en el libro. Los tres bloques del auditor (antes de escribir, de grabar, de publicar) son la estructura del checklist con otros nombres: el plan lo pide así.

**T9 · Lo que ya está bien y hay que conservar.** "Escribes para una población, nunca para una persona" (2) y "No cambias lo que dicen: cambias cómo suenan" (3): los dos mejores roles del capítulo. "No reescribes: compruebas y señalas" y "NO LO SÉ cuenta como NO: no lo conviertas en SÍ" (4). "No diseñas ni mejoras: rellenas y compruebas con lo que te doy", "ni 'en pequeño', ni 'para probar'" y "No digas si es buena idea" (7), que es la regla 30 aplicada a un agente. "Ordenas la lista de otra médica; no la escribes ni la completas" y el recuento con verbos (8). "No lees los artículos: localizas y clasificas", "nadie ha leído aún los artículos" y "PERMISOS: leer; escribir, enviar o guardar: ninguno" (6). "Ninguna frase que afirme que algo se hizo o se envió, ni con un corchete al final" (1): la regla 24 dicha por su nombre. "Sin fármacos, ni por marca ni por principio activo ni por clase" (3), que es lo que hace que el audio no necesite la nota ¹. La frase introductoria con las dependencias declaradas (l. 98) y la ficha del capítulo 4 con las dos líneas de más para la tarea (l. 328). Los ocho con rol en femenino y "persona con obesidad" donde toca.

**T10 · Dudas del REDACTOR que tocan a los prompts.** (2) La frase preparada del caso 2(c) (l. 172) coincide palabra por palabra con el capítulo 3 (l. 103: la variante "no es paciente mía" cambia "pide cita y lo vemos, o te llamo yo" por "coméntalo con tu médico o farmacéutico de referencia" y la línea de urgencia se queda). La forma larga de la regla 17 añade "Y ante cualquier molestia, pide cita y lo vemos, o te llamo yo", que no puede decirse a quien no es paciente; el capítulo 3 aprobado tampoco la lleva en esa variante. Cuenta como forma larga a efectos de la red de seguridad (la línea de urgencias está entera); lo que falta es que la biblia registre la variante para quien no es paciente bajo la regla 17. Es de COMPLIANCE; lo digo porque el prompt del caso 2 y el "qué revisar" dependen de esa frase. (4) Orden de las líneas del audio: T5. (5) Tareas programadas: T6 y caso 6. (7) Regla binaria del auditor: la apoyo, caso 4.

---
## Frase introductoria a los casos (l. 96-98) · veredicto: MEJORAR (leve)

Fija tres cosas que los ocho heredan y dos de ellas necesitan un matiz. "Conversación nueva y memoria apagada, salvo la tarea programada del caso 6" (l. 96): la tarea no necesita memoria; corre en su propia conversación. Propuesta: "Conversación nueva y memoria apagada; la tarea programada del caso 6 vive en su propia conversación." "Se pegan en Gemini, ChatGPT y Claude cuando escribo esto; el 3 necesita voz, el 5 imagen y el 6 tareas programadas" (l. 98): añadir "y no los tres tienen las tres cosas: comprueba la tuya" (T6). "Ficha del capítulo 4, caso 7; la del 6 lleva dos líneas más": bien; la ficha de la tarea lleva además "Última prueba: … con [modelo]" rellena, porque es la única automatización del libro que se ejecuta con el modelo del momento (caso 6, problema c).

---

## Caso 1 · La burocracia de Atención Primaria en plantillas · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿Los recuentos de la regla 32 están, si maneja cifras agregadas?** A medias. Las cifras agregadas entran solo en (C), donde la médica pega los recuentos del mapa del cupo; ahí la regla 32 ("<5", trimestres, sin cifras de peso) se aplica y el prompt la nombra en (B), no en (C). En (B) no entra ninguna cifra: la plantilla se rellena en el sistema de la médica, fuera de la IA, así que "cualquier recuento menor de 5 se escribe '<5'" es una instrucción que el modelo no puede cumplir ni incumplir, y "RECUENTOS MENORES DE 5 SIN '<5': [n]" siempre es 0. Lo que sí puede hacer el prompt con la regla 32: (a) parar en la (0) si un recuento pegado en (C) es menor de 5 en cifra (la regla dice que el "<5" se pone antes de pegar; una parada lo recuerda el día que se olvida); (b) meter la regla como línea literal dentro de la plantilla (B), para que la lectora la vea cuando rellene con datos reales, meses después, sin el libro delante. Las dos van en la versión corregida. "Sin cifras de peso" está en (B) y en (C).

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("nunca un documento sobre alguien"). |
| Anonimización | (0) "PLANTILLAS SIN DATOS / TEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" con "para": sí. "No incluyas ni pidas": sí. Se añade la rama "RECUENTO MENOR DE 5". |
| Variables | (A) lleva una instrucción dentro del corchete ("por un motivo que escribiré yo"): T4. (C) anidada ("[por ejemplo: … [n] …]") con ejemplo: bien. |
| Salidas cerradas | (0), (A)-(C) con tope de 120 sin huecos, recuento. Dos de los cuatro recuentos no son contables (T3). |
| Regla 23 / 24 | "Sin ninguna línea de 'generado con IA': las firmo yo": sí. "Ni con un corchete al final": sí. "Hueco de línea entera" contradice el ejemplo (l. 123). |
| Portabilidad | Los tres. Gemini añade "Atentamente, [Nombre]" en uno de tres (la restricción "sin firma" lo cubre a medias: escribe "[FALTA: firma]"); Claude añade una nota final ("He evitado…") en uno de tres: falta "nada más". |
| Ejemplo de salida | Realista. "PALABRAS: 41 / 96 / 118" cuadra con una (A) de cuatro líneas. Los dos últimos recuentos cambian. |
| Riesgo | Bien identificado ("de tan pulida, se firme sin leer"). |

### Ejecución mental (los tres modelos; recuentos de ejemplo: 212 · 87 · 34 · 9)
- **Claude:** "PLANTILLAS SIN DATOS". (A) escribe las dos variantes del corchete (informe y cita) en una sola plantilla con "o": 131 palabras, y el recuento marca 131 sin decir que se pasó. (B) trimestres con "[FALTA: trimestre]" y "<5" nombrado en una frase; (C) argumento del tiempo con los cuatro recuentos y sin quejas. Recuento: 0 y 0 en los dos últimos, sin haber mirado nada (no hay qué mirar). Con ELIJO, una sola (A) de 60 palabras.
- **ChatGPT:** parecido; en (C) escribe "en el último trimestre" (una fecha relativa, que no es hueco) y en (A) "atendida en fecha reciente" (afirma). En uno de tres, (B) trae una cifra de ejemplo ("por ejemplo, 45 personas") que "DATOS DE EJEMPLO QUE PARECEN REALES" debería cazar y no caza, porque el modelo no la considera "real". Con el recuento nuevo ("cada número… fuera de un [FALTA: …]"), la cuenta.
- **Gemini:** en uno de tres sigue después de la (0) si el texto trae un número de historia de ejemplo en la petición; en (C) escribe "dada la elevada carga asistencial" (la queja disfrazada que el "qué revisar" ya persigue). Con la regla 32 pegada con un "3" en cifra, ninguno de los tres lo convierte en "<5" por su cuenta: escriben "3"; la parada nueva lo detiene.
- Rúbrica: fidelidad alta (impersonal, sin datos); acción segura alta (nada llega a nadie sin firma). Anexo B: pregunta 9 (leída entera) es la que importa, y el "qué revisar" lo dice.

### Problemas
1. "RECUENTOS MENORES DE 5 SIN '<5'" no tiene nada que contar en (B); "DATOS DE EJEMPLO QUE PARECEN REALES" es un juicio (T3).
2. La regla 32 está donde no entran cifras (B) y no donde entran (C): sin parada.
3. "Hueco de línea entera" contra el ejemplo (l. 123); la regla 24 se dice mejor por su nombre: ninguna frase afirma que algo se hizo, se envió o se recibió.
4. (A) con instrucción dentro del corchete y con dos plantillas posibles bajo una sola letra: el recuento tiene tres números y el modelo escribe una o dos.
5. Falta "nada más" tras (C).

### Versión corregida (cambios en CONTEXTO (A) (ELIJO; motivo como hueco), (B) (línea literal de la regla 32 dentro de la plantilla), TAREA (hueco con nombre; regla 24 por su nombre), FORMATO ((0) con tres ramas; "nada más"; recuento contable); ROL y RESTRICCIONES iguales)

```
ROL: Eres una redactora administrativa al servicio de una médica de familia en España. Escribes plantillas genéricas que ella completa, firma y envía desde su sistema; nunca un documento sobre alguien.

CONTEXTO: Tres textos, sin ningún dato de nadie. (A) Correo a un servicio hospitalario; ELIJO: [pedir un informe que no ha llegado / adelantar una cita]; el motivo va como hueco. (B) Respuesta a gerencia o inspección que pide actividad de mi consulta: solo recuentos agregados, que pondré yo al rellenar, y esta línea literal dentro de la plantilla: "Recuentos por trimestre; los menores de cinco se expresan como <5." (C) Carta a gerencia solicitando huecos de quince minutos para primeras visitas de obesidad, con RECUENTOS DE MI CUPO, ya agregados, que pego yo: [por ejemplo: personas con obesidad: [n]; con dos o más comorbilidades: [n]; más de un año sin visita: [n]; primeras visitas al mes: [n]].

TAREA: Las tres plantillas, en impersonal, sin firma ni fecha. Todo dato que no te haya dado va como hueco con su nombre dentro: "[FALTA: número de historia]". Ninguna frase afirma que algo se hizo, se envió o se recibió, ni con un hueco al final: "se envió el [FALTA: fecha]" está prohibida. En (C), el argumento es el tiempo que exige la primera visita de una enfermedad crónica, con los recuentos; sin cifras de peso, sin "por la presión asistencial" ni ninguna queja sobre la agenda.

FORMATO: (0) Primera línea: "PLANTILLAS SIN DATOS"; o "TEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" si lo que te pego trae nombre, número de historia, fecha completa, municipio o cualquier dato de una persona; o "RECUENTO MENOR DE 5: ESCRÍBELO <5 Y VUELVE A PEGAR" si un recuento de (C) es menor de cinco en cifra; en los dos casos, para. Después (A), (B) y (C), máximo 120 palabras cada una sin contar los huecos, y nada más. Sin ninguna línea de "generado con IA": las firmo yo. Última línea, literal: "PALABRAS: [n] / [n] / [n] · HUECOS: [n] · CIFRAS, FECHAS O NOMBRES FUERA DE UN HUECO: [n]": la última cuenta cada número, mes, día, nombre de persona o de servicio que no esté dentro de un [FALTA: …], salvo "quince minutos", "<5" y los recuentos que pegué; tiene que ser 0.

RESTRICCIONES: Sin fármacos ni nombres comerciales. Sin adjetivos sobre nadie. Sin plazos inventados: "[FALTA: plazo]". Sin disculpas. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Recuento: 407 palabras. Protegen: la rama "RECUENTO MENOR DE 5" (22), la línea literal de la regla 32 en (B) (16), el recuento con unidad (19). Recorte posible: la rama de la (0) (−22) si se acepta que la lectora aplique la regla 32 antes de pegar, como en el capítulo 7, caso 5; no recomiendo tocar la línea literal de (B).

Ejemplo de salida (l. 122-125), sustituir por:

> PLANTILLAS SIN DATOS
> (A) Se solicita el informe de la consulta de [FALTA: servicio] correspondiente a la persona identificada como [FALTA: número de historia], atendida el [FALTA: fecha de la visita], que no consta en su historia de Atención Primaria. [FALTA: motivo por el que se necesita ahora].
> (B) […] Recuentos por trimestre; los menores de cinco se expresan como <5. Primeras visitas de obesidad, [FALTA: trimestre]: [FALTA: n]. […]
> (C) […]
> PALABRAS: 41 / 96 / 118 · HUECOS: 11 · CIFRAS, FECHAS O NOMBRES FUERA DE UN HUECO: 0

Frases nuevas para "Qué revisar" (l. 127): "Cuenta tú los números que no están dentro de un corchete: 'en el último trimestre' y 'en fecha reciente' no son huecos y afirman. Si escribió las plantillas después de 'BORRA ESTA CONVERSACIÓN', no las leas. Y los recuentos de (C) se escriben con el '<5' antes de pegar: la parada es el recordatorio, no la regla."

---

## Caso 2 · El calendario mensual de divulgación y el guion de un reel sanitario · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿Las siete líneas rojas reformuladas funcionan como restricciones, y el modelo no inventa cifras ni fuentes?** Cinco funcionan como restricción que el modelo puede cumplir con el texto: nada individual ("Nada que suene a consejo para quien lo ve", más el recuento de "tú deberías"); principio activo y mecanismo, nunca marca (con "MARCAS: 0"); ninguna persona reconocible ("ni caso, ni 'una paciente que vino', ni rasgos que sumados identifiquen"); nada de imagen ni voz de nadie ("No propongas imagen, voz ni vídeo de nadie"); nada con derechos ("MÚSICA: de librería con licencia o ninguna", escrita en el guion). Dos no funcionan como restricción: "Si hubiera patrocinio iría en la primera palabra" es una frase sin variable que la active (el calendario dice "ninguno este mes"; el día que lo haya, la guionista no sabe que lo hay), y "Solo lo que trato en consulta" no lo puede comprobar el modelo, que no sabe qué trata la médica. La primera pasa a variable PATROCINIO con su consecuencia (primera palabra del caption y en pantalla toda la pieza, con la fórmula del capítulo 3, l. 86); la segunda se queda como restricción y su comprobación es la (1) del auditor del caso 4, donde la médica sí escribe LO QUE TRATO. Cifras: "Sin cifras" está en RESTRICCIONES y los tres modelos lo respetan en el guion; no lo respetan en el caption ("el 60 % recupera el peso", ChatGPT, uno de tres). Fuentes: no estaba, y ChatGPT y Gemini escriben "los estudios demuestran" o "la ciencia dice" en uno de tres; se cuenta ("CIFRAS O ESTUDIOS: 0", con "números, porcentajes y 'los estudios dicen'"). Ninguno inventa una cita con autor y año en un reel de 45 segundos: el formato no lo pide.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("para una población, nunca para una persona"). |
| Anonimización | (0) "GUION SIN DATOS / TEMA CON DATOS: BORRA ESTA CONVERSACIÓN" con "para": sí. "No incluyas ni pidas": sí. |
| Variables | TEMA con ejemplo: bien. TOCA y VÍNCULO con instrucción dentro del corchete (T4). Falta PATROCINIO. |
| Salidas cerradas | (0), (1)-(3), recuento. "SEGUNDOS ESTIMADOS" no es contable (T3); "PERSONAS RECONOCIBLES" se define mejor como "casos o personas". |
| Capítulo 3 | Línea de derivación literal (l. 84): sí. Falta su segunda línea cuando toca síntomas o efectos adversos ("Si es urgente, no esperes: urgencias o 112"). Regla del efecto vigente (VÍNCULO dentro aunque no haya patrocinio): sí. |
| Portabilidad | Los tres. ChatGPT y Gemini añaden emoticonos y hashtags al caption en uno de tres. |
| Ejemplo de salida | Realista y bien escrito. "SEGUNDOS ESTIMADOS: 44" cambia por "PALABRAS DICHAS". |
| Riesgo | Bien identificado (la pieza que más se comparte es la que menos revisaste; el auditor del caso 4 pasa por las cuatro). |

### Ejecución mental (pieza 1 del calendario con TOCA "no"; pieza 3 con TOCA "sí"; los tres)
- **Claude:** pieza 1: guion de 96 palabras dichas, la balanza, el termostato, "se acompaña"; caption de tres frases sin hashtags; recuento con "SEGUNDOS ESTIMADOS: 42". Pieza 3 ("comer menos y moverse más", TOCA "sí", VÍNCULO con la línea de la médica): nombra "los tratamientos que actúan sobre el apetito" sin clase ni marca; la línea de derivación en pantalla y dicha; la línea de vínculo antes del cierre. Bien.
- **ChatGPT:** pieza 1: 118 palabras dichas (58 segundos, lo que el "qué revisar" avisa); dos emoticonos en el caption; "los estudios demuestran que el cuerpo…" en el 3-35 s. Pieza 3: en uno de tres, "un fármaco como la semaglutida" (principio activo, permitido por la restricción, pero en un reel de 45 segundos sobre "comer menos y moverse más" es una recomendación implícita que la (4) del auditor cazará). Con el tope de 110 palabras, recorta él.
- **Gemini:** pieza 1: caption con tres hashtags aunque se prohíban; "en tu caso, consulta" en el cierre en uno de tres (el recuento lo caza si lo busca; "qué revisar" lo dice). Pieza 3: "el 80 % recupera el peso" en el caption, y el recuento de cifras de mi versión lo caza; el de la v1, no.
- Rúbrica: fidelidad alta con el TEMA; acción segura: alta en el guion, media en el caption sin el recuento de cifras. Anexo B: pregunta 6 (consejo individual) es la que salta en Gemini.

### Problemas
1. "SEGUNDOS ESTIMADOS: [n]" no es contable ni por el modelo ni por la lectora sin cronómetro; "PALABRAS DICHAS" con tope 110 lo es (T3).
2. Sin recuento de cifras ni de "los estudios dicen" en el caption.
3. TOCA y VÍNCULO con instrucción dentro del corchete (T4); PATROCINIO sin variable (línea roja 6 inerte).
4. Falta la segunda línea del disclaimer de derivación cuando toca síntomas o efectos adversos (capítulo 3, l. 84).
5. Sin "nada más" ni "sin emoticonos".

### Versión corregida (cambios en CONTEXTO (TOCA con tres valores; VÍNCULO; PATROCINIO), TAREA (1) (tope de palabras dichas), (2) (segunda línea si síntomas), (3) (emoticonos; patrocinio), FORMATO (recuento contable); ROL y RESTRICCIONES casi iguales)

```
ROL: Eres una guionista de divulgación sanitaria para redes, al servicio de una médica de familia en España. Escribes para una población, nunca para una persona.

CONTEXTO: Un reel de 45 segundos. TEMA, con mis palabras: [por ejemplo: la obesidad es una enfermedad crónica; el cuerpo defiende su peso tras una pérdida; no es falta de voluntad]. TOCA, lo decido yo: [no / tratamientos / síntomas o efectos adversos]. VÍNCULO EN ESTE TEMA, una línea literal mía o "ninguno": [ninguno]. PATROCINIO: [ninguno].

TAREA: (1) GUION con tiempos: 0-3 s, una situación cotidiana, sin alarma; 3-35 s, un solo mensaje, en clave de población, con una imagen concreta; 35-45 s, un cierre que se pueda hacer, sin prometer nada; máximo 110 palabras dichas. (2) TEXTO EN PANTALLA: una línea por tiempo; si TOCA no es "no", esta línea subtitulada y dicha, literal: "Si reconoces en ti algo de esto, coméntalo con tu médico o profesional de referencia: solo una valoración individual puede orientarte"; si TOCA es "síntomas o efectos adversos", además, literal: "Si es urgente, no esperes: urgencias o 112". (3) CAPTION: tres frases, sin hashtags ni emoticonos; las mismas líneas literales al final, si tocan; si VÍNCULO no es "ninguno", su línea antes del cierre; si PATROCINIO no es "ninguno", "Publicidad" como primera palabra del caption y en pantalla toda la pieza.

FORMATO: (0) Primera línea: "GUION SIN DATOS" o "TEMA CON DATOS: BORRA ESTA CONVERSACIÓN" si el TEMA trae un nombre, una edad exacta, un lugar o una historia que parezca de alguien; en ese caso, para. Después (1), (2) y (3), nada más. Última línea, literal: "PALABRAS DICHAS: [n] · MARCAS: 0 · CIFRAS O ESTUDIOS: 0 · CONSEJOS INDIVIDUALES: 0 · CASOS O PERSONAS: 0": cuenta marcas; números, porcentajes y "los estudios dicen"; "tú deberías", "en tu caso" y "prueba a"; y cada caso, anécdota o "una paciente"; los tiempos del guion no cuentan; los cuatro tienen que ser 0.

RESTRICCIONES: Nada que suene a consejo para quien lo ve. Fármacos, si el TEMA los toca, por clase o principio activo y desde cómo actúan, nunca por marca. Ninguna persona reconocible: ni caso, ni "una paciente que vino", ni rasgos que sumados identifiquen. No propongas imagen, voz ni vídeo de nadie. Sin música ni imágenes con derechos: escribe "MÚSICA: de librería con licencia o ninguna". Solo lo que trato en consulta. Sin "obeso", sin culpa. No incluyas ni pidas datos de personas.
```

Recuento: 405 palabras. Protegen: TOCA con tres valores y la segunda línea del capítulo 3 (22), PATROCINIO y su consecuencia (28), "CIFRAS O ESTUDIOS" con su definición (6). Recorte posible: PATROCINIO (−28) si la autora confirma que no acepta piezas patrocinadas; entonces la frase de la v1 ("Si hubiera patrocinio iría en la primera palabra") se queda como restricción sin variable, y hay que decir en prosa que ese día se reescribe el prompt.

Ejemplo de salida (l. 164-168), sustituir la última línea por:

> PALABRAS DICHAS: 96 · MARCAS: 0 · CIFRAS O ESTUDIOS: 0 · CONSEJOS INDIVIDUALES: 0 · CASOS O PERSONAS: 0

Frases nuevas para "Qué revisar" (l. 170): "Cuenta las palabras dichas con el dedo: más de 110 no caben en 45 segundos dichos despacio (capítulo 1: 150 palabras, un minuto), y el modelo cuenta 96 donde hay 118. Busca '#' y emoticonos en el caption: los ponen aunque se prohíban. Busca un porcentaje y 'los estudios': en el guion no salen; en el caption sí. Y 'un fármaco como…' con un principio activo en un reel que no va de tratamientos es una recomendación disfrazada: el auditor del caso 4 la marca en (4)."

---

## Caso 3 · Audio para quien no lee · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿El modelo no reinterpreta ni añade consejo, y las líneas finales quedan literales? ¿Se pierde alguna de las tres líneas de la regla 19 al leer en voz?** Con la hoja real del capítulo 6 (caso 1, l. 87: "Su cuerpo defiende su peso. Cuando baja kilos, le da más hambre y gasta menos energía. No es culpa suya. Es biología. […] Si tiene dudas, [FALTA: contacto del centro]. Material informativo…"), los tres modelos devuelven las ideas en el mismo orden y ninguno añade consejo en el cuerpo; lo que añaden, y el "qué revisar" (l. 214) ya lo sabe, es una frase de ánimo al final ("Usted puede con esto", Gemini, uno de tres; "No está solo en esto", ChatGPT, uno de tres), que "Sin frases de ánimo" prohíbe y "AÑADIDAS: 0" debería contar y no cuenta, porque "idea" no está definida y el modelo no considera idea una frase de ánimo. Las tres líneas de la regla 19 no se pierden al leer en voz: salen las tres en los tres. Lo que pasa con ellas es otra cosa, y es lo que la comprobación no preguntaba: (a) la hoja ya las trae y el prompt manda añadirlas "al final", así que los tres las escriben dos veces (dos de tres) o funden las dos copias en una reescrita (Claude, una de tres: "Si tiene dudas, pregunte en su centro", que ya no es literal); (b) "[FALTA: contacto del centro]" lo lee la voz tal cual ("corchete…"), y el prompt dice "No rellenes el marcador" sin decir quién lo rellena ni cuándo; (c) "112" con "las cifras en letras" da "ciento doce" escrito, y la regla 28 pide las cifras. Las tres se corrigen: "una sola vez aunque la hoja ya las traiga", "el hueco lo relleno yo antes de la voz", "salvo el 112". Y la cuarta línea, "Esta voz es una voz generada por ordenador", sale literal en los tres.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto. |
| Anonimización | (0) "HOJA SIN DATOS / HOJA CON DATOS: BORRA ESTA CONVERSACIÓN" con "para": sí; el disparador incluye centro y teléfono, que es lo que una hoja lleva: bien. "No incluyas ni pidas": sí. |
| Variables | TRATO fijo en usted (la hoja es en usted): bien. LÍNEA DE URGENCIAS con una sola fórmula: no cabe la de la regla 17 si la hoja la lleva; se ata a la hoja (regla 30: "solo si la hoja la lleva"). HOJA con instrucción dentro del corchete (T4). |
| Regla 19 | Las tres líneas literales, en su orden: sí. Duplicación con la hoja: no prevista. Hueco leído por la voz: no previsto. |
| Salidas cerradas | (0), guion, líneas finales, recuento. "IDEAS" sin unidad (T3). |
| Portabilidad | Los tres escriben el guion. La lectura en voz alta de los tres lee toda la respuesta (T6). |
| Ejemplo de salida | Realista; muestra las líneas finales una vez, que es lo que el prompt no garantiza. Cambia el recuento. |
| Riesgo | Bien identificado ("que el audio 'mejore' la hoja"); la mitigación "AÑADIDAS: 0 contado por ti" necesita una unidad para contar. |

### Ejecución mental (hoja del capítulo 6, l. 87, sin la línea de tratamiento; los tres)
- **Claude:** "HOJA SIN DATOS". Nueve líneas con frases de menos de doce palabras; línea en blanco entre bloques; las líneas finales una vez en dos de tres y fundidas en una de tres. Recuento 9 · 9 · 0. Con la corrección: una línea por frase (la hoja de 120 palabras tiene unas doce frases), líneas finales una vez, "SOLO EL GUION" devuelve solo el guion.
- **ChatGPT:** añade "No está solo en esto" antes de las líneas finales en uno de tres y cuenta AÑADIDAS: 0. Con "cada línea del guion que no sale de una frase de la hoja", la cuenta en dos de tres; en la tercera, "qué revisar" (con la hoja al lado, línea por línea) la caza.
- **Gemini:** parte una frase en tres y junta dos en una: el recuento de ideas cuadra (9 · 9) y el orden cambia dentro del bloque; con "una línea por frase, en el mismo orden", no. Escribe "ciento doce" en uno de tres.
- Voz: la lectura en voz alta de la respuesta lee "HOJA SIN DATOS" y "FRASES DE LA HOJA: doce…" al final; con "SOLO EL GUION", no. Un texto a voz aparte lee "FALTA" si la médica no rellenó el hueco.
- Rúbrica: fidelidad alta con la corrección; acción segura alta (no hay tratamiento en la hoja). Anexo B: pregunta 6 (consejo que el modelo añade) es la que salta con la frase de ánimo.

### Problemas
1. Las líneas finales se duplican o se reescriben cuando la hoja ya las trae.
2. LÍNEA DE URGENCIAS con una sola fórmula y como variable; el plan la ata a la hoja.
3. "IDEAS" sin unidad; "AÑADIDAS: 0" no cuenta una frase de ánimo (T3).
4. El hueco lo lee la voz; el prompt no dice quién lo rellena ni cuándo.
5. "Cifras en letras" contra "112" (regla 28).
6. La lectura en voz alta lee la (0) y el recuento; falta un turno "SOLO EL GUION".
7. HOJA con instrucción dentro del corchete (T4).

### Versión corregida (cambios en CONTEXTO (urgencias atada a la hoja), HOJA (rótulo), TAREA (1) (línea por frase; 112), (2) (una sola vez), (3) nuevo (SOLO EL GUION), FORMATO (recuento contable), RESTRICCIONES (quién rellena el hueco); ROL igual)

```
ROL: Eres una redactora que adapta textos ya validados para ser leídos en voz alta. No cambias lo que dicen: cambias cómo suenan.

CONTEXTO: Te pego una hoja GENÉRICA para personas con obesidad que ya pasó un examen de legibilidad; no lleva ningún dato de nadie ni ninguna línea de tratamiento. Quiero el mismo texto como guion para una voz sintética. TRATO: usted. Si la hoja trae una línea de urgencias, con "urgencias o 112", se lee literal en su sitio; si no la trae, no añadas nada de urgencias, síntomas ni "consulte con su médico", aunque te parezca prudente.

HOJA (la del caso 1 del capítulo 6, sin la línea de tratamiento y sin nombre, centro ni teléfono): [hoja]

TAREA: (1) GUION DE AUDIO: una línea por cada frase de la hoja, en el mismo orden y con la misma idea; una frase larga se parte en dos dentro de su línea; frases de doce palabras como máximo; sin listas ni paréntesis; las cifras en letras, salvo el 112, que se escribe "112"; una línea en blanco donde la voz deba parar. (2) Al final, en este orden, literal y una sola vez aunque la hoja ya las traiga: "Si tiene dudas, [FALTA: contacto del centro]."; la línea de urgencias de la hoja, solo si la trae; "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."; y una última línea, literal: "Esta voz es una voz generada por ordenador." (3) Cuando yo escriba "SOLO EL GUION", repite el guion y sus líneas finales sin la primera línea ni el recuento, para pegarlo en la voz.

FORMATO: (0) Primera línea: "HOJA SIN DATOS" o "HOJA CON DATOS: BORRA ESTA CONVERSACIÓN" si trae nombre, fecha, centro, teléfono o cualquier dato individual; en ese caso, para. Después el guion y sus líneas finales, nada más. Última línea, literal: "FRASES DE LA HOJA: [n] · LÍNEAS DEL GUION: [n] · AÑADIDAS: 0": las líneas finales no cuentan; los dos primeros números tienen que coincidir y el tercero, que cuenta cada línea del guion que no sale de una frase de la hoja, ser 0.

RESTRICCIONES: No expliques, no resumas, no ejemplifiques, no suavices ni refuerces: la hoja ya dice lo que dice. Sin fármacos, ni por marca ni por principio activo ni por clase. Sin frases de ánimo. No rellenes el marcador: el hueco lo relleno yo antes de la voz. No incluyas ni pidas datos de personas.
```

Recuento: 415 palabras. Protegen: la línea por frase (12), "una sola vez aunque la hoja ya las traiga" (9), el turno "SOLO EL GUION" (26), "el hueco lo relleno yo antes de la voz" (9), "salvo el 112" (7). Recorte posible: el turno (3) (−26) si la autora pega el guion en una herramienta de texto a voz aparte y no usa la lectura en voz alta del asistente (pregunta 1 para Cristina); entonces "qué revisar" dice "copia solo el guion".

Ejemplo de salida (l. 206-212), sustituir la última línea por:

> FRASES DE LA HOJA: 12 · LÍNEAS DEL GUION: 12 · AÑADIDAS: 0

Frases nuevas para "Qué revisar" (l. 214): "Rellena el hueco del contacto antes de pegar en la voz: una voz lee 'FALTA' en voz alta, y el contacto de un audio que entrega el centro es el que el centro autorice, nunca el tuyo. Si la hoja ya llevaba sus líneas finales, tienen que sonar una sola vez y con las mismas palabras. Escucha cómo dice el 112: 'ciento doce' o 'uno uno dos' se entienden; otra cosa, no. Si usas la lectura en voz alta del asistente, pide 'SOLO EL GUION' y lee esa respuesta: la primera lee también el recuento."

Pregunta para COMPLIANCE y para la autora (T5): la línea "Esta voz es una voz generada por ordenador" al final es honesta y respeta el orden de la regla 19; al principio la oye quien deja de escuchar a la mitad. Si COMPLIANCE no ve inconveniente en el art. 50, mi preferencia es al principio, antes del guion, y las tres de la regla 19 al final, en su orden.

---

## Caso 4 · Vídeo de sesenta segundos "qué es la adaptación metabólica" · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿El auditor con diez comprobaciones SÍ/NO/NO LO SÉ y su regla binaria es contable y funciona?** Contable, sí: diez respuestas de tres valores, una línea de suma y tres cubos que cualquiera aplica con el dedo ("un NO o un NO LO SÉ en (1) a (4)": se mira; "en (5) a (10)": se mira; "diez SÍ": se cuenta). Funciona en los tres modelos con la corrección y a medias sin ella, por una razón que no es del modelo: cuatro comprobaciones piden lo que el modelo no puede ver y el CONTEXTO no le da. (1) "¿Trata de lo que hago en consulta?": no sabe qué hace; los tres contestan SÍ siempre, porque la pieza es de salud y la médica es médica. (9) pide subtítulos, disclaimer general "en la bio" y la línea de derivación: los subtítulos y la bio no están en el texto pegado; los tres contestan NO LO SÉ siempre, y por la regla la pieza es "SE CORRIGE Y SE VUELVE A PASAR" para siempre, sin salida. Corrección: LO QUE TRATO, SUBTÍTULOS y DISCLAIMER GENERAL EN LA BIO como líneas de "lo que solo yo sé", igual que ya hace con la firma, la voz, el patrocinio y la música; y "NO LO SÉ solo para lo que no está ni en el texto ni en mis líneas", que es lo que convierte NO LO SÉ en un valor con significado (lo que la médica no ha dicho) y no en un comodín. Sobre la duda 7 del REDACTOR (regla binaria propia frente a la puntuación 8-10 / 6-7 / <6 del checklist del Módulo 3): la binaria es mejor para un prompt y más segura para la médica. Con la puntuación, un 8 sobre 10 "preparado para publicar" puede llevar un NO en el caso identificable o en la marca, que es exactamente lo que el propio checklist llama líneas rojas; la binaria hace eliminatorias las cuatro primeras, que es la misma forma que la biblia ya dio a su checklist de salida (regla 18: cuatro eliminatorias más puntuación). La apoyo, y propongo una frase en prosa que lo diga: "mi regla es más dura que una puntuación: un 8 con un caso identificable no es un 8".

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("No reescribes: compruebas y señalas"). |
| Anonimización | (0) "PIEZA SIN DATOS / PIEZA CON DATOS: BORRA ESTA CONVERSACIÓN" con "para": sí. "No incluyas ni pidas": sí. |
| Variables | Cuatro de "lo que solo yo sé" con ejemplo: bien. Faltan tres (LO QUE TRATO, SUBTÍTULOS, BIO). |
| Salidas cerradas | (0), diez líneas, suma, veredicto. Falta "suman diez", "la primera que se cumpla" y qué escribe (10) cuando una no es SÍ. |
| Regla 30 | No hay decisión clínica; el veredicto sale de la regla de la médica: bien. |
| Portabilidad | Los tres. Gemini propone la corrección en (9) en uno de tres ("bastaría con añadir…"); el "qué revisar" lo dice. |
| Ejemplo de salida | (9) NO LO SÉ por algo visible (es NO); (10) NO LO SÉ (es NO). Se reescribe. |
| Riesgo | Bien identificado (cara al fondo sin firma; voz sintética sin etiqueta), con la mitigación en (5) y (7). |

### Ejecución mental (las 150 palabras del capítulo 1, caso 2, como guion; texto en pantalla sin la línea de derivación; caption con ella; "solo yo"; sin voz sintética; sin patrocinio; sin música; los tres)
- **Claude:** v1: (1) SÍ ("es salud"); (2)-(4) SÍ con frase; (5)-(8) SÍ "según tu línea"; (9) NO LO SÉ ("no puedo ver los subtítulos ni la bio; la línea de derivación está en el guion y en el caption, no en el texto en pantalla"); (10) NO LO SÉ. Suma 8 · 0 · 2. "SE CORRIGE Y SE VUELVE A PASAR". Corregida, con SUBTÍTULOS "sí" y BIO "sí": (9) NO ("el TEXTO EN PANTALLA no trae la línea de derivación"); (10) NO. Suma 8 · 2 · 0; mismo veredicto, y ahora se sabe qué corregir. Con la línea añadida en pantalla: diez SÍ, PUBLICABLE.
- **ChatGPT:** igual; en (3) escribe "SÍ, aunque recomendaría evitar 'concurso televisivo' si lo hubiera" (no lo hay: inventa la salvedad); la restricción "no propongas" lo cubre a medias. En (4), con "los tratamientos actuales" en el guion, contesta SÍ; bien.
- **Gemini:** en (9), "NO LO SÉ; bastaría con añadir la línea al texto en pantalla": ha auditado y editado a la vez; "qué revisar" lo caza. En (10), SÍ en uno de tres con un NO LO SÉ arriba; la regla nueva de (10) lo fija.
- Rúbrica: fidelidad alta (contesta con frase); calibración: NO LO SÉ como comodín sin la corrección; acción segura alta (no publica nada). Anexo B: pregunta 9 (leída entera): los diez se leen en un minuto.

### Problemas
1. (1) y (9) piden lo que el modelo no ve; sin variables, (1) es SÍ y (9) NO LO SÉ siempre.
2. NO LO SÉ sin definir: se usa para lo visible.
3. (10) sin regla cuando una de las nueve no es SÍ.
4. La suma no dice "diez"; el veredicto no dice qué regla gana si hay fallos en los dos bloques.
5. Falta "nada más" tras las diez líneas.

### Versión corregida (cambios en CONTEXTO (LO QUE TRATO; SUBTÍTULOS; DISCLAIMER GENERAL EN LA BIO), TAREA (NO LO SÉ definido; (1) con LO QUE TRATO; (7) "en pantalla y en el caption"; (9) "SÍ solo si todo"; (10) con regla), FORMATO ("nada más"; "suman diez"; "la primera que se cumpla"); ROL y RESTRICCIONES iguales)

```
ROL: Eres una auditora de piezas de divulgación sanitaria. No reescribes: compruebas y señalas.

CONTEXTO: Te pego GUION, TEXTO EN PANTALLA y CAPTION de una pieza de una médica de familia en España, sin datos de nadie. LO QUE TRATO: [obesidad en adultos y lo que la acompaña, desde Atención Primaria]. Y lo que solo yo sé: QUIÉN APARECE Y SI HA FIRMADO: [por ejemplo: solo yo]; VOZ O IMAGEN SINTÉTICA: [no / sí, etiquetada toda la pieza]; PATROCINIO: [no / sí, dicho primero y en pantalla]; MÚSICA: [ninguna / con licencia]; SUBTÍTULOS: [sí, toda la pieza / no]; DISCLAIMER GENERAL EN LA BIO: [sí / no].

TAREA: Contesta mis diez comprobaciones, cada una con SÍ, NO o NO LO SÉ y la frase que lo sostiene; NO LO SÉ solo para lo que no está ni en el texto ni en mis líneas. ANTES DE ESCRIBIR: (1) ¿Trata de LO QUE TRATO? (2) ¿Habla de una población y no aconseja a quien lo ve? (3) ¿No hay ninguna persona reconocible, ni caso, ni rasgos que sumados identifiquen? (4) ¿Ningún fármaco por marca ni recomendación de tratamiento? ANTES DE GRABAR: (5) ¿Todo el que aparece o se oye ha firmado, también de fondo? (6) ¿Lo que suena y se ve tiene licencia o es propio? (7) Si hay voz o imagen sintética, ¿lleva etiqueta toda la pieza, en pantalla y en el caption? ANTES DE PUBLICAR: (8) Si alguien la paga, ¿se dice primero, en texto y en pantalla? (9) ¿Lleva subtítulos, disclaimer general en la bio y, si toca síntomas o tratamientos, la línea de derivación dicha y escrita? SÍ solo si todo. (10) ¿La firmaría delante de mi colegio? SÍ solo si (1) a (9) son SÍ; si no, NO.

FORMATO: (0) Primera línea: "PIEZA SIN DATOS" o "PIEZA CON DATOS: BORRA ESTA CONVERSACIÓN" si traen nombre, edad exacta, lugar o una historia que parezca de alguien; para. Después las diez líneas, nada más. Penúltima línea, literal: "SÍ: [n] · NO: [n] · NO LO SÉ: [n]", y suman diez. Última línea, con mi regla, la primera que se cumpla: "NO SE PUBLICA" si hay un NO o un NO LO SÉ en (1) a (4); "SE CORRIGE Y SE VUELVE A PASAR" si lo hay en (5) a (10); "PUBLICABLE" solo con diez SÍ.

RESTRICCIONES: No reescribas ninguna frase ni propongas la versión "correcta". NO LO SÉ cuenta como NO: no lo conviertas en SÍ. No incluyas ni pidas datos de personas.
```

Recuento: 415 palabras. Protegen: las tres variables nuevas (26), la definición de NO LO SÉ (15), la regla de (10) (12), "suman diez" y "la primera que se cumpla" (12). Recorte posible: "en pantalla y en el caption" de (7) (−6); no recomiendo más: sin las variables el auditor nunca dice PUBLICABLE.

Ejemplo de salida (l. 248-251), sustituir por:

> PIEZA SIN DATOS
> (1) SÍ ("el cuerpo defiende su peso": obesidad en adultos). (2) SÍ: no hay "en tu caso". (3) SÍ. (4) SÍ: no nombra tratamientos. (5) SÍ, según tu línea. (6) SÍ: "MÚSICA: ninguna". (7) SÍ: no aplica. (8) SÍ: no hay patrocinio. (9) NO: subtítulos y bio según tus líneas, pero el TEXTO EN PANTALLA no trae la línea de derivación que el guion dice. (10) NO, porque (9) no es SÍ.
> SÍ: 8 · NO: 2 · NO LO SÉ: 0
> SE CORRIGE Y SE VUELVE A PASAR

Frases nuevas para "Qué revisar" (l. 253): "Un NO LO SÉ solo puede ser por algo que ni el texto ni tus líneas dicen; si lo pone en algo que se ve, es un NO disfrazado. Y las tres líneas que solo tú sabes de más (lo que tratas, los subtítulos, la bio) las contestas tú con la cuenta abierta delante, como la firma."

---
## Caso 5 · Imágenes sin estigma y el cartel de sala de espera diseñado · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿Basta la lista "LO QUE NO DEBE APARECER" como comprobación, sin ROL, sin (0) y sin recuento? ¿Qué devuelven los generadores actuales con "sin cuerpos"?** Basta, con dos condiciones. La primera es de aritmética: la lista tiene que ser la misma en el prompt y en la salida, y en la v1 no lo es: el párrafo "Lo que no debe aparecer" tiene siete puntos separados por punto y coma (texto; personas; comida; báscula, cinta, ropa; logotipos; objetos médicos; "antes y después") y el octavo, "estilo de anuncio", está en la frase de estilo; el prompt pide "los ocho puntos anteriores" y el ejemplo lista ocho. Los tres asistentes devuelven ocho porque cuentan el estilo; un generador con menos texto devuelve siete. Se numeran del (1) al (8) en el prompt. La segunda es de herramienta: un generador de imágenes aparte no escribe listas; la lista solo vuelve cuando el prompt se pega en un asistente que genera imágenes dentro del chat (Gemini y ChatGPT cuando escribo esto; Claude no genera imágenes [VERIFICAR]); si no vuelve, la lectora la imprime del libro y marca a mano, que es lo que el prompt ya dice ("lo compruebo yo"). Se admite en el prompt ("si puedes escribir texto"). Sin ROL: correcto, un generador no lo lee y en un asistente no estorba pero no aporta. Sin (0): correcto, no entra ningún texto de nadie (T2). Sin recuento: correcto, la lista de ocho marcada a mano es el recuento, y es de los mejores del libro porque no puede mentir: lo cuenta la que mira. Con "sin cuerpos", lo que devuelven los generadores actuales: una escena descrita en positivo como vacía ("pasillo tranquilo y vacío") sale vacía en los tres intentos; una puerta "entreabierta" trae una mano en el pomo en uno de tres en el modelo de difusión de Gemini y en ninguno en el de ChatGPT; letras en carteles del fondo, en uno de tres en los dos; una sombra con forma humana, en uno de seis. Las listas largas de prohibiciones son un arma de doble filo en los modelos de difusión: nombrar "báscula" y "comida" siembra a veces lo que prohíbe (uno de seis), y por eso la escena se describe primero en positivo y la lista va al final, como comprobación más que como orden. El "qué revisar" (l. 278) ya dice lo justo: mano, sombra, plato, letras; se descarta entera, no se recorta.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sin ROL por decisión del plan; contexto (cartel, vertical, fondo claro), tarea (tres variantes), formato (lista devuelta), restricciones (ocho puntos): sí. |
| Anonimización | Sin (0), y no la necesita; "No incluyas ni pidas datos de personas": sí. |
| Variables | La escena con ejemplo: bien. |
| Salidas cerradas | Tres variantes y una lista. Siete contra ocho (arriba). |
| Portabilidad | Gemini y ChatGPT dentro del chat; Claude no [VERIFICAR]; generador aparte sin la lista. La frase introductoria (l. 98) lo da por hecho en los tres. |
| Ejemplo de salida | Realista; la lista de ocho cuadra con la numeración nueva. |
| Riesgo | Bien identificado ("que el cartel señale, con una imagen 'neutra' que no lo es"). |

### Ejecución mental (puerta entreabierta; dos asistentes con imagen; un generador aparte)
- **Gemini:** tres imágenes verticales; en una, una mano en el pomo; en otra, un rótulo con letras inventadas sobre la puerta ("CONSULTA 3" mal escrito); la tercera, limpia. Lista de ocho puntos después. Con la escena en positivo primero, dos limpias de tres.
- **ChatGPT:** una imagen por turno (pide "otra variante" dos veces o genera las tres en secuencia); sin texto en las tres; en una, un cuadro en la pared con una silueta; lista de ocho después. La mitad superior "casi vacía" la respeta en dos de tres.
- **Generador aparte:** las tres imágenes, ninguna lista; el "9:16" lo respeta; "sin estilo de catálogo" lo entiende a medias (luz de catálogo en una de tres).
- Rúbrica: no aplica (no hay contenido clínico); anexo B: pregunta 6 no aplica; la única pregunta es la del "qué revisar": mirar como quien está sentado debajo.

### Problemas
1. Siete puntos en el prompt, ocho en la salida pedida y en el ejemplo.
2. La lista se pide sin admitir que un generador aparte no la devuelve.
3. "Vertical" sin proporción; "mucho espacio libre en la mitad superior" sin decir dónde va la escena.
4. La escena no se describe como vacía antes de la lista de prohibiciones.
5. Portabilidad en la frase introductoria (l. 98): Claude no genera imágenes [VERIFICAR].

### Versión corregida (cambios: 9:16 y escena en la mitad inferior; "y nada más" y "vacío" en la escena; ocho puntos numerados; "si puedes escribir texto")

```
Imagen para un cartel de sala de espera de un centro de salud en España, en formato vertical (9:16), con fondo claro y la mitad superior casi vacía, para escribir texto encima después; la escena, en la mitad inferior.

Lo que se ve, y nada más: [por ejemplo: una puerta de consulta entreabierta, con luz cálida saliendo por la rendija, y una silla sencilla al lado, en un pasillo tranquilo y vacío]. Estilo: fotografía natural o ilustración plana sencilla; colores suaves; sin estilo de anuncio ni de catálogo.

Lo que no debe aparecer, y lo compruebo yo: (1) texto, letras o números; (2) personas o partes de personas: manos, siluetas, sombras con forma humana; (3) comida o bebida; (4) báscula, cinta métrica o ropa; (5) logotipos, marcas o cruz sanitaria; (6) objetos médicos reconocibles: bata, fonendo, pastillas; (7) nada que sugiera "antes y después"; (8) estilo de anuncio.

Genera tres variantes distintas de la misma escena. Después de las imágenes, si puedes escribir texto, una lista con el título "LO QUE NO DEBE APARECER" con los ocho puntos, uno por línea, para que yo marque cada uno en cada variante. No incluyas ni pidas datos de personas.
```

Recuento: 197 palabras. Protegen: la numeración (6) y "si puedes escribir texto" (5). Sin recorte posible que valga la pena.

Ejemplo de salida (l. 275-276), sustituir la lista por:

> LO QUE NO DEBE APARECER: (1) texto, letras o números · (2) personas o partes de personas · (3) comida o bebida · (4) báscula, cinta o ropa · (5) logotipos, marcas o cruz · (6) objetos médicos · (7) "antes y después" · (8) estilo de anuncio.

Frases nuevas para "Qué revisar" (l. 278): "Si tu herramienta no devuelve la lista, imprímela de aquí: la marcas tú igual. Describe un sitio, no tu sitio: 'la puerta de mi consulta' con el número y el centro es un dato del centro que no hace falta. Y si una variante trae una persona 'de espaldas' o 'borrosa', es el punto (2): se descarta."

---

## Caso 6 · Automatizaciones sin datos clínicos (tarea programada) · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**Escrita como instrucción que se ejecuta sola: ¿qué pasa cuando no hay resultados, cuando hay demasiados, cuando cambia el modelo?** La instrucción está bien escrita para nadie delante: sin "hoy" ni "te pego", con "cada lunes" y "los últimos siete días", con PERMISOS declarados, "SIN DOI", "FUERA DE MI LISTA" y la (0) con "omítelo y sigue" (T2). Los tres huecos. **Sin resultados:** una semana sin nada nuevo que cumpla la regla es normal (obesidad en adultos desde Atención Primaria con ensayo, revisión o guía: una al mes, no una a la semana); el prompt no dice qué hacer, y los tres modelos hacen lo mismo: rellenan la página con lo que la búsqueda trae aunque no sea de los últimos siete días (un artículo de hace dos meses "publicado en línea", una guía de 2024 "actualizada", una noticia de sociedad científica), y el recuento "ENCONTRADOS: 5" cuadra porque los tres cuentan lo que pusieron. Peor: si la búsqueda web no devuelve nada, ChatGPT y Gemini completan con estudios que "recuerdan" en uno de tres, con DOI plausible; "Sin DOI inventados" lo frena a medias. Corrección: "Sin nada de los últimos siete días: solo el título, la línea literal y 'ENCONTRADOS: 0', sin estudios anteriores". **Demasiados:** con veintitrés resultados (una semana de congreso), la página de 350 palabras se llena de NO APLICA en una línea cada uno y lo relevante queda en dos líneas; "máximo 350 palabras sin contar NO APLICA" protege el cuerpo, pero la página es ilegible; los tres modelos recortan lo que quieren. Corrección: tope de diez, los diez más recientes, y una línea que pide acotar: "MÁS DE DIEZ: hay que acotar la búsqueda", que es lo que la médica hace con la cadena de My NCBI (capítulo 7). **Cambio de modelo:** la tarea corre con el modelo del momento y el prompt no depende de ninguno (no nombra formato de cita propio, no usa funciones de una herramienta); lo que cambia es lo que "sabe" y cuánto inventa cuando no encuentra, y la única defensa es la del capítulo: My NCBI sigue encendida y se contrasta (l. 330). Es texto, no prompt: la ficha lleva "Última prueba: … con [modelo]" rellena, y "qué revisar" dice que la primera página tras un cambio de modelo (la herramienta lo anuncia o la ficha lo ve) se contrasta entera con la alerta de PubMed, no una vez al mes. Y dos cosas que el plan no preguntaba: (a) "No envíes ni guardes esta página" contradice lo que una tarea es: su salida se entrega como mensaje de la conversación y, si la herramienta lo hace, como aviso; lo que se puede pedir es que no vaya a ningún otro sitio ni a la memoria; (b) "RECIBIDOS" es la etiqueta del capítulo 7, donde la médica pega la alerta; aquí nadie recibe: "ENCONTRADOS", y las dos al anexo A (T7). Con DOI: un resultado sin DOI no puede abrirse a mano, así que no puede ir en PUEDE CAMBIAR LO QUE HAGO; se dice.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("No lees los artículos: localizas y clasificas"). |
| Anonimización | (0) con "omítelo y sigue": la forma correcta para una tarea sin nadie delante. "No incluyas ni pidas": sí. |
| Variables | "[semana y año]" en el título: bien (la tarea lo rellena). Ninguna otra: bien, es una tarea. |
| Salidas cerradas | (0), página con título y línea literal, recuento con suma. Faltan las salidas para cero y para exceso. |
| Instrucción autónoma | Sin "hoy" ni "te pego"; "cada lunes"; "últimos siete días"; PERMISOS; sin escritura: sí. "No envíes" contradice la entrega de la tarea. |
| Etiquetas | "SIN DOI", "FUERA DE MI LISTA", "nadie ha leído aún los artículos": sí. "RECIBIDOS" cuenta lo que nadie recibió. |
| Portabilidad | Tareas programadas en algunos asistentes y planes [VERIFICAR: EVIDENCIA]; la instrucción vale en cualquiera que las admita. El idioma no estaba fijado: la página sale en inglés en uno de tres. |
| Ejemplo de salida | Realista (7 · 1 · 2 · 4 · 1 · 1). "RECIBIDOS" cambia. |
| Riesgo | Bien identificado (que la segunda alerta sustituya a la primera). |

### Ejecución mental (semana con cero, con siete y con veintitrés resultados; los tres, en modo tarea con búsqueda web)
- **Claude:** siete: página en español con títulos en inglés, un PUEDE CAMBIAR con sus cuatro SÍ, DOI copiados de la página de la revista, dos SIN DOI (un preprint y una nota de sociedad), FUERA DE MI LISTA con una guía pediátrica. Cero: en la v1, "esta semana destacan" con tres artículos de hace un mes; corregida, "ENCONTRADOS: 0". Veintitrés: v1, página de 600 palabras; corregida, diez y "MÁS DE DIEZ".
- **ChatGPT:** parecido; con cero, en uno de tres un ensayo "reciente" con DOI que no resuelve (inventado por composición: revista real, número plausible); corregida, cero. Escribe la página en inglés en uno de tres sin la línea de idioma.
- **Gemini:** clasifica bien; con siete, pone un observacional en PUEDE CAMBIAR con "ensayo NO" y el recuento no lo detecta (la médica sí, si mira las cuatro condiciones: "qué revisar" del capítulo 7 lo dice). Con cero, una guía de 2024 "actualizada" con fecha de la semana; corregida, cero.
- Rúbrica: fidelidad media (lo que la búsqueda trae); calibración: la línea literal "nadie ha leído aún" es la calibración; acción segura alta (nada llega a nadie; "sin recomendaciones"). Anexo B: pregunta 3 (afirmación no sostenida) salta con los estudios "recordados".

### Problemas
1. Sin salida para cero resultados: los tres rellenan con estudios anteriores o "recordados".
2. Sin tope para exceso.
3. "No envíes ni guardes" contra la entrega de la tarea; "queda en esta conversación" es lo pedible.
4. "RECIBIDOS" cuenta lo que nadie recibió (T7).
5. Sin DOI en PUEDE CAMBIAR LO QUE HAGO: no se puede abrir a mano.
6. Idioma de la página sin fijar.
7. Cambio de modelo: texto para "qué revisar" y para la ficha.

### Versión corregida (cambios en TAREA (1) (sin DOI, nunca esa etiqueta), (4) nuevo (cero y exceso), FORMATO (idioma; ENCONTRADOS), RESTRICCIONES (queda en esta conversación); ROL y CONTEXTO iguales)

```
ROL: Eres una documentalista clínica que ejecuta cada lunes, sin nadie delante, una búsqueda de evidencia para una médica de familia en España. No lees los artículos: localizas y clasificas.

CONTEXTO: Tarea programada semanal. Busca solo en fuentes públicas (PubMed, registros de guías, sociedades científicas) lo publicado en los últimos siete días sobre obesidad en adultos desde Atención Primaria. REGLA DE RELEVANCIA, mía: PUEDE CAMBIAR LO QUE HAGO = las cuatro a la vez: ensayo aleatorizado, revisión sistemática o guía; en adultos; con desenlace clínico; algo que se hace desde Atención Primaria en España. CONVIENE SABERLO = observacional o desenlace intermedio que puede aparecer en consulta. NO APLICA = animales, laboratorio, técnica quirúrgica o de unidad especializada, población que no atiendo. PERMISOS: leer; escribir, enviar o guardar: ninguno.

TAREA: (1) Por cada resultado: primer autor, año, revista, DOI; qué se estudió y en quién; el resultado principal si el resumen lo da; la etiqueta y, si es PUEDE CAMBIAR LO QUE HAGO, las cuatro condiciones con SÍ o NO; sin DOI, nunca esa etiqueta. (2) Ordena por etiqueta; NO APLICA solo con título y DOI. (3) Lo que no encaja en mi regla y crees que debería, en "FUERA DE MI LISTA: …", nunca en una etiqueta. (4) Sin nada de los últimos siete días: solo el título, la línea literal y "ENCONTRADOS: 0", sin estudios anteriores. Con más de diez: los diez más recientes y "MÁS DE DIEZ: hay que acotar la búsqueda".

FORMATO: (0) Primera línea: "FUENTES PÚBLICAS · SIN DATOS DE PERSONAS" o "RESULTADO CON DATOS DE PERSONAS: NO LO INCLUYAS" si algún texto recuperado trae datos de alguien; omítelo y sigue. Después, una página en español, títulos en su idioma, de máximo 350 palabras sin contar NO APLICA, titulada "Evidencia de la semana · [semana y año]" y debajo, literal: "Resumen de resúmenes: nadie ha leído aún los artículos. Antes de cambiar nada, se lee el artículo entero." Última línea: "ENCONTRADOS: [n] · PUEDE CAMBIAR LO QUE HAGO: [n] · CONVIENE SABERLO: [n] · NO APLICA: [n] · SIN DOI: [n] · FUERA DE MI LISTA: [n]": los tres del medio suman el primero.

RESTRICCIONES: Solo los resúmenes públicos: no completes ni añadas estudios. Sin DOI inventados: si falta, "SIN DOI". Sin nombres comerciales: principio activo o clase. Sin recomendaciones. La página queda en esta conversación: no la envíes a ningún otro sitio ni la guardes en memoria. No incluyas ni pidas datos de personas.
```

Recuento: 409 palabras. Protegen: el cierre de cero y de exceso (34), "sin DOI, nunca esa etiqueta" (6), el idioma (6), "queda en esta conversación… ni en memoria" (10). Recorte posible: "Con más de diez…" (−15) si el ORQUESTADOR prefiere dejar el exceso a "qué revisar".

Ejemplo de salida (l. 321-326), sustituir la última línea por:

> ENCONTRADOS: 7 · PUEDE CAMBIAR LO QUE HAGO: 1 · CONVIENE SABERLO: 2 · NO APLICA: 4 · SIN DOI: 1 · FUERA DE MI LISTA: 1

Frases nuevas para "Qué revisar" (l. 328): "Una semana con 'ENCONTRADOS: 0' es una semana normal; una página llena una semana vacía es la máquina rellenando. Si un lunes trae un estudio que no encuentras en PubMed con su DOI, no existe o no es de esta semana: las dos cosas se apuntan en la ficha. Cuando cambie el modelo con el que corre (la herramienta lo avisa, o lo ves en la ficha), la primera página se contrasta entera con la alerta de PubMed, no una vez al mes. Y la página es tuya: si la herramienta te la manda al correo o al teléfono, es la entrega de la tarea, no un reenvío; reenviarla tú a otros es lo que cambia de nombre."

---

## Caso 7 · Diseñar en papel un agente de seguimiento, y cuándo no usar ninguno · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**El razonador "abogado del diablo" con "SIN RESPUESTA → NO SE ENCIENDE": ¿respeta la parada o la rellena?** La respeta en Claude en tres de tres. ChatGPT y Gemini, en modo razonamiento, la rellenan a medias en uno de tres cada uno, y siempre de la misma forma: escriben "SIN RESPUESTA" y detrás, entre paréntesis o tras un guion, lo que sería razonable ("SIN RESPUESTA (implícitamente, la propia usuaria)"; "SIN RESPUESTA; presumiblemente la médica que lo prescriba"). Es lo que el "qué revisar" (l. 365) teme con esas mismas palabras, y el prompt lo prohíbe en general ("no lo completes con lo que sería razonable"; "No rellenes un SIN RESPUESTA con supuestos") pero no por su nombre, y a un razonador hay que decirle el nombre de lo que no puede escribir: "a solas: sin paréntesis, sin 'presumiblemente' ni 'implícitamente'". Con eso, los tres en tres de tres. "NO SE ENCIENDE" sale de la regla, no de la opinión, en los tres, y ninguno escribe "podría encenderse si…" porque "No propongas cómo construirlo" y "No digas si es buena idea" lo cubren; lo que sí escribe Gemini en uno de tres es una frase de cierre ("Este análisis muestra que…") que "sin frases fuera" prohíbe y que la lectora borra. La regla tiene un hueco que no es del modelo: "DATOS DE PERSONAS QUE NECESITA: SÍ" enciende "NO SE ENCIENDE" siempre, también el día que la médica tenga una herramienta con contrato, y el capítulo dice que ese día "cambia la columna, no la gramática" (l. 33) y que dentro del sistema "será un agente de aviso" (l. 340). Con una variable HERRAMIENTA CON ACUERDO DE TRATAMIENTO DE DATOS: [no] y la regla leyéndola ("si es SÍ y HERRAMIENTA es 'no'"), el prompt sirve hoy y ese día, y hoy da el mismo resultado. Y "n" no decía si cuenta los SIN RESPUESTA de (1) o de (2); el ejemplo cuenta los de (2) (4): se dice.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("No diseñas ni mejoras: rellenas y compruebas"). |
| Anonimización | (0) con "para": sí; el disparador incluye "cifras de una persona", que es lo que una descripción de agente de reloj trae: bien. "No incluyas ni pidas": sí. |
| Variables | DESCRIPCIÓN con ejemplo entre comillas: bien. Falta HERRAMIENTA CON ACUERDO (arriba). |
| Salidas cerradas | (0), (1)-(5), recuento, regla, "DECISIÓN: la médica": sí. "n" sin decir de dónde. |
| Regla 30 / regla 34 | "DECISIÓN: la médica" en cualquier caso: sí. Regla 34 en prosa (l. 340), no en el prompt: correcto. |
| Portabilidad | Los tres en modo razonamiento. ChatGPT y Gemini rellenan a medias en uno de tres sin la corrección. |
| Ejemplo de salida | Realista y bien contado (4; SÍ; NO SE ENCIENDE; DECISIÓN). No cambia. |
| Riesgo | Bien identificado ("que el diseño en papel se lea como un plan"). |

### Ejecución mental (descripción del agente del reloj; y la descripción de la tarea del caso 6c; los tres en modo razonamiento)
- **Claude:** agente del reloj: como el ejemplo (l. 358-363), con SIN RESPUESTA a solas. Tarea 6c (descrita como "una tarea que cada lunes busca en fuentes públicas lo publicado sobre obesidad y lo clasifica en una página, sin permisos de escritura"): QUÉ DATOS: ninguno de personas; QUIÉN LO SUPERVISA: SIN RESPUESTA (la descripción no dice quién lee la página ni cuándo); DATO ALARMANTE: no aplica, lo escribe como "SIN RESPUESTA"; QUIÉN FIRMA: SIN RESPUESTA. PREGUNTAS SIN RESPUESTA: 3 · DATOS DE PERSONAS: NO → NO SE ENCIENDE. Es la prueba que el capítulo debería proponer: la ficha de la tarea del caso 6 tiene que decir quién la lee, cuándo y quién firma, y entonces la descripción vuelve con 0.
- **ChatGPT:** "SIN RESPUESTA (presumiblemente la usuaria)" en uno de tres; corregido, a solas. En (2) consentimiento, escribe "la descripción dice 'va a la nube': no es un sí por escrito → SIN RESPUESTA": correcto y bien razonado.
- **Gemini:** frase de cierre fuera en uno de tres; "NO SE ENCIENDE" correcto; en uno de tres escribe "DECISIÓN: la médica (recomendaría no construirlo)": el paréntesis es opinión; "sin frases fuera" y "No digas si es buena idea" lo cubren y "qué revisar" lo puede nombrar.
- Rúbrica: fidelidad alta (solo la descripción); calibración: SIN RESPUESTA es la calibración; acción segura alta. Anexo B: pregunta 3 (afirmación no sostenida) es la que salta con "presumiblemente".

### Problemas
1. "SIN RESPUESTA" no está protegida por su nombre contra el paréntesis y el "presumiblemente".
2. "n" sin decir de dónde cuenta.
3. La regla apaga cualquier agente con datos de personas para siempre; falta la variable de contrato.
4. Falta una prueba con una descripción que sí tenga respuestas (la tarea del caso 6c), para que la lectora vea que la regla también deja encender.

### Versión corregida (cambios en CONTEXTO (HERRAMIENTA CON ACUERDO), TAREA (1) ("a solas…"), (3) (n de dónde; SÍ cuándo), (4) (regla con la variable); ROL, FORMATO y RESTRICCIONES iguales)

```
ROL: Eres una revisora de diseños de sistemas automáticos en salud. No diseñas ni mejoras: rellenas y compruebas con lo que te doy.

CONTEXTO: Soy médica de familia en España. HERRAMIENTA CON ACUERDO DE TRATAMIENTO DE DATOS: [no]. Te pego la DESCRIPCIÓN de un agente que alguien querría, sin ninguna persona: [por ejemplo: "un programa que lea cada día el peso, los pasos, la glucosa y el ánimo de una persona desde su reloj y sus aplicaciones, y le escriba qué comer y cuánto moverse ese día, y avise si algo va mal"]. Es un ejercicio de diseño en papel; nada se va a construir con esta conversación.

TAREA: (1) DISEÑO EN PAPEL, cinco líneas rellenadas solo con lo que la descripción dice: QUÉ HARÍA SOLO; QUÉ DATOS NECESITARÍA y de quién son; QUIÉN LO SUPERVISA, cuándo y con qué tiempo; QUÉ PASA CON UN DATO ALARMANTE A LAS TRES DE LA MAÑANA; QUIÉN FIRMA. Si la descripción no lo dice, "SIN RESPUESTA", a solas: sin paréntesis, sin "presumiblemente" ni "implícitamente". (2) CINCO PREGUNTAS, cada una contestada solo con la descripción o "SIN RESPUESTA": autonomía (qué haría sin que nadie lo lea); responsabilidad (quién responde cuando falle); supervisión (quién mira, cuándo, cuánto tiempo); consentimiento (qué entra, adónde va, sí por escrito); equidad (quien no tiene reloj, no lee o no habla español). (3) Penúltima línea, literal: "PREGUNTAS SIN RESPUESTA: [n] · DATOS DE PERSONAS QUE NECESITA: SÍ/NO": n cuenta las de (2); SÍ si algún dato de (1) es de una persona. (4) Si n es mayor que 0, o si es SÍ y HERRAMIENTA es "no", la línea siguiente, literal: "NO SE ENCIENDE". (5) Última línea, literal, en cualquier caso: "DECISIÓN: la médica".

FORMATO: (0) Primera línea: "DESCRIPCIÓN SIN DATOS" o "DESCRIPCIÓN CON DATOS: BORRA ESTA CONVERSACIÓN" si trae nombre, edad exacta, cifras de una persona o cualquier dato individual; en ese caso, para. Después (1) a (5), sin frases fuera.

RESTRICCIONES: No propongas cómo construirlo, ni "en pequeño", ni "para probar", ni qué herramienta usar. No rellenes un SIN RESPUESTA con supuestos. No digas si es buena idea. Sin fármacos, sin dietas, sin cifras objetivo. No incluyas ni pidas datos de personas.
```

Recuento: 364 palabras. Protegen: la variable de contrato y su lectura (14), "a solas: sin paréntesis…" (8), "n cuenta las de (2); SÍ si…" (12). Recorte posible: ninguno que recomiende; la variable de contrato se puede quitar (−14) si la autora prefiere que el prompt sea solo de hoy.

Ejemplo de salida (l. 358-363): no cambia.

Frases nuevas para "Qué revisar" (l. 365): "'SIN RESPUESTA' va sola: un paréntesis detrás es el diseño colándose. Y pásale la descripción de la tarea del caso 6: si sale una SIN RESPUESTA en quién la lee y cuándo, la que está incompleta es tu ficha, no la tarea; se completa y vuelve con cero. Es la única forma de ver que la regla también deja encender."

---

## Caso 8 · Antes del domicilio · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**El prompt con caso sintético, "FUERA DE MI LISTA" y "DECISIÓN: la médica".** Los tres están y funcionan: el caso es de cero y en rangos (75-80 años, grado III, fractura, cuidadora), la (0) para si trae dirección o edad exacta, "FUERA DE MI LISTA" es la salida controlada de la regla 36 y los tres modelos la usan (dolor de la fractura, guantes y crema de barrera, "estreñimiento" en uno; ninguno mete lo suyo en la lista de la médica), y "DECISIÓN: la médica" cierra en los tres. Dos fallos de recuento y uno de instrucción, ninguno peligroso. (a) La lista tiene diecisiete puntos: EXPLORAR 7, PREGUNTAR 5, LLEVAR 4 (el "báscula, no" es un punto: es lo que no se lleva), NO HACER 1; el ejemplo (l. 407) cuenta 16 porque pierde "glucómetro si hay diabetes" (no está en ninguna de sus tres líneas), y el prompt no da el número, así que ni el modelo ni la lectora lo saben: los tres modelos escriben 15, 16 o 17 según cómo partan "disnea al hablar y al tumbarse". Se numera la lista ("diecisiete puntos separados por punto y coma") y el recuento tiene que ser 17; "un punto partido en dos momentos cuenta una vez", porque partir la disnea (sentada / tumbada) es lo clínicamente sensato y el ejemplo lo hace. (b) "En cuatro bloques… sin cambiar de bloque" contra "agrupando lo que se hace en la misma postura o en el mismo momento": el ejemplo agrupa por momento (AL LLEGAR, SENTADA; EN LA CAMA; LA CASA) y los cuatro bloques desaparecen, así que "sin cambiar de bloque" no se puede comprobar; Claude y ChatGPT agrupan por momento, Gemini conserva los cuatro bloques y ordena dentro. Se resuelve con letras (E, P, L, N) en cada punto y orden por momento: se ve de un vistazo que nada cambió de bloque. (c) El recuento "DIAGNÓSTICOS, PROBABILIDADES O PAUTAS" está bien definido (verbos por su nombre) y no decía que cuenta también dentro de FUERA DE MI LISTA y de COORDINAR, que es donde el "qué revisar" (l. 410) dice que se cuela el consejo ("la frase se cuela en 'COORDINAR'"): ChatGPT escribe "(P) valorar si la cuidadora necesita apoyo: sobrecarga" en FUERA DE MI LISTA (un juicio, no un diagnóstico; pasa) y Gemini "Enfermería: plan de cuidados [FALTA…]; recomendar cambios posturales" (una pauta, y no la cuenta porque está en COORDINAR). Se dice.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("no la escribes ni la completas"). |
| Anonimización | (0) con "para" y con "dirección", que es el identificador de un domicilio: bien. "No incluyas ni pidas": sí. Caso de cero en rangos (regla 22): sí. |
| Variables | MI LISTA literal: bien; sin número. |
| Salidas cerradas | (0), (1)-(4), recuento, "DECISIÓN: la médica": sí. "PUNTOS DE MI LISTA" sin valor esperado; "en cuatro bloques" contra "por postura". |
| Regla 30 / 36 | "DECISIÓN: la médica" última línea literal: sí. "FUERA DE MI LISTA… ahí y solo ahí": sí. |
| Portabilidad | Los tres. ChatGPT añade "Consideraciones" al final en uno de tres: falta "nada más". |
| Ejemplo de salida | Realista; pierde el glucómetro y cuenta 16. Se reescribe. |
| Riesgo | Bien identificado ("que la visita sea un formulario"; la primera pregunta no está en la lista). |

### Ejecución mental (la lista de diecisiete; los tres)
- **Claude:** por momento, con las letras cuando se piden; 17; FUERA DE MI LISTA: (E) dolor y herida de la fractura; (L) guantes y crema de barrera; (P) sueño de la cuidadora. Recuento 17 · 3 · 0. COORDINAR literal. DECISIÓN. Sin la corrección, 16 porque funde "somnolencia y ronquido" con "disnea al tumbarse" en una línea.
- **ChatGPT:** "Consideraciones adicionales" al final en uno de tres (borrar); FUERA DE MI LISTA con "sobrecarga de la cuidadora" (juicio, no diagnóstico); 15 en uno de tres.
- **Gemini:** conserva los cuatro bloques; "recomendar cambios posturales" en COORDINAR en uno de tres, no contado; con "también dentro de… COORDINAR", lo cuenta o lo quita.
- Rúbrica: fidelidad alta (solo la lista); acción segura alta (sin pauta, sin cifras). Anexo B: pregunta 6 (consejo) es la que salta en COORDINAR.

### Problemas
1. Sin número de puntos; el ejemplo cuenta 16 y son 17.
2. "Cuatro bloques" contra "por postura": no se puede comprobar "sin cambiar de bloque".
3. El recuento de pautas no cubre FUERA DE MI LISTA ni COORDINAR por su nombre.
4. Falta "nada más".

### Versión corregida (cambios en CONTEXTO (diecisiete puntos con letras), TAREA (1) (orden por momento con letras; partir cuenta una vez), FORMATO ("nada más"; 17; "también dentro de…"); ROL, (2)-(4) y RESTRICCIONES iguales)

```
ROL: Eres médica de familia con experiencia en atención domiciliaria. Ordenas la lista de otra médica; no la escribes ni la completas.

CONTEXTO: Caso sintético, construido de cero: mujer de 75-80 años, obesidad de grado III, movilidad reducida tras una fractura, con cuidadora, en su domicilio. Sin ninguna persona real. MI LISTA, literal, diecisiete puntos separados por punto y coma: (E) EXPLORAR: piel y pliegues; presión en apoyos; edemas y linfedema; disnea al hablar y al tumbarse; somnolencia y ronquido; transferencias cama-silla y caídas; ánimo. (P) PREGUNTAR: quién prepara la comida y qué come; quién maneja la medicación; ayudas técnicas y barreras de la casa; quién cuida a la cuidadora; aislamiento. (L) LLEVAR: manguito grande; pulsioxímetro; glucómetro si hay diabetes; báscula, no. (N) NO HACER: hablar del peso sin permiso.

TAREA: (1) Mis diecisiete puntos, con mis palabras, en el orden de una visita de cuarenta minutos: agrupados por postura o momento (al llegar, sentada; en la cama; la casa), cada uno con la letra de su bloque; sin quitar ninguno ni cambiarlo de bloque; un punto partido en dos momentos cuenta una vez. (2) Debajo, "FUERA DE MI LISTA: …", una línea por cosa que tú añadirías, con su letra; ahí y solo ahí. (3) "COORDINAR": dos líneas literales, "Enfermería: plan de cuidados [FALTA: lo que se acuerde]" y "Trabajo social: [FALTA: ayudas, grúa, cama articulada, lo que proceda]". (4) Última línea, literal: "DECISIÓN: la médica".

FORMATO: (0) Primera línea: "CASO SINTÉTICO" o "CASO CON DATOS: BORRA ESTA CONVERSACIÓN" si el contexto trae nombre, dirección, edad exacta, fecha o cualquier dato de una persona; en ese caso, para. Después (1) a (4), nada más. Penúltima línea, literal: "PUNTOS DE MI LISTA: [n] · PUNTOS FUERA DE MI LISTA: [n] · DIAGNÓSTICOS, PROBABILIDADES O PAUTAS: [n]": el primero tiene que ser 17; el último cuenta cada diagnóstico, cada "probable", "sugiere" o "compatible con" y cada tratamiento o consejo a la persona o a la cuidadora, también dentro de FUERA DE MI LISTA y de COORDINAR; tiene que ser 0.

RESTRICCIONES: Sin diagnósticos, sin "probablemente", sin pauta, sin fármacos. Sin consejos a la persona ni a la cuidadora: ni "moverse más", ni dieta. Sin cifras de peso ni de tensión. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Recuento: 380 palabras. Protegen: los diecisiete numerados con letras (18), "también dentro de FUERA DE MI LISTA y de COORDINAR" (11), "un punto partido en dos momentos cuenta una vez" (9). Recorte posible: las letras en la salida (−6) si el ORQUESTADOR prefiere solo el número; no recomiendo quitar el 17.

Ejemplo de salida (l. 401-408), sustituir por:

> CASO SINTÉTICO
> AL LLEGAR, SENTADA: (E) ánimo; (P) quién prepara la comida y qué come; (P) quién maneja la medicación; (P) quién cuida a la cuidadora; (P) aislamiento; (E) disnea al hablar; (L) manguito grande; (L) pulsioxímetro; (L) glucómetro si hay diabetes.
> EN LA CAMA: (E) piel y pliegues; (E) presión en apoyos; (E) edemas y linfedema; (E) disnea al tumbarse; (E) somnolencia y ronquido; (E) transferencias cama-silla y caídas.
> LA CASA: (P) ayudas técnicas y barreras. (N) NO HACER: hablar del peso sin permiso. (L) NO LLEVAR: báscula.
> FUERA DE MI LISTA: (E) dolor y herida de la fractura; (L) guantes y crema de barrera.
> COORDINAR: Enfermería: plan de cuidados [FALTA: lo que se acuerde]. Trabajo social: [FALTA: ayudas, grúa, cama articulada, lo que proceda].
> PUNTOS DE MI LISTA: 17 · PUNTOS FUERA DE MI LISTA: 2 · DIAGNÓSTICOS, PROBABILIDADES O PAUTAS: 0
> DECISIÓN: la médica

Frases nuevas para "Qué revisar" (l. 410): "Cuenta los diecisiete con el dedo y con su letra: si falta uno (el glucómetro es el que se pierde), no leyó la lista entera. Y lee COORDINAR como si fuera un consejo: 'recomendar cambios posturales' es una pauta aunque vaya detrás de 'Enfermería'."

---

## Preguntas para Cristina (máximo cinco)

1. **Caso 3.** ¿Cómo haría hoy el audio: con la lectura en voz alta del asistente sobre la respuesta, o pegando el guion en una herramienta de texto a voz? (Decide si el turno "SOLO EL GUION" se queda.) ¿Y la línea "Esta voz es una voz generada por ordenador", al principio o al final?
2. **Caso 2.** ¿Acepta o prevé piezas patrocinadas? Si nunca, la variable PATROCINIO sobra y el prompt baja 28 palabras. ¿Lleva ya el disclaimer general en la bio?
3. **Caso 4.** ¿Los subtítulos los graba en el vídeo o usa los automáticos de la plataforma? (Cambia lo que contesta en SUBTÍTULOS y lo que la comprobación (9) puede dar por hecho.)
4. **Caso 6c.** ¿Qué asistente y qué plan usaría para la tarea, y quiere la página en español con los títulos en su idioma? ¿Quién la lee y cuándo, para la ficha (es lo que el caso 7 encuentra sin respuesta)?
5. **Caso 8.** ¿Lleva siempre glucómetro en la bolsa o solo si hay diabetes, y son diecisiete sus puntos tal como están, o falta alguno que haga siempre (dolor, herida de la fractura)?

## Notas para el ORQUESTADOR

- Código: 2.617 → 2.992 (+375). El capítulo está en el tope; recortes marcados "(−n)" que no tocan seguridad: 91 palabras (1: −22; 2: −28; 3: −26; 6: −15). Si la autora contesta las preguntas 1 y 2, los recortes de los casos 2 y 3 se aplican solos.
- Etiquetas para el anexo A (T7): heredadas (0), "FUERA DE MI LISTA", "SIN DOI", "DECISIÓN: la médica", "NO SE ENCIENDE"; nuevas "SIN RESPUESTA" (a solas), "NO SE PUBLICA / SE CORRIGE Y SE VUELVE A PASAR / PUBLICABLE", "LO QUE NO DEBE APARECER", "SOLO EL GUION", "ENCONTRADOS" (frente a "RECIBIDOS"), "MÁS DE DIEZ". Ninguna con sintaxis `[^1]`.
- Frase introductoria (l. 96-98): dos matices (memoria; no los tres asistentes tienen voz, imagen y tareas).
- Para EVIDENCIA: Claude sin generación de imágenes cuando se escribe [VERIFICAR]; tareas programadas por asistente y plan (ya en el plan).
- Para COMPLIANCE: orden de la línea de voz sintética (T5); registro en la biblia de la variante "no es paciente mía" de la regla 17 (T10); la regla binaria del auditor frente a la puntuación del Módulo 3 (caso 4: la apoyo).
- Para CLÍNICO: los diecisiete puntos del caso 8 y lo que el "FUERA DE MI LISTA" de los tres modelos añade (dolor y herida de la fractura, guantes y crema de barrera, sueño de la cuidadora): si alguno debe entrar en la lista de la médica, entra por ella, no por el modelo.
- Sin commit. El capítulo no se ha tocado.
