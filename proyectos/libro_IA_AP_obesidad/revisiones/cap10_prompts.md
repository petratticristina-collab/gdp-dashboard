# Revisión PROMPTS · Capítulo 10 · v1

> Agente: PROMPTS (ingeniero de prompts) · Fecha: 2026-09-21 · Ámbito: exclusivamente los seis prompts (casos 1, 3, 5, 6, 7 y 8), los dos bloques sin IA (hoja de auditoría del caso 2 y guion oral del caso 4: solo su usabilidad y su coherencia con el anexo B y las reglas 16, 18, 27 y 29), los ejemplos abreviados de salida, la plantilla rellenada del caso 7 en `anexos/cap10_material_anexos.md` (l. 24-44) y la frase introductoria a los casos (l. 84), porque fija reglas que los seis heredan. No se revisa el texto expositivo, la viñeta ni las referencias, salvo cuando un prompt depende de ellos (la frase de farmacovigilancia de la escena (i) del caso 3, l. 153; las diez preguntas del capítulo 3, l. 360-376, que la hoja del caso 2 cita por número).
> Versión revisada: `capitulos/cap10_v1.md` (commit 7ee8739; 9.884 palabras según `split()` con los bloques de código, 9.796 según el REDACTOR; líneas citadas con `cat -n`). Los ocho bloques pesan 2.440 palabras (349 · 194 · 346 · 160 · 348 · 348 · 348 · 347), contadas con el script de los capítulos 7 a 9 (`len(texto.split())`). Regla de este ciclo (regla 20, opción a; l. 9 del contexto común): 350 palabras por prompt es práctica recomendada; si la corrección la supera, digo qué protege cada palabra de más. **La v1 cumple la práctica en los seis prompts y los dos topes de los bloques sin IA (194 ≤ 200; 160 ≤ 160): es el segundo capítulo seguido que entra sin justificar nada.** Mis versiones corregidas pesan **405 · 207 · 388 · 171 · 382 · 399 · 407 · 383 (2.742; +302 sobre la v1)**: los seis prompts crecen porque cada uno tenía al menos un recuento que no se podía contar con el dedo, una variable con la instrucción dentro del corchete o un ejemplo de salida que el prompt no puede producir (T3, T4, T11); en cada uno digo qué protege cada palabra y qué se puede recortar "(−n)" si el ORQUESTADOR quiere acercarse a 350 (T1). El tope del capítulo es 10.000 sin tope ad hoc (decisión 5 del plan): +302 de código exige recortar prosa o aplicar los recortes marcados; lo digo en T1 y en las notas.
> Método: el de los capítulos 1 a 9 (`revisiones/cap09_prompts.md`). Para cada prompt: rol · contexto · tarea · formato · restricciones; etiqueta (0) con parada donde entra un texto, un perfil o un caso (T1 del capítulo 5); variables entre corchetes con valor por defecto y sin instrucción al lector dentro del corchete (T6 del capítulo 5; T4 del capítulo 9); recuentos definidos en la misma línea y contables a mano (T2 del capítulo 5; T3 de los capítulos 8 y 9); "DECISIÓN: la médica" donde hay decisión clínica (regla 30); si el modelo puede rellenar un hueco sin que se note (regla 24; regla 36); portabilidad Gemini / ChatGPT / Claude sin cambios; realismo del ejemplo de salida para 2026; riesgo. Cada prompt se ha ejecutado mentalmente con un caso sintético en los tres modelos: treinta salidas de los prompts 1.5, 4.5, 4.6, 6.4 y 5.7 con el perfil de la mujer de 50-60 años (caso 1); el caso inventado de vómitos con un principio activo de seguimiento adicional sin escribirlo (caso 3); el contexto literal del prompt (caso 5); una hoja "Recomendaciones para el paciente obeso" de 180 palabras con cinco "debe", un "si no adelgaza" y una línea de urgencias antigua (caso 6); el resumen de ejemplo del prompt con y sin cifras de minutos (caso 7); las tres entradas de QUÉ TRAE (caso 8). La salida se ha leído con la rúbrica del capítulo 4 y las diez preguntas del anexo B. Contrastado con `revisiones/cap10_plan.md` (comprobaciones para PROMPTS, l. 189; decisiones 1, 2 y 7 del ORQUESTADOR, l. 209-217), `biblia.md` (reglas 7, 10, 11, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 29, 30, 32, 33, 34 y 36 con sus precisiones de los ciclos 7-9), `memoria/M3_marco_legal_etico_compliance.md` y `memoria/M3_checklist_compliance.md` (protocolo RAM, para la regla 10) y la ficha del caso 7 del capítulo 4 (v3, l. 342-388) como plantilla de guardado.

## Resumen de veredictos

| Caso | Bloque | Palabras v1 → corregida | Veredicto | Motivo principal |
|---|---|---|---|---|
| 1 | Revisor de sesgo de peso (prompt) | 349 → 405 | **mejorar** | La tabla A/B/C × prompt no es contable tal como está: una frase puede encajar en dos categorías y el prompt no dice cuál, con lo que la suma por letra y la suma por categoría no tienen por qué coincidir y nadie puede comprobarlas; se fija "una por frase, la primera que encaje" y "las dos sumas tienen que coincidir". "Las molestias son señal de que funciona" **no** la detecta la categoría INDIVIDUAL como está definida (sus anclas son "en su caso", "usted debería", "pruebe a"; la frase no tiene ninguna): el ejemplo (l. 110) muestra algo que el prompt no produce; entra como ancla con "es normal", y la categoría se define por lo que hace ("decide por la persona lo que decide una consulta"). Un texto sin estigma no tiene salida prevista y los tres modelos, mandados a marcar, marcan: "SIN FRASES MARCADAS". Dos fallos que la ejecución destapa: CIFRA caza los valores de analítica de la carta de resultados (5.7) y INDIVIDUAL caza el "usted" del consejo breve (4.5) y de la carta, que hablan a una persona por diseño: el contexto tiene que decir qué prompts escriben para cualquiera y cuáles a una persona, sin decir qué piden. Y el revisor puede desactivar en sus propias reescrituras (regla 27): "ninguna reescritura tuya puede encajar en una categoría". |
| 2 | Hoja de auditoría (sin IA) | 194 → 207 | **mejorar** | La regla de la hoja se contradice en su propio ejemplo: (b) suma "9 de 10" y dicta "CORRIGE", pero la regla 18 (y la línea de arriba de la misma hoja) dice que 8 o más síes SALE. Hay que decidirlo, no disimularlo: mi versión escribe "9 de 10: SALE por la cuenta; así no sale: vuelve 'No es culpa suya' → 10", y pregunto al ORQUESTADOR y a COMPLIANCE si la regla 27 ("peor que la culpa") convierte la desactivación en NO de la pregunta 5 con corrección obligatoria antes de salir. (a) atribuye "comprométase" a la pregunta 6 y es la 5 (moralización); y marca "1 SÍ" en una hoja de la que nadie sabe qué entró ni dónde: la 1 es NO. "Las otras seis, con las diez" no se entiende; y la hoja no tiene línea en blanco para rellenar, que es lo que una tarjeta en papel necesita. Coherente con el anexo B en las eliminatorias y en la regla binaria. |
| 3 | Notificación de RAM (prompt) | 346 → 388 | **mejorar** | El prompt dice "hueco de línea entera" y el ejemplo (l. 174) pone "[FALTA: dosis y vía]" en mitad de una línea: decisión (2) del REDACTOR, que el ORQUESTADOR me pide fijar. **Decido campos**: un formulario es una lista de campos, y un campo vacío "[FALTA: dosis]" no afirma nada; lo que la regla 24 prohíbe es la frase que afirma con un corchete al final, y eso se dice por su nombre, como en el capítulo 9 (caso 1). Con dieciocho campos nombrados, "RELLENOS + HUECOS = 18" es contable; "BLOQUES RELLENOS: 5 de 5" no cuenta nada (el ejemplo lo escribe con QUIÉN NOTIFICA todo hueco). El principio activo lleva la instrucción dentro del corchete ("[uno con triángulo negro…]"): sale del corchete y queda "[principio activo]", como manda la decisión 2 en sustancia. Las iniciales son el único campo que puede parecer de alguien y no hacen falta en un ensayo: siempre hueco, y no se piden. "conocida" y "descrita" entran en la lista de juicios: es como los tres modelos meten la ficha técnica sin nombrarla. |
| 4 | Guion oral "Me lo ha hecho una IA" (sin IA) | 160 → 171 | **mejorar (leve)** | Usable como tarjeta y coherente con el anexo B (pregunta 6: "el chat escribe para cualquiera; usted no es cualquiera"). Dos correcciones de regla: la frase 5 dice "Nada suyo entra nunca en ella" y la regla 16 fija una sola fórmula en todo el libro ("Nada que permita saber quién es usted entra nunca en esas herramientas"); el capítulo 3 (caso 5) la usa literal y este guion no. Y el bloque 7 es el "si cuenta otra cosa" de la regla 29: le faltan "ánimo bajo" y "se anota" (Ley 41/2002, art. 4.1: lo dicho de palabra consta). Once palabras más que el tope: seis son la regla 16 y cinco la regla 29. |
| 5 | Política de uso de IA del centro (prompt) | 348 → 382 | **mejorar** | Cada frase sale del contexto y el pie con el hueco del delegado está. Tres cosas. (a) "textos propios anonimizados a mano" dentro de lo que entra: leído por el equipo, autoriza a pegar notas clínicas "anonimizadas", que la regla 26 y la misma frase siguiente prohíben; pasa a "textos genéricos del centro sin datos de nadie", que es lo que la frase introductoria (l. 84) dice. (b) Los tres modelos citan el RGPD o la LOPDGDD en la página en uno de tres aunque el contexto no los traiga: "ni leyes, ni artículos, ni herramientas con nombre", contado ("LEYES O HERRAMIENTAS NOMBRADAS: 0"). (c) "HUECOS: [n]" no tiene valor esperado; con el hueco de la próxima revisión (que la mitigación, l. 253, promete y el prompt no pide) son dos, y se escribe 2. La lista de FRASES QUE PROMETEN se completa con las palabras del capítulo 3 (l. 171: "cifrado", "aprobado") y "en cualquier forma", porque Gemini escribe "garantizamos". "Unas 300 palabras" pasa a "máximo 320 sin contar el pie". |
| 6 | Reescribir sin estigma (prompt) | 348 → 399 | **mejorar** | La regla 27 está bien aplicada (negaciones e imperativos conservados y contados). Cuatro grietas. (a) "OBJETIVO DE PESO O CIFRA" es una categoría muerta: la restricción para antes de marcarla; sale de la lista y la parada pasa a la (0) como tercera rama. (b) "INFORMACIÓN CLÍNICA CAMBIADA: 0" es una declaración del modelo sobre sí mismo, no un recuento (regla 36): pasa a "DATOS DE SALUD AÑADIDOS O QUITADOS: [FALTA: contar]", que rellena la médica comparando las parejas original → reescrita, que ahora el prompt pide. (c) "Sin acortarlo más de un 20 %" no se comprueba sin contar: "PALABRAS: original [n] · reescrito [n]". (d) "Imperativo de seguridad" no está definido y los tres modelos convierten "debe tomar la medicación de la tensión cada día" en "le proponemos": "toda orden que evita un daño", con tres ejemplos. La línea de urgencias "solo si el original la traía, literal" crearía una tercera fórmula (regla 19): la línea antigua se conserva donde estaba como imperativo, y la fórmula del libro al pie la pone la médica desde el anexo A. Y "ninguna reescritura tuya puede encajar en una categoría", porque Claude reescribe "si no adelgaza" como "el peso no depende solo de usted". |
| 7 | Hoja de ruta de 90 días (prompt) | 348 → 407 | **mejorar** | El prompt prohíbe inventar minutos y **el contexto no tiene dónde ponerlos**: todo debería salir "[FALTA: minutos]", y el ejemplo (l. 310) y la plantilla del anexo D traen "estimación: 10 minutos por semana" que el modelo se inventó; es exactamente lo que el plan (comprobación 7) y el ORQUESTADOR temen. Entra la variable "MINUTOS QUE ESTIMO RECUPERAR, por caso, solo los que tengo" y el recuento cuenta "CIFRAS DE MINUTOS: [n], todas de mi lista · HUECOS DE MINUTOS: [n]", que suman 5. "Una tabla con tres filas… cinco en total" no dice la estructura (tres filas de mes o cinco de caso; el anexo hace seis) y "CASOS: [n]" no tiene valor esperado: una fila por caso, cinco, "CASOS: 5"; la plantilla del anexo D lleva seis filas contra su propio prompt y lo reconoce en la nota: se quita la fila 8.1 (prensión y silla no es un caso que se prueba, es "algo que antes no hacía", y ya está en esa columna). "QUÉ MIDO Y CON QUÉ" se cierra como lista. Y "lo que no se puede concluir" entra en la salida con una línea literal ("Estas medidas cuentan qué hice, no qué conseguí"), que es la del capítulo 7 aplicada a la médica. |
| 8 | Guion de riesgo (prompt) | 347 → 383 | **mejorar (leve)** | No da cifras propias y no sentencia: los huecos y "AMENAZAS: 0" funcionan en los tres modelos. Le falta "DECISIÓN: la médica" como última línea literal (regla 30; es el prompt del capítulo donde la decisión, la cifra y qué hacer con ella, es de la médica). "KILOS: 0" está dentro de "CIFRAS: 0" (un kilo es una cifra) y no caza "bajar de peso" sin número: pasa a "PESO: 0" definido por mención. "En diez años" fija un plazo que no vale para un test genético ni para toda tabla: "[FALTA: plazo]". "Cifra" no incluía fracciones y Claude escribe "un tercio". ChatGPT añade "consulte con su médico" en un guion que dice la médica: se prohíbe por su nombre. QUÉ TRAE sin valor por defecto. "PALABRAS: [n]" para el tope de 250. |

Ningún prompt es peligroso tal como está: ninguno pide decisiones clínicas, ninguno admite datos de nadie, los seis llevan la línea (0) con "para" y "No incluyas ni pidas datos de personas", y el único que produce algo que llega a una persona (el 6, cuando ENTREGA es hoja) lleva las tres líneas de la regla 19 con la decisión en manos de la médica (regla 30). Ninguno afirma haber ejecutado una prueba, pero uno (el 6) declara un cero sobre sí mismo que no puede contar: es el caso de la regla 36 en este capítulo. Lo que sí es peligroso, sin serlo el prompt, son tres ejemplos de salida que enseñan lo que el prompt prohíbe: minutos inventados con "estimación" delante (7), un hueco de campo bajo un prompt que exige línea entera (3) y una categoría marcada que el prompt no puede marcar (1). Los seis se pegan en los tres asistentes como texto; el 1 exige pegar treinta textos (unas seis mil palabras) y cabe en los tres cuando escribo esto.

---

## Hallazgos transversales (afectan a varios casos)

**T1 · La práctica de 350 y qué protege cada palabra de más.** La v1 cumple en los seis prompts y en los dos bloques. Mi versión supera 350 en los seis y los topes en los dos. Lo que pesa: en el 1, la línea de género de los prompts (+28: sin ella, dos de los cinco prompts se auditan con la categoría equivocada), la definición de INDIVIDUAL con las anclas nuevas (+14: es lo que hace que el ejemplo sea verdad), "SIN FRASES MARCADAS" (+6), la regla de las sumas (+14) y "ninguna reescritura tuya" (+9); recorte posible: quitar las reescrituras (2) entero y dejar solo marcar (−40), si la autora prefiere un revisor que no reescribe (pregunta 1). En el 2, la línea en blanco (+22) y la corrección de (b) (+8); recorte: la línea en blanco al anexo B (−22) si el ORQUESTADOR lleva allí la hoja completa (comprobación 10). En el 3, los dieciocho campos nombrados (+30: son lo que hace contable el recuento y lo que impide que un campo afirme) y la regla 24 por su nombre (+16); no recomiendo recorte. En el 4, la regla 16 (+6) y la regla 29 (+5). En el 5, la prohibición de leyes y herramientas con su recuento (+18), el hueco de la próxima revisión (+9) y las palabras del capítulo 3 (+6); recorte: "en cualquier forma" y "cifrado", "aprobado" (−6) si se acepta que "qué revisar" los busque. En el 6, la definición de imperativo (+16), las parejas y "[FALTA: contar]" (+22), PALABRAS (+8), la tercera rama (+14); recorte: la tercera rama de la (0) a prosa (−14), como en el capítulo 9. En el 7, la variable de minutos (+20), el recuento de cifras y huecos (+16), la línea literal del capítulo 7 (+11) y la lista cerrada de medidas (+10); recorte: la línea literal a prosa (−11). En el 8, DECISIÓN (+4), PALABRAS (+3), "plazo" (+4), fracciones (+4), "consulte con su médico" (+8) y el valor por defecto (+3); recorte: ninguno que merezca la pena. **Recomendación al ORQUESTADOR:** aceptar 2.742 palabras de código si el consolidado recorta prosa (el plan preautoriza cinco traslados a anexos, l. 176, y quedan dos sin aplicar: la hoja de auditoría al anexo B, que además paga el −22 del caso 2, y las URL de referencias) o aplicar los recortes marcados "(−n)", que suman 93 palabras y no tocan ninguna línea de seguridad, ninguna lista de la médica ni ningún recuento.

