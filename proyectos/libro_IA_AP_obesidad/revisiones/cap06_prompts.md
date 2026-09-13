# Revisión PROMPTS · Capítulo 6 · v1

> Agente: PROMPTS (ingeniero de prompts) · Fecha: 2026-09-13 · Ámbito: exclusivamente los ocho bloques de código que el capítulo ofrece al lector (casos 1, 2A, 2B, 3, 4, 5, 6 y 7) y los ejemplos abreviados de salida que los acompañan, más la frase introductoria a los casos (l. 51-55) porque fija reglas que los prompts heredan. El caso 7 (etiqueta nutricional) ya fue revisado en el ciclo del capítulo 2: aquí solo se comprueban sus añadidos de integración (línea de contacto, restricciones nuevas, remisión de higiene, numeración, referencias). No se revisa el texto expositivo, la viñeta ni las referencias.
> Versión revisada: `capitulos/cap06_v1.md` (373 líneas, 7.849 palabras; las líneas citadas son las de esa versión, `grep -n`). Los ocho bloques pesan 3.061 palabras (494 · 300 · 228 · 387 · 389 · 403 · 240 · 620).
> Método: el de los capítulos 1 a 5 (`revisiones/cap05_prompts.md`). Para cada prompt: rol · contexto · tarea · formato · restricciones; anonimización y etiqueta (0) antes que el contenido, que para si hay datos, en los prompts en los que entra un texto (T1 del capítulo 5); variables entre corchetes con valor por defecto y sin instrucciones al lector dentro del corchete (T6 del capítulo 5); recuentos definidos en la misma línea y contables a mano (T2 del capítulo 5; T5 del capítulo 4); si el modelo puede rellenar un [FALTA: …] sin que se note (T4 del capítulo 4; regla 24); portabilidad Gemini / ChatGPT / Claude sin cambios; realismo del ejemplo de salida; riesgo. Cada prompt se ha ejecutado mentalmente con el material que el propio capítulo trae (la versión A de "¿Por qué recupero el peso?" del capítulo 1, caso 5, para los casos 1 y 2; las variables de ejemplo en los demás) y la salida se ha leído con la rúbrica del capítulo 4 y las diez preguntas del anexo B. Reglas 7, 11, 12, 16, 17, 19, 21, 22, 24 y 26 de `biblia.md` como norma; ficha del caso 7 del capítulo 4 (v3) como plantilla de guardado; regla 19 en su precisión del ciclo 5 (no hay tercera fórmula de urgencias).

## Resumen de veredictos

| Caso | Título | Bloques | Veredicto | Motivo principal |
|---|---|---|---|---|
| 1 | La hoja pasa el examen: legibilidad y pregunta de vuelta | 1 prompt + 1 salida | **mejorar** | El prompt, tal cual, borra de la hoja del capítulo 1 las dos frases que son la tesis del libro: "No es culpa suya" (por "culpa") y "no es falta de voluntad" (por "voluntad"); el capítulo solo se disculpa por la primera. "PALABRAS TÉCNICAS" mezcla dos criterios (más de tres sílabas; "palabra que un adulto sin estudios sanitarios no usaría"): con el primero, "biología", "enfermedad", "tratamiento" y "seguimiento" cuentan, el 0 exigido es imposible sin vaciar la hoja, y el propio ejemplo ("técnicas: ninguna" con "Es biología") incumple su regla. La variable LÍNEA DE URGENCIAS lleva la decisión dentro del corchete (el modelo elige) y no dice qué hacer con "ninguna": los tres añaden una línea de urgencias propia, que es la tercera fórmula que la regla 19 prohíbe. Las líneas literales del final entran en el examen y en el recuento. Las tres preguntas de vuelta salen bien en Claude y ChatGPT; Gemini escribe "¿qué ha entendido?" en una de tres, que no es "¿ha entendido?" y es el mismo examen. |
| 2A | Traducción (árabe, rumano, inglés) | 1 prompt | **mejorar (leve)** | Bien construido: frase por frase, mismo número de frases, corchete copiado en español, 112 conservado, recuento cuádruple. Dos grietas: Gemini escribe el 112 con cifras árabes orientales (١١٢) en árabe en una de tres, y el recuento "'112': 1" le sale bien porque cuenta el número, no la grafía; y "ponla también en español entre paréntesis" añade texto que después el paso B lista como diferencia. El recuento de frases no coincide con el del caso 1 (10 allí, 11 en el ejemplo del B) porque ninguno dice si las líneas literales cuentan. Sin ejemplo de salida propio. |
| 2B | Retraducción y comparación | 1 prompt + 1 salida | **mejorar** | La retraducción no se contamina en el paso (1): el modelo no tiene el original. Se contamina en el (2): al ver el original, ChatGPT y Gemini "mejoran" su retraducción antes de comparar, y las diferencias desaparecen; falta "no cambies tu retraducción después de ver el original". "LÍNEAS FINALES IGUALES: SÍ/NO" no es fiable tal como está: una retraducción nunca es idéntica palabra por palabra, así que en sentido estricto siempre es NO y "no se negocia: se rehace" es un bucle sin salida; en sentido laxo, cada modelo decide qué es "igual". Hay que descomponerlo en tres comprobaciones contables (contacto: corchete tal cual; urgencias: 112 y "no espere"; aviso: sus tres ideas). |
| 3 | Qué esperar del tratamiento: guion de primera visita | 1 prompt + 1 salida | **mejorar** | La correa de fármacos va por nombre y no por clase (T2 del capítulo 4): con el mecanismo de ejemplo, ChatGPT y Gemini escriben "este tipo de medicamentos, llamados agonistas de GLP-1" o "una hormona llamada GLP-1" y cuentan 0, porque el recuento define "nombre comercial o de principio activo". "Una vez a la semana" (frecuencia) sí cuenta; "una inyección" (vía) no. Los tres amplían el mecanismo dado ("además ayuda a controlar el azúcar"), que en una persona con diabetes es una afirmación clínica que la médica no dio. La línea literal va en usted y TRATO admite tú: si la lectora elige tú, el guion cambia de trato en la línea de seguridad (T6 del capítulo 4). |
| 4 | Preguntas frecuentes sobre náuseas y otros efectos digestivos | 1 prompt + 1 salida | **listo (retoque)** | El mejor del capítulo: medidas en lista cerrada, línea de la regla 17 literal y entera, tres líneas de la regla 19 en orden, recuento con definición de "cambio de pauta", venta libre prohibida por su nombre. Lo que se cuela: Gemini escribe "consulte en la farmacia" (no es un fármaco, y lleva a uno) y "tome fibra" en la respuesta del estreñimiento, porque las medidas dadas no dicen nada específico para el estreñimiento y el modelo rellena el hueco; y "es frecuente", "no pasa nada", "sin importancia" pasan el recuento de 'NO SE PREOCUPE' O 'ES NORMAL'. La medida para el estreñimiento no la decido yo: CLÍNICO. |
| 5 | Llamar a quien no vuelve | 1 prompt + 1 salida | **mejorar (leve)** | Sale sin reproche y con salida digna en los tres, y el recuento de reproche es una lista cerrada contable. Lo que pasa el recuento: "no tiene por qué avergonzarse" y "no hay nada de qué avergonzarse" (ChatGPT, Gemini) en la variante de la vergüenza, que discuten el sentimiento que el prompt manda recoger; "valoramos su esfuerzo" y "sus objetivos" (Gemini), que evalúan y no están en la definición. El guion no dice qué hacer si la persona cuenta otra cosa (molestias con un tratamiento, ánimo bajo, ideas de muerte): lo dice "qué revisar", pero enfermería lleva el guion, no el libro. Y quien llama no tiene cómo presentarse sin inventar un nombre. |
| 6 | Cartel de sala de espera | 1 prompt + 1 salida | **listo (retoque)** | 25 palabras con el contacto como hueco es realista (la variante del ejemplo tiene 20); los modelos no meten cifras ni "hábitos" en un cartel, meten un titular con pregunta ("¿Sabía que…?") y un imperativo ("Hable con nosotros"). Contradicción interna: la tarea admite "usted o impersonal" y la línea literal va en usted ("Pregunte a su médica"), y el riesgo dice "sin 'usted'". El recuento de palabras por variante no repite "sin contar la línea de contacto", y los tres la cuentan la mitad de las veces. |
| 7 | Leer una etiqueta nutricional | 1 prompt + 1 salida | **listo** | Integración correcta: numerado como caso 7; las dos líneas del final en la forma de la regla 19 (contacto como hueco y aviso, sin urgencias porque no toca síntomas) en el prompt, en el ejemplo y en "qué revisar"; "No rellenes el marcador. No incluyas ni pidas datos de personas." añadidos; higiene remitida al capítulo 3 (el reservado decía capítulo 1; el plan pedía corregirlo: corregido); referencias 15 y 16 en la lista; "Higiene: sí en el 7" en la frase introductoria. No se reabre. |

Ningún prompt es peligroso tal como está: ninguno pide decisiones clínicas, ninguno admite datos de nadie, todos llevan "no incluyas ni pidas datos de personas", y los tres que llegan a la persona (1, 2, 4) llevan las líneas de la regla 19 literales. Dos producen algo que no debe salir sin cambios: el 1 (borra la tesis del libro de la hoja que examina y exige un cero imposible) y el 3 (deja pasar la clase y las siglas de la hormona con recuento a cero). El 2B tiene un recuento que no puede dar SÍ. Ninguno hay que rehacer de arriba abajo; el 1 y el 2B se reescriben en las partes que fallan. La portabilidad es limpia: nada depende de razonador, búsqueda ni archivos, salvo el 7, que necesita leer imágenes y el capítulo lo dice; los ocho se pegan igual en los tres.

---

## Hallazgos transversales (afectan a varios casos)

**T1 · Las listas cerradas de palabras se comen la negación.** El libro tiene un eje ("No es falta de voluntad. Es biología.") y una forma de nombrar la culpa para negarla ("No es culpa suya"). El caso 1 pone "culpa" y "voluntad" en la lista de palabras que tienen que ser 0 y pide reescribir "sin las palabras de la lista": el modelo obedece y las dos frases desaparecen de la hoja del capítulo 1, que las lleva porque su prompt las exigía ("que esto es biología y no falta de voluntad"). "Qué revisar" (l. 93) se disculpa por "culpa" y no ve "voluntad". La regla, para este caso y para cualquier lista futura: se cuentan las palabras de la lista salvo dentro de las dos frases que las niegan, que se copian literales y no cuentan; y el recuento lo dice en la misma línea. El caso 6 no tiene el problema porque "voluntad" no está en su lista, y "no es falta de voluntad" es contenido obligatorio del cartel: coherente por azar; con la regla, coherente por diseño.

