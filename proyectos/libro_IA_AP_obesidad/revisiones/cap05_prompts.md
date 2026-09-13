# Revisión PROMPTS · Capítulo 5 · v1

> Agente: PROMPTS (ingeniero de prompts) · Fecha: 2026-09-13 · Ámbito: exclusivamente los ocho bloques de código que el capítulo ofrece al lector (casos 1 a 8) y los ocho ejemplos abreviados de salida que los acompañan, más la frase introductoria a los casos (l. 69-71) porque fija reglas que los prompts heredan. No se revisa el texto expositivo, el cuadro de la Tercera parte ni las referencias.
> Versión revisada: `capitulos/cap05_v1.md` (395 líneas, 7.921 palabras; las líneas citadas son las de esa versión, `grep -n`).
> Método: el de los capítulos 1 a 4 (`revisiones/cap04_prompts.md`). Para cada prompt: rol · contexto · tarea · formato · restricciones; anonimización y etiqueta (0) antes que el contenido, que para si hay datos (T1 del capítulo 3, T7 del capítulo 4); variables entre corchetes con valor por defecto; recuentos definidos en la misma línea y contables a mano (T5 del capítulo 4); si el modelo puede rellenar un [FALTA: …] o un POR ACLARAR sin que se note (T4 del capítulo 4); portabilidad Gemini / ChatGPT / Claude sin cambios; realismo del ejemplo de salida (lo que devuelven los modelos de consumo en 2026); riesgo. Cada prompt se ha ejecutado mentalmente con el caso sintético que el propio prompt trae (o con uno construido de cero, regla 22) y la salida se ha leído con la rúbrica del capítulo 4 (fidelidad · priorización · calibración · confusores · acción segura) y con las diez preguntas del anexo B. Reglas 7, 11, 12, 13, 16, 17, 19, 21 y 22 de `biblia.md` aplicadas como norma; ficha del caso 7 del capítulo 4 (v3) como plantilla de guardado.

## Resumen de veredictos

| Caso | Título | Bloques | Veredicto | Motivo principal |
|---|---|---|---|---|
| 1 | Notas sueltas → nota estructurada con [FALTA] | 1 prompt + 1 salida | **mejorar (leve)** | Las notas telegráficas sintéticas son verosímiles (así se escribe con prisa) y contienen, sin buscarlo, las dos trampas correctas: "metformina ok" y "pregunta x rodilla", que el modelo convierte en "buena tolerancia" y "consulta por gonalgia" si no se le prohíbe por su nombre. "HECHOS: [n]" no dice qué es un hecho contable (el ejemplo dice 10 y las notas tienen 10 anotaciones separadas por punto: esa es la definición). El corchete "[o la estructura de tu sistema…]" es una instrucción al lector metida dentro del prompt: quien lo pega tal cual confunde al modelo. Y el ejemplo marca "[FALTA: unidad]" en la cintura cuando el prompt dice "con la unidad que yo puse o sin ella". |
| 2 | Interconsulta a la unidad de obesidad o a Endocrinología | 1 prompt + 1 salida | **mejorar** | La correa contra "lo hecho ya en AP" es buena, pero los tres modelos la esquivan con huecos a medias ("Se ha realizado intervención sobre hábitos [FALTA: fecha]"): la frase afirma y el corchete solo pide la fecha. Además el perfil sí contiene cosas hechas en AP (apnea tratada, tensión tratada, seguimiento mensual) y la tarea dice "nada de esto está en el perfil": el modelo no sabe dónde ponerlas. Gemini añade el criterio entre paréntesis "(p. ej., IMC ≥ 40)" aunque el hueco sea literal; y "técnicas quirúrgicas nombradas: 0" no dice si "cirugía bariátrica" del motivo cuenta. |
| 3 | Informes a petición de la persona | 1 prompt + 1 salida | **mejorar (leve)** | Bien construido y con el mejor recuento del capítulo (palabras concretas, contables con el buscador). Un agujero: la finalidad ("turnos de noche y somnolencia diurna") se convierte en dato clínico de la persona en SITUACIÓN FUNCIONAL ("presenta somnolencia diurna que dificulta el turno de noche [FALTA: desde cuándo]"), que es justo lo que el informe no debe afirmar sin que la médica lo haya visto. Faltan en la lista contable "adherencia", "estilo de vida" y "dieta", que es por donde entran Gemini y ChatGPT. |
| 4 | Del informe hospitalario a mi lista de tareas | 1 prompt + 1 salida | **mejorar** | Sin etiqueta (0): es el prompt en que más probable es que un día entre un informe real ("solo esta vez", dice el propio riesgo), y no tiene freno. Los tres modelos añaden filas que el informe no encarga ("revisar medicación crónica según pérdida de peso", "apoyo psicológico", "recordar la revisión en la unidad") y escriben 0 en el recuento; la solución es una columna "frase del informe que lo encarga, literal": fila sin cita es fila inventada. El alta sintética es demasiado limpia para probar el prompt: sin una sola pauta con dosis ni una tarea que sea claramente de enfermería, no se ve si el modelo copia o retoca. |
| 5 | Plan de cuidados compartido con enfermería | 1 prompt + 1 salida | **mejorar (leve)** | El caso más seguro del capítulo (no entra ningún dato). "TAREAS DE ENFERMERÍA: [n] · TAREAS DE MEDICINA: [n]" no está definido (¿celda?, ¿fila?, ¿verbo?) y cada modelo cuenta una cosa distinta; los tres rellenan "tensión por encima del umbral que fijemos" con "≥ 140/90" salvo que el umbral vaya como hueco literal; y la columna "qué se registra, como [FALTA: campo]" acaba con el mismo marcador en las siete filas. |
| 6 | Resumen de dos años de evolución | 1 prompt + 1 salida | **mejorar** | La lista de palabras de causa o tendencia incluye "por": la propia lista 3 del ejemplo empieza por "Por qué bajó y volvió a subir", así que con la regla tal cual el recuento correcto sería 1 y el ejemplo dice 0. Solución: el recuento se aplica solo a las listas 1 y 2 (la 3 habla de causas por diseño), se quita "por" suelto y se añaden los conectores de dos palabras y las palabras que de verdad escriben los modelos: "control" ("buen/mal control"), "descenso/aumento" como valoración, "abandono" (mes 9: "no acude"). "HITOS: [n]" sin definir (un hito es cada mes de la tabla: 9). Y sin etiqueta (0), en el único caso rojo del capítulo. |
| 7 | La carta de resultados que no alarma | 1 prompt + 1 salida | **listo (retoque)** | Regla 19 bien aplicada (contacto como hueco con la forma única, disclaimer en usted, tope "sin contar las líneas literales"); CONTEXTO DE VOZ coherente, literal, con el "ASÍ ESCRIBES" del capítulo 4. Los modelos no meten cifras ni diagnósticos si se les prohíbe; lo que meten es una valoración que la médica no dio: "todo está dentro de la normalidad", "los resultados son buenos", que además contradice "hay un dato que quiero comentar". Y "no se preocupe", la frase que más alarma, no está en la lista de palabras de alarma. La fórmula del 112 que propone "qué revisar" ("Si se encuentra mal, no espere: urgencias o 112") es una tercera fórmula, fuera de las dos fijadas por la regla 19. |
| 8 | Respuesta a una reclamación con calma | 1 prompt + 1 salida | **mejorar (leve)** | Sale bien en Claude y aceptable en ChatGPT; Gemini se disculpa dos veces y se justifica con "mi intención era ayudarle", que es "por su bien" con otras palabras y no está en la definición del recuento. La tarea (3) pide afirmar que el peso se aborda "siempre pidiendo permiso" cuando el hecho es que esta vez no se pidió: es una defensa, y los tres modelos la escriben como tal. Faltan "pido disculpas" y "perdone" en la definición de disculpa, y las promesas típicas ("tomaré medidas", "no volverá a ocurrir") por su nombre. Es un texto que llega a la persona sin las líneas de la regla 19: el capítulo lo exime; COMPLIANCE decide. |

Ningún prompt es peligroso tal como está: ninguno pide decisiones clínicas, todos llevan "no incluyas ni pidas datos de personas" y los tres que producen texto para alguien (2, 3, 7, 8) prohíben fármacos, cifras y juicios. Tres producen algo que no debe salir sin cambios: el 4 (filas inventadas con recuento a cero y sin freno para un informe real), el 2 (huecos a medias que suenan a la consulta de la lectora) y el 6 (recuento que se contradice con su propio ejemplo). Ninguno hay que rehacer de arriba abajo; el 4 y el 6 se reescriben en las partes que fallan. La portabilidad es limpia: nada depende de razonador, búsqueda ni archivos; los ocho se pegan igual en los tres.

---

## Hallazgos transversales (afectan a varios casos)

**T1 · La etiqueta (0) falta justo donde más falta hace.** Los casos 1, 2 y 3 llevan la línea (0) antes del contenido y con "para" (T1 del capítulo 3, T7 del capítulo 4): bien. Los casos 4, 6 y 8 no la llevan, y son los tres en que lo que se pega podría ser real: un alta ("solo esta vez", l. 210), una tabla de dos años (el "único rojo", l. 268) y una reclamación (la frase introductoria, l. 71, dice que el 8 se borra "porque la queja fue de alguien"). La etiqueta no protege por sí sola (el capítulo 4 ya lo dice: "EJEMPLOS LIMPIOS lo dice el modelo; la limpieza la hiciste tú"), pero es el único freno que actúa después de pulsar Enter, y cuesta una línea. Lo que detecta en cada caso es distinto y hay que decirlo: en el 4, nombre, número de historia, fecha completa, hospital o nombre de un médico; en el 6, fechas de calendario en vez de meses relativos y pesos exactos en vez de rangos; en el 8, nombre, fecha, número de reclamación o expediente. En los tres, "en ese caso, para".

**T2 · Recuentos: la mitad no son contables a mano.** El capítulo hereda bien la salida cerrada con recuento y "tiene que ser 0" (T5 del capítulo 4), y "qué revisar" manda contarlo a mano en los casos 1, 2, 3, 4, 6 y 7. Pero: "HECHOS: [n]" (caso 1) no dice qué es un hecho ("3 sem caminando 20 min x4-5/sem" son uno o tres); "HITOS: [n]" (caso 6) no está definido; "TAREAS DE ENFERMERÍA / DE MEDICINA" (caso 5) no significa nada contable; "técnicas quirúrgicas nombradas" (caso 2) no dice si "cirugía bariátrica" cuenta; "TAREAS: [n]" (caso 4) da 3 en el ejemplo cuando la tabla del propio ejemplo tiene al menos cuatro filas; y "FRASES CON CAUSA O TENDENCIA" (caso 6) contiene "por", que hace que el ejemplo del libro incumpla su propia regla. Regla única, la del capítulo 4: cada recuento se define en la misma línea, con una unidad que la lectora pueda contar con el dedo (anotaciones separadas por punto, filas de la tabla, meses de la tabla, corchetes, palabras de una lista cerrada). Y los que "tienen que ser 0" son autoauditoría: el modelo escribe 0 aunque haya escrito "buena tolerancia"; por eso "qué revisar" tiene que decir qué buscar con el buscador del navegador (lo hace en el 3, 6 y 7; falta en el 1 y el 4).

**T3 · El hueco a medias es la forma nueva de inventar.** El capítulo 4 cerró el hueco rellenado con aproximaciones ("en las próximas semanas"). Este capítulo, al pedir documentos con muchos huecos, abre otra puerta que los tres modelos cruzan: la frase afirmativa con un corchete al final. "Se ha realizado intervención sobre hábitos [FALTA: fecha]" (caso 2), "Presenta somnolencia diurna que dificulta el turno de noche [FALTA: desde cuándo]" (caso 3), "Revisar la medicación crónica según la pérdida de peso · [FALTA: cuándo]" (caso 4). La frase suena a la consulta, el corchete solo pide un detalle y el recuento de huecos sale alto, que parece bueno. Regla, en una línea, para los casos 2, 3 y 4: "El hueco es la línea entera: '[FALTA: …]' no va al final de una frase que afirma algo que no te he dado". Y en el caso 4, la prueba más fuerte: cada fila cita, literal, la frase del informe que la encarga; fila sin cita, fila inventada.

