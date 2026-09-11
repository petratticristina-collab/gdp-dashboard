# Capítulo 2 · Qué es (y qué no es) la IA generativa

**Lo justo para usarla con criterio, sin ingeniería.**

Son las tres y cuarto. La última paciente se ha ido hace veinte minutos, la sesión del jueves es mía y tengo en pantalla una guía de sesenta páginas que no me va a dar tiempo a leer. La primera vez que le pedí a un chat que me resumiera una guía, me devolvió un párrafo impecable con una cita que no existía. Ahí empezó todo.

La cita tenía autores, revista, año y un DOI con muy buena pinta. La busqué para ponerla en la diapositiva. No estaba en PubMed. No estaba en la revista. No estaba en ningún sitio. Tardé más en convencerme de que no existía que en escribir el prompt.

No me enfadé con la máquina. Me enfadé conmigo, por haberme fiado. Y después entendí que había hecho justo aquello para lo que está construida. Este capítulo cuenta qué es eso, sin ingeniería y con lo justo para que no te pase a ti. O para que, cuando te pase, lo veas venir.

*Como todas las escenas de consulta de este libro, la viñeta final es una composición de varias personas.*

## Lo que te vas a llevar

- Qué hace de verdad un modelo de lenguaje, con una imagen y cinco palabras: token, ventana de contexto, azar, multimodalidad y alucinación.
- Por qué se equivoca con tanta seguridad y la única pregunta que importa antes de cada tarea: cuánto cuesta que se equivoque aquí.
- Cómo distinguir la IA gratuita, la de pago, la de frontera y la local, y siete casos para comprobarlo con tus manos, ninguno con datos de pacientes.

---

## Primera parte · Una máquina de completar frases

### Lo que hay detrás del chat

Cuando escribes en el móvil "tengo cita con el" y el teclado te propone "médico", está haciendo en pequeño lo mismo que hace un modelo de lenguaje: apostar por lo que sigue. La diferencia es de tamaño. El teclado ha visto tus mensajes; el modelo ha leído una parte enorme de lo que se ha escrito en internet, en libros y en revistas (Vaswani 2017).

La imagen que uso en las sesiones es otra. Imagina un residente de primer año que se ha leído la biblioteca entera. No recuerda de qué libro sacó cada cosa. Nunca ha visto a esta paciente. Y ha aprendido, en miles de exámenes, que dejar una pregunta en blanco puntúa peor que contestar con aplomo. Eso es un modelo de lenguaje: un compañero leidísimo, sin memoria de fuentes, sin acceso a la persona y entrenado para que la frase suene bien.

Y suena bien de verdad: los modelos grandes aprueban preguntas de examen de licencia médica, y los más recientes con nota (Singhal 2023). Pero aprobar un examen no es pasar consulta. El residente lo sabría. La máquina, no.

Se llama modelo de lenguaje de gran tamaño, LLM por sus siglas en inglés. Se entrena con una sola tarea: dado un texto, adivinar la pieza que sigue. Después se le pule con miles de ejemplos de conversación para que responda como asistente. El pulido cambia el tono. No cambia el motor.

### Cinco palabras, una frase cada una

- **Token.** La pieza mínima que el modelo lee y escribe. No es una palabra: es un trozo. "Adiposidad" pueden ser tres. Los límites y los precios de estas herramientas se cuentan en tokens.
- **Ventana de contexto.** La mesa de trabajo. Todo lo que el modelo puede tener delante a la vez: tu prompt, los archivos que adjuntas, la conversación anterior. Lo que no cabe en la mesa no existe para él.
- **Azar.** La misma pregunta, dos veces, dos respuestas. No es un fallo: elige entre varias piezas probables con una pizca de sorteo. Por eso importa tanto un prompt cerrado. Y por eso la calculadora del capítulo 8 la escribió una máquina que no es determinista, pero el programa que salió sí lo es: mismos datos, mismo resultado, siempre.
- **Multimodalidad.** Los modelos actuales leen imágenes, PDF y audio; algunos, vídeo. Para ellos, la foto de una etiqueta es texto. Es la puerta a un uso que cabe en siete minutos, y también a subir sin querer una imagen con una persona dentro.
- **Alucinación.** Una respuesta plausible y falsa. Merece sección propia.

Y tres cosas que un modelo no hace si nadie se lo activa: no busca en internet, no recuerda tu conversación de ayer y no sabe qué día es. Tiene una fecha de corte de conocimiento y, de lo posterior, nada. Tampoco ve tu historia clínica. Hoy, para ti y para mí, eso es una ventaja.

### Por qué suena seguro cuando se equivoca

Vuelve al residente que no deja preguntas en blanco. Cuando le pido una referencia, no la busca: la construye. Ha visto millones de referencias y conoce su forma: apellido, inicial, revista real, año, un DOI que empieza por 10. Cada pieza es probable. El conjunto es falso. Eso es una alucinación: no un error de cálculo, sino texto con forma de verdad (Ji 2023).

