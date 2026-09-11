# Capítulo 2 · Qué es (y qué no es) la IA generativa

**Lo justo para usarla con criterio, sin ingeniería.**

Me ha pasado más de una vez: pedir a un chat que me resuma una guía y recibir un párrafo impecable con una cita al pie. Autores, revista, año, un DOI con muy buena pinta. La busco para la diapositiva. No existe.

No me enfado con la máquina. Me enfado conmigo, por haberme fiado. Y después entiendo que ha hecho justo aquello para lo que está construida: completar la frase. Este capítulo cuenta qué es eso, sin ingeniería, con lo justo para que lo veas venir.

*Como todas las escenas de consulta de este libro, la viñeta final es una composición de varias personas.*

## Lo que te vas a llevar

- Qué hace de verdad un modelo de lenguaje, con una imagen y cinco palabras: token, ventana de contexto, azar, multimodalidad y alucinación.
- Por qué se equivoca con tanta seguridad y la única pregunta que importa antes de cada tarea: cuánto cuesta que se equivoque aquí.
- Cómo distinguir la IA gratuita, la de pago, la de frontera y la local, y seis casos para tocarla con tus manos, ninguno con datos de pacientes.

---

## Primera parte · Una máquina de completar frases

### Lo que hay detrás del chat

Cuando escribes en el móvil "tengo cita con el" y el teclado te propone "médico", hace en pequeño lo mismo que un modelo de lenguaje: apostar por lo que sigue. La diferencia es de tamaño: el modelo ha leído una parte enorme de internet, de los libros y de las revistas (Brown 2020).

La imagen que uso en las sesiones es otra. Imagina un residente de primer año que se ha leído la biblioteca entera. No recuerda de qué libro sacó cada cosa. Nunca ha visto a esta paciente. Y ha aprendido, en miles de exámenes, que dejar una pregunta en blanco puntúa peor que contestar con aplomo. Eso es un modelo de lenguaje: un compañero leidísimo, sin memoria de fuentes, sin acceso a la persona, entrenado para que la frase suene bien.

Y suena bien de verdad: los modelos grandes aprueban preguntas del examen de licencia médica (Singhal 2023), los más recientes con nota (Singhal 2025). Pero aprobar un examen no es pasar consulta. El residente lo sabría. La máquina, no.

Se llama modelo de lenguaje de gran tamaño, LLM por sus siglas en inglés. El motor es una arquitectura publicada en 2017 (Vaswani 2017). Se entrena con una sola tarea: dado un texto, adivinar la pieza que sigue (Brown 2020). Después se pule con miles de conversaciones de ejemplo para que responda como asistente (Ouyang 2022). El pulido cambia el tono. No cambia el motor.

### Cinco palabras, una frase cada una

- **Token.** La pieza mínima que el modelo lee y escribe. No es una palabra: es un trozo. "Adiposidad" puede ser dos o tres. Límites y precios se cuentan en tokens.
- **Ventana de contexto.** La mesa de trabajo: todo lo que el modelo tiene delante a la vez, tu prompt, los archivos, la conversación anterior. Lo que no cabe en la mesa no existe para él.
- **Azar.** La misma pregunta, dos veces, dos respuestas. No es un fallo: elige entre varias piezas probables con una pizca de sorteo. Por eso importa tanto un prompt cerrado. Y por eso la calculadora del capítulo 8 la escribió una máquina que no se repite, pero el programa que salió sí: mismos datos, mismo resultado, siempre.
- **Multimodalidad.** Los modelos actuales leen imágenes, PDF y audio; algunos, vídeo. Para ellos, la foto de un envase es texto. Es la puerta a usos nuevos, y a subir sin querer una imagen con una persona dentro.
- **Alucinación.** Una respuesta plausible y falsa. Merece sección propia.

Y tres cosas que un modelo no hace si nadie se lo activa: no busca en internet, no recuerda tu conversación de ayer y no sabe qué día es. Tiene una fecha de corte de conocimiento y, de lo posterior, nada. Tampoco ve tu historia clínica. Hoy, para ti y para mí, es una ventaja.

### Por qué suena seguro cuando se equivoca

Vuelve al residente que no deja preguntas en blanco. Cuando le pido una referencia, no la busca: la construye. Conoce su forma: apellido, inicial, revista real, año, un DOI que empieza por 10. Cada pieza es probable. El conjunto es falso. Eso es una alucinación: texto con forma de verdad (Ji 2023).

En un estudio de 2023, de 115 referencias que un chat generó para textos médicos, casi la mitad no existía y solo un 7 % era correcta del todo; lo que más fallaba era el PMID (Bhattacharyya 2023). Con la versión siguiente del mismo modelo, las inventadas bajaron de más de la mitad a menos de un quinto; bajaron, no desaparecieron (Walters 2023). Y un trabajo de 2025, aún sin revisión por pares, dio el porqué con una imagen de examen: si contestar mal no resta y dejar en blanco no suma, el alumno aprende a contestar siempre (Kalai 2025). A la máquina la hemos educado así.

Por eso la pregunta "¿se equivoca?" no sirve: sí, siempre puede. La útil es otra: **¿cuánto cuesta que se equivoque en esta tarea?**