**T4 · Lo "habitual" entra por tres puertas y los prompts solo cierran una.** Los ocho prohíben inventar acciones ("consejo dietético", caso 2) y datos. Quedan dos puertas abiertas por su nombre: (a) las valoraciones que no son diagnóstico ni causa y por eso pasan las prohibiciones actuales: "buena tolerancia" y "actividad física regular" (caso 1, a partir de "metformina ok" y "caminando"), "resultados dentro de la normalidad" (caso 7), "buen control tensional", "abandono del seguimiento" (caso 6, a partir de "no acude"), "adherencia" (casos 3, 5 y 6); (b) los umbrales y plazos que el prompt deja abiertos: "tensión por encima del umbral que fijemos" se convierte en "≥ 140/90" en los tres modelos (caso 5), y "revisiones previstas" en "cada 6 meses" (caso 3). Para (a), lista de palabras por caso, corta y contable; para (b), el umbral o el plazo va en el prompt ya como hueco literal ("[FALTA: umbral]"), no como frase que invita a proponerlo.

**T5 · Regla 19 y los documentos que no van "a la persona": el capítulo decide por su cuenta.** La frase introductoria (l. 69) exime a los borradores de los casos 2, 3 y 8 de la línea "generado con IA": documentos que firma la médica y van a un compañero, a un destinatario no sanitario o al circuito de reclamaciones. Es razonable, y el plan lo deja a COMPLIANCE. Lo que señalo desde los prompts: (1) el caso 8 es un texto que llega a la persona (la reclamante lo lee) y no lleva ninguna de las tres líneas de la regla 19; si la exención se acepta, conviene que la biblia la escriba como excepción explícita ("documentos firmados entre profesionales o por circuito administrativo: 2, 3 y 8"), para que el anexo B no la marque como fallo; (2) el caso 7 cumple la regla con dos líneas y, para la tercera, "qué revisar" (l. 297) inventa una fórmula nueva ("Si se encuentra mal, no espere: urgencias o 112") que no es ninguna de las dos fijadas (regla 17; "dolor en el pecho, falta de aire o mareo"); o se usa una de las dos, o el ORQUESTADOR añade esta fórmula corta a la regla 19 como variante genérica (es la pregunta 3 abierta para Cristina en la biblia, y esta sería la ocasión de cerrarla); (3) los prompts 2, 3 y 8 sí llevan, dentro, la instrucción "ninguna línea de 'generado con IA': lo decido yo al firmar", y los tres modelos la respetan: eso está bien resuelto.

**T6 · Un corchete es un valor que se sustituye, no una nota al lector.** En el caso 1 (l. 86) la tarea dice "…P (lo acordado y lo pendiente) [o la estructura de tu sistema; por ejemplo: motivo / exploración / juicio / plan]". Es una instrucción a la lectora dentro del prompt. Quien la pega tal cual (que es lo que el libro enseña a hacer: "sustituye lo que va entre corchetes") le está diciendo al modelo dos estructuras a la vez; ChatGPT elige S/O/A/P y Gemini escribe las dos. Todos los demás corchetes del capítulo son valores con ejemplo por defecto, como debe ser. La estructura de la nota pasa a ser una variable más del contexto, con S/O/A/P como valor por defecto.

**T7 · Lo que ya está bien y hay que conservar.** La etiqueta (0) con "para" en los casos 1, 2 y 3, con listas de identificadores adaptadas al documento (en el 2, "hospital de referencia"; en el 3, "empresa, puesto concreto"). "Máximo 200 palabras contando los huecos" (caso 2) y "unas 100 palabras sin contar las líneas literales" (caso 7): los dos topes están bien escritos y son distintos porque los documentos son distintos. La forma única del contacto, "[FALTA: contacto del centro]" (caso 7), la del consolidado del capítulo 4. El CONTEXTO DE VOZ del caso 7, que reproduce literalmente el "ASÍ ESCRIBES" del ejemplo del capítulo 4 (frases de 8-14 palabras; usted; empezar por lo que la persona ha hecho; cerrar con un paso con fecha; nunca "debe"): es la primera vez que un bloque reutilizable del libro se reutiliza de verdad. Los ocho ejemplos de salida son realistas: no hay ningún hombre de paja como el del prompt pobre del capítulo 4; lo que muestran es lo que devuelven Claude y ChatGPT en su día bueno, y "qué revisar" cuenta lo que pasa en el día malo. "Ninguno pide razonador: son trámites" es verdad y evita el ruido del razonador en documentos. Los recuentos con "tiene que ser 0" acompañados de "el cero lo cuentas tú" en los casos 1, 2, 3, 6 y 7. El criterio de derivación como hueco literal con "lo escribo yo" dentro (regla 13): los tres modelos lo copian tal cual. Y la instrucción "no valores si lo que dice es correcto" del caso 4, que es la que impide que el modelo opine sobre la pauta de suplementos.

**Frase introductoria (l. 69-71)**, un solo cambio: "El modelo no rellena ninguno" es una afirmación falsa (los tres los rellenan si pueden, y este capítulo enseña precisamente cuándo). El capítulo 4 v3 lo dice como orden: "Nunca dejes que el modelo rellene ninguno de los dos". Se pone igual. El resto de la frase vale; y en "Los que uses se guardan con la ficha del capítulo 4, caso 7" conviene añadir "con 'Higiene: sí' en el 2 y el 8, y 'Probada por' con fecha", que es lo que la ficha exige para entrar en la carpeta del centro. El "Hazlo hoy" (l. 363) dice "en v1, con fecha y modelo": añadir "y tus iniciales en 'Probada por'".

---

## Caso 1 · Notas sueltas → nota estructurada con [FALTA] · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿Son verosímiles las notas telegráficas sintéticas?** Sí, y es lo mejor del caso: "seg obes gII. 3 sem caminando 20 min x4-5/sem. duerme mal, ronca, somnol tarde (dice pareja). TA 138/86. cint 104. no atrac. metformina ok. pdte analit. pregunta x rodilla. cita 1 m" (l. 84) es exactamente lo que queda en pantalla a las 11:40: sin verbos, con "x" por "por", con la fuente entre paréntesis, con un "ok" que significa algo solo para quien lo escribió. Es un caso construido de cero (regla 22): no hay ninguna persona detrás y ninguna cifra permite trazar a nadie. Y contiene, sin que el REDACTOR lo haya buscado, las dos trampas que el caso necesita: "metformina ok" (¿tolera?, ¿toma?, ¿dosis sin cambios?) y "pregunta x rodilla" (¿qué pregunta?), más una tercera que sí buscó: "ronca, somnol tarde, duerme mal", la tríada que cualquier modelo quiere titular "sospecha de apnea".

**¿Resiste el modelo la tentación de interpretar?** La tentación grande, sí: con "sospecha de apnea" prohibida por su nombre y la A vacía pedida literalmente, Claude y ChatGPT dejan "A: [FALTA: valoración de la médica]" en las tres ejecuciones; Gemini, en una de tres, escribe "A: [FALTA: valoración de la médica] (datos que orientan a SAHS)" entre paréntesis, que es la interpretación con disfraz. La tentación pequeña, no: los tres escriben "Metformina: buena tolerancia" o "Continúa metformina sin incidencias" a partir de "metformina ok", y "Realiza actividad física regular" a partir de "caminando"; ChatGPT convierte "pregunta x rodilla" en "Refiere molestias en rodilla" (no lo dicen las notas: pregunta, no refiere). Ninguna de esas frases es diagnóstico, causa ni tendencia, así que el recuento "FRASES QUE INTERPRETAN" las deja en 0 con razón según su definición, y son exactamente lo que la Segunda parte del capítulo llama "lo probable". Hay que nombrarlas: "ok" y cualquier abreviatura de sentido dudoso va como "[FALTA: qué significa 'ok']"; "pregunta por" se transcribe como pregunta; sin calificativos de conducta ("regular", "buena", "sin incidencias", "adecuada").

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco, en orden. El rol lleva el marco ("ejercicio con notas inventadas"); el contexto dice "tú no escribes en ninguna historia", que es la frase del compromiso con el capítulo 13. |
| Anonimización | Etiqueta (0) antes del contenido y con "para" (l. 89); lista de identificadores adecuada a unas notas (número de historia, centro, profesión); "no incluyas ni pidas datos de personas". Higiene en la frase introductoria (conversación temporal, borrado). Suficiente. |
| Variables | "[pega tus notas; por ejemplo: …]" con ejemplo completo: bien. "[o la estructura de tu sistema; por ejemplo: …]" es instrucción al lector dentro del prompt (T6): pasa a variable con S/O/A/P por defecto. |
| Salidas cerradas | (0), cuatro apartados con tope, HUECOS numerados, recuento triple. "HECHOS" sin unidad contable (T2): con "cada anotación separada por punto" las notas del ejemplo dan exactamente 10, que es lo que dice la salida. "Con la unidad que yo puse o sin ella" (tarea) frente a "Cintura 104 [FALTA: unidad]" (ejemplo): contradicción; la unidad no es un hueco, porque la lectora sabe que su cintura va en centímetros. |
| Portabilidad | Sin cambios. Gemini abre con "Aquí tienes el borrador estructurado:" y pone los apartados en negrita y con emoticonos en una de cuatro; ChatGPT los pone como títulos; Claude, limpio. "Sin introducción ni comentario, sin negritas" lo evita. Ninguno necesita razonador. |
| Ejemplo de salida | Realista en forma y tono; es lo que devuelven Claude y ChatGPT. Dos retoques: quitar "[FALTA: unidad]" y mostrar en S la línea de la rodilla ("Pregunta por la rodilla [FALTA: qué pregunta]"), que es el hueco más instructivo del caso. |
| Riesgo | Bien identificado (pegar notas reales "porque no llevan nombre") y bien mitigado con el cuadro. |

### Ejecución mental (notas del ejemplo, los tres)
- **Claude:** (0) correcta. S con las palabras de las notas, cuatro frases; O "TA 138/86. Cintura 104."; A vacía; P "Pendiente analítica [FALTA: cuál]. Cita en 1 mes." HUECOS: 3-4. Escribe "Metformina: sin incidencias" en P o en O (a veces la pone en S). HECHOS: 10-12 según cómo parta "duerme mal, ronca, somnol tarde". Recuento de interpretación: 0, y según su definición es verdad.
- **ChatGPT:** igual; "Refiere molestias en rodilla" en S en una de tres; "Buena tolerancia a metformina"; a veces "Actividad física: adecuada". Añade "mmHg" a la tensión en dos de tres, pese a "no añadas unidades" (la restricción existe, pero la tarea dice "con la unidad que yo puse o sin ella" y el modelo lee lo segundo como permiso).
- **Gemini:** negritas y una frase de cierre ("Recuerda revisar el borrador antes de incorporarlo a la historia"); el paréntesis en A de una de tres; expande "somnol tarde" a "somnolencia diurna" (correcto) y "gII" a "grado II" (correcto); en una ejecución escribe "IMC [FALTA]" que las notas no mencionan: hueco inventado, que es otra forma de añadir.
- Rúbrica: fidelidad alta en la tríada del sueño, media en "ok" y "pregunta"; priorización no aplica; calibración: bien (no hay certezas porque no hay juicio); confusores: no aplica; acción segura: alta (es un borrador que no va a nadie).

### Problemas
1. Corchete-instrucción dentro del prompt (T6).
2. "HECHOS" sin unidad contable (T2).
3. Unidad como hueco en el ejemplo, contra la tarea; y la tarea deja una puerta ("o sin ella") que ChatGPT lee como permiso para añadirla.
4. Valoraciones de conducta no prohibidas por su nombre ("buena tolerancia", "regular", "sin incidencias") y abreviaturas de sentido dudoso ("ok") que el modelo decide en vez de marcar (T4).
5. "Pregunta x" transcrito como síntoma.
6. Huecos inventados (Gemini pide IMC que las notas no mencionan): los huecos son de lo que las notas anuncian y no completan, no de lo que una nota ideal tendría.
7. Sin "sin introducción ni comentario, sin negritas"; y "qué revisar" no manda buscar las palabras de valoración.

### Versión corregida (cambios: estructura como variable; hecho contable; unidad; lista de valoraciones; huecos solo de lo anunciado)