En un estudio de 2023, de 115 referencias que un chat generó para textos médicos, casi la mitad no existía y solo un 7 % era correcta del todo (Bhattacharyya 2023). Con la versión siguiente del mismo modelo, las inventadas bajaron de la mitad a menos de un quinto; bajaron, no desaparecieron (Walters 2023). Y un trabajo de 2025 explicó el porqué con una imagen de examen: si contestar mal no resta y dejar en blanco no suma, el alumno aprende a contestar siempre (Kalai 2025). A la máquina la hemos educado así.

Por eso la pregunta "¿se equivoca?" no sirve: sí, siempre puede. La útil es otra: **¿cuánto cuesta que se equivoque en esta tarea?**

- **Coste bajo.** Un borrador que vas a leer entero y corregir: las frases del capítulo 1, el guion de una sesión. Si falla, pierdes dos minutos.
- **Coste medio.** Algo que puede llegar a otra persona sin que tú lo notes: una hoja para pacientes, un resumen que reenvías. Si falla, lo repites en voz alta.
- **Coste alto.** Una dosis, una interacción, un diagnóstico, una cita en un informe, un dato de una persona. Si falla, daña. Aquí la respuesta puede ser: no, o no con esta herramienta.

A más coste, más comprobación, mejor herramienta y menos prisa. La comprobación es doble: antes de pegar, para que no entre nada que no deba; después de leer, para que no salga nada que no sea cierto. Ninguna de las dos la hace la máquina por ti.

### La mesa es grande, pero se lee mal por el medio

Las ventanas de contexto ya admiten libros enteros. Pero caber no es leer. Un estudio de 2024 lo midió: cuando la información está al principio o al final de un texto largo, el modelo la encuentra; cuando está a mitad, la pierde con frecuencia (Liu 2024). Lo notarás en cuanto subas una guía.

Tres gestos lo mitigan: pon lo importante al principio o al final del prompt; dirige la atención ("mira solo el apartado de diagnóstico"); y pide la cita literal con la página, para poder abrirla. El caso 3 lo hace paso a paso.

### Y trae los sesgos de lo que ha leído

Se ha entrenado con internet. E internet está lleno de "comer menos y moverse más", de chistes sobre el peso y de dietas milagro. Si no le dices lo contrario, el modelo devuelve el tono medio de lo que leyó, y el tono medio es el estigma. Se ha demostrado con la medicina basada en la raza: varios modelos repetían mitos ya desmentidos (Omiye 2023). Con el peso no tengo un estudio que citar; tengo la experiencia de pedir diez consejos y recibir la fórmula de siempre.

Por eso los prompts de este libro llevan restricciones tan largas. No es manía. Es que el valor por defecto de la máquina no es el nuestro.

## Segunda parte · No todo lo que se llama IA es lo mismo

### "Lo dijo la IA" es como "lo dijo el médico"

¿Qué médico? ¿Cuándo? ¿Con qué datos delante? Decir "la IA" es como decir "el aparato": el tensiómetro de la farmacia y el Holter miden los dos, y no sirven para lo mismo. Hoy conviven, como mínimo, cuatro niveles. Los nombres cambian cada pocos meses: comprueba la versión vigente antes de fiarte de esta lista.

- **Gratuita.** La versión sin pagar de Gemini, ChatGPT, Claude o similares. Sirve para aprender y para casi todo lo del capítulo 1. Sus límites: un modelo menos capaz o más antiguo, que con mucho tráfico se sustituye por otro más ligero sin avisar; menos mensajes, menos contexto, a veces sin archivos. Y la casilla de entrenamiento con tus datos suele venir activada.
- **De pago.** Unos veinte euros al mes cuando escribo esto. Acceso al mejor modelo de ese proveedor, más contexto, archivos, ejecución de código, búsqueda en profundidad. Sigue siendo una herramienta de consumo: sin acuerdo de tratamiento de datos y con las mismas reglas de privacidad que la gratuita.
- **Frontera.** El modelo más capaz que existe en cada momento, sea de quien sea. A veces solo está en los planes caros. Para tareas con coste de error alto y datos públicos: comparar dos guías, revisar un texto tuyo, escribir el código de una calculadora.
- **Local.** Modelos abiertos que se descargan y corren en tu propio ordenador; nada sale de él. Exigen equipo y manos, y rinden por debajo. Para Atención Primaria es un escenario futuro, no un punto de partida. Y correr en tu ordenador no es cumplir la normativa: el ordenador del centro tiene sus propias reglas.

Hay una quinta categoría que yo no tengo: la herramienta con acuerdo de tratamiento de datos que te dé tu servicio de salud. Si la tienes, lee su contrato y qué cubre. Si no, estás donde yo, y todo este libro funciona desde ahí. Ninguna herramienta de consumo está autorizada como producto sanitario, y hay quien reclama una regulación específica para estos modelos en salud (Meskó 2023). El marco legal, sin miedo, va en el capítulo 3.