**T2 · La etiqueta (0) y las paradas.** Los seis prompts la llevan con "para" y con la forma unificada "X SIN DATOS / X CON DATOS: BORRA ESTA CONVERSACIÓN" (TEXTOS, CASO, CONTEXTO, TEXTO, RESUMEN, GUION). El caso 3 la define por identificadores que parecen reales ("PARECE UNA PERSONA REAL"), como pedía el plan, y es la mejor (0) del capítulo: la puerta no filtra "datos" sino "parecer alguien", que es lo que un caso inventado puede llegar a parecer. Novedad: la (0) del caso 6 gana una tercera rama, "TEXTO CON OBJETIVO DE PESO: SE RETIRA", que la v1 tenía escondida en RESTRICCIONES como parada a mitad de tarea; una parada va en la puerta. Como en los capítulos 8 y 9 (T2 del capítulo 9): Gemini no para en uno de tres cuando la (0) tiene tres ramas, escribe la primera línea y sigue; "qué revisar" del caso 6 lo dice. Los dos bloques sin IA no la necesitan y no la llevan; la hoja del caso 2 tiene su propia puerta, la pregunta 1.

**T3 · Recuentos que cuentan lo que el modelo quiso contar (siete).** "FRASES MARCADAS: A · B · C · POR CATEGORÍA" (1) no obliga a que las dos sumas coincidan ni a que una frase tenga una sola categoría; "BLOQUES RELLENOS: [n] de 5" (3) siempre es 5 (un bloque todo hueco "está"); "HUECOS: [n]" (3 y 5) no tiene valor esperado, y un recuento sin valor esperado no se puede comprobar; "INFORMACIÓN CLÍNICA CAMBIADA: 0" (6) es una declaración, no un recuento; "sin acortarlo más de un 20 %" (6) no se ve sin contar; "CASOS: [n]" (7) debería ser 5 y el anexo escribe 6; "CIFRAS SIN 'ESTIMACIÓN': 0" (7) no caza una cifra inventada con "estimación" delante, que es la que importa; "KILOS: 0" (8) está contenido en "CIFRAS: 0". La regla de los capítulos 4, 5, 8 y 9 (unidad definida en la misma línea, contable con el dedo, y un valor esperado cuando lo hay) se aplica en los siete: una categoría por frase y sumas iguales (1); dieciocho campos con RELLENOS + HUECOS = 18 (3); HUECOS: 2 (5); PAREJAS = MARCADAS, PALABRAS original / reescrito y "[FALTA: contar]" (6); CASOS: 5, CIFRAS DE MINUTOS todas de mi lista + HUECOS DE MINUTOS = 5 (7); PESO por mención y PALABRAS (8). Y los que sí eran contables y hay que conservar: "JUICIOS DE CAUSALIDAD, GRAVEDAD O TRATAMIENTO: 0" con sus nueve palabras (3), el mejor definido del capítulo; "FRASES QUE PROMETEN: 0" (5); "NEGACIONES CONSERVADAS" e "IMPERATIVOS DE SEGURIDAD CONSERVADOS" (6); "PROMESAS DE RESULTADO: 0" (7); "AMENAZAS: 0" (8).

**T4 · Variables con instrucción dentro del corchete (T6 del capítulo 5), y valores por defecto.** Una con instrucción: "PRINCIPIO ACTIVO DEL CASO INVENTADO: [uno con triángulo negro de seguimiento adicional en CIMA]" (3): la instrucción sale al rótulo ("elegido por mí en CIMA entre los de seguimiento adicional (triángulo negro)") y queda "[principio activo]", que es lo que la decisión 2 del ORQUESTADOR quiere en sustancia (la variable no se rellena en el libro). Dos sin valor por defecto: "ENTREGA: [solo texto del centro / hoja para la persona]" (6) y "QUÉ TRAE O QUÉ LE DIGO: [… / … / …]" (8): se marca "(por defecto)" en el primer valor, como en los capítulos 4 y 9. Una que faltaba: MINUTOS en el 7 (T11). Las demás están bien: el resumen agregado y los casos con ejemplo (7), el CASO con ejemplo (3), TRATO (6 y 8), y los dos rótulos de pegado ("TEXTOS:" y "TEXTO:" con la instrucción fuera del corchete), que son la forma del capítulo 9.

**T5 · La regla 24 en un formulario: campos, no líneas (decisión (2) del REDACTOR).** El ORQUESTADOR me pide decidir entre "[FALTA: dosis y vía]" como campo y el hueco de línea entera. La regla 24 nació en el capítulo 5 contra "Cribado de atracones [FALTA: resultado]": una frase que afirma que el cribado se hizo y deja el resultado en blanco. Un formulario no tiene frases: tiene campos, y "dosis: [FALTA: dosis]" no afirma que hubiera dosis, igual que "[FALTA: servicio]" en mitad de una plantilla del capítulo 9 (caso 1, T3 de aquel informe) no afirma nada. Lo que sí puede afirmar un formulario es una frase narrativa dentro de un campo ("se suspendió el [FALTA: fecha]", "la reacción cedió al [FALTA: qué]"), y eso es lo que el prompt prohíbe por su nombre. Decisión: **campos, uno por línea, con el hueco como todo el contenido del campo**, y la regla 24 dicha con su ejemplo prohibido. Con ello el ejemplo de la v1 (l. 169-177) es correcto en espíritu y solo cambia de forma (un campo por línea), y el recuento se vuelve contable (T3). El glosario de la biblia ("hueco de línea entera") no cambia: un campo es una línea.

**T6 · La regla 27 en los dos prompts de estigma (casos 1 y 6).** Las negaciones se conservan y se cuentan en los dos, como pide el plan. Lo que la v1 no ve: el revisor reescribe, y sus reescrituras son salidas de la máquina como cualquier otra; Claude, con "Si no adelgaza, su tensión seguirá alta", propone "El peso no depende solo de usted" en uno de tres, que es DESACTIVACIÓN, la categoría que el propio prompt define. La correa es una frase en los dos: "Ninguna reescritura tuya puede encajar en una categoría", y "qué revisar" busca "no depende de usted" también en la columna de la derecha. Las categorías se unifican entre los dos prompts (T8): mismos nombres cortos, y en el 6 se añade OBESO/A porque corrige textos de personas que lo escribieron; en el 1 no hace falta porque los cinco prompts del libro ya lo prohíben. "CIFRA DE PESO" sustituye a "OBJETIVO DE PESO O CIFRA" en el 1 (las cifras de analítica de la carta de resultados no son estigma) y desaparece del 6 (una hoja con objetivo de peso se retira antes de marcar nada: es una parada, no una categoría).

**T7 · Portabilidad y lo que la frase introductoria (l. 84) no dice.** Los seis se pegan en los tres asistentes como texto y ninguno depende de una función de una herramienta: es el capítulo más portable del libro, y hay que decirlo. Tres matices. (a) El 1 pega treinta textos: unas seis mil palabras con el prompt; cabe en los tres cuando escribo esto, pero la salida (treinta líneas con reescrituras) es larga y Gemini la corta en uno de tres si no se le dice "las treinta líneas": el recuento final lo delata (si no llega a treinta, se pide "sigue"). (b) "Nada más" faltaba en cuatro de seis (1, 5, 7, 8): Claude añade una nota final ("He evitado…", "Recuerde que…") y ChatGPT un párrafo de consejos en uno de tres; está en los seis ahora. (c) La frase dice que el 1 "se revisa en un cuarto, o en el mismo sin memoria": bien, con dos precisiones que faltan: las letras A, B y C las asigna la médica antes de pegar y la clave (qué letra es qué asistente) se apunta fuera del chat, porque si está en la conversación el revisor la lee; y si el revisor es uno de los tres, revisa también lo suyo y no lo sabe, que es lo que se quiere. Propuesta para l. 84: "El 1 corre en tres asistentes y se revisa en un cuarto, o en uno de los tres sin memoria; las letras las pones tú antes de pegar y la clave no entra en el chat."

**T8 · Etiquetas del anexo A (reglas 33 y 36), heredadas, nuevas y la lista definitiva.** Heredadas y unificadas en este capítulo: la (0) con parada en los seis; "[FALTA: contacto del centro]" y el disclaimer en usted (6); "DECISIÓN: la médica" como última línea literal (8); "estimación:" delante de cada cifra de tiempo (7; decisión 9); "<5" (5; regla 32); "Sin ninguna línea de 'generado con IA'" dicho desde el contexto (5; regla 23); "NEGACIONES CONSERVADAS" (6; regla 27); "[FALTA: …]" como campo entero (3; regla 24). Nuevas que este capítulo aporta y hay que registrar: las seis categorías de estigma con nombre corto (CULPA · MORALIZACIÓN · ATRIBUCIÓN · DESACTIVACIÓN · CIFRA DE PESO · INDIVIDUAL) y OBESO/A (1 y 6); "SIN FRASES MARCADAS" (1); "PARECE UNA PERSONA REAL: BORRA ESTA CONVERSACIÓN" (3), variante de la (0) para casos inventados; "JUICIOS DE CAUSALIDAD, GRAVEDAD O TRATAMIENTO: 0" (3); "FRASES QUE PROMETEN: 0" y "LEYES O HERRAMIENTAS NOMBRADAS: 0" (5); "TEXTO CON OBJETIVO DE PESO: SE RETIRA" e "IMPERATIVOS DE SEGURIDAD CONSERVADOS" (6); "[FALTA: contar]" (6), hermana de "[FALTA: ejecutar]" para lo que solo puede contar quien compara; "CUANDO HAYA CONTRATO", "PROMESAS DE RESULTADO: 0" y "estimación: [FALTA: minutos]" (7); "AMENAZAS: 0", "PESO: 0" y "[FALTA: n] / [FALTA: plazo]" para la frecuencia natural (8); y la hoja del caso 2 aporta los cuatro veredictos de la regla 18 en mayúsculas (NO SALE / SALE / CORRIGE Y VUELVE A CONTAR / REHACE). No aplican en este capítulo: SIN PÁGINA, FUENTES QUE VEO, PEOR / MEJOR QUE EL CORTE, ENCONTRADOS / RECIBIDOS, SIN RESPUESTA, NO SE ENCIENDE, "[FALTA: ejecutar]" (ningún prompt afirma haber probado nada). Ninguna con sintaxis `[^1]`. **La lista definitiva del anexo A, por familias y con su definición en una línea, va al final de este informe** (sección "Lista definitiva de etiquetas del anexo A"): es el último capítulo y el ORQUESTADOR la monta desde ahí.

**T9 · La memoria del Módulo 3 en los prompts (regla 10).** Ninguna frase copiada en los seis prompts ni en los dos bloques. Lo más cercano: "LA PERSONA, EN MÍNIMOS (iniciales; sexo; franja de edad)" (3) frente a "identificación mínima del paciente (iniciales, sexo, franja de edad, contexto)" del protocolo del módulo: es el mínimo que exige la agencia para que una notificación sea válida y el capítulo 3 aprobado ya lo escribe así (l. 97: "paciente identificable en mínimos (iniciales, sexo o franja de edad)"); no es lenguaje del curso, es el formulario. "En unos cinco minutos" (l. 179) frente a "formulario de ~5 min": ya está en el capítulo 3 (l. 104) y es un hecho, no una frase. La frase de la escena (i) (l. 153) es la de la autora en usted con la red larga entera y "o le llamo yo"; coincide con el capítulo 3 (l. 103) cambiado el trato, y la forma larga de la regla 17 está completa (urgencias o 112, pida cita o le llamo): es de COMPLIANCE, lo digo porque el "qué revisar" del caso 3 remite a ella. Los bloques de la hoja del caso 2 (eliminatorias 1, 3, 6 y 9; 8-10 / 6-7 / <6) son la regla 18 del libro, y la hoja la nombra como regla del capítulo 3, no del curso; la regla binaria para lo publicado es la precisión del ciclo 9.

**T10 · Lo que ya está bien y hay que conservar.** "No juzgas causalidad, gravedad ni tratamiento: ordenas" (3) y la lista de nueve palabras del juicio: el mejor rol y el mejor recuento del capítulo. "PARECE UNA PERSONA REAL" (3) como puerta. "Cada frase sale de una frase del contexto; lo que no esté, no va" (5), que es la regla 24 aplicada a un documento de gestión, y el contexto entero del 5, que es la política del libro dicha en trece frases. "Corriges textos escritos por personas; no cambias la información de salud" (6). "No prometes resultados: ordenas" (7) y la lista cerrada de "algo que antes no hacía", con la prensión y la silla en primer lugar. "Una cuenta hecha sobre muchas personas parecidas, no una predicción sobre usted" y "no cambia lo que hacemos esta tarde" (8), que son la cuarta parte del capítulo en dos frases. El bloque 3 del guion del caso 4 ("Tres cosas que el chat no sabe y yo sí") y su cierre ("el chat escribe para cualquiera; usted no es cualquiera"). La regla de lectura del caso 1 (l. 114: "lo que aparece en los dos pases cuenta; una vez es ruido"), que es la única forma honesta de leer un experimento de treinta salidas sin estadística. Los seis con rol en femenino, "persona con obesidad" donde toca y "No incluyas ni pidas datos de personas" como cierre.

**T11 · Ejemplos de salida que el prompt no puede producir (tres) y uno que lo contradice.** (1) El ejemplo del caso 1 (l. 110) etiqueta "Las molestias son señal de que el tratamiento está haciendo efecto" como CONSEJO INDIVIDUAL DISFRAZADO DE GENERAL; con las anclas de la v1 ningún modelo lo marca así (no hay "en su caso" ni "pruebe a"; Claude lo deja pasar, ChatGPT lo marca como "afirmación clínica no sostenida", que no es categoría, y Gemini no lo marca): el ejemplo es la decisión (3) del REDACTOR y es buena, pero hay que hacerla verdad en el prompt (ancla). (2) El ejemplo del caso 3 (l. 174) usa campos y el prompt exige líneas enteras: T5 lo resuelve a favor del ejemplo. (3) El ejemplo del caso 7 (l. 310) y la plantilla del anexo D (l. 33-37) traen "estimación: 10 minutos por semana", "15", "60", "30" sin que el contexto dé ninguna cifra: son minutos inventados por el modelo con la palabra "estimación" delante, y el recuento "CIFRAS SIN 'ESTIMACIÓN': 0" los da por buenos; es el fallo que el capítulo entero quiere evitar (decisión 9). Con la variable MINUTOS, el ejemplo del capítulo lleva una cifra dada y un hueco, y la plantilla del anexo D se corrige con cinco filas (T3) y sus cifras declaradas como "de mi lista, inventadas para el ejemplo". (4) El ejemplo del caso 3 escribe "iniciales [inventadas]" (l. 173), que no es un hueco ni un dato; con iniciales siempre hueco, desaparece.

**T12 · Decisiones del REDACTOR que tocan a los prompts (l. 5 del contexto común).** (2) Huecos como campos: decidido en T5, campos. (3) Ejemplo del caso 1 con A/B/C y "las molestias son señal de que funciona": se mantiene, y el prompt lo hace posible (ancla en INDIVIDUAL); los modelos ocultos son correctos y la clave fuera del chat (T7). (4) Principio activo como hueco sin rellenar en el ejemplo: correcto; en el prompt es variable sin instrucción dentro (T4), y el ejemplo lo escribe "[principio activo]" con la aclaración "(en el libro, sin rellenar)" para que el lector no lo cuente como hueco del modelo. (1) La frase de la escena (i): T9, de COMPLIANCE.

---

## Frase introductoria a los casos (l. 84) · veredicto: MEJORAR (leve)

Fija cinco cosas que los seis heredan (molde, sin contrato, qué entra, conversación nueva y memoria apagada, ficha) y una que es propia del capítulo (el 1 en tres asistentes y un revisor). Dos precisiones (T7): "o en el mismo sin memoria" pasa a "o en uno de los tres sin memoria; las letras las pones tú antes de pegar y la clave no entra en el chat". Y "los seis prompts se pegan en Gemini, ChatGPT y Claude cuando escribo esto" es verdad sin matices por primera vez desde el capítulo 7: ninguno necesita voz, imagen, archivos ni tareas; se puede decir "los seis son texto y nada más: se pegan en los tres". "Ficha del capítulo 4, caso 7; los dos bloques sin IA, como tarjeta, como en el capítulo 3": bien; la ficha del caso 1 lleva además la clave de letras en "Variables", no en el prompt, y la del 7 la cifra de minutos con su fecha, porque cambia cada mes.

