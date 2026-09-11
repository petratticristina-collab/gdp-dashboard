# Revisión PROMPTS · Capítulo 1 · v1

> Agente: PROMPTS (ingeniero de prompts) · Fecha: 2026-09-11 · Ámbito: exclusivamente los seis prompts ofrecidos al lector (Casos 1-6). No se revisa el texto expositivo ni las referencias.
> Método: para cada prompt se comprueba la estructura rol · contexto · tarea · formato · restricciones (M2 potencIA), la instrucción de anonimización (decisión editorial 7 de `biblia.md`), la claridad de las variables entre corchetes, la portabilidad entre Gemini / ChatGPT / Claude, el realismo del ejemplo de salida y la identificación del riesgo. Cada prompt se ha ejecutado mentalmente con un caso sintético y la salida imaginada se ha leído con la rúbrica fidelidad · priorización · calibración · confusores · acción segura (M4).

## Resumen de veredictos

| Caso | Título | Veredicto | Motivo principal |
|---|---|---|---|
| 1 | Mapa de mi cupo | **mejorar** | La garantía de no identificación descansa en el modelo, cuando debe descansar en la exportación. Faltan columnas exactas, formato de archivo, normalización de categorías y tratamiento de vacíos. Incoherencia 7 vs 8 columnas. No funciona "sin cambios" en las tres herramientas. |
| 2 | Reescribir el consejo breve | **mejorar (leve)** | Prompt sólido. Las tres frases van fijas y "Hazlo hoy" pide sustituirlas: faltan corchetes. Pedir dos alternativas por frase. |
| 3 | La adaptación metabólica en 150 palabras | **listo** | Completo, seguro y portable. Solo dos ajustes de restricción (cifras) y una nota sobre el disclaimer si se imprime. |
| 4 | Sesión del centro (NotebookLM) | **mejorar** | Depende de NotebookLM; hace falta nota de portabilidad. Añadir lista de afirmaciones no sustentadas y formato de guion para hablar, no para leer. |
| 5 | Inventario de mi tiempo | **mejorar** | "Pregúntame en lugar de suponer" no es fiable en los tres modelos. Faltan definiciones de los cinco momentos (solapan), formato de la lista y criterio de "candidata a IA". Riesgo de identificación indirecta en las descripciones de tareas. |
| 6 | "¿Por qué recupero el peso?" en tres niveles | **mejorar (leve)** | Disclaimer en tuteo dentro de un texto en usted. Nivel C sin límite de hormonas ni sentido del cambio (riesgo de error fisiológico). Los recuentos de palabras deben ser aproximados. |

Ningún prompt es peligroso tal como está. Ninguno requiere reescritura completa. El Caso 1 es el que más trabajo necesita porque es el único en el que entra un archivo real en una herramienta de consumo.

---

## Hallazgos transversales (afectan a varios casos)

**T1 · Afirmación global falsa.** La introducción de la sección dice: *"Funcionan en Gemini, ChatGPT y Claude sin cambios."* No es cierto para el Caso 1 (necesita intérprete de código y el comportamiento difiere) ni para el Caso 4 (está escrito para NotebookLM: "las fuentes cargadas en este cuaderno"). Corrección propuesta:

> Los casos 2, 3, 5 y 6 funcionan en Gemini, ChatGPT y Claude sin cambios. El caso 1 necesita un asistente que ejecute código sobre archivos (lo tienen los tres, con diferencias que explico allí). El caso 4 está pensado para NotebookLM; al final del caso digo cómo adaptarlo.

**T2 · Instrucciones de comportamiento que los modelos no cumplen de forma fiable.** "Pregúntame en lugar de suponer" (Caso 5) y "detente y avísame sin procesar" (Caso 1) funcionan en Claude con bastante regularidad, pero ChatGPT y Gemini tienden a responder igualmente y añadir una nota. Norma para todo el libro: convertir cada instrucción condicional en una **salida determinista** ("clasifícalo como POR ACLARAR y lista las preguntas al final"; "escribe primero una tabla de columnas y detente ahí"). Es exactamente la idea del curso: la determinación vive en el proceso que obligas a seguir, no dentro del modelo.

**T3 · Recuentos de palabras.** Los tres modelos fallan en recuentos exactos (±15 %). Donde el capítulo pide "150 palabras", "100 / 180 / 250", escribir "aproximadamente" o dar un rango. Evita que el lector crea que el modelo se equivoca cuando entrega 168.

**T4 · Género del rol.** El Caso 2 dice "Eres médico de familia"; los Casos 3 y 6, "Eres médica de familia". Unificar (recomiendo el femenino, que es la voz de la autora) o usar "profesional de medicina de familia".

