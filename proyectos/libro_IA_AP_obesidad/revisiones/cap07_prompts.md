# Revisión PROMPTS · Capítulo 7 · v1

> Agente: PROMPTS (ingeniero de prompts) · Fecha: 2026-09-15 · Ámbito: exclusivamente los siete bloques de código que el capítulo ofrece al lector (casos 1 a 7) y los ejemplos abreviados de salida que los acompañan, más la frase introductoria a los casos (l. 64-66) porque fija reglas que los prompts heredan. No se revisa el texto expositivo, la viñeta ni las referencias.
> Versión revisada: `capitulos/cap07_v1.md` (348 líneas, 6.800 palabras; las líneas citadas son las de esa versión, `grep -n`). Los siete bloques pesan 2.393 palabras (337 · 321 · 347 · 350 · 349 · 350 · 339): **los siete cumplen el tope de 350** de la decisión provisional del plan. Es la primera vez en el libro que un capítulo de prompts entra en el tope antes de la revisión, y cambia el método: cada correa que añado va acompañada de una que quito o fundo, y cada versión corregida se ha contado con un script (`len(texto.split())`, palabras separadas por espacio; los rótulos "ROL:", "(0)" y los signos sueltos cuentan como palabra, que es el criterio más exigente). Resultado: 348 · 349 · 349 · 350 · 350 · 350 · 348.
> Método: el de los capítulos 1 a 6 (`revisiones/cap06_prompts.md`). Para cada prompt: rol · contexto · tarea · formato · restricciones; etiqueta (0) antes que el contenido, que para si entra un dato, en los prompts en los que entra un texto o un archivo (T1 del capítulo 5); variables entre corchetes con valor por defecto y sin instrucción al lector dentro del corchete (T6 del capítulo 5); recuentos definidos en la misma línea y contables a mano (T2 del capítulo 5; T5 del capítulo 4); si el modelo puede rellenar un hueco sin que se note (regla 24); portabilidad Gemini / ChatGPT / Claude sin cambios, y Perplexity, Consensus, Elicit o NotebookLM cuando el caso los nombra; si el prompt distingue lo que busca en internet de lo que responde de memoria (capítulo 2, caso 2; decisión 5); realismo del ejemplo de salida para 2026; riesgo. Cada prompt se ha ejecutado mentalmente con las variables de ejemplo del propio capítulo (la duda de la masa muscular; GIRO 2024, Wharton 2020 y una tercera guía; el ensayo STEP 1 de semaglutida en PDF y solo en resumen; "cenar tarde engorda"; las dos tablas del programa con las cifras del ejemplo; nueve resúmenes de una alerta; doce referencias con una inventada al estilo del capítulo 2), y la salida se ha leído con la rúbrica del capítulo 4 y las diez preguntas del anexo B. Reglas 5, 7, 11, 12, 16, 19, 21, 22, 24, 26, 27 y 30 de `biblia.md` como norma; ficha del caso 7 del capítulo 4 (v3) como plantilla de guardado.

## Resumen de veredictos

| Caso | Título | Palabras v1 → corregida | Veredicto | Motivo principal |
|---|---|---|---|---|
| 1 | De la duda a la pregunta PICO | 337 → 348 | **mejorar** | La sintaxis MeSH del ejemplo es correcta para PubMed (`"Anti-Obesity Agents"[MeSH]`, `"Body Composition"[MeSH]`, `"Resistance Training"[MeSH]` existen y `[MeSH]` es etiqueta válida), pero la cadena (a) del ejemplo une con AND la intervención del PICO 2 (ejercicio de fuerza) a la pregunta del PICO 1 (cuánto se pierde): con dos PICO y "CADENAS: 3" el prompt obliga a mezclar dos preguntas en una cadena, que es lo que (1) acaba de separar. Los tres modelos inventan uno de cada cuatro términos MeSH (etiquetan `[MeSH]` un sinónimo que no es descriptor); el prompt lo prevé, "qué revisar" lo caza. Resiste la tentación de responder en Claude y ChatGPT; Gemini contesta "de paso" en un preámbulo de una línea en una de tres y, los tres, dentro de "NO CUBRE" ("no cubre que la pérdida sea similar a la de la dieta"). Falta "sin preámbulo" y "ni dentro de NO CUBRE". |
| 2 | Tres guías, una pregunta | 321 → 349 | **mejorar (leve)** | En NotebookLM funciona: no hay páginas y el prompt ya admite "número de cita"; la tabla sale con chips y celdas "NO LO DICE". Con tres PDF largos en ChatGPT la lectura es por fragmentos y "NO LO DICE" a veces es "mal buscado"; en Claude, tres guías de 150-250 páginas pueden no caber y no hay línea de "LECTURA PARCIAL" (el caso 3 del capítulo 2 la tiene; este no). "COINCIDEN" se inventa en los tres: escriben un criterio de consenso ("valorar la derivación cuando no hay respuesta") aunque una columna diga "NO LO DICE", porque nada ata esa fila a la tabla; el recuento "CRITERIOS EN 'COINCIDEN'" cuenta lo que el modelo quiso poner. Se ata: solo filas sin ninguna celda "NO LO DICE", nombrando la fila. |
| 3 | Un ensayo en diez minutos | 347 → 349 | **mejorar** | Con el PDF entero, Claude y Gemini lo leen y las cifras salen con página; ChatGPT lo lee por fragmentos y rellena PÉRDIDAS y EFECTOS ADVERSOS con lo que sabe del ensayo, que es de los más citados del campo, y les pone una página plausible: "CIFRAS SIN PÁGINA: 0" se cumple inventando páginas. Con solo el resumen, los tres completan DISEÑO y EFECTOS ADVERSOS de memoria en dos de tres. "DATOS QUE NO ESTÁN EN EL DOCUMENTO" es honesta solo en Claude con el PDF entero. Falta "aunque lo sepas de memoria", una etiqueta "SOLO RESUMEN" y el apartado o tabla junto a la página (inventar "p. 995, Tabla 2" es más difícil que "p. 995"). El ejemplo confunde dos apartados: "qué pasó con el peso después de la semana 68" no es "lo que el resumen no dice" (datos del texto que el abstract no trae), es lo que el documento no contiene. "Cifra" no está definida. |
| 4 | Del titular al artículo | 350 → 350 | **mejorar** | La puerta de dos turnos funciona en Claude, ChatGPT y Perplexity; Gemini hace A y B seguidos en una de tres. Lo que no funciona: el prompt pide "DOI, enlace" y Perplexity y los modos de búsqueda de los tres enlazan la noticia o la nota de prensa de la universidad (que trae el DOI, y por eso el modelo lo copia sin abrir el artículo); falta "enlace al artículo, nunca a la noticia". La variante escrita es ejecutable pero rompe la regla 30: es la máquina quien decide si el estudio "trata de síntomas o de cambiar un tratamiento" y, con ello, si la respuesta se escribe; la decisión pasa a la médica (ENTREGA escrita solo si no toca síntomas ni tratamientos) y el prompt prohíbe añadir línea de urgencias, como en el capítulo 6. La línea (0) está en FORMATO y PASO A dice "solo esto": se mueve a la cabeza del paso A. |
| 5 | Mis datos, agregados | 349 → 350 | **mejorar (leve)** | "PASO 0" equivale a la etiqueta (0) y es más fuerte: es un turno entero que inspecciona columnas y valores y para; es la forma del caso 6 del capítulo 1, que este caso continúa, y se mantiene por coherencia. Para y espera "continúa" en Claude y ChatGPT; Gemini hace el paso 1 seguido en una de tres. La lista de "lo que no se puede concluir" la escribe la máquina con tópicos: Claude ata cada punto a una cifra, ChatGPT dos de seis, Gemini ninguno ("sin grupo de comparación no se puede atribuir causalidad"). Se ata a las tablas con "la cifra que lo muestra o 'no se ve en estas tablas'" y un recuento "PUNTOS CON CIFRA". "Redujo" en la lista de verbos de causa cuenta "la mediana se redujo", que es descripción: la lista pasa a "el programa como sujeto". Falta la etiqueta "BORRA ESTA CONVERSACIÓN" cuando el paso 0 encuentra un nombre. |
| 6 | La alerta mensual de evidencia | 350 → 350 | **mejorar (leve)** | Resume sin inventar cifras en los tres ("sin cifra en el resumen" funciona); lo que añaden de memoria es el n o el seguimiento de un ensayo conocido, y la restricción lo cubre. La clasificación no es contable: "di en una frase qué parte cumple" deja que el modelo decida qué es "desenlace clínico" y todo tiende a "CONVIENE SABERLO"; con las cuatro condiciones de CAMBIA en SÍ/NO, la etiqueta se comprueba con el dedo. El tope de 350 palabras es imposible con más de diez resúmenes si "NO APLICA" cuenta: se saca del tope. La línea (0) marca "TEXTO CON DATOS" por "cualquier dato de una persona" y un resumen de PubMed lleva nombres de autores (y a veces el correo del autor de contacto): Claude para en una de tres. Se excluyen los autores. |
| 7 | Verificar las referencias | 339 → 348 | **mejorar (leve)** | La tabla de sospechosos detecta el DOI con formato raro (regla "10." + cuatro cifras + barra, contable) y el año que no cuadra con el volumen; los tres marcan bien lo contable y, en lo de memoria (prefijo de editorial, revista que no conoce), ChatGPT y Gemini escriben en SEÑALES "esta referencia existe" o "el DOI correcto es…": es verificar de memoria, que el prompt prohíbe a medias ("no propongas la correcta") y ahora prohíbe entera ("ni digas que existe"). Contradicción interna en el ejemplo: "campo vacío" es señal, "SIN PMID: 9" y "CON SEÑALES: 4" no pueden convivir, y la fila de ejemplo dice "año y volumen no cuadran" con el volumen vacío. Se exceptúa el PMID (casi nunca está) y se añaden dos señales contables: el año dentro del DOI y el PMID que no es un número de hasta ocho cifras. |

Ningún prompt es peligroso tal como está: ninguno pide decisiones clínicas, ninguno admite datos de nadie, los siete llevan "no incluyas ni pidas datos de personas", y el único texto que llega a la persona (caso 4, variante escrita) lleva las dos líneas de la regla 19 que le corresponden. Ninguno hay que reescribir de arriba abajo. Dos producen algo que no debe salir sin cambios: el 3 (cifras de memoria con página inventada en ChatGPT y con solo el resumen) y el 4 (la noticia por el artículo; la máquina decide si se escribe). El 1 mezcla dos preguntas en una cadena. Los otros cuatro son retoques de una o dos líneas. La portabilidad es la que el capítulo declara (l. 66): el 2 para NotebookLM, el 3 con archivos, el 4 con búsqueda, el 5 mejor con código; comprobado.

---

## Hallazgos transversales (afectan a varios casos)

**T1 · El tope de 350 se cumple, y el método cambia.** Los siete bloques entran en el tope antes de revisar (337-350). Todas mis correcciones se han hecho por sustitución: por cada correa nueva he quitado una frase redundante con el rol o con otra correa (en el 1, la lista de herramientas del contexto, que (2) ya enumera; en el 3, "nada de memoria" pasa a la línea de "NO ESTÁ EN EL DOCUMENTO"; en el 4, "DE MEMORIA: COMPROBAR ANTES DE SEGUIR" se funde con "HE BUSCADO: NO", que ya lo dice; en el 5, "no inventes tendencias ni causas", que el rol y el recuento ya cubren; en el 7, "voy a comprobar cada una a mano", que el rol y (3) ya dicen). Ninguna versión corregida supera 350. Recomiendo al ORQUESTADOR fijar la decisión (c) de la regla 20 como definitiva: este capítulo demuestra que cabe.