### Chat o razonador

Dentro de cada proveedor hay, además, dos maneras de responder. El **modo chat** contesta al momento: rápido, barato, suficiente para borradores y trámites. El **modo razonador** se para antes de escribir: descompone la pregunta, se corrige y tarda desde treinta segundos hasta varios minutos. Nació de un hallazgo sencillo: si obligas al modelo a escribir los pasos intermedios, acierta más en problemas de varios pasos (Wei 2022). Los razonadores lo hacen de fábrica.

Cuál usar lo decide el coste de error, no la novedad. Reescribir una frase: chat. Un caso sintético con fricción, una comparativa entre guías, un código: razonador. Y una advertencia: razonar más no es verificar. Un razonador puede llegar con más pasos a una conclusión falsa, y la escribe igual de bien.

### Seis preguntas antes de pegar nada

Antes de cada tarea, seis preguntas. Caben en un post-it.

- **¿Qué modelo y qué versión?** Mira el nombre en el desplegable. Anótalo cuando algo te funcione: dentro de tres meses no será el mismo.
- **¿Qué plan?** Gratuito o de pago cambia el modelo, el contexto y las herramientas.
- **¿Cuánto cabe en la mesa?** Un PDF de doscientas páginas puede no caber. O caber y leerse mal por el medio.
- **¿Qué herramientas tiene activas?** Búsqueda en internet, archivos, código, memoria. Sin búsqueda no hay citas fiables ni nada posterior a su fecha de corte.
- **¿Tiene acuerdo de tratamiento de datos?** Si no lo sabes, no lo tiene.
- **¿Cuánto cuesta que se equivoque?** Y, por tanto, cuánto vas a comprobar.

Las seis caben en una que aprendí en mi formación en IA y he hecho mía: qué nivel de IA exige esta tarea. Y con cualquier herramienta de consumo, la higiene del capítulo 1: entrenamiento desactivado, borrar al terminar, versión vigente comprobada.

---

## Siete casos para tocar la máquina

Cada caso trae situación, prompt literal (rol · contexto · tarea · formato · restricciones), ejemplo abreviado de salida, qué revisar y riesgo. Sustituye lo que va entre corchetes; ninguno admite datos de pacientes. Los casos 1, 2, 5 y 6 funcionan igual en Gemini, ChatGPT y Claude; el 3 y el 4 dependen de que tu plan admita archivos e imágenes; el 7 no usa IA. Las cifras de los ejemplos son inventadas. Los nombres de los modelos y de los modos cambian: comprueba la versión vigente.

### Caso 1 · La misma pregunta en tres modelos

**Momento:** docencia. **Herramienta:** Gemini, ChatGPT y Claude en tres pestañas, sin búsqueda en internet activada.

**Situación.** Quieres enseñar al equipo, en cinco minutos de sesión, que "la IA" no es una cosa. Lo más rápido: tres respuestas a la misma pregunta clínica general. Pega el mismo prompt en las tres herramientas, en conversaciones nuevas.

```
ROL: Eres médica de familia con formación en obesidad como enfermedad crónica.

CONTEXTO: Respondo a una pregunta clínica general para una sesión docente de Atención Primaria. No hay ningún paciente detrás: no incluyas ni pidas datos de personas.

TAREA: Responde a esta pregunta: "[pregunta general, por ejemplo: ¿Qué cambios hormonales explican que se recupere el peso después de una dieta?]".

FORMATO: Un párrafo de unas 150 palabras. Debajo, una tabla con cada afirmación que has hecho, en tres columnas: afirmación; certeza (ALTA / MEDIA / BAJA); fuente con autor y año si conoces una real. Si no conoces la fuente, escribe SIN FUENTE: no la inventes. Última línea: el nombre de tu modelo y tu fecha de corte de conocimiento, si los conoces; si no, escribe NO DISPONIBLE.

RESTRICCIONES: Sin nombres comerciales de medicamentos. Usa siempre "persona con obesidad". No busques en internet en este ejercicio.
```

**Ejemplo abreviado de salida (una de las tres).**

> Tras una pérdida de peso, la leptina desciende y la grelina aumenta, lo que eleva el hambre y reduce la saciedad […].
> | Afirmación | Certeza | Fuente |
> |---|---|---|
> | La leptina baja tras perder peso | ALTA | Sumithran 2011 |
> | El GLP-1 sube tras perder peso | MEDIA | SIN FUENTE |

**Qué revisar antes de usarla.** Cuenta los SIN FUENTE de cada modelo y comprueba en PubMed las fuentes que sí da. Mira qué afirmaciones se contradicen entre los tres: en el ejemplo, una dice que el GLP-1 sube; el capítulo 1 explica que baja. Esa contradicción es la sesión.

**Riesgo principal y mitigación.** Que el equipo elija "la mejor" respuesta por cómo suena. Mitigación: la tabla se enseña para mostrar variabilidad, no para votar; la verdad se comprueba fuera, en la fuente.

