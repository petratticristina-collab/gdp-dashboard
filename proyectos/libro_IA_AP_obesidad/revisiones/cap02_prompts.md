# Revisión PROMPTS · Capítulo 2 · v1

> Agente: PROMPTS (ingeniero de prompts) · Fecha: 2026-09-11 · Ámbito: exclusivamente los seis prompts y la ficha que el capítulo ofrece al lector (Casos 1-7). No se revisa el texto expositivo ni las referencias.
> Método: el mismo que en el capítulo 1. Para cada prompt se comprueba la estructura rol · contexto · tarea · formato · restricciones, la instrucción de anonimización con comprobación humana previa (decisión editorial 7 de `biblia.md`), la claridad de las variables entre corchetes con ejemplo por defecto, que las salidas sean cerradas y deterministas (regla T2 del capítulo 1: nada de "pregúntame si dudas"), la portabilidad Gemini / ChatGPT / Claude, el realismo del ejemplo de salida y la identificación del riesgo. Cada prompt se ha ejecutado mentalmente con un caso sintético y la salida se ha leído con la rúbrica fidelidad · priorización · calibración · confusores · acción segura.

## Resumen de veredictos

| Caso | Título | Veredicto | Motivo principal |
|---|---|---|---|
| 1 | La misma pregunta en tres modelos | **mejorar (leve)** | "No busques en internet" no es controlable en Gemini ni en ChatGPT; el nombre de modelo y la fecha de corte autoinformados son poco fiables y el capítulo no lo dice; la escala de certeza no está definida. |
| 2 | Cazar una alucinación | **mejorar** | El ejemplo omite la columna "título" (la que sirve para buscar). Con la pregunta tal cual, los modelos actuales aciertan casi siempre porque la literatura de adaptación metabólica es canónica: hay que empujar al modelo fuera del canon para que el ejercicio enseñe lo que quiere enseñar. Misma nota de búsqueda que el caso 1. |
| 3 | Lo que se pierde en medio | **mejorar** | La etiqueta ENCONTRADO / NO ENCONTRADO va después de la cita, con lo que el modelo ya ha recitado de memoria cuando la escribe (el propio ejemplo lo demuestra). Falta paso 0 (páginas que ve), frase ancla, distinción página del PDF / página impresa y nota de portabilidad: en ChatGPT y Gemini un PDF largo no se lee, se busca por fragmentos; en NotebookLM no hay páginas. |
| 4 | Leer una etiqueta nutricional | **reescribir** | Sin puerta de legibilidad, el modelo estima lo borroso con seguridad; sin regla para envases con varias tablas (100 g / ración / preparado / con leche) las mezcla; sin regla de idiomas elige uno al azar; sin lista cerrada de azúcares el recuento cambia según el modelo. Falta la comprobación aritmética que delata una lectura errónea y el aviso sobre la ubicación GPS de las fotos del móvil. |
| 5 | Qué nivel de IA exige esta tarea | **mejorar (leve)** | Buen prompt, hereda las correcciones del capítulo 1. Falta la regla explícita que asigna el nivel: sin ella, cada modelo decide con su criterio y la tabla no es auditable. "RAZONADOR O FRONTERA" mezcla un modo con un nivel. |
| 6 | Chat frente a razonador | **mejorar (leve)** | Sólido. Falta la regla de tres cambios para el caso inventado (arquetipo), la definición de la escala de certeza, la trazabilidad deducción → hecho y una nota de portabilidad sobre los modos, con un plan B cuando el plan gratuito no tiene razonador. |
| 7 | Inventario de lo que tengo | **listo** | Ficha clara. Añadir dos líneas: memoria entre conversaciones y qué pasa con los archivos subidos. |

Ningún prompt es peligroso tal como está. Uno requiere reescritura completa (Caso 4), no porque sea inútil sino porque en los tres escenarios que más se van a dar en consulta (foto regular, envase multilingüe, envase con dos tablas) devuelve una transcripción segura y equivocada, y la persona que la lee no tiene forma de notarlo. Los Casos 3 y 4 son los que reciben más trabajo por indicación del ORQUESTADOR.

---

## Hallazgos transversales (afectan a varios casos)

**T1 · "No busques en internet" no es una instrucción, es un deseo.** Los Casos 1 y 2 dependen de que el modelo responda de memoria. En Claude la búsqueda se desactiva en la configuración y el modelo lo respeta. En ChatGPT no hay interruptor: el modelo decide buscar si le parece útil, y con una pregunta sobre referencias le parece útil casi siempre. En Gemini la búsqueda de Google forma parte del producto y el usuario no puede apagarla. Consecuencia: en dos de las tres herramientas el ejercicio del Caso 2 puede salir con cinco referencias reales, y el lector concluir que el problema no existe. Norma para ambos casos: (a) mantener la instrucción, porque a veces funciona; (b) pedir una línea final determinista ("HE BUSCADO EN INTERNET: SÍ / NO"); (c) enseñar la señal externa: si la respuesta trae enlaces, iconos de fuente o un bloque "Fuentes", ha buscado, diga lo que diga. Añadir esto en la frase introductoria de los casos y en "qué revisar" de los Casos 1 y 2.

**T2 · El modelo no sabe quién es.** El Caso 1 pide "el nombre de tu modelo y tu fecha de corte". Los tres modelos contestan, y con frecuencia mal: ChatGPT se llama a sí mismo por la versión anterior, Gemini da la familia sin versión, Claude acierta la familia y a veces falla la versión; la fecha de corte sale con meses de error. No es un defecto del prompt, es una lección: el nombre fiable está en el desplegable, no en la respuesta. Debe decirse en "qué revisar" del Caso 1 y, de paso, refuerza el paso 1 de "Hazlo hoy".

**T3 · Escalas de certeza sin definir.** El Caso 2 define SEGURA / PROBABLE / DUDOSA con precisión. Los Casos 1 y 6 usan ALTA / MEDIA / BAJA sin definirlas, así que cada modelo las rellena con su propio umbral y el lector compara etiquetas que no significan lo mismo. Propongo una definición única para todo el libro, que puede ir al glosario de `biblia.md`: **ALTA** = lo sostendría cualquier manual o guía con estos datos; **MEDIA** = compatible, pero hay explicaciones o estudios discrepantes; **BAJA** = plausible, no lo afirmaría sin comprobarlo.

**T4 · La etiqueta va antes que el contenido.** Cuando se pide "escribe la cita y, debajo, si la has encontrado" (Caso 3) o "transcribe y, si no se lee, pon ILEGIBLE" (Caso 4), el modelo genera primero el contenido y luego se juzga a sí mismo; para entonces ya ha recitado o estimado. La forma determinista es al revés: primero la etiqueta (ENCONTRADO / NO ENCONTRADO; legibilidad BUENA / REGULAR / MALA), después el contenido solo si la etiqueta lo permite. Es la misma idea del capítulo 1 (Caso 1, paso 0): la decisión vive en el orden que obligas a seguir, no dentro del modelo. Aplicado en las versiones corregidas de los Casos 3 y 4.

