# Capítulo 7 · Buscar y leer evidencia sin ahogarte

**Deep Research, NotebookLM y lectura crítica en el tiempo que de verdad tienes.**

Un paciente me preguntó por un estudio que había salido en el telediario. No lo había leído. Tardé dos minutos en tenerlo delante y diez en saber qué opinar.

Hace unos años le habría dicho "lo miro y le cuento", y no lo habría mirado: entre la noticia y el artículo hay un titular, una nota de prensa y una tarde que no tengo. Esta vez el artículo estaba en pantalla antes de que se sentara del todo.

Los diez minutos siguientes no los hizo la máquina. Los hice yo: quién entró en el estudio, cuánto duró, qué midió y qué había exagerado la tele. Le contesté con dos frases y una tercera que no sale en los telediarios: lo que aún no se sabe.

*Como todas las escenas de consulta de este libro, es una composición de varias personas.*

## Lo que te vas a llevar

- Qué herramienta para qué pregunta: orientarse, encontrar estudios, leer lo tuyo y verificar; ninguna sustituye a PubMed, a CIMA ni a la guía en PDF.
- Una plantilla para leer un ensayo en diez minutos y la pregunta que decide: ¿esto cambia lo que hago el lunes con las personas de mi cupo?
- Un protocolo para que ninguna referencia entre en una sesión, un artículo o un libro sin que la hayas abierto.

---

## Primera parte · Enterrada, no lejos

A PubMed entran más de un millón de artículos nuevos cada año (Landhuis 2016 [VERIFICAR cifra en el original]). Nadie lee eso. La evidencia no está más lejos que hace veinte años: está más enterrada.

Y la pregunta llega antes que el artículo: la trae la persona, del telediario, o la trae la consulta: "¿se pierde músculo con esto?", "¿a quién derivo?", "¿el programa del centro sirve?". Antes contestaba con lo que recordaba, o no contestaba.

Ahora hago tres cosas: convierto la duda en una pregunta que se pueda buscar; dejo que la máquina desentierre, localice, estructure y ordene; y leo yo lo desenterrado, con rúbrica, en el tiempo que tengo. Lo tercero cuesta lo mismo, y es lo que vale.

La máquina desentierra. Leer sigue siendo mío.

---

## Segunda parte · Cuatro tipos de herramienta

"Buscar con IA" son cuatro cosas distintas, y confundirlas es el error más común. Los nombres cambian cada pocos meses: es cuando escribo esto; comprueba la versión vigente.

| Tipo | Qué entra | Qué devuelve | Cuándo miente |
|---|---|---|---|
| **Buscador con IA** (Perplexity; Deep Research y los modos de búsqueda profunda de Gemini, ChatGPT y Claude) | Una pregunta en lenguaje natural. Nada de nadie. | Un texto redactado con enlaces a webs. Para orientarse y pasar del titular al artículo. | Cuando la fuente es una web y no un estudio; cuando resume la nota de prensa y no el ensayo. |
| **Buscador de evidencia** (Consensus, Elicit, Scite, OpenEvidence) | Una pregunta clínica. Nada de nadie. | Estudios indexados y clasificados, a veces con un "consenso". Para encontrar y ordenar. | Cuando el "consenso" se lee como metaanálisis y es un recuento de resúmenes. |
| **Asistente con archivos o NotebookLM** | Tus documentos: guías públicas, un ensayo de acceso abierto. Nada de nadie. | Respuestas con cita a tus fuentes, comparaciones, resúmenes. | Cuando "recuerda" en vez de leer (capítulo 2, caso 3); cuando el dato del medio del PDF no aparece. |
| **PubMed y CIMA** | Una cadena de búsqueda; un principio activo. | Lo que existe: el registro del artículo, la ficha técnica autorizada. Sin IA. | No mienten. Se quedan cortos: PubMed no lee por ti; CIMA dice lo autorizado, no lo último publicado. |

La diferencia que más importa es la del capítulo 2 (caso 2): un buscador con IA busca y después redacta; un chat sin búsqueda redacta de memoria, y de memoria construye referencias con forma de verdad. Si la respuesta trae enlaces, ha buscado; si no, no te fíes de ninguna cita.

---

## Tercera parte · Leer con rúbrica también un artículo

Un resumen estructurado de un ensayo es una salida de la máquina como cualquier otra: bien escrita y capaz de equivocarse con aplomo. Las cinco preguntas del capítulo 4 le sirven tal cual:

- **Fidelidad.** ¿Dice lo que dice el artículo? Cada cifra con su página; la que no la tiene, no existe.
- **Priorización.** ¿El desenlace principal va primero? Si abre con un secundario llamativo, ha enumerado, no leído.
- **Calibración.** ¿El efecto lleva su intervalo de confianza? Una cifra sola es un titular.
- **Confusores.** ¿Quién entró, contra qué se comparó, quién lo pagó? Población, comparador y financiación.
- **Acción segura.** ¿Cambia lo que hago el lunes con las personas de mi cupo? Si no, es cultura; si sí, se lee entero antes.

El itinerario de herramientas, de orientarse a verificar, y leer un artículo con la misma rúbrica que una salida los traigo de mi formación en IA; el "qué cambia el lunes" es de esta consulta.

---

## Siete casos para buscar y leer

Mismo molde que en los capítulos 4 a 6; ninguno admite datos identificables. POR ACLARAR la contestas tú fuera del chat; [FALTA: …] lo rellenas tú fuera de la IA (capítulo 3). Nunca dejes que el modelo rellene ninguno de los dos.

