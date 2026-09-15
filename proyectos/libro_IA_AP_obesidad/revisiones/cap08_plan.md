# Capítulo 8 · Plan del ARQUITECTO, con las decisiones del ORQUESTADOR (15-09-2026)

> Punto de partida: `indice_v2_caps_8-10.md` (capítulo 8 = antiguos 8 y 12), la biblia (decisiones 1-9, reglas 10-33, compromisos de los capítulos 4-7 con el antiguo capítulo 8) y los datos de la calculadora de la autora registrados en CLAUDE.md y en la biblia (decisión 9). Estado: capítulos 1-3 y 5 aprobados; 4, 6 y 7 terminados, pendientes de aprobación; la autora ha pedido seguir. Regla 20, opción (a): tope 10.000; 350 palabras por prompt como práctica recomendada.

## Ficha

- **Título:** Capítulo 8 · Apoyo a la decisión, asistentes propios y tu proyecto en siete puntos
- **Subtítulo:** De la calculadora de veinte minutos a la de veinte segundos, y de un chat a un asistente con tus guías.
- **Parte:** II · Usar (último capítulo de la parte). **Dependencias:** 4 (rúbrica, cadena, ficha), 7 (tres guías; PICO del músculo; regla 31 de licencias). Prepara el 9 y el 10.
- **Extensión objetivo:** 7.500-8.500 palabras. Tope 10.000. Siete prompts; se recomienda ≤ 350 palabras cada uno, sin obligación.
- **Formato obligatorio:** el de la biblia (decisión 2), con la frase introductoria a los casos de los capítulos 5-7 como modelo.

## Gancho

El de la v2 del índice: "Durante años dejé de hacer la prueba de la silla porque interpretar el resultado me costaba más que hacerla. Tres tablas, tres artículos, interpolar a mano. Hoy tardo veinte segundos y la hago en todas las visitas. En medio hubo ocho semanas, muchos errores y una plantilla de siete puntos." Cierra con la frase de composición.

## Los tres aprendizajes clave

Los del índice v2. Precisiones: el "ciclo clínico" (representar, hipotetizar, contrastar, falsar, actualizar, auditar) y "máquinas no deterministas creando deterministas" vienen del programa formativo: se reformulan con voz propia y una sola frase los atribuye a "mi formación en IA" (reglas 10 y 21); los verbos del ciclo se conservan sin los calificativos del curso, como se hizo con la cadena del capítulo 4.

## Tesis del capítulo en una frase

La máquina no decide y la máquina no calcula bien sola; lo que sí hace es construir contigo la herramienta que calcula siempre igual y el asistente que cita siempre la guía. Construirlos sin datos de nadie es posible: así empecé yo.

## Los siete casos (con las decisiones del ORQUESTADOR)