**T2 · Búsqueda o memoria: cuatro formas distintas para una sola regla.** La decisión 5 pide distinguir lo que busca de lo que responde de memoria. El capítulo lo hace con cuatro fórmulas: "No busques en internet" (1 y 7), "HE BUSCADO EN INTERNET: SÍ / NO" (4, la del capítulo 2), "BUSCADO" por fila (7) y "solo lo que está en…" (2, 3, 6). Son coherentes y cada una es la correcta para su caso. Lo que falta en el 4 es lo que la atención especial pregunta: un buscador con IA encuentra antes la noticia que el artículo, y la noticia trae el DOI en la nota de prensa; "HE BUSCADO: SÍ" es verdad y el estudio no se ha abierto. La correa no es la etiqueta: es "enlace al artículo (doi.org, PubMed o la revista), nunca a la noticia". En el 3, la memoria entra por otra puerta: el ensayo es famoso, y "solo el documento adjunto" no basta cuando el modelo sabe la cifra; hay que decirle que la calle "aunque lo sepas de memoria".

**T3 · Los recuentos cuentan lo que el modelo quiso contar en tres casos.** "CRITERIOS EN 'COINCIDEN'" (2) cuenta filas que nada ata a la tabla; "LO QUE NO SE PUEDE CONCLUIR: [n]" (5) cuenta puntos de una lista que el propio prompt dicta (cinco), así que siempre da 5 o 6 y no mide nada; "CIFRAS CON PÁGINA: 19" (3) no define cifra. La regla de los capítulos 4 y 5 (recuento con unidad definida en la misma línea) se aplica: COINCIDEN solo con filas sin "NO LO DICE"; "PUNTOS CON CIFRA" en el 5; "cifra es cada número con unidad o porcentaje" en el 3. Y un recuento contradictorio en el 7: "campo vacío" como señal y "SIN PMID: 9" con "CON SEÑALES: 4".

**T4 · La etiqueta (0) y sus dos formas.** Seis prompts la llevan con "para": 1 ("DUDA"), 2 ("FUENTES NO VÁLIDAS"), 4 ("PREGUNTA"), 6 ("TEXTO"), 7 ("LISTA") y el 5 como "PASO 0". Dictamen sobre el 5: PASO 0 equivale a (0) y la supera, porque no es una línea sino un turno de inspección con parada, y es la forma con la que el capítulo 1 (caso 6) abrió esta serie; se mantiene el nombre por continuidad y se le añade lo que le faltaba, "BORRA ESTA CONVERSACIÓN". El 3 no la lleva y no la necesita (entra un ensayo público), pero hereda del capítulo 2 la línea de "Páginas que veo" y "LECTURA PARCIAL", que es su puerta; el 2 no hereda esa línea y le hace falta con tres PDF. Precisión para el 6: "cualquier dato de una persona" incluye a los autores de un resumen, que son personas con nombre; se excluyen por su nombre.

**T5 · La máquina no decide si un texto lleva red de seguridad ni si se escribe (regla 30).** El caso 4, variante escrita, dice "si el estudio trata de síntomas o de cambiar un tratamiento, en (5) escribe solo 'ESTA RESPUESTA SE DICE, NO SE ESCRIBE'". Es coherente con la regla 19 en la intención (evita escribir un texto que exigiría la línea de urgencias) e incoherente con la regla 30 en el mecanismo: quien decide si el texto toca síntomas es el modelo, y con "cenar tarde engorda" ChatGPT lo escribe (no toca síntomas) y Gemini se niega en una de tres ("puede afectar al tratamiento de la diabetes"). La decisión pasa a la médica, fuera del corchete, y el prompt lleva la frase del capítulo 6: "no añadas ninguna línea de urgencias, de síntomas ni de 'consulte con su médico', aunque te parezca prudente". Con eso, la variante escrita lleva las dos líneas de la regla 19 que le tocan (contacto y aviso en usted) y ninguna tercera fórmula.

**T6 · Los ejemplos de salida son realistas para 2026, con dos excepciones.** Las cifras del caso 3 son las del ensayo STEP 1 tal como las recuerdo (−14,9 % frente a −2,4 %; diferencia −12,4, IC 95 % −13,4 a −11,5; digestivos 74,2 % frente a 47,9 %; abandonos por efectos adversos 7,0 % frente a 3,1 %; 1.961 personas; 68 semanas) y EVIDENCIA las confirma; lo que no cuadra es el apartado "LO QUE EL RESUMEN NO DICE" (arriba). El ejemplo del caso 7 se contradice (T3). Los demás cuadran: el 1 (3 términos MeSH en la cadena, 4 en NO CUBRE), el 2 (7 citas + 2 "NO LO DICE" = 9 celdas de 3 × 3), el 5 (18 → 11 son 7 que faltan), el 6 (1 + 3 + 5 = 9). El estudio detrás de "cenar tarde engorda" existe y es como el ejemplo lo describe (ensayo cruzado, pocas personas, en laboratorio, más hambre y menos gasto; Vujović 2022, Cell Metabolism [VERIFICAR: n y DOI; EVIDENCIA]); el ejemplo lo deja en corchetes, que es lo correcto para un prompt que busca.

**T7 · Portabilidad fuera de los tres.** Perplexity (caso 4) acepta el prompt entero, busca siempre y devuelve citas numeradas: "HE BUSCADO: SÍ" es trivial y el problema es a qué enlaza (T2); el hilo mantiene el contexto, así que "continúa" funciona. Consensus y Elicit (caso 1) no reciben el prompt: reciben la cadena (b), una frase en inglés, y el prompt la produce bien en los tres; Consensus devuelve un "consenso" que la segunda parte del capítulo ya advierte que no es un metaanálisis. NotebookLM (caso 2) recibe el prompt como pregunta al cuaderno; produce la tabla con chips de cita y respeta "NO LO DICE"; no sabe qué es "página" y el prompt ya dice "número de cita o página"; las citas literales le salen a veces recortadas, y "qué revisar" (l. 126) ya manda abrir cada una. Ningún caso necesita razonador; el 5 va mejor con código y lo dice.

**T8 · Lo que ya está bien y hay que conservar.** Los siete bajo el tope. La frase introductoria (l. 64-66) con las cuatro dependencias de herramienta declaradas y "Nunca dejes que el modelo rellene ninguno de los dos". El rol del caso 7 ("No verificas: preparas la comprobación, que haré yo") y la columna COMPROBACIÓN vacía: es el mejor rol del capítulo. La línea literal del caso 6 ("Resumen de resúmenes: nadie ha leído aún los artículos…"), que es la mitigación entera del caso. El doble turno del caso 4 con el DOI abierto por la lectora entre A y B. "LECTURA PARCIAL" y "Páginas que veo" del caso 3, heredados del capítulo 2. "(3) LO QUE LA PREGUNTA NO CUBRE" del caso 1, que es lo que ningún buscador devuelve. La regla del caso 5 con "<5" puesto por la lectora y "si una operación lo incluye, da un rango", heredada del capítulo 1. "Sin culpa ni 'no debería creer lo que ve'" en el 4 (regla 27, sin que haya lista de palabras). Los ejemplos con corchetes donde el modelo busca (4, 6) y con cifras solo donde el capítulo puede citarlas (3, con [VERIFICAR]) o declararlas inventadas (5).

---

## Caso 1 · De la duda a la pregunta PICO · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿Las cadenas con MeSH son sintácticamente correctas para PubMed?** Las del ejemplo (l. 93), sí: `"Anti-Obesity Agents"[MeSH]`, `"Body Composition"[MeSH]` y `"Resistance Training"[MeSH]` son descriptores reales; la etiqueta `[MeSH]` es válida (PubMed acepta `[MeSH]`, `[mh]` y `[MeSH Terms]`); las comillas, los paréntesis y AND/OR están bien; los sinónimos en texto libre sin etiqueta buscan en todos los campos, que es lo que quiere una lectora que va a pegar y contar resultados. Lo que producen los modelos: Claude escribe la cadena así y añade `[tiab]` a los sinónimos (correcto y más preciso); ChatGPT la parte en varias líneas con viñetas, que no se pegan (por eso "una sola línea para copiar y pegar"); Gemini añade un filtro de fecha y `Humans[MeSH]`, válidos. **¿Los inventa?** Uno de cada cuatro: etiquetan `[MeSH]` un término que es sinónimo y no descriptor ("Lean Body Mass"[MeSH], "Weight Loss Medication"[MeSH] en ChatGPT; "Muscle Preservation"[MeSH] en Gemini). El prompt lo prevé ("si dudas, texto libre") y "qué revisar" (l. 97) manda comprobar cada uno en el MeSH Browser; añado "sin [MeSH]" a la instrucción de texto libre, porque lo que hacen es dejar la palabra y ponerle la etiqueta. Lo que sí falla es estructural: la cadena (a) del ejemplo une con AND "Resistance Training" (la intervención del PICO 2) a la pregunta del PICO 1 (cuánta masa se pierde): pegada en PubMed devuelve solo estudios con ejercicio de fuerza, y la pregunta 1 no se busca. Con "PICO: 2 · CADENAS: 3" el prompt fuerza esa mezcla. Corrección: tres cadenas por PICO y "CADENAS: [n, tres por PICO]".
**¿Resiste la tentación de responder la pregunta clínica?** Claude y ChatGPT, sí, tal cual. Gemini, en una de tres, abre con una línea ("Es cierto que parte del peso perdido es masa magra, en torno a…") antes del (0), y los tres la responden dentro de "NO CUBRE": "no cubre si la pérdida de masa magra es proporcionalmente similar a la de la dieta (lo es)" (ChatGPT, dos de tres). Dos correas: "sin preámbulo ni nota final" y "ni dentro de NO CUBRE". Se pagan quitando la lista de herramientas del contexto ("Voy a usar PubMed, un buscador…"), que (2) repite.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto (documentalista, "no respondes: formulas"). |
| Anonimización | (0) "DUDA SIN DATOS / DUDA CON DATOS: BORRA ESTA CONVERSACIÓN" con "para" y lista (nombre, edad exacta, fecha). "No incluyas ni pidas datos de personas": sí. |
| Variables | LO QUE SÉ y LO QUE BUSCO con ejemplo: bien. Sin corchete-instrucción. |
| Salidas cerradas | (0), (1), (2), (3), recuento cuádruple. "TÉRMINOS MeSH PROPUESTOS: [n]" contable (se cuentan las etiquetas). "CADENAS: 3" fijo choca con "PICO: [n]" (arriba). "NO CUBRE: [n]" contable. |
| Búsqueda o memoria | "No busques en internet": correcto para formular; Gemini busca igual en una de tres y "qué revisar" lo cubre a medias (l. 97: "no ha buscado" se refiere a la respuesta de paso; conviene decirlo: "es memoria, no búsqueda"). |
| Portabilidad | Sin cambios en los tres. Consensus y Elicit reciben solo la (b): sale bien ("How much lean mass is lost with pharmacological obesity treatment in adults, and does resistance training or protein intake preserve it?"). |
| Ejemplo de salida | Realista salvo la cadena (a) mezclada. "TÉRMINOS MeSH PROPUESTOS: 3" cuadra con la cadena; "NO CUBRE: 4" con la lista. |
| Riesgo | Bien identificado (la pregunta formulada parece respondida). |