No dispongo de ninguna herramienta con acuerdo de tratamiento de datos, como la mayoría; por eso aquí entran preguntas generales, documentos públicos, resúmenes de PubMed y tablas agregadas que construyes tú, y ninguna persona. Conversación nueva y memoria apagada. Hoy los siete se pegan en Gemini, ChatGPT y Claude; el 2 está pensado para NotebookLM; el 3 necesita archivos; el 4, búsqueda activada; el 5 va mejor con código. Comprueba la versión vigente. Ficha del capítulo 4, caso 7.

### Caso 1 · De la duda a la pregunta PICO

**Momento:** consulta. **Herramienta:** consumo, sin búsqueda; después, PubMed y un buscador de evidencia.

**Situación.** "¿Se pierde músculo con el tratamiento farmacológico de la obesidad, y qué lo evita?" Es una duda de consulta, no una pregunta de búsqueda; la diferencia son cuatro letras: población, intervención, comparador, desenlace (Richardson 1995). El prompt no contesta la duda: la convierte en pregunta y en tres cadenas, y dice qué no cubre.

```
ROL: Eres una documentalista clínica que ayuda a médicas de familia a formular preguntas de búsqueda. No respondes preguntas clínicas: las formulas.

CONTEXTO: Soy médica de familia en España. Tengo una duda de consulta, general, sin ninguna persona detrás. LO QUE SÉ, con mis palabras: [por ejemplo: al bajar de peso se pierde algo de masa magra, con dieta y con fármacos]. LO QUE BUSCO: [por ejemplo: cuánta masa muscular se pierde con el tratamiento farmacológico de la obesidad en adultos y qué la conserva: ejercicio de fuerza, proteína]. Voy a usar PubMed, un buscador de evidencia en inglés y un buscador con IA en español.

TAREA, en este orden:
(1) La pregunta en formato PICO, una línea por letra: Población; Intervención; Comparador; Desenlace, medible (qué se mide, con qué y en cuánto tiempo). Si LO QUE BUSCO mezcla dos preguntas, sepáralas y numera dos PICO.
(2) TRES CADENAS DE BÚSQUEDA: (a) para PubMed, con AND/OR, términos MeSH marcados [MeSH] y sus sinónimos en texto libre; (b) en inglés y en lenguaje natural, una frase, para un buscador de evidencia; (c) en español, una frase, para orientarme en un buscador con IA.
(3) LO QUE LA PREGUNTA NO CUBRE: lo que alguien creería que responde y no (otras poblaciones, otros desenlaces, seguridad, coste, a quién se indica).

FORMATO: (0) Una línea: "DUDA SIN DATOS" o "DUDA CON DATOS: BORRA ESTA CONVERSACIÓN" si LO QUE SÉ o LO QUE BUSCO contienen un nombre, una edad exacta, una fecha o cualquier dato de una persona; en ese caso, para. Después (1), (2) y (3). Última línea, literal: "PICO: [n] · CADENAS: 3 · TÉRMINOS MeSH PROPUESTOS: [n], todos por comprobar en el MeSH Browser · NO CUBRE: [n]".

RESTRICCIONES: No respondas la pregunta clínica, ni en una frase. Sin cifras de eficacia. Sin nombres de fármacos, comerciales ni de principio activo: si hace falta, por mecanismo o clase. No inventes términos MeSH: si dudas, ponlo en texto libre. No busques en internet. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> DUDA SIN DATOS
> PICO 1. P: adultos con obesidad en tratamiento farmacológico. I: el tratamiento. C: estilo de vida sin fármaco, o placebo. D: cambio de masa magra (DXA o bioimpedancia) a 6-12 meses. PICO 2. […]
> (a) ("Anti-Obesity Agents"[MeSH] OR "weight loss medication") AND ("Body Composition"[MeSH] OR "lean mass" OR "muscle mass") AND ("Resistance Training"[MeSH] OR "protein intake")
> NO CUBRE: mayores de 75 años; fuerza o función, no masa; seguridad; a quién se indica.
> PICO: 2 · CADENAS: 3 · TÉRMINOS MeSH PROPUESTOS: 3, todos por comprobar en el MeSH Browser · NO CUBRE: 4

**Qué revisar antes de usarla.** Los términos MeSH, uno por uno, en el MeSH Browser de la NLM: la máquina los inventa igual que inventa referencias. Pega la (a) en PubMed: cero resultados es un término mal escrito; miles, que falta el desenlace. La (b) en Consensus, Elicit o el que uses; la (c) en Perplexity o en el modo de búsqueda de tu asistente, solo para orientarte. Si el modelo ha contestado la pregunta "de paso", no lo leas: no ha buscado.

**Riesgo principal y mitigación.** Que la pregunta bien formulada parezca ya respondida. Mitigación: el prompt no responde, y "NO CUBRE" te recuerda qué no vas a saber.

### Caso 2 · Tres guías, una pregunta: coincidencias y discrepancias con cita [AP]

**Momento:** consulta. **Herramienta:** NotebookLM o asistente con archivos, con guías públicas cargadas.

**Situación.** Buscar un dato en una guía con página ya está (capítulo 2, caso 3), y la sesión con NotebookLM también (capítulo 1, caso 3). Esto es la misma pregunta a tres guías a la vez, y lo que importa es dónde no coinciden. Solo documentos públicos de su web oficial, para uso personal: la GIRO 2024 de la SEEDO, la canadiense (Wharton 2020) y una tercera si la conoces [VERIFICAR: NICE NG246, 2025]. A quién derivas no lo decide la tabla: capítulo 8.

```
ROL: Eres una documentalista clínica que compara guías. Trabajas solo con las fuentes cargadas; lo que sepas por tu cuenta no cuenta.