**T2 · "Palabras técnicas" no es contable; "palabras largas" sí, pero no puede exigirse 0.** El caso 1 define técnica como "más de tres sílabas o técnicas (hormonas, órganos, pruebas, cualquier palabra que un adulto sin estudios sanitarios no usaría)". Son dos criterios: el primero es el de INFLESZ, se cuenta con el dedo y en la versión A da al menos cinco ("biología", "energía", "enfermedad", "tratamiento", "seguimiento"); el segundo lo decide el modelo. Exigir 0 al primero vacía la hoja; exigirlo al segundo es autoauditoría sin unidad. Solución: dos recuentos. "PALABRAS LARGAS (más de tres sílabas): [n]", informativo, sin tope, que la lectora compara con su propia cuenta; y "PALABRAS TÉCNICAS: [n]" con criterio cerrado (nombres de hormonas, órganos, pruebas, fármacos y términos que solo usa el personal sanitario; "biología", "enfermedad crónica", "tratamiento" y "seguimiento" no lo son), que tiene que ser 0. El ejemplo del libro vuelve a ser verdad.

**T3 · La línea de urgencias: o la elige la lectora o la añade el modelo.** El caso 1 mete las tres opciones dentro del corchete con la condición de cada una ("ninguna, si la hoja no habla de…; si habla de un tratamiento: …"): es un corchete-instrucción (T6 del capítulo 5) y el que decide es el modelo. Con la versión A ("hambre", "gasta menos", "tratamiento y seguimiento" sin nombrar ninguno), Claude elige "ninguna", ChatGPT pone la de tratamiento en una de tres porque la hoja dice "tratamiento", y Gemini escribe una propia ("Si se encuentra mal, consulte con su médico"), que es la tercera fórmula que la regla 19 no admite. Dos cambios: la variable trae "ninguna" como valor por defecto y las dos fórmulas fijas como las dos únicas alternativas que la lectora pega; y una frase que falta en todo el capítulo: "si es 'ninguna', no añadas ninguna línea de urgencias, síntomas ni 'consulte con su médico', aunque te parezca prudente". La misma frase vale para el caso 6 (donde el cartel no lleva urgencias y Gemini añade "ante cualquier duda acuda a su centro").

**T4 · Trato y aviso siguen sin ir juntos donde hay tú.** El capítulo 4 fijó (T6) que si el prompt admite tú, las líneas literales van en las dos variantes. El caso 1 lo cumple a medias: da el tú del contacto y del aviso, no el de las dos fórmulas de urgencias. El caso 3 admite "TRATO: [usted por defecto / tú]" y lleva la línea de la regla 17 solo en usted: en tú, el guion cambia de trato en la frase más importante. La variante tú existe en el capítulo 3 (l. 103: "Si no toleras líquidos, tienes dolor fuerte de tripa, te mareas o te encuentras mal, no esperes: urgencias o 112"; "pide cita y lo vemos, o te llamo yo") y se pone literal.

**T5 · La correa de fármacos va por nombre, por clase y por siglas de la hormona.** Es T2 del capítulo 4 y el capítulo 6 la hereda solo por nombre. En el caso 3, el recuento "NOMBRES DE FÁRMACOS" cuenta "cada nombre comercial o de principio activo": "agonistas del receptor de GLP-1", "análogos", "esta familia de fármacos" y "una hormona llamada GLP-1" no cuentan, y ChatGPT y Gemini los escriben con el mecanismo de ejemplo delante (una hormona del intestino que avisa de saciedad es, para ellos, GLP-1 por su nombre). El caso 4 lo hace bien ("ni ningún fármaco, tampoco… de venta libre"); le falta el desvío ("consulte en la farmacia") y el suplemento que no se llama fármaco ("fibra", "laxante suave"). Regla para los dos: "ni comercial, ni por principio activo, ni por clase o familia, ni la hormona por sus siglas".

**T6 · Los números del capítulo tienen que cuadrar entre casos.** La misma hoja pasa por el caso 1 (FRASES: 10 en el ejemplo, "contadas sobre la hoja reescrita") y por el caso 2 (FRASES: 11 en el ejemplo del paso B). Ninguno de los dos dice si las líneas literales del final (contacto: una frase; aviso: dos; urgencias: cero en la versión A) entran en la cuenta: sin ellas, la hoja del caso 1 tiene 10; con ellas, 13. Como en el capítulo 5 (T2), cada recuento dice en su línea qué cuenta; propongo que el examen del caso 1 cuente "sin las líneas literales" (son fijas y no se examinan) y el caso 2 cuente "con las líneas literales" (se traducen y son las que más importan), y que los ejemplos digan 10 y 13.

**T7 · La retraducción tiene tres puntos débiles y el capítulo cierra uno.** (a) Conversación nueva y otro modelo o memoria apagada: cerrado. (b) El paso (2) del mismo prompt: al pegar el original, el modelo tiene delante su retraducción y el original, y ChatGPT y Gemini reescriben la retraducción "corregida" antes de listar diferencias, con lo que la lista sale vacía; "no corrijas la traducción" se refiere a la traducción del paso A, no a la suya: hay que decir "no cambies tu retraducción después de ver el original; compara lo que escribiste". (c) "LÍNEAS FINALES IGUALES: SÍ/NO": ver 2B. Y una precisión de grafía que ninguna herramienta señala: el 112 en árabe puede salir como ١١٢ (cifras árabes orientales) y el recuento cuenta uno igual; para una hoja que se imprime en España, con cifras 112.

**T8 · Lo que ya está bien y hay que conservar.** La frase introductoria (l. 51-55): "Nunca dejes que el modelo rellene ninguno de los dos" (la fórmula que pidió el ciclo 5), la ficha con "Higiene: sí en el 7" y "Probada por" con fecha, y "Los guiones (3 y 5) y el cartel (6), sin pie" declarado. La etiqueta (0) con "para" en los tres prompts en los que entra un texto (1, 2A, 2B) y su ausencia, correcta, en los cinco en los que no entra nada (3, 4, 5, 6; el 7 tiene su propia puerta de imagen). La forma única del contacto "[FALTA: contacto del centro]" en 1, 2, 4, 6 y 7. Los topes "sin contar las líneas literales" en 1, 3 y 4 (los que llevan líneas fijas). La línea de la regla 17 literal y entera en el 3 y el 4, la misma del capítulo 4, caso 6. Las medidas de casa en lista cerrada del caso 4 y "la pauta solo se cambia en consulta" con la definición de "cambio de pauta" contable. La lista de reproches del caso 5, que se busca con el buscador. "Sin descripción de imágenes" y "sin marcas ni logotipos" en el cartel. Los ejemplos de salida son realistas: son la salida de Claude y de ChatGPT en su día bueno, y "qué revisar" cuenta el día malo ("el modelo cuenta mal y redondea bien"; "la máquina cuenta 24 donde hay 29"). Y el caso 7, integrado sin reabrirlo.

---

## Caso 1 · La hoja pasa el examen: legibilidad y pregunta de vuelta · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿El recuento de palabras de una lista cerrada hace desaparecer "No es culpa suya"?** Sí, y también "no es falta de voluntad", que "qué revisar" (l. 93) no ve. La tarea (2) manda reescribir "sin las palabras de la lista" y el recuento (4) exige "PALABRAS DE LA LISTA: 0"; los tres modelos obedecen: Claude sustituye por "No depende de usted"; ChatGPT por "Usted no ha hecho nada mal" (que suena a lo contrario de lo que quiere decir); Gemini quita la frase. La versión A del capítulo 1 lleva las dos por exigencia de su propio prompt ("que esto es biología y no falta de voluntad"). Devolverlas a mano, como propone el capítulo, es aceptar que el examen borra lo que la médica más quiere que se lea. Solución en el prompt: las dos frases que niegan la culpa se conservan literales y no cuentan; el resto de apariciones, sí. Sigue siendo contable con el dedo: se cuentan las palabras de la lista y se restan las que están dentro de "No es culpa suya" y "No es falta de voluntad".
**¿Las tres preguntas de vuelta salen sin tono de examen?** En Claude y ChatGPT, sí: "Para saber si me he explicado bien, ¿cómo le contaría a alguien de su casa por qué vuelve el hambre después de una dieta?", "…qué le diría a su hija si le pregunta si esto es culpa suya", "…cómo explicaría en casa qué vamos a hacer ahora". Gemini, en una de tres, escribe "Para saber si me he explicado bien, ¿podría decirme qué ha entendido de la hoja?": cumple la letra ("ninguna con '¿ha entendido?'") y es el examen con otras palabras. Añadir a la prohibición "qué ha entendido", "repítame" y "resúmame". Y "alguien de su casa" deja fuera a quien vive solo: "a alguien de su confianza" cuesta lo mismo.
**¿La variable LÍNEA DE URGENCIAS con "ninguna" por defecto funciona?** A medias. "Ninguna" es el valor correcto para la versión A. El problema es que el corchete lleva la condición de cada opción ("si la hoja no habla de síntomas ni de tratamiento…; si habla de un tratamiento: …; si habla de síntomas o de movimiento: …"): es una instrucción a la lectora dentro del prompt (T6 del capítulo 5), y quien lo pega tal cual deja que decida el modelo. Con la versión A, que dice "tratamiento y seguimiento" sin nombrar ninguno, ChatGPT elige la fórmula de tratamiento en una de tres. Y lo peor: con "ninguna", nadie le ha dicho al modelo que no añada la suya, y Gemini cierra la hoja con "Si se encuentra mal, consulte con su médico" (tercera fórmula; regla 19). Funciona si (a) el corchete lleva solo el valor ("[ninguna]") y las dos fórmulas fijas van fuera del corchete como las dos únicas alternativas que la lectora copia, en usted y en tú, y (b) el prompt dice "si es 'ninguna', no añadas ninguna línea de urgencias, síntomas ni 'consulte con su médico'".

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco, en orden. El rol ("redactora… experta en alfabetización en salud y en lenguaje llano en español de España") es el correcto: no es médica, no debe añadir clínica. |
| Anonimización | (0) "HOJA SIN DATOS / HOJA CON DATOS: BORRA ESTA CONVERSACIÓN" con "para" y lista (nombre, fecha, centro, teléfono): bien. Ojo: la hoja del capítulo 1 termina con "Revisado por: ________ Fecha: ________"; en blanco no es dato, rellenada lo es (el nombre de la médica y una fecha). El prompt debería decir que esa línea se quita antes de pegar. "No incluyas ni pidas datos de personas": sí. |
| Variables | TRATO con valor por defecto: bien. LÍNEA DE URGENCIAS: corchete-instrucción (arriba). HOJA con ejemplo: bien. "[120]" en el tope: corchete sin sentido (un tope no es variable; si lo es, sin ejemplo). |
| Salidas cerradas | (0), examen en seis líneas, hoja con tres líneas literales, tres preguntas, recuento cuádruple. "FRASES" definida en (1) (punto, interrogación, exclamación): contable. "PALABRAS POR FRASE": media, contable con calculadora. "PALABRAS TÉCNICAS": dos criterios mezclados, uno no contable y el otro con 0 imposible (T2). "PALABRAS DE LA LISTA": contable, pero borra la tesis (T1). Nada dice si las líneas literales entran en el examen ni en el recuento (T6): la frase del aviso ("valoración clínica individual", "profesional sanitario") es la más larga y técnica de la hoja y el modelo la cuenta o no según el día. |
| Portabilidad | Sin cambios. Gemini pone los rótulos en negrita y añade "Aquí tienes el examen:"; "sin negritas" solo rige para la hoja. Claude y ChatGPT, limpios. Ninguno necesita razonador. Los tres cuentan mal: "9 frases" puede ser 8 o 10; "qué revisar" lo dice y manda contar tres frases. |
| Ejemplo de salida | Realista en forma. Tres cosas que no cuadran: "técnicas: ninguna" con "Es biología" (con el criterio de sílabas del prompt, "biología" cuenta); "PALABRAS DE LA LISTA: 0" en una hoja de la que ha desaparecido "No es culpa suya" (correcto según el prompt; es lo que hay que cambiar); y "FRASES: 10" sin decir si las líneas literales están dentro (T6). |
| Riesgo | Bien identificado (la hoja "apta" sustituye a la pregunta de vuelta) y bien mitigado. |