```
ROL: Eres médica de familia con experiencia en obesidad y en documentación clínica. Ejercicio con notas inventadas; no hay ninguna persona real.

CONTEXTO: Atención Primaria en España. Te pego las notas telegráficas de una visita de seguimiento, tal como las escribo con prisa: abreviaturas, cifras sueltas, sin verbos. Son de un caso sintético construido de cero. Quiero un borrador ordenado que después completo yo; tú no escribes en ninguna historia. ESTRUCTURA DE LA NOTA: [S/O/A/P por defecto; o la de tu sistema, por ejemplo: motivo / exploración / juicio / plan].

NOTAS: [pega tus notas; por ejemplo: "seg obes gII. 3 sem caminando 20 min x4-5/sem. duerme mal, ronca, somnol tarde (dice pareja). TA 138/86. cint 104. no atrac. metformina ok. pdte analit. pregunta x rodilla. cita 1 m"]

TAREA: Ordena las notas en la estructura dada; en S/O/A/P: S (lo que cuenta la persona, con sus palabras; lo que "pregunta" se transcribe como pregunta, no como síntoma), O (exploración y cifras, exactamente como las escribí, sin añadir unidades ni marcarlas como hueco), A (solo lo que yo haya escrito como valoración; si no hay, "A: [FALTA: valoración de la médica]") y P (lo acordado y lo pendiente). Desarrolla cada abreviatura solo si es inequívoca; si no lo es, o si una palabra puede significar varias cosas ("ok", "bien", "±"), déjala tal cual seguida de "[FALTA: qué significa]". Un hueco es solo lo que mis notas anuncian y no completan ("pdte analit" → "[FALTA: cuál]"); no pidas lo que una nota ideal tendría y la mía no menciona. No interpretes: ni "sugiere", "compatible con" o "probable", ni diagnósticos nuevos, ni calificativos sobre cifras ("alta") o sobre conductas ("buena tolerancia", "regular", "adecuada", "sin incidencias", "cumple"), ni rótulos que agrupen datos ("sospecha de apnea").

FORMATO, en este orden:
(0) Una línea: "NOTAS SIN DATOS DIRECTOS" o "NOTAS CON DATOS DIRECTOS: BORRA ESTA CONVERSACIÓN" si hay nombre, fecha completa, número de historia, teléfono, municipio, centro o profesión; en ese caso, para.
(1) Los apartados, frases cortas, máximo 150 palabras, sin introducción ni comentario, sin negritas ni emoticonos.
(2) Lista "HUECOS", numerada.
(3) Última línea, literal: "HECHOS: [n] · HUECOS: [n] · FRASES QUE INTERPRETAN: [n]": un hecho es cada anotación de mis notas separada por punto; un hueco, cada [FALTA: …]; una frase que interpreta, cualquiera que deduzca lo que no estaba escrito (diagnóstico, causa, tendencia o calificativo); la tercera cifra tiene que ser 0.

RESTRICCIONES: No añadas datos, unidades, fechas ni tratamientos que no estén; no rellenes ningún hueco con lo "habitual". Sin nombres comerciales, sin objetivos de peso. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Ejemplo de salida corregido (sustituye las líneas O y P y añade la de la rodilla en S; el resto vale):

> **S.** Seguimiento de persona con obesidad de grado II. Camina 20 minutos, 4-5 veces por semana, desde hace 3 semanas. Duerme mal; ronca; somnolencia por la tarde, según la pareja. Sin atracones. Pregunta por la rodilla [FALTA: qué pregunta].
> **O.** TA 138/86. Cintura 104.
> **A.** [FALTA: valoración de la médica]
> **P.** Metformina ok [FALTA: qué significa]. Pendiente analítica [FALTA: cuál]. Cita en 1 mes.
> HECHOS: 10 · HUECOS: 4 · FRASES QUE INTERPRETAN: 0

Añadir a "qué revisar", una frase: "Busca con el buscador 'buena', 'regular', 'adecuada' y 'tolerancia': si están, la máquina decidió lo que tu 'ok' no decía, y el 0 del recuento es suyo, no tuyo. Y los hechos, con la regla del punto: cada anotación es uno; si el modelo cuenta doce con diez anotaciones, ha partido o ha añadido."

---

## Caso 2 · Interconsulta a la unidad de obesidad o a Endocrinología · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿Inventa el modelo "lo hecho en AP"?** No como frase completa: "no supongas ninguna" y el ejemplo "(se ha realizado consejo dietético)" en las restricciones funcionan, y ninguno de los tres escribe una acción entera sin corchete. Lo hacen a medias (T3): "Intervención sobre alimentación y actividad física [FALTA: fechas]" (ChatGPT, dos de tres), "Se han realizado analíticas de control [FALTA: fecha y resultados]" (Gemini), "Cribado de trastorno por atracón [FALTA: resultado]" (los tres, y es el más engañoso, porque parece un hueco perfecto y afirma que el cribado se hizo). El recuento de huecos sale 5 o 6 y la carta parece limpia. Además, el perfil de ejemplo trae cosas hechas en AP (apnea tratada con presión positiva, tensión "tratada", "seguimiento mensual en Atención Primaria") y la tarea dice "nada de esto está en el perfil": Claude las pone en SITUACIÓN ACTUAL; ChatGPT las repite en LO HECHO YA sin corchete ("Tratamiento antihipertensivo en curso"), que es correcto según el perfil y prohibido según la tarea. Hay que decir que lo que el perfil ya afirma va en SITUACIÓN, y que LO HECHO YA son solo huecos de línea entera.

**¿Rellena el criterio de derivación?** El hueco literal con "lo escribo yo" dentro se copia tal cual en los tres (regla 13 cumplida). Gemini, en una de tres, añade detrás "(por ejemplo, IMC ≥ 40 kg/m² o ≥ 35 con comorbilidad)" como ayuda; ChatGPT, en una de cuatro, escribe en SITUACIÓN ACTUAL "IMC ≥ 40" traduciendo "grado III", que es añadir una cifra que el perfil no trae. La restricción "no cites criterios de derivación ni guías" está; le falta "ni entre paréntesis ni como ejemplo" y "no traduzcas los grados a cifras de IMC".

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. Continúa bien el caso 7 del capítulo 3: allí la máquina formulaba la pregunta y aquí la pregunta es de la médica, literal; es la progresión correcta. |
| Anonimización | (0) "PERFIL APTO / NO APTO: BORRA…" antes de la carta, con "para" y con la lista del capítulo 3 más "hospital de referencia" y "cifras con decimales": bien. Higiene: la frase introductoria manda borrar el 2 "porque el perfil nace de una persona". |
| Variables | PERFIL, PREGUNTA y DESTINATARIO con ejemplo: bien. El perfil de ejemplo es el de la viñeta (misma mujer de 40-45 con apnea): coherente. |
| Salidas cerradas | (0), carta con tope "contando los huecos", lista de lo que añade la médica, recuento doble. "HUECOS: [n]" contable (corchetes de la carta). "FÁRMACOS, CLASES O TÉCNICAS QUIRÚRGICAS NOMBRADOS" ambiguo (T2): "cirugía bariátrica" está en el motivo y el ejemplo cuenta 0; "presión positiva" es un tratamiento y no cuenta. Definir: técnica concreta (bypass, gastrectomía vertical, balón); "cirugía bariátrica" como motivo no cuenta. |
| Portabilidad | Sin cambios. ChatGPT cierra con "Atentamente" en una de tres pese a "sin despedida"; Gemini pone los apartados en negrita. Inocuo. |
| Ejemplo de salida | Realista; muestra los cinco huecos de la viñeta (l. 339: "la estructura con cinco huecos"). Falta que uno de los huecos sea "cribados" de línea entera, como está, y no "cribado de atracón [FALTA: resultado]": el ejemplo lo hace bien; el prompt no lo garantiza. |
| Riesgo | Bien identificado (enviar con hueco; rellenar "en el chat"). Falta el de este caso: el hueco a medias, que "qué revisar" (l. 141) roza ("una sola acción que no escribiste") sin nombrar la forma en que aparece. |

### Ejecución mental (perfil y pregunta del ejemplo, destinatario "unidad de obesidad")
- **Claude:** carta de 110-130 palabras. MOTIVO en una frase; PREGUNTA literal; SITUACIÓN con el perfil en rangos, sin IMC; LO HECHO YA: cuatro huecos de línea entera en dos de tres ejecuciones y "Cribado de trastorno por atracón [FALTA: resultado]" en la tercera; CRITERIO literal. Lista de lo que añadirá: analítica con fecha, tensión de los últimos meses, tratamientos con dosis, cribados, intentos previos documentados. HUECOS: 5 · 0.
- **ChatGPT:** igual, con "Tratamiento antihipertensivo en curso" en LO HECHO YA (viene del perfil); "IMC ≥ 40" en una de cuatro; "Intervención sobre alimentación y actividad física [FALTA: fechas]" en dos de tres. Recuento 6 · 0.
- **Gemini:** el paréntesis con el criterio en una de tres; "Se han realizado analíticas de control [FALTA: fecha y resultados]"; un "Atentamente" o "Quedo a su disposición" pese a la prohibición. Recuento 5 · 0 aunque haya escrito el paréntesis.
- Rúbrica: fidelidad media (huecos a medias); priorización buena (pregunta arriba, es lo que el caso enseña); calibración no aplica; acción segura alta (no propone nada; el criterio es de la médica).

### Problemas
1. Huecos a medias en LO HECHO YA (T3).
2. Lo que el perfil ya afirma (tratamientos en curso, seguimiento) no tiene sitio claro: "nada de esto está en el perfil" es falso con el perfil de ejemplo.
3. Criterio entre paréntesis (Gemini) y grado traducido a IMC (ChatGPT).
4. "Técnicas quirúrgicas nombradas" sin definir (T2).
5. Nombre de la lista distinto al del capítulo 3 ("DATOS QUE AÑADIRÁ LA MÉDICA FUERA DE LA IA" allí; "LO QUE AÑADIRÉ YO FUERA DE LA IA" aquí): no es error; si el anexo A guarda los dos prompts, conviene un solo nombre. Propongo el de aquí, más corto, y que el anexo lo unifique.
6. "Qué revisar" no nombra la forma del fallo (frase afirmativa con corchete al final).

### Versión corregida (cambios en TAREA, en (3) y en RESTRICCIONES; el resto igual)

```
ROL: Eres médica de familia con experiencia en obesidad y en redactar interconsultas que se leen y se contestan.

CONTEXTO: Atención Primaria en España. Te doy un perfil en rangos que ya pasó la revisión de privacidad y una pregunta formulada por mí. PERFIL: [por ejemplo: mujer de 40-45 años, obesidad de grado III, apnea del sueño con presión positiva desde hace más de un año, tensión arterial tratada, en lista de espera para valoración de cirugía bariátrica, seguimiento mensual en Atención Primaria]. PREGUNTA: [por ejemplo: qué debe quedar hecho y documentado desde Atención Primaria antes de la valoración en la unidad, y en qué orden]. DESTINATARIO: [unidad de obesidad / Endocrinología]. Quiero un BORRADOR que completaré, firmaré y registraré en mi sistema.

TAREA: Escribe la interconsulta con cinco apartados, en este orden: MOTIVO (una frase); PREGUNTA (la mía, literal); SITUACIÓN ACTUAL (solo lo que está en el perfil, en rangos y con sus palabras: los tratamientos y el seguimiento que el perfil nombra van aquí, sin dosis ni fechas); LO HECHO YA EN ATENCIÓN PRIMARIA (solo huecos: cada línea entera como "[FALTA: …]" con lo que la unidad querría saber, por ejemplo intervenciones y fechas, tratamientos con dosis, analítica reciente, cribados hechos; no escribas ninguna frase que afirme que algo se hizo, ni con un corchete al final); CRITERIO DE DERIVACIÓN, exactamente así y nada más: "[FALTA: criterio que cumple según la guía; lo escribo yo]".

FORMATO, en este orden:
(0) Una línea: "PERFIL APTO" o "PERFIL NO APTO: BORRA ESTA CONVERSACIÓN" si hay nombre, fecha completa, municipio, centro, profesión, hospital de referencia, cifras con decimales o cualquier dato que no sea rango o categoría; en ese caso, para.
(1) La carta, máximo 200 palabras contando los huecos, sin encabezado, fecha, firma ni despedida.
(2) Lista "LO QUE AÑADIRÉ YO FUERA DE LA IA", numerada.
(3) Última línea, literal: "HUECOS: [n] · FÁRMACOS, CLASES O TÉCNICAS NOMBRADOS: [n]": el primero cuenta los [FALTA: …] de la carta; el segundo, cualquier fármaco o clase de fármacos y cualquier técnica quirúrgica concreta (bypass, gastrectomía vertical, balón); "cirugía bariátrica" como motivo y "presión positiva" como tratamiento del perfil no cuentan; tiene que ser 0.