### Caso 2 · Cazar una alucinación

**Momento:** docencia. **Herramienta:** cualquier asistente conversacional, primero sin búsqueda; después, PubMed.

**Situación.** Es el ejercicio con el que aprendí yo. Pides cinco referencias sobre adaptación metabólica y compruebas cuántas existen. Diez minutos que cambian cómo miras una cita generada.

```
ROL: Eres una documentalista científica que trabaja con revistas biomédicas indexadas.

CONTEXTO: Preparo una lista de lectura sobre adaptación metabólica tras la pérdida de peso en personas adultas. Es un ejercicio de formación; no hay pacientes ni datos de personas.

TAREA: Dame cinco referencias de artículos originales o revisiones sobre adaptación metabólica tras la pérdida de peso.

FORMATO: Tabla con seis columnas: primer autor; año; revista; título; DOI; PMID. Y una séptima, CERTEZA, con uno de estos tres valores: SEGURA (recuerdas la referencia con detalle), PROBABLE (recuerdas autores y tema, no los datos exactos), DUDOSA. Si no llegas a cinco con certeza SEGURA o PROBABLE, deja las filas restantes vacías y escribe "LISTA INCOMPLETA".

RESTRICCIONES: No inventes DOI ni PMID: si no los recuerdas, escribe DESCONOCIDO en esa casilla. No busques en internet en este ejercicio. No incluyas datos de personas.
```

**Ejemplo abreviado de salida.**

> | Autor | Año | Revista | DOI | PMID | CERTEZA |
> |---|---|---|---|---|---|
> | Fothergill | 2016 | Obesity | 10.1002/oby.21538 | DESCONOCIDO | SEGURA |
> | Martínez | 2019 | Int J Obes | 10.1038/s41366-019-0311-x | 30976123 | PROBABLE |

**Qué revisar antes de usarla.** Todo: el ejercicio es la revisión. Busca cada fila en PubMed por título y primer autor; pega cada DOI en el navegador. Cuatro resultados posibles: existe y dice lo que parece; existe, pero el DOI o el año están mal; existe, pero trata de otra cosa; no existe. En mi experiencia, las cinco filas rara vez salen del primer grupo, ni con la etiqueta SEGURA. Después repite con la búsqueda en internet activada y compara: mejora mucho, no desaparece.

**Riesgo principal y mitigación.** Confiar en un DOI porque tiene forma de DOI. Mitigación: ninguna referencia entra en un documento tuyo sin que la hayas abierto. Ninguna.

### Caso 3 · Lo que se pierde en medio

**Momento:** consulta (preparación). **Herramienta:** asistente que admita archivos adjuntos; NotebookLM lo hace mejor, con citas.

**Situación.** Quieres un dato concreto de una guía larga y pública, por ejemplo la GIRO de la SEEDO (2024), y no recuerdas en qué página está. Sube solo documentos públicos, descargados de su web oficial, para uso personal. Dos turnos: primero sin ayuda, después dirigiendo la atención.

```
ROL: Eres una asistente de lectura de documentos clínicos.

CONTEXTO: Te adjunto una guía clínica pública sobre obesidad en personas adultas [por ejemplo: la guía GIRO de la SEEDO, 2.ª edición, 2024]. No contiene datos de pacientes y no debes añadir ninguno.

TAREA: Busca en el documento adjunto [dato concreto, por ejemplo: los puntos de corte de perímetro de cintura que la guía utiliza para definir obesidad abdominal] y transcríbelo literalmente.

FORMATO: (1) La cita literal, entre comillas, sin resumir. (2) La página y el apartado donde está. (3) Una línea con una de estas dos etiquetas: ENCONTRADO EN EL DOCUMENTO / NO ENCONTRADO EN EL DOCUMENTO. Si es NO ENCONTRADO, no lo completes con lo que sepas de otras fuentes: escribe la etiqueta y para.

RESTRICCIONES: Solo el documento adjunto. Sin interpretación clínica. Sin recomendaciones. Si hay varios pasajes, transcríbelos todos con su página.
```

Segundo turno, en la misma conversación: `Revisa solo el apartado [nombre o número, por ejemplo: "Diagnóstico y evaluación"] y repite la tarea con el mismo formato.`

**Ejemplo abreviado de salida.**

> Turno 1: "Se considera obesidad abdominal a partir de [cifra] cm en varones y [cifra] cm en mujeres". Página: no localizada. NO ENCONTRADO EN EL DOCUMENTO.
> Turno 2: "[cita literal de la guía]". Página 31, apartado 4.2. ENCONTRADO EN EL DOCUMENTO.

**Qué revisar antes de usarla.** Abre el PDF por la página que dice y comprueba que la frase está ahí, tal cual. En el ejemplo, el turno 1 recitó una cifra de memoria y lo confesó a medias: cifra sin página. Es la mezcla más peligrosa: un dato real de otra fuente, atribuido a esta.

