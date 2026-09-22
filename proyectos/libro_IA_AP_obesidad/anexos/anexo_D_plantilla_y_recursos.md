# Anexo D · Plantilla de proyecto en siete puntos, el ejemplo de la calculadora y recursos

Montado el 22-09-2026 a partir de las v3; pendiente de la pasada final de la autora.

Este anexo reúne lo que los capítulos 8, 9 y 10 remiten aquí: la plantilla de siete puntos en blanco y el ejemplo rellenado de la calculadora de condición física (capítulo 8), la tabla de lo que cambia de nombre legal al salir de la consulta, la hoja de ruta de 90 días, cómo se monta una comunidad de práctica, las tres listas del reloj, la herramienta nueva en quince minutos y las entradas legales completas del capítulo 10, y una lista de recursos: las fuentes públicas que el libro carga en las herramientas o consulta sin IA. Las marcas [POR ACLARAR] y [VERIFICAR] se conservan tal como están en los capítulos.

---

## 1 · La plantilla de siete puntos, en blanco (capítulo 8, tercera parte)

Antes de escribir una línea de código, una página: siete puntos, cada uno con su pregunta. Los proyectos que no sirven mueren en el punto 3 o en el 5; mejor en la página. El punto 5 es el antídoto del exceso de seguridad: la columna del medio (lo que salió mal) da credibilidad a las otras dos. Si el punto 3 incluye a una persona, el proyecto cambia o se para.

| Punto | La pregunta que hay que contestar | Tu proyecto |
|---|---|---|
| **1 · Problema** | ¿Qué dejo de hacer, o hago mal, por falta de tiempo o de tablas? Con un ejemplo de la semana pasada. | |
| **2 · Herramienta** | ¿Qué máquina lo resuelve: una que conversa, una que calcula o ninguna? ¿Qué versión, cuando escribo esto? | |
| **3 · Datos** | ¿Qué entra, de quién es y qué pasa después con ello? Si hay una persona, el proyecto cambia o se para. | |
| **4 · Solución** | ¿Qué hace, en una frase que entienda una compañera sin haberla visto? | |
| **5 · Validación** | ¿Cómo sé que acierta? Lo comprobado, lo que salió mal y lo que aún no he mirado: tres listas. | |
| **6 · Impacto** | ¿Qué cambia y para quién? Con la cifra medida, o con "estimación mía" delante. | |
| **7 · Escalabilidad** | ¿Puede otro cupo construirlo y usarlo sin mí? ¿Qué le hace falta: el código con licencia, instrucciones, una sesión? ¿Y qué es legalmente si sale de mi consulta: herramienta propia, material didáctico o producto sanitario? | |

Las preguntas son las del capítulo 8, literales; la tercera columna es tuya.

---

## 2 · El ejemplo rellenado: la calculadora de condición física (capítulo 8, caso 1)

Las instrucciones y la auditoría son mías; el código lo escribió el modelo y lo aloja [POR ACLARAR: quién; si escribió o corrigió código, es coautor y se dice]. La licencia con la que se comparte [POR ACLARAR: licencia elegida], porque sin licencia un repositorio público se puede mirar, no usar. La plantilla rellenada, con las cifras que tengo y las que no:

| Punto | La calculadora |
|---|---|
| **1 · Problema** | Interpretar tres tablas me costaba unos veinte minutos por informe (estimación mía): dejé de hacer la prueba de la silla. |
| **2 · Herramienta** | Un asistente que escribe código; Streamlit, para publicarla como página web. Comprueba la versión vigente. |
| **3 · Datos** | En la IA: las tablas publicadas y mis instrucciones. En la app: edad en años, sexo, talla y resultado; sin nombre ni fecha, y no se guardan: lo dice el código y se puede leer. Corre en [POR ACLARAR: el ordenador del centro / un alojamiento de terceros; lo tecleado pasa por su servidor durante la sesión]. |
| **4 · Solución** | Introduces los tres resultados y devuelve el percentil de cada prueba y un color. La versión que uso hoy escribe además una etiqueta ("normal", "bajo") y una frase de interpretación con consejo ("conviene seguimiento"); la auditoría pide quitarlas y poner en su lugar la fuente y la población de cada tabla: el percentil lo dice la app, y lo que conviene lo digo yo [POR ACLARAR: si ya está hecho]. |
| **5 · Validación** | Comprobado: casos a mano contra cada tabla. Lo que la auditoría del 11 de septiembre de 2026 destapó: la caminata no interpolaba, saltaba de década en década; la silla etiquetaba mal por debajo del percentil 10; la población de referencia, la fuente y el aviso no se veían; el semáforo decía "normal" y añadía frases de consejo que no son suyas; una dependencia de base de datos sin uso. [POR ACLARAR: qué se corrigió y cuándo]. No mirado: la fiabilidad entre observadores de mis propias pruebas. |
| **6 · Impacto** | En uso desde abril de 2026; quince personas evaluadas en la fase inicial; de unos veinte minutos a segundos por informe, estimación mía, no medida. El impacto clínico está por medir. |
| **7 · Escalabilidad** | El código, en un repositorio público con licencia [POR ACLARAR: licencia elegida; quién figura como autor y cómo se cita], para que otra compañera con un dinamómetro, una silla y una tarde construya la suya y la audite con los tres casos a mano; le falta una sesión de veinte minutos y la lista de lo que aún no hace. La app que uso yo no se distribuye: usada por otros con sus pacientes sería un producto sanitario, y eso es otro proyecto (tercera parte). |