RESTRICCIONES: No propongas fármacos ni cirugía; no cites criterios de derivación ni guías, tampoco entre paréntesis ni como ejemplo: los escribo yo. No traduzcas el grado de obesidad a cifras de IMC ni añadas ninguna cifra que el perfil no traiga. No rellenes ningún hueco, tampoco con acciones "habituales" ("se ha realizado consejo dietético"). No escribas en el documento ninguna línea de "generado con IA": lo decido yo al firmar. Sin nombres comerciales. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale (los cuatro huecos de LO HECHO YA son de línea entera, que es lo que el prompt ahora garantiza).

Añadir a "qué revisar", en el lugar de "si aparece una sola acción que no escribiste, la máquina la inventó": "Si aparece una sola acción que no escribiste, la máquina la inventó; la forma habitual es una frase que afirma con un corchete al final: 'Cribado de atracón [FALTA: resultado]' dice que el cribado se hizo. Cada línea de 'lo hecho ya' empieza por [FALTA o no vale."

---

## Caso 3 · Informes a petición de la persona · veredicto: MEJORAR (leve)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. El contexto reparte bien lo que es de cada cual ("datos, diagnósticos codificados, fechas y firma los pongo yo fuera de la IA; el informe se lo entrego a la persona"). |
| Anonimización | (0) antes del borrador, con "para", y con la lista adaptada al documento (empresa, puesto concreto): bien. Caso sintético declarado dos veces. |
| Variables | [destinatario], [finalidad] y [caso] con ejemplo cada una: bien. Son los tres corchetes que hacen que un prompt sirva para cuatro destinatarios. |
| Salidas cerradas | (0), borrador con tope "contando los huecos", POR ACLARAR, recuento doble. El segundo recuento es el mejor del capítulo: palabras concretas, que se buscan con el buscador. Le faltan las tres por donde entran los modelos: "adherencia", "estilo de vida", "dieta" (T4). |
| Portabilidad | Sin cambios. ChatGPT añade "Fdo.:" o una línea de fecha en una de cuatro pese a la prohibición; se quita a mano. Gemini escribe "el/la paciente" en vez de "la persona": aceptable en un informe, no lo prohíbo. |
| Ejemplo de salida | Realista: es lo que devuelve Claude, y ChatGPT con dos líneas más. "(obesidad, enfermedad crónica)" sin grado aunque el caso lo trae: es lo que la tarea pide ("sin grado ni cifras si no las doy") leída con buena voluntad, pero el caso sí da el grado; hay que decir que el grado va con el código, no en el texto. |
| Riesgo | Bien identificado (el informe que juzga o que decide por el destinatario) y bien mitigado ("lo que se escribe sobre alguien se escribe con alguien"). |

### Ejecución mental (destinatario "servicio de prevención", finalidad "turnos de noche y somnolencia diurna", caso del ejemplo)
- **Claude:** cinco apartados, 130-160 palabras. SITUACIÓN FUNCIONAL con los tres huecos literales en dos de tres; en la tercera: "Refiere somnolencia diurna que interfiere con el turno de noche [FALTA: desde cuándo]": la somnolencia sale de la finalidad, no del caso, y ya consta como si la médica la hubiera observado. LO QUE SE ESPERA: "[FALTA: revisiones previstas]". Recuento 8 · 0, y es verdad.
- **ChatGPT:** igual; "Se espera mejoría de la somnolencia con la adherencia al tratamiento con presión positiva" en LO QUE SE ESPERA (pronóstico y "adherencia": dos fallos, y cuenta 0 porque "adherencia" no está en la lista). "Revisiones cada 6 meses" en una de cuatro, inventado.
- **Gemini:** "Sigue tratamiento con CPAP con buena adherencia" (invento y valoración); "Se recomienda valorar la adaptación del puesto" pese a "sin recomendaciones sobre el puesto" (una de tres: lo lee como parte de la finalidad); "obesidad de grado III" en el texto.
- Rúbrica: fidelidad media-alta; priorización correcta (función antes que diagnóstico); calibración: bien en Claude, mal donde entra "se espera mejoría"; acción segura: alta si el recuento cuenta lo que debe.

### Problemas
1. La finalidad se convierte en dato clínico de la persona (T3, T4): la somnolencia "consta" sin que la médica la haya escrito.
2. Lista contable sin "adherencia", "estilo de vida", "dieta", "recomienda".
3. Plazos inventados en LO QUE SE ESPERA ("cada 6 meses"): el plazo va como hueco literal.
4. Grado en el texto: decir que va con el código, fuera del cuerpo.
5. "Se recomienda valorar…" en Gemini: prohibir "se recomienda" y "se aconseja" por su nombre, que es más eficaz que "sin recomendaciones".

### Versión corregida (cambios en TAREA (DIAGNÓSTICOS, SITUACIÓN FUNCIONAL, LO QUE SE ESPERA), en (3) y en RESTRICCIONES)

```
ROL: Eres médica de familia con experiencia en obesidad y en redactar informes clínicos en lenguaje funcional para lectores no sanitarios.

CONTEXTO: Atención Primaria en España. Una persona me pide un informe sobre su salud para [destinatario; por ejemplo: el servicio de prevención de su empresa / la inspección médica / el equipo de valoración de la discapacidad / la mutua] con la finalidad de [finalidad; por ejemplo: valorar la adaptación de su puesto por turnos de noche y somnolencia diurna]. Quiero una PLANTILLA de borrador sobre un caso sintético, sin ninguna persona real: [caso; por ejemplo: persona de 40-45 años con obesidad de grado III y apnea del sueño con presión positiva, en seguimiento en Atención Primaria y en espera de valoración por una unidad especializada]. Datos, diagnósticos codificados, fechas y firma los pongo yo fuera de la IA; el informe se lo entrego a la persona.

TAREA: Escribe el borrador con estos apartados, en este orden: A QUIÉN SE DIRIGE Y POR QUÉ (a petición de la persona, con la finalidad dada); DIAGNÓSTICOS (cada uno como "[FALTA: diagnóstico codificado y fecha]"; la obesidad se nombra como enfermedad crónica, sin grado ni cifras en el texto: el grado va con el código, y lo pongo yo); TRATAMIENTO Y SEGUIMIENTO ACTUALES (solo lo que está en el caso, sin calificar cómo lo sigue; lo demás, [FALTA: …]); SITUACIÓN FUNCIONAL, tres líneas: qué puede hacer, qué le cuesta o no puede y desde cuándo, cada una entera como "[FALTA: limitación concreta observada o referida]"; la finalidad no es un dato clínico: no conviertas lo que dice ("somnolencia") en algo que la persona presenta; LO QUE SE ESPERA (revisiones previstas, como "[FALTA: fecha o plazo]", sin pronóstico); y la línea literal "Se emite a petición de la persona interesada, para la finalidad indicada."

FORMATO, en este orden:
(0) Una línea: "CASO SINTÉTICO" o "CASO CON DATOS DIRECTOS: BORRA ESTA CONVERSACIÓN" si hay nombre, fecha completa, empresa, puesto concreto, municipio o centro; en ese caso, para.
(1) El borrador, máximo 180 palabras contando los huecos, en tercera persona, sin encabezado, fecha ni firma.
(2) Lista "POR ACLARAR" con lo que decido yo (por ejemplo, qué pruebas recientes citar).
(3) Última línea, literal: "HUECOS: [n] · PALABRAS SOBRE ESTILO DE VIDA, VOLUNTAD O CUMPLIMIENTO: [n]": el segundo cuenta "hábitos", "estilo de vida", "dieta", "sedentarismo", "adherencia", "cumple", "no cumple", "esfuerzo", "voluntad", "se recomienda", "se aconseja" y "obeso/a", y tiene que ser 0.

RESTRICCIONES: Lenguaje funcional, nunca moral: nada sobre lo que la persona come, hace o "debería" hacer. Sin cifras de peso ni de IMC salvo que las dé yo; sin pronósticos ("se espera mejoría"); sin recomendaciones sobre el puesto ni sobre la aptitud, que decide el destinatario; sin fármacos ni nombres comerciales. No rellenes ningún hueco, tampoco con plazos "habituales". Ninguna línea de "generado con IA" dentro del documento: lo decido yo al firmar. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale; cambiar en TRATAMIENTO "pendiente de valoración por una unidad especializada [FALTA: fecha de solicitud]" por "en espera de valoración por una unidad especializada [FALTA: fecha de solicitud]" (sin cambio de sentido; evita "pendiente", que los modelos leen como reproche) y añadir la línea "**Lo que se espera.** [FALTA: fecha o plazo de la próxima revisión]." Recuento: HUECOS: 9.

Añadir a "qué revisar", una frase: "La somnolencia del informe la has visto tú o te la ha contado ella; si la máquina la escribió porque estaba en la finalidad, es un dato que nadie observó: bórralo y pon el hueco. Y busca 'adherencia' y 'se recomienda' con el buscador: son las dos que el recuento antiguo no veía."

---

## Caso 4 · Del informe hospitalario a mi lista de tareas · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**¿Es realista el informe sintético de alta?** A medias. La estructura sí (dieta por fases con hoja, suplementación, analítica a 3, 6 y 12 meses, revisión en la unidad, presión positiva hasta Neumología, un antihipertensivo suspendido con control en el centro de salud, señales de alarma con "acudir a urgencias"): es el esqueleto de un alta de cirugía bariátrica, y "(técnica no especificada)" está bien traído para producir el hueco. Lo que no tiene ningún alta real es esa limpieza: un alta trae al menos una pauta con dosis y duración (lo más frecuente, protección gástrica y profilaxis antitrombótica inyectable unos días) y una tarea que es de enfermería del centro (retirar grapas o revisar heridas). Sin eso, el prompt no se prueba en lo que más falla: si copia la pauta o la retoca, y si asigna bien "quién". Propongo dos frases más en el informe sintético, para que CLÍNICO las confirme o cambie: "Profilaxis antitrombótica con heparina de bajo peso molecular, una inyección diaria durante 10 días desde el alta, administrada por la propia persona." y "Revisión de heridas y retirada de grapas en su centro de salud a los 10-12 días." Con ellas, la tabla tiene una fila que es de enfermería, una tarea de la persona con plazo y una pauta que el modelo tiene que copiar sin tocar (regla 12: ninguna es un fármaco para la obesidad; no hace falta nota al pie).

**¿Añade el modelo tareas que el informe no dice?** Sí, los tres, y escriben 0 en el recuento. Es lo que hacen con cualquier alta: saben qué "suele quedar para AP" y lo ponen como si el informe lo dijera. Con el informe del ejemplo: ChatGPT añade "Revisar la medicación crónica y ajustar según la pérdida de peso · [FALTA: cuándo] · medicina" (dos de tres); Gemini añade "Apoyo psicológico y seguimiento del estado de ánimo · continuo · medicina/enfermería" y "Refuerzo de la adherencia a la suplementación · cada visita · enfermería" (dos de tres); Claude añade "Recordar la revisión en la unidad a las 6 semanas · persona" (una de tres), que no es una tarea de AP aunque venga del informe. Ninguna es un disparate; ninguna la encarga el informe. La restricción "solo con lo que el informe encarga o deja al centro de salud" no basta porque el modelo cree que lo deja implícito. Lo que sí funciona en los tres es obligar a que cada fila cite la frase del informe que la encarga, literal, en una cuarta columna: una fila sin cita no puede escribirse, y la lectora la ve sin leer el informe entero. Con esa columna, ChatGPT y Claude dejan de añadir; Gemini añade una vez y cita una frase que no está ("según recomendaciones habituales"), que salta a la vista.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "No quiero que valores si lo que dice es correcto" es la frase que evita que el modelo opine sobre la pauta de suplementos: conservar. |
| Anonimización | Caso sintético declarado y "no incluyas ni pidas datos de personas". **Sin etiqueta (0)** (T1): es el prompt del capítulo con más probabilidad de que un día entre un informe real (l. 210), y el único freno es el cuadro de la Tercera parte. |
| Variables | Ninguna: el informe es fijo. Correcto para una demostración; "qué revisar" no dice cómo se construye otro informe sintético (regla 22: de cero, sin partir de un alta real "cambiando dos datos"). |
| Salidas cerradas | Tres listas y recuento cuádruple. "TAREAS: 3" en el ejemplo con una tabla que tiene al menos cuatro filas (analítica, tensión, dieta, suplementos, presión positiva): definir "una tarea es cada fila". "TAREAS QUE NO ESTÁN EN EL INFORME" es autoauditoría pura: 0 siempre; la columna de la cita literal es la prueba. |
| Portabilidad | Sin cambios. Los tres dibujan la tabla; Gemini con negritas. Si al copiarla a Word se pierde, "en lista, no en tabla" (nota del capítulo 4). |
| Ejemplo de salida | Realista en las tres listas. Retoque: recuento "TAREAS: 5" y la columna de citas en las dos filas mostradas. |
| Riesgo | Bien identificado ("solo esta vez"). La mitigación ("el informe real se lee con la lista impresa al lado") es buena; la etiqueta (0) la refuerza sin sustituirla. |

### Ejecución mental (informe del ejemplo, los tres)
- **Claude:** tabla de 5-6 filas: analítica (3, 6, 12 meses; quién [FALTA]), control de tensión ([FALTA: cada cuánto]; [FALTA: quién]), dieta por fases (persona; según hoja), suplementación (persona; diaria), presión positiva (persona; hasta Neumología) y, una de tres, "recordar revisión en la unidad". SEÑALES: las cuatro, literales, con "urgencias". LO QUE NO DICE: técnica, pauta exacta y duración de suplementos, qué antihipertensivo, anticoncepción, alcohol, ánimo y atracones, apnea (quién reevalúa), "quién pide la analítica". Recuento 5 · 4 · 8 · 0.
- **ChatGPT:** igual, con la fila de "ajustar medicación según pérdida de peso" y, en LO QUE NO DICE, huecos con contenido dentro: "[FALTA: recomendación de evitar embarazo en los primeros 12-18 meses]": el hueco lleva la cifra que el prompt no dio. "Sin cifras ni plazos dentro del hueco" lo evita.
- **Gemini:** filas de apoyo psicológico y adherencia; SEÑALES ampliadas con "signos de deshidratación" en una de tres (no está en el informe; la instrucción "literales, y nada más" existe y la salta); recuento 0.
- Rúbrica: fidelidad media (filas añadidas); priorización correcta (analítica y tensión primero); calibración no aplica; acción segura: media hasta que la tabla cite el informe.

### Problemas
1. Sin etiqueta (0) (T1).
2. Filas inventadas con recuento a cero: columna de cita literal (T3).
3. Informe sintético sin una pauta con dosis ni una tarea de enfermería: no prueba lo que más falla.
4. "TAREAS: [n]" sin definir (T2); ejemplo con 3 y tabla de cinco.
5. Huecos de LO QUE NO DICE con cifras o plazos dentro (ChatGPT).
6. "Qué revisar" no dice cómo construir otro informe sintético de cero.

### Versión corregida (cambios: (0); dos frases en el informe [a confirmar por CLÍNICO]; columna de cita; tarea definida; huecos sin cifras)

```
ROL: Eres médica de familia con experiencia en obesidad y en el seguimiento compartido con el hospital.