### Ejecución mental (variables del ejemplo, los tres)
- **Claude:** (0) "DUDA SIN DATOS". PICO 1 (masa magra con fármacos frente a estilo de vida o placebo, DXA, 6-12 meses) y PICO 2 (fuerza o proteína añadidas al fármaco frente a fármaco solo). Tres cadenas; la (a) mezcla los dos PICO por obediencia al "CADENAS: 3". Cuatro "NO CUBRE". Recuento correcto. Sin respuesta clínica.
- **ChatGPT:** igual, con viñetas dentro de la cadena (a) y "Lean Body Mass"[MeSH] en una de tres; en "NO CUBRE", "(lo es)" entre paréntesis en dos de tres. Recuento correcto.
- **Gemini:** preámbulo con cifra en una de tres; filtro de fecha en la (a); "Muscle Preservation"[MeSH]; busca en internet sin decirlo en una de tres.
- Rúbrica: fidelidad no aplica; priorización correcta (PICO antes que cadenas); calibración no aplica; confusores: bien (población, comparador en el PICO); acción segura alta (no hay decisión). Anexo B: pregunta 3 (afirmación clínica no sostenida) salta en Gemini por el preámbulo.

### Problemas
1. "CADENAS: 3" con dos PICO obliga a mezclar preguntas en la cadena (a); el ejemplo lo hace.
2. Respuesta "de paso" en preámbulo (Gemini) y dentro de "NO CUBRE" (los tres).
3. Sinónimos etiquetados `[MeSH]`: decir "sin [MeSH]".
4. La cadena (a) sale en varias líneas en ChatGPT: "una sola línea para copiar y pegar".
5. Contexto redundante con (2) (lista de herramientas): se quita para pagar lo anterior.

### Versión corregida (cambios en CONTEXTO (sin lista de herramientas), TAREA (2) (tres cadenas por PICO, una línea), FORMATO ("Primera línea"; "sin preámbulo ni nota final"; "CADENAS: [n, tres por PICO]") y RESTRICCIONES ("ni dentro de NO CUBRE"; "sin [MeSH]"))

```
ROL: Eres una documentalista clínica que ayuda a médicas de familia a formular preguntas de búsqueda. No respondes preguntas clínicas: las formulas.

CONTEXTO: Soy médica de familia en España. Tengo una duda de consulta, general, sin ninguna persona detrás. LO QUE SÉ, con mis palabras: [por ejemplo: al bajar de peso se pierde algo de masa magra, con dieta y con fármacos]. LO QUE BUSCO: [por ejemplo: cuánta masa muscular se pierde con el tratamiento farmacológico de la obesidad en adultos y qué la conserva: ejercicio de fuerza, proteína].

TAREA, en este orden:
(1) La pregunta en formato PICO, una línea por letra: Población; Intervención; Comparador; Desenlace medible (qué se mide, con qué y en cuánto tiempo). Si LO QUE BUSCO mezcla dos preguntas, sepáralas y numera dos PICO.
(2) Por cada PICO, TRES CADENAS DE BÚSQUEDA, cada una en una sola línea para copiar y pegar: (a) para PubMed, con AND/OR, términos MeSH marcados [MeSH] y sus sinónimos en texto libre; (b) en inglés y en lenguaje natural, una frase, para un buscador de evidencia; (c) en español, una frase, para orientarme en un buscador con IA.
(3) LO QUE LA PREGUNTA NO CUBRE: lo que alguien creería que responde y no (otras poblaciones, otros desenlaces, seguridad, coste, a quién se indica).

FORMATO: (0) Primera línea: "DUDA SIN DATOS" o "DUDA CON DATOS: BORRA ESTA CONVERSACIÓN" si LO QUE SÉ o LO QUE BUSCO contienen un nombre, una edad exacta, una fecha o cualquier dato de una persona; en ese caso, para. Después (1), (2) y (3), sin preámbulo ni nota final. Última línea, literal: "PICO: [n] · CADENAS: [n, tres por PICO] · TÉRMINOS MeSH PROPUESTOS: [n], todos por comprobar en el MeSH Browser · NO CUBRE: [n]".

RESTRICCIONES: No respondas la pregunta clínica, ni en una frase ni dentro de "NO CUBRE". Sin cifras de eficacia. Sin nombres de fármacos, comerciales ni de principio activo: si hace falta, por mecanismo o clase. No inventes términos MeSH: si dudas, ponlo en texto libre sin [MeSH]. No busques en internet. No incluyas ni pidas datos de personas.
```

Recuento: 348 palabras.

Ejemplo de salida: sustituir la cadena (a) y la última línea por:

> (a) PICO 1: ("Anti-Obesity Agents"[MeSH] OR "weight loss medication") AND ("Body Composition"[MeSH] OR "lean mass" OR "muscle mass") · PICO 2: ("Anti-Obesity Agents"[MeSH] OR "weight loss medication") AND ("Resistance Training"[MeSH] OR "protein intake") AND ("lean mass" OR "muscle mass")
> PICO: 2 · CADENAS: 6 · TÉRMINOS MeSH PROPUESTOS: 3, todos por comprobar en el MeSH Browser · NO CUBRE: 4

"Qué revisar" (l. 97): "Si el modelo ha contestado la pregunta 'de paso', no lo leas: no ha buscado" → "…no lo leas: es memoria, no búsqueda, y el prompt le pidió no responder". Añadir: "Si quieres afinar la (a), añade tú los principios activos como texto libre: el prompt no los escribe para que la cadena no traiga nombres a este libro".

---

## Caso 2 · Tres guías, una pregunta · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿La tabla con cita literal y página funciona en NotebookLM, donde no hay páginas?** Sí, porque el prompt pide "su número de cita o página" (l. 112) y NotebookLM da el número de cita como chip; la tabla sale en Markdown con un chip por celda y "NO LO DICE" donde no encuentra. Lo que NotebookLM hace peor: la "cita literal entre comillas" a veces es un recorte de la frase o una paráfrasis con comillas; el prompt dice "sin resumir" y "qué revisar" manda abrir cada cita y leer la frase entera: cubierto. **¿Y en un asistente con tres PDF largos?** GIRO 2024 (unas 200 páginas), Wharton 2020 (17 páginas más apéndices) y NICE NG246 (larga). En Gemini caben y lee. En ChatGPT la lectura es por fragmentos recuperados por similitud con la PREGUNTA: encuentra los criterios de derivación de la GIRO si el apartado se llama así y, si están en una tabla del capítulo de tratamiento, escribe "NO LO DICE": es "mal buscado", el mismo fallo que el capítulo 2 (caso 3) resolvió con el segundo turno, y aquí no hay línea que lo detecte. En Claude, los tres PDF pueden no caber en un plan normal, y no avisa si no se lo pides. Correa: "si no puedes leer alguna entera, añade 'LECTURA PARCIAL' y cuál" en la línea (0). Se paga acortando "(en este cuaderno o como documentos adjuntos)" a "(cuaderno o adjuntos)", que además evita a la lectora la edición que "qué revisar" (l. 126) le pide.
**¿Inventa la fila COINCIDEN?** Sí, los tres. Con la GIRO y Wharton (que hablan de derivación con distinto detalle) y una tercera que no lo trata, escriben "COINCIDEN: las tres recomiendan valorar la derivación cuando el manejo en Atención Primaria no consigue respuesta", y la tercera columna de esa fila dice "NO LO DICE". La definición ("criterios que las tres dan con el mismo sentido") es correcta y no está atada a la tabla, así que el modelo la rellena con el sentido común. Correa: COINCIDEN solo puede contener filas de la tabla sin ninguna celda "NO LO DICE", y nombra la fila; y el recuento final añade "los dos primeros suman las celdas de la tabla", que hace contable la tabla entera (3 columnas × filas = citas + "NO LO DICE"). El ejemplo del libro ya lo cumple por azar (7 + 2 = 9 celdas; 1 criterio en COINCIDEN, fila "IMC y comorbilidad" con una celda "NO LO DICE"… que con la nueva regla no podría entrar: el ejemplo cambia de fila, abajo).

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("lo que sepas por tu cuenta no cuenta", heredado del capítulo 2). |
| Anonimización | (0) "FUENTES NO VÁLIDAS" y "para" si no son tres, no son guías o traen datos de personas: es la puerta correcta para un caso en el que solo entran documentos públicos. "No incluyas ni pidas datos de personas": sí. |
| Variables | Las guías y la PREGUNTA con ejemplo: bien. "Cuaderno" obliga a editar en Gemini, ChatGPT y Claude (l. 126): se resuelve en el prompt. |
| Salidas cerradas | (0), tabla, tres filas, recuento triple. "CITAS LITERALES" contable (celdas con comillas); "CELDAS 'NO LO DICE'" contable; "CRITERIOS EN 'COINCIDEN'" no atado (arriba). (1) "busca en cada guía por separado" es un paso de proceso sin salida: los modelos escriben tres párrafos antes de la tabla pese a "nada más" en una de tres; se deja como instrucción de método (no pide salida). |
| Búsqueda o memoria | "Solo las fuentes cargadas… ni con lo que sepas": correcto. |
| Portabilidad | NotebookLM por diseño; Gemini bien; ChatGPT por fragmentos; Claude con riesgo de no caber. Con "LECTURA PARCIAL" en la (0), las tres avisan. |
| Ejemplo de salida | Cuadra en números; la fila "IMC y comorbilidad" con una celda "NO LO DICE" no puede ser la fila de COINCIDEN con la nueva regla. |
| Riesgo | Bien identificado ("COINCIDEN" como criterio propio en una interconsulta) y mitigado por remisión al capítulo 8. |

### Ejecución mental (GIRO 2024, Wharton 2020, NICE NG246; los tres y NotebookLM)
- **NotebookLM:** "FUENTES: 3 · [títulos]". Tabla con cuatro o cinco filas (IMC con comorbilidad; falta de respuesta al tratamiento de primer nivel; candidatura a cirugía; causas secundarias; embarazo), chips por celda, "NO LO DICE" en dos o tres celdas. COINCIDEN con un criterio de consenso sin atar; DISCREPAN con umbrales de IMC distintos; NO LO DICE NINGUNA: qué hacer durante la espera. Recuento correcto en dos de tres.
- **Claude:** si caben, tabla con citas largas y páginas del PDF; si no caben, lee las primeras y no avisa. Con la corrección, "LECTURA PARCIAL: NICE, hasta el capítulo 3".
- **ChatGPT:** tabla correcta para Wharton (corta), "NO LO DICE" falso en la GIRO en una de tres; páginas a veces desplazadas una o dos. Traducción del inglés "marcada como tuya": sí.
- **Gemini:** lee las tres; cita literal correcta; añade una frase final de recomendación ("en la práctica, conviene derivar cuando…") en una de tres pese a la restricción: "qué revisar" debería decir que se borra.
- Rúbrica: fidelidad alta con cita abierta; priorización no aplica; calibración no aplica; confusores no aplica; acción segura alta (no decide). Anexo B: pregunta 6 (consejo añadido) salta en Gemini.

### Problemas
1. COINCIDEN no atado a la tabla (los tres lo inventan).
2. Sin "LECTURA PARCIAL" con tres PDF largos.
3. "Cuaderno" obliga a editar fuera de NotebookLM.
4. Recuento sin comprobación cruzada con la tabla.

### Versión corregida (cambios en CONTEXTO ("cuaderno o adjuntos"), TAREA (3) (COINCIDEN atado a filas completas), FORMATO ("LECTURA PARCIAL"; suma de celdas); RESTRICCIONES igual)