Lo que la tabla no dice y el capítulo sí: el prompt que pide el código, con sus pruebas automáticas y el recuento "CIFRAS DE REFERENCIA EN EL CÓDIGO: 0", está en el anexo A (capítulo 8, caso 1); la auditoría con cuatro casos a mano por prueba, la búsqueda de "ejemplo", "sample" y "fallback" en el código y la fuente, la población y el aviso en pantalla, en "Qué revisar" del mismo caso.

---

## 3 · Tres usos, tres reglas

Qué es, legalmente, lo que construiste si sale de tu consulta (herramienta propia, material didáctico o producto sanitario) está explicado en el capítulo 8, tercera parte, bajo la plantilla: no se repite aquí. La tabla siguiente lo lleva a todo lo que el libro construye, dentro y fuera de la consulta.

---

## 4 · Lo que cambia de nombre legal al salir de la consulta (capítulo 10, tercera parte)

Tabla completa. El capítulo 8 dijo "tres usos, tres reglas" y el 9 puso nombre legal a un agente que no se enciende; aquí van juntos: qué es cada cosa dentro de tu consulta y qué es al salir.

| Qué es | Dentro de tu consulta | Fuera de ella |
|---|---|---|
| Una hoja o un mensaje para la persona | Material informativo revisado y firmado: las tres líneas y el disclaimer en su trato (reglas 11 y 19). | Publicado, es una pieza pública: sin marca, con los disclaimers que toquen y tus vínculos (capítulo 3; RD 1416/1994); sin etiqueta de "generado" si la revisaste tú y respondes de ella (Reglamento (UE) 2024/1689, art. 50.4). |
| Una voz o una imagen sintética | Honesta: "Esta voz es una voz generada por ordenador" aunque nadie lo exija. | Exigible si imita a alguien real, tú incluida, desde el 2 de agosto de 2026 (art. 50.4 [VERIFICAR literal en EUR-Lex]; capítulo 9). |
| La calculadora o el formulario | Herramienta propia sobre tablas publicadas: respondes tú y manda la política del centro (Reglamento (UE) 2017/745, art. 5.5 [VERIFICAR con tu servicio de salud]). | Código compartido para aprender: material didáctico si el repositorio declara finalidad, licencia y que no diagnostica ni recomienda. App para otros cupos: producto sanitario, y quien la distribuye es fabricante (MDR, art. 2.1; anexo VIII, regla 11 [VERIFICAR clase y régimen; la frontera del suministro gratuito no se afirma en ningún sentido]). |
| El asistente propio con guías | Despliegue profesional de un modelo de uso general (AI Act, art. 4; sin las obligaciones de alto riesgo del art. 26). | Publicado "para otros médicos": software producto sanitario, y su proveedora, la médica. Si un día es producto sanitario con evaluación de terceros, sistema de alto riesgo (art. 6.1; capítulo 3). El calendario del reglamento, con la fórmula del libro: se aplica por fases entre 2025 y 2028: lo prohibido y la alfabetización desde febrero de 2025, la transparencia desde agosto de 2026 y las obligaciones de alto riesgo, aplazadas en 2026, entre finales de 2027 y 2028 (Reglamento (UE) 2024/1689, art. 113, modificado por el Reglamento (UE) 2026/1744) [VERIFICAR en EUR-Lex antes de imprimir]. |
| El agente de aviso | En papel: no se enciende (capítulo 9, caso 7). | Dentro del sistema, con contrato y alguien que lo mire: software con finalidad médica, aun dentro (MDR, arts. 2.1 y 5.5; capítulo 9). Fuera del sistema, no existe. |
| La página semanal de evidencia | Una página que se lee sola (capítulo 9, caso 6). | Publicada para otros equipos, es una publicación con responsabilidad editorial: la tuya, con tu nombre, la fecha y las fuentes abiertas, y sin etiqueta de "generado" porque la has leído entera (capítulo 3). Si nombra tratamientos y está en abierto, entra en lo que el capítulo 3 dice de lo público: un espacio solo para profesionales es lo prudente. |