**T5 · Higiene de la herramienta, tres cosas nuevas que el capítulo 1 no cubría.** (a) Las fotos del móvil llevan ubicación GPS y fecha en los metadatos; no todas las herramientas los eliminan al subir. Una captura de pantalla de la foto no los lleva. Va en el Caso 4. (b) Los archivos subidos no desaparecen al cerrar la pestaña: quedan en la conversación y, en alguna herramienta, en una biblioteca de archivos aparte. "Borrar la conversación" es lo mínimo; comprobar la biblioteca, lo correcto. Va en los Casos 3, 4 y en la ficha del Caso 7. (c) La "memoria" entre conversaciones (ChatGPT, Gemini y Claude la tienen o la están activando) hace que un caso sintético o un dato pegado por error reaparezcan semanas después aunque la conversación se haya borrado. Va en la ficha del Caso 7.

**T6 · Un PDF largo no se lee, se busca.** El capítulo explica "lost in the middle" (Liu 2024) como si el modelo leyera el documento entero. En Claude, si cabe en la ventana, es así. En ChatGPT y en Gemini, un PDF de cierto tamaño se trocea y el modelo recupera los fragmentos que parecen relevantes a la pregunta: no hay "medio" que se pierda, hay fragmentos que no se recuperan. Para el lector la consecuencia es la misma (el dato enterrado no aparece) y el remedio también (dirigir la atención, segundo turno), pero cambia una cosa: NO ENCONTRADO puede significar "no lo he buscado con las palabras adecuadas", y el turno 2 funciona porque cambia la búsqueda, no porque cambie la lectura. Propongo una frase en la nota de portabilidad del Caso 3, sin tocar el texto expositivo (eso es del REDACTOR).

**T7 · Resuelto desde el capítulo 1.** Género del rol unificado en femenino en los seis prompts; "unas 150 palabras" en vez de recuentos exactos; POR ACLARAR y REVISAR PRIVACIDAD como salidas deterministas en el Caso 5; frase introductoria de portabilidad matizada por casos. Buen trabajo del REDACTOR; solo hay que retocar la frase introductoria para los Casos 1, 2 y 6 (ver abajo).

**Frase introductoria corregida** (sustituye "Los casos 1, 2, 5 y 6 funcionan igual en Gemini, ChatGPT y Claude; el 3 y el 4 dependen de que tu plan admita archivos e imágenes; el 7 no usa IA"):

> Los casos 1, 2, 5 y 6 se pegan igual en Gemini, ChatGPT y Claude. Dos matices: en los casos 1 y 2, "sin buscar en internet" solo se puede garantizar en la herramienta que te deje apagar la búsqueda (hoy, Claude); en las demás, mira si la respuesta trae enlaces. En el caso 6, el modo razonador depende del plan; te digo qué hacer si no lo tienes. El 3 y el 4 dependen de que tu plan admita archivos e imágenes; el 7 no usa IA.

---

## Caso 1 · La misma pregunta en tres modelos · veredicto: MEJORAR (leve)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, los cinco. |
| Anonimización y comprobación humana previa | Sí: "No hay ningún paciente detrás: no incluyas ni pidas datos de personas". Aquí no entra ningún dato; suficiente. |
| Variables con ejemplo por defecto | Sí: `[pregunta general, por ejemplo: …]`. Clara. |
| Salidas cerradas | Sí: SIN FUENTE, NO DISPONIBLE. Pero la escala ALTA / MEDIA / BAJA no está definida (T3). |
| Portabilidad | Necesita nota: "No busques en internet" (T1). |
| Ejemplo de salida | Realista. La tabla es exactamente lo que devuelven los tres. Ver nota para CLÍNICO sobre la fila del GLP-1. |
| Riesgo principal | Bien identificado (votar por cómo suena). Falta el segundo: creer el nombre de modelo autoinformado (T2). |

### Ejecución mental (pregunta por defecto, tres pestañas, conversaciones nuevas)
- **Gemini:** párrafo correcto (leptina baja, grelina sube, PYY y GLP-1 bajan, gasto energético baja), cita Sumithran 2011 y a veces Rosenbaum 2010, ambas reales. Con frecuencia busca en Google aunque se le diga que no y añade enlaces; la línea final dice "Soy Gemini" sin versión y una fecha de corte aproximada.
- **ChatGPT:** párrafo parecido; añade con frecuencia una cifra ("el gasto baja hasta 300 kcal/día") sin fuente, que el formato no prohíbe. Se identifica a menudo con una versión anterior a la que aparece en el desplegable.
- **Claude:** respeta "sin buscar"; marca más SIN FUENTE que los otros dos; identifica la familia y a veces falla la versión.
- En los tres: la tabla tiene entre 5 y 9 filas y los umbrales de ALTA / MEDIA no coinciden, así que la comparación entre modelos es en parte una comparación entre escalas.

Rúbrica: fidelidad alta en el párrafo; calibración no comparable sin escala común; acción segura correcta (no hay decisión).

### Problemas
1. "No busques en internet" no se puede garantizar en Gemini ni en ChatGPT (T1). Pedir una línea final determinista y enseñar la señal externa.
2. Escala de certeza sin definir (T3).
3. Cifras sin fuente: el formato permite que el párrafo lleve números que la tabla no cubre. Cerrar: sin cifras salvo que vayan con fuente.
4. Incoherencia leve de rol: el modelo es "médica de familia" y en la última línea debe decir "el nombre de tu modelo". Los tres lo resuelven, pero conviene marcar "fuera del rol".
5. "Qué revisar" no advierte de que el nombre autoinformado es poco fiable (T2).

### Versión corregida
```
ROL: Eres médica de familia con formación en obesidad como enfermedad crónica.

CONTEXTO: Respondo a una pregunta clínica general para una sesión docente de Atención Primaria. No hay ningún paciente detrás: no incluyas ni pidas datos de personas. Es un ejercicio de comparación entre modelos: responde solo con lo que sabes, sin buscar en internet.

TAREA: Responde a esta pregunta: "[pregunta general, por ejemplo: ¿Qué cambios hormonales explican que se recupere el peso después de una dieta?]".

FORMATO, en este orden:
(1) Un párrafo de unas 150 palabras.
(2) Una tabla con cada afirmación del párrafo, una por fila, en tres columnas: afirmación; certeza; fuente. Certeza con uno de estos valores: ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, pero hay estudios o explicaciones discrepantes), BAJA (plausible, no lo afirmarías sin comprobarlo). Fuente: primer autor y año de un estudio real que conozcas con seguridad; si no, escribe SIN FUENTE. No inventes ninguna.
(3) Dos líneas finales, fuera del rol de médica: "Modelo: [nombre y versión que crees ser, o NO DISPONIBLE] · Fecha de corte de conocimiento: [fecha o NO DISPONIBLE]" y "He buscado en internet para responder: SÍ / NO".

RESTRICCIONES: Sin nombres comerciales de medicamentos. Usa siempre "persona con obesidad". Sin cifras ni porcentajes salvo que vayan acompañados de fuente en la tabla.
```