**Riesgo principal y mitigación.** Que el modelo "recuerde" en vez de leer. Mitigación: cita literal con página, etiqueta cerrada y tus ojos en el PDF. Si el documento es muy largo y tu plan es gratuito, quizá no cabe entero en la mesa: pregúntale cuántas páginas ve, o sube solo el capítulo que necesitas.

### Caso 4 · Leer una etiqueta nutricional

**Momento:** consulta o educación grupal. **Herramienta:** asistente multimodal, que lea imágenes.

**Situación.** "Esto es light, ¿no?" Te enseñan un paquete de letra diminuta. Una foto de la etiqueta, solo la etiqueta: sin manos, sin ticket, sin la cocina de nadie detrás. La haces tú, con tu móvil, y la borras al terminar, del chat y del carrete.

```
ROL: Eres una dietista-nutricionista que lee etiquetas de alimentos envasados.

CONTEXTO: Te adjunto la foto de la etiqueta de un producto envasado. En la imagen no hay personas ni datos personales, y no debes inferir nada sobre quién lo consume.

TAREA: (1) Transcribe la tabla nutricional tal como aparece: energía, grasas, de las cuales saturadas, hidratos de carbono, de los cuales azúcares, fibra, proteínas y sal, por 100 g o 100 ml y por ración si figura. (2) Transcribe la lista de ingredientes en su orden. (3) Señala los tres primeros ingredientes y cuántos azúcares añadidos o edulcorantes aparecen en la lista, con sus nombres. (4) Si un número o una palabra no se lee con claridad, escribe ILEGIBLE en esa casilla; no lo estimes.

FORMATO: La tabla; debajo, la lista de ingredientes; debajo, tres frases descriptivas en lenguaje llano, trato de [usted / tú], que digan qué lleva el producto y en qué cantidad, sin valorarlo.

RESTRICCIONES: No digas si el producto es "bueno", "malo", "sano" o "light", ni si conviene a alguien. Sin consejos individuales, sin necesidades diarias, sin mencionar peso ni dietas. Sin nombres de marca: llama al producto por su tipo ("galleta de cereales", "yogur de sabores").
```

**Ejemplo abreviado de salida.**

> Por 100 g: energía 452 kcal; grasas 18 g, saturadas 8,2 g; hidratos 64 g, azúcares 23 g; fibra 3,1 g; sal 0,9 g. Ración (30 g): azúcares 6,9 g.
> Ingredientes: harina de trigo, azúcar, aceite de palma […]. Azúcares añadidos: azúcar, jarabe de glucosa (2).

**Qué revisar antes de usarla.** Los números, con la etiqueta delante: un 4,5 se lee como 45 con facilidad. El orden de los ingredientes, que es lo que de verdad informa: la normativa europea obliga a listarlos de mayor a menor peso (Reglamento 1169/2011). Y que las tres frases no se hayan deslizado hacia "es poco saludable": eso lo hablas tú, con la persona.

**Riesgo principal y mitigación.** Dos: un decimal mal leído y una foto con más de lo que querías. Mitigación: ILEGIBLE en vez de estimar, y la foto la revisas tú antes de subirla. Este caso necesita que tu plan lea imágenes; cuando escribo esto, las versiones gratuitas de las tres grandes lo hacen. Comprueba la tuya.

### Caso 5 · Qué nivel de IA exige esta tarea [AP]

**Momento:** administración. **Herramienta:** papel, o cualquier asistente conversacional.

**Situación.** Tienes la lista de tareas del capítulo 1 o, si no la hiciste, diez tareas de una jornada cualquiera. Quieres saber, tarea por tarea, qué nivel de herramienta, qué comprobación y qué datos. Se puede hacer con lápiz; el prompt solo lo ordena. Antes de pegar, lee la lista: tareas, no personas.

```
ROL: Eres una consultora que ayuda a médicas de familia a decidir cuándo y cómo usar IA generativa con seguridad.

CONTEXTO: Te pego diez tareas de una jornada de Atención Primaria, descritas de forma genérica y sin datos de personas; ya lo he revisado. Trabajo solo con herramientas de consumo, sin acuerdo de tratamiento de datos. Los niveles posibles son cinco: PAPEL (mejor sin IA); GRATUITA; DE PAGO; RAZONADOR O FRONTERA; SOLO CON CONTRATO (necesita datos clínicos reales y hoy no la hago con IA).

TAREA: Para cada tarea indica: (a) coste de error si la IA se equivoca: BAJO (lo leo entero y lo corrijo), MEDIO (podría llegar a otra persona sin que yo lo note), ALTO (afecta a una decisión clínica, a un dato de paciente o a un documento oficial); (b) datos de pacientes que necesita: NINGUNO / SOLO RECUENTOS AGREGADOS / DATOS REALES; (c) nivel de herramienta; (d) la comprobación humana que haría antes de usar la salida, en una línea. Si una tarea no está clara, clasifícala como POR ACLARAR y escribe la pregunta que me harías.

FORMATO: Tabla con la tarea y las cuatro columnas. Debajo, dos listas: tareas que hoy no debo hacer con IA y por qué; tareas donde una herramienta gratuita basta.

RESTRICCIONES: No inventes tareas ni cambies mis descripciones. No propongas automatizar decisiones clínicas. Si una tarea implica datos identificables, el nivel es SOLO CON CONTRATO aunque parezca sencilla. Como comprobación adicional a la mía, si una línea contiene algo que parezca identificar a una persona, no la clasifiques: ponla en una lista "REVISAR PRIVACIDAD".

TAREAS:
[una por línea, por ejemplo: resumir una guía pública para la sesión del jueves; redactar una hoja informativa sobre etiquetas; contestar una reclamación; preparar la interconsulta de una paciente; …]
```