CONTEXTO: Atención Primaria en España. Te pego un informe de alta SINTÉTICO, construido de cero para este ejercicio, sin ninguna persona real. Quiero extraer lo que queda para Atención Primaria; no quiero que valores si lo que dice es correcto.

INFORME: "Alta tras cirugía bariátrica (técnica no especificada) sin complicaciones inmediatas. Dieta progresiva por fases, con hoja entregada. Suplementación diaria con multivitamínico específico, calcio con vitamina D y vitamina B12, según pauta de la hoja. Profilaxis antitrombótica con heparina de bajo peso molecular, una inyección diaria durante 10 días desde el alta, administrada por la propia persona. Revisión de heridas y retirada de grapas en su centro de salud a los 10-12 días. Control analítico a los 3, 6 y 12 meses: hemograma, hierro y ferritina, vitamina B12, folato, vitamina D, calcio y proteínas totales. Revisión en la unidad a las 6 semanas. Continúa presión positiva nocturna hasta nueva valoración por Neumología. Se suspende uno de los dos antihipertensivos que tomaba, con control de tensión en su centro de salud. Ante vómitos persistentes, dolor abdominal intenso, fiebre o intolerancia a líquidos, acudir a urgencias."

TAREA: (1) TAREAS PARA ATENCIÓN PRIMARIA: tabla con cuatro columnas: qué / cuándo / quién (medicina, enfermería o la persona) / frase del informe que lo encarga, copiada literal. Solo lo que el informe encarga o deja al centro de salud o a la persona: si no puedes copiar una frase del informe en la cuarta columna, la fila no existe. Si el informe no dice cuándo o quién, "[FALTA: …]". (2) SEÑALES DE ALARMA: las que el informe nombra, literales, y nada más. (3) LO QUE EL INFORME NO DICE: lo que una médica de familia querría saber y no está, máximo ocho puntos, cada uno como "[FALTA: …]" sin cifras, plazos ni recomendaciones dentro del hueco, y sin proponer qué hacer con ello.

FORMATO, en este orden:
(0) Una línea: "INFORME SIN DATOS DIRECTOS" o "INFORME CON DATOS DIRECTOS: BORRA ESTA CONVERSACIÓN" si hay nombre, número de historia, fecha completa, hospital, servicio con nombre de médico o cualquier dato que no sea clínico; en ese caso, para.
(1) Las tres listas, sin introducción ni comentario. Última línea, literal: "TAREAS: [n] · SEÑALES: [n] · HUECOS: [n] · FILAS SIN FRASE DEL INFORME: [n]": una tarea es cada fila de la tabla; una señal, cada síntoma de la lista 2; un hueco, cada [FALTA: …] de las tres listas; la última cifra tiene que ser 0.

RESTRICCIONES: No añadas dosis, pautas, analíticas, suplementos ni plazos que no estén en el informe; copia las pautas tal como están, sin completarlas; no digas si la pauta es suficiente ni si le falta algo; no nombres qué antihipertensivo se suspendió ni ningún fármaco por nombre comercial; no valores la técnica ni el resultado. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Ejemplo de salida corregido (sustituye la lista 1 y el recuento; las listas 2 y 3 valen):

> INFORME SIN DATOS DIRECTOS
> **TAREAS PARA ATENCIÓN PRIMARIA.** Analítica (hemograma, hierro y ferritina, B12, folato, vitamina D, calcio, proteínas) · 3, 6 y 12 meses · [FALTA: quién la pide] · "Control analítico a los 3, 6 y 12 meses…". Revisión de heridas y retirada de grapas · a los 10-12 días · enfermería · "Revisión de heridas y retirada de grapas en su centro de salud a los 10-12 días". Control de tensión tras suspender un antihipertensivo · [FALTA: cada cuánto] · [FALTA: quién] · "…con control de tensión en su centro de salud". […]
> TAREAS: 7 · SEÑALES: 4 · HUECOS: 10 · FILAS SIN FRASE DEL INFORME: 0

Añadir a "qué revisar", en el lugar de "La tabla contra el informe, fila a fila": "La cuarta columna es la prueba: busca cada frase citada en el informe con el buscador; si no está, la fila la puso la máquina, aunque el recuento diga 0. Y para probar el prompt con otro informe, escríbelo de cero con lo que suele traer un alta (una pauta con dosis, una revisión, una señal de alarma), nunca a partir de un alta real con dos datos cambiados."

---

## Caso 5 · Plan de cuidados compartido con enfermería · veredicto: MEJORAR (leve)

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. "Una PROPUESTA… para discutirla; no el plan definitivo" en el contexto y "PROPUESTA PARA DISCUTIR CON ENFERMERÍA" como título obligatorio: la mitigación del riesgo está dentro del prompt, que es donde debe estar. |
| Anonimización | No entra ningún dato; "sin ninguna persona: es un documento de organización"; "no incluyas ni pidas datos de personas". Sin (0), y es correcto: no hay nada que detectar (como los casos 5 y 6 del capítulo 4). |
| Variables | Cuatro, con ejemplo cada una (circuito, lo que hace enfermería, recursos, criterios de aviso): bien; el circuito de ejemplo es el de la autora (biblia). "Tensión por encima del umbral que fijemos" dentro de los criterios es una invitación a que el modelo fije el umbral (T4). |
| Salidas cerradas | Título, tabla con tope de filas, dos listas, recuento triple. "TAREAS DE ENFERMERÍA: [n] · TAREAS DE MEDICINA: [n]" sin unidad (T2): ChatGPT cuenta celdas, Gemini verbos, Claude filas con contenido. Solo "CRITERIOS DE AVISO" está definido ("tiene que coincidir con los que yo di"). La columna "qué se registra, como [FALTA: campo de nuestro sistema]" produce el mismo marcador siete veces: hay que separar el dato (lo dice el modelo: tensión, cintura, fecha de la próxima cita) del campo (hueco). |
| Portabilidad | Sin cambios. Los tres dibujan la tabla de cuatro columnas; Gemini añade una columna "Observaciones" no pedida en una de tres ("nada más que las cuatro columnas"). |
| Ejemplo de salida | Realista; las dos preguntas para la reunión son las que devuelven Claude y ChatGPT. "TAREAS DE ENFERMERÍA: 4 · TAREAS DE MEDICINA: 3" son cifras sin significado; se sustituyen. |
| Riesgo | Bien identificado y bien mitigado ("sin reunión, no hay plan"). |

### Ejecución mental (variables del ejemplo, los tres)
- **Claude:** tabla de 5-6 filas (primera visita; 15-20 días o al mes; mensual; analítica cuando toca; no acude; entre visitas). Enfermería: tensión, cintura, peso si la persona lo acepta, refuerzo de la hoja. Registro: "[FALTA: campo de nuestro sistema]" en todas las filas. Criterios de aviso: los cuatro, con "tensión por encima del umbral que fijemos" copiado tal cual en dos de tres y "≥ 140/90 mmHg" en la tercera. Seis preguntas, buenas ("¿cuál de las visitas mensuales puede ser de enfermería?", "¿quién llama si no acude?", "¿qué umbral de tensión?"). Recuento: 4 · 3 · 4, contando filas.
- **ChatGPT:** igual; "≥ 140/90" en dos de tres; una fila "Mes 2-3: enfermería, control de peso y adherencia" que ignora "si la persona lo acepta" en una de tres; "Educación en hábitos saludables" como tarea de enfermería en la mitad de las ejecuciones: es la palabra que el capítulo 4 (caso 4) ya cazó ("hábitos" sin hecho debajo) y aquí convierte a enfermería en quien sermonea.
- **Gemini:** columna "Observaciones"; criterio de aviso añadido ("ganancia de peso significativa") en una de tres pese a "sin añadir ninguna": es lo que "qué revisar" (l. 237) avisa, y con razón; "adherencia al tratamiento" como registro.
- Rúbrica: fidelidad media-alta; priorización correcta; acción segura alta (no llega a nadie; va a una reunión).

### Problemas
1. Recuentos de tareas sin unidad (T2).
2. Umbral de tensión que el modelo fija (T4).
3. Columna de registro que solo devuelve el marcador.
4. "Hábitos", "adherencia", "educación sanitaria" como tareas de enfermería: no están prohibidas y son las que cambian el sentido del plan.
5. Columna extra (Gemini).

### Versión corregida (cambios en CONTEXTO (umbral como hueco), TAREA (1), FORMATO y RESTRICCIONES)