Añadir a "qué revisar": "Compara la línea 'Modelo:' con el nombre del desplegable: es frecuente que no coincidan. Ese es el segundo aprendizaje de la sesión: la máquina tampoco sabe con seguridad quién es. Y si la respuesta trae enlaces o un bloque de fuentes, ha buscado aunque diga que no."

Nota para CLÍNICO (no arbitro): el ejemplo usa "el GLP-1 sube tras perder peso" como la afirmación que el capítulo 1 contradice. En la literatura el sentido del GLP-1 tras pérdida de peso por dieta es discrepante entre estudios (Sumithran 2011 lo encontró disminuido; otros trabajos lo encuentran aumentado), así que un modelo que lo marque MEDIA está bien calibrado y la "contradicción" que la sesión quiere enseñar puede no ser limpia. Si CLÍNICO lo confirma, sugiero que el ejemplo use la leptina o el gasto energético, donde el sentido es unánime.

---

## Caso 2 · Cazar una alucinación · veredicto: MEJORAR

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, los cinco. La escala SEGURA / PROBABLE / DUDOSA está definida: es el mejor cierre de certeza del capítulo. |
| Anonimización | Sí, y adecuada: no entra ningún dato. |
| Variables | No hay ni hacen falta. |
| Salidas cerradas | Sí: DESCONOCIDO, LISTA INCOMPLETA. Bien. |
| Portabilidad | Necesita nota (T1): si el modelo busca, el ejercicio cambia de sentido. |
| Ejemplo de salida | **Incoherente con el formato:** el prompt pide siete columnas (incluida "título") y el ejemplo muestra seis, sin título. El título es la columna que el lector usa para buscar en PubMed. |
| Riesgo principal | Bien identificado (el DOI con forma de DOI). |

### Ejecución mental (Claude sin búsqueda; ChatGPT y Gemini con su comportamiento por defecto)
- **Claude:** devuelve Sumithran 2011 (NEJM), Fothergill 2016 (Obesity), Rosenbaum 2010, Leibel 1995 y Hall 2016 o Müller 2016, casi todas reales y con DOI correctos, varias con PMID DESCONOCIDO. La lección "la mitad no existe" no aparece: el tema es canónico y el modelo lo tiene bien aprendido.
- **ChatGPT:** parecido, y con frecuencia busca por su cuenta y devuelve cinco reales con enlace. Lección perdida, salvo que el lector sepa leer la señal.
- **Gemini:** busca casi siempre. Igual.
- Cuando sí falla, falla como dice el capítulo: DOI de otro artículo, año movido, PMID de ocho dígitos plausible pero de otra cosa. Y con etiqueta SEGURA.
- **Prueba con la variante corregida** (al menos dos referencias posteriores a 2021 y una en revista en español): los tres modelos flaquean. Aparecen revistas reales (Nutrición Hospitalaria, Endocrinología, Diabetes y Nutrición) con autores plausibles y DOI que no resuelven, o artículos reales con años equivocados. El ejercicio vuelve a enseñar lo que quiere enseñar sin cambiar de tema.

Rúbrica: calibración es exactamente lo que se mide; acción segura alta (nada entra sin abrirse).

### Problemas
1. Ejemplo sin columna "título"; añadirla (es la que permite buscar).
2. Tema demasiado canónico para que el fallo aparezca de forma fiable en 2026. Empujar al modelo fuera del canon con dos condiciones (recencia, idioma) sin cambiar el tema.
3. Nota de búsqueda (T1) y línea final determinista.
4. El lector no tiene dónde apuntar el resultado de su comprobación; los "cuatro resultados posibles" están en prosa. Darle la columna.
5. "Artículos originales o revisiones": pedir que no mezcle datos de dos artículos en una fila (es el fallo más frecuente: autores de uno, DOI de otro).

### Versión corregida
```
ROL: Eres una documentalista científica que trabaja con revistas biomédicas indexadas.

CONTEXTO: Preparo una lista de lectura sobre adaptación metabólica tras la pérdida de peso en personas adultas. Es un ejercicio de formación; no hay pacientes ni datos de personas. Responde solo con lo que recuerdas: no busques en internet.

TAREA: Dame cinco referencias de artículos originales o revisiones sobre adaptación metabólica tras la pérdida de peso. Al menos dos publicadas a partir de 2021 y al menos una en una revista en español.

FORMATO: Tabla con siete columnas: primer autor; año; revista; título completo; DOI; PMID; CERTEZA. CERTEZA toma uno de estos valores: SEGURA (recuerdas autores, título, revista y año con detalle), PROBABLE (recuerdas autores y tema, no los datos exactos), DUDOSA (podría no existir tal como la escribes). Ordena de mayor a menor certeza. Si no llegas a cinco con certeza SEGURA o PROBABLE, deja las filas restantes vacías y escribe debajo "LISTA INCOMPLETA". Última línea: "He buscado en internet: SÍ / NO".

RESTRICCIONES: No inventes DOI ni PMID: si no los recuerdas, escribe DESCONOCIDO en esa casilla. No combines datos de dos artículos en una misma fila. No busques en internet en este ejercicio. No incluyas datos de personas.
```

Ejemplo de salida corregido (añadir la columna título y una fila de comprobación del lector):

> | Autor | Año | Revista | Título | DOI | PMID | CERTEZA | **Tu comprobación** |
> |---|---|---|---|---|---|---|---|
> | Fothergill | 2016 | Obesity | Persistent metabolic adaptation 6 years after… | 10.1002/oby.21538 | DESCONOCIDO | SEGURA | EXISTE Y COINCIDE |
> | Martínez | 2022 | Nutr Hosp | Adaptación metabólica tras pérdida ponderal… | 10.20960/nh.0000 | DESCONOCIDO | PROBABLE | NO EXISTE |
>
> (La última columna la rellenas tú con uno de cuatro valores: EXISTE Y COINCIDE / EXISTE CON ERRORES / EXISTE PERO TRATA DE OTRA COSA / NO EXISTE.)

Nota de portabilidad a añadir tras el prompt:

> **Si la respuesta trae enlaces, ha buscado.** Claude deja apagar la búsqueda en la configuración. ChatGPT decide buscar por su cuenta cuando le parece útil, y Gemini busca casi siempre: en ese caso las cinco pueden ser reales y el ejercicio no enseña nada. Repite en otra herramienta o escribe al principio: "Contesta solo de memoria; si necesitas buscar, no lo hagas y marca DUDOSA".

Coherencia con "Hazlo hoy": el paso 2 sigue diciendo "cinco referencias"; no cambia.

---