**T5 · Privacidad de la herramienta de consumo, no solo del dato.** Los prompts anonimizan bien el contenido, pero el capítulo no dice al lector que (a) revise en la configuración de la herramienta si sus conversaciones y archivos se usan para entrenar el modelo, y (b) borre la conversación y el archivo al terminar. Solo el Caso 1 menciona borrar el archivo. Propongo una frase en "Dos herramientas, dos reglas" y repetirla en "Antes de nada" del Caso 1.

**T6 · Coherencia usted/tú en material para pacientes.** El disclaimer estándar de `biblia.md` está en tuteo ("revisado por *tu* profesional sanitario"), pero los textos de los Casos 3 y 6 se piden en trato de usted. En la hoja impresa del Caso 6 conviven "Hable con su médica" y "tu profesional sanitario". Esto es una decisión de Cristina, no mía (ver pregunta al final).

---

## Caso 1 · Mapa de mi cupo · veredicto: MEJORAR

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, los cinco. Bien separados. |
| Instrucción de anonimización | Sí (tarea 1: comprobar y detenerse). Insuficiente como única garantía; ver problemas. |
| Variables entre corchetes | No hay. Correcto: todo va en el archivo. Pero las columnas no están definidas con precisión suficiente para exportarlas. |
| Portabilidad | **Necesita nota.** Ver abajo. |
| Ejemplo de salida | Realista en cifras (312/1.480 = 21,1 %; 97/312 = 31 %). **Error:** dice "8 columnas" y el prompt define 7. |
| Riesgo principal | Bien identificado (reidentificación por combinación). Falta el segundo riesgo real: el archivo contiene más de lo que se ve. |

### Ejecución mental (caso sintético: CSV de 1.480 filas, 7 columnas, 23 vacíos en IMC, 40 filas con "Obesidad 1" en vez de "obesidad_1", columna dm2 con vacíos donde el sistema no registró nada)

- **ChatGPT (intérprete de código):** carga pandas, lista columnas, hace `value_counts`. Cuenta "obesidad_1" y "Obesidad 1" como categorías distintas salvo que se le diga que normalice; la cifra de obesidad sale 40 personas por debajo. Trata el vacío de dm2 como "no" al cruzar, sin avisar. Muestra el código solo si se pide (lo pide el prompt; lo mostrará). Aplica "<5" en tablas si se lo dices, aunque a veces lo olvida en la parte narrativa.
- **Gemini (ejecución de código):** comportamiento similar; a veces resume en prosa y hay que insistir para la tabla. Muestra el código en un bloque desplegable.
- **Claude (herramienta de análisis):** lee CSV y xlsx en el chat, pero su intérprete es JavaScript, no Python. El "código para que pueda revisarlo" será JS; a un lector no técnico le da igual, pero conviene decirlo. Es el que mejor respeta "detente si encuentras identificadores".
- En los tres: la comprobación de identificadores es heurística. Una columna `id` con enteros de 8 dígitos puede pasar como "número de fila"; el modelo no sabe si es un CIP. **Conclusión: la garantía no puede estar en el prompt; tiene que estar en la exportación y en un paso previo de inspección que el modelo ejecute antes de contar.**

Lectura con la rúbrica: fidelidad media (cuenta lo que hay, pero categorías sucias y vacíos distorsionan); calibración baja (no avisa de lo que trata como "no"); acción segura correcta (no recomienda nada clínico, como se le pide).

### Problemas
1. **Columnas exactas no garantizadas.** El prompt nombra 7 columnas; el ejemplo dice 8; el texto "Antes de nada" describe las mismas 7 pero sin nombres de columna ni valores admitidos. El lector no sabe qué exportar exactamente. Hay que dar la **tabla de columnas con sus valores admitidos** y decir que cualquier columna que no esté en esa lista se borra.
2. **Cómo se garantiza que no hay identificadores.** Hoy depende de que el modelo "compruebe". Hace falta una cadena de tres barreras, de las que solo la tercera es el modelo:
   - *Barrera 1, en la exportación:* solo las 7 columnas de la lista; edad ya en décadas con tope superior abierto ("80 o más") para no dejar celdas pequeñas; IMC ya categorizado (nunca el valor numérico); última visita ya en tramos (nunca la fecha); sin municipio, sin centro, sin médico, sin número de fila del sistema.
   - *Barrera 2, en el archivo:* copiar solo los valores a un **libro nuevo en blanco** y guardar como **CSV**. Un .xlsx filtrado puede conservar hojas ocultas, caché de tablas dinámicas o filas "eliminadas" con los nombres originales. Y **desordenar las filas** (ordenar por una columna aleatoria y borrarla): si el archivo conserva el orden alfabético del listado original, cada fila es vinculable a una persona por quien tenga ese listado.
   - *Barrera 3, en el prompt:* paso 0 obligatorio en el que el modelo escribe la lista de columnas con número de valores distintos y ejemplos, y **se detiene** hasta que el lector confirme. Una columna con más de 10 valores distintos, o con texto libre, o con números de más de 3 dígitos, es sospechosa por definición. Esta salida es determinista: no depende de que el modelo "decida" avisar.