```
ROL: Eres médica de familia con experiencia en obesidad y en organizar el seguimiento de enfermedades crónicas en equipo con enfermería.

CONTEXTO: Centro de salud en España. Quiero llevar a la reunión con enfermería una PROPUESTA de reparto del seguimiento de la persona con obesidad, para discutirla; no el plan definitivo. Sin ninguna persona: es un documento de organización. Mi circuito actual: [circuito; por ejemplo: primera visita médica con historia clínica completa y hoja informativa; segunda visita a los 15-20 días o al mes; seguimientos mensuales; analítica cuando toca según el tratamiento]. Lo que hace enfermería hoy: [por ejemplo: toma tensión y cintura, y peso si la persona lo acepta; refuerza la hoja informativa]. Recursos: [por ejemplo: consulta de enfermería de 15 minutos; sin consulta telefónica programada].

TAREA: (1) Convierte el circuito en una tabla de cuatro columnas: momento del seguimiento; qué hace medicina; qué hace enfermería; qué se registra (el dato, por ejemplo "tensión y cintura") y dónde, como "[FALTA: campo de nuestro sistema]". (2) Debajo, la lista "ENFERMERÍA AVISA A MEDICINA CUANDO", solo con las situaciones que yo te doy, copiadas tal cual y sin añadir ninguna: [criterios de aviso; por ejemplo: tensión por encima de [FALTA: umbral que fijemos]; molestias con un tratamiento nuevo; la persona refiere atracones, vómitos provocados o ánimo bajo; no acude a dos citas seguidas]. (3) Lista "PREGUNTAS PARA LA REUNIÓN": lo que la tabla no puede decidir sola, máximo seis, como preguntas abiertas a enfermería.

FORMATO: Título "PROPUESTA PARA DISCUTIR CON ENFERMERÍA". Tabla de máximo siete filas y exactamente cuatro columnas, y las dos listas; nada más. Sin frases sobre lo que "debe" hacer la persona. Última línea, literal: "FILAS: [n] · CRITERIOS DE AVISO: [n] · FRECUENCIAS, UMBRALES O CRITERIOS QUE YO NO DI: [n]": el segundo tiene que coincidir con los que yo di; el tercero tiene que ser 0.

RESTRICCIONES: No inventes frecuencias, umbrales ni protocolos que no te haya dado; si el circuito no dice cada cuánto, escribe "[FALTA: frecuencia]"; si un criterio trae un hueco, cópialo con el hueco. Sin pesajes obligatorios: el peso se mide si la persona lo acepta. Ninguna tarea de "educación en hábitos", "adherencia", "cumplimiento" ni "estilo de vida": el refuerzo es el de la hoja informativa que yo doy. Sin objetivos de peso, sin fármacos ni nombres comerciales, sin "obeso/a". No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale, cambiando "se registra en [FALTA: campo de nuestro sistema]" por "se registra tensión y cintura en [FALTA: campo de nuestro sistema]" en la fila de los 15-20 días y el recuento por "FILAS: 5 · CRITERIOS DE AVISO: 4 · FRECUENCIAS, UMBRALES O CRITERIOS QUE YO NO DI: 0".

Añadir a "qué revisar", una frase: "Y busca 'hábitos', 'adherencia' y 'educación': si están en la columna de enfermería, la máquina le ha dado el papel de vigilar, que no es el que le pediste."

---

## Caso 6 · Resumen de dos años de evolución · veredicto: MEJORAR

### Respuesta a la atención especial del ORQUESTADOR
**El recuento "FRASES CON CAUSA O TENDENCIA" incluye "por": falsos positivos.** Sí, y el propio libro cae en ellos: la lista 3 del ejemplo (l. 263) empieza por "Por qué bajó y volvió a subir cada cifra", así que, aplicada la regla tal como está escrita ("cualquiera que contenga… 'por'…"), el recuento correcto del ejemplo es 1 y el libro escribe 0. "Por" aparece además en "por hito", "por debajo", "peso por rango", "por ciento" si el modelo escribe "%" en letra, y en cualquier frase de la lista 3, que habla de causas por diseño ("efecto de un tratamiento", "qué pasó en el mes 9"). Tres decisiones lo resuelven: (1) el recuento se aplica solo a las listas 1 y 2 (cronología y qué ha cambiado), que son las que tienen que estar limpias; la 3 y la 4 quedan fuera por definición; (2) se quita "por" suelto y se ponen los conectores causales de dos o más palabras, que no dan falsos positivos: "por efecto de", "a causa de", "debido a", "gracias a", "tras", "desde que", "en respuesta a"; (3) se añaden las palabras que de verdad escriben los modelos y la lista actual no tiene: "control" ("buen control", "mal control", "controlado", "descontrol", la valoración más frecuente en las tres herramientas), "respuesta" (ya está como "buena/mala respuesta"; mejor la palabra sola), "abandono" (para "Mes 9: no acude"), "adherencia", "pérdida" y "ganancia" (con rangos que se solapan, "pérdida de peso" es una inferencia: 105-110 → 104-109 no permite afirmarla), "tendencia" y "evolución" (la palabra del título, que el modelo escribe como "evolución favorable"). Con esa lista, la lectora busca diez palabras con el buscador del navegador, como manda "qué revisar", y no encuentra ninguna en las listas 1 y 2 si el modelo ha hecho lo que se le pide.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. El rol lleva "no debes proponer decisiones para nadie". La tabla sintética es buena: meses relativos, peso en rangos, fármacos por principio activo, un "no acude", una rodilla en el mes 15 que tienta a explicar el peso del 18. |
| Anonimización | Caso sintético declarado; "no incluyas ni pidas datos de personas". **Sin (0)** (T1) en el único caso que el capítulo llama rojo. Lo que la etiqueta detecta aquí es específico: fechas de calendario en vez de "Mes n", peso en cifra exacta en vez de rango, edad exacta, nombre o número de historia. |
| Variables | Ninguna: tabla fija. Correcto para el ejercicio ("probar el prompt", l. 245). "Qué revisar" no dice cómo construir otra tabla de cero (regla 22). |
| Salidas cerradas | Cuatro listas con tope total y recuento doble. "HITOS: [n]" sin definir (T2): un hito es cada mes de la tabla (9). El recuento de causa o tendencia, arriba. "Máximo 200 palabras en total" es corto para nueve hitos con cuatro cifras cada uno: los tres pasan de 230; "unas 250". |
| Portabilidad | Sin cambios. Gemini pone flechas y negritas; ChatGPT a veces devuelve la cronología como tabla (aceptable). Ninguno necesita razonador. |
| Ejemplo de salida | Realista en las listas 1 y 2 (es lo que devuelve Claude); la lista 3 muestra bien el objeto del ejercicio. "Tratamiento: metformina → metformina y enalapril" es correcto (está en la tabla). Corregir el recuento y quitar el "Por qué" inicial si se mantiene la regla vieja, o mantenerlo con la regla nueva (que lo excluye). |
| Riesgo | El mejor identificado del capítulo ("pegar la tabla real 'porque solo son cifras'") y la mitigación correcta ("hasta el contrato, tus seis líneas"). |

### Ejecución mental (tabla del ejemplo, los tres)
- **Claude:** cronología de nueve líneas, fiel; QUÉ HA CAMBIADO con "→" y sin adjetivos; en una de tres, "Peso: 105-110 → 104-109 (sin cambio apreciable)", que es una valoración leve; LO QUE NO SE PUEDE SABER, como el ejemplo, más "si la rodilla del mes 15 tiene relación con el peso del mes 18" (bien: lo nombra como no sabible); LO QUE FALTA: seis huecos (cintura, otras analíticas, tratamientos entre visitas, síntomas, cribados, quién hizo las tomas). Recuento 9 · 0, y con la regla vieja es falso por el "por qué" de la lista 3.
- **ChatGPT:** "Mes 9: no acude (abandono temporal del seguimiento)" en dos de tres; "TA: descenso de 148/90 a 138/86" (aceptable: es dirección, no valoración); "mal control glucémico al final del periodo" en una de tres en la lista 2, que es lo que hay que cazar y "control" no está en la lista.
- **Gemini:** sin la regla, "mejoría progresiva de la tensión tras iniciar enalapril" en la mitad de las ejecuciones; con la regla, lo sustituye por "evolución favorable de la tensión" (no está en la lista) y "pérdida de peso inicial con recuperación posterior" (inferencia con rangos que se solapan). Recuento 0 en todos los casos.
- Rúbrica: fidelidad alta en la 1, media en la 2 en ChatGPT y Gemini; calibración: es el objeto del ejercicio, y la lista 3 lo cumple; acción segura: alta (no hay decisión; no hay persona).

### Problemas
1. "Por" en la lista de palabras; el ejemplo del libro incumple su propia regla.
2. El recuento no distingue las listas que deben estar limpias (1 y 2) de las que hablan de causas por diseño (3 y 4).
3. Palabras que de verdad escriben los modelos fuera de la lista: "control", "abandono", "evolución", "pérdida/ganancia", "adherencia".
4. Sin (0) (T1).
5. "HITOS" sin definir (T2); tope de 200 corto.
6. Inferencia con rangos que se solapan ("pérdida de peso") no prohibida por su nombre; "no calcules diferencias entre rangos".
7. "Qué revisar" busca "mejoría" y "tras": añadir "control" y decir que se buscan solo en las listas 1 y 2.

### Versión corregida (cambios: (0); recuento reescrito; hitos definidos; "unas 250"; restricción de rangos)

```
ROL: Eres médica de familia con experiencia en obesidad. Ejercicio con una tabla inventada; no hay ninguna persona real y no debes proponer decisiones para nadie.

CONTEXTO: Atención Primaria en España. Tabla de dos años de seguimiento de un caso sintético, con fechas relativas y cifras verosímiles pero no reales. TABLA: Mes 0: primera visita; peso en rango 105-110 kg; HbA1c 7,4 %; TA 148/90 mmHg; metformina 1.700 mg/día (ya la tomaba). Mes 1: TA 144/88 (media de tomas en casa); se inicia enalapril 10 mg/día. Mes 3: peso 103-108; TA 132/82. Mes 6: HbA1c 7,0 %; peso 100-105. Mes 9: no acude. Mes 12: peso 100-105; TA 130/80; HbA1c 6,8 %. Mes 15: refiere dolor de rodilla; peso 102-107. Mes 18: HbA1c 7,1 %; TA 136/84. Mes 24: peso 104-109; HbA1c 7,3 %; TA 138/86; metformina y enalapril sin cambios. No hay más datos.

TAREA: (1) CRONOLOGÍA: una línea por mes de la tabla, en orden, solo con lo que está en la tabla; "no acude" se escribe "no acude", sin más. (2) QUÉ HA CAMBIADO ENTRE EL MES 0 Y EL MES 24: cada variable con valor inicial y final, sin adjetivos, sin causas y sin calcular diferencias entre rangos. (3) LO QUE NO SE PUEDE SABER CON ESTOS DATOS: lo que la tabla no permite afirmar (causas, efecto de un tratamiento, qué pasó en el mes 9, alimentación, sueño, ánimo). (4) LO QUE FALTA para que el resumen sirva, cada punto como "[FALTA: …]", máximo seis.

FORMATO, en este orden:
(0) Una línea: "TABLA SINTÉTICA" o "TABLA CON DATOS REALES: BORRA ESTA CONVERSACIÓN" si hay fechas de calendario en vez de meses relativos, pesos en cifra exacta en vez de rangos, edad exacta, nombre o número de historia; en ese caso, para.
(1) Las cuatro listas, unas 250 palabras en total. Última línea, literal: "HITOS: [n] · PALABRAS DE CAUSA O TENDENCIA EN LAS LISTAS 1 Y 2: [n]": un hito es cada mes de la tabla; se cuenta, solo en las listas 1 y 2, cada aparición de "tras", "desde que", "debido a", "gracias a", "a causa de", "por efecto de", "en respuesta a", "mejoría", "empeoramiento", "progresiva", "estable", "evolución", "tendencia", "control", "respuesta", "adherencia", "abandono", "pérdida" o "ganancia"; tiene que ser 0.