## Caso 3 · Lo que se pierde en medio · veredicto: MEJORAR

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, los cinco. |
| Anonimización y comprobación humana previa | Sí: solo documentos públicos, descargados de su web oficial; "no contiene datos de pacientes y no debes añadir ninguno". Correcto para este uso. |
| Variables con ejemplo por defecto | Sí, dos, ambas con ejemplo (GIRO 2024; puntos de corte de cintura). Claras. |
| Salidas cerradas | Etiqueta ENCONTRADO / NO ENCONTRADO: bien pensada, **mal colocada** (T4). |
| Portabilidad | **Necesita nota** (T6): NotebookLM no da páginas; ChatGPT y Gemini buscan por fragmentos; planes gratuitos con límite de tamaño. |
| Ejemplo de salida | Realista, y precisamente por eso delata el problema: el turno 1 da una cita "de memoria" y después la etiqueta NO ENCONTRADO. El formato lo permite. |
| Riesgo principal | Bien identificado ("recordar en vez de leer"). La mitigación depende del orden de la salida, que hoy es el contrario. |

### Ejecución mental (GIRO 2.ª edición en PDF, dato: puntos de corte de perímetro de cintura)
- **ChatGPT (PDF largo):** trocea el documento y recupera fragmentos que contienen "perímetro de cintura". Encuentra el pasaje si la búsqueda acierta; da un número de página que a menudo no coincide con el del PDF (cuenta páginas de texto extraído o cita la impresa). Cuando no acierta, escribe una cifra correcta (102 / 88 cm) y "página no localizada": el ejemplo del capítulo, literal.
- **Gemini:** parecido; tiende a dar la cifra "según la guía" con una seguridad que no distingue lo leído de lo sabido.
- **Claude:** si el PDF cabe en la ventana, lo lee entero y responde con página del PDF razonablemente fiable; si no cabe, avisa de que el archivo excede el límite (los otros dos no avisan: leen parte).
- **NotebookLM:** localiza bien y devuelve una cita numerada que abre el pasaje; no hay "página": el formato del prompt no encaja tal cual.
- **Turno 2** ("revisa solo el apartado…"): mejora en los tres, por motivos distintos: en Claude dirige la atención; en ChatGPT y Gemini cambia la consulta de recuperación. Para el lector, indistinguible y útil.
- Dato con varias cifras (por población, por sexo, por método): los tres tienden a devolver el primer pasaje y omitir el segundo salvo que se les obligue.

Rúbrica: fidelidad depende del orden de salida (hoy media); calibración baja en Gemini; acción segura correcta (sin interpretación).

### Problemas
1. **Etiqueta después de la cita** (T4). Con el orden actual, el modelo escribe primero lo que "sabe" y después se califica; el ejemplo lo muestra. Poner la etiqueta primero y la cita solo si la etiqueta lo permite.
2. **Sin frase ancla.** Una cita recitada de memoria no viene con la frase que la precede en el texto. Pedir la frase anterior es la comprobación más barata de que el modelo ha leído: si no puede darla, no ha leído.
3. **Página del PDF frente a página impresa.** "Página 31" puede ser la posición en el archivo o el número impreso, y en guías con portada e índice difieren en 5-10 páginas. El lector abre por la 31 y no lo encuentra. Pedir ambas.
4. **Paso 0 ausente.** El capítulo dice en la mitigación "pregúntale cuántas páginas ve"; hacerlo salida obligatoria al principio, para detectar lectura parcial antes de fiarse de un NO ENCONTRADO.
5. **Tarea enterrada en el propio prompt.** El capítulo enseña "pon lo importante al principio o al final" y el prompt pone el dato en medio. Repetir el dato en la última línea (se nota especialmente cuando el documento va delante en la conversación).
6. **Nota de portabilidad** (T6) y de higiene de archivos (T5b).
7. Variable del turno 2: añadir rango de páginas opcional, que es lo que más ayuda a los tres modelos.

### Versión corregida

Texto previo al prompt: "Adjunta el PDF antes de escribir el prompt (en NotebookLM, cárgalo como fuente). Solo documentos públicos, descargados de su web oficial, para uso personal. Al terminar, borra la conversación y comprueba si la herramienta guarda los archivos en una biblioteca aparte."

```
ROL: Eres una asistente de lectura de documentos clínicos. Trabajas solo con el texto del documento adjunto; lo que sepas por tu cuenta no cuenta en esta tarea.

CONTEXTO: Te adjunto una guía clínica pública sobre obesidad en personas adultas [por ejemplo: la guía GIRO de la SEEDO, 2.ª edición, 2024]. No contiene datos de pacientes y no debes añadir ninguno.

TAREA: Localiza en el documento adjunto [dato concreto, por ejemplo: los puntos de corte de perímetro de cintura que la guía utiliza para definir obesidad abdominal] y transcríbelo literalmente.

FORMATO, en este orden y sin saltarte ninguna línea:
(0) "Documento: [título que aparece en el archivo] · Páginas que veo: [número]". Si no puedes leer el archivo entero, escribe "LECTURA PARCIAL" y hasta qué página llegas.
(1) Una sola etiqueta: ENCONTRADO EN EL DOCUMENTO / NO ENCONTRADO EN EL DOCUMENTO.
(2) Solo si es ENCONTRADO, por cada pasaje: la cita literal entre comillas, sin resumir ni corregir; la frase completa que la precede en el texto; la página (número de página del PDF y, si es distinto, el número impreso en la página) y el apartado.
(3) Si es NO ENCONTRADO: escribe "No aparece en el texto que he leído" y para. No completes con lo que sepas de otras fuentes ni propongas la cifra que "suele" usarse.

RESTRICCIONES: Solo el documento adjunto. Sin interpretación clínica. Sin recomendaciones. Si hay varios pasajes (por ejemplo, cifras distintas por sexo o por población), transcríbelos todos, cada uno con su página. Recuerda: lo único que busco es [repite el dato concreto], literal y con página.
```

Segundo turno, en la misma conversación: `Revisa solo el apartado [nombre o número, por ejemplo: "Diagnóstico y evaluación"], entre las páginas [x] y [y] si las conoces, y repite la tarea desde la línea (1) con el mismo formato.`

Ejemplo de salida corregido:

> Turno 1: Documento: Guía GIRO 2.ª ed. · Páginas que veo: 212. NO ENCONTRADO EN EL DOCUMENTO. No aparece en el texto que he leído.
> Turno 2: ENCONTRADO EN EL DOCUMENTO. "[cita literal de la guía]". Frase anterior: "[frase que la precede]". Página 31 del PDF (impresa: 27), apartado 4.2.
>
> (Lo que ya no puede pasar: una cifra "de memoria" con etiqueta NO ENCONTRADO. Lo que sí puede pasar: que el turno 1 diga NO ENCONTRADO porque no ha buscado bien; por eso existe el turno 2.)

Nota de portabilidad a añadir tras el prompt:

> **Según la herramienta.** En NotebookLM no hay páginas: cambia "página" por "número de cita" y abre cada cita con un clic. En ChatGPT y Gemini, un PDF largo no se lee de principio a fin: el modelo busca fragmentos que parecen responder a tu pregunta, así que NO ENCONTRADO a veces significa "no lo he buscado con las palabras adecuadas"; el segundo turno lo arregla porque cambia la búsqueda. Claude lee el documento entero si cabe y te avisa si no cabe; los otros dos no avisan: mira la línea (0). En planes gratuitos hay límite de tamaño: si no cabe, sube solo el capítulo que necesitas.