3. **Normalización de categorías y vacíos.** El capítulo lo advierte en "qué revisar", pero es mejor que el prompt lo resuelva: unificar mayúsculas, espacios y guiones antes de contar, y tratar el vacío como "sin dato", nunca como "no".
4. **"Si una celda tiene menos de 5 personas"** es ambiguo: el lector puede entender celda de hoja de cálculo. Decir "cualquier recuento inferior a 5 en cualquier tabla".
5. **Falta la denominación de "obesidad".** El prompt define categorias pero no dice que obesidad = obesidad_1 + obesidad_2 + obesidad_3. El modelo lo deduce, pero es mejor explicitarlo.
6. **Nota de portabilidad** y de privacidad de la herramienta (T5).

### Versión corregida

Texto previo al prompt (sustituye "Antes de nada"):

> **Antes de nada · lo que exportas y lo que no.** Exporta exactamente estas siete columnas y ninguna más. Si tu sistema añade un identificador, un número de fila, el centro, el municipio o la fecha, bórralos.
>
> | Columna | Valores admitidos |
> |---|---|
> | `grupo_edad` | 18-29 / 30-39 / 40-49 / 50-59 / 60-69 / 70-79 / 80 o más |
> | `sexo` | mujer / hombre / otro-no consta |
> | `categoria_imc` | normopeso / sobrepeso / obesidad_1 / obesidad_2 / obesidad_3 / sin dato |
> | `hta` | si / no / sin dato |
> | `dm2` | si / no / sin dato |
> | `dislipemia` | si / no / sin dato |
> | `ultima_visita` | 0-6 meses / 7-12 meses / mas de 12 meses / sin dato |
>
> Tres gestos más, que cuestan dos minutos: (1) copia solo los valores a un libro nuevo en blanco y guárdalo como CSV, porque un Excel filtrado puede guardar por dentro las hojas y filas que crees haber borrado; (2) desordena las filas antes de guardar (añade una columna con `=ALEATORIO()`, ordena por ella y bórrala), para que el orden no coincida con tu listado de cupo; (3) en la herramienta, revisa que tus conversaciones no se usen para entrenar el modelo y borra archivo y conversación al terminar.

```
ROL: Eres un analista de datos que apoya a una médica de familia en la gestión de su cupo. No haces recomendaciones clínicas.

CONTEXTO: Te adjunto un archivo CSV exportado de un sistema de historia clínica y anonimizado antes de subirlo. Debe contener exactamente siete columnas categóricas: grupo_edad (18-29 / 30-39 / 40-49 / 50-59 / 60-69 / 70-79 / 80 o más), sexo (mujer / hombre / otro-no consta), categoria_imc (normopeso / sobrepeso / obesidad_1 / obesidad_2 / obesidad_3 / sin dato), hta, dm2 y dislipemia (si / no / sin dato) y ultima_visita (0-6 meses / 7-12 meses / mas de 12 meses / sin dato). "Obesidad" significa obesidad_1, obesidad_2 u obesidad_3 juntas.

TAREA, en dos turnos:
PASO 0 (solo esto en tu primera respuesta): escribe una tabla con cada columna del archivo, su número de valores distintos y tres ejemplos de valor. Marca como SOSPECHOSA cualquier columna que no esté en la lista de siete, que tenga más de 10 valores distintos, que contenga texto libre, fechas o números de más de tres cifras. Si hay alguna columna sospechosa, no hagas nada más: dime cuál es y espera. Si no la hay, termina con la frase "Archivo comprobado: 7 columnas categóricas, sin identificadores" y espera a que yo escriba "continúa".
PASO 1 (cuando yo escriba "continúa"): (1) Normaliza las categorías antes de contar: mayúsculas, espacios, tildes y guiones; escribe qué valores has unificado. Trata los vacíos como "sin dato", nunca como "no". (2) Cuenta cuántas personas tienen obesidad y qué porcentaje del total representan. (3) Cruza obesidad con hta, dm2 y dislipemia. (4) Indica cuántas personas con obesidad tienen ultima_visita "mas de 12 meses" y qué porcentaje de las personas con obesidad son.

FORMATO: Una tabla resumen con los recuentos y porcentajes; debajo, cinco frases en lenguaje llano con los hallazgos principales; después, el número de filas con "sin dato" en cada columna; y al final el código completo que has ejecutado, para que pueda revisarlo.

RESTRICCIONES: No inventes datos ni rellenes huecos. Cualquier recuento inferior a 5, en cualquier tabla o frase, se muestra como "<5". No hagas recomendaciones clínicas ni sugieras tratamientos. Si el archivo no se puede leer, dímelo; no lo reconstruyas.
```