- **Coste bajo.** Un borrador que vas a leer entero y corregir: las frases del capítulo 1, el guion de una sesión. Si falla, pierdes dos minutos.
- **Coste medio.** Algo que puede llegar a otra persona sin que lo notes: un resumen que reenvías. Una hoja para pacientes roza el coste alto: se fotocopia y se reparte durante meses. Por eso lleva tu firma y el disclaimer, y la lees entera antes.
- **Coste alto.** Una dosis, una interacción, un diagnóstico, una cita en un informe, un dato de una persona. Si falla, daña. Aquí la respuesta puede ser no, o no con esta herramienta.

A más coste, más comprobación, mejor herramienta y menos prisa. La comprobación es doble: antes de pegar, para que no entre nada que no deba; después de leer, para que no salga nada falso. Ninguna de las dos la hace la máquina por ti.

### La mesa es grande, pero se lee mal por el medio

Las ventanas de contexto ya admiten libros enteros, cuando escribo esto. Pero caber no es leer. Un estudio de 2024 lo midió: si la información está al principio o al final de un texto largo, el modelo la encuentra; a mitad, la pierde con frecuencia (Liu 2024). Y en algunas herramientas un PDF largo ni se lee: se busca por fragmentos. El efecto es el mismo: el dato enterrado no sale.

Tres gestos lo mitigan: pon lo importante al principio o al final del prompt; dirige la atención ("mira solo el apartado de diagnóstico"); pide la cita literal con la página. El caso 3 lo hace paso a paso.

### Y trae los sesgos de lo que ha leído

Se ha entrenado con internet. E internet está lleno de "comer menos y moverse más", de chistes sobre el peso y de dietas milagro. Si no le dices lo contrario, el modelo devuelve el tono medio de lo que leyó, y el tono medio es el estigma. Se ha demostrado con la medicina basada en la raza: varios modelos repetían mitos ya desmentidos (Omiye 2023). Con el peso no tengo un estudio que citar; he visto pedir diez consejos y recibir la fórmula de siempre.

Por eso los prompts de este libro llevan restricciones tan largas. No es manía: el valor por defecto de la máquina no es el nuestro.

## Segunda parte · No todo lo que se llama IA es lo mismo

### "Lo dijo la IA" es como "lo dijo el médico"

¿Qué médico? ¿Cuándo? ¿Con qué datos delante? Decir "la IA" es como decir "el aparato": el tensiómetro de la farmacia y el Holter miden los dos, y no sirven para lo mismo. Hoy conviven, como mínimo, cuatro niveles; los nombres cambian cada pocos meses.

- **Gratuita.** La versión sin pagar de Gemini, ChatGPT, Claude o similares. Sirve para aprender y para casi todo lo del capítulo 1. Sus límites: un modelo menos capaz o más antiguo, que con mucho tráfico se cambia por otro más ligero sin que lo notes; menos mensajes, menos contexto, pocos archivos. Y la casilla de entrenamiento con tus datos viene activada en las tres, cuando escribo esto.
- **De pago.** Entre veinte y veinticinco euros al mes, cuando escribo esto. El mejor modelo de ese proveedor, más contexto, archivos, ejecución de código, búsqueda en profundidad. Sigue siendo una herramienta de consumo: sin acuerdo de tratamiento de datos y con las mismas reglas de privacidad que la gratuita.
- **Frontera.** El modelo más capaz que existe en cada momento, sea de quien sea; a veces solo en los planes caros. Para tareas con coste de error alto y datos públicos: comparar dos guías, revisar un texto tuyo, escribir el código de una calculadora.
- **Local.** Modelos abiertos que corren en tu propio ordenador; nada sale de él. Exigen equipo y manos, y rinden por debajo: para Atención Primaria es un escenario futuro. Y correr en tu ordenador no es cumplir la normativa; el ordenador del centro tiene sus reglas.

Hay una quinta categoría que yo no tengo: la herramienta con acuerdo de tratamiento de datos que te dé tu servicio de salud. Si la tienes, lee qué cubre. Si no, estás donde yo, y todo este libro funciona desde ahí. Ninguna de las que nombro se comercializa como producto sanitario [VERIFICAR], y hay quien reclama una regulación específica para estos modelos en salud (Meskó 2023). El marco legal, sin miedo, va en el capítulo 3.

### Chat o razonador

Dentro de cada proveedor hay, además, dos maneras de responder. El **modo chat** contesta al momento: rápido, barato, suficiente para borradores y trámites. El **modelo de razonamiento**, razonador para abreviar, se para antes de escribir: descompone la pregunta, se corrige y tarda de veinte segundos a varios minutos. Nació de un hallazgo sencillo: si obligas al modelo a escribir los pasos intermedios, acierta más (Wei 2022). Los razonadores lo hacen de fábrica. Si tu plan no lo trae, hay un remedio casero: pedirle los pasos por escrito. Lo enseño en el caso 5.

Cuál usar lo decide el coste de error, no la novedad. Reescribir una frase: chat. Un caso sintético con fricción, una comparativa entre guías, un código: razonador. Y una advertencia: razonar más no es verificar. Un razonador puede llegar con más pasos a una conclusión falsa, y la escribe igual de bien.

### Seis preguntas antes de pegar nada

Antes de cada tarea, seis preguntas. Caben en un post-it.