Coherencia: "qué revisar" del capítulo ya dice "abre el PDF por la página que dice"; añadir "si da dos números de página, prueba los dos".

---

## Caso 4 · Leer una etiqueta nutricional · veredicto: REESCRIBIR

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, los cinco. La tarea en cuatro pasos es buena; se queda corta en los escenarios reales. |
| Anonimización y comprobación humana previa | Sí en la Situación ("solo la etiqueta: sin manos, sin ticket…", "la haces tú… y la borras") y en el contexto. La comprobación humana está en el riesgo, no antes de subir; hay que moverla. Falta la ubicación GPS de la foto (T5a). |
| Variables | `[usted / tú]`. Clara. |
| Salidas cerradas | ILEGIBLE por casilla: bien, pero llega tarde (T4). Sin puerta de legibilidad global, sin regla de varias tablas, sin regla de idiomas, sin lista cerrada de azúcares. |
| Portabilidad | Sin cambios en el prompt; las tres leen imágenes. Difieren en calidad de lectura de letra pequeña (Gemini y ChatGPT algo mejor que Claude con fotos regulares; los tres fallan con brillos). |
| Ejemplo de salida | Realista y aritméticamente coherente (23 g de azúcares por 100 g → 6,9 g por ración de 30 g). Le falta la fila de proteínas, que la tarea pide. |
| Riesgo principal | Bien identificados los dos (decimal, foto con más de lo que querías). Falta el tercero y más traicionero de lo multimodal: cuando no lee, **rellena con los valores típicos de ese tipo de producto**, y el resultado parece una transcripción. |

### Ejecución mental (tres escenarios sintéticos)

**Escenario A · foto regular (galleta, letra de 5 puntos, algo de brillo).** Los tres modelos transcriben la tabla completa y con seguridad. Donde el brillo tapa "4,5 g", ChatGPT y Gemini escriben "4,5 g" o "45 g" sin ILEGIBLE; Claude pone ILEGIBLE con más frecuencia, no siempre. Lo que ninguno hace espontáneamente: decir que la foto es mala antes de empezar. La instrucción "si no se lee, ILEGIBLE" compite con el impulso de completar, y suele perder. Con la puerta de legibilidad al principio (BUENA / REGULAR / MALA, y MALA = parar), los tres cumplen bastante bien porque la decisión se toma antes de generar la tabla.

**Escenario B · envase multilingüe (ES / PT / FR en la misma cara) o comprado fuera (etiqueta en inglés, o formato de EE. UU. sin columna por 100 g y con sodio en mg).** Sin instrucción, el modelo elige un idioma sin decirlo y, si el español está cortado en la foto, mezcla ingredientes de dos idiomas. Con etiqueta anglosajona convierte sodio a sal y "Total Carbohydrate" a hidratos con sus propios factores, sin avisar. Con la regla "usa el español si existe; si no, di qué idioma usas y traduce dejando el original entre paréntesis; no conviertas unidades", el resultado es trazable.

**Escenario C · envase con varias tablas** (cereales "por 100 g" y "por 30 g con 125 ml de leche"; puré "producto seco" y "preparado"; multipack con dos variantes). Los tres modelos tienden a devolver una sola tabla, eligiendo la que "parece principal", o a mezclar columnas: azúcares del preparado con energía del seco. Este es el error con consecuencia clínica: una persona con diabetes que cuenta hidratos se lleva la cifra de la columna equivocada. La regla "una tabla por columna del envase, con el título que le da el envase, sin elegir ni mezclar" lo resuelve; la comprobación aritmética (4 × hidratos + 4 × proteínas + 9 × grasas + 2 × fibra ≈ kcal) delata la mezcla, porque las columnas cruzadas no cuadran.

**Azúcares añadidos.** "Cuántos azúcares añadidos o edulcorantes aparecen" sin lista cerrada: ChatGPT cuenta "jarabe de glucosa" y "azúcar"; Gemini añade "maltodextrina"; Claude duda con "zumo concentrado de manzana". El recuento cambia según el modelo y el lector no sabe cuál es el bueno. Con lista cerrada más una categoría "con interrogante", el recuento es reproducible.

Rúbrica: fidelidad media-baja en los escenarios A y C sin correcciones; calibración baja (no dice que no ve); confusores: valores típicos del producto; acción segura correcta (no valora).

### Problemas
1. Sin puerta de legibilidad previa a la transcripción (T4). El modelo estima lo borroso.
2. Sin regla para varias tablas o columnas: mezcla o elige. Consecuencia clínica posible.
3. Sin regla de idiomas ni de unidades (sodio / sal, kJ / kcal, formato de EE. UU.).
4. Sin lista cerrada de azúcares y edulcorantes: recuento no reproducible.
5. Sin comprobación aritmética que delate lecturas erróneas y columnas cruzadas.
6. Riesgo no nombrado: rellenar con valores típicos del tipo de producto.
7. Metadatos de la foto (ubicación GPS, fecha) y persistencia de archivos subidos (T5).
8. La comprobación humana de la foto está en el riesgo; debe ir antes de subir, en la Situación.
9. Restricción "sin necesidades diarias" choca con la columna %IR impresa en muchos envases: aclarar que se copia si figura, no se calcula.
10. Ejemplo sin proteínas.
11. Las tres frases finales en trato de usted/tú: si se entregan impresas, son material para el paciente y necesitan el disclaimer (pregunta para Cristina).

### Versión corregida

Texto previo al prompt (sustituye la segunda mitad de la Situación):

> **Antes de la foto.** De frente, sin flash, la tabla ocupando la pantalla; si el envase tiene dos tablas, dos fotos. Mírala en grande antes de subirla: solo etiqueta, sin manos, sin ticket, sin cocina de nadie. Las fotos del móvil llevan dentro la ubicación y la hora; si haces una captura de pantalla de la foto y subes la captura, no las lleva. Al terminar, borra la foto del carrete, la conversación y, si la herramienta tiene biblioteca de archivos, el archivo.