Nota de portabilidad a añadir tras el prompt:

> **Según la herramienta.** En ChatGPT y Gemini el código será Python; en Claude, JavaScript. No necesitas entenderlo; necesitas que exista para que alguien pueda revisarlo. Si la herramienta responde al paso 0 y sigue contando sin esperar, escribe: "Te he pedido que pares en el paso 0. Repite solo el paso 0". Sube CSV, no Excel.

Corregir el ejemplo de salida: "He comprobado que las **7** columnas son categóricas…" y añadir la línea de normalización ("He unificado 'Obesidad 1' con 'obesidad_1' en 40 filas").

Añadir al riesgo principal: "y por lo que el archivo guarda sin que lo veas (hojas ocultas, filas 'borradas', orden del listado original). Mitigación: libro nuevo, CSV, filas desordenadas".

---

## Caso 2 · Reescribir el consejo breve · veredicto: MEJORAR (leve)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, completos y bien pensados: los cuatro criterios (a-d) de la tarea son evaluables. |
| Anonimización | Sí ("trabaja solo con las frases"). Aquí no hay datos: la instrucción cumple la decisión editorial 7 sin sobrecargar. |
| Variables | **No hay corchetes**, y "Hazlo hoy" paso 2 dice "pega el prompt del caso 2 con tus frases". El lector tiene que adivinar que puede sustituir las tres frases. |
| Portabilidad | Sin cambios en los tres. |
| Ejemplo de salida | Realista. Es la clase de tabla que devuelven los tres modelos. Las dos reescrituras respetan las 25 palabras. |
| Riesgo principal | Bien identificado (fórmula vacía). |

### Ejecución mental
Los tres modelos devuelven la tabla con tres filas. Riesgo observado: la tercera frase ("fuerza de voluntad") tiende a reescribirse con una promesa suave ("juntos lo vamos a conseguir"), que choca con "sin promesas de resultado"; el lector debe cazarlo, y el capítulo ya lo advierte. Claude tiende a frases más largas que 25 palabras; ChatGPT a preguntas retóricas; Gemini a "entiendo que…". Pedir **dos alternativas** por frase da al lector elección real y reduce el efecto guion.

Rúbrica: fidelidad alta, acción segura alta (no hay decisión clínica), calibración no aplica.

### Problemas
1. Frases fijas sin corchetes (contradice "Hazlo hoy").
2. Rol en masculino (T4).
3. "Trato de usted" fijo; hay consultas donde se tutea. Convertirlo en variable.
4. Una sola versión por frase.

### Versión corregida
```
ROL: Eres médica de familia con formación en comunicación centrada en la persona y en el abordaje de la obesidad como enfermedad crónica.

CONTEXTO: Trabajo en Atención Primaria con consultas de siete minutos. Estas son tres frases que digo a menudo a personas con obesidad y que quiero dejar de decir tal cual:
1. "[frase 1, por ejemplo: Tiene que comer menos.]"
2. "[frase 2, por ejemplo: Es cuestión de moverse más.]"
3. "[frase 3, por ejemplo: Con un poco de fuerza de voluntad lo consigue.]"

TAREA: Reescribe cada frase para que (a) reconozca que la obesidad tiene una base biológica, (b) no culpe ni moralice, (c) abra una conversación en lugar de cerrarla, y (d) pueda decirse en voz alta en menos de diez segundos. Dame dos alternativas por frase con tonos distintos, para que yo elija la que suena a mí.

FORMATO: Tabla con cuatro columnas: frase original, alternativa 1, alternativa 2, por qué funcionan mejor (una línea).

RESTRICCIONES: Máximo 25 palabras por frase reescrita. Trato de [usted / tú]. Sin "debería", sin promesas de resultado ("lo va a conseguir", "seguro que"), sin mencionar fármacos ni dietas concretas, sin la palabra "obeso/a". No incluyas datos de ningún paciente: trabaja solo con las frases.
```