Regla de lectura: el nombre no lo cambia el aviso en pantalla; lo cambian lo que hace y para quién lo publicas (capítulo 8). El reglamento de IA mira la finalidad, no la herramienta (capítulo 3). Nada de esta tabla afirma clase ni régimen sancionador sin comprobación [VERIFICAR]. Las normas citadas están en la lista de referencias del capítulo 10 (RD 1416/1994, AI Act, Reglamento 2026/1744, MDR) y en la del capítulo 3.

---


---

## 5 · Plantilla: hoja de ruta de 90 días, a cinco filas (capítulo 10, caso 7)

Ejemplo completo de salida del prompt del caso 7, con la variable MINUTOS QUE ESTIMO RECUPERAR vacía: por eso las cinco filas llevan el hueco. Sirve de plantilla: sustituye los casos por los tuyos y los huecos por las cifras de tu lista, con "estimación" delante.

> RESUMEN SIN DATOS
>
> | Mes | Momento | Qué hago | Caso del libro | Minutos | Algo que antes no hacía | Qué mido y con qué |
> |---|---|---|---|---|---|---|
> | 30 DÍAS | Consulta | Elegir una frase reescrita del consejo breve y decirla en el último minuto | 1.1 | estimación: [FALTA: minutos] | La prensión y la silla en la primera visita y a los tres meses | Contador de la historia clínica: visitas con función registrada |
> | 30 DÍAS | Administración | Plantilla de correo al hospital por un informe que no llegó | 9.1 | estimación: [FALTA: minutos] | — | Cronómetro: tres correos antes y tres después |
> | 60 DÍAS | Seguimiento de crónicos | Mensaje entre visitas por el canal del centro, huecos rellenados en mi sistema | 4.6 | estimación: [FALTA: minutos] | La llamada a quien no vuelve | Recuento a mano de mensajes enviados y de llamadas hechas |
> | 90 DÍAS | Docencia | Sesión de veinte minutos para el equipo | 1.3 | estimación: [FALTA: minutos] | La sesión de veinte minutos | Recuento a mano: sesión hecha; fichas nuevas en la carpeta |
> | 90 DÍAS | Divulgación | Una pieza al mes, pasada por el auditor | 9.2 | estimación: [FALTA: minutos] | La pregunta de vuelta | Recuento a mano de piezas con auditoría rellenada |
>
> CUANDO HAYA CONTRATO: 5.2 (interconsulta con datos reales).
> Estas medidas cuentan qué hice, no qué conseguí.
> CASOS: 5 · MOMENTOS CUBIERTOS: 5 de 5 · CIFRAS DE MINUTOS: 0, todas de mi lista · HUECOS DE MINUTOS: 5 · PROMESAS DE RESULTADO: 0

Nota: una fila por caso, cinco filas, tres cosas por mes como máximo y un caso por momento. Ninguna cifra de minutos que no esté en tu lista se queda en la tabla, aunque lleve "estimación" delante. Si la tabla trae un caso SOLO CON CONTRATO dentro de los tres meses, se saca a mano.

La hoja de cálculo para medir, sin IA, tiene cuatro columnas por mes: minutos por informe con reloj (antes / después), hojas entregadas, preguntas de vuelta hechas, y la variable clínica (porcentaje del cupo con IMC y cintura registrados; personas con obesidad sin visita en más de doce meses). Debajo, las dos listas del capítulo 7: lo que estas cifras dicen y lo que no se puede concluir, con el denominador que crece con el registro: cuantas más personas tengan IMC y obesidad como problema activo, más larga será la lista de las que llevan un año sin venir; ese mes no ha empeorado nada, ha empezado a verse.