| # | Caso | Momento | Herramienta | Decisiones |
|---|---|---|---|---|
| 1 | **La calculadora de condición física, punto por punto [AP]** | consulta y seguimiento | asistentes de IA para código (Claude y ChatGPT, según la autora), app publicada como código abierto; sin datos de pacientes dentro de la IA | Caso destacado y ejemplo rellenado de la plantilla de siete puntos (problema, herramienta, datos, solución, validación, impacto, escalabilidad). Hechos de la autora (biblia y CLAUDE.md): tres pruebas (caminata de seis minutos, prensión, silla) con percentiles de tres fuentes publicadas (STAAB 2024; Tomkinson 2024; EXERNET 2012 [VERIFICAR citas completas]); en uso desde abril de 2026; quince personas evaluadas en la fase inicial; de unos veinte minutos a segundos, **como estimación de la autora, no medición**; la app no guarda datos: edad, sexo, talla y resultado se introducen y no se almacenan. **Lo que la auditoría destapó (11-09-2026):** interpolación solo por décadas en la caminata, etiqueta errónea por debajo del percentil 10 en la silla, población de referencia y disclaimer no visibles, dependencia de base de datos sin uso. El capítulo lo cuenta como parte del método ("validación honesta"), y el estado de corrección va como [POR ACLARAR: la autora confirma qué se corrigió y cuándo]. El repositorio público figura a nombre de otra persona: [POR ACLARAR: autoría o alojamiento del código; quién se cita]. El prompt del caso es el que pide el código de una calculadora determinista con tablas publicadas como datos, con la regla "el mismo dato, la misma salida", y una auditoría de tres pruebas antes de usarla. |
| 2 | **Mi asistente de derivación y tratamiento [AP]** | consulta | Gema, Project o GPT personalizado (cuando escribo esto) con GIRO 2024, Wharton 2020 y NICE NG246 como fuentes (documentos públicos, regla 31) | Instrucciones de sistema del asistente como prompt del caso: responde solo con las fuentes cargadas, cita literal con página o número de cita, separa derivación programada de la que no espera (sospecha de causa secundaria: hipercortisolismo, tiroides muy alterada, edemas con disnea; complicación), nunca decide ("DECISIÓN: la médica"), nunca nombra comerciales, no admite datos de personas (perfiles en rangos). Ejemplo con un perfil sintético. Cumple la regla 13 (los criterios de derivación y tratamiento se remitían a este capítulo). Continúa el caso 2 del capítulo 7 (tres guías). |
| 3 | **Analítica de seguimiento en tratamiento farmacológico** | seguimiento de crónicos | asistente de consumo, caso sintético | Un caso sintético de cero (regla 22): persona en tratamiento con un fármaco para la obesidad por mecanismo (agonista del receptor de GLP-1 como clase, sin nombre), con diabetes tipo 2 en sulfonilurea, en su primera analítica de seguimiento. El prompt ordena lo esperable, lo que alerta y lo que se deriva, con la escala ALTA/MEDIA/BAJA, sin decidir tratamiento ("DECISIÓN TERAPÉUTICA: la médica"). "Qué revisar" es donde el capítulo paga los compromisos heredados: intensificación con HbA1c 7,6 % y metformina (capítulo 4; ADA 2025, ADA-EASD 2022); ajuste de sulfonilurea o insulina al añadir un incretínico (capítulo 6); anticoncepción y antelación antes de buscar embarazo, con la ficha técnica (capítulo 7); valoración de respuesta a los meses y retirada sin culpa (GIRO 2024; Wharton 2020); días de enfermedad con metformina, SGLT2, diuréticos e IECA/ARA-II; dosis de ácido fólico en obesidad según guía [VERIFICAR]. **Nota al pie de transparencia obligatoria (regla 12)**, en superíndice ¹ con párrafo propio. Sin dosis, sin marcas, sin "a quién": lo que la guía dice, con cita. |
| 4 | **Cribado de sarcopenia en obesidad: función antes que masa [AP]** | seguimiento de crónicos | calculadora determinista o asistente con rúbrica | Fuerza de prensión, levantarse de la silla cinco veces, velocidad de la marcha, SARC-F; puntos de corte del consenso europeo (EWGSOP2, Cruz-Jentoft 2019 [VERIFICAR]) y la obesidad sarcopénica (ESPEN/EASO 2022 [VERIFICAR]); un semáforo, no un diagnóstico; qué se deriva. Responde a la pregunta del músculo del capítulo 7 (caso 1) y usa las tres pruebas de la calculadora. Sin datos de nadie: caso sintético o la propia calculadora. |
| 5 | **Probar el asistente antes de usarlo** | docencia | diez casos sintéticos; preguntas trampa; la rúbrica del capítulo 4 | Protocolo de una hora: diez casos sintéticos de cero (incluidos tres trampa: pedir dosis, pedir diagnóstico cerrado, pedir "dieta milagro"), la rúbrica (fidelidad, priorización, calibración, confusores, acción segura) y un registro de fallos con fecha y modelo; criterio de salida ("con un fallo de acción segura, no se usa"). Nada se usa con una persona sin pasar por aquí. Absorbe el antiguo caso 13.3. |
| 6 | **De la calculadora a un formulario determinista [AP]** | seguimiento de crónicos | asistente que escribe código o formulario | "Máquinas no deterministas creando deterministas": cómo se pide código que al mismo dato responde siempre lo mismo (tablas como datos, sin que el modelo "recuerde" cifras; pruebas con valores límite; el mismo caso tres veces). El cuestionario de cribado del caso 4 como versión mínima en dos tardes. Qué sale mal (la interpolación de la calculadora) y cómo se audita (tres pruebas a mano contra la tabla publicada). |
| 7 | **Presentarlo en siete diapositivas y compartirlo** | docencia | asistente conversacional | Del documento de siete puntos a la sesión de diez minutos; validación honesta en la diapositiva 5 (lo que has comprobado y lo que aún no); compartir: código abierto con licencia, docencia a otros médicos de familia, comunidad de práctica; un proyecto de Atención Primaria escala cuando otro cupo lo usa. Absorbe los antiguos 12.5 y 12.7 (la biblioteca de prompts del equipo ya está en el capítulo 4, caso 7: remitir). |

Orden: 1 a 7. La viñeta usa los casos 1, 4 y 6.

## Estructura del desarrollo (antes de los casos)

- **Primera parte · Veinte minutos por informe.** La prueba de la silla que dejé de hacer; por qué la función importa en obesidad (sarcopenia, caídas, independencia; GIRO 2024; SEEDO GO! si la autora lo confirma); el problema no era la prueba, era la interpretación.
- **Segunda parte · El ciclo: la máquina abre, tú cierras.** Representar, hipotetizar, contrastar, falsar, actualizar, auditar, con el caso del capítulo 4 como recuerdo y el asistente con guías como herramienta; "no cerrar el diagnóstico" ya está (capítulo 4, caso 4): aquí, cómo se cierra con la guía. Máquinas no deterministas creando deterministas, en tres frases y con la calculadora como prueba. Atribución única (regla 21).
- **Tercera parte · La plantilla de siete puntos.** Una página: problema, herramienta, datos, solución, validación, impacto, escalabilidad, con la pregunta guía de cada punto; la calculadora rellenada en la tabla del caso 1; validación honesta como antídoto del exceso de seguridad del capítulo 2.
- **Siete casos.**
- **Viñeta.**
- **En 60 segundos · Hazlo hoy · Referencias.**