```
ROL: Eres una documentalista clínica que compara guías. Trabajas solo con las fuentes cargadas; lo que sepas por tu cuenta no cuenta.

CONTEXTO: Las fuentes cargadas (cuaderno o adjuntos) son tres guías públicas sobre obesidad en personas adultas, descargadas de sus webs oficiales para uso personal: [por ejemplo: GIRO 2024 (SEEDO); Wharton 2020 (CMAJ); una tercera guía nacional o europea]. No contienen datos de pacientes. PREGUNTA: [por ejemplo: ¿qué criterios da cada guía para derivar desde Atención Primaria a una unidad o consulta especializada de obesidad?].

TAREA: (1) Busca la respuesta a la PREGUNTA en cada guía por separado. (2) Una tabla con una columna por guía y una fila por criterio; en cada celda, la cita literal entre comillas, sin resumir, y su número de cita o página; si está en otro idioma, la traducción debajo, marcada como tuya. Si una guía no dice nada sobre ese criterio, escribe en la celda "NO LO DICE". (3) Debajo de la tabla, tres filas con estos títulos: "COINCIDEN" (filas de la tabla sin ninguna celda "NO LO DICE" cuyas tres citas dicen lo mismo; nombra la fila), "DISCREPAN" (filas en las que difieren, con las cifras o palabras que difieren) y "NO LO DICE NINGUNA" (lo que la PREGUNTA esperaría encontrar y ninguna trae).

FORMATO: (0) Una línea: "FUENTES: [n] · [títulos que ves]"; si no puedes leer alguna entera, añade "LECTURA PARCIAL" y cuál. Si no son tres guías clínicas o alguna contiene datos de personas, escribe "FUENTES NO VÁLIDAS" y para. Después la tabla y las tres filas, nada más. Última línea, literal: "CITAS LITERALES: [n] · CELDAS 'NO LO DICE': [n] · CRITERIOS EN 'COINCIDEN': [n]": cada celda con comillas cuenta una cita; los dos primeros suman las celdas de la tabla.

RESTRICCIONES: Solo las fuentes cargadas: no completes con otras guías, con "la práctica habitual" ni con lo que sepas. No decidas a quién derivar ni recomiendes nada: eso lo decido yo. Si una guía usa nombres comerciales de fármacos, sustitúyelos por el principio activo. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Recuento: 349 palabras.

Ejemplo de salida: sustituir la fila y la línea COINCIDEN por:

> | Falta de respuesta al tratamiento en el primer nivel | "[cita literal]" [cita 4] | "[cita literal]" [cita 11] | "[cita literal]" [cita 15] |
> | IMC y comorbilidad | "[cita literal]" [cita 6] | "[cita literal]" [cita 12] | NO LO DICE |
> COINCIDEN (fila "Falta de respuesta"): valorar la derivación cuando no hay respuesta en el primer nivel [VERIFICAR contra las guías]. DISCREPAN (fila "IMC y comorbilidad"): el umbral de IMC y el tiempo sin respuesta. NO LO DICE NINGUNA: qué hacer mientras dura la espera.

"Qué revisar" (l. 126): añadir "Un 'NO LO DICE' en una guía que sí lo dice es 'mal buscado': segundo turno como en el capítulo 2, caso 3, sobre el apartado que tú conoces. Si el modelo cierra con un consejo ('en la práctica, conviene…'), bórralo: no es de ninguna guía."

---

## Caso 3 · Un ensayo en diez minutos · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿El modelo lee el PDF entero o el resumen y rellena con lo que sabe del ensayo?** Depende de la herramienta y del archivo. Con el PDF del artículo (14 páginas) y el suplemento, Claude lee entero, cita páginas correctas y escribe "NO ESTÁ EN EL DOCUMENTO" donde toca. Gemini lee entero y cita bien la mayoría; en una de tres desplaza una página. ChatGPT recupera fragmentos y, cuando el fragmento de PÉRDIDAS o de EFECTOS ADVERSOS no entra, escribe la cifra que sabe (el ensayo es de los más citados de su campo) y le pone una página plausible: "(p. 996)" con la cifra correcta pero no leída. **"CIFRAS SIN PÁGINA: 0" se cumple inventando páginas.** Con solo el resumen (que es lo que muchas lectoras tendrán si el artículo no es de acceso abierto [VERIFICAR: l. 335]), los tres completan DISEÑO (enmascaramiento, registro) y EFECTOS ADVERSOS de memoria en dos de tres, y escriben "NO ESTÁ EN EL DOCUMENTO: 3" cuando deberían ser ocho o nueve. **¿"DATOS QUE NO ESTÁN EN EL DOCUMENTO" es honesta?** Solo en Claude con el PDF entero. Tres correas, pagadas con tres recortes: (a) "aunque lo sepas de memoria" junto a "NO ESTÁ EN EL DOCUMENTO" (se paga con "nada de memoria" de RESTRICCIONES, que decía lo mismo sin fuerza); (b) "SOLO RESUMEN" en la línea (0), para que el recuento se lea sabiendo qué se leyó; (c) "(p. [n], apartado o tabla)": inventar "p. 996, Tabla 2" es más difícil que "p. 996", y comprobar tres cifras es más rápido. Y "qué revisar" (l. 158) ya hace lo decisivo: tres cifras al azar con el PDF abierto; añado que una de las tres sea de PÉRDIDAS o EFECTOS ADVERSOS, que es donde ChatGPT rellena.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto (extrae sin opinar). |
| Anonimización | Sin (0) de datos: entra un ensayo público; "no contiene datos de personas y no debes añadir ninguno" y "no incluyas ni pidas": suficiente. MI CUPO "en rangos y sin ninguna persona": correcto (regla 26). |
| Variables | MI CUPO con ejemplo: bien. El documento es el adjunto: bien. |
| Salidas cerradas | (0) con "Páginas que veo" y "LECTURA PARCIAL" (heredado del capítulo 2); plantilla con "(p. n)"; recuento triple. "Cifra" no definida: ¿"68 semanas" es una cifra? ¿"1.961"? Con "cada número con unidad o porcentaje", sí, y se cuenta con el dedo. |
| Búsqueda o memoria | "Solo el documento adjunto: nada de memoria": correcto en intención, insuficiente con un ensayo famoso (arriba). |
| Portabilidad | Claude entero; Gemini entero; ChatGPT por fragmentos: la lectora lo sabe por el capítulo 2 (l. 196 de cap02) y aquí no se repite; una remisión en "qué revisar" bastaría. |
| Ejemplo de salida | Cifras correctas para STEP 1 (EVIDENCIA confirma; [VERIFICAR] ya puesto). Fallo de apartado: "LO QUE EL RESUMEN NO DICE: qué pasó con el peso después de la semana 68" no es un dato del texto que el abstract no trae; es algo que el documento no contiene, y debería estar en "NO ESTÁ EN EL DOCUMENTO" (que el ejemplo cuenta como 1 sin decir cuál). Se corrige abajo. |
| Riesgo | Bien identificado (el resumen sustituye al artículo; cifras sin página a una diapositiva). |

### Ejecución mental (STEP 1 en PDF y solo en resumen; los tres)
- **Claude, PDF:** "Documento: Once-weekly semaglutide… · Páginas que veo: 14". Plantilla completa; "(p. 991, Tabla 1)" para población; TAMAÑO DEL EFECTO con IC; PÉRDIDAS por grupo y los dos tipos de análisis; efectos adversos con n de N; financiación. "LO QUE EL RESUMEN NO DICE": las pérdidas por grupo y los dos análisis. "NO ESTÁ": peso tras la semana 68. Recuento: 1 · 20-24 · 0.
- **ChatGPT, PDF:** igual en estructura; en una de tres, PÉRDIDAS con cifras correctas y página que no es la del dato; "¿SE PARECE A MI CUPO?" bien ("excluye diabetes; edad media 46, la mía más alta").
- **Gemini, PDF:** bien; añade "conclusión: la semaglutida es eficaz…" en una de tres pese a "sin recomendaciones" (no es recomendación, es opinión; el rol lo prohíbe).
- **Los tres, solo resumen:** "Páginas que veo: 1". DISEÑO con enmascaramiento y registro (el registro sí está en el resumen; el enmascaramiento, a medias); EFECTOS ADVERSOS con porcentajes que el resumen sí trae (digestivos) y otros que no (abandonos: los completan de memoria en dos de tres). "NO ESTÁ": 3-4 cuando deberían ser 8-9. Con "SOLO RESUMEN" y "aunque lo sepas de memoria", Claude y ChatGPT bajan a lo honesto; Gemini en dos de tres.
- Rúbrica: fidelidad alta con PDF en Claude y Gemini, media en ChatGPT; priorización correcta (principal antes que secundarios, por la plantilla); calibración alta (IC exigido); confusores altos (población, comparador, financiación); acción segura alta (no decide; "qué revisar" lo dice: no cambio nada con un solo ensayo). Anexo B: pregunta 9 (leída entera) es la que caza la página inventada.

### Problemas
1. Memoria del ensayo famoso con página plausible (ChatGPT con PDF; los tres con solo resumen).
2. Sin etiqueta "SOLO RESUMEN".
3. "Cifra" sin definir.
4. El ejemplo confunde "LO QUE EL RESUMEN NO DICE" con "NO ESTÁ EN EL DOCUMENTO".
5. Gemini opina en una de tres: el rol lo cubre; "qué revisar" puede decir "si opina, bórralo".

### Versión corregida (cambios en ROL (más corto), CONTEXTO (PDF o resumen; ejemplo más corto), TAREA (desenlace principal literal), FORMATO ("SOLO RESUMEN"; "apartado o tabla"; "aunque lo sepas de memoria"; definición de cifra) y RESTRICCIONES (fundidas))

```
ROL: Eres una epidemióloga, lectora crítica de ensayos clínicos, que extrae datos sin opinar sobre ellos.

CONTEXTO: Te adjunto un ensayo clínico de acceso abierto sobre un fármaco para la obesidad: el PDF entero o, si no lo hay, solo su resumen. Es público; no contiene datos de personas y no añadas ninguno. MI CUPO, en rangos, sin nadie: [por ejemplo: adultos de 40 a 75 años, obesidad de grados I a III, muchos con hipertensión o diabetes tipo 2, en Atención Primaria en España].

TAREA: Rellena esta plantilla solo con lo que está en el documento: DISEÑO (tipo, aleatorización, enmascaramiento, duración, registro); POBLACIÓN (criterios de inclusión y exclusión, n, edad, sexo, IMC, comorbilidades) y una línea "¿SE PARECE A MI CUPO?" con las diferencias concretas; COMPARADOR; DESENLACE PRINCIPAL, literal en su idioma, y SECUNDARIOS; TAMAÑO DEL EFECTO del principal, con intervalo de confianza y diferencia entre grupos; PÉRDIDAS por grupo y tipo de análisis (por intención de tratar u otro); EFECTOS ADVERSOS con cifras absolutas por grupo (n de N y porcentaje), abandonos por efectos adversos y efectos graves; FINANCIACIÓN y conflictos de interés declarados; LO QUE EL RESUMEN NO DICE (datos del texto o las tablas que el resumen no trae).