CONTEXTO: En este cuaderno hay tres guías públicas sobre obesidad en personas adultas, descargadas de sus webs oficiales para uso personal: [por ejemplo: GIRO 2024 (SEEDO); Wharton 2020 (CMAJ); una tercera guía nacional o europea]. No contienen datos de pacientes. PREGUNTA: [por ejemplo: ¿qué criterios da cada guía para derivar desde Atención Primaria a una unidad o consulta especializada de obesidad?].

TAREA: (1) Busca la respuesta a la PREGUNTA en cada guía por separado. (2) Una tabla con una columna por guía y una fila por criterio; en cada celda, la cita literal entre comillas, sin resumir, y su número de cita o página; si está en otro idioma, la traducción debajo, marcada como tuya. Si una guía no dice nada sobre ese criterio, escribe en la celda "NO LO DICE". (3) Debajo de la tabla, tres filas con estos títulos: "COINCIDEN" (criterios que las tres dan con el mismo sentido), "DISCREPAN" (criterios en los que difieren, con las cifras o palabras que difieren) y "NO LO DICE NINGUNA" (lo que la PREGUNTA esperaría encontrar y ninguna trae).

FORMATO: (0) Una línea: "FUENTES: [n] · [títulos que ves]". Si no son tres, o alguna no es una guía clínica, o alguna contiene datos de personas, escribe "FUENTES NO VÁLIDAS" y para. Después la tabla y las tres filas, nada más. Última línea, literal: "CITAS LITERALES: [n] · CELDAS 'NO LO DICE': [n] · CRITERIOS EN 'COINCIDEN': [n]": cada celda con comillas cuenta una cita.

RESTRICCIONES: Solo las fuentes cargadas: no completes con otras guías, con "la práctica habitual" ni con lo que sepas. No decidas a quién derivar ni recomiendes nada: eso lo decido yo. Si una guía usa nombres comerciales de fármacos, sustitúyelos por el principio activo. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> FUENTES: 3 · GIRO 2024 · Wharton 2020 · [tercera guía]
> | IMC y comorbilidad | "[cita literal]" [cita 4] | "[cita literal]" [cita 11] | NO LO DICE |
> COINCIDEN: valorar la derivación cuando no hay respuesta en el primer nivel [VERIFICAR contra las guías]. DISCREPAN: el umbral de IMC y el tiempo sin respuesta. NO LO DICE NINGUNA: qué hacer mientras dura la espera.
> CITAS LITERALES: 7 · CELDAS 'NO LO DICE': 2 · CRITERIOS EN 'COINCIDEN': 1

**Qué revisar antes de usarla.** Abre cada cita con un clic y lee la frase entera con la anterior y la siguiente: NotebookLM cita bien casi siempre, y "casi" no vale. "DISCREPAN" es el valor de la tabla: un umbral distinto suele ser un sistema sanitario distinto, no un error. "NO LO DICE NINGUNA" es lo que decides tú sin guía. Con Gemini, ChatGPT o Claude, adjunta los tres PDF y cambia "cuaderno" por "documentos adjuntos"; rellenan con lo que saben.

**Riesgo principal y mitigación.** Que "COINCIDEN" se lea como criterio propio y salga en una interconsulta. Mitigación: la interconsulta es el capítulo 5 y la decisión el 8; esta tabla es lectura.

### Caso 3 · Un ensayo en diez minutos

**Momento:** docencia. **Herramienta:** asistente con archivos; el PDF de acceso abierto o, si no lo hay, su resumen.

**Situación.** Un ensayo tiene cuarenta páginas con el suplemento, y esa tarde no la tengo. La plantilla saca lo que la rúbrica necesita: diseño, quién entró, contra qué, qué se midió y con qué intervalo, quién se fue, qué efectos, quién pagó y lo que el resumen no dice. El ejemplo usa un ensayo de acceso abierto de semaglutida, a la dosis de obesidad, frente a placebo (Wilding 2021 [VERIFICAR acceso abierto y datos]); a quién se indica lo decide el capítulo 8.¹

¹ Declaración de transparencia: mantengo vínculos con Novo Nordisk, detallados al inicio del libro. Aquí los fármacos aparecen por principio activo o por clase, solo para leer un ensayo; a quién se indican y cómo se sigue va en el capítulo 8.