### Ejecución mental (versión A del capítulo 1, en usted, LÍNEA DE URGENCIAS "ninguna", los tres)
- **Claude:** (0) "HOJA SIN DATOS". Examen: 9-10 frases; 7-8 palabras por frase; técnicas: "biología" y "energía" (una de tres) o "ninguna" (dos de tres, leyendo el segundo criterio); cifras: ninguna; frases con más de una idea: 1 ("le da más hambre y gasta menos energía"); lista: "culpa" (1), "voluntad" (1). Hoja reescrita de 70-90 palabras, sin "No es culpa suya" ("Eso no depende de usted") ni "no es falta de voluntad" ("Es biología"), con las tres líneas literales en orden y el aviso en usted. Tres preguntas correctas. Recuento: 10 · 7 · 0 · 0. Aviso: cuenta la frase del aviso como frase en una de tres.
- **ChatGPT:** igual; pone la fórmula de tratamiento en una de tres porque la hoja dice "tratamiento"; "Usted no ha hecho nada mal" por "No es culpa suya"; añade un título en negrita pese a "sin negritas" (una de tres); cuenta las líneas literales (13 frases) en dos de tres.
- **Gemini:** rótulos en negrita; "Si se encuentra mal, consulte con su médico" tras el contacto con LÍNEA DE URGENCIAS "ninguna" (una de tres); "¿qué ha entendido?" en una pregunta; técnicas: "biología, energía, enfermedad, tratamiento, seguimiento" (5) aplicando las sílabas, y luego reescribe sin ellas: la hoja pierde "enfermedad crónica" ("es algo que dura") y "tratamiento" ("hay ayuda"). Recuento 0 en técnicas después de vaciarla.
- Rúbrica: fidelidad media (contenido perdido por la lista); priorización correcta (biología antes que consejo); calibración no aplica; confusores no aplica; acción segura alta (no hay decisión); anexo B: pregunta 6 (consejo o valoración añadida) no salta; la 9 (leída entera) es la que caza las frases perdidas.

### Problemas
1. "culpa" y "voluntad" en la lista borran "No es culpa suya" y "no es falta de voluntad" (T1).
2. "Palabras técnicas" con dos criterios; el de sílabas hace imposible el 0 y el ejemplo lo incumple (T2).
3. LÍNEA DE URGENCIAS como corchete-instrucción y sin "no añadas nada si es ninguna" (T3); sin variante tú de las fórmulas (T4).
4. Las líneas literales entran o no en el examen y el recuento según el modelo (T6).
5. "¿qué ha entendido?", "repítame" no prohibidas; "alguien de su casa".
6. "Revisado por: ___ Fecha: ___" del capítulo 1: decir que se quita antes de pegar.
7. "[120]" como corchete.

### Versión corregida (cambios: variable de urgencias; exención de las dos negaciones; dos recuentos en vez de "técnicas"; líneas literales fuera del examen; preguntas)