- **¿Qué modelo y qué versión?** Mira el nombre en el desplegable, no lo que la máquina dice ser. Anótalo cuando algo te funcione: en tres meses no será el mismo.
- **¿Qué plan?** Gratuito o de pago cambia el modelo, el contexto y las herramientas.
- **¿Cuánto cabe en la mesa?** Un PDF de doscientas páginas puede no caber. O caber y leerse mal por el medio.
- **¿Qué herramientas tiene activas?** Búsqueda, archivos, código, memoria. Sin búsqueda no hay citas fiables ni nada posterior a su fecha de corte.
- **¿Tiene acuerdo de tratamiento de datos?** Si no lo sabes, no lo tiene.
- **¿Cuánto cuesta que se equivoque?** Y, por tanto, cuánto vas a comprobar.

La clasificación en niveles y esta lista las aprendí en mi formación en IA y las he hecho mías, con una pregunta más, la quinta, que allí no hacía falta y aquí es la primera. Y con cualquier herramienta de consumo, los tres gestos de higiene del capítulo 1: entrenamiento desactivado, borrar al terminar (también la biblioteca de archivos), versión vigente comprobada. No los repito en cada caso: dalos por puestos.

---

## Seis casos para tocar la máquina

Cada caso trae situación, prompt literal (rol · contexto · tarea · formato · restricciones), ejemplo abreviado de salida, qué revisar y riesgo. Sustituye lo que va entre corchetes; ninguno admite datos de pacientes. Los casos 1, 2, 4 y 5 se pegan igual en Gemini, ChatGPT y Claude, con dos matices. En el 1 y el 2, "sin buscar en internet" solo se garantiza donde puedas apagar la búsqueda. En el 5, el razonador depende del plan. El 3 necesita un plan que admita archivos; el 6 no usa IA. Las cifras de los ejemplos son inventadas.

### Caso 1 · La misma pregunta en tres modelos

**Momento:** docencia. **Herramienta:** Gemini, ChatGPT y Claude en tres pestañas, con la búsqueda en internet apagada donde se pueda.

**Situación.** Quieres enseñar al equipo, en cinco minutos, que "la IA" no es una cosa. Lo más rápido: el mismo prompt en las tres, en conversaciones nuevas.

```
ROL: Eres médica de familia con formación en obesidad como enfermedad crónica.

CONTEXTO: Respondo a una pregunta clínica general para una sesión docente de Atención Primaria. No hay ningún paciente detrás: no incluyas ni pidas datos de personas. Es un ejercicio de comparación entre modelos: responde solo con lo que sabes, sin buscar en internet.

TAREA: Responde a esta pregunta: "[pregunta general, por ejemplo: ¿Qué cambios hormonales explican que se recupere el peso después de una dieta?]".

FORMATO, en este orden:
(1) Un párrafo de unas 150 palabras.
(2) Una tabla con cada afirmación del párrafo, una por fila, en tres columnas: afirmación; certeza; fuente. Certeza con uno de estos valores: ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, con explicaciones o estudios discrepantes), BAJA (plausible, no lo afirmaría sin comprobarlo). Fuente: primer autor y año de un estudio real que conozcas con seguridad; si no, escribe SIN FUENTE. No inventes ninguna.
(3) Dos líneas finales, fuera del rol de médica: "Modelo: [nombre y versión que crees ser, o NO DISPONIBLE] · Fecha de corte de conocimiento: [fecha o NO DISPONIBLE]" y "He buscado en internet para responder: SÍ / NO".

RESTRICCIONES: Sin nombres comerciales de medicamentos. Usa siempre "persona con obesidad". Sin cifras ni porcentajes salvo que vayan acompañados de fuente en la tabla.
```

**Ejemplo abreviado de salida (una de las tres).**

> Tras una pérdida de peso, la leptina desciende y la grelina también se reduce, con lo que el apetito se normaliza […].
> | La leptina baja tras perder peso | ALTA | Sumithran 2011 | · | La grelina baja tras perder peso | ALTA | SIN FUENTE | · | El GLP-1 baja | MEDIA | SIN FUENTE |
> Modelo: [nombre] · Fecha de corte: [mes y año] · He buscado en internet: NO

**Qué revisar antes de usarla.** Cuenta los SIN FUENTE de cada modelo y comprueba en PubMed las fuentes que sí da. Mira qué se contradice entre los tres. En el ejemplo, una dice que la grelina baja, con etiqueta ALTA; el capítulo 1 explica que sube, y ahí la literatura es unánime. Esa contradicción es la sesión.

Con el GLP-1 la literatura no se pone de acuerdo: Sumithran 2011 no lo encontró cambiado; Iepsen 2016 lo encontró aumentado. Un modelo que marque MEDIA ahí está bien calibrado.¹ La certeza se contrasta con la literatura, no con la de otro modelo. Después compara la línea "Modelo:" con el desplegable: a menudo no coinciden. Y si la respuesta trae enlaces, ha buscado, diga lo que diga.

**Riesgo principal y mitigación.** Que el equipo elija "la mejor" respuesta por cómo suena. Mitigación: la tabla muestra variabilidad, no se vota; la verdad se comprueba en la fuente.

¹ Declaración de transparencia: mantengo vínculos con Novo Nordisk, detallados al inicio del libro. En este capítulo el GLP-1 se nombra como hormona y no se nombra ningún fármaco; el tratamiento farmacológico de la obesidad se aborda en el capítulo 8.