```
ROL: Eres una lectora crítica de ensayos clínicos, epidemióloga, que extrae datos de un artículo sin opinar sobre ellos.

CONTEXTO: Te adjunto el PDF de un ensayo clínico de acceso abierto sobre un fármaco para la obesidad. Es público; no contiene datos de personas y no debes añadir ninguno. MI CUPO, en rangos y sin ninguna persona: [por ejemplo: adultos de 40 a 75 años, obesidad de grados I a III, la mayoría con hipertensión o diabetes tipo 2, atendidos en Atención Primaria en España].

TAREA: Rellena esta plantilla solo con lo que está en el documento, con la página de cada dato: DISEÑO (tipo, aleatorización, enmascaramiento, duración, registro); POBLACIÓN (criterios de inclusión y exclusión, n, edad, sexo, IMC, comorbilidades) y una línea "¿SE PARECE A MI CUPO?" con las diferencias concretas; COMPARADOR; DESENLACE PRINCIPAL tal como lo define el artículo, y SECUNDARIOS; TAMAÑO DEL EFECTO del principal, con su intervalo de confianza y la diferencia entre grupos; PÉRDIDAS por grupo y tipo de análisis (por intención de tratar u otro); EFECTOS ADVERSOS con cifras absolutas por grupo (n de N y porcentaje), abandonos por efectos adversos y efectos graves; FINANCIACIÓN y conflictos de interés declarados; LO QUE EL RESUMEN NO DICE (datos del texto o las tablas que el abstract no trae).

FORMATO: (0) "Documento: [título] · Páginas que veo: [n]"; si no puedes leer el archivo entero, "LECTURA PARCIAL" y hasta dónde llegas. Después la plantilla, cada dato con "(p. [n])". Si un dato no está en el documento, escribe en su apartado "NO ESTÁ EN EL DOCUMENTO". Última línea, literal: "DATOS QUE NO ESTÁN EN EL DOCUMENTO: [n] · CIFRAS CON PÁGINA: [n] · CIFRAS SIN PÁGINA: [n]"; la última tiene que ser 0.

RESTRICCIONES: Solo el documento adjunto: nada de memoria, de otros ensayos ni de guías. Sin recomendaciones, sin decir a quién se indica el fármaco ni compararlo con otros. Nombra el fármaco por su principio activo; si el artículo usa el nombre comercial, sustitúyelo. No redondees ni conviertas: copia cada cifra con su unidad. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida (Wilding 2021 [VERIFICAR cada cifra en el artículo]).**

> Documento: Once-weekly semaglutide in adults with overweight or obesity · Páginas que veo: 14
> DISEÑO. Aleatorizado, doble ciego, con placebo, 68 semanas (p. [n]). POBLACIÓN. 1.961 adultos con IMC ≥ 30, o ≥ 27 con comorbilidad, sin diabetes (p. [n]). ¿SE PARECE A MI CUPO? En parte: excluye diabetes.
> TAMAÑO DEL EFECTO. Cambio de peso a la semana 68: −14,9 % frente a −2,4 %; diferencia −12,4 puntos (IC 95 %: −13,4 a −11,5) (p. [n]). EFECTOS ADVERSOS. Digestivos: 74,2 % frente a 47,9 %; abandonos por efectos adversos: 7,0 % frente a 3,1 % (p. [n]). FINANCIACIÓN. El fabricante del fármaco (p. [n]).
> LO QUE EL RESUMEN NO DICE: qué pasó con el peso después de la semana 68.
> DATOS QUE NO ESTÁN EN EL DOCUMENTO: 1 · CIFRAS CON PÁGINA: 19 · CIFRAS SIN PÁGINA: 0

**Qué revisar antes de usarla.** Tres cifras al azar, con el PDF abierto por la página que dice: la diferencia entre grupos, una de efectos adversos y las pérdidas. Si una no está en esa página, ninguna vale. "¿SE PARECE A MI CUPO?" la contestas tú con la tabla 1 del artículo delante: quiénes no entraron es lo que importa. Las cifras son las del ensayo leído, citadas, y no son un consejo: en quién, cuándo y cómo se sigue es el capítulo 8. La acción segura, aquí: no cambio nada con un solo ensayo.

**Riesgo principal y mitigación.** Que el resumen sustituya al artículo y las cifras viajen sin página a una diapositiva. Mitigación: "(p. n)" en cada cifra, "CIFRAS SIN PÁGINA: 0" y tres comprobadas a mano.

### Caso 4 · Del titular al artículo [AP]

**Momento:** divulgación y consulta. **Herramienta:** buscador con IA (Perplexity o el modo de búsqueda de tu asistente, activado); después, PubMed.

**Situación.** "He visto en la tele que cenar tarde engorda." En dos minutos, el estudio original, no la noticia; en diez, dos frases para la persona: lo que se vio, en quién y lo que la noticia estiró. El prompt pide primero el estudio con DOI y, solo cuando lo has abierto, la lectura. La respuesta suele decirse; si se escribe, lleva las líneas del capítulo 4. Sin culpa por lo visto en la tele.

```
ROL: Eres una documentalista científica que localiza, buscando en internet, el estudio original detrás de una noticia.

CONTEXTO: Soy médica de familia en España. Una persona me pregunta por un estudio que vio en un medio; te paso sus palabras, sin ningún dato suyo. LO QUE HA OÍDO: [por ejemplo: "que han descubierto que cenar tarde engorda"]. MEDIO Y FECHA: [por ejemplo: telediario, esta semana]. ENTREGA: [oral por defecto / escrita].

TAREA, en dos turnos:
PASO A (solo esto en tu primera respuesta): (1) una cadena de búsqueda de una línea; (2) el estudio original que mejor encaja (si dudas, dos): primer autor, año, revista, DOI, enlace y la línea "HE BUSCADO EN INTERNET: SÍ / NO"; si es NO, añade "DE MEMORIA: COMPROBAR ANTES DE SEGUIR"; si no hay ninguno, "NO LOCALIZADO" y para. Para; escribiré "continúa" tras abrir el DOI.
PASO B: (3) QUÉ DICE EL ESTUDIO, tres líneas: diseño y tamaño; en quién; resultado principal con cifra e intervalo si los hay. (4) QUÉ DIJO EL TITULAR Y QUÉ NO CUADRA, dos líneas. (5) RESPUESTA PARA LA PERSONA, dos frases en usted, sin cifras, sin consejo, sin decir si le conviene: qué se vio, en quién y qué falta por saber.

FORMATO: (0) Una línea: "PREGUNTA SIN DATOS" o "PREGUNTA CON DATOS: BORRA ESTA CONVERSACIÓN" si LO QUE HA OÍDO contiene nombre, edad exacta, tratamiento propio o cualquier dato personal; en ese caso, para. Si ENTREGA es escrita, (5) termina, literal, con "Si tiene dudas, [FALTA: contacto del centro]." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."; si el estudio trata de síntomas o de cambiar un tratamiento, en (5) escribe solo "ESTA RESPUESTA SE DICE, NO SE ESCRIBE". Última línea del paso B, literal: "ESTUDIOS: [n] · CIFRAS EN (3): [n] · CIFRAS EN (5): 0".