Ajustar el ejemplo de salida a cuatro columnas (basta con añadir una segunda alternativa a las dos filas que ya hay).

---

## Caso 3 · La adaptación metabólica en 150 palabras · veredicto: LISTO

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, completos. El contexto declara explícitamente que no hay datos de la persona. |
| Anonimización | Sí, y de la forma correcta para este uso: "escribe para un caso genérico". |
| Variables | No hacen falta. |
| Portabilidad | Sin cambios. "Nivel de lectura de 12 años" lo interpretan los tres. |
| Ejemplo de salida | Realista (109 palabras; el prompt pide máximo 150). El "termostato" es la metáfora que los tres modelos eligen espontáneamente. Fisiología correcta: más hambre, menos saciedad, menos gasto en reposo. |
| Riesgo principal | Bien identificado (nihilismo). La mitigación es de comunicación, no de prompt; correcta. |

### Ejecución mental
Los tres devuelven un párrafo muy parecido al ejemplo. Desvíos observables: ChatGPT añade con frecuencia una cifra ("hasta un 15 % menos de gasto") que el prompt permite si es "muy sencilla"; esa puerta conviene cerrarla, porque el capítulo ya dice en "qué revisar" que ninguna cifra debe aparecer sin saber de dónde sale. Gemini a veces introduce "recaída" como "volver a ganar peso no es una recaída", lo que técnicamente incumple la restricción pero es inofensivo. Claude respeta las palabras prohibidas.

Rúbrica: fidelidad alta, calibración adecuada (no promete), acción segura alta.

### Problemas (menores)
1. "Sin cifras salvo que sean muy sencillas" abre la puerta a cifras inventadas. Sustituir por "sin cifras ni porcentajes".
2. El texto es oral y no lleva disclaimer, lo que es correcto. Pero si el lector decide imprimirlo, pasa a ser material entregado: añadir una línea en "qué revisar".
3. Añadir "sin diagnósticos ni consejos individuales" para que el modelo no cierre con "en su caso…".

### Versión corregida (cambios mínimos, marcados)
```
ROL: Eres médica de familia especialista en obesidad y muy buena explicando ciencia en lenguaje sencillo.

CONTEXTO: Necesito una explicación oral para decir en consulta a una persona adulta con obesidad que ha bajado de peso varias veces y lo ha recuperado. No tengo datos de esta persona ni los necesitas: escribe para un caso genérico.

TAREA: Explica qué es la adaptación metabólica y por qué el cuerpo defiende su peso tras una pérdida (más hambre, menos saciedad, menor gasto energético).

FORMATO: Un solo párrafo de 150 palabras como máximo, trato de [usted / tú], nivel de lectura de 12 años.

RESTRICCIONES: Sin cifras ni porcentajes. Sin culpa ni palabras como "fracaso" o "recaída". Sin nombrar medicamentos ni dietas. Sin consejos individuales ("en su caso…"). Termina con una frase que abra a que la enfermedad tiene tratamiento y seguimiento, sin prometer resultados. No uses el término "obeso/a".
```

Línea para "qué revisar": "Este texto es para decirlo tú. Si lo imprimes para entregarlo, deja de ser oral: añade el disclaimer del caso 6 y fírmalo."

---

## Caso 4 · Sesión del centro · veredicto: MEJORAR

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, completos. La tarea en tres bloques es clara y el formato con minutaje es útil. |
| Anonimización | Sí, doble: en "Antes de nada" (solo documentos públicos) y en restricciones (sin casos de pacientes). |
| Variables | No hay, pero las fuentes que hay que cargar están nombradas fuera del prompt. Correcto para NotebookLM. |
| Portabilidad | **Necesita nota.** "Las fuentes cargadas en este cuaderno" solo tiene sentido en NotebookLM. En Gemini, ChatGPT o Claude hay que adjuntar los PDF a la conversación (o a un Proyecto / Gem) y cambiar la frase. |
| Ejemplo de salida | Plausible en contenido y minutaje (6+7+5 = 18 min + 2 de preguntas). Detalle: NotebookLM cita con números que enlazan a pasajes, no con "[Lancet 2025, sección 2]"; el ejemplo es una traducción legible, aceptable, pero conviene decir "las citas aparecen como números que puedes abrir". |
| Riesgo principal | Bien identificado (atribución falsa) y con mitigación correcta (cita a cita, fuente en pantalla). |