### Caso 2 · Cazar una alucinación

**Momento:** docencia. **Herramienta:** cualquier asistente, primero sin búsqueda; después, PubMed.

**Situación.** Es el ejercicio que más me ha enseñado. Pides cinco referencias sobre adaptación metabólica y compruebas cuántas existen. Diez minutos que cambian cómo miras una cita. Como el tema es clásico y los modelos lo tienen bien aprendido, el prompt los empuja fuera del canon: a lo reciente y al español. Ahí flaquean.

```
ROL: Eres una documentalista científica que trabaja con revistas biomédicas indexadas.

CONTEXTO: Preparo una lista de lectura sobre adaptación metabólica tras la pérdida de peso en personas adultas. Es un ejercicio de formación; no hay pacientes ni datos de personas. Responde solo con lo que recuerdas: no busques en internet.

TAREA: Dame cinco referencias de artículos originales o revisiones sobre adaptación metabólica tras la pérdida de peso. Al menos dos publicadas a partir de 2021 y al menos una en una revista en español.

FORMATO: Tabla con siete columnas: primer autor; año; revista; título completo; DOI; PMID; CERTEZA. CERTEZA toma uno de estos valores: SEGURA (recuerdas autores, título, revista y año con detalle), PROBABLE (recuerdas autores y tema, no los datos exactos), DUDOSA (podría no existir tal como la escribes). Ordena de mayor a menor certeza. Si no llegas a cinco con certeza SEGURA o PROBABLE, deja las filas restantes vacías y escribe debajo "LISTA INCOMPLETA". Última línea: "He buscado en internet: SÍ / NO".

RESTRICCIONES: No inventes DOI ni PMID: si no los recuerdas, escribe DESCONOCIDO en esa casilla. No combines datos de dos artículos en una misma fila. No busques en internet en este ejercicio. No incluyas datos de personas.
```

**Si la respuesta trae enlaces, ha buscado.** Cuando escribo esto, Claude deja apagar la búsqueda; ChatGPT decide por su cuenta y Gemini busca casi siempre. Entonces las cinco pueden ser reales y el ejercicio no enseña nada: repite en otra herramienta o añade al principio "Contesta solo de memoria; si necesitas buscar, marca DUDOSA".

**Ejemplo abreviado de salida.**

> | Fothergill | 2016 | Obesity | Persistent metabolic adaptation 6 years after… | 10.1002/oby.21538 | DESCONOCIDO | SEGURA | **Tu comprobación:** EXISTE Y COINCIDE |
> | Martínez | 2022 | Nutr Hosp | Adaptación metabólica tras pérdida ponderal… | 10.20960/[inventado] | [PMID inventado] | PROBABLE | **Tu comprobación:** NO EXISTE |
> He buscado en internet: NO

La última columna la añades tú: EXISTE Y COINCIDE / EXISTE CON ERRORES / EXISTE PERO TRATA DE OTRA COSA / NO EXISTE. La segunda fila es falsa a propósito: revista real, autor plausible, año reciente. Así se disfrazan. No la "corrijas".

**Qué revisar antes de usarla.** Todo: el ejercicio es la revisión. Cada fila en PubMed por título y primer autor; cada DOI en el navegador. Pocas veces he visto salir las cinco limpias, ni con la etiqueta SEGURA. Repite con la búsqueda activada: mejora mucho, no desaparece.

**Riesgo principal y mitigación.** Confiar en un DOI porque tiene forma de DOI. Mitigación: ninguna referencia entra en un documento tuyo sin que la hayas abierto. Ninguna.

### Caso 3 · Lo que se pierde en medio

**Momento:** consulta (preparación) y docencia. **Herramienta:** asistente que admita archivos y devuelva la página de cada cita. Los generales lo hacen si se lo pides; las pensadas para leer documentos (NotebookLM, cuando escribo esto), por diseño.

**Situación.** Quieres un dato concreto de una guía larga y pública, por ejemplo la GIRO de la SEEDO (2024), y no recuerdas en qué página está. Adjunta el PDF antes del prompt (en NotebookLM, como fuente). Solo documentos públicos, de su web oficial, para uso personal. Dos turnos: primero te dice cuántas páginas ve y busca; después diriges la atención.

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

**Según la herramienta**, cuando escribo esto. En NotebookLM no hay páginas: cambia "página" por "número de cita" y abre cada cita con un clic. En ChatGPT y Gemini un PDF largo se busca por fragmentos: NO ENCONTRADO a veces significa "mal buscado", y el segundo turno lo arregla. Claude lee el documento entero si cabe y avisa si no cabe; los otros dos no avisan: mira la línea (0). En planes gratuitos, sube solo el capítulo que necesitas.

**Ejemplo abreviado de salida.**

> Turno 1: Documento: Guía GIRO 2.ª ed. · Páginas que veo: [número]. NO ENCONTRADO EN EL DOCUMENTO. No aparece en el texto que he leído.
> Turno 2: ENCONTRADO EN EL DOCUMENTO. "[cita literal]". Frase anterior: "[frase que la precede]". Página 31 del PDF (impresa: 27), apartado 4.2 [VERIFICAR página y apartado en la 2.ª ed. de GIRO].