RESTRICCIONES: Sin nombres comerciales: principio activo o clase. No recomiendes empezar, dejar ni cambiar nada. Sin culpa ni "no debería creer lo que ve". Sin DOI inventados: si falta, "SIN DOI". No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> PREGUNTA SIN DATOS
> PASO A. Cadena: (late eating OR meal timing) AND (obesity OR weight gain). Estudio: [primer autor], [año], [revista], doi:[del artículo]. HE BUSCADO EN INTERNET: SÍ.
> PASO B. QUÉ DICE EL ESTUDIO. Ensayo cruzado, [n] adultos con sobrepeso, [duración], en laboratorio; más hambre y menos gasto con la cena tardía, [cifra del artículo]. QUÉ DIJO EL TITULAR. "Cenar tarde engorda"; el estudio midió hambre y gasto durante días, no kilos durante meses.
> RESPUESTA PARA LA PERSONA. Se ha visto, en un grupo pequeño y durante pocos días, que cenar tarde da más hambre al día siguiente. Lo que no se sabe es si eso cambia el peso a la larga.
> ESTUDIOS: 1 · CIFRAS EN (3): 3 · CIFRAS EN (5): 0

**Qué revisar antes de usarla.** El DOI en el navegador, antes de "continúa": si lleva a otro artículo, o a nada, se empieza en otra herramienta. "HE BUSCADO: NO" con un DOI perfecto es el caso 2 del capítulo 2. Perplexity y los modos de búsqueda de Gemini, ChatGPT y Claude, cuando escribo esto, enlazan la noticia antes que el estudio: pide el artículo y comprueba en PubMed. La respuesta la dices con tus palabras.

**Riesgo principal y mitigación.** Que la máquina "encuentre" el estudio que la noticia inventó, o resuma la nota de prensa como artículo. Mitigación: el DOI abierto por ti antes del paso B y la etiqueta de memoria.

### Caso 5 · Mis datos, agregados: el antes y después del programa del centro [AP]

**Momento:** seguimiento de crónicos. **Herramienta:** consumo, mejor si ejecuta código; tablas agregadas construidas en el ordenador del centro.

**Situación.** El programa de obesidad del centro lleva un año y alguien pregunta si sirve. Continúa el caso 6 del capítulo 1: recuentos, nunca filas, "<5" puesto por ti antes de subir nada y la política de datos del centro consultada. La máquina describe y, sobre todo, lista lo que no se puede concluir: el caso 6 del capítulo 5 enseñó que inventa tendencias y causas.

```
ROL: Eres una analista de datos que apoya a una médica de familia. Describes; no explicas causas ni recomiendas.

CONTEXTO: Te pego dos tablas agregadas por trimestre del programa de obesidad de mi centro, hechas por mí en la hoja de cálculo del centro. Sin filas individuales: cada celda es un número de personas, una media o una mediana; los recuentos menores de 5 ya aparecen como "<5". Tabla 1: personas en el programa; con visita en el trimestre; por categoría de IMC (obesidad_1 / obesidad_2 / obesidad_3 / sin dato). Tabla 2, con su n: mediana de HbA1c en quienes tienen diabetes; media de tensión sistólica; personas sin visita en dos trimestres seguidos. Sin grupo de comparación.

TAREA, en dos turnos:
PASO 0 (solo esto en tu primera respuesta): por cada tabla, sus columnas, valores distintos por columna y tres ejemplos. Marca SOSPECHOSO cualquier valor que no sea trimestre, categoría de arriba o número (texto libre, fechas, nombres, códigos); si lo hay, dime cuál y para. Si no, escribe "Tablas comprobadas: solo agregados, sin identificadores" y espera a que yo escriba "continúa".
PASO 1: (1) LECTURA DESCRIPTIVA, máximo seis frases: qué sube, baja o se mantiene, con cifra y n; nada más. (2) LO QUE NO SE PUEDE CONCLUIR, lista numerada, una frase sobre estas tablas por cada punto: sin grupo de comparación; regresión a la media; pérdidas y quién falta en cada numerador; cambio de composición entre trimestres; medias que ocultan a quien empeora; otros que veas. (3) QUÉ DATO PEDIRÍA para decir más, tres líneas.

FORMATO: El paso 0; después (1), (2), (3) y tus operaciones escritas, para comprobarlas. Última línea, literal: "FRASES DESCRIPTIVAS: [n] · LO QUE NO SE PUEDE CONCLUIR: [n] · VERBOS DE CAUSA: [n]": verbo de causa: "gracias a", "consiguió", "logró", "redujo", "efecto de", "mejoró por"; tiene que ser 0.

RESTRICCIONES: No inventes tendencias ni causas. Mantén "<5"; si una operación lo incluye, da un rango. Sin recomendaciones clínicas; no digas si el programa funciona. Si los totales no cuadran, dímelo y no los reconstruyas. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida (paso 1; cifras inventadas).**

> LECTURA DESCRIPTIVA. Personas en el programa: de 41 a 63. Con visita en el trimestre: del 85 % al 62 %. Mediana de HbA1c con diabetes: 7,4 % (n = 18) a 7,0 % (n = 11). Sin visita en dos trimestres: de <5 a 14.
> LO QUE NO SE PUEDE CONCLUIR. 1. Sin grupo de comparación, la HbA1c pudo bajar por lo mismo que en quien no está en el programa. 2. Quienes entraron con HbA1c más alta tienden a bajar solos: regresión a la media. 3. En el cuarto trimestre faltan 7 de 18. […]
> FRASES DESCRIPTIVAS: 5 · LO QUE NO SE PUEDE CONCLUIR: 6 · VERBOS DE CAUSA: 0

**Qué revisar antes de usarla.** Dos sumas y una mediana a mano. Busca "gracias", "logró", "efecto" y "mejora": el recuento dice cero y a veces miente. Lee la lista 2 antes que la 1: es la que vale y nadie la pide en la reunión. La regresión a la media no es una excusa: es lo que pasa cuando seleccionas a quien está peor (Barnett 2005). Y "sin visita en dos trimestres" no es un dato: son personas, y la llamada del capítulo 6 (caso 5) es para ellas.

**Riesgo principal y mitigación.** Presentar el antes y después como efecto del programa, con celdas que dejen adivinar quién es quién. Mitigación: la lista de lo que no se puede concluir, dicha en voz alta; "<5" puesto por ti; nunca el listado, solo tablas pegadas.

### Caso 6 · La alerta mensual de evidencia para el equipo [AP]

**Momento:** docencia. **Herramienta:** una alerta de PubMed (My NCBI) como fuente; un asistente de consumo para clasificar.

**Situación.** Lo honesto primero: la alerta fiable y gratuita es la de PubMed. Guardas una búsqueda en My NCBI y cada mes llega un correo con los resúmenes. La IA no busca aquí: clasifica lo que la alerta trae, con una regla tuya, en una página para la sesión. Resumir un resumen no es leer el artículo, y la página lo dice. Copia los resúmenes sin la cabecera del correo: tu dirección es un dato.

```
ROL: Eres una documentalista clínica que resume resúmenes para un equipo de Atención Primaria. No has leído los artículos: solo lo que te pego.