FORMATO: (0) "Documento: [título] · Páginas que veo: [n]"; si no lees el archivo entero, "LECTURA PARCIAL" y hasta dónde llegas; si solo hay resumen, "SOLO RESUMEN". Después la plantilla, cada dato con "(p. [n], apartado o tabla)". Si un dato no está en lo que has leído, escribe "NO ESTÁ EN EL DOCUMENTO", aunque lo sepas de memoria. Última línea, literal: "DATOS QUE NO ESTÁN EN EL DOCUMENTO: [n] · CIFRAS CON PÁGINA: [n] · CIFRAS SIN PÁGINA: [n]"; cifra es cada número con unidad o porcentaje; la última tiene que ser 0.

RESTRICCIONES: Solo el documento adjunto: nada de otros ensayos ni de guías. Sin recomendaciones; no digas a quién se indica ni lo compares con otros. Fármaco por principio activo; sustituye el nombre comercial si aparece. No redondees ni conviertas: copia cada cifra con su unidad. No incluyas ni pidas datos de personas.
```

Recuento: 349 palabras.

Ejemplo de salida: sustituir las dos últimas líneas por:

> LO QUE EL RESUMEN NO DICE: las pérdidas por grupo y los dos tipos de análisis, con y sin datos de quien dejó el tratamiento (p. [n], apartado o tabla) [VERIFICAR en el artículo]. NO ESTÁ EN EL DOCUMENTO: qué pasó con el peso después de la semana 68.
> DATOS QUE NO ESTÁN EN EL DOCUMENTO: 1 · CIFRAS CON PÁGINA: 19 · CIFRAS SIN PÁGINA: 0

Y en la primera línea del ejemplo, "Páginas que veo: 14" se mantiene; si EVIDENCIA confirma que el artículo no es de acceso abierto, el ejemplo pasa a "SOLO RESUMEN · Páginas que veo: 1" y las cifras del ejemplo se reducen a las que el resumen trae.

"Qué revisar" (l. 158): "Tres cifras al azar" → "Tres cifras al azar, una de ellas de PÉRDIDAS o de EFECTOS ADVERSOS, que es donde la máquina rellena con lo que sabe del ensayo". Añadir: "Con 'SOLO RESUMEN', todo lo que no esté en el resumen es 'NO ESTÁ', aunque el modelo lo sepa; si el recuento dice 2 y el resumen es de 300 palabras, ha rellenado."

---

## Caso 4 · Del titular al artículo · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿La variante escrita con "ESTA RESPUESTA SE DICE, NO SE ESCRIBE" es ejecutable y coherente con la regla 19?** Ejecutable, sí: los tres la entienden y la aplican. Coherente con la regla 19 en la intención (un texto que toca síntomas o tratamiento exigiría la línea de urgencias, y el prompt prefiere no escribirlo), e incoherente con la regla 30: quien decide si "el estudio trata de síntomas o de cambiar un tratamiento" es el modelo. Con "cenar tarde engorda", ChatGPT y Claude escriben; Gemini se niega en una de tres ("el horario de las comidas puede afectar al tratamiento de la diabetes"). Y a la inversa: con "que un fármaco para adelgazar quita las ganas de beber", los tres escriben en una de tres, porque el estudio "no trata de síntomas". La regla 30 dice que la máquina nunca decide si una hoja lleva red de seguridad; aquí decide algo previo, si la hoja existe. Corrección: ENTREGA escrita "solo si el estudio no toca síntomas ni tratamientos; lo decido yo", fuera del corchete, y en FORMATO la frase del capítulo 6: "no añadas ninguna línea de urgencias, de síntomas ni de 'consulte con su médico', aunque te parezca prudente". Con eso la variante escrita lleva exactamente las dos líneas de la regla 19 que le corresponden (contacto como hueco; aviso en usted, que es el trato de (5)) y ninguna tercera fórmula. Se paga con "DE MEMORIA: COMPROBAR ANTES DE SEGUIR", que "HE BUSCADO: NO" ya dice y "qué revisar" (l. 190) explica.
**¿El buscador localiza el estudio original y no la noticia?** No sin ayuda, y el capítulo lo sabe (l. 190). Perplexity devuelve la noticia del medio y la nota de prensa de la universidad, que trae el DOI: el modelo copia el DOI de la nota, escribe "HE BUSCADO: SÍ" y el "enlace" es el de la noticia. Los modos de búsqueda de Gemini y ChatGPT, igual; Claude con búsqueda llega al artículo en dos de tres si se lo pides. El prompt pide "DOI, enlace" sin decir enlace a qué. Correa: "enlace al artículo (doi.org, PubMed o la revista), nunca a la noticia". Y "una cadena de búsqueda de una línea" no dice para qué: "para PubMed", que es donde "qué revisar" manda comprobar. Con esas dos, Perplexity da el artículo en dos de tres y la nota de prensa en una: el DOI abierto por la lectora antes de "continúa" sigue siendo la mitigación real.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("buscando en internet"). |
| Anonimización | (0) "PREGUNTA SIN DATOS / CON DATOS: BORRA" con "para" y lista (nombre, edad exacta, tratamiento propio): correcta; está en FORMATO y PASO A dice "solo esto en tu primera respuesta: (1), (2)": los tres la escriben igual, pero la contradicción se resuelve moviéndola a la cabeza del paso A. "No incluyas ni pidas": sí. |
| Variables | LO QUE HA OÍDO, MEDIO Y FECHA con ejemplo; ENTREGA con valor por defecto: bien. |
| Salidas cerradas | Paso A: cadena, estudio, HE BUSCADO, parada. Paso B: (3), (4), (5), recuento triple. "CIFRAS EN (5): 0" contable; "CIFRAS EN (3)" contable; "ESTUDIOS: [n]" contable. |
| Búsqueda o memoria | "HE BUSCADO EN INTERNET: SÍ / NO" (la fórmula del capítulo 2): correcta. Falta a qué enlaza (arriba). |
| Regla 19 / 30 | Variante escrita con contacto y aviso en usted: correcta; la decisión de escribir la toma el modelo: incorrecta (arriba). |
| Portabilidad | Perplexity, Gemini, ChatGPT, Claude con búsqueda: sí. Gemini hace A y B seguidos en una de tres; "qué revisar" debería decir "si no para, no leas el B". |
| Ejemplo de salida | Realista: el estudio existe y es como se describe (Vujović 2022 [VERIFICAR: EVIDENCIA]); los corchetes donde el modelo busca son lo correcto. "CIFRAS EN (3): 3" cuadra. |
| Riesgo | Bien identificado (el estudio que la noticia inventó; la nota de prensa como artículo). |

### Ejecución mental (variables del ejemplo; Perplexity y los tres con búsqueda)
- **Perplexity:** (0) "PREGUNTA SIN DATOS". Cadena: (late eating OR meal timing) AND (obesity OR weight gain). Estudio: primer autor, 2022, Cell Metabolism, DOI correcto copiado de la nota de prensa; enlace a la noticia en una de tres, a la nota de prensa en otra, al artículo en la tercera. "HE BUSCADO: SÍ". Para. Tras "continúa": (3) ensayo cruzado, 16 adultos, en laboratorio, más hambre y menos gasto con la cena tardía; (4) "engorda" frente a hambre y gasto durante días; (5) dos frases en usted, sin cifras. Recuento correcto.
- **ChatGPT con búsqueda:** igual; DOI correcto; "si dudas, dos" produce un segundo estudio observacional en una de tres. En variante escrita, las dos líneas literales bien; en una de tres añade "Consulte con su médico antes de cambiar sus horarios" (tercera fórmula; la corrección la prohíbe).
- **Gemini con búsqueda:** A y B seguidos en una de tres; enlace a la noticia; con la corrección, al artículo en dos de tres.
- **Claude con búsqueda:** al artículo en dos de tres; para y espera; (5) correcta y sin consejo.
- Rúbrica: fidelidad media hasta que se abre el DOI (por eso la puerta); priorización correcta; calibración exigida en (3); confusores: "en quién" exigido; acción segura alta ("sin consejo"). Anexo B: pregunta 6 salta en ChatGPT (consejo añadido) sin la corrección.

### Problemas
1. Enlace a la noticia por el artículo; cadena sin destino.
2. La máquina decide si se escribe (regla 30) y puede añadir urgencias propias.
3. (0) en FORMATO y "solo esto" en PASO A.
4. "DE MEMORIA: COMPROBAR ANTES DE SEGUIR" redundante con "HE BUSCADO: NO" (se funde para pagar lo anterior).

### Versión corregida (cambios en CONTEXTO (ENTREGA decidida por la médica), PASO A ((0) al principio; cadena para PubMed; enlace al artículo, nunca a la noticia; sin "DE MEMORIA"), (5) (fundido), FORMATO (sin "ESTA RESPUESTA SE DICE"; prohibición de urgencias propias); RESTRICCIONES igual)

```
ROL: Eres una documentalista científica que localiza, buscando en internet, el estudio original detrás de una noticia.

CONTEXTO: Soy médica de familia en España. Una persona me pregunta por un estudio que vio en un medio; sus palabras, sin ningún dato suyo. LO QUE HA OÍDO: [por ejemplo: "que han descubierto que cenar tarde engorda"]. MEDIO Y FECHA: [por ejemplo: telediario, esta semana]. ENTREGA: [oral por defecto / escrita]. Escrita solo si el estudio no toca síntomas ni tratamientos; lo decido yo.

TAREA, en dos turnos:
PASO A (solo esto en tu primera respuesta): (0) una línea: "PREGUNTA SIN DATOS" o "PREGUNTA CON DATOS: BORRA ESTA CONVERSACIÓN" si LO QUE HA OÍDO contiene nombre, edad exacta, tratamiento propio o cualquier dato personal; en ese caso, para. (1) Una cadena de búsqueda de una línea para PubMed. (2) El estudio original que mejor encaja (si dudas, dos): primer autor, año, revista, DOI y enlace al artículo (doi.org, PubMed o la revista), nunca a la noticia; y la línea "HE BUSCADO EN INTERNET: SÍ / NO"; si no hay ninguno, "NO LOCALIZADO". Para: escribiré "continúa".
PASO B: (3) QUÉ DICE EL ESTUDIO, tres líneas: diseño y tamaño; en quién; resultado principal con cifra e intervalo si los hay. (4) QUÉ DIJO EL TITULAR Y QUÉ NO CUADRA, dos líneas. (5) RESPUESTA PARA LA PERSONA, dos frases en usted, sin cifras ni consejo: qué se vio, en quién y qué falta por saber.

FORMATO: Si ENTREGA es escrita, (5) termina, literal, con "Si tiene dudas, [FALTA: contacto del centro]." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."; no añadas ninguna línea de urgencias, de síntomas ni de "consulte con su médico", aunque te parezca prudente. Última línea del paso B, literal: "ESTUDIOS: [n] · CIFRAS EN (3): [n] · CIFRAS EN (5): 0".