**Qué revisar antes de usarla.** Abre el PDF por la página que dice; si da dos números, prueba los dos. La frase está o no está, tal cual. Este orden ya no permite lo que he visto más de una vez: una cifra recitada de memoria con un "no encontrado" debajo. Y el porqué clínico del ejemplo: en España conviven dos juegos de puntos de corte de cintura, 102/88 y 94/80 centímetros. Cuál usa la guía, y en qué página, es lo que la máquina, de memoria, no puede darte.

**Riesgo principal y mitigación.** Que el modelo "recuerde" en vez de leer. Mitigación: etiqueta antes que cita, frase previa, dos números de página y tus ojos en el PDF.

### Caso 4 · Clasificar mis tareas: papel, gratuita, de pago o nada [AP]

**Momento:** administración. **Herramienta:** papel, o cualquier asistente.

**Situación.** Tienes la lista de tareas del capítulo 1 o, si no la hiciste, diez tareas de una jornada cualquiera. Quieres saber, tarea por tarea, qué nivel de herramienta, qué comprobación y qué datos. Se puede hacer con lápiz; el prompt solo lo ordena. Antes de pegar, la regla del capítulo 1: tareas, no personas. Si el modelo devuelve algo en REVISAR PRIVACIDAD, esa línea ya ha entrado: borra la conversación.

```
ROL: Eres una consultora que ayuda a médicas de familia a decidir cuándo y cómo usar IA generativa con seguridad.

CONTEXTO: Te pego diez tareas de una jornada de Atención Primaria, descritas de forma genérica y sin datos de personas; ya lo he revisado. Trabajo solo con herramientas de consumo, sin acuerdo de tratamiento de datos. Los niveles posibles son cinco: PAPEL (mejor sin IA); GRATUITA; DE PAGO; DE PAGO CON RAZONADOR O MODELO DE FRONTERA; SOLO CON CONTRATO (necesita datos clínicos reales y hoy no la hago con IA).

TAREA: Para cada tarea indica: (a) coste de error si la IA se equivoca: BAJO (lo leo entero y lo corrijo), MEDIO (podría llegar a otra persona sin que yo lo note), ALTO (afecta a una decisión clínica, a un dato de paciente o a un documento oficial); (b) datos de pacientes que necesita: NINGUNO / SOLO RECUENTOS AGREGADOS / DATOS REALES; (c) nivel de herramienta, aplicando esta regla en este orden y parando en la primera que se cumpla: si (b) es DATOS REALES → SOLO CON CONTRATO; si la tarea exige mi presencia o una decisión clínica → PAPEL; si (a) es ALTO → DE PAGO CON RAZONADOR O MODELO DE FRONTERA; si (a) es MEDIO → DE PAGO; si (a) es BAJO → GRATUITA; (d) la comprobación humana que haría antes de usar la salida, en una línea. Si una tarea no está clara o admite dos lecturas, clasifícala como POR ACLARAR en las cuatro columnas y escribe la pregunta que me harías.

FORMATO: Tabla con la tarea y las cuatro columnas (a-d). Debajo, tres listas: tareas que hoy no debo hacer con IA y por qué; tareas donde una herramienta gratuita basta; preguntas de las tareas POR ACLARAR.

RESTRICCIONES: No inventes tareas ni cambies mis descripciones. No propongas automatizar decisiones clínicas. No rebajes el nivel que sale de la regla aunque la tarea parezca sencilla. Como comprobación adicional a la mía, si una línea contiene algo que parezca identificar a una persona (nombre, dirección, parentesco con detalles, fecha), no la clasifiques: ponla en una lista "REVISAR PRIVACIDAD" y dime por qué.

TAREAS:
[una por línea, por ejemplo: resumir una guía pública para la sesión del jueves; redactar una hoja informativa sobre etiquetas; contestar una reclamación; preparar una plantilla de interconsulta con un caso sintético; …]
```

**Ejemplo abreviado de salida.**

> | Resumir guía pública para sesión | MEDIO | NINGUNO | DE PAGO | Abrir cada cita en el PDF |
> | Contestar una reclamación | POR ACLARAR | ¿Plantilla genérica o reclamación concreta con datos? |
> | Interconsulta de una paciente concreta | ALTO | DATOS REALES | SOLO CON CONTRATO | Hoy no |

**Qué revisar antes de usarla.** Cada fila, con la regla y no con el modelo: si (b) dice DATOS REALES y (c) no dice SOLO CON CONTRATO, la fila está mal. La tabla la firmas tú; si el modelo puso GRATUITA donde dudabas, gana la duda. "SOLO CON CONTRATO" significa "hoy no", no "búscate la manera". La plantilla de interconsulta se escribe en el capítulo 5, con caso sintético; los datos de la persona los pones tú, fuera de la IA.

**Riesgo principal y mitigación.** Que la tabla funcione como permiso. Mitigación: ante la duda, un nivel más alto o papel; y revisarla cuando cambie la herramienta o tu plan.

### Caso 5 · Chat frente a razonador

**Momento:** docencia (entrenar el criterio). **Herramienta:** el mismo asistente en modo chat y con el razonador.