---


---

## 6 · Cómo se monta una comunidad de práctica del área (capítulo 10, caso 8b)

- **Frecuencia y duración.** Una reunión al mes, cuarenta y cinco minutos, misma hora; en el centro o en línea.
- **Tres casos de uso por reunión, uno por persona.** Cada uno con su ficha (capítulo 4, caso 7): versión, modelo leído en el desplegable, "Probada por" y fecha. Sin ficha, no se presenta.
- **Un auditor por ficha.** Alguien que no la escribió la revisa con las cinco preguntas del capítulo 4 (fidelidad, priorización, calibración, confusores, acción segura) y dice qué falló. Los papeles rotan: quien explora una herramienta nueva un mes, integra otra el siguiente y audita al tercero; nadie hace las tres cosas en el mismo mes.
- **Un proyecto compartido**, con la plantilla de siete puntos (capítulo 8; anexo D, plantilla en blanco). Si el punto 3 incluye a una persona, el proyecto cambia o se para.
- **La sesión de veinte minutos** (capítulos 8 y 9) como puerta de entrada de quien llega: se repite cada vez que entra alguien.
- **Una carpeta compartida con las fichas**, nunca con las conversaciones (capítulo 4). Las fichas no llevan datos; las conversaciones pueden llevarlos.
- **Lo que no es.** Un grupo de mensajería donde se pegan casos: ahí no entra nada de nadie (capítulo 3). Tampoco un lugar donde se comparte una app para que otros la usen con pacientes (capítulo 8, tercera parte).
- **El siguiente círculo.** La sociedad científica (SEEDO): grupos de trabajo, jornadas y quien lleva años haciendo esto con menos herramientas y más criterio.
- **Cuando cambia el modelo.** La primera reunión después de un cambio de modelo se dedica a repasar las fichas más usadas: es lo que un grupo aguanta mejor que una persona.

---


---

## 7 · Los datos del reloj, en tres listas (capítulo 10, caso 4)

Del caso 4 del capítulo 10, que se queda con la regla corta: el aviso de ritmo irregular no se ignora, y tampoco una frecuencia en reposo que sube de forma sostenida tras empezar un tratamiento de esa clase; la tensión sin manguito y la grasa de la báscula, sí. Aquí, las tres listas completas.

**Los datos del reloj**, en tres listas (capítulo 9).

- **Qué mirar.** Los pasos como tendencia de semanas, nunca el día. El sueño como pregunta, no como cifra: ronquidos, somnolencia, apnea (capítulo 5). La frecuencia cardiaca en reposo como curiosidad que no cambia nada hoy, salvo que suba de forma sostenida tras empezar un tratamiento de esa clase [VERIFICAR CIMA, secciones 4.4 y 4.8] o el reloj avise de ritmo irregular: eso es un pulso y un electro en consulta, no un dato de la nube.
- **Qué ignorar.** Las calorías que estima. La "edad metabólica". La glucosa de un sensor sin diabetes (capítulo 9). La tensión del reloj sin manguito: la que vale es la de casa con aparato validado y manguito de su talla (capítulo 9). El porcentaje de grasa de la báscula de impedancia. El peso diario, lo primero que le quitaría (capítulo 5).
- **Qué no meter en ningún chat.** La exportación de la app, la captura de pantalla, la foto de la analítica: datos de salud de una persona aunque los traiga ella; "anonimizados", también (capítulo 3).

---


---

## 8 · La herramienta nueva en quince minutos (capítulo 10, caso 5)

Del caso 5 del capítulo 10, sin prompt. Se rellena en papel antes de que la herramienta se acerque a nadie; la ficha (capítulo 4, caso 7) guarda las nueve respuestas con fecha.

**La herramienta nueva en quince minutos**, sin prompt. Las seis preguntas del capítulo 2 (modelo y versión, plan, cuánto cabe, herramientas activas, acuerdo de tratamiento de datos, coste de error) y tres de este libro:

- **¿Qué nombre legal tiene lo que hace?** (capítulo 10, tercera parte).
- **¿Quién firma lo que sale?** Con nombre.
- **¿Ha pasado el examen de diez casos y tres trampas** (capítulo 8, caso 5) antes de acercarse a alguien?

Nueve respuestas en quince minutos. Una en blanco, y la herramienta espera.

---


---