**Ejemplo abreviado de salida.**

> | Tarea | Coste de error | Datos | Nivel | Comprobación |
> |---|---|---|---|---|
> | Resumir guía pública para sesión | MEDIO | NINGUNO | DE PAGO | Abrir cada cita en el PDF |
> | Interconsulta de una paciente | ALTO | DATOS REALES | SOLO CON CONTRATO | No aplica hoy |

**Qué revisar antes de usarla.** Cada fila, con tu criterio: la tabla la firmas tú. Si el modelo puso GRATUITA donde tú dudabas, gana la duda. Y "SOLO CON CONTRATO" significa "hoy no", no "búscate la manera".

**Riesgo principal y mitigación.** Que la tabla funcione como permiso. Mitigación: ante la duda, un nivel más alto o papel; y la tabla se revisa cuando cambie la herramienta o tu plan.

### Caso 6 · Chat frente a razonador

**Momento:** consulta (entrenar el propio criterio). **Herramienta:** el mismo asistente en modo chat y en modo razonador. El nombre del modo cambia según la herramienta y el mes; búscalo en el desplegable de modelos.

**Situación.** Un caso inventado por ti, escrito de memoria, sin ninguna persona real detrás. Pegas el prompt dos veces, en dos conversaciones nuevas: una en modo chat, otra en modo razonador. Cronometra. Es un ejercicio de razonamiento, no una consulta.

```
ROL: Eres médica de familia con experiencia en obesidad. Esto es un ejercicio de razonamiento sobre un caso inventado; no es una consulta real y no debes tomar ni proponer decisiones para ninguna persona concreta.

CONTEXTO: Caso sintético, escrito por mí: [descripción inventada, por ejemplo: mujer de unos cincuenta años, obesidad de grado II, hipertensión tratada con un fármaco, dos glucemias en ayunas en rango de prediabetes, ronquidos con somnolencia diurna, cansancio y ánimo bajo desde hace meses, cuatro intentos previos de bajar de peso con recuperación, un antidepresivo desde hace un año]. No hay más datos.

TAREA: No cierres ningún diagnóstico. Escribe cuatro listas: (1) lo que está en el caso, hecho por hecho; (2) lo que deduces de cada hecho y con qué certeza (ALTA / MEDIA / BAJA); (3) lo que falta y cambiaría el razonamiento, ordenado por importancia; (4) qué preguntaría y qué exploraría una médica de familia en la siguiente visita, sin proponer tratamientos.

FORMATO: Cuatro listas numeradas, máximo siete puntos cada una. Al final, una línea con los atajos de razonamiento que has vigilado en tu propia respuesta (por ejemplo, quedarte con la primera explicación).

RESTRICCIONES: Sin nombres comerciales ni propuestas de fármacos. Sin diagnósticos cerrados. No añadas datos al caso: si los necesitas, van en la lista 3. Usa "persona con obesidad".
```

**Ejemplo abreviado de salida.**

> Modo chat (12 segundos): lista 2 con cinco deducciones, tres de ellas ALTA; "la somnolencia sugiere apnea del sueño (ALTA)".
> Modo razonador (2 minutos y medio): la misma sospecha en MEDIA; añade en la lista 3 el antidepresivo como posible causa de ganancia de peso y pregunta por atracones nocturnos y por función tiroidea.

**Qué revisar antes de usarla.** Las certezas: ¿qué marcó ALTA que tú pondrías en MEDIA? Las ausencias: ¿nombró las cinco cosas que el capítulo 1 pide mirar antes de atribuirlo todo a la biología? Y el tiempo: el razonador tardó diez veces más para un caso que tú resuelves mentalmente en treinta segundos. Eso también es un dato.

**Riesgo principal y mitigación.** Que el ejercicio te tiente a pegar un caso real. Mitigación: solo casos inventados en herramientas de consumo; la derivación y el tratamiento van en el capítulo 8, no en un chat.

### Caso 7 · Inventario de lo que tengo [AP]