**Situación.** Un caso inventado de cero: no una paciente real con dos datos cambiados, que sigue siendo ella. Hazlo como un arquetipo compuesto: mezcla rasgos de varias personas, cambia la edad, el orden y el número de las cosas, y escríbelo con la historia clínica cerrada. Si te viene una cara, cambia el caso. Pega el prompt en dos conversaciones nuevas: una en modo chat, otra con el razonador. Cronometra. Es un ejercicio de razonamiento, no una consulta. La estructura, separar lo que hay de lo que deduzco y de lo que falta, la aprendí en mi formación en IA; el caso y las listas son míos.

```
ROL: Eres médica de familia con experiencia en obesidad. Esto es un ejercicio de razonamiento sobre un caso inventado; no es una consulta real y no debes tomar ni proponer decisiones para ninguna persona concreta.

CONTEXTO: Caso sintético, compuesto por mí a partir de rasgos de varias personas y sin corresponder a ninguna real: [descripción inventada, por ejemplo: mujer de unos cincuenta años, obesidad de grado II, hipertensión tratada con un fármaco, dos glucemias en ayunas en rango de prediabetes, ronquidos con somnolencia diurna, cansancio y ánimo bajo desde hace meses, cuatro intentos previos de bajar de peso con recuperación, un antidepresivo desde hace un año]. No hay más datos.

TAREA: No cierres ningún diagnóstico. Escribe cuatro listas: (1) lo que está en el caso, hecho por hecho, numerados; (2) lo que deduces, indicando entre paréntesis el número del hecho o hechos de la lista 1 de los que sale cada deducción, y la certeza: ALTA (lo sostendría cualquier manual o guía), MEDIA (compatible, con explicaciones o estudios discrepantes), BAJA (plausible, no lo afirmaría sin comprobarlo); (3) lo que falta y cambiaría el razonamiento, ordenado por importancia; (4) qué preguntaría y qué exploraría una médica de familia en la siguiente visita, sin proponer tratamientos. Si hay ánimo bajo, incluye las preguntas de seguridad.

FORMATO: Cuatro listas numeradas, máximo siete puntos cada una. Al final, una línea con los atajos de razonamiento que has vigilado en tu propia respuesta (por ejemplo: quedarte con la primera explicación, atribuirlo todo al peso, dar por hecho lo que el caso no dice).

RESTRICCIONES: Sin nombres comerciales ni propuestas de fármacos. Sin diagnósticos cerrados. No añadas datos al caso: si los necesitas, van en la lista 3. No me hagas preguntas: si algo es ambiguo, di cómo lo has interpretado en la lista 1. Usa "persona con obesidad".
```

**Dónde está el razonador.** Busca en el desplegable algo como "Thinking", "razonamiento" o "pensar más". Si tu plan no lo tiene, o la herramienta decide sola cuándo razonar, haz la segunda pasada con esta primera línea añadida: "Antes de responder, escribe tu razonamiento paso a paso; solo después escribe las cuatro listas". No es lo mismo, pero basta para ver la diferencia.

**Ejemplo abreviado de salida.**

> Modo chat (unos diez segundos): cinco deducciones, tres en ALTA; "sospecha de apnea del sueño (hechos 2, 3 y 5): ALTA". Lista 3: analítica, cuestionario de sueño.
> Razonador (de 20 segundos a 2 minutos): la misma sospecha de apnea, en ALTA. Cambia la lista 3: cuál es el antidepresivo; función tiroidea; atracones nocturnos; y, por el ánimo bajo de meses, ideas de muerte.

**Qué revisar antes de usarla.** Las certezas: ¿qué marcó ALTA que tú pondrías en MEDIA? Y al revés: más cauto no es más correcto. Con ronquidos, somnolencia, grado II e hipertensión, la sospecha de apnea es alta, y así debe quedar.

Las ausencias: ¿nombró las cinco cosas que el capítulo 1 pide mirar antes de atribuirlo todo a la biología? ¿Preguntó por ideas de muerte? Casi ningún modelo lo hace si no se lo pides. Tú sí. ¿Preguntó cuál antidepresivo? No todos engordan igual, y cambiarlo es decisión tuya. Y el tiempo: el razonador tardó varias veces más para un caso que tú ordenas en la cabeza en treinta segundos. Ordenar no es resolver: este caso son tres visitas.

**Riesgo principal y mitigación.** Que el ejercicio te tiente a pegar un caso real. Mitigación: solo casos compuestos, con la historia clínica cerrada; si la "invención" se parece a alguien, no es una invención. La derivación y el tratamiento van en el capítulo 8, no en un chat.

### Caso 6 · Inventario de lo que tengo [AP]

**Momento:** administración. **Herramienta:** ninguna. Una hoja.

**Situación.** Quieres saber con qué trabajas de verdad: herramientas, cuenta, qué tienen activado y qué no puede entrar. Es el único caso sin prompt: una ficha, a mano.