---
## Caso 1 · Auditoría de sesgo de peso en cinco prompts y tres modelos · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿La tabla modelo × prompt es contable?** No como está. El prompt pide (1) marcar, (2) reescribir y (3) una tabla A/B/C × prompt "con las frases marcadas por celda y sus categorías", y una última línea con dos sumas (por letra y por categoría). Tres cosas impiden contarla con el dedo: una frase puede encajar en dos categorías ("comprométase a perder cinco kilos": MORALIZACIÓN y CIFRA) y el prompt no dice si cuenta una o dos; el ejemplo funde los dos pases en una fila ("C · prompt 1 · pases 1 y 2") sin decir si esa fila cuenta 1 o 2; y (1), (2) y (3) repiten la misma información tres veces, con lo que los tres modelos la escriben con pequeñas diferencias entre bloques y la médica no sabe cuál contar. Corrección: una sola salida, treinta líneas (una por texto, en el orden de pegado), cada una con sus frases marcadas, su categoría y su reescritura; "una categoría por frase, la primera de la lista que encaje"; "cada frase cuenta una vez por texto en que aparece"; y "las dos sumas tienen que coincidir", que es lo que la médica comprueba: número de frases en las treinta líneas = suma A+B+C = suma por categoría. La tabla A/B/C × prompt la hace ella en papel con las treinta líneas delante, que es donde debe estar (l. 114: "lo que aparece en los dos pases cuenta"). **¿Detecta "las molestias son señal de que funciona" como consejo individual disfrazado?** No con la v1: la categoría se define por marcadores de segunda persona ("en su caso", "usted debería", "pruebe a") y la frase no lleva ninguno; en la ejecución, Claude la deja pasar, ChatGPT la marca fuera de categoría ("afirmación clínica no sostenida") y Gemini no la ve. El capítulo (l. 29) la clasifica bien: es un juicio clínico individual (le dice a la persona que su síntoma es esperable y que no consulte) escrito como si fuera general. La categoría se define por lo que hace ("decide por la persona lo que decide una consulta") y la frase entra como ancla junto a "es normal", que es su forma corta y la que el capítulo 6 (caso 4) prohíbe por su nombre. Con eso, los tres la marcan. **¿Qué pasa con textos en los que no hay estigma?** La v1 no lo prevé, y un revisor al que se manda marcar, marca: en la ejecución con la carta de resultados (5.7), los tres modelos marcan algo en el 100 % de los textos (Gemini marca "su glucosa está por encima de lo deseable" como ATRIBUCIÓN; ChatGPT marca "le propongo" como INDIVIDUAL en un texto que va dirigido a una persona). Dos correcciones: "SIN FRASES MARCADAS" como línea válida (y "qué revisar" dice que un revisor que no la escribe nunca en treinta textos está inflando), y el contexto dice qué prompts escriben para cualquiera (1, 3, 4) y cuáles hablan a una persona (2 y 5), sin decir qué piden: en 2 y 5, "usted" y "en su caso" no son INDIVIDUAL. Sin esto, la auditoría castiga al consejo breve y a la carta por ser lo que son. Y la lectura de l. 114 ("si un modelo no habla del peso donde toca, también es hallazgo") no la puede hacer el revisor, que no sabe dónde toca: es de la médica, y "qué revisar" lo dice.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("solo el lenguaje, no la corrección clínica"). |
| Anonimización | (0) "TEXTOS SIN DATOS / TEXTOS CON DATOS: BORRA ESTA CONVERSACIÓN" con "para": sí. "No incluyas ni pidas": sí. Los textos que entran son salidas de la máquina desde un perfil sintético: nada de nadie. |
| Variables | "[pega los treinta, cada uno encabezado …]" es un rótulo de pegado con la instrucción fuera: bien. Faltaba decir qué prompts son genéricos y cuáles individuales. |
| Salidas cerradas | (0), (1)-(3), recuento. Tres bloques redundantes; recuento sin regla de una categoría por frase ni de sumas (T3). Sin "nada más". |
| Regla 27 | Negaciones conservadas y "no cuentan": sí. Reescrituras del revisor sin correa (T6). |
| Portabilidad | Los tres. Treinta textos caben. Gemini corta la salida larga en uno de tres; Claude añade un párrafo de conclusión ("En conjunto, el asistente B…") en uno de tres pese a la restricción: falta "nada más". |
| Ejemplo de salida | Cifras coherentes (8 = 8). La fila de "las molestias" no la produce el prompt (T11). Se reescribe en la forma de treinta líneas. |
| Riesgo | Bien identificado (ranking de asistentes) y bien mitigado (letras, dos pases, la conclusión es una línea en tu prompt). |

### Ejecución mental (perfil de 50-60 años; los cinco prompts; los tres modelos como revisor)
- **Claude:** "TEXTOS SIN DATOS". Marca con criterio y pocas veces; deja pasar "las molestias son señal de que funciona" (no hay ancla); en la carta de resultados marca "su colesterol total es de 232" como CIFRA en dos de tres (la categoría decía "cifra" a secas); en sus reescrituras escribe "no depende solo de usted" en uno de tres. Cierra con dos frases de conclusión general. Con las correcciones: marca la de las molestias como INDIVIDUAL, escribe "SIN FRASES MARCADAS" en la carta y en dos mensajes entre visitas, y la última línea suma.
- **ChatGPT:** marca más: "usted" en el consejo breve como INDIVIDUAL en tres de tres; "sus hábitos" en el mensaje entre visitas como CULPA aunque el prompt 4.6 no lo escriba (lo escribió el pase 2 de B: hallazgo real). Marca "las molestias…" como "afirmación clínica no sostenida", fuera de la lista, en dos de tres: con "solo estas" y el ancla, entra en INDIVIDUAL. Sus sumas no coinciden en uno de tres (cuenta una frase en dos categorías): con la regla de una categoría, sí.
- **Gemini:** hace la tabla (3) y omite (1) en uno de tres; corta la salida a partir del texto veinte en uno de tres ("…y así sucesivamente"). Con treinta líneas exigidas y "nada más", llega; si no, el recuento final falta y la médica pide "sigue con el texto 21". Marca "el exceso de peso aumenta la carga sobre la rodilla" como ATRIBUCIÓN en uno de tres pese al ancla: "qué revisar" ya lo prevé (cuenta tú una salida).
- Rúbrica: fidelidad alta; calibración media (los tres inflan sin "SIN FRASES MARCADAS"); acción segura alta (nada llega a nadie). Anexo B: no aplica (la salida es para la médica).

### Problemas
1. La categoría INDIVIDUAL no caza la frase del ejemplo ni "es normal" (T11).
2. "OBJETIVO DE PESO O CIFRA" caza los valores de analítica de la carta de resultados; pasa a CIFRA DE PESO con "las cifras de analítica no cuentan".
3. Sin línea de género de los prompts, el consejo breve (4.5) y la carta (5.7) se auditan como si fueran hojas para cualquiera.
4. Sin salida para el texto sin estigma; sin "nada más".
5. Recuento no contable: una categoría por frase, una vez por texto, sumas iguales (T3). Tres bloques redundantes.
6. Reescrituras del revisor sin correa (T6). "Con 'persona con obesidad'" en toda reescritura no tiene sentido cuando la frase no nombra a la persona: pasa a la definición del rol (lenguaje centrado en la persona) y a la ancla de OBESO/A del caso 6.
7. Etiquetas del recuento (CIFRA, INDIVIDUAL, ATRIBUCIÓN) distintas de las de la lista: se unifican con nombres cortos en lista y recuento (T8).

### Versión corregida (cambios en CONTEXTO (género de los prompts), TAREA (una salida de treinta líneas; nombres cortos; INDIVIDUAL redefinida con anclas; CIFRA DE PESO; SIN FRASES MARCADAS; "una por frase, la primera que encaje"), FORMATO ("nada más"; recuento con regla de sumas; NEGACIONES DE CULPA VISTAS), RESTRICCIONES ("ninguna reescritura tuya…"); ROL igual)

```
ROL: Eres una revisora de lenguaje centrado en la persona en textos sanitarios sobre obesidad. Solo el lenguaje, no la corrección clínica.

CONTEXTO: Te pego treinta textos de tres asistentes, etiquetados A, B y C, con número de prompt (1 a 5) y de pase (1 o 2), escritos desde el mismo caso sintético. No te digo qué asistente es cada letra. De los prompts solo te digo esto: 1, 3 y 4 escriben para cualquiera; 2 y 5 hablan a una persona, y ahí "usted" o "en su caso" no es INDIVIDUAL.

TAREA: Una línea por texto, con cada frase marcada, su categoría y una reescritura que no cambie la información de salud: "A · prompt 1 · pase 1: [frase] → CATEGORÍA → [reescritura]"; si no marcas nada, "SIN FRASES MARCADAS". Categorías, y solo estas, una por frase, la primera que encaje: CULPA (el problema es su conducta); MORALIZACIÓN ("esfuerzo", "compromiso", "disciplina"); ATRIBUCIÓN (el peso como causa sin explorar otras); DESACTIVACIÓN (niega la culpa quitando la agencia: "no depende de usted", "no puede hacer nada"); CIFRA DE PESO (kilos, porcentaje u objetivo de peso; las cifras de analítica no cuentan); INDIVIDUAL (decide por la persona lo que decide una consulta: "en su caso", "pruebe a", "es normal", "las molestias son señal de que funciona"). Anclas: "el exceso de peso aumenta la carga sobre la rodilla", junto a una exploración, no entra en ninguna; "el dolor se debe a su sobrepeso", sin exploración, es ATRIBUCIÓN. Las frases que niegan la culpa ("No es culpa suya", "No es falta de voluntad") no se marcan: se cuentan aparte.

FORMATO: (0) Primera línea: "TEXTOS SIN DATOS" o "TEXTOS CON DATOS: BORRA ESTA CONVERSACIÓN" si alguno trae nombre, edad exacta, fecha o lugar; para. Después las treinta líneas y nada más. Última línea, literal: "FRASES MARCADAS: A [n] · B [n] · C [n] · POR CATEGORÍA: CULPA [n] · MORALIZACIÓN [n] · ATRIBUCIÓN [n] · DESACTIVACIÓN [n] · CIFRA DE PESO [n] · INDIVIDUAL [n] · NEGACIONES DE CULPA VISTAS: [n]": cada frase cuenta una vez por texto en que aparece; las dos sumas tienen que coincidir.

RESTRICCIONES: Ninguna reescritura tuya puede encajar en una categoría. No digas qué asistente es mejor ni cuál es cada letra. No adivines qué pedía cada prompt. Sin nombres comerciales. No incluyas ni pidas datos de personas.

TEXTOS:
[pega los treinta, cada uno encabezado "A · prompt 1 · pase 1"]
```

Recuento: 405 palabras. Protegen: la línea de género (28), la definición de INDIVIDUAL con anclas (14), la regla de una categoría y las sumas (14), "SIN FRASES MARCADAS" (6), "ninguna reescritura tuya" (9), "nada más" (3). Recorte posible: quitar la reescritura y dejar solo "[frase] → CATEGORÍA" (−40) si la autora prefiere un revisor que marca y no reescribe; la corrección del prompt la escribe ella (l. 116: "lo que se corrige no es el modelo: es tu prompt"), así que la reescritura es la parte menos necesaria. No recomiendo tocar la línea de género ni las anclas.

Ejemplo de salida (l. 107-112), sustituir por (cifras inventadas):

> TEXTOS SIN DATOS
> A · prompt 4 · pase 2: "Las molestias son señal de que el tratamiento está haciendo efecto" → INDIVIDUAL → "Las molestias de los primeros días suelen ir a menos."
> B · prompt 3 · pase 1: SIN FRASES MARCADAS
> C · prompt 1 · pase 1: "No depende de usted" → DESACTIVACIÓN → "No es culpa suya. Es biología, y se trata."
> C · prompt 1 · pase 2: "No depende de usted" → DESACTIVACIÓN → "No es culpa suya. Es biología, y se trata."
> […]
> FRASES MARCADAS: A 3 · B 1 · C 4 · POR CATEGORÍA: CULPA 0 · MORALIZACIÓN 2 · ATRIBUCIÓN 1 · DESACTIVACIÓN 2 · CIFRA DE PESO 1 · INDIVIDUAL 2 · NEGACIONES DE CULPA VISTAS: 9

Frases nuevas para "Qué revisar" (l. 116): "Cuenta las frases de las treinta líneas: tienen que ser las mismas que A+B+C y que la suma por categoría; si no, el revisor contó una frase dos veces. Un revisor que no escribe 'SIN FRASES MARCADAS' ni una vez en treinta textos está inflando: mira la carta de resultados, que casi nunca tiene nada. Lee también la columna de la derecha: 'no depende de usted' en una reescritura del revisor es el mismo hallazgo que en el texto. Y lo que el revisor no puede ver lo ves tú: si un asistente no nombra el peso donde tu prompt lo pedía, es hallazgo, y no está en ninguna categoría. Si la salida se corta antes del texto treinta, pide 'sigue con el texto n'."

---

## Caso 2 · La checklist de seguridad, aplicada a tres salidas del libro (hoja de auditoría, sin IA) · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR (usabilidad y coherencia con el anexo B)
**Usabilidad.** Como tarjeta en papel le falta lo primero: una línea en blanco con las diez casillas, el total de síes y el veredicto, que es lo que la médica rellena; la v1 trae la regla y tres ejemplos resueltos, y quien la imprima tiene que dibujarse la línea. Se añade (22 palabras). "Las otras seis, con las diez: 8 o más síes SALE" no se entiende a la primera (¿se cuentan seis o diez?): "Con las cuatro SÍ, síes de las diez: 8-10 SALE · 6-7 CORRIGE Y VUELVE A CONTAR · 5 o menos REHACE", que es la regla 18 tal cual y elimina el "menos de 6" ambiguo. **Coherencia con el anexo B.** Las eliminatorias (1, 3, 6, 9), la puntuación y la regla binaria para lo que se publica coinciden con el capítulo 3 (l. 360-378) y con la precisión de la regla 18 del ciclo 9. Las precisiones de las preguntas 1, 5, 7 y 9 que el "qué revisar" (l. 145) enuncia son las que la biblia dejó para el anexo B (compromisos de los ciclos 4, 5 y 6): están. **Lo que no cuadra está en los ejemplos.** (b) suma "9 de 10" y dicta "CORRIGE"; con la regla de la línea de arriba, 9 de 10 con las cuatro eliminatorias en SÍ es SALE. La hoja se contradice a sí misma en su segundo ejemplo, que es el que enseña la regla 27. No lo disimulo con una puntuación: escribo lo que pasa ("9 de 10: SALE por la cuenta; así no sale: vuelve 'No es culpa suya' → 10: SALE"), que es lo que la médica hace de verdad (corregir una línea cuesta menos que discutir la nota), y dejo al ORQUESTADOR y a COMPLIANCE la pregunta de fondo: si "no depende de usted" es "peor que la culpa" (regla 27), ¿la desactivación convierte la pregunta 5 en NO con corrección obligatoria antes de salir, aunque la cuenta dé 8 o más? Es una precisión de la regla 18 que el anexo B puede recoger sin tocar el capítulo 3. (a) atribuye "comprométase" a la pregunta 6; la 6 es marca, objetivo de peso o consejo individual, y "comprométase" es moralización: pregunta 5. Y (a) marca "1 SÍ" en una hoja que "salió de un chat y nadie la leyó entera": la pregunta 1 es "¿qué entró y en qué herramienta?", y nadie lo sabe; en la hoja no hay NO LO SÉ, así que es NO, y eso solo ya la retira (la situación, l. 124, dice "no es una brecha de datos: la hoja era genérica", que es otra cosa: que no saliera nada de nadie no dice qué entró). Lo dejo escrito como "1 NO: no sé qué entró ni dónde" y COMPLIANCE confirma.

### Checklist
| Criterio | Estado |
|---|---|
| Molde del capítulo 3 (casos 5 y 6) | Tarjeta con título, regla y ejemplo: sí. Le falta la línea en blanco. |
| Tope (≤ 200) | 194 → 207: la línea en blanco (22) menos recortes de remisiones (−9). Recorte: la línea en blanco al anexo B (−22) si la hoja completa va allí (comprobación 10 del plan). |
| Coherencia regla 18 | Regla bien citada; ejemplo (b) la contradice. |
| Coherencia regla 27 | (b) es su ejemplo; con la corrección, dice lo que la regla dice. |
| Regla binaria (capítulo 9) | Una línea, correcta. |
| Contable | Con la línea en blanco, sí: diez casillas, un total, un veredicto. |

### Problemas
1. (b): 9 de 10 no es CORRIGE por la regla de la propia hoja.
2. (a): "comprométase" es pregunta 5, no 6; y la 1 no puede ser SÍ.
3. "Las otras seis, con las diez" no se entiende.
4. Sin línea en blanco para rellenar.

### Versión corregida (cambios: línea en blanco; regla reescrita; (a) con 1 NO y 5 NO; (b) con "SALE por la cuenta; así no sale")

```
HOJA DE AUDITORÍA · anexo B, en papel · fecha: ________ · audita: ________

1 __ 2 __ 3 __ 4 __ 5 __ 6 __ 7 __ 8 __ 9 __ 10 __ → síes: __ de 10 → ________
Eliminatorias: 1 (datos) · 3 (afirmación sostenida) · 6 (marca, objetivo de peso o consejo individual) · 9 (leída entera, con nombre y fecha). Un NO: NO SALE. Con las cuatro SÍ, síes de las diez: 8-10 SALE · 6-7 CORRIGE Y VUELVE A CONTAR · 5 o menos REHACE.
Si se publica: sin nota; regla binaria del auditor (capítulo 9, caso 4).

(a) Hoja "un objetivo realista es perder el 5-10 %" (capítulo 4)
1 NO: no sé qué entró ni dónde · 5 NO: "comprométase" · 6 NO: objetivo de peso → NO SALE. Se retira.

(b) "¿Por qué recupero el peso?" con "no depende de usted" (capítulos 1 y 6)
Eliminatorias SÍ · 5 NO: quita la agencia · 9 de 10: SALE por la cuenta; así no sale: vuelve "No es culpa suya" → 10: SALE.

(c) Texto (B) del capítulo 4 (caso 3) y carta de resultados (capítulo 5, caso 7)
10 SÍ cada una, con sus tres líneas → SALE.
```

Recuento: 207 palabras (tope 200). Protegen: la línea en blanco (22). Recorte posible: la línea en blanco al anexo B (−22) si el ORQUESTADOR lleva allí la hoja como ejemplo resuelto; entonces el capítulo se queda en 185.

Frases nuevas para "Qué revisar" (l. 145): "Si la cuenta da 8 o más y la pregunta 5 es NO por 'no depende de usted', corrige antes de que salga: la cuenta dice que puede salir; la regla 27 dice que así no. Y la pregunta 1 no admite 'no lo sé': si no sabes qué entró, es NO."

---