```
ROL: Eres una dietista-nutricionista que lee etiquetas de alimentos envasados y transcribe lo que ve, sin valorarlo.

CONTEXTO: Te adjunto la foto de la etiqueta de un producto envasado, hecha por mí y revisada antes de subirla. En la imagen no hay personas ni datos personales, y no debes inferir nada sobre quién lo consume. Es una transcripción para uso educativo; no sustituye a la etiqueta.

TAREA, en este orden:
(0) Legibilidad. Antes de transcribir nada, escribe una línea: "Legibilidad: BUENA / REGULAR / MALA". Si es MALA (números borrosos, brillos sobre la tabla, tabla cortada), escribe "REPETIR FOTO" y para. Si en la imagen aparece cualquier persona, parte del cuerpo, texto manuscrito, ticket o dirección, escribe "IMAGEN NO APTA" y para.
(1) Idioma y tablas. Di en qué idiomas está la etiqueta y cuántas tablas o columnas distintas hay (por 100 g o 100 ml; por ración; producto tal cual o preparado; con o sin leche; sin cocinar o cocinado). Usa la versión en español si existe; si no, indica el idioma que usas.
(2) Transcripción, una tabla por cada columna del envase, con el título que le da el envase, sin mezclarlas ni elegir una: energía (kJ y kcal), grasas, de las cuales saturadas, hidratos de carbono, de los cuales azúcares, fibra, proteínas, sal, y cualquier otra fila que figure. Copia los números con el mismo decimal y la misma unidad que ves. Si el envase imprime la columna %IR, cópiala; no calcules ninguna. Si un número o una palabra no se lee con claridad, escribe ILEGIBLE en esa casilla: no lo estimes ni lo completes con los valores habituales de ese tipo de producto.
(3) Lista de ingredientes, en su orden y con su texto exacto; si está en otro idioma, tradúcela al español dejando el original entre paréntesis.
(4) Los tres primeros ingredientes. Después, los azúcares y edulcorantes que aparecen en la lista, contados y nombrados, usando solo esta lista: azúcar, sacarosa, glucosa, dextrosa, fructosa, jarabe o sirope (de glucosa, de glucosa-fructosa, de maíz, de agave, de arroz), miel, melaza, azúcar invertido, maltodextrina, zumo o concentrado de fruta añadido; y edulcorantes: sucralosa, aspartamo, acesulfamo K, sacarina, ciclamato, glucósidos de esteviol, polialcoholes (sorbitol, maltitol, xilitol, eritritol) o cualquier E-950 a E-969. Si ves otro que creas que es un azúcar añadido, ponlo aparte con un interrogante.
(5) Comprobación aritmética, por cada tabla por 100 g o 100 ml: los azúcares no pueden superar a los hidratos, las saturadas no pueden superar a las grasas, y 4 × hidratos + 4 × proteínas + 9 × grasas + 2 × fibra debe quedar a menos de un 10 % de las kcal. Escribe "COHERENTE" o "INCOHERENTE: [qué no cuadra]" y, si es INCOHERENTE, la casilla que crees mal leída.

FORMATO: Las líneas (0) y (1); las tablas; la lista de ingredientes; el punto (4); la línea (5); y al final tres frases descriptivas en lenguaje llano, trato de [usted / tú], que digan qué lleva el producto y en qué cantidad por ración, sin valorarlo.

RESTRICCIONES: No digas si el producto es "bueno", "malo", "sano" o "light", ni si conviene a alguien. Sin consejos individuales, sin necesidades diarias, sin mencionar peso ni dietas. Sin nombres de marca: llama al producto por su tipo ("galleta de cereales", "yogur de sabores"). No conviertas unidades (sodio a sal, kJ a kcal, onzas a gramos): copia lo impreso.
```

Ejemplo de salida corregido:

> Legibilidad: BUENA. Idiomas: español y portugués. Tablas: una (por 100 g y por ración de 30 g).
> Por 100 g: energía 1.890 kJ / 452 kcal; grasas 18 g, saturadas 8,2 g; hidratos 64 g, azúcares 23 g; fibra 3,1 g; proteínas 6,5 g; sal 0,9 g. Ración (30 g): azúcares 6,9 g.
> Ingredientes: harina de trigo, azúcar, aceite de palma […]. Azúcares añadidos: azúcar, jarabe de glucosa (2). Edulcorantes: ninguno.
> Comprobación: 4×64 + 4×6,5 + 9×18 + 2×3,1 = 450 kcal frente a 452. COHERENTE.

Añadir a "qué revisar": "Si la legibilidad es REGULAR, cuenta los ILEGIBLE: más de tres, repite la foto. Si dice INCOHERENTE, casi siempre es un decimal mal leído; mira esa casilla antes que ninguna. Y comprueba que el modelo ha transcrito tantas tablas como tiene el envase: la que falta suele ser la que importa."

Añadir al riesgo principal: "y el tercero, el más difícil de ver: cuando no lee un número, el modelo tiende a poner el valor habitual de ese tipo de producto, y el resultado parece una transcripción. La comprobación aritmética y la etiqueta delante son la única defensa."

Nota de portabilidad: no hace falta cambiar el prompt. Basta decir que las tres leen imágenes en el plan gratuito cuando se escribe esto, que las fotos con brillos fallan en las tres y que, si una responde a (0) con BUENA y luego llena la tabla de ILEGIBLE, se ha calificado mal: repetir la foto.

---

## Caso 5 · Qué nivel de IA exige esta tarea · veredicto: MEJORAR (leve)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, los cinco. |
| Anonimización y comprobación humana previa | Sí, doble: en la Situación ("antes de pegar, lee la lista: tareas, no personas"), en el contexto ("ya lo he revisado") y como red en restricciones (REVISAR PRIVACIDAD). Hereda bien el Caso 5 del capítulo 1. |
| Variables con ejemplo por defecto | Sí: la lista, con cuatro ejemplos. Clara. |
| Salidas cerradas | Sí: POR ACLARAR con pregunta al final, REVISAR PRIVACIDAD, tres valores de datos, tres de coste. Bien. |
| Portabilidad | Sin cambios. |
| Ejemplo de salida | Realista y coherente con el prompt; le falta una fila POR ACLARAR, que es la novedad del formato. |
| Riesgo principal | Bien identificado (la tabla como permiso). Mitigación correcta. |

### Ejecución mental (diez tareas sintéticas, entre ellas "contestar una reclamación" y "preparar la interconsulta de una paciente")
- Los tres modelos rellenan la tabla y las dos listas. Diferencias: ChatGPT asigna DE PAGO a casi todo; Gemini asigna GRATUITA con generosidad; Claude es el más conservador y pone PAPEL en dos o tres tareas. Con la misma lista, tres tablas distintas. No es un problema de los modelos: **el prompt no dice cómo se pasa de (a) y (b) a (c)**, así que cada uno aplica su criterio.
- "Contestar una reclamación": ChatGPT la clasifica como SOLO CON CONTRATO (lleva nombre); Gemini como GRATUITA ("una plantilla de respuesta"); Claude pregunta al final. Las tres lecturas son razonables; la salida correcta es POR ACLARAR con la pregunta "¿quieres una plantilla genérica o la respuesta a una reclamación concreta?". Con regla explícita, los tres llegan ahí.
- "Interconsulta de una paciente": SOLO CON CONTRATO en los tres. Bien.
- REVISAR PRIVACIDAD: funciona en los tres cuando hay un nombre; con "la hija de la señora de la calle X", Claude y ChatGPT lo detectan, Gemini a veces no. La barrera sigue siendo el lector, como dice la Situación.

Rúbrica: priorización buena; calibración depende de la regla (hoy no comparable); acción segura alta.