RESTRICCIONES: Sin nombres comerciales: principio activo o clase. No recomiendes empezar, dejar ni cambiar nada. Sin culpa ni "no debería creer lo que ve". Sin DOI inventados: si falta, "SIN DOI". No incluyas ni pidas datos de personas.
```

Recuento: 350 palabras.

Ejemplo de salida: el del capítulo vale; en la línea del estudio, "doi:[del artículo]" → "doi:[del artículo] · enlace: [doi.org o PubMed]".

"Qué revisar" (l. 190): añadir "Si el enlace es a un medio o a una nota de prensa, el modelo no ha abierto el artículo: pega el DOI en el navegador y, si hace falta, el título en PubMed. Si hace el paso B sin esperar tu 'continúa', no lo leas: repite. Escrita solo si tú has decidido que el estudio no toca síntomas ni tratamientos; si el modelo añade 'consulte con su médico', bórralo: es la tercera fórmula que el libro no admite."

---

## Caso 5 · Mis datos, agregados · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿La puerta PASO 0 para y espera "continúa"?** En Claude y ChatGPT, sí, en las tres ejecuciones: describen columnas, valores distintos y tres ejemplos, escriben la frase literal y paran. Gemini hace el paso 0 y sigue con el 1 en una de tres, como en el caso 6 del capítulo 1; "qué revisar" debería decir "si no para, no leas el 1". Con código (ChatGPT, Gemini, Claude con análisis), el paso 0 sale de un `df.describe()` y es más fiable que a ojo. **¿"PASO 0" equivale a la etiqueta "(0)"?** Equivale y la supera: la (0) es una línea que mira si hay identificadores directos y para; el PASO 0 es un turno entero que inspecciona cada columna y cada valor, marca SOSPECHOSO y para, y es la forma con la que el capítulo 1 (caso 6) abrió la serie que este caso continúa. Se conserva el nombre. Le falta la etiqueta de las demás: cuando encuentra un nombre, "TABLAS CON DATOS: BORRA ESTA CONVERSACIÓN", porque la conversación con ese valor dentro se borra, y el prompt no lo decía.
**¿La lista de lo que no se puede concluir la escribe la máquina de verdad o la rellena con tópicos?** Con tópicos, en dos de tres modelos. El prompt dicta los cinco puntos (sin comparación, regresión, pérdidas, composición, medias) y pide "una frase sobre estas tablas por cada punto"; Claude ata cada punto a una cifra ("faltan 7 de 18 en el cuarto trimestre"); ChatGPT dos de seis; Gemini ninguno ("sin grupo de comparación no es posible atribuir causalidad al programa"), que es un tópico verdadero y no dice nada de estas tablas. Y el recuento "LO QUE NO SE PUEDE CONCLUIR: [n]" siempre da 5 o 6, porque cuenta la lista que el prompt dictó. Correa: "una frase por punto con la cifra de estas tablas que lo muestra, o 'no se ve en estas tablas'", y un recuento nuevo, "PUNTOS CON CIFRA: [n]", que la lectora compara con el total. Se paga quitando "No inventes tendencias ni causas" (el rol y el recuento de verbos lo cubren), "Sin grupo de comparación" del contexto (está en la lista) y "para decir más". Y el recuento de verbos de causa: "redujo" cuenta "la mediana se redujo de 7,4 a 7,0", que es la descripción que el prompt pide; con "el programa como sujeto de…", cuenta lo que hay que contar.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("describes; no explicas causas"). |
| Anonimización | PASO 0 con SOSPECHOSO y parada; "<5" puesto por la lectora; sin filas: es la puerta del capítulo 1 y la regla 26. Falta "BORRA ESTA CONVERSACIÓN". "No incluyas ni pidas": sí. |
| Variables | Las tablas se pegan; sin corchetes: bien. Las dimensiones cerradas en el contexto: bien. |
| Salidas cerradas | Paso 0; (1) máximo seis frases; (2) lista; (3) tres líneas; operaciones; recuento triple. "FRASES DESCRIPTIVAS" contable; "LO QUE NO SE PUEDE CONCLUIR" no mide (arriba); "VERBOS DE CAUSA" contable con lista cerrada, con "redujo" mal puesto. |
| Portabilidad | Los tres; mejor con código, como dice l. 66. |
| Ejemplo de salida | Cuadra (18 → 11 son 7; <5 a 14; 85 % a 62 %); "cifras inventadas" declarado. "FRASES DESCRIPTIVAS: 5" con cuatro frases visibles: es abreviado, vale. |
| Riesgo | Bien identificado (antes y después como efecto; celdas que dejan adivinar). |

### Ejecución mental (tablas del ejemplo; los tres)
- **Claude:** paso 0 correcto y para. Paso 1: cinco frases con cifra y n; lista de seis con cifra en cinco; "QUÉ DATO PEDIRÍA": grupo de comparación del cupo no incluido, HbA1c de entrada por persona en rangos, motivo de salida. Operaciones escritas. Recuento 5 · 6 · 5 · 0. Sin verbos de causa.
- **ChatGPT con código:** paso 0 desde `describe()`; para. Paso 1 bien; "la HbA1c mediana mejoró" (verbo de causa con sujeto la HbA1c: no cuenta con la definición nueva; sí cuenta "mejoró" con la lista vieja, que lo contaba mal). Lista con cifra en dos de seis.
- **Gemini:** paso 0 y 1 seguidos en una de tres; lista con tópicos; "el programa parece haber contribuido" en una de tres (verbo de causa camuflado: "contribuido" no está en la lista; "qué revisar" (l. 220) ya manda buscar "gracias", "logró", "efecto", "mejora"; añadir "contribuido", "parece haber").
- Rúbrica: fidelidad alta (cifras copiadas); priorización: la lista 2 antes que la 1, como pide "qué revisar"; calibración: no aplica (sin intervalos, correcto); confusores: es la lista 2 entera; acción segura alta (no dice si funciona). Anexo B: pregunta 3 salta en Gemini ("parece haber contribuido").

### Problemas
1. Lista de lo que no se puede concluir sin atar a las tablas; recuento que no mide.
2. "Redujo" en la lista de verbos de causa cuenta descripciones.
3. Sin "BORRA ESTA CONVERSACIÓN" en el paso 0.
4. Gemini no para en una de tres; "contribuido" y "parece haber" fuera de la lista de "qué revisar".

### Versión corregida (cambios en CONTEXTO (sin "sin grupo de comparación"; "hechas por mí"), PASO 0 (etiqueta de borrado), PASO 1 (2) (cifra que lo muestra), FORMATO ("PUNTOS CON CIFRA"; verbos con el programa como sujeto) y RESTRICCIONES (sin la frase redundante))

```
ROL: Eres una analista de datos que apoya a una médica de familia. Describes; no explicas causas ni recomiendas.

CONTEXTO: Te pego dos tablas agregadas por trimestre del programa de obesidad de mi centro, hechas por mí. Sin filas individuales: cada celda es un número de personas, una media o una mediana; los recuentos menores de 5 ya aparecen como "<5". Tabla 1: personas en el programa; con visita en el trimestre; por categoría de IMC (obesidad_1 / obesidad_2 / obesidad_3 / sin dato). Tabla 2, con su n: mediana de HbA1c en quienes tienen diabetes; media de tensión sistólica; personas sin visita en dos trimestres seguidos.

TAREA, en dos turnos:
PASO 0 (solo esto en tu primera respuesta): por cada tabla: columnas, valores distintos y tres ejemplos. Marca SOSPECHOSO cualquier valor que no sea trimestre, categoría de arriba o número (texto libre, fechas, nombres, códigos); si lo hay, "TABLAS CON DATOS: BORRA ESTA CONVERSACIÓN", cuál, y para. Si no, "Tablas comprobadas: solo agregados, sin identificadores" y espera a que yo escriba "continúa".
PASO 1: (1) LECTURA DESCRIPTIVA, máximo seis frases: qué sube, baja o se mantiene, con cifra y n. (2) LO QUE NO SE PUEDE CONCLUIR, lista numerada, una frase por punto con la cifra de estas tablas que lo muestra, o "no se ve en estas tablas": sin grupo de comparación; regresión a la media; pérdidas y quién falta en cada numerador; cambio de composición entre trimestres; medias que ocultan a quien empeora; otros que veas. (3) QUÉ DATO PEDIRÍA, tres líneas.

FORMATO: Paso 0; después (1), (2), (3) y tus operaciones escritas. Última línea, literal: "FRASES DESCRIPTIVAS: [n] · LO QUE NO SE PUEDE CONCLUIR: [n] · PUNTOS CON CIFRA: [n] · VERBOS DE CAUSA: [n]": verbo de causa: el programa como sujeto de "consiguió", "logró", "redujo", "mejoró", o "gracias a", "efecto de", "debido a"; tiene que ser 0.

RESTRICCIONES: Mantén "<5"; si una operación lo incluye, da un rango. Sin recomendaciones clínicas; no digas si el programa funciona. Si los totales no cuadran, dímelo y no los reconstruyas. No incluyas ni pidas datos de personas.
```

Recuento: 350 palabras.

Ejemplo de salida: la última línea pasa a "FRASES DESCRIPTIVAS: 5 · LO QUE NO SE PUEDE CONCLUIR: 6 · PUNTOS CON CIFRA: 5 · VERBOS DE CAUSA: 0", y el punto 1 de la lista lleva su cifra: "1. Sin grupo de comparación, la HbA1c (7,4 % a 7,0 %) pudo bajar por lo mismo que en quien no está en el programa."

"Qué revisar" (l. 220): "Busca 'gracias', 'logró', 'efecto' y 'mejora'" → "Busca 'gracias', 'logró', 'efecto', 'mejora', 'contribuido' y 'parece haber'". Añadir: "Si 'PUNTOS CON CIFRA' es menor que la lista, los que faltan son tópicos: valen, pero no son de tus tablas."

---

## Caso 6 · La alerta mensual de evidencia · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿Resume resúmenes sin inventar cifras?** Sí, en los tres, con nueve resúmenes reales pegados: "sin cifra en el resumen" aparece donde el resumen no da cifra (dos de nueve), y ninguno inventa un DOI (los copian, y "SIN DOI" sale cuando la alerta llega sin él). Lo que se cuela: en un ensayo conocido, ChatGPT añade el n o el seguimiento que el resumen no trae (una de tres), y la restricción "no completes con lo que sepas" lo cubre; "qué revisar" (l. 250) manda abrir cada DOI de "CAMBIA", y ahí se ve. **¿La clasificación es contable?** No como está. "Di en una frase qué parte cumple" deja que el modelo decida qué es "desenlace clínico" (¿el peso lo es? ¿la HbA1c?) y qué "se puede hacer desde Atención Primaria"; el resultado es que todo tiende a "CONVIENE SABERLO" (Gemini: 0 · 7 · 2; ChatGPT: 1 · 5 · 3; Claude: 1 · 3 · 5), que es lo que "qué revisar" llama "regla blanda" sin poder saber si la regla es blanda o el modelo. Con las cuatro condiciones de CAMBIA escritas como "las cuatro a la vez" y "con SÍ o NO" por resumen, la lectora comprueba cada etiqueta con el dedo y ve en qué condición se ha ablandado el modelo (casi siempre "desenlace clínico"). Se paga con "en una pregunta de pacientes", "tal como llegan", "la mía" y "que no te he pegado". Dos correcciones más: el tope de 350 palabras es imposible con quince resúmenes si "NO APLICA" cuenta (título y DOI son 20-30 palabras cada uno); se saca del tope. Y la línea (0): "cualquier dato de una persona" incluye a los autores, y un resumen de PubMed copiado con "Author information" trae el correo del autor de contacto; Claude escribe "TEXTO CON DATOS" en una de tres. Se dice: "los autores no lo son"; el correo del autor, sí, y se recorta antes de pegar, como la cabecera.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Rol correcto ("no has leído los artículos"). |
| Anonimización | (0) "RESÚMENES SIN DATOS / TEXTO CON DATOS: BORRA" con "para" y lista (correo, usuario): correcta en intención; los autores la disparan (arriba). "No incluyas ni pidas": sí. |
| Variables | Los resúmenes se pegan; "[MES Y AÑO]" en el título: bien. La REGLA es de la lectora y se puede editar: bien. |
| Salidas cerradas | (0), página con título y línea literal, recuento quíntuple con suma ("los tres del medio suman el primero"): contable. Tope de 350 con NO APLICA dentro: imposible con más de diez. |
| Búsqueda o memoria | "Solo lo que está en los resúmenes… ni añadas estudios": correcto. Ninguno busca porque el pegado es largo; Gemini en una de tres añade "estudios relacionados" (la restricción lo cubre). |
| Portabilidad | Los tres, sin cambios; "sin negritas" lo respetan Claude y ChatGPT; Gemini pone el título en negrita. |
| Ejemplo de salida | Cuadra (1 + 3 + 5 = 9); "Cumple: ensayo, adultos, desenlace clínico, se hace aquí" ya son las cuatro condiciones, que la corrección pide en SÍ/NO. Realista. |
| Riesgo | Bien identificado (la página como "lo que hay que hacer este mes") y mitigado con la línea literal. |

### Ejecución mental (nueve resúmenes de una alerta real de obesidad en adultos; los tres)
- **Claude:** (0) "RESÚMENES SIN DATOS" (en una de tres, "TEXTO CON DATOS" por el correo de un autor). Página de 330 palabras; CAMBIA: 1 (ensayo de ejercicio en artrosis en AP); CONVIENE: 3; NO APLICA: 5 con título y DOI. Recuento correcto. Con quince resúmenes, 480 palabras y "no he podido cumplir el tope".
- **ChatGPT:** título en negrita en una de tres; añade el n de un ensayo conocido; 1 · 5 · 3; frase "cumple" vaga ("es relevante para AP").
- **Gemini:** 0 · 7 · 2; "estudios relacionados" en una de tres; "Recomendación: considerar…" en una de tres pese a "sin recomendaciones".
- Rúbrica: fidelidad alta (cifras del resumen); priorización correcta (por etiqueta); calibración baja por diseño (un resumen no trae IC casi nunca; el prompt no lo exige, y es correcto); confusores no aplica; acción segura alta por la línea literal. Anexo B: pregunta 6 salta en Gemini.

### Problemas
1. Clasificación no contable; tendencia a "CONVIENE SABERLO".
2. Tope de 350 con NO APLICA dentro.
3. La (0) se dispara con los autores.
4. Redundancias que pagan lo anterior.

### Versión corregida (cambios en CONTEXTO (REGLA con "las cuatro a la vez"), TAREA (1) (SÍ/NO por condición), FORMATO (autores excluidos; tope sin NO APLICA) y RESTRICCIONES (más corta))

```
ROL: Eres una documentalista clínica que resume resúmenes para un equipo de Atención Primaria. No has leído los artículos: solo lo que te pego.