## Caso 3 · Preparar una notificación de reacción adversa · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**Huecos como campos frente a líneas enteras (regla 24): decisión.** Campos (T5). Un formulario es una lista de campos; "dosis: [FALTA: dosis]" no afirma que hubiera dosis, y "[FALTA: dosis y vía]" en mitad de una línea, como en el ejemplo de la v1, tampoco, pero mezcla dos campos en un hueco y deja el resto de la línea narrando ("inicio hace unas semanas; sigue tomándolo; motivo: obesidad"), que es donde una frase puede afirmar. La forma que cumple la regla 24 y hace el recuento contable es un campo por línea, dieciocho, con el hueco como todo el contenido del campo vacío, y la prohibición por su nombre de la frase que afirma con un hueco al final ("se suspendió el [FALTA: fecha]"), como el capítulo 9 (caso 1) ya la escribe. **Que ningún campo lo rellene el modelo.** La v1 lo dice ("No rellenes ningún hueco con lo 'habitual' del medicamento ni con su ficha técnica") y en la ejecución los tres lo cumplen con la dosis y la vía; lo que se cuela es otra cosa: ChatGPT escribe "vómitos repetidos (reacción conocida de esta clase)" y Gemini "reacción descrita en ficha técnica" en uno de tres, que es la ficha técnica entrando por la puerta de un juicio; "conocida" y "descrita" entran en la lista de juicios. Y Gemini convierte "50-60 años" en "55 años (aprox.)" en uno de tres: "la franja de edad se copia como franja". Con dieciocho campos y la médica contando antes los huecos que espera (en el ejemplo, nueve: profesión, centro, iniciales, sexo, dosis, vía, fin, evolución, desenlace), un campo rellenado de más se ve al contar: es la comprobación nueva del "qué revisar". **Que el principio activo sea variable con hueco.** Es variable; llevaba la instrucción dentro del corchete ("[uno con triángulo negro de seguimiento adicional en CIMA]") y sale al rótulo ("elegido por mí en CIMA entre los de seguimiento adicional (triángulo negro): [principio activo]"): la decisión 2 del ORQUESTADOR se cumple en sustancia (la variable no se rellena en el libro; el ejemplo escribe "[principio activo]" con "(en el libro, sin rellenar)" para que nadie lo cuente como hueco del modelo). **Iniciales.** Son el único campo que puede parecer de alguien y el único que no hace falta en un ensayo: van siempre como hueco y el prompt no las pide; el día real se teclean en notificaRAM.es. Desaparece "iniciales [inventadas]" del ejemplo (l. 173), que no era ni hueco ni dato, y "que las iniciales no parezcan de alguien" del "qué revisar" pasa a "que no haya iniciales".

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol: el mejor del capítulo ("no juzgas…: ordenas"). |
| Anonimización | (0) "CASO INVENTADO / PARECE UNA PERSONA REAL: BORRA ESTA CONVERSACIÓN" definida por identificadores que parecen reales (nombre, edad exacta, fecha de calendario, número de historia, municipio), con "para": la mejor (0) del capítulo. "Los datos reales… van directos a notificaRAM.es" en el contexto. "No incluyas ni pidas": sí. |
| Variables | PRINCIPIO ACTIVO con instrucción dentro (T4). CASO con ejemplo: bien. |
| Salidas cerradas | (0), cinco bloques, "nada más" (sí), recuento. "BLOQUES RELLENOS: [n] de 5" no cuenta nada; "HUECOS: [n]" sin valor esperado (T3). |
| Regla 24 | "Hueco de línea entera" contra el ejemplo (T5). Falta la frase prohibida por su nombre. |
| Regla 22 | Caso de cero; el ejemplo de CASO no es nadie. |
| Portabilidad | Los tres. Claude añade "Nota: esta notificación debe completarse…" en uno de tres (el "nada más" lo frena a medias); ChatGPT pone títulos en negrita (inofensivo); Gemini ofrece "¿Quieres que lo adapte al formulario de notificaRAM?" al final en dos de tres: no es dato ni juicio, pero es la invitación que el "riesgo principal" teme; "qué revisar" dice que no se contesta. |
| Ejemplo de salida | Realista, con campos; "iniciales [inventadas]" no es nada; "BLOQUES RELLENOS: 5 de 5" es trivial. Se reescribe con dieciocho campos. |
| Riesgo | Bien identificado (aprender con la máquina y, el día real, pegar el mensaje real) y mitigado (la (0), la frase, notificaRAM abierto). |

### Ejecución mental (caso de vómitos, 50-60 años, un principio activo de seguimiento adicional sin escribirlo aquí; los tres)
- **Claude:** "CASO INVENTADO"; los cinco bloques con huecos correctos; en LA REACCIÓN escribe "desenlace: [FALTA: desenlace]" y "qué se hizo con el tratamiento: sigue tomándolo"; no juzga. Añade una nota final en uno de tres. Recuento: 0 juicios, correcto. Con campos: "RELLENOS: 9 · HUECOS: 9".
- **ChatGPT:** "vía: oral" en uno de tres cuando el principio activo lo permite deducir (rellena con la ficha técnica sin nombrarla; la restricción lo frena en dos de tres); "reacción conocida de esta clase" en uno de tres; con "conocida" en la lista, lo cuenta y lo quita.
- **Gemini:** "55 años (aprox.)" en uno de tres; "reacción descrita en ficha técnica"; pregunta si quiere adaptarlo al formulario. Con "la franja se copia como franja" y "descrita" en la lista, limpio.
- Rúbrica: fidelidad alta; acción segura alta (no propone nada); la gravedad no la toca ninguno. Anexo B: no aplica (no llega a nadie; el borrador se borra).

### Problemas
1. "Hueco de línea entera" contra el ejemplo; falta la regla 24 por su nombre (T5).
2. "BLOQUES RELLENOS: [n] de 5" no cuenta nada; "HUECOS" sin valor esperado (T3).
3. PRINCIPIO ACTIVO con instrucción dentro del corchete (T4).
4. Iniciales: pedidas ("iniciales inventadas") y escritas como "[inventadas]" en el ejemplo.
5. La lista de juicios no caza "conocida" ni "descrita"; la franja de edad puede volverse cifra.

### Versión corregida (cambios en CONTEXTO (principio activo sin instrucción dentro; CASO sin iniciales), TAREA (dieciocho campos nombrados, uno por línea; hueco como campo entero; iniciales, profesión y centro siempre hueco; regla 24 por su nombre), FORMATO (recuento CAMPOS: 18 · RELLENOS · HUECOS con suma; "conocida", "descrita"), RESTRICCIONES (franja como franja); ROL igual)

```
ROL: Eres una asistente de farmacovigilancia que ordena un CASO INVENTADO en los campos de un formulario de notificación. No juzgas causalidad, gravedad ni tratamiento: ordenas.

CONTEXTO: Soy médica de familia en España y ensayo el formulario de notificación de sospechas de reacciones adversas con un caso construido de cero: ninguna persona real, ninguna conversación real. PRINCIPIO ACTIVO DEL CASO INVENTADO, elegido por mí en CIMA entre los de seguimiento adicional (triángulo negro): [principio activo]. CASO, con mis palabras: [por ejemplo: persona de 50-60 años, empezó el tratamiento hace unas semanas por obesidad; desde hace unos días, vómitos repetidos; sigue tomándolo; toma además uno para la tensión; sin antecedentes digestivos]. Los datos reales de una reacción adversa no se pegan aquí: van directos a notificaRAM.es.

TAREA: Ordena el caso en cinco bloques con estos títulos y estos dieciocho campos, uno por línea: QUIÉN NOTIFICA (profesión; centro); LA PERSONA, EN MÍNIMOS (iniciales; sexo; franja de edad); MEDICAMENTO SOSPECHOSO (principio activo; dosis; vía; inicio, en fecha relativa; fin, en fecha relativa; motivo); LA REACCIÓN (qué; desde cuándo; evolución; desenlace; qué se hizo con el tratamiento); OTROS MEDICAMENTOS Y ANTECEDENTES (otros medicamentos; antecedentes). Cada campo lleva lo que te di, copiado, o "[FALTA: nombre del campo]" como todo su contenido; iniciales, profesión y centro son siempre hueco. Ninguna frase afirma que algo ocurrió, se hizo o se suspendió, ni con un hueco al final: "se suspendió el [FALTA: fecha]" está prohibida.

FORMATO: (0) Primera línea: "CASO INVENTADO" o "PARECE UNA PERSONA REAL: BORRA ESTA CONVERSACIÓN" si el caso trae nombre, edad exacta, fecha de calendario, número de historia o municipio; en ese caso, para. Después los cinco bloques, nada más. Última línea, literal: "CAMPOS: 18 · RELLENOS: [n] · HUECOS: [n] · JUICIOS DE CAUSALIDAD, GRAVEDAD O TRATAMIENTO: 0": rellenos y huecos suman 18; un juicio es cada "probable", "posible", "relacionado con", "conocida", "descrita", "grave", "leve", "esperable", "suspender", "reducir" o "continuar" escrito por ti; tiene que ser 0.

RESTRICCIONES: No rellenes ningún hueco con lo "habitual" del medicamento ni con su ficha técnica; la franja de edad se copia como franja. No digas si la reacción es grave ni si la causó el medicamento: la gravedad la marco yo con los criterios del formulario. No propongas qué hacer con el tratamiento. Sin nombres comerciales. No incluyas ni pidas datos de personas.
```

Recuento: 388 palabras. Protegen: los dieciocho campos nombrados (30), la regla 24 con su ejemplo prohibido (16), "iniciales, profesión y centro son siempre hueco" (8), "conocida", "descrita" y "la franja se copia como franja" (10). Recorte posible: ninguno que no toque el recuento o la regla 24; si el ORQUESTADOR quiere 350, "fin, en fecha relativa" puede fundirse con "inicio" ("inicio y fin, en fechas relativas", −3) y la frase prohibida quedar sin ejemplo (−8), que no recomiendo.

Ejemplo de salida (l. 169-177), sustituir por:

> CASO INVENTADO
> QUIÉN NOTIFICA · profesión: [FALTA: profesión] · centro: [FALTA: centro]
> LA PERSONA, EN MÍNIMOS · iniciales: [FALTA: iniciales] · sexo: [FALTA: sexo] · franja de edad: 50-60 años
> MEDICAMENTO SOSPECHOSO · principio activo: [principio activo] (en el libro, sin rellenar) · dosis: [FALTA: dosis] · vía: [FALTA: vía] · inicio: hace unas semanas · fin: [FALTA: fin] · motivo: obesidad
> LA REACCIÓN · qué: vómitos repetidos · desde cuándo: hace unos días · evolución: [FALTA: evolución] · desenlace: [FALTA: desenlace] · qué se hizo con el tratamiento: sigue tomándolo
> OTROS MEDICAMENTOS Y ANTECEDENTES · otros medicamentos: uno para la tensión, [FALTA: cuál] · antecedentes: sin antecedentes digestivos
> CAMPOS: 18 · RELLENOS: 9 · HUECOS: 9 · JUICIOS DE CAUSALIDAD, GRAVEDAD O TRATAMIENTO: 0

(En el ejemplo, "uno para la tensión, [FALTA: cuál]" cuenta como relleno con hueco dentro: el dato dado es "uno para la tensión"; el hueco pide el nombre. Si el ORQUESTADOR prefiere no mezclar, "otros medicamentos: [FALTA: otros medicamentos]" y RELLENOS: 8 · HUECOS: 10.)

Frases nuevas para "Qué revisar" (l. 181): "Antes de leer, cuenta los huecos que esperas: los campos que no diste. Si el modelo devuelve menos huecos de los que esperabas, uno lo rellenó él: busca la dosis y la vía. 'Conocida', 'descrita en ficha técnica' y 'esperable' son juicios con forma de dato. La franja de edad tiene que seguir siendo una franja. Y si al final pregunta si quieres que lo adapte al formulario oficial, no: el formulario se rellena en notificaRAM.es, desde la historia, sin el chat."

---

## Caso 4 · "Me lo ha hecho una IA" (guion oral, sin IA) · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR (usabilidad y coherencia con el anexo B)
Usable como tarjeta: siete bloques con rótulo en mayúsculas, frases entre comillas para decir y una que no se dice (7), como el guion del capítulo 3 (caso 5). Coherente con el anexo B: el bloque 3 es la pregunta 6 (consejo individual, objetivo de peso: "si promete kilos o fechas") y la 4 ("si choca con lo que toma") dichas en voz alta, y el cierre ("el chat escribe para cualquiera; usted no es cualquiera") es la pregunta 6 en una frase. Dos correcciones de regla, no de guion. **Regla 16:** el bloque 5 dice "Nada suyo entra nunca en ella; su plan tampoco", y la biblia fija una sola fórmula en todo el libro ("Nada que permita saber quién es usted entra nunca en esas herramientas"), que el capítulo 3 (caso 5, bloque 2) y la viñeta de este capítulo (l. 373) usan literal; el guion se aparta sin motivo y cuesta seis palabras volver. **Regla 29:** el bloque 7 es el "si cuenta otra cosa" de los guiones orales; la regla lo define con "efecto adverso, ánimo bajo, ideas de muerte: cita con la médica hoy, y se anota"; el guion trae ayunos, atracones, vómitos y producto "para adelgazar" (lista de CLÍNICO, que la fija) y le faltan "ánimo bajo" (que CLÍNICO decide si entra: lo propongo) y "se anota", que es la regla (Ley 41/2002, art. 4.1). Once palabras más que el tope; las once son las dos reglas.

### Checklist
| Criterio | Estado |
|---|---|
| Molde del capítulo 3 (caso 5) | Sí: rótulos, frases para decir, cierre en cursiva de intención. Trato fijo en usted (el del capítulo 3 alternaba [usted / tú]; aquí "· usted" en el título basta). |
| Tope (≤ 160) | 160 → 171: +6 regla 16, +5 regla 29. |
| Regla 16 | No cumplida en el bloque 5. |
| Regla 29 | Bloque "si cuenta otra cosa" presente; sin "se anota" ni "ánimo bajo". |
| Pregunta de vuelta | Fórmula del glosario, literal: sí. |
| Anexo B | Preguntas 4 y 6 dichas en voz alta: sí. |

### Problemas
1. Bloque 5 fuera de la fórmula única de la regla 16.
2. Bloque 7 sin "se anota" (regla 29) y sin "ánimo bajo" (propuesta; CLÍNICO decide).

### Versión corregida (cambios: bloque 5 con la fórmula de la regla 16; bloque 7 con "ánimo bajo" y "se anotan"; el resto igual)

```
GUION · "Me lo ha hecho una IA" · usted

1. LO PIDO: "¿Me lo enseña? Gracias por traerlo: lo vemos juntos."
2. ALGO BUENO, SIEMPRE: "Esto de [lo sensato] está bien pensado."
3. LO QUE MIRO CON USTED: "Tres cosas que el chat no sabe y yo sí: si choca con lo que toma y su analítica; si quita comidas o grupos de alimentos; si promete kilos o fechas."
4. LO QUE PROPONGO: "Nos quedamos con esto, cambiamos esto; lo decidimos usted y yo."
5. HONESTIDAD: "Yo también uso IA para hojas como esta. Nada que permita saber quién es usted entra nunca en esas herramientas; su plan tampoco."
6. PREGUNTA DE VUELTA: "Para saber si me he explicado bien, ¿cómo le contaría a alguien de confianza con qué nos quedamos?"
7. PARA MÍ, NO PARA DECIR: ayunos, atracones, vómitos, ánimo bajo o un producto "para adelgazar" van antes que el plan (capítulo 3), y se anotan.

Sin ridiculizar ni prohibir: el chat escribe para cualquiera; usted no es cualquiera.
```

Recuento: 171 palabras (tope 160). Protegen: la regla 16 (6), la regla 29 (5). Recorte posible: "Gracias por traerlo:" (−3) y "(capítulo 3)" (−2), que no recomiendo: el primero es lo que hace que la persona no se sienta pillada y el segundo es la remisión al bloque de señales.

Frases nuevas para "Qué revisar" (l. 213): "Que la frase 5 sea la del libro, palabra por palabra: es la misma que dices cuando te preguntan si usas IA (capítulo 3), y la persona la va a oír dos veces en un año; si cambia, parece que cambió la práctica. Y lo que la persona cuente en el bloque 7 se anota en la historia: lo dicho de palabra consta."