### Problemas
1. Sin regla de asignación de nivel: la tabla no es auditable ni comparable entre herramientas. Darla en el prompt, en orden de prioridad, para que el lector pueda comprobar cada fila con la regla y no con la opinión del modelo.
2. "RAZONADOR O FRONTERA" mezcla un modo (razonador) con un nivel (frontera); el capítulo los explica por separado. Renombrar: "DE PAGO CON RAZONADOR O MODELO DE FRONTERA".
3. Ejemplo sin fila POR ACLARAR.
4. "Tabla con la tarea y las cuatro columnas": decir "(a-d)" para que el modelo no invente una quinta.

### Versión corregida
```
ROL: Eres una consultora que ayuda a médicas de familia a decidir cuándo y cómo usar IA generativa con seguridad.

CONTEXTO: Te pego diez tareas de una jornada de Atención Primaria, descritas de forma genérica y sin datos de personas; ya lo he revisado. Trabajo solo con herramientas de consumo, sin acuerdo de tratamiento de datos. Los niveles posibles son cinco: PAPEL (mejor sin IA); GRATUITA; DE PAGO; DE PAGO CON RAZONADOR O MODELO DE FRONTERA; SOLO CON CONTRATO (necesita datos clínicos reales y hoy no la hago con IA).

TAREA: Para cada tarea indica: (a) coste de error si la IA se equivoca: BAJO (lo leo entero y lo corrijo), MEDIO (podría llegar a otra persona sin que yo lo note), ALTO (afecta a una decisión clínica, a un dato de paciente o a un documento oficial); (b) datos de pacientes que necesita: NINGUNO / SOLO RECUENTOS AGREGADOS / DATOS REALES; (c) nivel de herramienta, aplicando esta regla en este orden y parando en la primera que se cumpla: si (b) es DATOS REALES → SOLO CON CONTRATO; si la tarea exige mi presencia o una decisión clínica → PAPEL; si (a) es ALTO → DE PAGO CON RAZONADOR O MODELO DE FRONTERA; si (a) es MEDIO → DE PAGO; si (a) es BAJO → GRATUITA; (d) la comprobación humana que haría antes de usar la salida, en una línea. Si una tarea no está clara o admite dos lecturas, clasifícala como POR ACLARAR en las cuatro columnas y escribe la pregunta que me harías.

FORMATO: Tabla con la tarea y las cuatro columnas (a-d). Debajo, tres listas: tareas que hoy no debo hacer con IA y por qué; tareas donde una herramienta gratuita basta; preguntas de las tareas POR ACLARAR.

RESTRICCIONES: No inventes tareas ni cambies mis descripciones. No propongas automatizar decisiones clínicas. No rebajes el nivel que sale de la regla aunque la tarea parezca sencilla. Como comprobación adicional a la mía, si una línea contiene algo que parezca identificar a una persona (nombre, dirección, parentesco con detalles, fecha), no la clasifiques: ponla en una lista "REVISAR PRIVACIDAD" y dime por qué.

TAREAS:
[una por línea, por ejemplo: resumir una guía pública para la sesión del jueves; redactar una hoja informativa sobre etiquetas; contestar una reclamación; preparar la interconsulta de una paciente; …]
```

Ejemplo de salida corregido (añadir una fila):

> | Contestar una reclamación | POR ACLARAR | POR ACLARAR | POR ACLARAR | ¿Plantilla genérica o respuesta a una reclamación concreta con datos? |

Añadir a "qué revisar": "Comprueba cada nivel con la regla, no con el modelo: si (b) dice DATOS REALES y (c) no dice SOLO CON CONTRATO, la fila está mal, la haya escrito quien la haya escrito."

---

## Caso 6 · Chat frente a razonador · veredicto: MEJORAR (leve)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, los cinco. El rol incluye el marco ("ejercicio sobre un caso inventado; no es una consulta real"): bien. |
| Anonimización y comprobación humana previa | Sí en el prompt ("caso sintético, escrito por mí"). Débil en la Situación: "escrito de memoria" es justo el modo en que un caso real se cuela con tres detalles cambiados. Falta la regla del arquetipo. |
| Variables con ejemplo por defecto | Sí, con un ejemplo completo y bien construido (es el arquetipo del libro con variaciones). |
| Salidas cerradas | Cuatro listas, máximo siete puntos, atajos al final: bien. Escala ALTA / MEDIA / BAJA sin definir (T3). "No añadas datos: van en la lista 3" es una buena salida determinista. |
| Portabilidad | **Necesita nota.** "Modo chat / modo razonador" no existe con ese nombre en ninguna de las tres, y en planes gratuitos puede no existir o activarse solo. |
| Ejemplo de salida | Realista en contenido. El tiempo del razonador ("dos minutos y medio") está en el extremo alto; lo habitual es entre 20 segundos y 2 minutos. Decir un rango. |
| Riesgo principal | Bien identificado (pegar un caso real). Mitigación correcta. |

### Ejecución mental (caso por defecto)
- **Modo chat, los tres:** lista 1 correcta; lista 2 con apnea del sueño en ALTA, "prediabetes" en ALTA, hipotiroidismo en MEDIA-BAJA, depresión o efecto del antidepresivo en MEDIA; lista 3 pide analítica, TSH, escala de somnolencia, historia del sueño; lista 4 correcta y sin tratamientos. Ninguno cierra diagnóstico. Sin definir la escala, ChatGPT reparte más ALTA que Claude.
- **Modo razonador, los tres:** más prudencia en las certezas, más elementos en la lista 3 (antidepresivo como causa de ganancia de peso, atracones nocturnos, alcohol, corticoides, menopausia), y a veces añade datos al caso ("probablemente sedentaria") pese a la restricción; la instrucción "si los necesitas, van en la lista 3" reduce el problema pero no lo elimina. Los atajos vigilados salen genéricos ("sesgo de anclaje") salvo que se le den ejemplos concretos.
- **Trazabilidad:** sin pedir que cada deducción cite el hecho del que sale, la lista 2 mezcla deducciones de un hecho con deducciones del conjunto, y el lector no puede auditarlas. Pedirlo cuesta una línea y convierte la lista 2 en algo comprobable.
- **Modos según herramienta (cuando escribo esto; cambia cada pocos meses):** Gemini ofrece modelos "Thinking" en el desplegable, también en gratuito; ChatGPT decide por sí mismo cuándo razonar y en pago deja forzarlo ("pensar más"); Claude tiene el razonamiento extendido como opción en pago. Es decir: en algún plan gratuito el lector no podrá elegir, y en ChatGPT puede que "modo chat" haya razonado sin decirlo.

Rúbrica: fidelidad alta; calibración mejor en razonador; confusores bien manejados; acción segura alta (sin tratamientos, sin cierre).