**Momento:** administración. **Herramienta:** ninguna. Una hoja.

**Situación.** Quieres saber con qué trabajas de verdad: qué herramientas, con qué cuenta, qué tienen activado y qué no puede entrar en ellas. Es el único caso sin prompt: una ficha, rellenada a mano.

```
INVENTARIO DE HERRAMIENTAS · [fecha]

Herramienta: [Gemini / ChatGPT / Claude / NotebookLM / Perplexity / otra]
Modelo que aparece en el desplegable: [nombre y versión]
Cuenta: [personal / de organización]     Plan: [gratuito / de pago]
Acuerdo de tratamiento de datos con mi servicio de salud: [no / sí: contrato visto por mí el (fecha)]
Entrenamiento con mis conversaciones: [desactivado / activado / no lo sé]
Herramientas activas: [búsqueda en internet / archivos / imágenes / código / memoria / ninguna]
Lo que entra: [textos propios, documentos públicos, casos inventados, recuentos agregados]
Lo que no entra: [ningún dato de paciente, ninguna imagen con personas, ningún documento interno del centro]
Herramientas con contrato que me ofrece mi centro o mi servicio de salud: [ninguna / nombre y qué cubre]
Próxima revisión de esta ficha: [dentro de tres meses]
```

**Ejemplo abreviado de salida (ficha rellenada).**

> Gemini, cuenta personal, plan gratuito. Acuerdo de datos: no. Entrenamiento: no lo sé. Herramientas: imágenes y archivos. Del centro: ninguna.

**Qué revisar antes de usarla.** Cada "no lo sé" es una tarea: el entrenamiento se desactiva en la configuración de la cuenta, y el nombre del modelo está en el desplegable. Pregunta a tu centro, o a su delegado de protección de datos, si existe alguna herramienta con contrato: a veces la hay y nadie lo ha contado.

**Riesgo principal y mitigación.** Creer que "gratuita" es "privada", o que "de organización" es "con contrato". Mitigación: la ficha a la vista, junto al post-it de las seis preguntas, y una revisión cada tres meses. Las políticas cambian más deprisa que las guías.

---

## Caso ilustrativo, no real: arquetipo compuesto

> Esta viñeta combina rasgos de varias personas que han llegado a mi consulta con una respuesta de un chat. Se han modificado la ocupación, el modelo de IA citado y la petición concreta; la edad es aproximada y no hay fechas, lugares ni cifras que permitan reconocer a nadie.

Tiene entre cuarenta y cincuenta años, obesidad de grado II y una analítica reciente que pidió por su cuenta. Entra con un folio doblado en cuatro y lo pone sobre la mesa antes de sentarse. "Me dice que tengo resistencia a la insulina y que necesito tal medicación."¹

"¿Quién se lo dice?" "La IA." Y ahí está mi pregunta de siempre: ¿cuál? Me cuenta que pegó su analítica en un chat gratuito, con su nombre y todo, y que le contestó "mejor que muchos médicos". Leo el folio. Es amable, ordenado y suena a que sabe. No me sorprende: en un estudio que comparó respuestas de un chat y de médicos a preguntas de un foro público, los evaluadores prefirieron las del chat y las encontraron más empáticas (Ayers 2023). Amable no es lo mismo que correcta.

Y no todo está mal. La resistencia a la insulina es frecuente cuando hay exceso de grasa visceral; la máquina completó la frase más probable. Lo que no sabe es lo que él no le contó: que su padre tuvo diabetes, que duerme cinco horas, que dejó de fumar hace dos años y ganó doce kilos, y que la "medicación" que pide no se elige con una analítica. El chat no lo conoce. Yo, en seis minutos, lo conozco un poco más.

Se lo explico con la imagen de este capítulo: la máquina no consultó nada; construyó la frase que mejor sonaba con lo que le dio. Le digo lo que hizo bien: mirar, preguntar, venir. Y lo que quiero que no vuelva a hacer, sin regañar: pegar su nombre y sus datos en una herramienta que nadie ha contratado para guardarlos. Anoto obesidad como problema activo, con IMC y cintura. Le pido la analítica que falta. Las opciones de tratamiento existen y hablaremos de ellas en la siguiente visita: son el capítulo 8.

Se va con el folio en el bolsillo y con una cita. Quizá vuelva a preguntarle al chat. Pero ahora sabe qué le contesta: un compañero leidísimo que nunca lo ha visto.

¹ Declaración de transparencia: mantengo vínculos con Novo Nordisk, detallados al inicio del libro. En esta viñeta no se nombra ningún fármaco; el tratamiento farmacológico de la obesidad se aborda en el capítulo 8.

---

## En 60 segundos