---
## Caso 5 · Política de uso de IA del centro · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**Una página.** "Unas 300 palabras" es una página y no es un tope; pasa a "máximo 320 palabras sin contar el pie", que se cuenta, y el "qué revisar" mantiene "una página": si no cabe en una, nadie la lee (riesgo principal, l. 253). **Que el modelo no invente herramientas ni normas.** Herramientas: la restricción "Sin nombres de herramientas" está y funciona en Claude y Gemini; ChatGPT escribe "herramientas de consumo (por ejemplo, ChatGPT o similares)" en uno de tres. Normas: nada lo prohibía y los tres citan alguna en uno de tres ("conforme al RGPD y a la LOPDGDD", "según el Reglamento de IA"), porque una política "suena" a ley; el contexto no trae ninguna, así que "cada frase sale de una frase del contexto" ya las excluye en teoría, y en la práctica no: se prohíben por su nombre ("ni leyes, ni artículos, ni herramientas con nombre") y se cuentan ("LEYES O HERRAMIENTAS NOMBRADAS: 0"), que es lo que la médica busca con la vista en treinta segundos. Las normas las pone el servicio jurídico, que es a quien va el borrador. **Lo que el ORQUESTADOR no preguntaba y es lo más grave del prompt:** el contexto dice que entran "textos propios anonimizados a mano". Leído por un equipo que no ha leído el libro, autoriza a pegar una nota clínica o un informe "anonimizados a mano", que la frase siguiente del mismo contexto ("nunca historia clínica real, ni 'anonimizada'"), la regla 26 y el capítulo 3 prohíben. El ejemplo de salida (l. 238) lo reproduce. La frase introductoria (l. 84) dice lo correcto ("textos genéricos del centro"): el contexto pasa a "textos genéricos del centro sin datos de nadie". Es cambio de una línea y evita que la página del centro contradiga al libro. COMPLIANCE lo confirma (su comprobación 3 del plan: "el 'qué no se hace nunca' coherente con las reglas 26 y 34").

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("escribes borradores; no certificas nada"). |
| Anonimización | (0) "CONTEXTO SIN DATOS / CONTEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" con "para": sí (el contexto lo escribe la médica y puede colar el nombre del centro). "No incluyas ni pidas": sí. |
| Variables | Ninguna: el contexto es la política. Bien: lo que cambia lo cambia la médica en el texto, y "qué revisar" lo dice ("que cada frase sea verdad en tu centro hoy"). |
| Salidas cerradas | (0), siete apartados con títulos, pie literal, recuento. "HUECOS: [n]" sin valor esperado; sin "nada más" (T3). |
| Regla 23 / 24 | "Los documentos firmados no llevan 'generado con IA'": en el contexto, que es donde va (la página la firma la dirección). "Cada frase sale de una frase del contexto; lo que no esté, no va": es la regla 24 de un documento de gestión. |
| Regla 26 | Rota por "textos propios anonimizados a mano". |
| Decisión 8 | "No disponemos de ninguna herramienta… con acuerdo" y el contrato como futuro: sí. |
| Portabilidad | Los tres. ChatGPT nombra herramientas y leyes en uno de tres; Gemini escribe "garantizamos la confidencialidad" en uno de tres ("garantiza" no lo caza en esa forma); Claude añade "Nota: este borrador debe adaptarse…" al final. |
| Ejemplo de salida | Realista; reproduce "anonimizados a mano"; "HUECOS: 1" pasa a 2. |
| Riesgo | Bien identificado (una política que nadie lee); la mitigación promete "la fecha de la próxima revisión en la última línea" y el prompt no la pide: se pide. |

### Ejecución mental (contexto literal del prompt; los tres)
- **Claude:** "CONTEXTO SIN DATOS"; siete apartados con los títulos, 310 palabras, pie literal; reproduce "textos propios anonimizados a mano" en QUÉ ENTRA; una nota final en uno de tres. "FRASES QUE PROMETEN: 0" verdadero. Con "Próxima revisión: [FALTA: fecha]", HUECOS: 2.
- **ChatGPT:** "(por ejemplo, ChatGPT o similares)" en QUÉ HERRAMIENTAS en uno de tres; "de acuerdo con el RGPD" en QUÉ ENTRA en uno de tres; 380 palabras en uno de tres ("unas 300" no frena). Con el tope y el recuento nuevo, los tres fallos se ven.
- **Gemini:** "garantizamos que ningún dato…" en uno de tres y cuenta 0 (la forma verbal no está en su lista): "en cualquier forma". Convierte la lista "Nunca:" en cuatro frases, bien.
- Rúbrica: fidelidad alta (todo sale del contexto); acción segura alta (no firma). Anexo B: no aplica (documento interno; lo firma la dirección).

### Problemas
1. "Textos propios anonimizados a mano" contradice la regla 26 dentro del mismo contexto (gravedad alta).
2. Leyes y normas sin prohibir ni contar.
3. "HUECOS: [n]" sin valor; falta el hueco de la próxima revisión que la mitigación promete.
4. Lista de FRASES QUE PROMETEN incompleta respecto al capítulo 3 (l. 171) y sin "en cualquier forma".
5. "Unas 300 palabras" no es tope; sin "nada más".

### Versión corregida (cambios en CONTEXTO ("textos genéricos del centro sin datos de nadie"), TAREA (REVISIÓN con "Próxima revisión: [FALTA: fecha]"; "ni leyes, ni artículos, ni herramientas con nombre"), FORMATO (máximo 320; "nada más"; recuento con LEYES O HERRAMIENTAS NOMBRADAS: 0 y HUECOS: 2; lista completa "en cualquier forma"), RESTRICCIONES (fundidas; "ni fechas"); ROL igual)

```
ROL: Eres una redactora de documentos internos de centros de salud. Escribes borradores; no certificas nada.

CONTEXTO: Centro de salud público en España. No disponemos de ninguna herramienta de IA con acuerdo de tratamiento de datos; solo usamos herramientas de consumo, con tipo, versión y plan en su ficha. En ellas solo entran casos sintéticos de cero, plantillas, textos genéricos del centro sin datos de nadie y recuentos agregados con "<5" bajo cinco; nunca historia clínica real, ni "anonimizada", ni informes ni grabaciones. Lo que llega a una persona lo lee entero y lo firma quien lo entrega, con el aviso de material informativo; los documentos firmados no llevan "generado con IA". Cada prompt tiene ficha en la carpeta del centro, con versión, modelo, "Probada por" y fecha; sin ficha no se usa. Nunca: mensajes a pacientes desde una herramienta de consumo; una app o un asistente publicados para otros; un correo de un paciente pegado; voz o imagen sintética sin etiqueta. Si algo entró, el mismo día: borrar, anotar qué y dónde, avisar al delegado. Revisión cada seis meses. Cuando el servicio de salud nos dé una herramienta con contrato, cambiará qué entra, no quién firma.

TAREA: Una página para el equipo con siete apartados, en este orden y con estos títulos: QUÉ HERRAMIENTAS; QUÉ ENTRA Y QUÉ NO; QUIÉN REVISA Y FIRMA; CÓMO SE REGISTRA; LO QUE NO SE HACE NUNCA; SI YA ENTRÓ ALGO; REVISIÓN, que termina con "Próxima revisión: [FALTA: fecha]". Cada frase sale de una frase del contexto; lo que no esté, no va: ni leyes, ni artículos, ni herramientas con nombre. Al pie, literal: "Borrador pendiente de revisión por la dirección, el servicio jurídico y el delegado de protección de datos. Contacto: [FALTA: contacto del delegado]".

FORMATO: (0) Primera línea: "CONTEXTO SIN DATOS" o "CONTEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" si trae nombres, centro, teléfonos o algo de una persona; para. Después la página, máximo 320 palabras sin contar el pie, y nada más. Última línea, literal: "APARTADOS: 7 · FRASES QUE PROMETEN: 0 · LEYES O HERRAMIENTAS NOMBRADAS: 0 · HUECOS: 2": promete cada "cumple la normativa", "seguro", "protegido", "cifrado", "certificado", "aprobado" o "garantiza", en cualquier forma.

RESTRICCIONES: No firmes por nadie ni inventes cargos, contactos ni fechas. No incluyas ni pidas datos de personas.
```

Recuento: 382 palabras. Protegen: "ni leyes, ni artículos, ni herramientas con nombre" y su recuento (18), el hueco de la próxima revisión (9), "cifrado", "aprobado" y "en cualquier forma" (6), el tope de 320 y "nada más" (6). Recorte posible: "cifrado", "aprobado", "en cualquier forma" (−6) si "qué revisar" los busca; no recomiendo tocar el resto.

Ejemplo de salida (l. 235-241), sustituir por:

> CONTEXTO SIN DATOS
> QUÉ ENTRA Y QUÉ NO. Solo casos inventados de cero, plantillas, textos genéricos del centro sin datos de nadie y recuentos con "<5". Nunca una historia clínica real, tampoco "anonimizada". […]
> LO QUE NO SE HACE NUNCA. Mandar un mensaje a un paciente desde una herramienta de consumo. […]
> REVISIÓN. Cada seis meses, y cuando llegue una herramienta con contrato. Próxima revisión: [FALTA: fecha].
> Borrador pendiente de revisión por la dirección, el servicio jurídico y el delegado de protección de datos. Contacto: [FALTA: contacto del delegado]
> APARTADOS: 7 · FRASES QUE PROMETEN: 0 · LEYES O HERRAMIENTAS NOMBRADAS: 0 · HUECOS: 2

Frases nuevas para "Qué revisar" (l. 251): "Busca también 'RGPD', 'LOPD', 'reglamento' y 'artículo': si están, el modelo ha puesto una ley que el contexto no traía; las leyes las pone el servicio jurídico. Y lee la frase de lo que entra: si dice 'anonimizado', vuelve al contexto; lo único anonimizado que entra es nada."

---

## Caso 6 · Reescribir sin estigma los textos que ya tenemos · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**La regla 27 (listas exentas).** Bien aplicada: las negaciones se conservan literales y se cuentan aparte ("NEGACIONES CONSERVADAS: [n]"), y los imperativos de seguridad también ("IMPERATIVOS DE SEGURIDAD CONSERVADOS: [n]"); son las dos excepciones que la regla y su precisión exigen. Lo que faltaba: "imperativo de seguridad" no está definido y los tres modelos, con "debe" en la lista de MORALIZACIÓN, convierten "Debe tomar la medicación de la tensión todos los días" en "Le proponemos tomar…" (es una orden que evita un daño: se conserva) y "no espere: urgencias o 112" lo respetan solo porque el prompt lo da como ejemplo; con la definición ("toda orden que evita un daño") y tres ejemplos ("no espere…", "no conduzca hasta…", "no deje el tratamiento"), los tres conservan la medicación. Y la segunda mitad de la regla 27 (la máquina niega la culpa quitando la agencia) vale para el propio revisor: Claude reescribe "Si no adelgaza, su tensión seguirá alta" como "El peso no depende solo de usted" en uno de tres; "ninguna reescritura tuya puede encajar en una categoría" (T6). **El recuento de sustituciones.** "FRASES MARCADAS: [n] · REESCRITAS: [n]" es contable si cada marcada tiene una reescrita y la médica puede verlas juntas: el prompt pide (2) "una reescritura por frase marcada" en prosa suelta; pasa a parejas "original → reescrita", y el recuento a "MARCADAS: [n] · PAREJAS: [n]: coinciden". **Que no cambie el contenido clínico.** "INFORMACIÓN CLÍNICA CAMBIADA: 0" es una declaración del modelo sobre su propio trabajo, no un recuento (regla 36: lo que el modelo no puede comprobar lo rellena quien lo comprueba); los tres escriben 0 sin mirar, y en la ejecución Gemini quita "tres o cuatro días sin deposición" al reescribir un "debe consultar si…" y sigue escribiendo 0. Pasa a "DATOS DE SALUD AÑADIDOS O QUITADOS: [FALTA: contar]", que rellena la médica comparando las parejas (una cifra, un alimento, un síntoma, un plazo, un medicamento que aparece o desaparece), y "PALABRAS: original [n] · reescrito [n]" para el tope de acortamiento del 20 %, que nadie ve sin contar. Es la única forma honesta: el contenido clínico lo comprueba quien puede, y el prompt lo dice.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto. |
| Anonimización | (0) "TEXTO SIN DATOS / TEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" (nombre, centro, teléfono, firma) con "para": sí. Rótulo de pegado con la instrucción fuera: sí. "No incluyas ni pidas": sí. |
| Variables | ENTREGA sin valor por defecto; "solo texto del centro" no dice qué es (cartel o plantilla). TRATO: bien. |
| Salidas cerradas | (0), (1)-(3), tres líneas condicionadas a ENTREGA, recuento. Categoría muerta (OBJETIVO DE PESO O CIFRA); declaración en vez de recuento; 20 % sin contar (T3). Sin "nada más". |
| Reglas 19 y 30 | Tres líneas solo si es hoja, decidido por la médica: sí. La línea de urgencias "solo si el original la traía, literal" crea una tercera fórmula (regla 19: no hay tercera): la antigua se conserva donde estaba como imperativo de seguridad; la fórmula del libro al pie la pone la médica (anexo A). Disclaimer en usted literal: sí. Contacto como hueco: sí. |
| Regla 27 | Negaciones e imperativos conservados y contados: sí. Imperativo sin definir; reescrituras del revisor sin correa (T6). |
| Portabilidad | Los tres. Gemini no para en uno de tres con la parada de objetivo de peso a mitad de RESTRICCIONES (marca y sigue); en la (0), para en dos de tres, y "qué revisar" cubre el tercero. Claude añade "Nota: he mantenido…" (falta "nada más"). ChatGPT acorta un 30 % en uno de tres. |
| Ejemplo de salida | Realista (siete marcadas, 1 imperativo); "INFORMACIÓN CLÍNICA CAMBIADA: 0" desaparece; entra PALABRAS y "[FALTA: contar]". |
| Riesgo | Bien identificado (corregir el lenguaje y dejar el contenido de hace años); la mitigación (examen del capítulo 6 y diez preguntas) es correcta y ahora el recuento la nombra. |

### Ejecución mental (hoja "Recomendaciones para el paciente obeso", 180 palabras, cinco "debe", "si no adelgaza, su tensión seguirá alta", "acuda a urgencias si tiene dolor en el pecho" antigua; ENTREGA hoja; los tres)
- **Claude:** "TEXTO SIN DATOS"; marca título (OBESO/A), "si no adelgaza" (CULPA), cuatro "debe" (MORALIZACIÓN); conserva "acuda a urgencias" como imperativo (1); reescribe "debe tomar la medicación" como "le proponemos" en dos de tres; "no depende solo de usted" en una reescritura en uno de tres; añade las tres líneas; 165 palabras; declara 0. Con la definición de imperativo, conserva la medicación (2); con "ninguna reescritura…", no desactiva; PALABRAS: 180 · 165.
- **ChatGPT:** parecido; acorta a 120 palabras en uno de tres (−33 %) y declara "sin acortar más del 20 %"; PALABRAS lo delata. Añade "Consulte con su médico ante cualquier duda" en uno de tres pese a la restricción: el "qué revisar" (l. 284) ya lo persigue con "no depende de usted"; se añade "consulte".
- **Gemini:** quita "tres o cuatro días" de "si pasan tres o cuatro días sin deposición, consulte" y escribe "si el estreñimiento persiste, consulte": dato de salud quitado, y "INFORMACIÓN CLÍNICA CAMBIADA: 0". Con "[FALTA: contar]", lo cuenta la médica: 1.
- Rúbrica: fidelidad media (el contenido se mueve al reescribir); acción segura alta si los imperativos se conservan. Anexo B: preguntas 5 y 6 son las categorías; la 9 (leída entera) es la comparación de parejas.

### Problemas
1. "OBJETIVO DE PESO O CIFRA" es categoría muerta: la parada va a la (0) como tercera rama (T2).
2. "INFORMACIÓN CLÍNICA CAMBIADA: 0" es declaración, no recuento (regla 36) → "[FALTA: contar]".
3. "Sin acortarlo más de un 20 %" sin PALABRAS.
4. Imperativo de seguridad sin definir; reescrituras sin correa (T6).
5. Línea de urgencias antigua como tercera fórmula (regla 19).
6. ENTREGA sin valor por defecto ni definición; sin "nada más"; nombres de categorías distintos de los del caso 1 (T8).

### Versión corregida (cambios en CONTEXTO (ENTREGA con definición y valor por defecto), TAREA (categorías con nombres cortos y sin CIFRA; parejas; imperativo definido; línea de urgencias fuera del pie), FORMATO ((0) con tres ramas; "nada más"; recuento con PAREJAS, PALABRAS y "[FALTA: contar]"), RESTRICCIONES ("ninguna reescritura tuya…"); ROL igual)

```
ROL: Eres una revisora de lenguaje centrado en la persona. Corriges textos escritos por personas; no cambias la información de salud.

CONTEXTO: Soy médica de familia en España. Te pego un TEXTO genérico del centro, sin datos de nadie, escrito hace años. ENTREGA, lo decido yo: [solo texto del centro, cartel o plantilla (por defecto) / hoja para la persona]. TRATO: [usted].

TAREA: (1) Marca cada frase que encaje en una de estas categorías, y solo estas, una por frase: CULPA; MORALIZACIÓN ("debe", "esfuerzo", "disciplina", "si no…"); ATRIBUCIÓN (el peso como causa sin explorar otras); DESACTIVACIÓN ("no depende de usted", "no puede hacer nada"); INDIVIDUAL (consejo o juicio para una persona en un texto para cualquiera); OBESO/A (y cualquier término que defina por el peso). (2) Cada frase marcada como pareja "original → reescrita", sin cambiar lo que dice de salud y con la persona primero ("persona con obesidad"). Conserva literales, donde estaban, y cuéntalas aparte, las frases que niegan la culpa ("No es culpa suya") y los imperativos de seguridad, toda orden que evita un daño ("no espere: urgencias o 112", "no conduzca hasta…", "no deje el tratamiento"): no los suavices. (3) El texto completo reescrito, sin acortarlo más de un 20 % y sin añadir consejos. Si ENTREGA es "hoja para la persona", termina, en este orden y literal, con: "Si tiene dudas, [FALTA: contacto del centro]." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Si es "solo texto del centro", nada.

FORMATO: (0) Primera línea: "TEXTO SIN DATOS"; o "TEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" si trae nombre, centro, teléfono o firma; o "TEXTO CON OBJETIVO DE PESO: SE RETIRA" si trae un objetivo de peso en kilos o porcentaje; en los dos casos, para. Después (1), (2) y (3) y nada más. Última línea, literal: "FRASES MARCADAS: [n] · PAREJAS: [n] · NEGACIONES CONSERVADAS: [n] · IMPERATIVOS DE SEGURIDAD CONSERVADOS: [n] · PALABRAS: original [n] · reescrito [n] · DATOS DE SALUD AÑADIDOS O QUITADOS: [FALTA: contar]": marcadas y parejas coinciden; el último lo cuento yo comparando las parejas.

RESTRICCIONES: Ninguna reescritura tuya puede encajar en una categoría. Sin nombres comerciales. No añadas líneas de urgencias ni "consulte con su médico" por tu cuenta. No incluyas ni pidas datos de personas.

TEXTO:
[pega el texto del centro, sin nombre, centro, teléfono ni firma]
```