CONTEXTO: Te pego los resúmenes de mi alerta mensual de PubMed sobre obesidad en adultos, tal como llegan (título, autores, revista, DOI, resumen), sin la cabecera del correo. Son públicos. REGLA DE RELEVANCIA, la mía: CAMBIA LO QUE HAGO = ensayo aleatorizado, revisión sistemática o guía, en adultos, con desenlace clínico y algo que se pueda hacer desde Atención Primaria en España; CONVIENE SABERLO = estudio observacional o desenlace intermedio que puede aparecer en consulta o en una pregunta de pacientes; NO APLICA = animales, laboratorio, cirugía o unidades especializadas, o población que no atiendo.

TAREA: (1) Clasifica cada resumen con la REGLA y di en una frase qué parte cumple. (2) Para cada uno, en este orden: primer autor, año, revista, DOI; una línea con qué se estudió y en quién; otra con el resultado principal y su cifra si el resumen la da; y la etiqueta. (3) Ordena: primero CAMBIA LO QUE HAGO, después CONVIENE SABERLO, después NO APLICA solo con título y DOI.

FORMATO: (0) Una línea: "RESÚMENES SIN DATOS" o "TEXTO CON DATOS: BORRA ESTA CONVERSACIÓN" si el pegado contiene una dirección de correo, un nombre de usuario o cualquier dato de una persona; en ese caso, para. Después, una página: máximo 350 palabras, sin negritas, con el título "Evidencia del mes · [MES Y AÑO]" y debajo esta línea, literal: "Resumen de resúmenes: nadie ha leído aún los artículos. Antes de cambiar nada, se lee el artículo entero." Última línea, literal: "RECIBIDOS: [n] · CAMBIA LO QUE HAGO: [n] · CONVIENE SABERLO: [n] · NO APLICA: [n] · SIN DOI: [n]": los tres del medio suman el primero.

RESTRICCIONES: Solo lo que está en los resúmenes: no completes con lo que sepas ni añadas estudios que no te he pegado. No inventes DOI ni cifras: si faltan, "SIN DOI" o "sin cifra en el resumen". Sin nombres comerciales: principio activo o clase. Sin recomendaciones. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> RESÚMENES SIN DATOS
> Evidencia del mes · [mes y año]
> Resumen de resúmenes: nadie ha leído aún los artículos. Antes de cambiar nada, se lee el artículo entero.
> CAMBIA LO QUE HAGO. [Primer autor], [año], [revista], doi:[del resumen]. Ensayo aleatorizado en adultos con obesidad y artrosis de rodilla, en Atención Primaria; menos dolor a los 12 meses con ejercicio supervisado, [cifra del resumen]. Cumple: ensayo, adultos, desenlace clínico, se hace aquí.
> RECIBIDOS: 9 · CAMBIA LO QUE HAGO: 1 · CONVIENE SABERLO: 3 · NO APLICA: 5 · SIN DOI: 0

**Qué revisar antes de usarla.** Que los números sumen. Cada DOI de "CAMBIA LO QUE HAGO", en el navegador, y ese artículo se lee entero con el caso 3 antes de la sesión: uno o dos al mes, y eso cabe. Si todo sale "CONVIENE SABERLO", la regla es blanda. Las búsquedas programadas de tu asistente, si las tiene cuando escribo esto, son la segunda alerta: la de PubMed da lo que existe, sin ranking de nadie.

**Riesgo principal y mitigación.** Que la página se lea como "lo que hay que hacer este mes". Mitigación: la segunda línea, literal, y leer entero el uno o dos que cambian algo.

### Caso 7 · Verificar las referencias de mi sesión: el protocolo

**Momento:** docencia. **Herramienta:** asistente de consumo, sin búsqueda; después, PubMed y el navegador.

**Situación.** El capítulo 2 (caso 2) enseñó a cazar una referencia inventada. Esto es el protocolo para que no se escape ninguna, en tres pasos: (1) el prompt convierte la lista en tabla y marca lo que tiene aspecto sospechoso; (2) cada una se comprueba a mano, en PubMed por título y en el navegador por DOI; (3) cada una recibe su etiqueta. El prompt no verifica: prepara la verificación. Es el método con el que se han comprobado las referencias de este libro.