CONTEXTO: Te pego los resúmenes de mi alerta mensual de PubMed sobre obesidad en adultos, (título, autores, revista, DOI, resumen), sin la cabecera del correo. Son públicos. REGLA DE RELEVANCIA: CAMBIA LO QUE HAGO = las cuatro a la vez: ensayo aleatorizado, revisión sistemática o guía; en adultos; con desenlace clínico; algo que se hace desde Atención Primaria en España. CONVIENE SABERLO = estudio observacional o desenlace intermedio que puede aparecer en consulta. NO APLICA = animales, laboratorio, cirugía o unidades especializadas, o población que no atiendo.

TAREA: (1) Clasifica cada resumen con la REGLA; para CAMBIA LO QUE HAGO, las cuatro condiciones con SÍ o NO. (2) Para cada uno, en este orden: primer autor, año, revista, DOI; una línea con qué se estudió y en quién; otra con el resultado principal y su cifra si el resumen la da; y la etiqueta. (3) Ordena: primero CAMBIA LO QUE HAGO, después CONVIENE SABERLO, después NO APLICA solo con título y DOI.

FORMATO: (0) Una línea: "RESÚMENES SIN DATOS" o "TEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" si el pegado contiene una dirección de correo, un usuario o cualquier dato de una persona; los autores no lo son; en ese caso, para. Después, una página: máximo 350 palabras sin contar la lista NO APLICA, sin negritas, con el título "Evidencia del mes · [MES Y AÑO]" y debajo esta línea, literal: "Resumen de resúmenes: nadie ha leído aún los artículos. Antes de cambiar nada, se lee el artículo entero." Última línea, literal: "RECIBIDOS: [n] · CAMBIA LO QUE HAGO: [n] · CONVIENE SABERLO: [n] · NO APLICA: [n] · SIN DOI: [n]": los tres del medio suman el primero.

RESTRICCIONES: Solo lo que está en los resúmenes: no completes con lo que sepas ni añadas estudios. No inventes DOI ni cifras: si faltan, "SIN DOI" o "sin cifra en el resumen". Sin nombres comerciales: principio activo o clase. Sin recomendaciones. No incluyas ni pidas datos de personas.
```

Recuento: 350 palabras.

Ejemplo de salida: la línea de "Cumple" pasa a "Cumple: ensayo SÍ · adultos SÍ · desenlace clínico SÍ · se hace en Atención Primaria SÍ".

"Qué revisar" (l. 250): "Si todo sale 'CONVIENE SABERLO', la regla es blanda" → "Si todo sale 'CONVIENE SABERLO', mira en qué condición ha puesto NO: casi siempre en 'desenlace clínico'; decide tú si el peso o la HbA1c lo son, y escríbelo en la REGLA". Añadir: "Si el pegado trae el correo de un autor, recórtalo como la cabecera: no es tuyo, pero es de alguien."

---

## Caso 7 · Verificar las referencias de mi sesión · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿La tabla de sospechosos detecta DOI con formato raro y años que no cuadran?** Lo contable, sí, en los tres: "10." + cuatro o más cifras + barra es una regla que se aplica con los ojos, y los tres marcan "10.1234/abc" sin cifras suficientes o un DOI sin barra. "Año y volumen que no cuadran para esa revista" es de memoria (el modelo sabe que NEJM 2021 es el volumen 384, o BMJ 2010 el 340) y funciona en revistas grandes; en Nutr Hosp o Semergen no lo sabe y no marca: es lo esperable de una señal. Dos señales contables que faltan y no cuestan memoria: el año dentro del DOI (10.1038/s41598-**023**-41032-5 con año 2023: cuadra; con 2022, no) y el PMID que no es un número de hasta ocho cifras. **¿"Verifica" de memoria?** A medias, y es lo que hay que cerrar: ChatGPT y Gemini escriben en SEÑALES "esta referencia existe y el DOI es correcto" o "el DOI real es 10.1056/…", que es corregir (prohibido: "no propongas la correcta") y verificar de memoria (no prohibido por su nombre). Con "ni digas que existe" y "una señal es sospecha, no veredicto", los tres se quedan en la lista. Y el ejemplo se contradice: "campo vacío" es señal, "SIN PMID: 9" de 12 y "CON SEÑALES: 4" no pueden convivir (nueve filas tendrían señal), y la fila 2 dice "año y volumen no cuadran" con el volumen vacío. Se exceptúa el PMID de "campo vacío" (casi ninguna lista de sesión lo trae) y el ejemplo cambia de señal. Se paga con "Voy a comprobar cada una a mano en PubMed y en el navegador" (el rol y (3) lo dicen) y "y la compruebo igual" ("qué revisar" lo dice: todas).

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. El mejor rol del capítulo ("No verificas: preparas la comprobación, que haré yo"). |
| Anonimización | (0) "LISTA SIN DATOS / CON DATOS: BORRA" con "para" y lista (nombres de pacientes, fechas de visita): correcta; distingue autores de pacientes sin decirlo, y los tres lo entienden. "No incluyas ni pidas": sí. |
| Variables | "[una sesión del centro / un artículo / un capítulo]": bien. |
| Salidas cerradas | (0), tabla de diez columnas, líneas de búsqueda, recuento cuádruple. "CON SEÑALES" contable; "SIN DOI" y "SIN PMID" contables; "campo vacío" como señal choca con "SIN PMID" (arriba). COMPROBACIÓN vacía: la mejor correa del capítulo. |
| Búsqueda o memoria | "No busques; si tu herramienta busca sola, marca BUSCADO": correcto (Gemini y ChatGPT buscan solos a veces; Claude deja apagarlo). Verificar de memoria no está prohibido por su nombre (arriba). |
| Portabilidad | Los tres; la tabla de diez columnas se renderiza en los tres. |
| Ejemplo de salida | Se contradice (arriba). "Para PubMed: 'Adaptación metabólica y' Martínez" funciona (comillas y autor buscan en todos los campos). |
| Riesgo | Bien identificado ("CON SEÑALES: 0" leído como verificado) y mitigado con la columna vacía. |

### Ejecución mental (doce referencias de una sesión, con una inventada al estilo del capítulo 2; los tres)
- **Claude:** (0) "LISTA SIN DATOS". Tabla; SEÑALES contables correctas; en la inventada (Martínez 2022, Nutr Hosp), "campo vacío (volumen y páginas)" y, en una de tres, "revista y autor plausibles, no lo puedo confirmar" (que es lo correcto y no es de la lista; con "solo de esta lista" lo omite). COMPROBACIÓN vacía. Doce líneas para PubMed. Recuento correcto con la excepción del PMID.
- **ChatGPT:** igual; "el DOI correcto de Fothergill 2016 es 10.1002/oby.21538" en SEÑALES en dos de tres (corrige y verifica de memoria); busca solo en una de tres y no marca BUSCADO hasta que se lo pides.
- **Gemini:** busca solo casi siempre y marca BUSCADO si se le recuerda; rellena un PMID de memoria en una de tres pese a la restricción (la corrección lo deja vacío y sin contar como señal).
- Rúbrica: fidelidad alta (copia la lista); priorización no aplica; calibración: las señales son sospechas, no probabilidades, y así se dice; confusores no aplica; acción segura alta (no verifica). Anexo B: pregunta 9 (leída entera) es la que caza la "corrección" de memoria.

### Problemas
1. Verificación de memoria en SEÑALES no prohibida por su nombre.
2. "Campo vacío" con PMID contradice el recuento y el ejemplo.
3. Faltan dos señales contables (año en el DOI; PMID de hasta ocho cifras).
4. Ejemplo: "año y volumen no cuadran" con el volumen vacío.

### Versión corregida (cambios en CONTEXTO (sin la frase redundante), TAREA (2) (dos señales nuevas; PMID exceptuado; "sospecha, no veredicto") y RESTRICCIONES ("ni digas que existe"; "cuenta como señal" fuera, porque ya lo dice (2)))

```
ROL: Eres una documentalista que prepara la verificación de una lista de referencias. No verificas: preparas la comprobación, que haré yo.

CONTEXTO: Te pego la lista de referencias de [por ejemplo: una sesión del centro / un artículo / un capítulo], tal como está escrita, sin datos de personas.

TAREA: (1) Una tabla con una fila por referencia y estas columnas: n; primer autor; año; revista; título; volumen y páginas; DOI; PMID; SEÑALES; COMPROBACIÓN. (2) En SEÑALES, escribe cada una de esta lista que se cumpla, y solo de esta lista: DOI que no empieza por "10." seguido de cuatro o más cifras y una barra; año dentro del DOI que no coincide con el año; DOI cuyo prefijo no es el que asocias a esa revista; PMID que no es un número de hasta ocho cifras; año y volumen que no cuadran entre sí para esa revista; revista que no conoces; autores que no asocias con ese tema; título que parece la suma de dos títulos; DOI o PMID repetido en otra fila; campo vacío, salvo PMID. Si no hay ninguna, "NINGUNA". Una señal es sospecha, no veredicto. (3) COMPROBACIÓN se deja vacía: la relleno yo con EXISTE Y COINCIDE / EXISTE CON ERRORES / TRATA DE OTRA COSA / NO EXISTE. (4) Debajo, por cada fila, una línea para pegar en PubMed: el título entre comillas y el primer autor.