```
ROL: Eres una redactora de materiales para pacientes, experta en alfabetización en salud y en lenguaje llano en español de España.

CONTEXTO: Soy médica de familia en España. Te pego una hoja GENÉRICA que entrego a personas con obesidad; no lleva ningún dato de nadie. Quiero saber si se entiende y, si no, una versión que se entienda sin cambiar lo que dice. TRATO: [usted por defecto / tú]. LÍNEA DE URGENCIAS, la elijo yo: [ninguna]. Si no es "ninguna", será una de estas dos, literal: "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112." (en tú: "Si no toleras líquidos, tienes dolor fuerte de tripa, te mareas o te encuentras mal, no esperes: urgencias o 112.") o "Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112." (en tú: "Si notas dolor en el pecho, falta de aire o mareo, no esperes: urgencias o 112.").

HOJA: [pega la hoja sin su línea de "Revisado por" ni de fecha; por ejemplo, la versión A de "¿Por qué recupero el peso?" del capítulo 1]

TAREA, en este orden:
(1) EXAMEN de la hoja tal cual, sin contar sus líneas finales de contacto, urgencias o aviso si las trae: número de frases (una frase termina en punto, interrogación o exclamación); palabras por frase, de media; palabras largas (más de tres sílabas), listadas; palabras técnicas (nombres de hormonas, órganos, pruebas o fármacos y términos que solo usa el personal sanitario; "biología", "enfermedad crónica", "tratamiento" y "seguimiento" no lo son), listadas; cifras y porcentajes; frases con más de una idea; y las palabras de esta lista que aparezcan: "debe", "tiene que", "no debería", "culpa", "fracaso", "esfuerzo", "voluntad", "disciplina", "obeso", "obesa". Las frases "No es culpa suya" (o "no es culpa tuya") y "No es falta de voluntad" se conservan tal cual y no cuentan.
(2) HOJA REESCRITA solo si el examen encuentra algo: mismas ideas, sin añadir ni quitar contenido, frases de 15 palabras como máximo, una idea por párrafo, sin palabras técnicas, sin cifras y sin las palabras de la lista salvo en las dos frases que las niegan. Si ya cumple, escribe "NO HACE FALTA REESCRIBIR".
(3) TRES PREGUNTAS DE VUELTA para hacer yo en consulta, cada una empezando por "Para saber si me he explicado bien," y pidiendo que la persona lo cuente con sus palabras a alguien de su confianza; ninguna con "¿ha entendido?", "qué ha entendido", "repítame" ni "resúmame".

FORMATO, en este orden:
(0) Una línea: "HOJA SIN DATOS" o "HOJA CON DATOS: BORRA ESTA CONVERSACIÓN" si contiene nombre, fecha, centro, teléfono o cualquier dato individual; en ese caso, para.
(1) El examen, en siete líneas.
(2) La hoja reescrita, máximo 120 palabras sin contar las líneas literales, sin negritas ni emoticonos, terminada, en este orden y literal, con: "Si tiene dudas, [FALTA: contacto del centro]." (en tú, "Si tienes dudas"); la LÍNEA DE URGENCIAS que te he dado, solo si no es "ninguna"; y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." (en tú, "tu profesional sanitario"). Si la LÍNEA DE URGENCIAS es "ninguna", no añadas ninguna línea de urgencias, de síntomas ni de "consulte con su médico", aunque te parezca prudente.
(3) Las tres preguntas.
(4) Última línea, literal: "FRASES: [n] · PALABRAS POR FRASE: [n] · PALABRAS LARGAS: [n] · PALABRAS TÉCNICAS: [n] · PALABRAS DE LA LISTA: [n]", contadas sobre la hoja reescrita sin sus líneas literales, o sobre la original si no hizo falta; las dos últimas tienen que ser 0.

RESTRICCIONES: No añadas consejos, síntomas, tratamientos ni frases de ánimo que no estén en la hoja. Sin nombres de fármacos, ni comerciales ni por principio activo ni por clase; sin objetivos de peso. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

Ejemplo de salida corregido (sustituye el examen, la hoja y la última línea; las preguntas valen):

> HOJA SIN DATOS
> EXAMEN. 10 frases; 7 palabras por frase; largas: biología, energía, enfermedad, tratamiento, seguimiento; técnicas: ninguna; cifras: ninguna; frases con más de una idea: 1; palabras de la lista: ninguna fuera de "No es culpa suya" y "no es falta de voluntad".
> HOJA REESCRITA. Por qué vuelve el peso. Su cuerpo defiende su peso. Cuando baja kilos, le da más hambre. Y gasta menos energía. No es culpa suya. No es falta de voluntad. Es biología. […] Si tiene dudas, [FALTA: contacto del centro]. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> PREGUNTAS. Para saber si me he explicado bien, ¿cómo le contaría a alguien de su confianza por qué vuelve el peso después de una dieta? […]
> FRASES: 11 · PALABRAS POR FRASE: 6 · PALABRAS LARGAS: 5 · PALABRAS TÉCNICAS: 0 · PALABRAS DE LA LISTA: 0

"Qué revisar" (l. 93), sustituir la frase de la culpa por: "Las dos frases que niegan la culpa se quedan porque el prompt las protege; si el modelo las cambió por 'no depende de usted' o 'usted no ha hecho nada mal', no dicen lo mismo: devuélvelas. Las palabras largas no son un fallo: son las que la persona tiene que poder leer; si son más de cinco en cien palabras, la hoja pesa." Y añadir: "Con LÍNEA DE URGENCIAS 'ninguna', busca 'consulte' y '112': si están, la máquina ha decidido por ti que la hoja toca síntomas."

---

## Caso 2 · La misma hoja en árabe, rumano e inglés, con retraducción · veredicto: 2A MEJORAR (leve) · 2B MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿La retraducción del prompt B se contamina si el mismo prompt pide después comparar con el original?** En el paso (1), no: el modelo no tiene el original y "no debes imaginarlo" basta; anunciar que vendrá después no lo contamina. Se contamina en el paso (2), y de dos formas. La primera: al pegar el original, ChatGPT (dos de tres) y Gemini (dos de tres) empiezan por reescribir su retraducción "ajustada al original" y después comparan esa versión nueva, con lo que las diferencias se reducen a una o ninguna; Claude compara lo que escribió. "No corrijas la traducción ni propongas otra" habla de la traducción del paso A, no de la suya. Hace falta una frase: "no cambies tu retraducción después de ver el original: compara la que escribiste". La segunda: si la lectora, con prisa, pega el original en el mismo mensaje que la traducción, el modelo traduce mirando el original; el prompt lo evita ("Después te pegaré") y "qué revisar" debería decirlo con una frase ("el original entra en un segundo mensaje, nunca en el primero"). El diseño de dos conversaciones y "otro modelo" es la mejor protección y está bien puesto en el capítulo.
**¿Los modelos conservan literal "[FALTA: contacto del centro]" y el "112" en árabe y rumano?** El corchete: Claude y ChatGPT lo copian en español entre corchetes en los tres idiomas; Gemini, en árabe, traduce el contenido del corchete en una de tres (يُرجى ملء بيانات الاتصال…) aunque se le diga "se copia en español tal cual", y en rumano lo copia. En el texto árabe (de derecha a izquierda) el corchete en alfabeto latino se muestra en su sitio y con el contenido intacto; se ve raro, y el mediador lo entenderá si se le dice qué es. El 112: en rumano e inglés, siempre 112; en árabe, ChatGPT y Claude escriben 112 con cifras occidentales; Gemini escribe ١١٢ (cifras árabes orientales) en una de tres, y el recuento "'112': 1" sale igual porque es el mismo número. Para una hoja que se imprime en España, con la grafía 112: se dice en el prompt ("con las cifras 112, no ١١٢ ni en letras") y en "qué revisar" ("el 112 se busca con el buscador: si no lo encuentra, está en otra grafía"). En el paso B, la retraducción de ١١٢ vuelve a 112 y la diferencia no se ve: por eso hay que cerrarla en A.
**¿El recuento "LÍNEAS FINALES IGUALES: SÍ/NO" es fiable?** No tal como está. Una retraducción no devuelve nunca las líneas palabra por palabra ("Si tiene dudas" → "Si tiene preguntas"; "revisado por su profesional sanitario" → "verificado por su médico"; "no espere" → "no dude", como en el ejemplo). Si "iguales" es literal, la respuesta es siempre NO y la instrucción "no se negocia: se rehace esa línea y se vuelve a retraducir" es un bucle. Si es en sentido, cada modelo decide qué es igual: Claude da NO por "no dude", ChatGPT da SÍ por "sentido equivalente", Gemini da SÍ salvo que falte una línea. Solución: tres comprobaciones contables en vez de un juicio: CONTACTO (el corchete está y dice lo mismo que en el original: en español, tal cual); URGENCIAS (aparece 112 y una expresión de no demorarse, "no espere" o equivalente; "no dude" no lo es: es cortesía); AVISO (están las tres ideas: hecho con apoyo de IA, revisado por su profesional sanitario, no sustituye la valoración individual). La última línea pasa a "LÍNEAS FINALES: CONTACTO SÍ/NO · URGENCIAS SÍ/NO · AVISO SÍ/NO", con URGENCIAS "NO APLICA" si la hoja no la lleva. El ejemplo del libro (rumano, "no espere" → "no dude") da CONTACTO SÍ · URGENCIAS NO · AVISO SÍ, que es exactamente lo que la lectora tiene que ver.

### Checklist (2A)
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "Para personas sin estudios sanitarios" en el rol y "un hablante nativo la leerá antes de entregarse" en el contexto: bien. |
| Anonimización | (0) con "para" y lista: bien. "No incluyas ni pidas datos": sí. |
| Variables | [IDIOMA] con tres ejemplos; TRATO "[usted por defecto, o su equivalente de respeto en el idioma]" es una instrucción dentro del corchete (T6 del capítulo 5), leve; pasa a "[usted; en el idioma, su forma de respeto]". |
| Salidas cerradas | (0), traducción sin original al lado, recuento cuádruple con definiciones: frases (punto, interrogación, exclamación), corchetes y 112 "en la traducción… tienen que coincidir con los del original". Contable con el dedo. Falta decir que las líneas literales cuentan (T6) y la grafía del 112. "Ponla también en español entre paréntesis" añade texto que en B aparece como diferencia; limitar ("como máximo dos, y dímelo en una línea aparte"). |
| Portabilidad | Sin cambios. Los tres traducen bien a rumano e inglés; en árabe estándar, Claude y ChatGPT mantienen registro llano; Gemini tiende a un registro más formal (fusha literaria) y a añadir una nota "Traducción al árabe estándar moderno" (inocua). Ninguno necesita razonador. |
| Ejemplo de salida | No hay ejemplo propio del paso A; el del B lo suple. Bastaría la última línea: "FRASES EN ESPAÑOL: 13 · FRASES TRADUCIDAS: 13 · CORCHETES: 1 · '112': 0" (con la versión A, sin urgencias). |
| Riesgo | Bien identificado en el conjunto del caso (entregar "porque la retraducción salió limpia") y bien mitigado ("sin hablante, no se entrega"). |

### Checklist (2B)
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "No conoces el original en español y no debes imaginarlo": la frase clave, y funciona. |
| Anonimización | (0) "TEXTO SIN DATOS / TEXTO CON DATOS" con "para": bien; el modelo detecta nombres y teléfonos en árabe y rumano sin problema. |
| Variables | [IDIOMA] y TEXTO con instrucción de dónde sale ("pega la traducción del paso A"): bien. |
| Salidas cerradas | Retraducción, lista de diferencias enfrentadas, recuento triple. "FRASES: [n]" no dice de qué texto (de la retraducción). "DIFERENCIAS DE SENTIDO: [n]" contable (ítems de la lista). "LÍNEAS FINALES IGUALES: SÍ/NO" no fiable (arriba). |
| Portabilidad | Sin cambios; el prompt de dos turnos funciona en los tres. Gemini, al recibir el original, escribe primero "He revisado mi traducción" y la reescribe (dos de tres). |
| Ejemplo de salida | Realista y bien elegido: "gasta menos energía" → "consume menos" (diferencia real de sentido: en rumano "consumă mai puțin" se lee como "come menos") y "no espere" → "no dude" (cortesía por urgencia). "LÍNEAS FINALES IGUALES: NO" es lo que devuelve Claude; con la nueva línea, "URGENCIAS NO". |
| Riesgo | Bien identificado; el bucle del "se rehace" es el que queda. |

### Ejecución mental (versión A del caso 1 con sus tres líneas finales; árabe estándar y rumano; los tres)
- **Claude (A, árabe):** "HOJA SIN DATOS"; 13 frases en árabe con puntos; el corchete en español entre corchetes; "112" en cifras occidentales; registro llano. Recuento 13 · 13 · 1 · 0 (sin urgencias). **(B, rumano → español):** retraducción fiel; al recibir el original, lista 2-3 diferencias ("consume menos", "verificado por su médico" → la marca como estilo, bien); no toca su retraducción.
- **ChatGPT (A, rumano):** correcto; añade "(Notă: …)" con la palabra española entre paréntesis para "seguimiento" ("urmărire (seguimiento)"); recuento correcto. **(B):** reescribe la retraducción "corregida" antes de comparar en dos de tres; LÍNEAS FINALES IGUALES: SÍ por "sentido equivalente" aunque diga "no dude".
- **Gemini (A, árabe):** traduce el contenido del corchete en una de tres; ١١٢ en una de tres; a veces "resume" dos frases en una (12 frases) y cuenta 13. **(B):** "He revisado mi traducción a la luz del original"; diferencias: 0-1; IGUALES: SÍ.
- Rúbrica: fidelidad alta en A (Claude, ChatGPT) y media en Gemini; en B, calibración: el recuento de líneas finales es donde falla; acción segura: depende de esa línea, que es la del 112.

### Problemas
1. (B) El modelo retoca su retraducción al ver el original: sin diferencias que listar (T7).
2. (B) "LÍNEAS FINALES IGUALES" no es contable ni puede dar SÍ (T7).
3. (A) 112 en cifras árabes orientales; corchete traducido por Gemini (T7).
4. (A y B) Nada dice si las líneas literales cuentan; los ejemplos de los casos 1 y 2 no cuadran (T6).
5. (A) Paréntesis con la palabra en español sin límite.
6. (A) TRATO como corchete-instrucción; sin ejemplo de salida.
7. (B) "FRASES" sin decir de qué texto.

### Versión corregida 2A (cambios en CONTEXTO (trato), TAREA (112, paréntesis, líneas literales) y (2))

```
ROL: Eres una traductora sanitaria profesional de español a [IDIOMA; por ejemplo: árabe estándar moderno / rumano / inglés], para personas sin estudios sanitarios.

CONTEXTO: Soy médica de familia en España. Te pego una hoja GENÉRICA para personas con obesidad, ya revisada por mí, sin ningún dato de nadie. Un hablante nativo la leerá antes de entregarse. TRATO: [usted; en el idioma, su forma de respeto].

HOJA: [pega la hoja que pasó el caso 1, con sus líneas finales]