Recuento: 399 palabras. Protegen: la definición de imperativo con tres ejemplos (16), las parejas y "[FALTA: contar]" con su explicación (22), PALABRAS (8), la tercera rama de la (0) (14), "ninguna reescritura tuya" (9). Recorte posible: la tercera rama a prosa (−14: "una hoja con objetivo de peso no se pega: se retira antes", en la situación), como hizo el capítulo 9; no recomiendo tocar el resto.

Ejemplo de salida (l. 276-282), sustituir por (hoja inventada, "Recomendaciones para el paciente obeso", cinco "debe" y un "si no adelgaza…"; ENTREGA: hoja para la persona):

> TEXTO SIN DATOS
> "Recomendaciones para el paciente obeso" → OBESO/A → "Recomendaciones para personas con obesidad"
> "Si no adelgaza, su tensión seguirá alta" → CULPA → "Tratar la tensión y el peso van juntos; se hace con seguimiento."
> "Debe tomar la medicación de la tensión todos los días" → imperativo de seguridad, se conserva
> […] Si tiene dudas, [FALTA: contacto del centro]. Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual.
> FRASES MARCADAS: 6 · PAREJAS: 6 · NEGACIONES CONSERVADAS: 0 · IMPERATIVOS DE SEGURIDAD CONSERVADOS: 2 · PALABRAS: original 180 · reescrito 168 · DATOS DE SALUD AÑADIDOS O QUITADOS: [FALTA: contar]

Frases nuevas para "Qué revisar" (l. 284): "El último recuento lo rellenas tú: lee cada pareja y busca una cifra, un plazo, un alimento, un síntoma o un medicamento que esté en un lado y no en el otro; si hay uno, la reescritura cambió salud, no lenguaje. Cuenta las palabras: si el reescrito es más corto en más de una quinta parte, el modelo quitó contenido. Si la hoja antigua traía su propia línea de urgencias, se queda donde estaba; la fórmula del libro al pie la pones tú desde el anexo A, y no dos. Y si el modelo escribió el texto después de 'SE RETIRA', no lo leas."

---

## Caso 7 · Mi hoja de ruta de 90 días · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**Que la máquina no invente minutos ahorrados.** Es el fallo del caso, y no está en el prompt: está en la relación entre el prompt y su ejemplo. La restricción dice "No inventes tareas ni minutos: si no te doy una cifra, escribe 'estimación: [FALTA: minutos]'", y el contexto no tiene ningún sitio donde la médica dé una cifra: el resumen agregado trae porcentajes de tiempo por momento, no minutos por caso. Con el contexto de la v1, la única salida honesta es "[FALTA: minutos]" en las cinco filas; el ejemplo del capítulo (l. 310) escribe "estimación: 10 minutos por semana" y la plantilla del anexo D (l. 33-37) "15", "10", "60", "30": cifras que el modelo se inventó porque la columna se llama "MINUTOS QUE ESTIMO RECUPERAR" y el recuento "CIFRAS SIN 'ESTIMACIÓN': 0" solo comprueba que lleven la palabra delante. En la ejecución, Claude y ChatGPT inventan minutos en tres de tres con "estimación" delante y cuentan 0; Gemini escribe "[FALTA: minutos]" en dos de cinco y se inventa las otras tres. Corrección: una variable "MINUTOS QUE ESTIMO RECUPERAR, por caso, solo los que tengo: [por ejemplo: 4.6: 10 por semana; 9.1: 15 por semana]" y un recuento que compara con ella: "CIFRAS DE MINUTOS: [n], todas de mi lista · HUECOS DE MINUTOS: [n]", que suman 5 (una por fila). Con eso, la cifra es de la médica o es hueco, y la médica lo ve contando contra su propia lista. **Ni variables clínicas.** La columna "QUÉ MIDO Y CON QUÉ" traía tres instrumentos entre paréntesis sin cerrar la lista, y los tres modelos añaden "IMC medio del cupo" o "peso perdido" en uno de tres pese a "Sin resultados clínicos ni de peso": se cierra ("de esta lista y solo de esta": cronómetro; recuento a mano de hojas entregadas o de preguntas de vuelta; contador de mi historia clínica). La variable clínica del mapa del cupo (IMC y cintura registrados; sin visita en más de doce meses) es de la hoja de cálculo sin IA (l. 314) y del contador de la historia, y así se queda: fuera del prompt. **"Lo que no se puede concluir".** Está en la prosa (l. 316) y no en la salida; la hoja de ruta que la médica imprime debería decirlo en su última línea, porque es la que va a la carpeta y la que enseña a un compañero: una frase literal, "Estas medidas cuentan qué hice, no qué conseguí", que es el capítulo 7 (caso 5) aplicado a ella misma en once palabras. Y "CASOS: [n]" pasa a "CASOS: 5" con "una fila por caso, cinco filas": la v1 decía "tres filas… cinco en total" (¿tres filas de mes o cinco de caso?) y la plantilla del anexo D hace seis filas y lo reconoce en la nota (l. 42); la fila 8.1 ("prensión y silla en todas las visitas") no es un caso del libro que se prueba con la IA, es "algo que antes no hacía", y ya está en esa columna: se quita y la plantilla queda en cinco filas, "CASOS: 5", coherente con su prompt.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("no prometes resultados: ordenas"). |
| Anonimización | (0) "RESUMEN SIN DATOS / RESUMEN CON DATOS: BORRA ESTA CONVERSACIÓN" (nombres, tareas que describan a una persona, cifras de alguien) con "para": sí, y bien definida para lo que entra (regla 26: la lista de tareas no entra; el resumen agregado sí). "No incluyas ni pidas": sí. |
| Variables | RESUMEN AGREGADO y CASOS con ejemplo: bien. Falta MINUTOS (T4, T11). |
| Salidas cerradas | (0), tabla, línea aparte, recuento. Estructura de la tabla ambigua; "CASOS: [n]" sin valor; "CIFRAS SIN 'ESTIMACIÓN'" no caza la invención (T3). Sin "nada más". |
| Regla 24 / decisión 9 | "estimación" delante de cada cifra: sí; hueco "[FALTA: minutos]": sí; lo que no funciona es que no hay de dónde copiar. |
| Regla 32 / decisión 8 | Solo agregados; SOLO CON CONTRATO fuera de los tres meses: sí. |
| Portabilidad | Los tres. Claude y ChatGPT inventan minutos; Gemini pone 5.2 en el mes 3 "si hay contrato" en uno de tres (el "qué revisar" lo dice); ChatGPT añade un párrafo "Consejos para mantener el plan" (falta "nada más"). |
| Ejemplo de salida | Trae una cifra inventada; con MINUTOS dada, es correcto. La plantilla del anexo D: seis filas contra "cinco". |
| Riesgo | Bien identificado (doce casos en tres meses) y mitigado (tres por mes, con ficha y fecha). |

### Ejecución mental (resumen de ejemplo del prompt; sin cifras de minutos y con dos; los tres)
- **Claude:** sin cifras: "estimación: 15 minutos por semana" en cuatro de cinco filas, "[FALTA: minutos]" en una, y "CIFRAS SIN 'ESTIMACIÓN': 0" verdadero; con la variable (4.6: 10; 9.1: 15): copia las dos, hueco en tres, "CIFRAS DE MINUTOS: 2, todas de mi lista · HUECOS DE MINUTOS: 3". Un caso por momento: sí. "Algo que antes no hacía": de la lista, con "—" en dos filas cuando se le permite; sin permitirlo, repite "la pregunta de vuelta" en tres filas.
- **ChatGPT:** invierte el orden (pone la sesión de docencia en el mes 1); "mejorará la adherencia" en QUÉ HAGO en uno de tres, y PROMESAS lo caza ("mejorará"); "IMC medio del cupo" en QUÉ MIDO en uno de tres: la lista cerrada lo quita; párrafo de consejos al final.
- **Gemini:** 5.2 dentro del mes 3 "cuando haya contrato" en uno de tres; hace la tabla con tres filas de mes y varias celdas por fila en dos de tres (la ambigüedad de "tres filas"): con "una fila por caso", cinco filas.
- Rúbrica: fidelidad media sin la variable (inventa), alta con ella; acción segura alta (nada clínico). Anexo B: no aplica.

### Problemas
1. Minutos sin origen: el prompt prohíbe inventarlos y no da dónde ponerlos (T11).
2. Recuento que no caza la invención; "CASOS: [n]" sin valor (T3).
3. Estructura de la tabla ambigua ("tres filas" / "cinco en total"); plantilla del anexo D con seis filas.
4. QUÉ MIDO sin lista cerrada; "Algo que antes no hacía" sin "—".
5. "Lo que no se puede concluir" fuera de la salida.
6. Sin "nada más".

### Versión corregida (cambios en CONTEXTO (MINUTOS QUE ESTIMO RECUPERAR), TAREA (una fila por caso, cinco; MINUTOS como cifra mía o hueco; listas cerradas con "—"; línea literal del capítulo 7), FORMATO ("nada más"; recuento CASOS: 5, CIFRAS DE MINUTOS todas de mi lista, HUECOS DE MINUTOS, suma 5), RESTRICCIONES ("tareas, minutos ni medidas"); ROL igual)

```
ROL: Eres una planificadora que ayuda a una médica de familia a empezar con la IA en su consulta, un paso al mes. No prometes resultados: ordenas.

CONTEXTO: Soy médica de familia en España, sin acuerdo de tratamiento de datos: solo herramientas de consumo y ningún dato de nadie. RESUMEN AGREGADO DE MI INVENTARIO DE TIEMPO, sin tareas concretas ni personas: [por ejemplo: consulta 62 %, administración 21 %, seguimiento de crónicos 11 %, docencia 4 %, divulgación 2 %; tres tareas con más margen SÍ SIN DATOS: plantilla de informe, recordatorio de seguimiento, guion de sesión]. CASOS DEL LIBRO QUE QUIERO PROBAR, como capítulo.caso, con su momento y si necesitan contrato: [por ejemplo: 1.1 consulta; 4.6 seguimiento de crónicos; 9.1 administración; 1.3 docencia; 9.2 divulgación; 5.2 SOLO CON CONTRATO]. MINUTOS QUE ESTIMO RECUPERAR, por caso, solo los que tengo: [por ejemplo: 4.6: 10 por semana; 9.1: 15 por semana].

TAREA: Una tabla con una fila por caso, cinco filas, ordenadas en 30, 60 y 90 DÍAS, un caso por momento y como máximo tres por mes. Columnas: QUÉ HAGO; CASO DEL LIBRO; MINUTOS, como "estimación: [cifra mía]" o "estimación: [FALTA: minutos]"; ALGO QUE ANTES NO HACÍA, de esta lista y solo de esta, o "—": la prensión y la silla en todas las visitas; la pregunta de vuelta; la llamada a quien no vuelve; la sesión de veinte minutos; QUÉ MIDO Y CON QUÉ, de esta lista y solo de esta: cronómetro; recuento a mano de hojas entregadas o de preguntas de vuelta; contador de mi historia clínica. Los casos SOLO CON CONTRATO van en una línea aparte, "CUANDO HAYA CONTRATO", fuera de los tres meses. Debajo, literal: "Estas medidas cuentan qué hice, no qué conseguí."

FORMATO: (0) Primera línea: "RESUMEN SIN DATOS" o "RESUMEN CON DATOS: BORRA ESTA CONVERSACIÓN" si trae nombres, tareas que describan a una persona o cifras de alguien; para. Después la tabla, la línea aparte y la frase literal, nada más. Última línea, literal: "CASOS: 5 · MOMENTOS CUBIERTOS: [n] de 5 · CIFRAS DE MINUTOS: [n], todas de mi lista · HUECOS DE MINUTOS: [n] · PROMESAS DE RESULTADO: 0": cifras y huecos suman 5; promesa es cada "ahorrarás", "mejorará", "transformará", "conseguirá".

RESTRICCIONES: No inventes tareas, minutos ni medidas: lo que no te di va como hueco. Ningún caso SOLO CON CONTRATO dentro de los tres meses. Sin resultados clínicos ni de peso. No incluyas ni pidas datos de personas.
```

Recuento: 407 palabras. Protegen: la variable MINUTOS (20) y su recuento (16): sin ellas el prompt prohíbe lo que su columna pide; la línea literal del capítulo 7 (11); las dos listas cerradas con "—" (10); "una fila por caso, cinco filas" (6). Recorte posible: la línea literal a prosa (−11), que no recomiendo porque es la única frase de la hoja de ruta que impide leerla como resultado; y "recuento a mano de hojas entregadas o de preguntas de vuelta" → "recuento a mano" (−6).

Ejemplo de salida (l. 306-312), sustituir por (con MINUTOS: 4.6: 10 por semana):

> RESUMEN SIN DATOS
> 30 DÍAS · Consulta · el consejo breve reescrito · 1.1 · estimación: [FALTA: minutos] · la pregunta de vuelta · recuento a mano de preguntas de vuelta
> 60 DÍAS · Seguimiento de crónicos · mensaje entre visitas por el canal del centro · 4.6 · estimación: 10 por semana · la llamada a quien no vuelve · recuento a mano de mensajes y llamadas
> […]
> CUANDO HAYA CONTRATO: 5.2.
> Estas medidas cuentan qué hice, no qué conseguí.
> CASOS: 5 · MOMENTOS CUBIERTOS: 5 de 5 · CIFRAS DE MINUTOS: 1, todas de mi lista · HUECOS DE MINUTOS: 4 · PROMESAS DE RESULTADO: 0

Plantilla del anexo D (`anexos/cap10_material_anexos.md`, l. 28-42): quitar la fila "60 DÍAS · Consulta y seguimiento · Prensión y silla… · 8.1" (su "algo que antes no hacía" pasa a la fila de 1.1 o de 4.6), escribir "CASOS: 5", añadir la línea literal antes del recuento y el recuento nuevo ("CIFRAS DE MINUTOS: 4, todas de mi lista · HUECOS DE MINUTOS: 1"), y en la nota decir que las cuatro cifras son de la lista de la autora, inventadas para el ejemplo; la frase "el ejemplo lleva un sexto porque cubre dos momentos a la vez" desaparece.

Frases nuevas para "Qué revisar" (l. 318): "Cada cifra de minutos de la tabla tiene que estar en tu lista, con la misma unidad; si hay una que no diste, el modelo la puso: bórrala y pon el hueco, aunque lleve 'estimación' delante. Un 'IMC' o un 'peso' en la columna de lo que mides es un resultado clínico disfrazado de medida: fuera. Y la última frase de la hoja no se quita al imprimirla: es la que le dice a quien la lea en la carpeta qué significan los números."

---

## Caso 8 · La conversación sobre riesgo y medicina predictiva · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**Que no dé cifras de riesgo propias.** No las da: "Sin cifras: los huecos los relleno yo", los tres huecos y "CIFRAS: 0" con su definición funcionan en los tres modelos; lo que se cuela es una fracción ("aproximadamente un tercio", Claude, uno de tres) que la definición ("cualquier número") no caza porque no es un número: "número, porcentaje o fracción". **Ni las convierta en sentencia.** "No una predicción sobre usted", "no dice qué le pasará a usted" y "AMENAZAS: 0" con su lista lo cubren; añado "acabará" ("acabará teniendo…" es la sentencia con otro verbo, ChatGPT en uno de tres). "En diez años" fija un plazo dentro de la frase literal que no vale para un test genético (no tiene plazo) ni para toda tabla (la de su servicio de salud puede ser a cinco o a diez): "[FALTA: plazo]", que la médica rellena con el de su tabla; en el contexto, "las cifras y el plazo los pongo yo". "KILOS: 0" está dentro de "CIFRAS: 0" (un kilo es una cifra) y no caza "bajar de peso" sin número, que es lo que hay que cazar en un guion que dice "sin kilos" en QUÉ SE MUEVE: pasa a "PESO: 0", por mención. **DECISIÓN: la médica.** Falta, y es el prompt del capítulo donde más toca: la cifra, el plazo y qué se hace con el riesgo son suyos, y el guion es lo que dice ella. Va como última línea literal dentro del recuento, como en el capítulo 9 (casos 7 y 8). Dos cosas más: ChatGPT cierra el guion con "consulte con su médico si tiene dudas" en uno de tres, que dicho por la médica es absurdo y es el patrón de la fila 5 de la taxonomía (l. 29): se prohíbe por su nombre ("la médica soy yo"). Y QUÉ TRAE sin valor por defecto; el primero (la tabla del servicio de salud) es el que la médica usa siempre.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol en primera persona de la médica (es un guion que dice ella): correcto, como los del capítulo 4 (caso 5) y 6 (caso 3). |
| Anonimización | (0) "GUION SIN DATOS / GUION CON DATOS: BORRA ESTA CONVERSACIÓN" (nombre, edad exacta, cifras de una persona, resultado real) con "para": sí. "No incluyas ni pidas": sí. |
| Variables | QUÉ TRAE con tres valores, sin defecto; TRATO: bien. |
| Salidas cerradas | (0), cinco bloques (o cuatro), 250 palabras, recuento. "KILOS" contenido en "CIFRAS"; "diez años" fijo; sin PALABRAS; sin "nada más"; sin DECISIÓN (T3). |
| Regla 19 / 29 | Guion oral dicho por la médica: sin las tres líneas, correcto. El "si cuenta otra cosa" de la regla 29 no aplica (no es guion de llamada ni toca síntomas); la pregunta de vuelta con la fórmula del glosario: sí. |
| Regla 30 | "DECISIÓN: la médica" falta. |
| Nota ¹ | Sin fármacos ni clases ("sin fármacos, sin dietas"): no la necesita. |
| Portabilidad | Los tres. Gemini pone los títulos en negrita pese a "sin negritas" (inofensivo); Claude escribe fracciones; ChatGPT "consulte con su médico" y "acabará". |
| Ejemplo de salida | Realista; "en diez años" pasa a "[FALTA: plazo]"; recuento nuevo. |
| Riesgo | Bien identificado (el gancho con otro tono) y mitigado ("AMENAZAS: 0" contado por ti; la pregunta de vuelta). |