### Ejecución mental (NotebookLM con 4 fuentes públicas)
Devuelve un guion por bloques con citas numeradas. Comportamientos a vigilar: (a) mezcla contenido de dos fuentes en una afirmación y cita solo una; (b) cuando algo no está en las fuentes, tiende a decirlo si se le pide (el prompt lo pide: bien), pero no lo lista de forma sistemática; (c) el "guion" sale como esquema para leer, no como texto para decir en voz alta, salvo que se le pida. En Gemini/ChatGPT/Claude con PDF adjuntos, el resultado es similar pero las citas son menos trazables (página o sección aproximada) y el modelo completa con conocimiento propio aunque se le prohíba: es el riesgo que el capítulo ya nombra, y por eso NotebookLM es la mejor elección aquí.

Rúbrica: fidelidad depende de la verificación (el prompt la fuerza), priorización buena, confusores: puede colar recomendaciones farmacológicas de la guía GIRO con nombre comercial si la guía los usa; la restricción lo cubre.

### Problemas
1. Nota de portabilidad ausente (T1).
2. Falta un cierre determinista: "lista de afirmaciones que querías incluir y no están en las fuentes". Convierte "si algo no está, dilo" en una salida obligatoria (T2).
3. Formato: pedir "texto para decir" (dos o tres frases por bloque) además de la frase clave; el lector no tiene la tarde para convertir un esquema en discurso.
4. Público mixto: pedir que el bloque 3 distinga qué puede hacer enfermería y qué medicina. Es lo que hace que el equipo se lo lleve.
5. Fuente "resumen de la Comisión de The Lancet 2025": mejor cargar el artículo completo si el lector tiene acceso; el resumen puede no contener lo que el guion afirma. Decirlo en "Antes de nada".

### Versión corregida
```
ROL: Eres una docente clínica que prepara sesiones para equipos de Atención Primaria.

CONTEXTO: Las fuentes cargadas en este cuaderno son guías y consensos públicos sobre obesidad como enfermedad crónica. El público es un equipo de centro de salud: medicina de familia, enfermería, residentes. Nadie es especialista en obesidad. La sesión dura 20 minutos, de los cuales los últimos 3 son debate.

TAREA: Redacta el guion de la sesión con este hilo: (1) por qué la obesidad es una enfermedad crónica y no una falta de voluntad, con la biología en tres ideas; (2) qué cambia en la práctica de AP: registro, lenguaje, seguimiento; (3) tres cosas que el equipo puede hacer desde el lunes, indicando cuáles corresponden a enfermería, cuáles a medicina y cuáles a ambos.

FORMATO: Guion por bloques con minutaje. En cada bloque: una frase clave, dos o tres frases para decir en voz alta y la cita de la fuente cargada de la que sale cada afirmación clínica. Al final: (a) tres preguntas para abrir debate; (b) una lista titulada "NO ESTÁ EN LAS FUENTES" con cualquier idea del hilo que no hayas podido sustentar en los documentos cargados; si está vacía, escríbelo.

RESTRICCIONES: Usa solo las fuentes cargadas; no completes con conocimiento propio. Sin nombres comerciales de medicamentos: si una fuente los usa, sustitúyelos por el principio activo. Usa siempre "persona con obesidad". No incluyas casos de pacientes ni datos de personas.
```

Nota de portabilidad a añadir:

> **Si no usas NotebookLM.** En Gemini, ChatGPT o Claude adjunta los mismos PDF a la conversación y cambia la primera frase del contexto por "Las fuentes son los documentos adjuntos". Las citas serán menos precisas (sección o página aproximada) y el modelo tenderá a rellenar con lo que sabe; la lista "NO ESTÁ EN LAS FUENTES" es tu red.

---

## Caso 5 · Inventario de mi tiempo · veredicto: MEJORAR

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, los cinco. |
| Anonimización | Sí (contexto y restricción). Pero la barrera vuelve a estar en el modelo, no en el registro. |
| Variables | `[pega aquí tu lista]` claro, pero sin formato: el lector no sabe si escribir "tarea - minutos", una tabla o prosa. |
| Portabilidad | Sin cambios, con la salvedad de T2 ("pregúntame en lugar de suponer"). |
| Ejemplo de salida | Realista: 1.860 min/semana (31 h en tareas de más de 5 min) es creíble; los porcentajes suman 100; las tres tareas con margen son las que aparecen en la práctica. |
| Riesgo principal | Bien identificado (tiempo de sombra). Falta el segundo riesgo: identificación indirecta en las descripciones. |