```
INVENTARIO DE HERRAMIENTAS · [fecha]

Herramienta: [Gemini / ChatGPT / Claude / NotebookLM / Perplexity / otra]
Modelo que aparece en el desplegable: [nombre y versión]
Cuenta: [personal / de organización]     Plan: [gratuito / de pago]
Acuerdo de tratamiento de datos con mi servicio de salud: [no / sí: contrato visto por mí el (fecha)]
Entrenamiento con mis conversaciones: [desactivado / activado / no lo sé]
Memoria entre conversaciones: [desactivada / activada / no lo sé]
Archivos que subo: [se borran con la conversación / quedan en una biblioteca aparte / no lo sé]
Herramientas activas: [búsqueda en internet / archivos / imágenes / código / memoria / ninguna]
Lo que entra: [textos propios, documentos públicos, casos inventados, recuentos agregados]
Lo que no entra: [ningún dato de paciente, ninguna imagen con personas, ningún documento interno del centro]
Herramientas con contrato que me ofrece mi centro o mi servicio de salud: [ninguna / nombre y qué cubre]
Próxima revisión de esta ficha: [dentro de tres meses]
```

**Ejemplo abreviado de salida (ficha rellenada).**

> Gemini, cuenta personal, plan gratuito. Acuerdo de datos: no. Entrenamiento: no lo sé. Memoria: no lo sé. Archivos: no lo sé. Del centro: ninguna.

**Qué revisar antes de usarla.** Cada "no lo sé" es una tarea: el entrenamiento y la memoria se desactivan en la configuración de la cuenta; el modelo está en el desplegable. Memoria activada significa que lo que pegues hoy puede reaparecer dentro de un mes, aunque borres la conversación. Con casos inventados no pasa nada; con un dato pegado por error, sí. Pregunta a tu centro, o a su delegado de protección de datos, si existe alguna herramienta con contrato: a veces la hay y nadie lo ha contado.

**Riesgo principal y mitigación.** Creer que "gratuita" es "privada", o que "de organización" es "con contrato". Mitigación: la ficha a la vista, junto al post-it de las seis preguntas, y revisarla cada tres meses. Las políticas cambian más deprisa que las guías.

---

## Caso ilustrativo, no real: arquetipo compuesto

> Esta viñeta combina rasgos de varias personas que han llegado a mi consulta con la respuesta de un chat. Se han modificado la edad, el motivo de la analítica, la herramienta y las cifras; no hay fechas ni lugares. Ninguna persona real coincide con esta descripción.

Tiene entre cuarenta y cincuenta años, obesidad de grado II y una analítica reciente que pidió por su cuenta. Entra con un folio doblado en cuatro y lo pone sobre la mesa antes de sentarse. "Me dice que tengo resistencia a la insulina y que necesito tal medicación."¹

"¿Quién se lo dice?" "La IA." Y ahí está mi pregunta de siempre: ¿cuál? Me cuenta que pegó su analítica en un chat gratuito, con su nombre y todo, y que le contestó "mejor que muchos médicos". Leo el folio. Es amable, ordenado y suena a que sabe. No me sorprende: en un estudio con preguntas de un foro público, no de consultas, otros sanitarios prefirieron las respuestas del chat a las de médicos voluntarios y las encontraron más empáticas (Ayers 2023). Amable no es lo mismo que correcta.

Le pregunto si ya la ha comprado o la está tomando. No. Bien: si un día lo hace, será con receta, con indicación y con alguien que le siga. Eso es el capítulo 8.

Y "resistencia a la insulina" no es un diagnóstico que hagamos con una cifra, ni una razón para un fármaco. La máquina completó la frase más probable. Lo que miro es lo de siempre: azúcar y hemoglobina glicosilada, lípidos, hígado, riñón y tensión. Le pregunto si ronca. Y lo que la máquina no sabe es lo que él no le contó: diabetes en la familia, poco sueño, un par de años sin fumar y bastante peso ganado. El chat no lo conoce. Yo, en seis minutos y una cita más, sí.

Se lo explico con la imagen de este capítulo: la máquina no consultó nada; construyó la frase que mejor sonaba con lo que le dio. Le digo lo que hizo bien: mirar, preguntar, venir. Y lo que quiero que no vuelva a hacer, sin regañar: pegar su nombre y sus datos en una herramienta que nadie ha contratado para guardarlos. Hoy, el folio, la cintura y la analítica que falta; anoto obesidad como problema activo. La explicación larga, en la siguiente.

Se va con el folio en el bolsillo y con una cita. Quizá vuelva a preguntarle al chat. Pero ahora sabe quién le contesta: un compañero leidísimo que nunca lo ha visto. La máquina no sabe que no sabe. Él, desde hoy, sí.

---

## En 60 segundos

1. Un modelo de lenguaje apuesta por la siguiente pieza de texto: por eso suena seguro aunque se equivoque.
2. La alucinación no es un fallo raro, es su forma de trabajar; la pregunta útil es cuánto cuesta que se equivoque aquí.
3. La mesa es grande, pero se lee mal por el medio: dirige la atención y pide la cita con página.
4. "La IA" no existe: hay gratuita, de pago, frontera y local, y modo chat o razonador; anota modelo, versión y plan, mirando el desplegable, no la respuesta.
5. Sin acuerdo de tratamiento de datos solo entran textos propios, documentos públicos, casos inventados y recuentos; lo que sale lo compruebas tú.

## Hazlo hoy · 10 minutos

Te propongo cuatro pasos:

1. **(1 min)** Abre tu asistente y mira el nombre del modelo en el desplegable. Apúntalo. Si no lo encuentras, ya has aprendido algo.
2. **(3 min)** Pega el prompt del caso 2: cinco referencias sobre adaptación metabólica.
3. **(5 min)** Busca las cinco en PubMed. Cuenta cuántas existen, cuántas están mal y cuántas no aparecen. Si la respuesta traía enlaces, apúntalo: ha buscado.
4. **(1 min)** En la configuración de la cuenta, desactiva el entrenamiento con tus conversaciones y la memoria. Borra la conversación.