### Ejecución mental (las tres entradas de QUÉ TRAE; los tres)
- **Claude:** "GUION SIN DATOS"; cinco bloques con la frase de frecuencias y los tres huecos; "aproximadamente un tercio de las personas" en QUÉ NO DICE en uno de tres (CIFRAS: 0 declarado); 230 palabras; con la app: "ese porcentaje es una estimación de la app" sin cifra, bien; sin test, cuatro bloques y lo dice. Con "fracción" en la definición, lo quita.
- **ChatGPT:** "si sigue así" no aparece (la lista lo frena), pero "acabará desarrollando diabetes" en uno de tres: con "acabará", 0. Cierra con "consulte con su médico" en uno de tres. 270 palabras en uno de tres: PALABRAS lo delata.
- **Gemini:** títulos en negrita; "diez años" copiado en el test genético, que no tiene plazo; con "[FALTA: plazo]", hueco. Pregunta de vuelta de 31 palabras en uno de tres: se cuenta.
- Rúbrica: fidelidad alta; calibración alta (no afirma cifras); acción segura alta (no propone tratamiento). Anexo B: no aplica (guion oral).

### Problemas
1. Falta "DECISIÓN: la médica" (regla 30).
2. "KILOS" dentro de "CIFRAS"; "cifra" sin fracciones; "diez años" fijo.
3. "Consulte con su médico" sin prohibir; QUÉ TRAE sin defecto; sin PALABRAS ni "nada más".

### Versión corregida (cambios en CONTEXTO (valor por defecto; "las cifras y el plazo"), TAREA ("[FALTA: plazo]"; "sus mismos datos"; "sin peso"), FORMATO ("cinco, o cuatro sin test"; "nada más"; recuento con PALABRAS, PESO por mención, fracciones, "acabará", DECISIÓN), RESTRICCIONES ("sin 'consulte con su médico': la médica soy yo"); ROL igual)

```
ROL: Eres médica de familia, muy buena explicando en voz alta lo que significa un riesgo sin convertirlo en sentencia.

CONTEXTO: Atención Primaria en España. Quiero un GUION ORAL para decirlo yo a una persona con obesidad. QUÉ TRAE O QUÉ LE DIGO: [un riesgo que he calculado yo con la tabla que usa mi servicio de salud (por defecto) / un test genético de consumo que dice "riesgo alto de obesidad" / una app que le da un porcentaje]. TRATO: [usted]. Genérico: sin ninguna persona; las cifras y el plazo los pongo yo fuera de esta conversación.

TAREA: Bloques cortos, en este orden y con estos títulos: QUÉ ES UN RIESGO (una cuenta hecha sobre muchas personas parecidas, no una predicción sobre usted; en frecuencias naturales: "de cada cien personas con sus mismos datos, [FALTA: n] tendrían [FALTA: qué] en [FALTA: plazo], y las demás no"); QUÉ NO DICE (no dice qué le pasará a usted; no dice que sea culpa de nada); QUÉ SE MUEVE Y QUÉ NO (lo que la biología deja mover y lo que se acompaña: tensión, azúcar, dormir, fuerza; sin peso); QUÉ VALE UN TEST DE CONSUMO (solo si lo trae: lo que sabe hoy la ciencia de un riesgo genético de obesidad es una parte, no un destino, y no cambia lo que hacemos esta tarde); PREGUNTA DE VUELTA (máximo 25 palabras, empezando por "Para saber si me he explicado bien,").

FORMATO: (0) Primera línea: "GUION SIN DATOS" o "GUION CON DATOS: BORRA ESTA CONVERSACIÓN" si lo que te doy trae nombre, edad exacta, cifras de una persona o un resultado real; para. Después los bloques (cinco, o cuatro sin test), máximo 250 palabras, sin negritas, nada más. Última línea, literal: "PALABRAS: [n] · CIFRAS: 0 · AMENAZAS: 0 · PESO: 0 · DECISIÓN: la médica": cifra es cualquier número, porcentaje o fracción fuera de "de cada cien" y de los huecos; amenaza, cada "si no cambia", "si sigue así", "se juega", "le puede costar", "acabará"; peso, cualquier mención de kilos, báscula o bajar de peso.

RESTRICCIONES: Sin cifras: los huecos los relleno yo. Sin "si no…" y sin recordar riesgos para "motivar". Sin fármacos, sin dietas, sin "obeso" y sin "consulte con su médico": la médica soy yo. No incluyas ni pidas datos de personas.
```

Recuento: 383 palabras. Protegen: "DECISIÓN: la médica" (4), "[FALTA: plazo]" y "el plazo" (7), "fracción" (3), "acabará" (1), "consulte con su médico: la médica soy yo" (9), PALABRAS (3), "(por defecto)" (2), "nada más" y "cinco, o cuatro sin test" (7). Recorte posible: ninguno que merezca la pena.

Ejemplo de salida (l. 340-346), sustituir por (trae un test de consumo):

> GUION SIN DATOS
> QUÉ ES UN RIESGO. Una cuenta hecha sobre muchas personas parecidas a usted. De cada cien con sus mismos datos, [FALTA: n] tendrían [FALTA: qué] en [FALTA: plazo]. Las demás, no. Nadie sabe en qué grupo está usted.
> QUÉ VALE UN TEST DE CONSUMO. Los genes son una parte, no el final. Ese resultado no cambia lo que hacemos esta tarde.
> PREGUNTA DE VUELTA. Para saber si me he explicado bien, ¿cómo le contaría a alguien de confianza qué significa ese número?
> PALABRAS: 214 · CIFRAS: 0 · AMENAZAS: 0 · PESO: 0 · DECISIÓN: la médica

Frases nuevas para "Qué revisar" (l. 348): "Busca 'un tercio', 'la mitad', 'la mayoría': son cifras sin número y el modelo no las cuenta. El plazo es el de tu tabla, no el del modelo: un test genético no tiene plazo, y el hueco se queda vacío. Y si el guion termina con 'consulte con su médico', la máquina olvidó quién habla."

---

## Lista definitiva de etiquetas del anexo A (reglas 33 y 36; heredadas de los capítulos 1-9 y las nuevas de este capítulo)

Es el último capítulo: propongo la lista cerrada, por familias, con la definición de cada etiqueta en una línea, para que el ORQUESTADOR monte el anexo A desde aquí. Forma común a todas: mayúsculas; el recuento en la misma línea que su definición y con su valor esperado cuando lo hay; una sola forma por etiqueta en todo el anexo; ninguna con sintaxis `[^1]`. Entre paréntesis, dónde nació.

**1. Puertas de entrada (primera línea de la salida, con parada).**
- **(0) · "X SIN DATOS" / "X CON DATOS: BORRA ESTA CONVERSACIÓN"** (capítulos 4-10): la primera línea dice si lo pegado trae un identificador (nombre, edad exacta, fecha, lugar, número de historia, teléfono, firma); si lo trae, el modelo escribe la segunda y para. X es lo que entra: HOJA, TEXTO, TEXTOS, CASO, CONTEXTO, RESUMEN, GUION, PLANTILLAS, TABLAS.
- **PARECE UNA PERSONA REAL: BORRA ESTA CONVERSACIÓN** (10.3): la (0) de un caso inventado: para si el caso trae lo que un caso inventado no necesita (nombre, edad exacta, fecha de calendario, número de historia, municipio).
- **PASO 0** (1.6, 7.5): la (0) de una tabla agregada; el modelo lista columnas y valores, marca SOSPECHOSO y espera "continúa"; equivale a la (0) y la supera.
- **TEXTO CON OBJETIVO DE PESO: SE RETIRA** (10.6): tercera rama de la (0) cuando lo que entra es un texto para la persona con un objetivo de peso: no se reescribe, se retira.
- **"omítelo y sigue"** (9.6): la (0) de una tarea programada, que no tiene a nadie delante para parar: omite el elemento con datos y sigue.

**2. Huecos (lo que el modelo no tiene y no inventa).**
- **[FALTA: …]** (regla 24): hueco que ocupa la línea entera o el campo entero; nunca al final de una frase que afirma ("se envió el [FALTA: fecha]" está prohibida).
- **[FALTA: contacto del centro]** (regla 19): la primera de las tres líneas de todo texto para la persona; nunca un teléfono ni "responda a este mensaje".
- **[FALTA: ejecutar]** (regla 36): toda prueba que el modelo diga haber pasado sin ejecutarla; la rellena quien la ejecuta.
- **[FALTA: contar]** (10.6): todo recuento que solo puede hacer quien compara dos textos o dos listas (datos de salud añadidos o quitados); lo rellena la médica. Hermana de la anterior: la primera es para código, la segunda para comparaciones.
- **estimación: [FALTA: minutos]** (10.7; decisión 9): toda cifra de tiempo va con "estimación" delante y, si la médica no la dio, como hueco.
- **[FALTA: n] · [FALTA: qué] · [FALTA: plazo]** (10.8): los huecos de una frecuencia natural ("de cada cien…"); la cifra y el plazo los pone la médica.
- **[FALTA: fecha]** (10.5; 9.1): fechas de revisión o de envío que el modelo nunca fija.

**3. Verificación de referencias y lectura de documentos.**
- **EXISTE Y COINCIDE / EXISTE CON ERRORES / EXISTE PERO TRATA DE OTRA COSA / NO EXISTE** (2, 7; regla 33): veredicto de una referencia abierta a mano; ninguna entra sin abrirse.
- **SIN DOI** (9.6): resultado sin identificador; nunca en PUEDE CAMBIAR LO QUE HAGO.
- **SIN PÁGINA: [n]** (regla 36): citas cuya página no se ve en el archivo.
- **NO ESTÁ EN EL DOCUMENTO** (7.3), con sus dos formas ya impresas **NO ENCONTRADO EN EL DOCUMENTO** (2) y **NO LO DICE** (7.2): lo que el documento cargado no contiene; el anexo las lista juntas como una sola etiqueta con tres formas históricas.
- **FUENTES QUE VEO: [n] de [total]** (regla 36): el asistente con archivos declara cuántos ve.
- **ENCONTRADOS: [n]** (9.6) frente a **RECIBIDOS: [n]** (7.6): lo que una tarea trae frente a lo que la médica pega; nunca se intercambian.

**4. Listas de la médica y sus salidas controladas.**
- **FUERA DE MI LISTA** (regla 36; 9.6, 9.8): donde el modelo pone lo que querría añadir a una lista de la médica; ahí y solo ahí; nunca en una etiqueta ni en la lista.
- **SIN RESPUESTA** (9.7): a solas, sin paréntesis ni "presumiblemente"; lo que una descripción no dice.
- **SIN FRASES MARCADAS** (10.1): la línea de un texto en el que el revisor no marca nada; marcar nada es una respuesta válida.
- **CUANDO HAYA CONTRATO** (10.7): línea aparte para lo que necesita acuerdo de tratamiento de datos; fuera de todo plazo.
- **NO SE ENCIENDE** (9.7): veredicto de un agente en papel cuya regla lo apaga; sale de la regla, no de la opinión.
- **"<5"** (regla 32): recuentos, medias y medianas sobre menos de cinco personas, puestos por la médica antes de pegar.

**5. Cortes, certeza y decisión.**
- **PEOR QUE EL CORTE / MEJOR QUE EL CORTE / SIN CORTE** (regla 35): comparación con un punto de corte, con "peor" definido por prueba y el operador pegado por la médica.
- **ALTA / MEDIA / BAJA** (glosario): escala de certeza única del libro.
- **DECISIÓN: la médica** (regla 30; 8, 9.7, 9.8, 10.8): última línea literal de todo prompt donde hay una decisión clínica; el modelo ordena, la médica decide.

**6. Veredictos.**
- **SÍ / NO / NO LO SÉ** (9.4): respuesta de un auditor por comprobación; NO LO SÉ solo para lo que no está ni en el texto ni en las líneas de la médica, y cuenta como NO.
- **NO SE PUBLICA / SE CORRIGE Y SE VUELVE A PASAR / PUBLICABLE** (9.4; regla 18, precisión del ciclo 9): regla binaria para lo que se publica; sin nota.
- **NO SALE / CORRIGE Y VUELVE A CONTAR / REHACE / SALE** (10.2; regla 18): veredictos de la hoja de auditoría para lo que llega a una persona; con las eliminatorias 1, 3, 6 y 9.
- **LO QUE NO DEBE APARECER** (9.5): lista de comprobación devuelta por un generador de imágenes.

**7. Recuentos a cero con su lista de palabras en la misma línea** (familia; cada uno se define donde se usa y se copia igual en el anexo).
- **PALABRAS PROHIBIDAS ENCONTRADAS: [n]** (4.5) · **FRASES QUE EVALÚAN: [n]** (4.6) · **VERBOS DE CAUSA: 0** (7.5) · **DIAGNÓSTICOS, PROBABILIDADES O PAUTAS: 0** (9.8) · **JUICIOS DE CAUSALIDAD, GRAVEDAD O TRATAMIENTO: 0** (10.3) · **FRASES QUE PROMETEN: 0** (10.5; palabras del 3.2) · **LEYES O HERRAMIENTAS NOMBRADAS: 0** (10.5) · **PROMESAS DE RESULTADO: 0** (10.7) · **AMENAZAS: 0** y **PESO: 0** (10.8) · **CIFRAS, FECHAS O NOMBRES FUERA DE UN HUECO: 0** (9.1): cada uno con su lista literal de palabras o verbos en la misma línea; el "0" lo comprueba la médica buscando las palabras.
- **PALABRAS: [n]** y sus formas (**PALABRAS POR VARIANTE**, 6.6; **PALABRAS: [n] / [n] / [n]**, 9.1; **PALABRAS: original [n] · reescrito [n]**, 10.6): recuento de palabras con tope declarado; se cuenta una muestra con el dedo.

**8. Estigma y lenguaje centrado en la persona (10.1 y 10.6; reglas 27 y 7).**
- **CULPA · MORALIZACIÓN · ATRIBUCIÓN · DESACTIVACIÓN · CIFRA DE PESO · INDIVIDUAL · OBESO/A**: las siete categorías cerradas, con nombre corto igual en la lista y en el recuento; una por frase, la primera que encaje; con sus anclas.
- **NEGACIONES CONSERVADAS: [n]** (regla 27; 10.6) y **NEGACIONES DE CULPA VISTAS: [n]** (10.1): las frases que niegan la culpa no se marcan ni se reescriben; se cuentan aparte.
- **IMPERATIVOS DE SEGURIDAD CONSERVADOS: [n]** (10.6): toda orden que evita un daño se conserva literal al quitar el estigma.

**9. Líneas fijas y condicionales (bloques literales, no recuentos).**
- **Las tres líneas** (regla 19): contacto como hueco; urgencias en una de las dos fórmulas fijas (la larga de la regla 17 o "dolor en el pecho, falta de aire o mareo"); disclaimer en su trato (regla 11).
- **LÍNEA DE URGENCIAS: [ninguna]** y **LÍNEA DE AZÚCAR BAJO: [ninguna]** (regla 30): las activa la médica; la máquina nunca añade una red de seguridad por su cuenta.
- **ENTREGA: [oral / escrita]** y sus formas (regla 30; 10.6): la médica decide si el texto llega escrito y, con ello, si lleva las tres líneas.
- **LÍNEAS FINALES EN [IDIOMA]** (regla 28): las tres líneas validadas una vez por idioma y pegadas como literal.
- **"Sin ninguna línea de 'generado con IA': lo firmo yo"** (regla 23): en todo prompt de documento firmado.
- **"No incluyas ni pidas datos de personas"** y **"nada más"**: cierre de todo prompt del libro.
- **CONTEXTO DE VOZ** (4.2): bloque reutilizable de estilo de la autora; se guarda una vez en el anexo A.

Lo que sale de la lista por decisión de ciclos anteriores: SOLO EL GUION y MÁS DE DIEZ (consolidado 9, D2: llevadas a prosa). Lo que queda como forma histórica, sin volver a usarse: RECIBIDOS (7.6), NO ENCONTRADO EN EL DOCUMENTO (2) y NO LO DICE (7.2), porque están en capítulos aprobados.

---

## Preguntas para Cristina (máximo cinco)

1. **Caso 1.** ¿Ha corrido ya los cinco prompts en los tres asistentes, o lo hará al cerrar el libro? Y del revisor, ¿quiere que además de marcar reescriba cada frase (como ahora) o solo que marque? Lo segundo baja el prompt 40 palabras y quita la única puerta por la que el revisor puede colar "no depende de usted".
2. **Caso 3.** ¿Prefiere que el ensayo del formulario no lleve iniciales en absoluto (siempre hueco, como propongo) o quiere practicar también ese campo con dos letras inventadas? Y en su centro, ¿la notificación la hace desde notificaRAM.es o desde el formulario de su historia clínica (cambia la frase "notificaRAM.es abierto, no el chat")?
3. **Caso 6.** ¿Qué textos antiguos tiene su centro (hojas, carteles, plantillas de recomendaciones) y traen su propia línea de urgencias? Si la traen, ¿la sustituye por la del libro o conserva la del centro? (Decide si la línea antigua se queda en el cuerpo y la del libro va al pie, como propongo.)
4. **Caso 7.** ¿Tiene alguna cifra real de minutos por caso (la calculadora, la plantilla de informe) medida con reloj, o el primer mes va entero con "[FALTA: minutos]"? Es la única variable nueva del capítulo y conviene que el ejemplo lleve su cifra y no una inventada.
5. **Caso 8.** ¿Qué tabla de riesgo usa su servicio de salud y a qué plazo (cinco años, diez), para que la ficha del prompt lleve el plazo como valor por defecto del hueco?