### Ejecución mental (lista sintética de 48 tareas, dos ambiguas, una que dice "llamada a la hija de la señora con demencia de la calle X")
- ChatGPT y Gemini clasifican las 48, incluidas las ambiguas, y añaden al final "he asumido que…". No preguntan. Claude a veces se detiene y pregunta, a veces clasifica y pregunta. El comportamiento no es predecible: **hay que pedir una categoría "por aclarar"**.
- "Consulta" y "seguimiento de crónicos" se solapan: una revisión programada de hipertensión es ambas. Sin definición, cada modelo reparte distinto y el porcentaje del 62 % no es comparable entre semanas.
- La tarea con "la hija de la señora… de la calle X": los tres modelos la procesan y, con suerte, avisan. Es un dato cuasi identificable escrito por la propia médica. La barrera correcta es en el registro: **anotar tipos de tarea, no episodios**.
- "Candidata a IA (sí/no)" es demasiado binario: un informe para inspección lleva datos reales y solo puede prepararse con herramienta con contrato; una plantilla de recordatorio se hace sin datos. El prompt debería distinguirlo, porque es exactamente la regla de "Dos herramientas, dos reglas".

Rúbrica: priorización buena, calibración baja (asume sin decir), acción segura: correcta gracias a "no propongas automatizar decisión clínica".

### Problemas
1. Instrucción de preguntar no fiable (T2).
2. Sin definición de los cinco momentos (decisión editorial 4 de `biblia.md` los nombra pero no los define; el prompt debe hacerlo en una línea cada uno).
3. Sin formato de la lista.
4. "Candidata a IA" binaria; debe tener tres valores.
5. Barrera de anonimización en el registro, no solo en el modelo.

### Versión corregida

Añadir antes del prompt: "Anota tareas, no personas: 'llamada de seguimiento' y no 'llamada a la hija de…'. Una tarea por línea, con este formato: descripción; minutos."

```
ROL: Eres un consultor de organización que ayuda a médicos de Atención Primaria a entender en qué se va su jornada.

CONTEXTO: Te pego una lista de tareas de una semana de trabajo, una por línea, con el formato "descripción; minutos". No contiene datos de pacientes, solo descripciones genéricas ("informe para inspección", "revisión de analíticas", "llamada de seguimiento"). Los cinco momentos en los que quiero clasificar son: CONSULTA (atención a demanda, presencial o telefónica); SEGUIMIENTO DE CRÓNICOS (revisiones programadas y sus preparativos); ADMINISTRACIÓN Y BUROCRACIA (informes, partes, recetas, correo, gestión); DOCENCIA Y FORMACIÓN (sesiones, residentes, estudio); DIVULGACIÓN Y COMUNIDAD (charlas, redes, actividades comunitarias).

TAREA: (1) Clasifica cada tarea en uno de los cinco momentos; si una descripción admite dos o no es clara, clasifícala como POR ACLARAR. (2) Suma minutos por momento (POR ACLARAR aparte). (3) Para cada tarea, indica si puede prepararse o redactarse con apoyo de IA, con tres valores posibles: NO (requiere mi presencia o una decisión clínica); SÍ SIN DATOS (plantilla, guion, texto base que no necesita datos de personas); SÍ SOLO CON HERRAMIENTA CON CONTRATO (necesita datos clínicos reales).

FORMATO: Tabla con tarea, momento, minutos, apoyo de IA (NO / SÍ SIN DATOS / SÍ SOLO CON CONTRATO) y por qué en una línea. Debajo: resumen de minutos y porcentaje por momento; las tres tareas donde más tiempo se recuperaría con "SÍ SIN DATOS"; y una lista de preguntas, una por cada tarea POR ACLARAR.

RESTRICCIONES: No inventes tareas ni duraciones. No cambies mis descripciones. No propongas automatizar nada que implique decisión clínica. Si alguna línea contiene algo que parezca identificar a una persona (nombre, dirección, parentesco con detalles, fecha), no la clasifiques: ponla en una lista "REVISAR PRIVACIDAD" y dime por qué.

LISTA:
[pega aquí tu lista, una tarea por línea: descripción; minutos]
```

Ajustar el ejemplo de salida: sustituir "candidata a IA" por los tres valores y añadir la línea "POR ACLARAR: 'revisión de casos' (40 min), 'gestión de correo' (55 min). ¿Qué incluían?" en lugar de la pregunta suelta.

---