## Viñeta clínica (arquetipo compuesto, declarado)

Hombre de 65-70 años, obesidad de grado II con pérdida de masa muscular, dolor lumbar y miedo a caerse; en la primera evaluación, naranja o rojo en las tres pruebas con el peso casi igual que un año antes; tres meses después, con ejercicio de fuerza pautado, la silla en verde y el peso casi igual. Se combinan rasgos de las personas evaluadas con la calculadora en su fase inicial; se modifican edad exacta, talla, resultados numéricos y circunstancias; sin municipio, fechas ni cifras trazables. Muestra: la prueba hecha en consulta (no en la IA), el resultado en veinte segundos con su percentil y su población de referencia visible, lo que la médica decide (fuerza, proteína, derivación si procede: capítulo 8 lo decide aquí, con la guía), y la frase de la persona. Promesa de datos (regla 16) con su fórmula, adaptada: nada suyo entra en la IA; en la calculadora entran edad, sexo, talla y el resultado, y no se guardan. Estribillo: "la función mejora antes que el peso".

## Reglas de la biblia que este capítulo tiene que cumplir de forma visible

- Reglas 12 (nota ¹ en el caso 3), 13 (aquí se decide lo que los capítulos 3-7 remitieron), 16, 19 (si algún texto llega a la persona), 21, 22, 27, 30, 31 (documentos públicos en el asistente), 33 (etiquetas).
- Decisión 8 y 9: la calculadora se construyó sin contrato y sin datos de pacientes en la IA; es el hilo narrativo del libro.
- Herramientas por nombre con "cuando escribo esto" (Gemas, Projects, GPT personalizados, Streamlit, Google Colab si se nombra).
- Cifras de tiempo e impacto: solo como estimación de la autora; "el impacto clínico está por medir".
- Ficha del capítulo 4 para guardar los prompts; el asistente propio se documenta con la misma ficha (instrucciones, fuentes, fecha de la última prueba, modelo).

## Lo que el REDACTOR no debe hacer

- No decir que la calculadora está validada clínicamente ni que ahorra tiempo medido: es una estimación y una experiencia con quince personas.
- No ocultar los errores de la auditoría ni presentarlos como corregidos sin confirmación de la autora ([POR ACLARAR]).
- No dar dosis, marcas ni "a quién se indica" fuera de lo que la guía citada dice; no decidir el tratamiento del caso 3: lo decide la médica con la guía delante, y el capítulo lo muestra.
- No copiar la plantilla de siete puntos del programa con sus frases: reformular (regla 10).
- No inventar referencias: STAAB, Tomkinson y EXERNET van con [VERIFICAR] si no se conocen con certeza.

## Referencias que el REDACTOR puede usar si las conoce con certeza (EVIDENCIA las comprobará)

- GIRO 2024; Wharton 2020; NICE NG246 (verificadas).
- EWGSOP2: Cruz-Jentoft 2019 (Age Ageing) [VERIFICAR]; obesidad sarcopénica: Donini 2022 (ESPEN/EASO) [VERIFICAR]; SARC-F: Malmstrom 2013/2016 [VERIFICAR].
- Prensión: Tomkinson 2024 (normas internacionales) [VERIFICAR]; silla: EXERNET 2012 [VERIFICAR]; caminata: cohorte STAAB 2024 [VERIFICAR].
- ADA 2025 Standards of Care; ADA-EASD 2022 consenso [VERIFICAR ediciones].
- Fichas técnicas por principio activo (CIMA), secciones 4.4-4.8.
- Sobre modelos que escriben código y determinismo: solo si se conoce con certeza; si no, sin referencia.

## Preguntas para Cristina que el REDACTOR deja planteadas (máximo 5 al cierre; las recoge el ORQUESTADOR)

1. Calculadora: ¿qué se corrigió tras la auditoría del 11-09-2026 y cuándo (interpolación, etiqueta bajo el percentil 10, disclaimer y población visibles)? ¿Quién figura como autor del código y cómo quiere que se cite el repositorio?
2. ¿Con qué asistentes escribió el código y cuántas iteraciones? ¿Guarda los prompts?
3. ¿Qué hace hoy con un percentil rojo en la silla o en la prensión: qué pauta, a quién deriva?
4. ¿Tiene ya un asistente propio con guías (Gema o Project)? ¿Con qué fuentes y qué le pregunta?
5. Caso 3: ¿qué analítica pide en el primer seguimiento de un tratamiento farmacológico y cada cuánto? ¿Qué hace con la sulfonilurea al empezar?