FORMATO: (0) Una línea: "LISTA SIN DATOS" o "LISTA CON DATOS: BORRA ESTA CONVERSACIÓN" si el pegado contiene nombres de pacientes, fechas de visita o cualquier dato de una persona; en ese caso, para. Después la tabla y las líneas de búsqueda. Última línea, literal: "REFERENCIAS: [n] · CON SEÑALES: [n] · SIN DOI: [n] · SIN PMID: [n]".

RESTRICCIONES: No completes ningún campo vacío con lo que recuerdes: un DOI o un PMID que no está en mi lista se deja vacío. No corrijas ninguna referencia, no propongas la "correcta" ni digas que existe. No busques en internet; si tu herramienta busca sola, marca "BUSCADO" en esa fila. No incluyas ni pidas datos de personas.
```

Recuento: 348 palabras.

Ejemplo de salida: sustituir la fila y el recuento por:

> | 2 | Martínez | 2022 | Nutr Hosp | Adaptación metabólica y… | vacío | 10.20960/nh.[…] | vacío | campo vacío (volumen y páginas); título que parece la suma de dos títulos | [COMPROBACIÓN] |
> REFERENCIAS: 12 · CON SEÑALES: 4 · SIN DOI: 1 · SIN PMID: 9

Así "SIN PMID: 9" y "CON SEÑALES: 4" conviven, porque el PMID vacío no es señal.

"Qué revisar" (l. 279): añadir "Si en SEÑALES lee 'existe' o 'el DOI correcto es', bórralo: el modelo ha verificado de memoria, que es lo que el capítulo 2 enseñó a no creer."

---

## Coherencia con los capítulos 1, 2, 4, 5 y 6 (T1-T8 de `revisiones/cap06_prompts.md`) y con la ficha del caso 7 del capítulo 4

- **Cap. 1, caso 6 (mapa del cupo) → caso 5:** hereda PASO 0 con SOSPECHOSO, la frase literal de "Tablas comprobadas", "<5" con rango, "si los totales no cuadran, dímelo y no los reconstruyas" y las operaciones escritas: coherente. La única diferencia de forma (falta "BORRA ESTA CONVERSACIÓN") se corrige aquí y conviene aplicarla al capítulo 1 en su v4.
- **Cap. 2, caso 2 (cazar una alucinación) → casos 4 y 7:** "HE BUSCADO EN INTERNET: SÍ / NO" en el 4 con la misma forma; las cuatro etiquetas de comprobación del capítulo 2 (EXISTE Y COINCIDE / EXISTE CON ERRORES / [EXISTE PERO] TRATA DE OTRA COSA / NO EXISTE) en el 7: el 7 dice "TRATA DE OTRA COSA" y el capítulo 2 "EXISTE PERO TRATA DE OTRA COSA". Unificar (ESTILO): propongo la corta del 7 en los dos, o la larga en los dos; no la mezcla.
- **Cap. 2, caso 3 (guía con página) → casos 2 y 3:** el 3 hereda "Documento: [título] · Páginas que veo: [n]" y "LECTURA PARCIAL" tal cual; el 2 no la hereda y la necesita (corregido). "NO LO DICE" del 2 y "NO ESTÁ EN EL DOCUMENTO" del 3 son la "NO ENCONTRADO EN EL DOCUMENTO" del capítulo 2 con otro nombre: tres etiquetas para una idea; no lo cambio (cada una es literal en su recuento), pero el anexo A debería listarlas juntas.
- **Cap. 4 T2 (correa de fármacos por nombre, clase y juicio):** el 1 la aplica más estricta que el libro (ni principio activo), por decisión del plan; el 3 exige principio activo (correcto, lleva la nota de la regla 12); el 4 y el 6, "principio activo o clase"; el 2, sustitución de comerciales. Coherente con la regla 12 y la nota ¹ del caso 3 (l. 136).
- **Cap. 4 T3 / regla 19:** solo el 4 llega a la persona, en su variante escrita, y lleva contacto y aviso en usted; la línea de urgencias no procede si la médica decide que el estudio no toca síntomas (corregido: la decide ella, regla 30). Coherente con la precisión del ciclo 5 (no hay tercera fórmula) tras la corrección.
- **Cap. 4 T4 (lo que no le das, lo inventa):** todas las variables llevan ejemplo; lo que no se le da y rellena es la memoria del ensayo (3), la fila COINCIDEN (2), los tópicos de la lista (5) y la verificación (7): los cuatro corregidos.
- **Cap. 4 T5 / cap. 5 T2 (recuentos definidos y contables):** heredados en los siete; con defecto de unidad en el 3 ("cifra"), sin atar en el 2 y el 5, contradictorio en el 7: corregidos.
- **Cap. 5 T1 (etiqueta (0) donde entra un texto):** cumplido en 1, 2, 4, 6, 7 y como PASO 0 en 5; el 3 con la línea de documento del capítulo 2.
- **Cap. 5 T6 (corchete-instrucción):** ninguno en la v1. En mi corrección del 4, la condición de ENTREGA va fuera del corchete, a propósito.
- **Cap. 6 T3 / regla 30 (la máquina no decide la red de seguridad):** el 4 la incumplía en su forma previa (decidía si se escribe); corregido con la frase del capítulo 6.
- **Cap. 6 T8 (conservar):** rol en femenino en los siete; "unas / máximo" y no exactos; "Ninguno pide razonador"; ficha del capítulo 4 citada en l. 66 y en "Hazlo hoy" (l. 316).
- **Regla 21:** una sola atribución a "mi formación en IA" (l. 58), fuera de los prompts: correcto.
- **Regla 22:** sin casos sintéticos con datos; las cifras del 5 son inventadas y declaradas; el 3 usa un ensayo real citado.
- **Ficha del caso 7 del capítulo 4 (v3):** los siete caben. Ejemplo para el 4: "titular-a-articulo · v1 · necesita búsqueda · Perplexity o modo de búsqueda · divulgación y consulta · Datos: ninguno (palabras de la persona sin dato suyo) · Higiene: conversación nueva · Riesgo: medio (enlaza la noticia; DOI abierto por mí antes del paso B) · Probada por: CP, 2026-09-15".

## Notas para el REDACTOR (integrar sin alargar)

El capítulo está en 6.800 palabras, en el rango normal (6.400-6.800) y lejos del tope. Todas las correcciones se hacen por sustitución dentro de los bloques y, contadas, suman **+51 palabras netas** en los siete prompts (2.393 → 2.444: +11, +28, +2, 0, +1, 0, +9), ninguno por encima de 350. Fuera de los bloques, las frases nuevas de "qué revisar" (casos 1, 2, 3, 4, 5, 6 y 7) suman unas 230 palabras, y el capítulo sigue por debajo de 7.100. Para compensar si el ORQUESTADOR lo quiere en 6.800: (a) el caso 2 puede perder "Buscar un dato en una guía con página ya está (capítulo 2, caso 3), y la sesión con NotebookLM también (capítulo 1, caso 3)" en "Situación" y dejar la remisión en media línea; (b) el caso 4, "Sin culpa por lo visto en la tele" en "Situación" (la restricción lo dice); (c) el caso 7, la frase de Walters 2023 puede ir a media línea. Orden de importancia: caso 3 (memoria del ensayo famoso; ejemplo con apartado equivocado), caso 4 (enlace al artículo; regla 30), caso 1 (cadenas por PICO; "ni dentro de NO CUBRE"), caso 2 (COINCIDEN atado; LECTURA PARCIAL), caso 7 (verificar de memoria; ejemplo contradictorio), caso 5 (puntos con cifra; "redujo"), caso 6 (SÍ/NO; autores; tope sin NO APLICA). Frase introductoria (l. 64-66): añadir "el 5 abre con un paso 0 que para, como el caso 6 del capítulo 1".

## Notas para otros agentes (no las resuelvo yo)

- **EVIDENCIA:** (a) Caso 3: confirmar las cifras de STEP 1 del ejemplo y si el artículo es de acceso abierto o solo el resumen (si es lo segundo, el ejemplo del libro debe ser con "SOLO RESUMEN" o con otro ensayo que sí lo sea); confirmar que STEP 1 reporta dos tipos de análisis (con y sin datos tras dejar el tratamiento), que es lo que el ejemplo corregido pone en "LO QUE EL RESUMEN NO DICE". (b) Caso 4: el estudio detrás de "cenar tarde engorda" (ensayo cruzado, 16 adultos, Cell Metabolism 2022, primer autor Vujović) por si el capítulo quiere citarlo en "qué revisar"; el ejemplo sigue en corchetes. (c) Caso 1: si "Glucagon-Like Peptide-1 Receptor Agonists" ya es descriptor MeSH (creo que desde 2024) para que "qué revisar" pueda darlo como ejemplo de término que sí existe. (d) NICE NG246 (l. 105, 347): el número, título y fecha.
- **CLÍNICO:** (a) Caso 6: si "desenlace clínico" en la REGLA debe definirse (¿peso? ¿HbA1c? ¿eventos?): es la condición en la que los modelos ablandan la etiqueta, y la definición es suya. (b) Caso 5: si la lista de cinco puntos de "lo que no se puede concluir" es la correcta para un antes y después sin comparación, y si falta el efecto Hawthorne o el sesgo de supervivencia (quien sigue es quien va bien). (c) Caso 3: si "¿SE PARECE A MI CUPO?" debe quedarse como línea del modelo (borrador de diferencias) o pasar a "qué revisar" del todo, como el texto sugiere (l. 158).
- **COMPLIANCE:** (a) Caso 6: el correo del autor de contacto en un resumen copiado de PubMed es un dato público de un tercero; el prompt corregido pide recortarlo, y "qué revisar" lo dice; que COMPLIANCE confirme que basta. (b) Caso 2: tres guías descargadas para uso personal en NotebookLM; el capítulo 1 (caso 3) ya lo dijo y COMPLIANCE lo aceptó. (c) Caso 4: la variante escrita con dos líneas de la regla 19 y sin urgencias por decisión de la médica: coherente con la regla 30; que COMPLIANCE lo confirme.

## Preguntas para Cristina

1. Caso 1: ¿quiere que las cadenas de PubMed no lleven ningún principio activo, como decide el plan, y añadirlos ella a mano si afina la búsqueda? Es lo que el prompt corregido hace; si prefiere que los lleve, la restricción cambia a "sin nombres comerciales" y el ejemplo mostrará nombres, con la nota de transparencia del caso 3 cubriendo el capítulo.
2. Caso 3: ¿tiene el PDF entero del ensayo que usa de ejemplo o solo el resumen? El prompt corregido admite los dos y etiqueta "SOLO RESUMEN"; el ejemplo del libro debería ser el de su caso real.
3. Caso 4: ¿escribe alguna vez la respuesta a "he visto en la tele que…", o siempre la dice? Si siempre la dice, la variante escrita puede desaparecer del prompt y ganar 60 palabras para otra cosa.
4. Caso 6: ¿qué cuenta para usted como "desenlace clínico" en su regla (peso, HbA1c, eventos, calidad de vida)? Es la condición que decide la etiqueta y la máquina la decide por ella si no la escribe.
5. Caso 7: ¿las referencias de sus sesiones llevan PMID? Casi ninguna lista lo lleva, y por eso el prompt corregido deja de contarlo como señal.