## Caso 6 · "¿Por qué recupero el peso?" en tres niveles · veredicto: MEJORAR (leve)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Sí, completos. La tarea fija los cuatro contenidos obligatorios: muy bien. |
| Anonimización | Sí, en contexto ("lector genérico"). |
| Variables | No hacen falta. |
| Portabilidad | Sin cambios. |
| Ejemplo de salida | Realista en tono y contenido. Tiene 69 palabras frente a las 100 pedidas; como es "abreviado" pasa, pero conviene que el ejemplo esté en rango para no enseñar al lector que el modelo entrega la mitad. |
| Riesgo principal | Bien identificado (desactivación) con mitigación concreta (siguiente paso y cita). |
| Disclaimer | Literal y correcto según `biblia.md`. **Choca en persona gramatical** con el texto ("Hable con su médica" / "tu profesional"). |

### Ejecución mental
Los tres modelos entregan A, B y C con el disclaimer. Desvíos observados: en el nivel C, ChatGPT y Gemini tienden a añadir hormonas de más (cortisol, "hormonas del estrés", adiponectina) y, con cierta frecuencia, invierten el sentido de alguna ("la leptina sube y da hambre"). También aparece la cifra de Polidori ("100 kcal por kilo perdido") aunque no se pida; es correcta, pero la restricción "sin cifras de pérdida de peso esperada" no la cubre. El nivel A sale a veces en tuteo si el prompt no fija el trato. Longitudes: ±20 % sobre lo pedido.

Rúbrica: fidelidad alta en A y B, media en C sin restricción de hormonas; confusores: cortisol; acción segura: alta (remite al profesional).

### Problemas
1. Trato no especificado; el ejemplo usa usted y el disclaimer tutea (T6).
2. Nivel C sin lista cerrada de hormonas ni exigencia de dirección del cambio.
3. "Sin cifras de pérdida de peso esperada" es estrecho; mejor "sin cifras ni porcentajes".
4. Recuentos de palabras exactos (T3).
5. Falta línea de firma: el capítulo dice "que lo firmes tú"; el prompt puede dejar el hueco preparado.

### Versión corregida
```
ROL: Eres médica de familia especialista en obesidad y redactora de materiales para pacientes.

CONTEXTO: Necesito un texto informativo para entregar en consulta a personas adultas con obesidad que han recuperado peso tras dietas. No dispones ni necesitas datos de ninguna persona concreta: escribe para un lector genérico. Trato de [usted / tú] en las tres versiones.

TAREA: Responde a la pregunta "¿Por qué recupero el peso después de una dieta?" en tres versiones: (A) nivel básico, frases muy cortas, unas 100 palabras; (B) nivel medio, unas 180 palabras; (C) nivel alto, unas 250 palabras, nombrando solo estas hormonas: leptina, grelina, GLP-1 y PYY, e indicando en cada una si sube o baja tras perder peso. Las tres deben explicar: que el peso está regulado, que tras bajar de peso aumenta el hambre y baja el gasto energético, que esto es biología y no falta de voluntad, y que la obesidad es una enfermedad crónica con tratamiento y seguimiento.

FORMATO: Tres textos separados con encabezado A, B, C y un título común breve. Al final de cada uno, incluye literalmente esta frase: "Material informativo generado con apoyo de IA y revisado por tu profesional sanitario. No sustituye la valoración clínica individual." Debajo, deja una línea: "Revisado por: ________  Fecha: ________".

RESTRICCIONES: Sin nombres de medicamentos. Sin cifras ni porcentajes. Sin "obeso/a", "fracaso", "recaída" ni "culpa". Sin recomendar dietas concretas ni consejos individuales. Sin otras hormonas que las cuatro indicadas. Tono cálido y directo, sin condescendencia. Si no estás seguro del sentido del cambio de una hormona, omítela en lugar de adivinar.
```

Añadir a "qué revisar": "En el nivel C comprueba el sentido de cada hormona: leptina baja, grelina sube, GLP-1 y PYY bajan. Si el modelo dice lo contrario, no lo corrijas a mano: pídele que lo revise y vuelve a leer."

---

## Preguntas y notas para el REDACTOR
- Aplicar T1 (frase global de portabilidad), T4 (género del rol) y T3 ("aproximadamente" en recuentos) en la v2.
- Añadir en "Dos herramientas, dos reglas" la frase sobre configuración de entrenamiento y borrado de conversaciones (T5).
- Las versiones corregidas mantienen la voz y la extensión; ninguna supera en más de un 25 % la longitud del prompt original, salvo el Caso 1, que es el que más lo necesita.
- El Caso 1 corregido es un prompt en dos turnos. Es una novedad para el lector: conviene una frase en la "Situación" que lo anuncie ("este prompt trabaja en dos pasos: primero comprueba, después cuenta").