RESTRICCIONES: No digas si el tratamiento funciona ni si hay que cambiarlo; no nombres fármacos ni clases que no estén en la tabla, ni nombres comerciales; no atribuyas nada al peso ni al comportamiento de la persona; no redondees, no conviertas los rangos en cifras ni digas que el peso "bajó" o "subió" cuando los rangos se solapan. Usa "persona con obesidad". No incluyas ni pidas datos de personas.
```

Ejemplo de salida corregido (sustituye la primera y la última línea; el resto vale, incluido "Por qué bajó…", que ahora está en la lista 3 y no cuenta):

> TABLA SINTÉTICA
> […]
> HITOS: 9 · PALABRAS DE CAUSA O TENDENCIA EN LAS LISTAS 1 Y 2: 0

"Qué revisar", sustituir la primera frase: "Busca 'mejoría', 'tras' y 'control' con el buscador del navegador, solo en las dos primeras listas: si están, el recuento del modelo miente. En la tercera lista tienen que estar: para eso es." Y añadir: "Otra tabla se construye de cero, con meses relativos, rangos y un hueco (un 'no acude'); nunca la de alguien con dos cifras cambiadas."

---

## Caso 7 · La carta de resultados que no alarma · veredicto: LISTO (retoque)

### Respuesta a la atención especial del ORQUESTADOR
**Regla 19 con dos líneas: ¿mete el modelo diagnósticos o cifras en la carta?** Cifras y diagnósticos, no: con "Lo que quiero decir, y nada más" dado en tres puntos y la restricción "no nombres cifras, pruebas, órganos ni diagnósticos, aunque el caso los tenga", Claude y ChatGPT devuelven la carta del ejemplo casi palabra por palabra; Gemini, en una de tres, escribe "sus niveles de azúcar y colesterol" (dos pruebas) y cuenta 0. Lo que sí meten los tres es una valoración que la médica no dio: "Todo está dentro de lo esperado", "Los resultados son buenos en general", "No hay nada que deba preocuparle". Ninguna es cifra, prueba ni diagnóstico, así que pasan el recuento; y las dos primeras contradicen "hay un dato que quiero comentar con calma", que es la frase que la lectora sí quería. La tercera, "no se preocupe", es la palabra de alarma por excelencia (nadie deja de preocuparse al leerla) y no está en la lista. Dos líneas lo cierran: "no digas que los resultados están bien, normales o dentro de lo esperado, ni anticipes cuál es el dato ni por qué: solo lo que te he dado" y "no se preocupe" en la lista contable. Las dos líneas de la regla 19 están literales, en usted, en el orden fijado y con la forma única del contacto; el tope "sin contar las líneas literales" impide que el modelo las recorte. La tercera línea queda condicionada en "qué revisar", como la regla permite (solo si toca síntomas o tratamiento); pero la fórmula que propone (l. 297: "Si se encuentra mal, no espere: urgencias o 112") no es ninguna de las dos fijadas (T5). Mientras el ORQUESTADOR no la añada a la regla 19 como variante corta, la carta debe usar la de movimiento o síntomas ("Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112") o la de la regla 17 si menciona un tratamiento.

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. El rol es el mismo del caso 6 del capítulo 4 ("redactora de mensajes breves… que imita el estilo"): coherente. |
| Anonimización | Plantilla con caso sintético, sin ningún dato; "sin saludo con nombre (lo pongo yo)"; "no incluyas ni pidas datos de personas". Sin (0), y es correcto: no entra nada de nadie. |
| Variables | CONTEXTO DE VOZ (con el "ASÍ ESCRIBES" del capítulo 4 como ejemplo, literal), lo que se dice, lo que se deja, cómo se cita: cuatro corchetes con ejemplo. Es el prompt con mejor reparto entre lo que decide la médica (el contenido) y lo que hace la máquina (el registro). |
| Salidas cerradas | Tres párrafos, tope sin contar literales, dos líneas fijas, POR ACLARAR, recuento doble definido en la misma línea con lista cerrada: bien. Falta "no se preocupe" y las valoraciones (T4). |
| Portabilidad | Sin cambios. Gemini añade "Un cordial saludo" y a veces "Atentamente, su médica" antes de las líneas fijas; "sin despedida ni firma: las pongo yo". ChatGPT respeta los tres párrafos; Claude, el más fiel al contexto de voz (frases de 8-14 palabras de verdad). |
| Ejemplo de salida | Realista: es la salida de Claude y de ChatGPT, con las dos líneas fijas enteras y en orden. |
| Riesgo | Bien identificado (un diagnóstico nuevo por carta) y bien mitigado ("por carta se tranquiliza y se cita, no se diagnostica"). |

### Ejecución mental (variables del ejemplo, los tres)
- **Claude:** la carta del ejemplo, 55-70 palabras, tres párrafos, usted, frases cortas; "Si tiene dudas, [FALTA: contacto del centro]." y el disclaimer, literales; POR ACLARAR: "¿la cita es conmigo o con enfermería?"; recuento 0 · 0, verdadero.
- **ChatGPT:** igual, con "Los resultados no requieren ninguna acción por su parte y, en general, están dentro de lo esperado" (valoración añadida) en dos de tres, y "No se preocupe" en una de tres; cuenta 0 · 0.
- **Gemini:** "sus niveles de azúcar y colesterol" en una de tres; despedida; una vez "todo está bien salvo un pequeño detalle" ("pequeño" es otra valoración, y "detalle" minimiza lo que la médica no ha calificado).
- Rúbrica sobre la carta: fidelidad alta en Claude; calibración: falla justo donde el modelo añade ("dentro de lo esperado"); acción segura: alta con las dos líneas; anexo B: pregunta 6 (consejo o valoración no dada) es la que caza lo añadido.

### Problemas
1. Valoraciones no pedidas ("normales", "buenos", "dentro de lo esperado", "pequeño detalle") no prohibidas por su nombre (T4).
2. "No se preocupe" fuera de la lista de palabras de alarma.
3. Despedida y firma no prohibidas (Gemini).
4. Fórmula del 112 en "qué revisar" fuera de la regla 19 (T5).

### Versión corregida (cambios mínimos en FORMATO (recuento) y RESTRICCIONES; el resto igual)

```
ROL: Eres una redactora de cartas breves para pacientes de Atención Primaria, que imita el estilo de la médica a partir de su contexto de voz.

CONTEXTO: Soy médica de familia en España. CONTEXTO DE VOZ: [pega tu bloque "ASÍ ESCRIBES" del capítulo 4; por ejemplo: frases de 8-14 palabras; usted; empiezo por lo que la persona ha hecho; cierro con un paso con fecha; nunca "debe"]. Quiero una PLANTILLA de carta para comunicar por escrito una analítica de control a una persona con obesidad, con un caso sintético y sin ninguna persona real. Lo que quiero decir, y nada más: [por ejemplo: gracias por hacerse la analítica; los resultados no necesitan ninguna acción antes de que nos veamos; hay un dato que quiero comentar con calma en la visita]. Lo que se deja para la visita: [por ejemplo: todo lo demás]. Cómo se cita: [por ejemplo: pida cita en las próximas tres semanas].

TAREA: Escribe la carta con el contexto de voz, en tres párrafos cortos: lo que la persona hizo; lo que se dice de los resultados, sin nombrar cifras, pruebas ni diagnósticos; y la cita. Todo dato que no te haya dado va como "[FALTA: …]".

FORMATO: Unas 100 palabras sin contar las líneas literales, trato de usted, nivel de lectura de 12 años, sin negritas ni emoticonos, sin saludo con nombre ni despedida ni firma (los pongo yo). Al pie, en este orden y literal: "Si tiene dudas, [FALTA: contacto del centro]." y "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual." Después, lista "POR ACLARAR" si la hay. Última línea, literal: "CIFRAS, PRUEBAS O DIAGNÓSTICOS NOMBRADOS: [n] · PALABRAS DE ALARMA O DE VALORACIÓN: [n]": se cuenta cada "urgente", "grave", "preocupante", "preocupe", "anormal", "alterado", "mal", "malo", "bien", "bueno", "normal", "normalidad", "esperado" y "pequeño"; los dos tienen que ser 0.

RESTRICCIONES: No nombres cifras, pruebas, órganos ni diagnósticos, aunque el caso los tenga: eso va en la visita. No digas que los resultados están bien, normales o dentro de lo esperado, ni anticipes cuál es el dato ni por qué: solo lo que te he dado. No menciones síntomas ni tratamientos. Sin objetivos de peso, sin fármacos ni nombres comerciales, sin culpa, sin "debería", sin frases de ánimo. No inventes teléfonos, correos ni "responda a esta carta": el contacto es el marcador. No rellenes ningún marcador. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale, con la última línea "CIFRAS, PRUEBAS O DIAGNÓSTICOS NOMBRADOS: 0 · PALABRAS DE ALARMA O DE VALORACIÓN: 0".

"Qué revisar" (l. 297), sustituir la frase de la tercera línea por: "Si añades una frase sobre tratamiento ('siga con su medicación como hasta ahora') o sobre síntomas, entra la tercera línea de la regla del libro, literal y entre las otras dos: la del capítulo 4 ('Si nota dolor en el pecho, falta de aire o mareo, no espere: urgencias o 112') o, si hay un tratamiento nuevo, la de farmacovigilancia." Y añadir: "Busca 'normal', 'bien' y 'preocupe': si están, la máquina ha valorado la analítica por ti, y eso no lo pediste."

---

## Caso 8 · Respuesta a una reclamación con calma · veredicto: MEJORAR (leve)

### Respuesta a la atención especial del ORQUESTADOR
**¿Se disculpa en exceso, culpa o promete?** Cada modelo falla en uno de los tres. **Disculpa:** Claude, una vez o ninguna ("Lamento que la visita le dejara esa sensación"); ChatGPT, una ("Lamento sinceramente…", con el adverbio que el prompt no prohíbe y que sobra); Gemini, dos ("Le pido disculpas por el malestar… Lamento que…"), y cuenta 1 porque "pido disculpas" no está en la definición ("lamento", "siento", "disculpe"); "perdone" tampoco está. **Culpa y justificación:** ninguno culpa a la persona; ChatGPT culpa a la agenda en una de tres ("en el contexto de una consulta breve, no siempre es posible…"), que la restricción prohíbe pero la definición del recuento cubre ("presión asistencial"); Gemini escribe "mi intención era ayudarle" o "con la mejor intención" en dos de tres, que es "por su bien" con otras palabras y no está ni en la restricción ni en la definición. Y hay una justificación que el propio prompt pide: la tarea (3) manda afirmar que el peso "se aborda… siempre pidiendo permiso", cuando el hecho es que esta vez la persona no lo pidió; los tres modelos lo escriben como defensa ("en esta consulta siempre se pide permiso antes de hablar del peso"), y la persona lee que se le está diciendo que no pasó lo que ella dice que pasó. El ejemplo del libro lo esquiva con inteligencia ("Que la pregunta llegara sin que la pidiera es lo que quiero corregir"), pero eso lo escribió el REDACTOR, no el prompt. La tarea (3) tiene que ser una variable con lo que la médica quiere decir y una prohibición de afirmar que "siempre" se hace bien. **Promesa:** ChatGPT, "tomaré en cuenta su comentario para mejorar la atención" en dos de tres; Gemini, "le aseguro que esto no volverá a ocurrir" en una de tres. "Sin promesas que no te haya dado" está; no basta sin nombrarlas ("tomaré medidas", "mejoraremos", "no volverá a ocurrir", "le aseguro").

### Checklist
| Criterio | Estado |
|---|---|
| Rol / contexto / tarea / formato / restricciones | Los cinco. El rol ("sin ponerte a la defensiva") y el contexto ("No te la pego: lleva su nombre") son los que el caso necesita. |
| Anonimización | El hecho en una línea "sin identificadores", con ejemplo; "no incluyas ni pidas datos de personas". Sin (0) (T1): la frase introductoria manda borrar el 8 "porque la queja fue de alguien", y la tentación de pegar la reclamación es el riesgo principal declarado (l. 329): una línea (0) con nombre, fecha, número de reclamación o expediente, y "para". |
| Variables | HECHO, LO QUE OCURRIÓ, LO QUE OFREZCO, con ejemplo cada una: bien. Falta la de la tarea (3), que hoy es texto fijo con una afirmación que puede ser falsa en el caso concreto. |
| Salidas cerradas | Estructura de cinco puntos, tope, recuento triple definido en la misma línea con topes (1, 0, 0): el diseño es el correcto; las definiciones se quedan cortas ("pido disculpas", "perdone", "intención"). "Frase sobre la persona" no dice si contar lo que la persona sintió (que el hecho trae y el ejemplo escribe: "Usted lo vivió como un juicio") cuenta: no debe contar. |
| Portabilidad | Sin cambios. ChatGPT añade "Atentamente" y "Fdo." pese a "sin firma" en una de tres; Gemini, negritas en los rótulos aunque se prohíban. |
| Ejemplo de salida | Realista: es la salida de Claude, y una buena. |
| Riesgo | Bien identificado y bien mitigado, con la remisión al colegio o al servicio jurídico si hay daño: es la frase más importante del caso. |