```
ROL: Eres una documentalista que prepara la verificación de una lista de referencias. No verificas: preparas la comprobación, que haré yo.

CONTEXTO: Te pego la lista de referencias de [por ejemplo: una sesión del centro / un artículo / un capítulo], tal como está escrita, sin datos de personas. Voy a comprobar cada una a mano en PubMed y en el navegador.

TAREA: (1) Una tabla con una fila por referencia y estas columnas: n; primer autor; año; revista; título; volumen y páginas; DOI; PMID; SEÑALES; COMPROBACIÓN. (2) En SEÑALES, escribe cada una de esta lista que se cumpla, y solo de esta lista: DOI que no empieza por "10." seguido de cuatro o más cifras y una barra; DOI cuyo prefijo no coincide con el de la editorial de esa revista; año y volumen que no cuadran entre sí para esa revista; revista que no conoces; autores que no asocias con ese tema; título que parece la suma de dos títulos; DOI o PMID repetido en otra fila; campo vacío. Si no hay ninguna, "NINGUNA". (3) COMPROBACIÓN se deja vacía: la relleno yo con EXISTE Y COINCIDE / EXISTE CON ERRORES / TRATA DE OTRA COSA / NO EXISTE. (4) Debajo, por cada fila, una línea para pegar en PubMed: el título entre comillas y el primer autor.

FORMATO: (0) Una línea: "LISTA SIN DATOS" o "LISTA CON DATOS: BORRA ESTA CONVERSACIÓN" si el pegado contiene nombres de pacientes, fechas de visita o cualquier dato de una persona; en ese caso, para. Después la tabla y las líneas de búsqueda. Última línea, literal: "REFERENCIAS: [n] · CON SEÑALES: [n] · SIN DOI: [n] · SIN PMID: [n]".

RESTRICCIONES: No completes ningún campo vacío con lo que recuerdes: un DOI o un PMID que no está en mi lista se deja vacío y cuenta como señal. No corrijas ninguna referencia ni propongas la "correcta". No busques en internet; si tu herramienta busca sola, marca "BUSCADO" en esa fila y la compruebo igual. No incluyas ni pidas datos de personas.
```

**Ejemplo abreviado de salida.**

> LISTA SIN DATOS
> | 2 | Martínez | 2022 | Nutr Hosp | Adaptación metabólica y… | vacío | 10.20960/nh.[…] | vacío | año y volumen no cuadran; campo vacío (volumen, PMID) | [COMPROBACIÓN] |
> Para PubMed: "Adaptación metabólica y" Martínez
> REFERENCIAS: 12 · CON SEÑALES: 4 · SIN DOI: 1 · SIN PMID: 9

**Qué revisar antes de usarla.** Todas, también las de "NINGUNA": una inventada puede no tener señales y una real tener tres. El orden importa: PubMed por título y primer autor; si aparece, el DOI en el navegador, y que abra ese artículo; después, que diga lo que la sesión dice que dice. "EXISTE CON ERRORES" se corrige; "TRATA DE OTRA COSA" es la peor, porque existe y se cita con confianza: se quita. De 115 referencias generadas por chat, casi la mitad no existía (Bhattacharyya 2023); con modelos más nuevos bajó, no desapareció (Walters 2023).

**Riesgo principal y mitigación.** Que "CON SEÑALES: 0" se lea como "verificado". Mitigación: la columna COMPROBACIÓN vacía hasta que la rellenas tú, y ninguna referencia entra en un documento tuyo sin que la hayas abierto. Ninguna.

---

## Caso ilustrativo, no real: arquetipo compuesto

> Esta viñeta combina varias consultas preconcepcionales de mujeres con obesidad en tratamiento farmacológico. Se modifican la edad, la paridad y el tratamiento; no hay municipio, fechas ni cifras que permitan trazar a nadie. Las búsquedas son las de los casos 1 y 4, y ninguna lleva un dato suyo.

Tiene entre treinta y treinta y cinco años, obesidad de grado II y, desde hace unos meses, un tratamiento que imita una hormona del intestino (nota del caso 3). En la primera visita le dije lo del guion del capítulo 6: si busca un embarazo, avíseme antes de nada. Ha venido a avisar. "Doctora, queremos ir a por el bebé. ¿Lo dejo hoy, o cuándo?"

La respuesta no la busco en la máquina; la busco en orden. Primero, la ficha técnica de su principio activo en CIMA, apartado de fertilidad, embarazo y lactancia: lo autorizado, con la antelación con que se suspende antes de buscar el embarazo. Un minuto. Segundo, lo que la GIRO 2024 dice de la mujer que planifica un embarazo [VERIFICAR apartado]. Tercero, PubMed, para la pregunta que la ficha no contesta.

La formulo con el caso 1, sin ella dentro: exposición inadvertida a esta clase de fármacos en el primer trimestre; qué se sabe y qué no. Lo que hay, cuando escribo esto, son series y registros, pocos y recientes, y ningún ensayo, porque no puede haberlo [VERIFICAR: revisión reciente]. Eso también es una respuesta, y se dice.

Ella trae algo leído: "He visto que no pasa nada si te quedas embarazada tomándolo". Caso 4: dos minutos, el estudio detrás del titular. Era un registro pequeño, y el titular había convertido "no se ha visto" en "no pasa". Se lo explico con dos frases: qué se ha visto, en cuántas, y qué falta por saber.

Lo que le digo sale de la ficha y de la guía, no de la máquina: se suspende antes de buscar el embarazo, con la antelación que dice la ficha de su fármaco, y lo planificamos juntas. Qué anticoncepción hasta entonces y el resto de la consulta preconcepcional es el capítulo 8, y se decide con ella. Y la frase de siempre: nada que permita saber quién es usted entra nunca en esas herramientas. Entró una pregunta general, un principio activo y un titular.