## 9 · Referencias legales completas del capítulo 10

La lista del capítulo 10 cita estas normas en forma corta y remite al capítulo 3, cuya lista las lleva completas (todas menos la 11, que solo está aquí). Numeración de la lista del capítulo 10.

9. Real Decreto 577/2013, de 26 de julio, por el que se regula la farmacovigilancia de medicamentos de uso humano. BOE núm. 179, de 27 de julio de 2013. Arts. 2, 6 y 12.5 [VERIFICAR numeración del 12.5].
11a. Reglamento (UE) n.º 1235/2010 del Parlamento Europeo y del Consejo, de 15 de diciembre de 2010, que modifica, en lo que respecta a la farmacovigilancia, el Reglamento (CE) n.º 726/2004 y el Reglamento (CE) n.º 1394/2007. DOUE L 348, de 31 de diciembre de 2010. Art. 23 del Reglamento (CE) n.º 726/2004.
11b. Directiva 2010/84/UE del Parlamento Europeo y del Consejo, de 15 de diciembre de 2010, que modifica, en lo que respecta a la farmacovigilancia, la Directiva 2001/83/CE. DOUE L 348, de 31 de diciembre de 2010 [VERIFICAR art. 102.e, nombre comercial y lote de los biológicos, y su transposición en el RD 577/2013].
11c. Reglamento de Ejecución (UE) n.º 198/2013 de la Comisión, de 7 de marzo de 2013, relativo a la selección de un símbolo de identificación de los medicamentos sujetos a un seguimiento adicional. DOUE L 65, de 8 de marzo de 2013 [VERIFICAR página; en CIMA, la versión vigente de las fichas técnicas].
12. Ley 44/2003, de 21 de noviembre, de ordenación de las profesiones sanitarias. BOE núm. 280, de 22 de noviembre de 2003. Art. 4.7.
13. Ley 41/2002, de 14 de noviembre, básica reguladora de la autonomía del paciente y de derechos y obligaciones en materia de información y documentación clínica. BOE núm. 274, de 15 de noviembre de 2002. Arts. 4, 7, 8 y 15.
14. Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales. BOE núm. 294, de 6 de diciembre de 2018. Art. 34.1.l).
15. Consejo General de Colegios Oficiales de Médicos. Código de Deontología Médica. Madrid: CGCOM; 2022 (aprobado por la Asamblea General en diciembre de 2022). Capítulo V, arts. 29-31 (secreto profesional y sus excepciones) [VERIFICAR apartado del art. 31 en el PDF oficial]. Disponible en: https://www.cgcom.es/sites/main/files/files/2022-03/codigo_deontologia_medica.pdf
16. Ley Orgánica 10/1995, de 23 de noviembre, del Código Penal. BOE núm. 281, de 24 de noviembre de 1995. Art. 199.2.
17. Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024, por el que se establecen normas armonizadas en materia de inteligencia artificial (Reglamento de Inteligencia Artificial). DOUE L, 12 de julio de 2024. Arts. 3.60, 4, 6.1, 14, 26, 50.4 y 113.
18. Reglamento (UE) 2026/1744 del Parlamento Europeo y del Consejo, de 8 de julio de 2026, por el que se modifican los Reglamentos (UE) 2024/1689, (UE) 2018/1139 y (UE) 2023/1230 en lo que respecta a la simplificación de la aplicación de normas armonizadas en materia de inteligencia artificial (Ómnibus digital sobre IA). DOUE L, 24 de julio de 2026 (en vigor el 27 de julio de 2026). Art. 113 nuevo: anexo III desde el 2 de diciembre de 2027, anexo I desde el 2 de agosto de 2028; el art. 50, desde el 2 de agosto de 2026 [VERIFICAR en EUR-Lex antes de imprimir].
19. Reglamento (UE) 2017/745 del Parlamento Europeo y del Consejo, de 5 de abril de 2017, sobre los productos sanitarios. DOUE L 117, de 5 de mayo de 2017. Arts. 2.1 y 5.5; anexo VIII, regla 11 [VERIFICAR clase y régimen con la AEMPS y el servicio de salud].
20. Real Decreto 1416/1994, de 25 de junio, por el que se regula la publicidad de los medicamentos de uso humano. BOE núm. 180, de 29 de julio de 1994. Arts. 5 y 7 [VERIFICAR literal en BOE]. Citado en el anexo D.


---