1. Un modelo de lenguaje apuesta por la siguiente pieza de texto: por eso suena seguro aunque se equivoque.
2. La alucinación no es un fallo raro, es su forma de trabajar; la pregunta útil es cuánto cuesta que se equivoque aquí.
3. La mesa es grande, pero se lee mal por el medio: dirige la atención y pide la cita con página.
4. "La IA" no existe: hay gratuita, de pago, frontera y local, y modo chat o razonador; anota modelo, versión y plan.
5. Sin acuerdo de tratamiento de datos solo entran textos propios, documentos públicos, casos inventados y recuentos; y lo que sale lo compruebas tú.

## Hazlo hoy · 10 minutos

Te propongo cuatro pasos:

1. **(1 min)** Abre tu asistente y mira el nombre del modelo en el desplegable. Apúntalo. Si no lo encuentras, ya has aprendido algo.
2. **(3 min)** Pega el prompt del caso 2: cinco referencias sobre adaptación metabólica.
3. **(5 min)** Busca las cinco en PubMed. Cuenta cuántas existen, cuántas están mal y cuántas no aparecen.
4. **(1 min)** Entra en la configuración de la cuenta y desactiva el entrenamiento con tus conversaciones. Borra la conversación.

Mañana alguien te traerá un folio doblado en cuatro. Tendrás siete minutos. La máquina no sabe que no sabe. Tú sí. Esa es toda la diferencia, y es tuya.

---

## Referencias

1. Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, et al. Attention is all you need. En: Advances in Neural Information Processing Systems 30 (NIPS 2017); Long Beach (CA); 2017. p. 5998-6008. arXiv:1706.03762.
2. Singhal K, Azizi S, Tu T, Mahdavi SS, Wei J, Chung HW, et al. Large language models encode clinical knowledge. Nature. 2023;620(7972):172-80. doi:10.1038/s41586-023-06291-w
3. Ji Z, Lee N, Frieske R, Yu T, Su D, Xu Y, et al. Survey of hallucination in natural language generation. ACM Comput Surv. 2023;55(12):248. doi:10.1145/3571730
4. Bhattacharyya M, Miller VM, Bhattacharyya D, Miller LE. High rates of fabricated and inaccurate references in ChatGPT-generated medical content. Cureus. 2023;15(5):e39238. doi:10.7759/cureus.39238
5. Walters WH, Wilder EI. Fabrication and errors in the bibliographic citations generated by ChatGPT. Sci Rep. 2023;13(1):14045. doi:10.1038/s41598-023-41032-5
6. Kalai AT, Nachum O, Vempala SS, Zhang E. Why language models hallucinate [preprint]. arXiv; 2025. arXiv:2509.04664. [VERIFICAR: comprobar identificador y si existe versión publicada en revista]
7. Liu NF, Lin K, Hewitt J, Paranjape A, Bevilacqua M, Petroni F, et al. Lost in the middle: how language models use long contexts. Trans Assoc Comput Linguist. 2024;12:157-73. doi:10.1162/tacl_a_00638
8. Omiye JA, Lester JC, Spichak S, Rotemberg V, Daneshjou R. Large language models propagate race-based medicine. NPJ Digit Med. 2023;6(1):195. doi:10.1038/s41746-023-00939-z
9. Meskó B, Topol EJ. The imperative for regulatory oversight of large language models (or generative AI) in healthcare. NPJ Digit Med. 2023;6(1):120. doi:10.1038/s41746-023-00873-0
10. Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, et al. Chain-of-thought prompting elicits reasoning in large language models. En: Advances in Neural Information Processing Systems 35 (NeurIPS 2022); New Orleans (LA); 2022. arXiv:2201.11903.
11. Sumithran P, Prendergast LA, Delbridge E, Purcell K, Shulkes A, Kriketos A, et al. Long-term persistence of hormonal adaptations to weight loss. N Engl J Med. 2011;365(17):1597-604. doi:10.1056/NEJMoa1105816
12. Fothergill E, Guo J, Howard L, Kerns JC, Knuth ND, Brychta R, et al. Persistent metabolic adaptation 6 years after "The Biggest Loser" competition. Obesity (Silver Spring). 2016;24(8):1612-9. doi:10.1002/oby.21538
13. Sociedad Española para el Estudio de la Obesidad (SEEDO). Guía Española GIRO: Guía española del manejo Integral y multidisciplinaR de la Obesidad en personas adultas. 2.ª ed. Lecube A, coordinador. Madrid: SEEDO; noviembre de 2024. Disponible en: https://www.seedo.es/images/site/giro/GUIA-GIRO-2a-edicin_26NOV2024.pdf
14. Reglamento (UE) n.º 1169/2011 del Parlamento Europeo y del Consejo, de 25 de octubre de 2011, sobre la información alimentaria facilitada al consumidor. Diario Oficial de la Unión Europea L 304, 22 de noviembre de 2011, p. 18-63.
15. Ayers JW, Poliak A, Dredze M, Leas EC, Zhu Z, Kelley JB, et al. Comparing physician and artificial intelligence chatbot responses to patient questions posted to a public social media forum. JAMA Intern Med. 2023;183(6):589-96. doi:10.1001/jamainternmed.2023.1838