### Problemas
1. Regla del arquetipo ausente en la Situación: "escrito de memoria" no basta. Aplicar la regla de tres cambios.
2. Escala de certeza sin definir (T3).
3. Sin trazabilidad deducción → hecho.
4. Nota de portabilidad sobre los modos, con plan B cuando no hay razonador: pedir por escrito los pasos intermedios, que es lo que el capítulo cita (Wei 2022).
5. Tiempo del ejemplo en el extremo.
6. "Sin propuestas de fármacos" es correcto; añadir "no preguntes nada: si algo es ambiguo, di cómo lo interpretas en la lista 1" para cerrar la salida.

### Versión corregida

Añadir a la Situación: "Regla de tres cambios: si el caso te lo inspira alguien real, cambia al menos tres rasgos (edad, sexo, comorbilidad, fármaco, orden de los hechos) y no uses a nadie que hayas visto este mes. Si no puedes reconocerlo tú, no lo reconocerá nadie."

```
ROL: Eres médica de familia con experiencia en obesidad. Esto es un ejercicio de razonamiento sobre un caso inventado; no es una consulta real y no debes tomar ni proponer decisiones para ninguna persona concreta.

CONTEXTO: Caso sintético, escrito por mí, sin ninguna persona real detrás: [descripción inventada, por ejemplo: mujer de unos cincuenta años, obesidad de grado II, hipertensión tratada con un fármaco, dos glucemias en ayunas en rango de prediabetes, ronquidos con somnolencia diurna, cansancio y ánimo bajo desde hace meses, cuatro intentos previos de bajar de peso con recuperación, un antidepresivo desde hace un año]. No hay más datos.

TAREA: No cierres ningún diagnóstico. Escribe cuatro listas: (1) lo que está en el caso, hecho por hecho, numerados; (2) lo que deduces, indicando entre paréntesis el número del hecho o hechos de la lista 1 de los que sale cada deducción, y la certeza: ALTA (lo sostendría cualquier manual con estos datos), MEDIA (compatible, pero hay otras explicaciones igual de probables), BAJA (posible, necesitaría más datos); (3) lo que falta y cambiaría el razonamiento, ordenado por importancia; (4) qué preguntaría y qué exploraría una médica de familia en la siguiente visita, sin proponer tratamientos.

FORMATO: Cuatro listas numeradas, máximo siete puntos cada una. Al final, una línea con los atajos de razonamiento que has vigilado en tu propia respuesta (por ejemplo: quedarte con la primera explicación, atribuirlo todo al peso, dar por hecho lo que el caso no dice).

RESTRICCIONES: Sin nombres comerciales ni propuestas de fármacos. Sin diagnósticos cerrados. No añadas datos al caso: si los necesitas, van en la lista 3. No me hagas preguntas: si algo es ambiguo, di cómo lo has interpretado en la lista 1. Usa "persona con obesidad".
```

Nota de portabilidad a añadir tras el prompt:

> **Dónde está el razonador.** Los nombres cambian: busca en el desplegable algo como "Thinking", "razonamiento" o "pensar más". Si tu plan no lo tiene, o la herramienta decide sola cuándo razonar, haz la segunda pasada así: pega el mismo prompt con esta primera línea añadida: "Antes de responder, escribe tu razonamiento paso a paso; solo después escribe las cuatro listas". No es lo mismo, pero se parece lo suficiente para ver la diferencia.

Ajustar el ejemplo: "Modo razonador (entre 20 segundos y 2 minutos, según la herramienta)".

---

## Caso 7 · Inventario de lo que tengo · veredicto: LISTO

No es un prompt: es una ficha en papel. Se revisa como plantilla.

| Criterio | Estado |
|---|---|
| Variables con ejemplo por defecto | Sí, todas, con opciones cerradas entre corchetes. Clara y rápida de rellenar. |
| Anonimización | No aplica; la ficha no sale del cajón. Las líneas "lo que entra / lo que no entra" son la regla del libro en dos renglones: muy bien. |
| Ejemplo | Realista (es la ficha típica de quien empieza: gratuito, "no lo sé" en entrenamiento). |
| Riesgo principal | Bien identificado ("gratuita" no es "privada"; "de organización" no es "con contrato"). |

### Dos líneas que faltan (T5b y T5c)
Añadir tras "Entrenamiento con mis conversaciones":

```
Memoria entre conversaciones: [desactivada / activada / no lo sé]
Archivos que subo: [se borran con la conversación / quedan en una biblioteca aparte / no lo sé]
```

Y en "qué revisar": "Memoria activada significa que lo que pegues hoy puede reaparecer en una conversación de dentro de un mes, aunque hayas borrado la de hoy. Con casos inventados no pasa nada; con un dato pegado por error, sí."

---

## Preguntas y notas para el REDACTOR
- Aplicar T1 (búsqueda: frase introductoria, línea determinista en Casos 1 y 2, señal de los enlaces), T3 (escala de certeza única; proponer al ORQUESTADOR que entre en el glosario de `biblia.md`) y T4 (etiqueta antes que contenido) en la v2.
- Las versiones corregidas mantienen la voz. El Caso 4 corregido es aproximadamente el doble de largo que el original; es el precio de que funcione con fotos regulares, envases multilingües y dobles tablas. Si el REDACTOR necesita acortarlo, lo que no se puede quitar es (0), (2) "una tabla por columna", la lista cerrada de (4) y la comprobación (5).
- El Caso 3 corregido tiene paso 0; como en el Caso 1 del capítulo 1, conviene una frase en la Situación que lo anuncie ("primero te dice cuántas páginas ve; después busca").
- Las notas de portabilidad describen las herramientas "cuando escribo esto"; mantener esa fórmula, que ya usa el capítulo.
- Nota para CLÍNICO (no la resuelvo yo): la fila del GLP-1 en el ejemplo del Caso 1.
- Nota para EVIDENCIA: la referencia inventada del ejemplo del Caso 2 (Martínez 2022, Nutr Hosp, DOI 10.20960/nh.0000) es deliberadamente falsa y debe seguir siéndolo; conviene que el capítulo lo diga en una línea para que nadie la "corrija".

## Preguntas para Cristina
1. Caso 4: las tres frases finales, ¿son para decirlas tú en consulta o para entregarlas? Si alguna vez se imprimen o se envían, son material para pacientes y necesitan el disclaimer estándar (variante usted). Puedo dejarlo preparado en el prompt con una línea opcional.
2. Caso 2: ¿te parece bien empujar al modelo fuera del canon ("al menos dos desde 2021 y una en español") para que el fallo aparezca? Con el tema tal cual, en 2026 los tres modelos aciertan a menudo y el ejercicio se desinfla.
3. Caso 3: ¿qué dato usas tú de verdad cuando enseñas este ejercicio con la GIRO? Si es el perímetro de cintura, conviene comprobar que la guía lo da en un único pasaje o en varios (por sexo, por población), porque el ejemplo de salida debe reflejarlo.
4. Caso 6: ¿quieres que el plan B (pedir los pasos por escrito cuando no hay razonador) vaya en el texto o solo en la nota? Es la primera vez que el libro enseña a "emular" un modo, y puede merecer dos frases en la sección "Chat o razonador".