## 10 · Recursos: las fuentes públicas que el libro carga o consulta

Son las fuentes que los prompts del libro dan por cargadas (guías descargadas de su web oficial: capítulos 7 y 8) o que se consultan sin IA (PubMed, CIMA, notificaRAM). Las citas van tal como aparecen en las listas de referencias de los capítulos, con sus marcas [VERIFICAR]; entre paréntesis, el capítulo del que se copia y los demás que la citan. No se añade ninguna dirección que no esté ya en un capítulo.

**Guías que se cargan en un asistente con archivos (capítulo 7, caso 2; capítulo 8, caso 2)**

- Sociedad Española para el Estudio de la Obesidad (SEEDO). Guía Española GIRO: Guía española del manejo Integral y multidisciplinaR de la Obesidad en personas adultas. 2.ª ed. Lecube A, coordinador. Madrid: SEEDO; noviembre de 2024. Disponible en: https://www.seedo.es/images/site/giro/GUIA-GIRO-2a-edicin_26NOV2024.pdf [VERIFICAR: ISBN en la página de créditos; 978-84-09-65969-2 según fuente secundaria] (capítulo 1, referencia 12; citada también en los capítulos 2 a 8).
- Wharton S, Lau DCW, Vallis M, Sharma AM, Biertho L, Campbell-Scherer D, et al. Obesity in adults: a clinical practice guideline. CMAJ. 2020;192(31):E875-E891. doi:10.1503/cmaj.191707 (capítulo 4, referencia 9; citada también en los capítulos 6, 7 y 8; en el capítulo 8 con [VERIFICAR plazo y umbral de respuesta; probablemente en la guía completa de Obesity Canada]).
- National Institute for Health and Care Excellence. Overweight and obesity management. NICE guideline NG246. Londres: NICE; 14 de enero de 2025. Disponible en: https://www.nice.org.uk/guidance/ng246 (capítulo 7, referencia 15; citada también en el capítulo 8).

**Lo que se consulta sin IA**

- National Library of Medicine. PubMed y My NCBI [Internet]. Bethesda (MD): NLM [consultado el 15 de septiembre de 2026]. Disponible en: https://pubmed.ncbi.nlm.nih.gov y https://account.ncbi.nlm.nih.gov (capítulo 7, referencia 4; citada también en el capítulo 9). La alerta fiable y gratuita de evidencia es la de My NCBI (capítulo 7, caso 6; capítulo 9, caso 6).
- Agencia Española de Medicamentos y Productos Sanitarios. Centro de Información online de Medicamentos (CIMA) [Internet]. Madrid: AEMPS [consultado el 15 de septiembre de 2026]. Fichas técnicas por principio activo, secciones 4.2, 4.4, 4.5 y 4.6. Disponible en: https://cima.aemps.es (capítulo 8, referencia 8; citada también en el capítulo 6, sección 4.8, y en el capítulo 7, sección 4.6). CIMA dice lo autorizado, no lo último publicado (capítulo 7).
- Agencia Española de Medicamentos y Productos Sanitarios. notificaRAM: formulario electrónico de notificación de sospechas de reacciones adversas a medicamentos del Sistema Español de Farmacovigilancia de medicamentos de uso Humano [Internet]. Madrid: AEMPS [consultado el 11 de septiembre de 2026]. Disponible en: https://www.notificaram.es (capítulo 3, referencia 17; en el capítulo 10, referencia 10, con "Manual de uso de NotificaRAM. Madrid: AEMPS; 2025 [VERIFICAR fecha y dirección; criterios de gravedad del formulario]"). Los datos reales van directos a notificaRAM.es, nunca por un chat (capítulos 3 y 10).

**Herramientas nombradas en el libro (capítulos 2, 7, 8 y 9)**

Gemini, ChatGPT y Claude como asistentes de consumo; NotebookLM y los espacios con archivos (Gema, Project, GPT personalizado) para guías cargadas; Perplexity y los modos de búsqueda como buscadores con IA; Consensus, Elicit, Scite y OpenEvidence como buscadores de evidencia [VERIFICAR OpenEvidence desde España]; Streamlit para la calculadora. Todos, "cuando escribo esto": comprueba la versión vigente y la política de datos; ninguno tiene acuerdo de tratamiento de datos con tu servicio de salud salvo que te lo den con contrato. No se imprime ninguna dirección de app en marcha (capítulo 8).