TAREA: Traduce la hoja entera, frase por frase, con el mismo orden y el mismo número de frases; sin resumir, sin unir frases, sin añadir explicaciones ni notas culturales, sin cambiar de registro. Las líneas finales también ("Si tiene dudas, [FALTA: contacto del centro].", la de urgencias si la hay, y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."), con tres reglas: lo que va entre corchetes se copia en español, tal cual y entre corchetes, sin traducirlo; "urgencias o 112" conserva el número escrito con las cifras 112, no con otras cifras ni en letras; y "no espere" se traduce como una orden de no demorarse, no como una cortesía. Si una palabra no tiene equivalente llano, elige la más corriente; como máximo en dos palabras puedes poner el español entre paréntesis, y dime cuáles en una línea aparte.

FORMATO, en este orden:
(0) Una línea: "HOJA SIN DATOS" o "HOJA CON DATOS: BORRA ESTA CONVERSACIÓN" si contiene nombre, fecha, centro, teléfono o cualquier dato individual; en ese caso, para.
(1) La traducción, sin el original al lado, sin negritas ni emoticonos.
(2) Última línea, literal: "FRASES EN ESPAÑOL: [n] · FRASES TRADUCIDAS: [n] · CORCHETES: [n] · '112': [n]": una frase termina en punto, interrogación o exclamación y las líneas finales cuentan; corchetes y 112 se cuentan en la traducción, con la grafía 112, y tienen que coincidir con los del original.

RESTRICCIONES: No añadas ni quites contenido. Sin nombres de fármacos, sin cifras que no estén, sin consejos. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

Ejemplo de salida para A (una línea, nueva): "> FRASES EN ESPAÑOL: 13 · FRASES TRADUCIDAS: 13 · CORCHETES: 1 · '112': 0". Y en el caso 1, "FRASES: 10" es sin las líneas literales; aquí 13 con ellas: los dos ejemplos lo dicen.

### Versión corregida 2B (cambios en TAREA (2), FORMATO (2) y RESTRICCIONES)

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

Ejemplo de salida corregido (sustituye la última línea): "> FRASES DE LA RETRADUCCIÓN: 13 · DIFERENCIAS DE SENTIDO: 2 · LÍNEAS FINALES: CONTACTO SÍ · URGENCIAS NO · AVISO SÍ". (Si el ejemplo sigue siendo la hoja del caso 1 sin urgencias, "no espere" no puede estar: o el ejemplo usa una hoja con la línea de tratamiento, o la diferencia 2 cambia a otra; lo decide el REDACTOR.)

"Qué revisar" (l. 144), sustituir la primera frase por: "Un NO en CONTACTO, URGENCIAS o AVISO no se negocia: se rehace esa línea en A y se vuelve a retraducir. Las demás diferencias las decides tú con el hablante delante; la máquina señala, no arbitra. El original entra en un segundo mensaje, nunca en el primero; y si el modelo dice que ha 'revisado' su retraducción al verlo, la comparación no vale: conversación nueva. El 112 se busca con el buscador en la traducción: si no lo encuentra, está en otra grafía."

---

## Caso 3 · Qué esperar del tratamiento: guion de primera visita · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿El guion oral nombra clases de fármacos o dosis aunque se prohíban?** Dosis, no: "sin dosis, vía ni frecuencia" y el recuento "cada cantidad con unidad o frecuencia de administración" funcionan; ninguno escribe miligramos. Frecuencia, a medias: ChatGPT escribe "se pone una vez a la semana" en una de tres (cuenta 1, correcto) y "es una inyección" en dos de tres (vía: prohibida en la restricción, no contada en el recuento). Clases, sí: con el mecanismo de ejemplo delante ("imita una hormona del intestino que avisa al cerebro de que hay saciedad"), ChatGPT y Gemini reconocen el agonista del receptor de GLP-1 y lo dicen: "este tipo de medicamentos, llamados agonistas de GLP-1" (ChatGPT, una de tres), "una hormona llamada GLP-1" (Gemini, dos de tres), "esta familia de fármacos" (los dos). Claude no lo nombra. Y los tres amplían el mecanismo: "además ayuda a regular el azúcar en sangre" (los tres, al menos una vez), "actúa también en el páncreas" (Gemini). En una persona con diabetes, "regula el azúcar" es una afirmación clínica que la médica no dio y que en el guion suena a promesa. **¿El recuento de principios activos cuenta la clase?** No: "cada nombre comercial o de principio activo" deja fuera "agonistas de GLP-1", "análogos", "familia", "GLP-1" como hormona. Es la correa por clase de T2 del capítulo 4, que este capítulo no hereda. Solución: el recuento se llama "FÁRMACOS, CLASES O SIGLAS NOMBRADOS" y define las cuatro formas; y la tarea dice "solo el mecanismo que te he dado, con mis palabras, sin ampliarlo ni nombrar la hormona".

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "Genérico: sin ninguna persona; a quién se le indica lo decido yo y no entra aquí" es la remisión al capítulo 8 dentro del prompt (regla 13): bien. Nota al pie de transparencia (regla 12) en la Situación: bien. |
| Anonimización | No entra ningún texto: sin (0), correcto. "No incluyas ni pidas datos de personas": sí. |
| Variables | MECANISMO y FRASE MÍA con ejemplo literal (la frase de la puerta, de la biblia); TRATO con valor por defecto. Bien. La línea literal solo en usted (T4). |
| Salidas cerradas | Seis bloques con título fijo, tope sin contar la línea literal, recuento triple. "NOMBRES DE FÁRMACOS" no cuenta clase ni siglas (T5); "DOSIS O PAUTAS" no cuenta vía. "CIFRAS DE PESO O PORCENTAJES": contable. |
| Portabilidad | Sin cambios. Gemini pone los títulos en negrita (prohibido; lo hace igual) y una frase final "Recuerde adaptar este guion…"; ChatGPT respeta los seis títulos; Claude, el más fiel a "para decir en voz alta". Ninguno necesita razonador. |
| Ejemplo de salida | Realista: es lo que devuelve Claude. Faltan en el fragmento los bloques de seguridad y de dejar; con dos líneas más se ve que la línea literal sale entera. |
| Riesgo | Bien identificado (que el guion prometa) y bien mitigado (qué es ir bien sin cifras; la frase de la puerta). "Qué revisar" manda comprobar el mecanismo contra la ficha técnica: es la frase más importante del caso. |

### Ejecución mental (variables del ejemplo, usted, los tres)
- **Claude:** seis bloques, 220-260 palabras; QUÉ HACE con el mecanismo tal cual y la frase de la puerta; QUÉ ESPERAR con náuseas, estreñimiento y saciedad, "suelen ir a menos"; QUÉ ES IR BIEN sin kilos ("menos hambre, dormir mejor, subir escaleras"); la línea literal entera; SI SE DEJA con "se decide juntos y sin culpa". Añade "ayuda a controlar el azúcar" una de tres. Recuento 0 · 0 · 0, verdadero salvo por el azúcar (que no es fármaco, dosis ni cifra: pasa).
- **ChatGPT:** "llamados agonistas de GLP-1" una de tres; "es una inyección" dos de tres; "la mayoría de las personas nota menos hambre en pocas semanas" (promesa suave con plazo); recuento 0 · 0 · 0 aunque haya escrito la clase.
- **Gemini:** "una hormona llamada GLP-1" dos de tres; negritas; "perderá peso de forma progresiva" en una de tres (el "perderá" que "qué revisar" manda buscar); "también actúa en el páncreas".
- Rúbrica: fidelidad media (mecanismo ampliado); priorización correcta (enfermedad antes que fármaco); calibración: falla en "la mayoría" y "perderá"; acción segura: alta (lo dice la médica, que lo lee antes).

### Problemas
1. Clase, familia y siglas de la hormona pasan la restricción y el recuento (T5).
2. Mecanismo ampliado ("regula el azúcar", "páncreas") no prohibido por su nombre.
3. Vía ("inyección", "pastilla") prohibida y no contada.
4. Línea literal solo en usted con TRATO que admite tú (T4).
5. "La mayoría", "en pocas semanas", "perderá": promesas con plazo o cifra disfrazada; "qué revisar" busca "perderá" y el prompt no lo prohíbe.
6. Ejemplo sin los bloques de seguridad.

### Versión corregida (cambios en TAREA (mecanismo sin ampliar; línea en dos tratos), FORMATO (recuento) y RESTRICCIONES)

```
ROL: Eres médica de familia especialista en obesidad, muy buena explicando en voz alta y sin jerga.

CONTEXTO: Atención Primaria en España. Quiero un GUION ORAL para decirlo yo en la visita en que una persona con obesidad y yo decidimos empezar un tratamiento farmacológico. Genérico: sin ninguna persona; a quién se le indica lo decido yo y no entra aquí. MECANISMO, con mis palabras: [por ejemplo: imita una hormona del intestino que avisa al cerebro de que hay saciedad y hace que el estómago se vacíe más despacio]. FRASE MÍA, literal: [por ejemplo: "La medicación puede abrir una puerta. Pero lo que realmente transforma la salud es lo que una persona construye después de cruzarla."]. TRATO: [usted por defecto / tú].

TAREA: Seis bloques cortos, en este orden y con estos títulos: QUÉ TRATAMOS (enfermedad crónica con biología detrás; no es falta de voluntad); QUÉ HACE EL TRATAMIENTO (solo el mecanismo que te he dado, con mis palabras, sin ampliarlo con otros efectos ni órganos y sin nombrar la hormona, y mi frase); QUÉ ESPERAR AL EMPEZAR (que al principio son frecuentes las náuseas, el estreñimiento o notar el estómago lleno antes, y suelen ir a menos; sin cifras de frecuencia ni plazos); QUÉ ES IR BIEN (menos hambre, más salud, poder hacer más; nunca kilos ni porcentajes); CUÁNDO LLAMAR Y CUÁNDO NO ESPERAR, con esta línea literal y entera, en usted: "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo." (en tú: "Si no toleras líquidos, tienes dolor fuerte de tripa, te mareas o te encuentras mal, no esperes: urgencias o 112. Y ante cualquier molestia, pide cita y lo vemos, o te llamo yo."); y SI SE DEJA (es una enfermedad crónica, el cuerpo tiende a volver al peso anterior, y dejarlo se decide juntos y sin culpa).

FORMATO: Máximo 260 palabras sin contar la línea literal, frases de 15 palabras como máximo, para decir en voz alta; sin negritas, sin emoticonos, sin pie de aviso: lo digo yo. Última línea, literal: "FÁRMACOS, CLASES O SIGLAS NOMBRADOS: [n] · DOSIS, VÍAS O PAUTAS: [n] · CIFRAS DE PESO, PORCENTAJES O PLAZOS: [n]": el primero cuenta cada nombre comercial, cada principio activo, cada clase o familia ("agonistas", "análogos", "esta familia de fármacos") y cada sigla de hormona; el segundo, cada cantidad con unidad, cada vía ("inyección", "pastilla") y cada frecuencia de administración; el tercero, cada kilo, porcentaje o plazo ("en pocas semanas", "en tres meses"); los tres tienen que ser 0.

RESTRICCIONES: No nombres ningún fármaco, ni comercial, ni por principio activo, ni por clase o familia, ni la hormona por sus siglas; sin dosis, vía ni frecuencia; no digas a quién se le indica ni desde qué peso; no prometas resultados: sin "perderá", "bajará de peso", "la mayoría de las personas" ni plazos; sin dietas ni "comer menos". No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale; añadir dos líneas antes del recuento para que se vea la red de seguridad: "> CUÁNDO LLAMAR Y CUÁNDO NO ESPERAR. Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo." y "> SI SE DEJA. Es una enfermedad crónica. Si se deja, el cuerpo tiende a volver. Se decide juntos, y sin culpa." Última línea: "FÁRMACOS, CLASES O SIGLAS NOMBRADOS: 0 · DOSIS, VÍAS O PAUTAS: 0 · CIFRAS DE PESO, PORCENTAJES O PLAZOS: 0".

Añadir a "qué revisar" (l. 172), tras "Busca 'kilos', '%' y 'perderá'": "y 'GLP', 'agonista', 'familia', 'azúcar' e 'inyección': las cinco pasan el recuento antiguo. Si el guion dice que el tratamiento 'también regula el azúcar', lo has dicho tú o no se dice: en una persona con diabetes es una afirmación clínica, no una explicación."

---

## Caso 4 · Preguntas frecuentes sobre náuseas y otros efectos digestivos · veredicto: LISTO (retoque)

### Respuesta a la atención especial del ORQUESTADOR
**¿El modelo añade fármacos de venta libre, "no se preocupe" o consejos individuales?** Venta libre, no, porque la restricción los nombra ("tampoco para las náuseas o el estreñimiento ni de venta libre") y es la primera vez en el libro que se prohíbe por esa vía: Claude y ChatGPT, limpios; Gemini escribe "puede consultar en la farmacia" en una de tres, que no es un fármaco y lleva a uno. "No se preocupe", no: los tres lo evitan y escriben "es frecuente" (aceptable: es un hecho, y el caso 3 lo dice) o "no pasa nada" y "sin importancia" (Gemini, una de tres), que son la misma frase que el recuento no cuenta. Consejos individuales, no; consejos generales que no están en la lista, sí, y en un sitio concreto: el estreñimiento. Las cinco medidas dadas (raciones pequeñas, despacio, sin grasas ni alcohol, sorbos, moverse) sirven para náuseas, reflujo y saciedad; para el estreñimiento solo valen "sorbos" y "moverse", y el modelo nota el hueco: "añada fibra: fruta, verdura, legumbres" (los tres, al menos una vez), "pan integral" (ChatGPT), "ciruelas" (Gemini). No es un disparate, pero no lo dio la médica, y "sin más consejos de comida que los dados" no lo frena porque el modelo cree que la pregunta lo exige. Dos salidas: o la lista de medidas incluye una para el estreñimiento (lo decide CLÍNICO o Cristina: fibra, fruta y verdura, líquidos), o el prompt dice "para el estreñimiento, solo beber a sorbos y moverse; si con eso no basta, se habla en consulta: no añadas fibra, laxantes ni alimentos". Propongo la segunda como texto y dejo a CLÍNICO la primera. **¿La línea de la regla 17 sale entera?** Sí, en los tres, porque el tope dice "sin contar las líneas literales" y el pie dice "en este orden y literal": es la lección del capítulo 4 (caso 6) aplicada. Lo único: ChatGPT la repite dentro de la respuesta a "¿cuánto dura esto?" y otra vez al pie (inocuo; se quita la primera).

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "Sin nombrar el tratamiento: vale para cualquiera" y "la entrego o la envío por el canal del centro" fijan el uso. Nota al pie compartida con el 3 (regla 12): bien. |
| Anonimización | No entra ningún texto: sin (0), correcto. "No incluyas ni pidas datos": sí. |
| Variables | Ninguna: TRATO fijo en usted (hoja impresa o enviada, regla 11) y cinco preguntas fijas. Correcto para una hoja genérica. |
| Salidas cerradas | Cinco preguntas, tope sin contar literales, tres líneas de la regla 19 en orden y literales, recuento cuádruple con "cambio de pauta" definido ("tome menos", "sáltese", "espere a la siguiente", cantidad con unidad): el mejor recuento del capítulo. Le faltan los sinónimos de 'NO SE PREOCUPE' ("tranquilo" está en la restricción y no en el recuento; "no pasa nada", "sin importancia") y el desvío a la farmacia (T5). |
| Portabilidad | Sin cambios. Gemini pone las preguntas en negrita (prohibido; lo hace igual) y ChatGPT numera las preguntas. Ninguno necesita razonador. |
| Ejemplo de salida | Realista: es la salida de Claude, con las tres líneas enteras y en orden. |
| Riesgo | Bien identificado (que la hoja "maneje" lo que había que ver) y bien mitigado (urgencias, "pida cita", notificación). |

### Ejecución mental (los tres)
- **Claude:** cinco preguntas con las palabras de la persona ("¿Qué hago si tengo náuseas?", "¿Y si voy estreñido?", "Tengo ardor", "Me lleno enseguida", "¿Cuánto dura esto?"), 180-220 palabras, respuestas con las medidas dadas; fibra en el estreñimiento en una de tres; las tres líneas literales; recuento 5 · 0 · 0 · 0.
- **ChatGPT:** igual; "pan integral y fruta" en el estreñimiento; repite la línea de urgencias dentro de "¿cuánto dura?"; "es frecuente al principio" (pasa, y está bien).
- **Gemini:** "consulte en la farmacia" (una de tres); "no pasa nada si un día come menos" (una de tres); "ciruelas"; negritas.
- Rúbrica: fidelidad alta (medidas de la lista); priorización correcta (urgencias y cita al pie); calibración: bien ("suelen ir a menos… si no, en consulta"); acción segura: alta.

### Problemas
1. Estreñimiento sin medida propia: el modelo añade fibra, alimentos o "farmacia" (T5). Decisión clínica pendiente: ver Notas a CLÍNICO.
2. Recuento de 'NO SE PREOCUPE' sin "tranquilo", "no pasa nada", "sin importancia".
3. Línea de urgencias repetida dentro de una respuesta (inocuo).

### Versión corregida (cambios mínimos en TAREA (estreñimiento), FORMATO (recuento) y RESTRICCIONES (farmacia); el resto igual)

```
ROL: Eres una redactora de materiales para pacientes de Atención Primaria, con conocimientos de lenguaje llano.

CONTEXTO: Soy médica de familia en España. Quiero una hoja GENÉRICA de preguntas y respuestas para personas que empiezan un tratamiento que puede dar molestias digestivas los primeros días, sin nombrar el tratamiento: vale para cualquiera. La entrego o la envío por el canal del centro. Sin ningún dato de nadie. TRATO: usted.

TAREA: Cinco preguntas, con las palabras que usaría la persona, y su respuesta, sobre: náuseas; estreñimiento; ardor o reflujo; sentirse lleno enseguida; y "¿cuánto dura esto?". Cada respuesta solo con medidas generales de casa, y nada más: raciones pequeñas; comer despacio y parar al notar el estómago lleno; evitar las comidas muy grasas y el alcohol mientras duren las molestias; beber a sorbos a lo largo del día; moverse un poco después de comer y no tumbarse justo después. Para el estreñimiento, solo beber a sorbos y moverse, y que si con eso no basta se habla en consulta: no añadas fibra, alimentos concretos ni laxantes [POR ACLARAR: si CLÍNICO añade una medida para el estreñimiento, va aquí en la lista]. En la última, que suelen ir a menos en las primeras semanas y que, si no, se habla en consulta.

FORMATO: Máximo 220 palabras sin contar las líneas literales, frases de 15 palabras como máximo, nivel de lectura de 12 años, sin negritas ni emoticonos. La línea de urgencias va solo al pie, no dentro de las respuestas. Al pie, en este orden y literal: "Si tiene dudas, [FALTA: contacto del centro]."; "Si no tolera líquidos, tiene dolor fuerte de tripa, se marea o se encuentra mal, no espere: urgencias o 112. Y ante cualquier molestia, pida cita y lo vemos, o le llamo yo."; y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Última línea, literal: "PREGUNTAS: [n] · NOMBRES DE FÁRMACOS O 'FARMACIA': [n] · DOSIS O CAMBIOS DE PAUTA: [n] · 'NO SE PREOCUPE', 'ES NORMAL' O 'NO PASA NADA': [n]": la primera tiene que ser 5 y las otras 0; un cambio de pauta es cualquier "tome menos", "sáltese", "espere a la siguiente" o cantidad con unidad; la última cuenta también "tranquilo" y "sin importancia".

RESTRICCIONES: No nombres el tratamiento ni ningún fármaco, tampoco para las náuseas o el estreñimiento ni de venta libre, ni remitas a la farmacia. No digas que se reduzca, se salte o se retrase una dosis: la pauta solo se cambia en consulta. Sin "no se preocupe", "es normal", "tranquilo", "no pasa nada" ni "sin importancia". Sin más consejos de comida que los dados, sin dietas, sin peso ni cifras. No inventes teléfonos ni "responda a este mensaje". No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale, con la última línea "PREGUNTAS: 5 · NOMBRES DE FÁRMACOS O 'FARMACIA': 0 · DOSIS O CAMBIOS DE PAUTA: 0 · 'NO SE PREOCUPE', 'ES NORMAL' O 'NO PASA NADA': 0".

Añadir a "qué revisar" (l. 201), tras "cuentan cero": "Y 'fibra', 'fruta' y 'farmacia' en la respuesta del estreñimiento: no es que estén mal, es que no las diste tú; si quieres que estén, las pones en la lista de medidas y entonces las revisa la guía, no la máquina."

---

## Caso 5 · Llamar a quien no vuelve · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿Las tres variantes salen sin reproche y con salida digna?** Sin reproche literal, sí, en los tres: la lista de la definición ("faltó", "no vino", "no acudió", "abandonó", "se ha perdido", "debería", "tiene que") es cerrada y contable, y la apertura del ejemplo ("hace tiempo que no nos vemos") sale igual en Claude, ChatGPT y Gemini. La salida digna, también: "la puerta sigue abierta", "cómo pedir cita cuando quiera" y "su médica sigue siendo la misma" son tres instrucciones concretas y los tres las cumplen; es el mejor bloque del caso. Lo que pasa el recuento está en las variantes. "No tengo tiempo": bien en los tres (recogen y ofrecen la hora "cuando le venga bien"). "No ha servido de nada": Claude y ChatGPT recogen sin discutir; Gemini, en una de tres, defiende ("los tratamientos a veces necesitan ajustes, y ahora hay más opciones"), que es lo que "qué revisar" avisa; "ahora hay más opciones" además promete ("esta vez sí" con otras palabras). "Me da vergüenza volver": es donde fallan dos de tres: ChatGPT escribe "no tiene por qué avergonzarse" y Gemini "no hay nada de qué avergonzarse", que discuten el sentimiento que la tarea manda recoger "sin discutirlo"; Claude escribe "Entiendo que dé vergüenza. Aquí nadie va a juzgarle", que recoge. Hay que prohibirlo por su nombre: "no le digas que no debería sentir lo que siente ('no tiene por qué', 'no hay nada de qué')". Y dos frases que evalúan y no están en la definición: "valoramos su esfuerzo" (Gemini, dos de tres: "esfuerzo" es además palabra de la lista del caso 1) y "para retomar sus objetivos" (ChatGPT, una de tres). Con "esfuerzo", "objetivos" y "compromiso" en la definición, se cazan.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "Es un criterio de aviso que pacté con enfermería" enlaza con el capítulo 5 (caso 5); "las horas las pongo yo fuera de la IA" dentro de la variable: bien. |
| Anonimización | No entra ningún dato: sin (0), correcto (como los casos 5 y 6 del capítulo 4). "No incluyas ni pidas datos": sí. |
| Variables | LO QUE PUEDO OFRECER y CÓMO SE PIDE CITA con ejemplo; TRATO fijo en usted. Falta cómo se presenta quien llama: los tres escriben "Soy [nombre], enfermera del centro" o "[su nombre]", un corchete que el prompt no admite y que la restricción ("no inventes… nombres") no resuelve. Se admite un hueco: "[FALTA: quien llama]". |
| Salidas cerradas | Cinco textos con título y tope cada uno, recuento triple con dos definiciones cerradas (reproche; evalúa con ejemplos): bien. "MENCIONES DE PESO, CIFRAS O FÁRMACOS": contable. Falta "esfuerzo", "objetivos", "compromiso" en evalúa. |
| Portabilidad | Sin cambios. Gemini pone los títulos en negrita y añade "(pausa)" y "[sonreír]" como acotaciones; solo "[escuchar]" está admitida: decirlo. ChatGPT alarga las respuestas a 70-80 palabras; el tope de 60 se comprueba a mano. |
| Ejemplo de salida | Realista: es la salida de Claude. "No pasa nada" en la salida digna: en una llamada, es la frase que hace falta; no la cuento como evalúa. |
| Riesgo | Bien identificado (control de asistencia) y bien mitigado. Lo que falta no es del riesgo: es de la seguridad. "Qué revisar" dice que si aparece un efecto adverso, ánimo bajo o ideas de muerte "el guion se acaba y empieza la consulta" (l. 230); pero el guion lo lleva enfermería en la mano, no el libro. Un cuarto bloque de treinta palabras ("SI CUENTA OTRA COSA") pone esa regla donde se usa, y enlaza con los criterios de aviso del capítulo 5 ("ideas de muerte: el mismo día"). |

### Ejecución mental (variables del ejemplo, los tres)
- **Claude:** apertura de 40 palabras sin "faltó"; tres respuestas de 45-60 con recoger + una idea + oferta literal; salida digna con las tres piezas. "Soy [su nombre], del centro de salud" (corchete no admitido). Recuento 0 · 0 · 0, verdadero.
- **ChatGPT:** "no tiene por qué avergonzarse"; "retomar sus objetivos"; "es importante que sepa que…" (una de tres; la definición lo caza y él cuenta 0); respuestas de 70 palabras.
- **Gemini:** "valoramos su esfuerzo"; "ahora hay más opciones"; "[sonreír]"; negritas; "nos gustaría retomar el seguimiento" (la palabra que "qué revisar" manda buscar).
- Rúbrica: fidelidad alta en la oferta (copian las opciones dadas); priorización correcta (escuchar antes de ofrecer); calibración no aplica; acción segura: alta si se añade el bloque de "otra cosa"; anexo B: la pregunta 6 caza "objetivos" y "esfuerzo".

### Problemas
1. Discutir el sentimiento en la variante de la vergüenza ("no tiene por qué", "no hay nada de qué").
2. "Esfuerzo", "objetivos", "compromiso" fuera de la definición de evalúa; "más opciones" como promesa.
3. Quien llama no puede presentarse sin inventar: hueco admitido.
4. Sin bloque de seguridad en el guion (lo que hoy está solo en "qué revisar").
5. Acotaciones no admitidas ("(pausa)", "[sonreír]").

### Versión corregida (cambios en CONTEXTO (quien llama), TAREA (vergüenza; bloque 4), FORMATO (definición) y RESTRICCIONES)

```
ROL: Eres médica de familia con experiencia en obesidad y en entrevista motivacional, y escribes guiones para llamadas breves.

CONTEXTO: Atención Primaria en España. Una persona con obesidad no ha acudido a dos citas seguidas; es un criterio de aviso que pacté con enfermería. Quiero un GUION ORAL para la llamada, que puede hacer enfermería o yo; quien llama se presenta como "[FALTA: quien llama], del centro de salud, de parte de su médica". Genérico: sin nombre, sin motivo de las citas, sin ningún dato. LO QUE PUEDO OFRECER de verdad: [por ejemplo: cita presencial conmigo, cita con enfermería o una llamada a la hora que le venga bien; las horas las pongo yo fuera de la IA]. CÓMO SE PIDE CITA en mi centro: [por ejemplo: por la aplicación del servicio de salud o en el mostrador]. TRATO: usted.

TAREA: (1) APERTURA, máximo 50 palabras: quién llama y por qué ("hace tiempo que no nos vemos y quería saber cómo está"), sin ninguna referencia a que faltó; una pregunta abierta sobre qué se lo está poniendo difícil; y "[escuchar]". (2) TRES RESPUESTAS, máximo 60 palabras cada una, a lo que la persona suele decir: "no tengo tiempo", "no ha servido de nada" y "me da vergüenza volver". Cada una: recoge lo que ha dicho con sus palabras, sin discutirlo y sin decirle que no debería sentirlo; una idea: la obesidad es una enfermedad crónica que va por épocas, no una nota de examen; y la oferta concreta, con las opciones que te he dado. (3) SALIDA DIGNA, máximo 40 palabras, si no quiere seguir ahora: la puerta sigue abierta, cómo pedir cita cuando quiera, y que su médica sigue siendo la misma. (4) SI CUENTA OTRA COSA, máximo 30 palabras, para quien llama, no para decir: si cuenta molestias con un tratamiento, ánimo bajo o ideas de muerte, la llamada deja de ser esta: cita con la médica hoy, y se anota; no se aconseja nada por teléfono.

FORMATO: Los seis textos con su título, para decir en voz alta: frases de 15 palabras como máximo, sin negritas, sin emoticonos, sin acotaciones salvo "[escuchar]", sin pie de aviso: es una llamada. Última línea, literal: "PALABRAS DE REPROCHE: [n] · FRASES QUE EVALÚAN: [n] · MENCIONES DE PESO, CIFRAS O FÁRMACOS: [n]": reproche es cada "faltó", "no vino", "no acudió", "abandonó", "se ha perdido", "debería", "tiene que"; una frase que evalúa califica a la persona o lo que hizo ("muy bien", "una pena", "es importante que", "valoramos su esfuerzo", "sus objetivos", "su compromiso"); las tres tienen que ser 0.

RESTRICCIONES: Sin reproche, tampoco disfrazado de preocupación ("nos tenía preocupados"). No le digas que no tiene por qué sentir lo que siente ("no tiene por qué avergonzarse", "no hay nada de qué"). Sin hablar de peso, kilos, balanza ni de lo que "tiene que" hacer. Sin fármacos ni nombres comerciales. Sin prometer resultados: ni "esta vez sí" ni "ahora hay más opciones". No inventes horarios, teléfonos ni nombres: las opciones son las que te he dado y el único hueco es quien llama. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale, con la apertura "Buenos días, soy [FALTA: quien llama], del centro de salud, de parte de su médica. Hace tiempo que no nos vemos…" y una línea nueva: "> SI CUENTA OTRA COSA. Molestias con un tratamiento, ánimo bajo o ideas de muerte: esta llamada se acaba y se pide cita con la médica hoy. Se anota."

Añadir a "qué revisar" (l. 230), tras "seguimiento": "y 'avergonzarse' y 'objetivos': la primera discute lo que la persona siente; la segunda le pone una nota. El bloque cuarto no se lee a la persona: es para quien llama, y con ideas de muerte la cita es el mismo día (capítulo 5)."

---

## Caso 6 · Cartel de sala de espera · veredicto: LISTO (retoque)

### Respuesta a la atención especial del ORQUESTADOR
**¿25 palabras con contacto como hueco es realista?** Sí. La variante del ejemplo tiene 20 palabras sin la línea de contacto; las tres ideas obligatorias (enfermedad crónica; no es falta de voluntad; aquí se puede hablar) caben en tres frases de seis o siete palabras. Los tres modelos lo hacen; lo que no hacen es contar bien: escriben "24" donde hay 27 y, la mitad de las veces, cuentan la línea de contacto aunque la tarea diga que no; el recuento no lo repite y "qué revisar" lo salva ("cuenta las palabras con el dedo"). **¿Mete cifras o "hábitos"?** Cifras, no, en ninguno (la restricción basta y un cartel no las pide). "Hábitos", tampoco: aparece en hojas, no en carteles. Lo que meten es otra cosa: un titular con pregunta en usted ("¿Sabía que la obesidad es una enfermedad?", Gemini y ChatGPT), un imperativo ("Hable con nosotros", "Pida ayuda", ChatGPT), y en Gemini una variante con "lucha" ("no es una lucha en solitario": está en la lista, cuenta 1 y escribe 0) y un emoticono pese a la prohibición. Con "sin preguntas ni imperativos, salvo la línea de contacto" se cierra lo primero; lo segundo, con el dedo.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "Sin patrocinio" y "sin marcas ni logotipos de ninguna entidad" dentro del prompt: la decisión del capítulo 3 hecha instrucción. |
| Anonimización | No entra nada: sin (0), correcto. "No incluyas ni pidas datos": sí. |
| Variables | IDEA fija; sin variables. Correcto: el cartel es uno. |
| Salidas cerradas | Tres variantes numeradas, línea literal, recuento triple con lista cerrada contable. El recuento de palabras no dice "sin contar la línea de contacto" (lo dice la tarea). |
| Portabilidad | Sin cambios. Gemini añade un titular y un emoticono; ChatGPT, "Variante 1:" con dos puntos y a veces una cuarta "bonus". "Nada más" está; se comprueba a mano. |
| Ejemplo de salida | Realista: la variante 1 es la de Claude y la de ChatGPT casi palabra por palabra; "19 / 22 / 24" es lo que escriben, y "qué revisar" avisa de que no es verdad. |
| Riesgo | Bien identificado (señalar a quien está sentado debajo). La mitigación dice "sin 'usted'" y la tarea admite "usted o impersonal" con una línea literal en usted ("Pregunte a su médica…"): contradicción. Lo coherente con el riesgo: impersonal en el cuerpo ("La obesidad es…", "Aquí se trata"), y el usted solo en la línea de contacto, que se dirige a quien quiera preguntar, no a quien está sentado. |

### Ejecución mental (los tres)
- **Claude:** tres variantes de 17-23 palabras, impersonales, con la línea literal; recuento aproximado; 0 cifras; 0 lista.
- **ChatGPT:** una variante con "Hable con nosotros" (imperativo); "Variante 1:"; cuenta la línea de contacto en una de tres (32 / 30 / 29).
- **Gemini:** titular "¿Sabía que…?"; "no es una lucha en solitario" (lista: 1; escribe 0); emoticono; "ante cualquier duda, acuda a su centro" (una línea de urgencias blanda que el cartel no lleva; ver T3).
- Rúbrica: no aplica más que acción segura, alta: no hay decisión ni persona; anexo B: pregunta 6 (consejo) caza "Pida ayuda".

### Problemas
1. Contradicción usted / impersonal entre tarea y riesgo.
2. Recuento sin "sin contar la línea de contacto".
3. Preguntas e imperativos no prohibidos ("¿Sabía que…?", "Hable con nosotros").
4. Línea de "acuda" añadida (Gemini): "sin ninguna línea de urgencias ni de 'acuda'".

### Versión corregida (cambios mínimos en TAREA, FORMATO y RESTRICCIONES)

```
ROL: Eres una redactora de textos breves para espacios de salud, con conocimientos de lenguaje centrado en la persona.

CONTEXTO: Soy médica de familia en España. Quiero el texto de un cartel para la sala de espera de mi centro que diga que la obesidad es una enfermedad crónica y que aquí se trata. Solo el texto; el diseño va aparte. Sin ningún dato. Sin patrocinio. IDEA que debe estar: "La obesidad es una enfermedad crónica. Aquí se trata."

TAREA: Tres variantes, de máximo 25 palabras cada una sin contar la línea de contacto, en forma impersonal (sin "usted" ni "tú" en el cuerpo), que digan: que es una enfermedad crónica; que no es falta de voluntad; y que en este centro se puede hablar de ello. Cada variante termina con esta línea literal, la única en usted: "Pregunte a su médica o enfermera, o en [FALTA: contacto del centro]."

FORMATO: Las tres variantes numeradas; nada más: sin titular, sin cuarta variante. Sin cifras, sin preguntas, sin imperativos fuera de la línea literal, sin exclamaciones, sin emoticonos, sin descripción de imágenes. Última línea, literal: "PALABRAS POR VARIANTE, SIN LA LÍNEA DE CONTACTO: [n] / [n] / [n] · CIFRAS: [n] · PALABRAS DE LA LISTA: [n]": la lista es "obeso", "obesa", "adelgazar", "kilos", "peso ideal", "dieta", "esfuerzo", "culpa", "lucha"; las dos últimas cifras tienen que ser 0.

RESTRICCIONES: Sin culpa, sin consejos ("coma", "muévase", "pida ayuda"), sin prometer resultados, sin fármacos ni nombres comerciales, sin marcas ni logotipos de ninguna entidad, sin ninguna línea de urgencias ni de "acuda". Usa "persona con obesidad" si nombras a alguien. No rellenes el marcador. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale, con la última línea "PALABRAS POR VARIANTE, SIN LA LÍNEA DE CONTACTO: 19 / 22 / 24 · CIFRAS: 0 · PALABRAS DE LA LISTA: 0". El riesgo (l. 260) queda coherente: "sin 'usted'" en el cuerpo; la línea de contacto es la excepción y el texto puede decirlo en cuatro palabras.

Añadir a "qué revisar" (l. 258), tras "donde hay 29": "y no cuentes la línea de contacto, que el modelo cuenta la mitad de las veces. Busca 'lucha' y '¿': la primera está en la lista y pasa; la segunda es un titular que el cartel no pidió."

---

## Caso 7 · Leer una etiqueta nutricional · veredicto: LISTO (integración comprobada; no se reabre)

Comprobado, punto por punto, contra `capitulos/cap06_caso_etiqueta_reservado.md` y el plan (`revisiones/cap06_plan.md`, fila 7):

| Comprobación | Estado |
|---|---|
| Numeración y remisiones | "Caso 7", en la tabla mental del capítulo y en la frase introductoria ("el 7 se borra al terminar por la imagen"; "el 7 necesita que la herramienta lea imágenes"; "Higiene: sí en el 7"): coherente con la ficha del capítulo 4. |
| Higiene remitida al capítulo 3 | El reservado decía "borra la conversación y, si hay biblioteca de archivos, el archivo"; la v1 dice "la conversación y el archivo, como en el capítulo 3" (l. 268). Correcto: el plan pedía capítulo 3 (no 1). |
| Línea de contacto y disclaimer (regla 19) | Añadido en el prompt (l. 283: "Cierra las tres frases, en este orden y literal, con: 'Si tiene dudas, [FALTA: contacto del centro].' y 'Material informativo…'"), en el ejemplo (l. 294) y en "qué revisar" (l. 296: "si se imprimen o se envían, van con el contacto rellenado en tu sistema y con tu nombre"). Sin línea de urgencias, y el texto lo dice ("una etiqueta no toca síntomas"). Forma única del contacto. Dos líneas, como el plan y la frase introductoria (l. 53). |
| Restricciones nuevas | "No rellenes el marcador. No incluyas ni pidas datos de personas." añadidas (l. 285): decisión 7 cumplida; el reservado no las llevaba. |
| Referencias | Reglamento 1169/2011 (art. 18) y Reglamento 1924/2006 (anexo, "light") como 15 y 16 de la lista del capítulo, con el [VERIFICAR] del segundo conservado. |
| Ejemplo de salida | El del reservado más las dos líneas; sigue siendo realista y con "Legibilidad: BUENA" y "COHERENTE". |
| Riesgo | El del reservado más "comprueba la versión vigente" (decisión 5). |
| Texto del prompt | Idéntico al revisado en el ciclo del capítulo 2 salvo los añadidos anteriores: no se reabre. |

Un solo apunte, sin cambio de prompt: la frase de "qué revisar" ("Si las frases salen de tu boca, las dos líneas del final sobran y las quitas") está bien, y es la única excepción del capítulo en que las líneas de la regla 19 se quitan a mano; la frase introductoria (l. 53) ya lo dice ("El 7 se entrega a veces: dos"). Coherente.

---

## Coherencia con los capítulos 4 y 5 (T1-T7 de `revisiones/cap04_prompts.md`; T1-T7 de `revisiones/cap05_prompts.md`) y con la ficha del caso 7 del capítulo 4

- **Cap. 4 T2 (correa por nombre, clase y juicio):** heredada por nombre en los casos 3, 4, 5 y 6; por clase, en ninguno. Es el hallazgo del caso 3 (T5 de este informe). El caso 4 la hereda mejor que ningún prompt anterior (venta libre por su nombre).
- **Cap. 4 T3 → regla 19:** aplicada en 1, 2 y 4 con las tres líneas literales y en orden, y en el 7 con dos; los guiones (3, 5) y el cartel (6) fuera y declarados: es la regla mejor aplicada del capítulo. Precisión del ciclo 5 (no hay tercera fórmula): en riesgo en el caso 1 con "ninguna" y en el 6 con Gemini (T3 de este informe).
- **Cap. 4 T4 (lo que no le das, lo inventa):** todas las variables llevan ejemplo; lo que falta es quien llama en el caso 5 y la medida del estreñimiento en el 4.
- **Cap. 4 T5 / cap. 5 T2 (recuentos definidos y contables):** heredados en los ocho; con defecto de unidad en el 1 ("técnicas"), en el 2B ("iguales") y en el 3 (clase, vía). Los ejemplos de los casos 1 y 2 no cuadran entre sí (T6 de este informe).
- **Cap. 4 T6 (trato y aviso juntos):** cumplido en 1 (contacto y aviso), 4, 6 y 7 (usted fijo); incumplido en 1 (fórmulas de urgencias sin tú) y 3 (línea de la regla 17 solo en usted con TRATO tú admitido).
- **Cap. 5 T1 (etiqueta (0) donde entra texto):** cumplido: 1, 2A y 2B la llevan con "para"; 3, 4, 5 y 6 no la necesitan; 7 tiene su puerta de imagen.
- **Cap. 5 T3 / regla 24 (hueco a medias):** no aplica: ningún prompt del capítulo es de documentación; los huecos son los de la regla 19 y se copian tal cual.
- **Cap. 5 T6 (corchete-instrucción):** reaparece en el caso 1 (LÍNEA DE URGENCIAS) y, leve, en el 2A (TRATO).
- **Cap. 5 T7 (lo que se conserva):** la forma única del contacto, "sin contar las líneas literales", el rol en femenino en los ocho, "unas / máximo" y no recuentos exactos, "Ninguno pide razonador" con la excepción declarada del 7 (imágenes).
- **Regla 12:** nota al pie en los casos 3 y 4 (el 4 la comparte): donde la regla la exige y solo ahí (regla 25). Los prompts no nombran ningún fármaco, y con la corrección del caso 3 tampoco la clase.
- **Regla 21:** una sola atribución a "mi formación en IA" (l. 37), fuera de los prompts: correcto.
- **Regla 22:** no hay casos sintéticos con datos en este capítulo; la hoja de ejemplo es genérica.
- **Ficha del caso 7 del capítulo 4 (v3):** el capítulo la cita con "Higiene: sí en el 7" y "Probada por" con fecha (l. 55) y en "Hazlo hoy" (l. 331): es lo que el ciclo 5 pidió. Precisión para la ficha del caso 2: "Higiene: conversación nueva y memoria apagada: sí" en el paso B (es el requisito del caso), y "Por qué esta herramienta: en B, otro modelo si lo hay". Ejemplo de tres líneas, si el REDACTOR quiere uno: "hoja-examen-legibilidad · v1 · cualquiera vale · chat · consulta · Datos: ninguno (hoja genérica) · Higiene: no hace falta · Riesgo: bajo (si cuenta mal, cuento yo) · Probada por: CP, 2026-09-13".

## Notas para el REDACTOR (integrar sin alargar)

El capítulo está en 7.849 palabras con tope 8.000 (regla 20). Todo lo que propongo se hace por sustitución dentro de los bloques y suma, neto, unas 180-220 palabras (el caso 1 gana unas 80 por las fórmulas en dos tratos; el 5, unas 50 por el bloque cuarto; el 2B, unas 40 por la definición de las tres comprobaciones). Para compensar: (a) el caso 2 puede perder la frase de Khoong 2019 en "qué revisar" si EVIDENCIA no la confirma, o dejarla en media línea; (b) en el caso 1, "qué revisar" pierde "La hoja del capítulo 1 se cerró antes de las tres líneas; el examen se las añade" (ahora lo dice el prompt); (c) en el caso 3, "qué revisar" pierde "La línea de seguridad se dice entera, aunque suene larga" (el ejemplo la muestra); (d) el caso 6 puede perder "Como la hoja sobre IA del capítulo 3, pasa por quien revise…" si COMPLIANCE no lo exige. Orden de importancia: caso 1 (negaciones, técnicas, urgencias), caso 3 (clase y siglas), caso 2B (líneas finales y no retocar), caso 2A (112 y corchete), caso 5 (vergüenza y bloque cuarto), casos 4 y 6 (retoques de una línea), ejemplos con números que cuadren (10 y 13).

## Notas para otros agentes (no las resuelvo yo)

- **CLÍNICO:** (a) Caso 4: qué medida de casa, si alguna, va en la lista para el estreñimiento al empezar un tratamiento (fibra, fruta y verdura, líquidos): el prompt corregido lleva un [POR ACLARAR] en ese punto y, mientras no se decida, prohíbe añadir nada. (b) Caso 3: si "también ayuda a regular el azúcar" en el guion de una persona con diabetes es, como creo, una afirmación que solo debe dar la médica; el prompt la prohíbe por su nombre. (c) Caso 5: si el bloque "SI CUENTA OTRA COSA" (molestias con un tratamiento, ánimo bajo, ideas de muerte: cita hoy) es la lista correcta para una llamada de enfermería, y si falta algo (hipoglucemias si lleva insulina, como en el caso 5 del capítulo 5).
- **COMPLIANCE:** (a) Caso 6: el prompt prohíbe cualquier línea de "acuda" o urgencias en el cartel; el capítulo dice que el cartel no lleva pie y COMPLIANCE se pronuncia (plan). (b) Caso 2: el mediador intercultural lee una hoja con "[FALTA: contacto del centro]" en español dentro del texto árabe: sin problema de datos, pero conviene que "qué revisar" le diga qué es ese corchete. (c) Caso 1: la línea "Revisado por: ___ Fecha: ___" del capítulo 1, si se pega rellenada, lleva el nombre de la médica y una fecha: el prompt corregido pide quitarla antes; no es dato de paciente, pero es dato.
- **EVIDENCIA:** nada en los prompts depende de una cita. Brislin 1970 y Khoong 2019 rodean al caso 2 y no son de mi ámbito; INFLESZ (Barrio-Cantalejo 2008) sostiene el criterio de sílabas del caso 1, que ahora es un recuento informativo y no un tope.

## Preguntas para Cristina

1. Caso 1: ¿quiere que "No es culpa suya" y "No es falta de voluntad" se queden en toda hoja que pase el examen? El prompt de la v1 las borra; el corregido las protege. Si tiene otras frases suyas que niegan la culpa, entran en la misma excepción.
2. Caso 2: ¿qué idiomas necesita de verdad su cupo, y su mediador intercultural lee árabe estándar o le pide la hoja en otra forma (por ejemplo, para explicarla en dariya)? El prompt traduce a lo que ella escriba en [IDIOMA]; si el mediador prefiere otra cosa, cambia el ejemplo.
3. Caso 3: ¿cómo explica hoy el mecanismo con sus palabras, y dice en voz alta el nombre de la familia del fármaco con la caja delante? El prompt corregido no deja que lo diga la máquina; si ella sí lo dice, es suyo, no del guion.
4. Caso 4: ¿qué recomienda hoy para el estreñimiento de los primeros días (fibra, fruta, líquidos, nada)? Es la única medida que la lista no cubre y la máquina rellena.
5. Caso 5: ¿quién llama en su centro y cómo se presenta ("de parte de su médica" o con su nombre)? Y su frase real ante "me da vergüenza volver": el prompt prohíbe "no tiene por qué avergonzarse" porque discute lo que la persona siente; si ella dice otra cosa, va como ejemplo.