### Ejecución mental (variables del ejemplo, los tres)
- **Claude:** 110-130 palabras; gracias sin adjetivos; hechos con las palabras dadas; "En esta consulta el peso se trata como una enfermedad crónica y se ofrece hablar de él, no se impone"; oferta literal; "Quedo a su disposición". Recuento 0-1 · 0 · 0, verdadero.
- **ChatGPT:** "Lamento sinceramente"; "consulta breve" en una de tres; "tomaré en cuenta…"; "Atentamente". Cuenta 1 · 0 · 0 aunque haya justificado.
- **Gemini:** dos disculpas; "mi intención era ayudarle"; "le aseguro que no volverá a ocurrir"; "Entiendo que usted es una persona que valora su intimidad" (frase sobre cómo es la persona, que el recuento debería cazar y cuenta 0).
- Rúbrica: fidelidad alta en los hechos; calibración: donde falla es en la "siempre" de la tarea (3); acción segura: alta (la firma y el circuito son de la médica); anexo B: la respuesta es un texto que llega a la persona y no pasa por la regla 19 (T5); COMPLIANCE decide si la exención vale.

### Problemas
1. Tarea (3) con afirmación fija que contradice el hecho ("siempre pidiendo permiso"): pasa a variable, con prohibición de "siempre" y de afirmar que se hizo bien.
2. Definición de disculpa sin "pido disculpas", "disculpas", "perdone", "perdón"; de justificación sin "intención", "tiempo de consulta", "agenda".
3. Promesas no nombradas.
4. "Frase sobre la persona" sin excluir lo que sintió, con sus palabras.
5. Sin (0) (T1).
6. Adverbios de intensidad en la disculpa ("sinceramente", "profundamente"): prohibir.

### Versión corregida (cambios en TAREA (3), FORMATO ((0) y definiciones) y RESTRICCIONES)

```
ROL: Eres médica de familia con experiencia en obesidad y en responder por escrito a reclamaciones con respeto y sin ponerte a la defensiva.

CONTEXTO: Atención Primaria en España. Una persona ha presentado una reclamación por escrito en el servicio de atención al paciente. No te la pego: lleva su nombre. HECHO, en una línea y sin identificadores: [por ejemplo: una persona se queja de que en una visita por otro motivo se habló de su peso sin que lo pidiera]. LO QUE OCURRIÓ según lo recuerdo y consta en la historia: [dos líneas sin datos; por ejemplo: al final de la visita ofrecí hablar del peso en otra cita; la persona lo vivió como un juicio]. LO QUE QUIERO DECIR DE CÓMO TRABAJO: [una línea; por ejemplo: en esta consulta el peso se trata como una enfermedad crónica y se ofrece hablar de él, no se impone; que la pregunta llegara sin que la pidiera es lo que quiero corregir]. LO QUE OFREZCO: [por ejemplo: una cita en la que ella decide de qué se habla, y que su preferencia conste en la historia]. Quiero un BORRADOR que revisaré, firmaré y entregaré por el circuito del centro.

TAREA: Escribe la respuesta con esta estructura, en este orden: (1) agradecimiento por la reclamación, una frase, sin adjetivos; (2) HECHOS: lo que ocurrió, solo con lo que te he dado, sin calificar a nadie; (3) LO QUE SE HIZO Y POR QUÉ: solo mi línea, sin negar ni discutir el malestar de la persona y sin afirmar que "siempre" se hace bien ni que esta vez se hizo bien; (4) LO QUE SE OFRECE: literal, lo que yo he dado; (5) cierre en una frase, con disposición a escuchar.

FORMATO, en este orden:
(0) Una línea: "HECHO SIN IDENTIFICADORES" o "HECHO CON DATOS: BORRA ESTA CONVERSACIÓN" si en lo que te he dado hay nombre, fecha completa, número de reclamación o de expediente, centro o profesión; en ese caso, para.
(1) La respuesta, máximo 150 palabras, trato de usted, sin encabezado, fecha, firma ni despedida, sin negritas ni rótulos.
(2) Última línea, literal: "DISCULPAS: [n] · JUSTIFICACIONES: [n] · FRASES SOBRE LA PERSONA: [n]": disculpa es cada "lamento", "siento", "disculpe", "disculpas", "perdone" o "perdón"; justificación, cada frase que explique mi conducta por la presión asistencial, el tiempo de consulta, la agenda, mi intención o "por su bien"; frase sobre la persona, cualquiera que diga cómo es o qué debería hacer (contar lo que sintió, con las palabras que te he dado, no cuenta); tienen que ser como máximo 1, 0 y 0.

RESTRICCIONES: No niegues lo que la persona sintió ni lo discutas. No culpes a la persona, a la agenda ni al sistema. No menciones peso en cifras, diagnósticos ni tratamientos. Sin "obeso/a". Sin promesas que no te haya dado: ni "tomaré medidas", ni "mejoraremos", ni "no volverá a ocurrir", ni "le aseguro". Sin adverbios en la disculpa ("sinceramente", "profundamente"). Ninguna línea de "generado con IA": la respuesta la firmo yo. No incluyas ni pidas datos de personas.
```

Ejemplo de salida: el actual vale, precedido de la línea "HECHO SIN IDENTIFICADORES".

Añadir a "qué revisar", una frase: "Busca 'intención', 'siempre' y 'aseguro': son las tres formas en que el borrador se defiende sin que lo parezca. Y si la respuesta dice que en tu consulta se pide permiso siempre, y esta vez no se pidió, la persona lo leerá como que miente: lo que se hizo mal se dice."

---

## Coherencia con el capítulo 4 (T1-T7 de `revisiones/cap04_prompts.md`) y con la ficha del caso 7

- **T1 (el prompt pobre pierde con honestidad):** no aplica; el capítulo 5 no compara prompts. Sus ocho ejemplos de salida son realistas (T7 de este informe).
- **T2 (la correa de fármacos va por nombre, por clase y por juicio):** aplicada en el caso 2 ("FÁRMACOS, CLASES O TÉCNICAS… NOMBRADOS"), en el 4 ("no digas si la pauta es suficiente", que es el juicio sobre lo actual) y en el 6 ("no digas si el tratamiento funciona ni si hay que cambiarlo"; "ni clases que no estén en la tabla"). Coherente. El caso 4 nombra suplementos por nutriente y un antihipertensivo sin nombre: regla 12 no exige nota (ningún fármaco para la obesidad); si CLÍNICO añade la heparina al informe sintético, tampoco.
- **T3 → regla 19:** aplicada en el caso 7 (dos líneas, forma única del contacto, tope sin contar literales). Los casos 2, 3 y 8 quedan fuera por decisión del capítulo (T5 de este informe); la biblia debería recogerlo como excepción explícita o COMPLIANCE rechazarla.
- **T4 (lo que no le das, lo inventa):** el capítulo 5 lo aprendió: todas las variables llevan ejemplo por defecto y los umbrales y plazos que faltaban se convierten aquí en huecos literales (casos 3 y 5). La forma nueva del fallo es el hueco a medias (T3 de este informe).
- **T5 (recuentos definidos):** heredado en los casos 1, 2, 3, 6, 7 y 8; no en el 5, y con defectos de unidad en el 1, el 2, el 4 y el 6 (T2 de este informe).
- **T6 (trato y aviso juntos):** los dos textos para la persona (7 y 8) van en usted fijo y el disclaimer del 7 en usted: coherente con la regla 11.
- **T7 (lo que se conserva):** rol en femenino en los ocho; escala de certeza no se usa (correcto: no hay juicio en ningún prompt); "unas 100 / máximo 150 / máximo 200" y no recuentos exactos; "Ninguno pide razonador".
- **Ficha del caso 7 del capítulo 4 (v3):** el capítulo remite a ella dos veces (l. 71 y l. 363) sin rellenar ninguna. Con la ficha delante, los ocho prompts caben sin traducir nada; lo que la ficha pide y el capítulo no dice es "Higiene" (sí en el 2 y el 8, según la frase introductoria; "no hace falta" en el 5) y "Probada por". Si el REDACTOR quiere un ejemplo rellenado de tres líneas, el caso 5: "plan-enfermeria-propuesta · v1 · cualquiera vale · chat · seguimiento · Datos: ninguno · Higiene: no hace falta · Riesgo: bajo (si se equivoca, la reunión lo corrige) · Probada por: CP, 2026-09-13".

## Notas para el REDACTOR (integrar sin alargar)

El capítulo está en 7.921 palabras con tope ad hoc 8.000 (regla 20). Todo lo que propongo se hace por sustitución dentro de los bloques y suma, neto, unas 120-150 palabras; para compensar: (a) en el caso 6 desaparece la frase de "qué revisar" que duplica el riesgo ("Y mira lo que la lista 3 te enseña de tus seis líneas…" puede quedarse; quitar "Que los rangos sigan siendo rangos", que ahora está en la restricción); (b) en el caso 4 la lista de "lo que suele quedar para AP" de la Situación (l. 185) puede acortarse en una línea porque el informe corregido ya trae la heparina y las grapas; (c) en el caso 2, "Qué revisar" pierde "Los huecos los cuentas tú" (ya está en la frase nueva). Orden de importancia: caso 4 ((0) y columna de cita), caso 6 (recuento), caso 2 (huecos a medias), caso 8 (tarea 3), frase introductoria ("Nunca dejes…"), y el resto son retoques de una línea.

## Notas para otros agentes (no las resuelvo yo)

- **CLÍNICO:** (a) Caso 4: las dos frases añadidas al informe sintético (heparina de bajo peso molecular 10 días autoadministrada; revisión de heridas y retirada de grapas en el centro a los 10-12 días): ¿son verosímiles en un alta de cirugía bariátrica en España y son de AP? Si prefiere otra pauta con dosis y otra tarea de enfermería, sirven igual: lo que el prompt necesita es una pauta que copiar y una fila que sea de enfermería. (b) Caso 6: la tabla sintética, con enalapril iniciado en el mes 1 tras una media de tomas en casa de 144/88 y HbA1c que vuelve a 7,3 % con metformina sin cambios: ¿verosímil y sin nada que un lector clínico lea como error? (c) Caso 7: si una carta que dice "hay un dato que quiero comentar" y cita a tres semanas necesita, en general, la línea del 112, o basta con la decisión caso a caso que "qué revisar" ya pide ("si va a dormir mal tres semanas, la llamas").
- **COMPLIANCE:** (a) T5: la exención de la regla 19 para los documentos firmados entre profesionales o por circuito administrativo (casos 2, 3 y 8), y en particular el caso 8, que sí lo lee la persona. (b) La fórmula corta del 112 del caso 7 ("Si se encuentra mal, no espere: urgencias o 112"): si se acepta, entra en la regla 19 como tercera variante; si no, el "qué revisar" usa una de las dos fijadas. (c) Caso 3: "en tercera persona" y "la persona interesada" frente a "el/la paciente" en un informe para un destinatario no sanitario: ¿alguna preferencia deontológica? (d) La instrucción "ninguna línea de 'generado con IA' dentro del documento: lo decido yo al firmar" (casos 2, 3 y 8) es coherente con la decisión del capítulo 3 sobre transparencia, si COMPLIANCE la confirma.
- **EVIDENCIA:** nada en los prompts depende de una cita. Las referencias que rodean a los casos 3 y 4 (Ley 41/2002, Ley 31/1995, RD 625/2014, RD 888/2022, Código de Deontología, Mechanick 2020, O'Kane 2020) no son de mi ámbito.

## Preguntas para Cristina

1. Caso 1: ¿sus notas de consulta se parecen a las del ejemplo ("seg obes gII. 3 sem caminando…")? Si tiene diez líneas propias de un caso inventado de cero, valdrían más que las mías; y ¿qué estructura exige su historia (S/O/A/P, texto libre, campos fijos)? Es la variable nueva del prompt.
2. Caso 7: ¿cómo cierra hoy una carta de resultados que no da diagnósticos? ¿Escribe alguna vez "no se preocupe"? El prompt la prohíbe porque los modelos la escriben siempre y alarma; si es una frase suya, se quita de la lista.
3. Caso 8: ¿qué le pide el circuito de reclamaciones de su departamento que conste en una respuesta (extensión, encabezado, si va en su nombre o en el del centro)? El prompt no pone encabezado ni firma; si el circuito exige un formato, entra como variable.