Se va con una fecha aproximada y la lista de lo que no se sabe, corta y honesta. La máquina desenterró en cinco minutos lo que antes era una tarde que no tenía. Leerlo y decírselo bien fue mío. No es falta de voluntad. Es biología, y es un calendario. Las dos cosas se planifican.

---

## En 60 segundos

1. La evidencia no está más lejos: está más enterrada. La máquina desentierra en minutos; decidir qué vale y qué cambia el lunes sigue costando lo mismo, y es tuyo.
2. Cuatro herramientas para cuatro cosas: orientarse, encontrar, leer lo tuyo, verificar. Si la respuesta no trae enlaces, la cita es de memoria.
3. Un ensayo se lee con plantilla y cada cifra lleva página; sin página, no existe.
4. Lo que no se puede concluir de tus datos vale más que lo que se puede; la máquina lo lista si se lo pides.
5. Ninguna referencia entra en un documento tuyo sin que la hayas abierto. Ninguna.

## Hazlo hoy · 10 minutos

1. **(2 min)** Escribe la última duda de consulta que no buscaste y pásala por el caso 1. Solo la pregunta.
2. **(3 min)** Crea una cuenta en My NCBI y guarda esa cadena de búsqueda con alerta mensual.
3. **(4 min)** Pega las referencias de tu última sesión en el caso 7 y comprueba a mano las dos con más señales.
4. **(1 min)** Guarda los dos con la ficha del capítulo 4: v1, fecha, modelo, iniciales.

El próximo estudio del telediario llegará antes que el artículo, como siempre. Ahora el artículo llega a los dos minutos. Los diez siguientes son tuyos, y no hay herramienta que los haga por ti.

---

## Referencias

**Volumen de la literatura y pregunta de búsqueda**

1. Landhuis E. Scientific literature: information overload. Nature. 2016;535(7612):457-8. doi:10.1038/nj7612-457a [VERIFICAR cifra de artículos anuales en PubMed]
2. Richardson WS, Wilson MC, Nishikawa J, Hayward RS. The well-built clinical question: a key to evidence-based decisions. ACP J Club. 1995;123(3):A12-3.
3. Sackett DL, Rosenberg WM, Gray JA, Haynes RB, Richardson WS. Evidence based medicine: what it is and what it isn't. BMJ. 1996;312(7023):71-2. doi:10.1136/bmj.312.7023.71
4. National Library of Medicine. PubMed y My NCBI [Internet]. Bethesda (MD): NLM [consultado el 15 de septiembre de 2026]. Disponible en: https://pubmed.ncbi.nlm.nih.gov y https://account.ncbi.nlm.nih.gov

**Lectura crítica de ensayos**

5. Schulz KF, Altman DG, Moher D; CONSORT Group. CONSORT 2010 statement: updated guidelines for reporting parallel group randomised trials. BMJ. 2010;340:c332. doi:10.1136/bmj.c332
6. CASPe. Programa de Habilidades en Lectura Crítica Español: plantillas de lectura crítica [Internet]. Alicante: CASPe [consultado el 15 de septiembre de 2026]. Disponible en: https://redcaspe.org [VERIFICAR URL vigente y plantilla de ensayo clínico]
7. Wilding JPH, Batterham RL, Calanna S, Davies M, Van Gaal LF, Lingvay I, et al.; STEP 1 Study Group. Once-weekly semaglutide in adults with overweight or obesity. N Engl J Med. 2021;384(11):989-1002. doi:10.1056/NEJMoa2032183. Registro: NCT03548935. [VERIFICAR acceso abierto y cifras del caso 3]
8. Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. Int J Epidemiol. 2005;34(1):215-20. doi:10.1093/ije/dyh299

**Referencias fabricadas por modelos de lenguaje**

9. Bhattacharyya M, Miller VM, Bhattacharyya D, Miller LE. High rates of fabricated and inaccurate references in ChatGPT-generated medical content. Cureus. 2023;15(5):e39238. doi:10.7759/cureus.39238
10. Walters WH, Wilder EI. Fabrication and errors in the bibliographic citations generated by ChatGPT. Sci Rep. 2023;13(1):14045. doi:10.1038/s41598-023-41032-5

**Guías y fuentes primarias**

11. Sociedad Española para el Estudio de la Obesidad (SEEDO). Guía Española GIRO: Guía española del manejo Integral y multidisciplinaR de la Obesidad en personas adultas. 2.ª ed. Lecube A, coordinador. Madrid: SEEDO; noviembre de 2024. Disponible en: https://www.seedo.es/images/site/giro/GUIA-GIRO-2a-edicin_26NOV2024.pdf [VERIFICAR ISBN en créditos; candidato 978-84-09-65969-2; apartado sobre embarazo]
12. Wharton S, Lau DCW, Vallis M, Sharma AM, Biertho L, Campbell-Scherer D, et al. Obesity in adults: a clinical practice guideline. CMAJ. 2020;192(31):E875-E891. doi:10.1503/cmaj.191707
13. National Institute for Health and Care Excellence. Overweight and obesity management. NICE guideline NG246. Londres: NICE; enero de 2025. Disponible en: https://www.nice.org.uk/guidance/ng246 [VERIFICAR número, título y fecha]
14. Agencia Española de Medicamentos y Productos Sanitarios. Centro de Información online de Medicamentos (CIMA) [Internet]. Madrid: AEMPS [consultado el 15 de septiembre de 2026]. Fichas técnicas autorizadas por principio activo, sección 4.6 (fertilidad, embarazo y lactancia). Disponible en: https://cima.aemps.es