Mañana alguien te traerá un folio doblado en cuatro. Tendrás siete minutos. La máquina no sabe que no sabe. Tú sí. Esa es toda la diferencia, y es tuya.

---

## Referencias

1. Brown TB, Mann B, Ryder N, Subbiah M, Kaplan J, Dhariwal P, et al. Language models are few-shot learners. En: Advances in Neural Information Processing Systems 33 (NeurIPS 2020); 2020. p. 1877-901. arXiv:2005.14165.
2. Singhal K, Azizi S, Tu T, Mahdavi SS, Wei J, Chung HW, et al. Large language models encode clinical knowledge. Nature. 2023;620(7972):172-80. doi:10.1038/s41586-023-06291-2
3. Singhal K, Tu T, Gottweis J, Sayres R, Wulczyn E, Amin M, et al. Toward expert-level medical question answering with large language models. Nat Med. 2025;31(3):943-50. doi:10.1038/s41591-024-03423-7
4. Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, et al. Attention is all you need. En: Advances in Neural Information Processing Systems 30 (NIPS 2017); Long Beach (CA); 2017. p. 5998-6008. arXiv:1706.03762. Disponible en: https://arxiv.org/abs/1706.03762
5. Ouyang L, Wu J, Jiang X, Almeida D, Wainwright CL, Mishkin P, et al. Training language models to follow instructions with human feedback. En: Advances in Neural Information Processing Systems 35 (NeurIPS 2022); New Orleans (LA); 2022. p. 27730-44. arXiv:2203.02155.
6. Ji Z, Lee N, Frieske R, Yu T, Su D, Xu Y, et al. Survey of hallucination in natural language generation. ACM Comput Surv. 2023;55(12):Article 248. doi:10.1145/3571730
7. Bhattacharyya M, Miller VM, Bhattacharyya D, Miller LE. High rates of fabricated and inaccurate references in ChatGPT-generated medical content. Cureus. 2023;15(5):e39238. doi:10.7759/cureus.39238
8. Walters WH, Wilder EI. Fabrication and errors in the bibliographic citations generated by ChatGPT. Sci Rep. 2023;13(1):14045. doi:10.1038/s41598-023-41032-5
9. Kalai AT, Nachum O, Vempala SS, Zhang E. Why language models hallucinate [preprint]. arXiv; 4 de septiembre de 2025 [consultado el 11 de septiembre de 2026]. arXiv:2509.04664. Disponible en: https://arxiv.org/abs/2509.04664
10. Liu NF, Lin K, Hewitt J, Paranjape A, Bevilacqua M, Petroni F, et al. Lost in the middle: how language models use long contexts. Trans Assoc Comput Linguist. 2024;12:157-73. doi:10.1162/tacl_a_00638
11. Omiye JA, Lester JC, Spichak S, Rotemberg V, Daneshjou R. Large language models propagate race-based medicine. NPJ Digit Med. 2023;6(1):195. doi:10.1038/s41746-023-00939-z
12. Meskó B, Topol EJ. The imperative for regulatory oversight of large language models (or generative AI) in healthcare. NPJ Digit Med. 2023;6(1):120. doi:10.1038/s41746-023-00873-0
13. Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, et al. Chain-of-thought prompting elicits reasoning in large language models. En: Advances in Neural Information Processing Systems 35 (NeurIPS 2022); New Orleans (LA); 2022. p. 24824-37. arXiv:2201.11903.
14. Sumithran P, Prendergast LA, Delbridge E, Purcell K, Shulkes A, Kriketos A, et al. Long-term persistence of hormonal adaptations to weight loss. N Engl J Med. 2011;365(17):1597-604. doi:10.1056/NEJMoa1105816
15. Iepsen EW, Lundgren J, Holst JJ, Madsbad S, Torekov SS. Successful weight loss maintenance includes long-term increased meal responses of GLP-1 and PYY3-36. Eur J Endocrinol. 2016;174(6):775-84. doi:10.1530/EJE-15-1116
16. Fothergill E, Guo J, Howard L, Kerns JC, Knuth ND, Brychta R, et al. Persistent metabolic adaptation 6 years after "The Biggest Loser" competition. Obesity (Silver Spring). 2016;24(8):1612-9. doi:10.1002/oby.21538
17. Sociedad Española para el Estudio de la Obesidad (SEEDO). Guía Española GIRO: Guía española del manejo Integral y multidisciplinaR de la Obesidad en personas adultas. 2.ª ed. Lecube A, coordinador. Madrid: SEEDO; noviembre de 2024. Disponible en: https://www.seedo.es/images/site/giro/GUIA-GIRO-2a-edicin_26NOV2024.pdf [VERIFICAR ISBN en créditos]
18. Ayers JW, Poliak A, Dredze M, Leas EC, Zhu Z, Kelley JB, et al. Comparing physician and artificial intelligence chatbot responses to patient questions posted to a public social media forum. JAMA Intern Med. 2023;183(6):589-96. doi:10.1001/jamainternmed.2023.1838