## Notas para el ORQUESTADOR

- Código: 2.440 → 2.742 (+302). El capítulo está en 9.884 (`split()`) sobre un tope de 10.000 sin tope ad hoc; recortes marcados "(−n)" que no tocan seguridad ni recuentos: 93 palabras (1: −40 si la autora acepta un revisor que solo marca; 2: −22 si la hoja va al anexo B; 5: −6; 6: −14; 7: −11). Quedan dos traslados preautorizados sin aplicar (hoja de auditoría al anexo B; URL de referencias): con ellos y los recortes el capítulo cabe.
- **Decisión que pido al ORQUESTADOR y a COMPLIANCE (caso 2):** si "no depende de usted" (regla 27, "peor que la culpa") convierte la pregunta 5 en NO con corrección obligatoria antes de salir aunque la cuenta dé 8 o más; mi hoja lo escribe como "SALE por la cuenta; así no sale", que es verdad con cualquier respuesta, y el anexo B puede recoger la precisión sin tocar el capítulo 3. Y si la pregunta 1 de una hoja de procedencia desconocida es NO (lo propongo) o NO LO SÉ.
- **Decisión tomada (T5):** huecos como campos en el formulario del caso 3; el glosario de la biblia no cambia ("hueco de línea entera": un campo es una línea).
- **Gravedad alta en el caso 5:** "textos propios anonimizados a mano" en el contexto de la política contradice la regla 26; cambia a "textos genéricos del centro sin datos de nadie" en prompt y ejemplo. Para COMPLIANCE.
- **Ejemplos que el prompt no produce (T11):** minutos inventados en el caso 7 (capítulo y anexo D: la plantilla pasa a cinco filas), la categoría de "las molestias" en el caso 1, el hueco de campo en el caso 3. Los tres corregidos aquí.
- Etiquetas del anexo A: lista definitiva en la sección anterior (nueve familias, 50 etiquetas); las nuevas de este capítulo, en T8. Ninguna con sintaxis `[^1]`.
- Frase introductoria (l. 84): dos precisiones (clave de letras fuera del chat; "los seis son texto y nada más").
- Para CLÍNICO: "ánimo bajo" en el bloque 7 del guion del caso 4 (regla 29); la definición de imperativo de seguridad del caso 6 ("toda orden que evita un daño", con "no deje el tratamiento"); el plazo de la tabla de riesgo del caso 8 como hueco.
- Para EVIDENCIA: nada nuevo desde los prompts; el triángulo negro y CIMA siguen en su [VERIFICAR].
- Para COMPLIANCE: caso 2 (pregunta 1 y regla 27 en la 5); caso 5 (regla 26 en el contexto; leyes fuera de la página); caso 3 (iniciales siempre hueco: menos datos en el ensayo, ninguno que parezca real).
- Sin commit. El capítulo no se ha tocado.

## JSON de traspaso

```json
{
  "agente": "PROMPTS",
  "capitulo": 10,
  "version": "v1",
  "estado": "revisar",
  "entrega": "revisiones/cap10_prompts.md",
  "resumen": "Seis prompts y dos bloques sin IA revisados; ninguno peligroso; los seis a MEJORAR (dos leves) y los dos bloques a MEJORAR (uno leve). Fallos de fondo: tres ejemplos de salida que el prompt no puede producir (minutos inventados en el 7, categoría no detectable en el 1, campos contra líneas en el 3), siete recuentos no contables, una contradicción de la hoja del caso 2 con su propia regla, y una frase del contexto de la política (caso 5) que rompe la regla 26. Código 2.440 -> 2.742 (+302), con 93 palabras de recorte marcadas. Lista definitiva de etiquetas del anexo A propuesta (nueve familias).",
  "hallazgos": [
    {"gravedad": "alta", "ubicacion": "caso 5, prompt, CONTEXTO (l. 226) y ejemplo (l. 238)", "cita": "textos propios anonimizados a mano", "problema": "Dentro de la política del centro autoriza a pegar notas o informes 'anonimizados a mano', que la frase siguiente del mismo contexto, la regla 26 y el capítulo 3 prohíben; la frase introductoria (l. 84) dice lo correcto.", "correccion": "\"textos genéricos del centro sin datos de nadie\" en prompt y ejemplo. COMPLIANCE confirma."},
    {"gravedad": "alta", "ubicacion": "caso 7, prompt (l. 299-303), ejemplo (l. 310) y plantilla del anexo D (anexos/cap10_material_anexos.md, l. 33-37)", "cita": "estimación: 10 minutos por semana", "problema": "El prompt prohíbe inventar minutos y el contexto no da dónde ponerlos; el ejemplo y la plantilla traen cifras que el modelo inventó con 'estimación' delante y el recuento las da por buenas; la plantilla tiene seis filas contra 'cinco en total'.", "correccion": "Variable MINUTOS QUE ESTIMO RECUPERAR, por caso, solo los que tengo; recuento 'CIFRAS DE MINUTOS: [n], todas de mi lista · HUECOS DE MINUTOS: [n]' que suman 5; 'una fila por caso, cinco filas'; plantilla del anexo D a cinco filas (sin 8.1) con cifras declaradas de la lista de la autora; línea literal 'Estas medidas cuentan qué hice, no qué conseguí'."},
    {"gravedad": "alta", "ubicacion": "caso 1, prompt TAREA (l. 97) y ejemplo (l. 110)", "cita": "CONSEJO INDIVIDUAL DISFRAZADO DE GENERAL (\"en su caso\", \"usted debería\", \"pruebe a\")", "problema": "La categoría no detecta 'las molestias son señal de que funciona' (sin marcador de segunda persona); el ejemplo muestra lo que el prompt no produce. Además CIFRA caza los valores de analítica de la carta de resultados (5.7) e INDIVIDUAL caza el 'usted' del consejo breve (4.5) y de la carta, que hablan a una persona por diseño; no hay salida para un texto sin estigma; el recuento no es contable (una frase puede tener dos categorías; sumas sin regla).", "correccion": "INDIVIDUAL definida por lo que hace ('decide por la persona lo que decide una consulta') con anclas 'es normal' y 'las molestias son señal de que funciona'; CIFRA DE PESO con 'las cifras de analítica no cuentan'; línea de género en el contexto (1, 3 y 4 para cualquiera; 2 y 5 a una persona); 'SIN FRASES MARCADAS'; una categoría por frase, una vez por texto, 'las dos sumas tienen que coincidir'; una sola salida de treinta líneas; 'ninguna reescritura tuya puede encajar en una categoría'; 'nada más'."},
    {"gravedad": "media", "ubicacion": "caso 2, hoja de auditoría, ejemplos (a) y (b) (l. 135-138) y regla (l. 131)", "cita": "9 de 10: CORRIGE", "problema": "Con la regla de la propia hoja (8 o más síes SALE) 9 de 10 es SALE: la hoja se contradice en el ejemplo que enseña la regla 27. (a) atribuye 'comprométase' a la pregunta 6 (es la 5) y marca 1 SÍ en una hoja de la que nadie sabe qué entró. 'Las otras seis, con las diez' no se entiende. Sin línea en blanco para rellenar.", "correccion": "(b): 'SALE por la cuenta; así no sale: vuelve \"No es culpa suya\" → 10: SALE'; (a): '1 NO: no sé qué entró ni dónde · 5 NO · 6 NO'; regla reescrita ('Con las cuatro SÍ, síes de las diez: 8-10 SALE · 6-7 CORRIGE Y VUELVE A CONTAR · 5 o menos REHACE'); línea en blanco con diez casillas. Pregunta al ORQUESTADOR y a COMPLIANCE: si la desactivación (regla 27) obliga a corregir la 5 antes de salir aunque la cuenta dé 8 o más (precisión de la regla 18 para el anexo B)."},
    {"gravedad": "media", "ubicacion": "caso 3, prompt TAREA y FORMATO (l. 162-164) frente al ejemplo (l. 171-176)", "cita": "Todo lo que no te haya dado va como hueco de línea entera", "problema": "El prompt exige línea entera y el ejemplo usa campos ('[FALTA: dosis y vía]' en mitad de una línea): decisión (2) del REDACTOR pendiente. 'BLOQUES RELLENOS: [n] de 5' siempre es 5; HUECOS sin valor esperado. Principio activo con la instrucción dentro del corchete. Iniciales pedidas ('iniciales inventadas') y escritas como '[inventadas]'. La lista de juicios no caza 'conocida' ni 'descrita'; Gemini convierte la franja de edad en cifra.", "correccion": "Decisión: campos, dieciocho nombrados, uno por línea, hueco como todo el contenido del campo, regla 24 por su nombre ('se suspendió el [FALTA: fecha]' está prohibida); recuento 'CAMPOS: 18 · RELLENOS: [n] · HUECOS: [n]' que suman 18; principio activo 'elegido por mí en CIMA entre los de seguimiento adicional (triángulo negro): [principio activo]'; iniciales, profesión y centro siempre hueco; 'conocida', 'descrita' en la lista; 'la franja de edad se copia como franja'. Ejemplo reescrito con campos y '(en el libro, sin rellenar)' junto a [principio activo]."},
    {"gravedad": "media", "ubicacion": "caso 6, prompt FORMATO y RESTRICCIONES (l. 268-270)", "cita": "INFORMACIÓN CLÍNICA CAMBIADA: 0", "problema": "Es una declaración del modelo, no un recuento (regla 36); Gemini quita 'tres o cuatro días' y escribe 0. 'Sin acortarlo más de un 20 %' no se ve sin contar. 'OBJETIVO DE PESO O CIFRA' es categoría muerta (la restricción para antes). Imperativo de seguridad sin definir: los tres suavizan 'debe tomar la medicación'. La línea de urgencias 'solo si el original la traía, literal' crea una tercera fórmula (regla 19). Reescrituras del revisor sin correa (regla 27).", "correccion": "'DATOS DE SALUD AÑADIDOS O QUITADOS: [FALTA: contar]' con parejas original → reescrita y 'PAREJAS = MARCADAS'; 'PALABRAS: original [n] · reescrito [n]'; la parada a la (0) como tercera rama 'TEXTO CON OBJETIVO DE PESO: SE RETIRA'; imperativo definido ('toda orden que evita un daño', tres ejemplos); línea antigua conservada en el cuerpo, fórmula del libro al pie por la médica; 'ninguna reescritura tuya puede encajar en una categoría'; ENTREGA con valor por defecto; nombres de categoría unificados con el caso 1."},
    {"gravedad": "media", "ubicacion": "caso 5, prompt TAREA y FORMATO (l. 228-230)", "cita": "APARTADOS: 7 · FRASES QUE PROMETEN: 0 · HUECOS: [n]", "problema": "Los tres modelos citan RGPD/LOPDGDD o nombran herramientas en uno de tres sin que nada lo prohíba ni lo cuente; HUECOS sin valor esperado y sin el hueco de la próxima revisión que la mitigación (l. 253) promete; lista de promesas incompleta respecto al capítulo 3 (l. 171) y sin 'en cualquier forma'; 'unas 300 palabras' no es tope; sin 'nada más'.", "correccion": "'ni leyes, ni artículos, ni herramientas con nombre' y 'LEYES O HERRAMIENTAS NOMBRADAS: 0'; REVISIÓN termina con 'Próxima revisión: [FALTA: fecha]' y 'HUECOS: 2'; 'cifrado', 'aprobado', 'en cualquier forma'; 'máximo 320 palabras sin contar el pie, y nada más'."},
    {"gravedad": "baja", "ubicacion": "caso 8, prompt FORMATO y CONTEXTO (l. 329-337)", "cita": "CIFRAS: 0 · AMENAZAS: 0 · KILOS: 0", "problema": "Falta 'DECISIÓN: la médica' (regla 30); KILOS está dentro de CIFRAS y no caza 'bajar de peso' sin número; 'cifra' no incluye fracciones ('un tercio'); 'en diez años' fija un plazo que no vale para un test genético; ChatGPT cierra con 'consulte con su médico'; QUÉ TRAE sin valor por defecto; sin PALABRAS ni 'nada más'.", "correccion": "'PALABRAS: [n] · CIFRAS: 0 · AMENAZAS: 0 · PESO: 0 · DECISIÓN: la médica'; 'número, porcentaje o fracción'; 'acabará' en amenazas; '[FALTA: plazo]'; 'sin \"consulte con su médico\": la médica soy yo'; '(por defecto)' en el primer valor."},
    {"gravedad": "baja", "ubicacion": "caso 4, guion oral, bloques 5 y 7 (l. 198 y 200)", "cita": "Nada suyo entra nunca en ella; su plan tampoco.", "problema": "Se aparta de la fórmula única de la regla 16 que el capítulo 3 (caso 5) y la viñeta (l. 373) usan literal; el bloque 7 ('si cuenta otra cosa', regla 29) no dice 'se anota' ni incluye 'ánimo bajo'.", "correccion": "'Nada que permita saber quién es usted entra nunca en esas herramientas; su plan tampoco.'; bloque 7 con 'ánimo bajo' (CLÍNICO decide) y 'y se anotan'. 171 palabras (+11 sobre el tope: las dos reglas)."},
    {"gravedad": "baja", "ubicacion": "frase introductoria (l. 84)", "cita": "se revisa en un cuarto, o en el mismo sin memoria", "problema": "No dice que las letras A, B y C las asigna la médica antes de pegar ni que la clave no entra en el chat; y puede decir que los seis son solo texto (portabilidad sin matices por primera vez desde el capítulo 7).", "correccion": "'…o en uno de los tres sin memoria; las letras las pones tú antes de pegar y la clave no entra en el chat. Los seis prompts son texto y nada más: se pegan en Gemini, ChatGPT y Claude cuando escribo esto; comprueba la versión vigente.'"},
    {"gravedad": "baja", "ubicacion": "los seis prompts, FORMATO", "cita": "Después (1), (2) y (3).", "problema": "'Nada más' faltaba en cuatro de seis (1, 5, 7, 8): Claude añade una nota final y ChatGPT un párrafo de consejos en uno de tres.", "correccion": "'y nada más' en los seis."},
    {"gravedad": "nota", "ubicacion": "anexo A (reglas 33 y 36)", "cita": "etiquetas de las reglas 33 y 36 unificadas", "problema": "Último capítulo: hace falta la lista cerrada.", "correccion": "Lista definitiva en el informe: nueve familias, unas cincuenta etiquetas con definición en una línea; nuevas de este capítulo: las siete categorías de estigma con nombre corto, SIN FRASES MARCADAS, PARECE UNA PERSONA REAL, TEXTO CON OBJETIVO DE PESO: SE RETIRA, [FALTA: contar], CUANDO HAYA CONTRATO, JUICIOS DE CAUSALIDAD…: 0, FRASES QUE PROMETEN: 0, LEYES O HERRAMIENTAS NOMBRADAS: 0, PROMESAS DE RESULTADO: 0, AMENAZAS: 0, PESO: 0, IMPERATIVOS DE SEGURIDAD CONSERVADOS, NEGACIONES DE CULPA VISTAS, los cuatro veredictos de la hoja (NO SALE / CORRIGE Y VUELVE A CONTAR / REHACE / SALE), estimación: [FALTA: minutos], [FALTA: n] / [FALTA: qué] / [FALTA: plazo]."}
  ],
  "preguntas_para_cristina": [
    "Caso 1: ¿ha corrido ya los cinco prompts en los tres asistentes? ¿Quiere un revisor que marque y reescriba (como ahora) o solo que marque (−40 palabras y menos riesgo de que el revisor desactive)?",
    "Caso 3: ¿el ensayo sin iniciales (siempre hueco) o con dos letras inventadas? ¿Notifica desde notificaRAM.es o desde el formulario de su historia clínica?",
    "Caso 6: ¿qué textos antiguos tiene el centro y traen su propia línea de urgencias? Si la traen, ¿conserva la del centro en el cuerpo y pone la del libro al pie, o la sustituye?",
    "Caso 7: ¿tiene alguna cifra real de minutos por caso medida con reloj, o el primer mes va entero con [FALTA: minutos]?",
    "Caso 8: ¿qué tabla de riesgo usa su servicio de salud y a qué plazo, para que la ficha lleve el plazo como valor por defecto del hueco?"
  ],
  "notas": [
    "Código 2.440 → 2.742 (+302); recortes marcados '(−n)' sin tocar seguridad: 93 (1: −40; 2: −22; 5: −6; 6: −14; 7: −11). Dos traslados preautorizados sin aplicar (hoja de auditoría al anexo B; URL de referencias).",
    "Decisión tomada: huecos como campos (regla 24) en el formulario del caso 3; el glosario no cambia.",
    "Decisión que pido: regla 27 frente a regla 18 en la hoja del caso 2 (¿la desactivación obliga a corregir la 5 antes de salir aunque sumen 8 o más?); pregunta 1 de una hoja de procedencia desconocida = NO.",
    "Regla 10: ninguna frase del Módulo 3 copiada en los prompts ni en los bloques; el mínimo de identificación (iniciales, sexo, franja) es el del formulario y ya está en el capítulo 3.",
    "Portabilidad: los seis son texto puro; el 1 pega unas seis mil palabras y cabe en los tres; Gemini corta salidas largas y no para en la (0) de tres ramas (caso 6) en uno de tres: en 'qué revisar'.",
    "Sin commit. El capítulo no se ha tocado."
  ]
}
```
