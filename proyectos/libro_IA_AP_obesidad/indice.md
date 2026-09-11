# Índice detallado del libro · v1 (ARQUITECTO)

> **Obra:** *Inteligencia artificial en la consulta de Atención Primaria: guía práctica para el abordaje de la obesidad* (título de trabajo; propuestas alternativas al final).
> **Autora:** Dra. Cristina Petratti, médica de familia, especialista en obesidad.
> **Elaborado:** 2026-09-11 por el agente ARQUITECTO del orquestador editorial, a partir de `biblia.md`, `prompt_gemini.md` y la memoria del programa *AI-Powered Metabolic Medicine* / potencIA.
> **Estado:** v1, pendiente de aprobación por la autora.

## Cómo leer este índice

- Cada capítulo lleva: título definitivo, subtítulo, frase gancho en primera persona (situación real de consulta de AP), tres aprendizajes clave, entre 5 y 8 casos de uso, la viñeta clínica propuesta (siempre arquetipo compuesto), dependencias y extensión objetivo.
- Cada caso de uso indica **herramienta** y **momento** del médico de familia: *consulta · seguimiento de crónicos · administración · docencia · divulgación*.
- **[AP]** marca los casos de uso específicos de Atención Primaria que no son traslación directa del ámbito hospitalario (cupo, longitudinalidad, enfermería de AP, domicilio, comunidad, burocracia propia de AP).
- **Herramientas.** Se nombran las de software (Gemini, ChatGPT, Claude, NotebookLM, Perplexity, Consensus, Scite, Elicit, Canva, HeyGen, ElevenLabs, Google AI Studio, n8n, Streamlit, Google Colab) con la advertencia de comprobar la versión vigente. En todo el libro se distingue **herramienta de consumo** (sin contrato de tratamiento de datos: solo datos sintéticos, anonimizados o agregados) de **herramienta con acuerdo de tratamiento de datos** (la que ofrezca el servicio de salud o el centro). Ningún caso de uso requiere introducir datos identificables de pacientes en herramientas de consumo.
- **Lenguaje.** "Persona con obesidad", nunca "obeso/a". Fármacos por principio activo y mecanismo. Eje del libro: **"Es biología, no falta de voluntad."**
- **Extensión total estimada:** 55.000 palabras en 14 capítulos (3.500-4.500 cada uno) más unas 12.000 en anexos.

---

## Materiales de apertura

- **Nota de transparencia** (obligatoria, antes del prólogo): declaración de la autora sobre su formación en programas patrocinados por la industria farmacéutica y vínculos vigentes; el libro es divulgación profesional para sanitarios, no publicidad; no contiene nombres comerciales de medicamentos de prescripción. Aplicación de la guía de disclosure del Módulo 3.
- **Prólogo de la autora** (800 palabras): por qué una médica de familia con 25 años de consulta escribe sobre IA; qué cambió en ocho semanas; qué promete el libro y qué no.
- **Cómo usar este libro** (400 palabras): lectura lineal o por momentos; los prompts se copian tal cual; qué hacer con las etiquetas [VERIFICAR]; el disclaimer estándar.

---

# PARTE I · ENTENDER

## Capítulo 1 · Es biología, no falta de voluntad

**Subtítulo:** Por qué la obesidad en Atención Primaria necesita otra manera de trabajar.

**Gancho:** "Son las 12:40, llevo cuatro pacientes de retraso y entra una mujer que lleva veinte años oyendo que tiene que comer menos. Tengo siete minutos para no repetírselo."

**Los 3 aprendizajes clave**
1. La obesidad es una enfermedad crónica con biología detrás: regulación del apetito, adaptación metabólica, recuperación ponderal. Tratarla como un fallo de voluntad es un error clínico, no solo de tono.
2. La obesidad vive en Atención Primaria: prevalencia, comorbilidad, longitudinalidad. Pero el tiempo de consulta no la contempla, y lo que no cabe en la agenda deja de hacerse.
3. La IA generativa no va a atender a nadie por ti. Puede devolverte minutos y estructura para hacer lo que solo tú puedes hacer: escuchar, decidir y acompañar.

**Casos de uso (6)**
1. **Mapa de mi cupo** · intérprete de código (Gemini, ChatGPT o Claude) sobre una hoja de cálculo exportada sin identificadores, solo variables agregadas · administración · [AP]. Cuántas personas con obesidad, con qué comorbilidades, cuántas sin visita en el último año.
2. **Reescribir el consejo breve** · cualquier asistente conversacional · consulta · [AP]. Tres frases habituales ("tiene que comer menos", "es cuestión de moverse") reescritas en lenguaje centrado en la persona, para siete minutos.
3. **La adaptación metabólica en 150 palabras** · asistente conversacional · consulta. Explicación para decir en voz alta, nivel de lectura de 12 años, sin culpa.
4. **Sesión del centro "la obesidad es una enfermedad crónica"** · NotebookLM con las guías SEEDO y GIRO públicas · docencia · [AP]. Guion de 20 minutos para el equipo, enfermería incluida.
5. **Inventario de mi tiempo** · asistente conversacional + hoja de cálculo · administración · [AP]. Una semana cronometrada, tareas clasificadas por los cinco momentos, para saber dónde duele.
6. **"¿Por qué recupero el peso?" en tres niveles** · asistente conversacional · consulta. La misma respuesta para tres niveles de alfabetización en salud, con el disclaimer estándar.

**Viñeta clínica (arquetipo compuesto):** mujer de entre 50 y 60 años, obesidad grado II, hipertensión y prediabetes, cuatro o cinco intentos previos de pérdida de peso con recuperación completa, que entra en consulta con la frase "ya sé lo que me va a decir". Se combinan los rasgos de varias pacientes con recuperación ponderal tras dietas restrictivas; se modifican profesión, municipio, situación familiar y edad exacta; no hay fechas ni cifras que permitan trazar a nadie. Es la paciente que reaparece en el capítulo 14.

**Dependencias:** ninguna. Es el capítulo de tesis.

**Extensión objetivo:** 3.500 palabras.

---

## Capítulo 2 · Qué es (y qué no es) la IA generativa

**Subtítulo:** Lo justo para usarla con criterio, sin ingeniería.

**Gancho:** "La primera vez que le pedí a un chat que me resumiera una guía, me devolvió un párrafo impecable con una cita que no existía. Ahí empezó todo."

**Los 3 aprendizajes clave**
1. Un modelo de lenguaje predice la siguiente palabra: por eso suena seguro aunque se equivoque. Tokens, ventana de contexto, no determinismo y multimodalidad explicados en una frase cada uno.
2. La alucinación no es un fallo raro: es la consecuencia natural de cómo funciona. La pregunta útil no es "¿se equivoca?", sino "¿cuál es el coste de que se equivoque en esta tarea?".
3. No todo lo que se llama IA es lo mismo. Antes de cada tarea: qué modelo, qué versión, qué plan, cuánto contexto, qué herramientas, y si tiene o no acuerdo de tratamiento de datos.

**Casos de uso (7)**
1. **La misma pregunta en tres modelos** · Gemini, ChatGPT y Claude en paralelo · docencia. Una pregunta clínica sobre obesidad, tres respuestas, una tabla de diferencias.
2. **Cazar una alucinación** · asistente conversacional + PubMed · docencia. Pedir cinco referencias sobre adaptación metabólica y comprobar cuántas existen.
3. **Lo que se pierde en medio** · asistente con carga de documentos · consulta. Subir una guía pública larga y preguntar por un dato enterrado a mitad; después, dirigir la atención a la sección concreta y comparar.
4. **Leer una etiqueta nutricional** · asistente multimodal, foto sin datos personales · consulta. Ejemplo de multimodalidad útil en siete minutos.
5. **Qué nivel de IA exige esta tarea** · tabla en papel o asistente · administración · [AP]. Diez tareas de una jornada de AP clasificadas por coste de error y nivel de herramienta necesaria.
6. **Chat frente a razonador** · modelo de razonamiento vs modelo conversacional · consulta. El mismo caso sintético en los dos modos; qué cambia y cuánto tarda.
7. **Inventario de lo que tengo** · sin herramienta de IA · administración · [AP]. Qué ofrece mi servicio de salud con contrato, qué uso por mi cuenta y qué no debo usar con datos de pacientes.

**Viñeta clínica (arquetipo compuesto):** hombre de 40-50 años, obesidad grado II, que llega con una respuesta de un chat gratuito impresa: "me dice que tengo resistencia a la insulina y que necesito tal medicación". Se combinan varios pacientes que consultan tras una búsqueda con IA; se modifican la ocupación, el modelo de IA citado y la petición concreta. Sirve para explicar en consulta qué es y qué no es esa respuesta.

**Dependencias:** capítulo 1.

**Extensión objetivo:** 3.500 palabras.

---

## Capítulo 3 · El marco ético y legal, sin miedo

**Subtítulo:** RGPD, AI Act, deontología y conflictos de interés aplicados a una consulta de siete minutos.

**Gancho:** "Una compañera me confesó que había pegado un informe entero en un chat gratuito para que se lo resumiera. No era mala fe: nadie le había explicado dónde estaba la línea."

**Los 3 aprendizajes clave**
1. La regla de los datos: qué puede entrar en qué herramienta. Datos mínimos, anonimización real (no basta con quitar el nombre) y diferencia entre herramienta de consumo y herramienta con acuerdo de tratamiento de datos. RGPD, LOPDGDD y Código de Deontología OMC 2022.
2. AI Act europeo en una página: la IA no decide, tú firmas. Supervisión humana explícita en todo uso clínico.
3. Transparencia y estigma también son ética: declarar conflictos de interés (regla del efecto vigente) y vigilar el sesgo de peso que los modelos heredan de sus datos.

**Casos de uso (7)**
1. **Anonimizar antes de pegar** · plantilla en papel + prompt de comprobación en asistente conversacional · consulta. El asistente revisa un texto ya anonimizado y señala lo que aún permitiría identificar (fechas, municipio pequeño, profesión rara).
2. **Modelo de información al paciente sobre uso de IA** · asistente conversacional · administración. Texto breve para la sala de espera o la web del centro; requiere revisión del servicio jurídico.
3. **Mi nota de transparencia** · asistente conversacional · divulgación. Declaración de vínculos para sesiones, artículos y redes, con lenguaje concreto y trazable.
4. **Detectar sesgo de peso en una respuesta** · asistente conversacional · consulta. El mismo motivo de consulta (dolor de rodilla) para una persona con y sin obesidad; comparar qué recomienda el modelo.
5. **"¿Doctora, usted usa IA?"** · sin herramienta · consulta · [AP]. Guion de respuesta honesta de 30 segundos para la relación longitudinal propia de AP.
6. **El minuto antes de pulsar Enter** · checklist en papel · consulta. Cinco comprobaciones (datos, herramienta, propósito, salida, firma) que caben en el margen de la agenda.
7. **Preparar una consulta a un compañero** · herramienta con contrato del servicio de salud o resumen anonimizado · seguimiento de crónicos · [AP]. Cómo pedir opinión a la unidad de obesidad o al endocrinólogo de referencia sin exponer datos.

**Viñeta clínica (arquetipo compuesto):** mujer joven, 25-30 años, obesidad grado I con antecedente de trastorno de la conducta alimentaria, que pide que "esto no conste en ningún sitio" y pregunta si sus datos "van a parar a una máquina". Se combinan varias consultas sobre privacidad y estigma; se modifican edad, profesión y contexto familiar. Enlaza con el capítulo 13.

**Dependencias:** capítulos 1 y 2.

**Extensión objetivo:** 3.500 palabras.

---

# PARTE II · USAR

## Capítulo 4 · Hablar con la IA

**Subtítulo:** Rol, contexto, tarea, formato: la gramática que cambia el resultado.

**Gancho:** "Le pedí 'dieta para adelgazar' y me devolvió lo mismo que un folleto de gasolinera. Le pedí lo mismo con rol, contexto, tarea y formato, y me devolvió algo que podía usar esa misma tarde."

**Los 3 aprendizajes clave**
1. La estructura rol · contexto · tarea · formato · restricciones. Un prompt pobre y el mismo prompt estructurado, lado a lado.
2. Tres técnicas que bastan: ejemplos propios (few-shot), pedir el razonamiento paso a paso y encadenar prompts (estructurar → analizar → criticar → comunicar).
3. Leer la respuesta con rúbrica: fidelidad, priorización, calibración, confusores, acción segura. "Si suena demasiado segura, probablemente lo es."

**Casos de uso (7)**
1. **Prompt pobre frente a prompt estructurado** · cualquier asistente conversacional · consulta. Plan de actividad física para una persona con obesidad y artrosis de rodilla (caso sintético).
2. **Que escriba como yo** · asistente conversacional con tres textos propios anonimizados como ejemplo · administración. Imitar tu tono en cartas y hojas de recomendaciones.
3. **La cadena de cuatro prompts** · asistente conversacional · seguimiento de crónicos. Caso sintético: estructurar sin opinar → analizar dilemas con nivel de certeza → criticar la propia respuesta → comunicar en doble salida (equipo y paciente).
4. **"No cierres diagnóstico"** · modelo de razonamiento · consulta. Separar hechos, inferencias, datos ausentes y conclusiones prematuras en una ganancia de peso reciente (caso sintético).
5. **El consejo breve de siete minutos** · asistente conversacional · consulta · [AP]. Prompt que produce una intervención de dos frases, una pregunta abierta y un siguiente paso pactado.
6. **Mensaje entre visitas** · asistente conversacional, sin identificadores · seguimiento de crónicos · [AP]. Texto de refuerzo para la consulta telefónica o el mensaje del centro, con disclaimer estándar.
7. **Mi biblioteca de prompts en Markdown** · editor de texto · administración. Cómo guardar, versionar y compartir los prompts que funcionan; puente hacia el Anexo A.

**Viñeta clínica (arquetipo compuesto):** hombre de 60-65 años, obesidad grado II, diabetes tipo 2 y artrosis, jubilado reciente, que "ahora tiene tiempo pero no sabe por dónde empezar". Caso sintético construido a propósito para correr la cadena de prompts; se combinan rasgos de pacientes con comorbilidad osteoarticular y se modifican cifras analíticas para que sean verosímiles pero no reales.

**Dependencias:** capítulos 2 y 3.

**Extensión objetivo:** 4.000 palabras.

---

## Capítulo 5 · Documentar mejor y más rápido

**Subtítulo:** Notas, interconsultas, informes y cartas sin perder la tarde.

**Gancho:** "A las tres me quedaban once historias por cerrar y una interconsulta que llevaba dos semanas posponiendo. La interconsulta salió en cuatro minutos. Las historias, en veinte. Antes eran la tarde entera."

**Los 3 aprendizajes clave**
1. De notas sueltas a nota estructurada: el modelo ordena, no inventa. Todo hueco se marca como [FALTA: …] y lo rellenas tú.
2. La interconsulta que se lee: motivo, pregunta concreta, criterios de derivación de las guías, lo ya hecho en AP.
3. Dónde se hace cada cosa: la historia clínica real solo entra en herramientas con contrato del servicio de salud; en las de consumo trabajas con plantillas, datos sintéticos o texto anonimizado de verdad.

**Casos de uso (8)**
1. **Notas sueltas → nota SOAP con [FALTA]** · herramienta con contrato, o asistente de consumo con caso sintético · consulta.
2. **Interconsulta a la unidad de obesidad o Endocrinología** · asistente conversacional con criterios SEEDO/GIRO como contexto · seguimiento de crónicos · [AP]. Con criterios de derivación explícitos y lo intentado en AP.
3. **Informe para incapacidad temporal, inspección o valoración de discapacidad** · asistente conversacional sobre plantilla anonimizada · administración · [AP]. Lenguaje funcional, no moral.
4. **Del informe hospitalario a mi plan** · herramienta con contrato · seguimiento de crónicos · [AP]. Extraer del alta o informe de consulta externa las tareas que quedan para AP, en lista.
5. **Plan de cuidados compartido con enfermería** · asistente conversacional · seguimiento de crónicos · [AP]. Quién hace qué en el seguimiento de la persona con obesidad en el centro.
6. **Resumen de dos años de evolución** · exclusivamente herramienta con contrato · seguimiento de crónicos · [AP]. Qué pedirle y qué comprobar; qué no hacer nunca en una herramienta de consumo.
7. **Recomendación escrita de actividad física** · asistente conversacional · consulta · [AP]. Plantilla que se personaliza en consulta sin datos identificables, con disclaimer estándar.
8. **Respuesta a una reclamación con calma** · asistente conversacional sobre texto anonimizado · administración. Tono, estructura, hechos.

**Viñeta clínica (arquetipo compuesto):** mujer de 40-45 años, obesidad grado III con apnea del sueño, en lista de espera para valoración de cirugía bariátrica, que necesita interconsulta, informe para su empresa y coordinación con enfermería en el mismo mes. Se combinan trayectorias documentales de varias pacientes; se modifican edad, profesión, hospital de referencia y tiempos de espera.

**Dependencias:** capítulos 3 y 4.

**Extensión objetivo:** 4.000 palabras.

---

## Capítulo 6 · Educar a la persona con obesidad

**Subtítulo:** Materiales que se entienden, en su idioma y sin culpa.

**Gancho:** "Le di una hoja de recomendaciones de tres páginas. Volvió a los tres meses y me dijo que no la había entendido. Tenía razón: la había escrito para mí."

**Los 3 aprendizajes clave**
1. Alfabetización en salud: pedir nivel de lectura, longitud y una sola idea por párrafo. El modelo lo hace bien si se lo pides.
2. Multiidioma con red: traducir, y verificar con re-traducción en una conversación nueva. Nunca entregar sin revisar.
3. Todo lo que llega al paciente lleva validación clínica y el disclaimer estándar. Sin excepciones, tampoco cuando hay prisa.

**Casos de uso (7)**
1. **Hoja "por qué recupero el peso"** · asistente conversacional · consulta. Nivel de lectura de 12 años, 200 palabras, sin culpa, con disclaimer.
2. **La misma hoja en árabe, rumano e inglés** · asistente conversacional con re-traducción · consulta · [AP]. Para la población real de un centro de salud.
3. **Qué esperar del tratamiento** · asistente conversacional · consulta. Guion de conversación de primera visita: objetivos realistas, principio activo y mecanismo (por ejemplo, agonistas del receptor de GLP-1), efectos adversos frecuentes, cuándo llamar.
4. **Preguntas frecuentes sobre náuseas y otros efectos adversos** · asistente conversacional · seguimiento de crónicos. Hoja de manejo doméstico y señales para consultar.
5. **Mensaje de refuerzo para la consulta telefónica** · asistente conversacional, sin identificadores · seguimiento de crónicos · [AP].
6. **Cartel de sala de espera** · Canva con texto generado y revisado · divulgación · [AP]. "La obesidad es una enfermedad crónica. Aquí se trata."
7. **De hoja a audio** · ElevenLabs u opción de voz del asistente · consulta · [AP]. Para personas con baja visión o baja alfabetización lectora.

**Viñeta clínica (arquetipo compuesto):** hombre de 50-55 años, origen magrebí, español funcional pero limitado, trabajador agrícola, obesidad grado II y diabetes tipo 2, que asiente a todo y no vuelve. Se combinan rasgos de pacientes con barrera idiomática de la zona; se modifican país de origen, sector laboral y composición familiar.

**Dependencias:** capítulos 3 y 4.

**Extensión objetivo:** 4.000 palabras.

---

## Capítulo 7 · Buscar y leer evidencia sin ahogarte

**Subtítulo:** Deep Research, NotebookLM y lectura crítica en el tiempo que de verdad tienes.

**Gancho:** "Un paciente me preguntó por un estudio que había salido en el telediario. No lo había leído. Tardé dos minutos en tenerlo delante y diez en saber qué opinar."

**Los 3 aprendizajes clave**
1. Qué herramienta para qué pregunta: Perplexity y Deep Research para orientarse; Consensus, Scite y Elicit para evidencia; NotebookLM para tus propias fuentes. Ninguna sustituye a PubMed para verificar.
2. Lectura crítica asistida: diseño, población, comparador, tamaño del efecto, conflicto de interés. El modelo estructura; tú juzgas.
3. Cada cita se comprueba. Una referencia con aspecto real que no existe es el error más caro del libro y de tu sesión.

**Casos de uso (7)**
1. **De la duda a la pregunta PICO** · asistente conversacional → Consensus o Elicit · consulta. Ejemplo: mantenimiento de masa muscular durante pérdida de peso farmacológica.
2. **Mis guías, con citas** · NotebookLM con SEEDO, GIRO, ADA/EASD públicas · consulta · [AP]. Preguntar "qué dice GIRO sobre derivación desde AP" y obtener respuesta con fuente.
3. **Un ensayo en diez minutos** · asistente con carga de documento · docencia. Plantilla de lectura crítica de un ensayo de un fármaco para la obesidad, por principio activo.
4. **Del titular al paper** · Perplexity + asistente · divulgación · [AP]. Preparar la respuesta a "he visto en la tele que…", en dos frases y con la fuente.
5. **Mis datos, agregados** · intérprete de código con datos anonimizados o sintéticos · seguimiento de crónicos · [AP]. Evolución de peso y HbA1c del programa de obesidad del centro, sin identificadores.
6. **Alerta mensual de evidencia para el equipo** · Deep Research programado o Scite · docencia · [AP]. Una página al mes para la sesión del centro.
7. **Verificar las referencias de mi sesión** · asistente + PubMed · docencia. Prompt de auditoría de citas y protocolo de comprobación manual.

**Viñeta clínica (arquetipo compuesto):** mujer de 30-35 años, obesidad grado II, que planifica un embarazo y pregunta por la seguridad de continuar o suspender su tratamiento. Se combinan varias consultas preconcepcionales; se modifican edad, paridad y tratamiento concreto. Es el caso que obliga a buscar evidencia bien y rápido.

**Dependencias:** capítulos 2 y 4.

**Extensión objetivo:** 4.000 palabras.

---

## Capítulo 8 · Apoyo a la decisión y asistentes propios

**Subtítulo:** Del chat al asistente con tus guías, y de la calculadora de veinte minutos a la de veinte segundos.

**Gancho:** "Durante años dejé de hacer la prueba de la silla porque interpretar el resultado me costaba más que hacerla. Tres tablas, tres artículos, interpolar a mano. Hoy tardo veinte segundos y la hago en todas las visitas."

**Los 3 aprendizajes clave**
1. El ciclo clínico de seis pasos con IA: representar → hipotetizar → contrastar → falsar → actualizar → auditar. El modelo abre hipótesis; tú las cierras.
2. Un asistente propio (Gema, Project, GPT personalizado) con las guías como base de conocimiento: cómo se construye, cómo se prueba con casos sintéticos y cuándo no fiarse.
3. Máquinas no deterministas creando máquinas deterministas: usar el modelo para construir una calculadora que al mismo dato responde siempre lo mismo. "La determinación no vive dentro del modelo; vive en el proceso que le obligas a seguir."

**Casos de uso (7)**
1. **CASO DESTACADO · La calculadora de condición física** · construida con asistentes de IA (código generado y auditado con Claude y ChatGPT), publicada como app Streamlit de código abierto · consulta y seguimiento de crónicos · [AP]. Tres pruebas (caminata de seis minutos, fuerza de prensión, levantarse de la silla) con percentiles de tres fuentes publicadas (cohorte STAAB 2024, normas internacionales de prensión de Tomkinson 2024, estudio español EXERNET 2012). Evaluación funcional de unos 20 minutos a segundos; 15 pacientes evaluados en la fase inicial; ahora se hacen las tres pruebas en todas las visitas de seguimiento. Se cuenta también lo que la auditoría destapó: interpolación solo por décadas en la caminata, etiqueta errónea por debajo del percentil 10 en la silla, población de referencia no visible en pantalla. Cero datos de pacientes en la herramienta: solo edad, sexo, talla y resultado de la prueba, sin guardar nada. [VERIFICAR: cifras de tiempo son estimación propia de la autora; el impacto clínico está por medir.]
2. **Mi asistente de derivación y tratamiento** · Gema o Project con SEEDO, GIRO y ADA/EASD como fuentes · consulta · [AP]. Responde "¿qué criterios cumple este perfil sintético para derivar?" con cita a la guía.
3. **Ganancia de peso reciente: no cierres el diagnóstico** · modelo de razonamiento · consulta. Caso sintético con hipotiroidismo, fármacos que aumentan peso, apnea y depresión como hipótesis paralelas; salida en hechos / inferencias / ausencias / sesgos.
4. **Semáforo cardiometabólico del cupo** · intérprete de código sobre datos agregados anonimizados · seguimiento de crónicos · [AP]. Quién lleva más de un año sin analítica, quién tiene HbA1c en rango de prediabetes y no está en el programa.
5. **Analítica de seguimiento en tratamiento farmacológico** · asistente conversacional con caso sintético · seguimiento de crónicos. Qué mirar en la analítica de una persona en tratamiento con agonistas del receptor de GLP-1: lo esperable, lo que alerta, lo que se deriva.
6. **Cribado de sarcopenia en obesidad** · calculadora determinista construida con IA o asistente con rúbrica · seguimiento de crónicos · [AP]. Fuerza relativa a la talla, velocidad de la marcha, preguntas SARC-F: un semáforo, no un diagnóstico.
7. **Probar el asistente antes de usarlo** · diez casos sintéticos + rúbrica (fidelidad, priorización, calibración, confusores, acción segura) · docencia. Protocolo de testing en una hora, con registro de fallos.

**Viñeta clínica (arquetipo compuesto):** hombre de 65-70 años, obesidad grado II con pérdida de masa muscular, dolor lumbar y miedo a caerse, cuyos percentiles funcionales están en naranja o rojo en las tres pruebas mientras el peso apenas cambia. Se combinan rasgos de las personas evaluadas con la calculadora en su fase inicial; se modifican edad exacta, talla, resultados numéricos y circunstancias sociales. Es el caso que enseña por qué la función importa más que la báscula.

**Dependencias:** capítulos 4 y 7. Prepara el capítulo 12.

**Extensión objetivo:** 4.500 palabras.

---

## Capítulo 9 · Contenido audiovisual para la consulta y la comunidad

**Subtítulo:** Vídeo, audio e infografías con validación clínica y sin estigma visual.

**Gancho:** "Explico el mecanismo de la saciedad ocho veces al día. Grabé una vez, bien, con un avatar que no se cansa. Ahora lo explico nueve veces, pero con más calma, porque la novena la ve el paciente en casa."

**Los 3 aprendizajes clave**
1. Cada mensaje tiene su formato: audio para quien no lee, vídeo de 60 segundos para lo que se explica con manos, infografía para lo que se recuerda con los ojos.
2. Las herramientas (Canva, HeyGen, ElevenLabs, generadores de imagen) producen; la validación clínica, el disclaimer y los derechos de imagen los pones tú.
3. Estigma visual: cómo se representa a las personas con obesidad importa tanto como lo que se dice. Pedir imágenes dignas es un prompt más.

**Casos de uso (7)**
1. **Vídeo de 60 segundos "qué es la adaptación metabólica"** · guion con asistente + HeyGen o vídeo propio · divulgación. Con checklist de compliance antes de publicar.
2. **Audio para quien no lee** · ElevenLabs sobre texto validado · consulta · [AP]. Hoja de recomendaciones en voz, en el idioma de la persona.
3. **Infografía de sala de espera** · Canva + texto generado · divulgación · [AP]. Una idea, una imagen, el disclaimer.
4. **Guion de reel sanitario** · asistente conversacional · divulgación. Con las siete líneas rojas del Módulo 3 como restricciones del prompt.
5. **Vídeo de preparación de la visita** · HeyGen multiidioma · seguimiento de crónicos · [AP]. Qué traer, qué preguntar, cuánto dura.
6. **Imágenes sin estigma** · generador de imagen · divulgación. Prompt para representar personas con obesidad en actividad, vestidas, con rostro y contexto, nunca "cuerpos sin cabeza".
7. **Podcast interno para residentes** · guion con asistente + grabación · docencia. Diez minutos por episodio, un tema de obesidad en AP.

**Viñeta clínica (arquetipo compuesto):** mujer de 45-50 años, cuidadora principal de un familiar dependiente, obesidad grado II, sin tiempo ni hábito de lectura, que escucha audios mientras cocina. Se combinan rasgos de pacientes cuidadoras; se modifican parentesco, situación laboral y municipio.

**Dependencias:** capítulos 3 y 6.

**Extensión objetivo:** 3.500 palabras.

---

# PARTE III · INTEGRAR

## Capítulo 10 · La jornada del médico de familia, momento a momento

**Subtítulo:** Los cinco momentos y la matriz herramienta × momento.

**Gancho:** "A las ocho abro la agenda: treinta y cuatro pacientes, seis huecos de urgencias, dos domicilios, una sesión y el correo de la inspección. Aquí es donde la IA tiene que caber. Si no cabe aquí, no sirve."

**Los 3 aprendizajes clave**
1. Los cinco momentos del médico de AP (consulta, seguimiento de crónicos, administración y burocracia, docencia y formación, divulgación y comunidad) y qué herramienta encaja en cada uno.
2. La matriz herramienta × momento: una página que resume el libro y se pega en el corcho.
3. Regla del coste de error: cuanto más cerca del paciente, más verificación y menos automatismo.

**Casos de uso (7)**
1. **Preparar la visita en 60 segundos** · herramienta con contrato del servicio de salud · consulta · [AP]. Resumen estructurado de lo pendiente antes de que entre la persona.
2. **Plan anual de revisiones del programa de obesidad** · asistente conversacional sobre el protocolo del centro · seguimiento de crónicos · [AP].
3. **La burocracia de AP** · asistente conversacional sobre plantillas · administración · [AP]. Certificados, respuestas a inspección, justificantes, correos al hospital.
4. **La sesión clínica del jueves** · NotebookLM + asistente · docencia. De la duda de la semana a 15 diapositivas con fuentes.
5. **Calendario mensual de divulgación** · asistente conversacional · divulgación. Cuatro piezas al mes, con disclosure y checklist.
6. **Antes del domicilio** · asistente conversacional con caso anonimizado o herramienta con contrato · consulta · [AP]. Qué explorar, qué preguntar, qué llevar en una visita domiciliaria a una persona con obesidad y movilidad reducida.
7. **Reparto de tareas con enfermería** · asistente conversacional · seguimiento de crónicos · [AP]. Quién hace la antropometría, quién la educación, quién la calculadora funcional.

**Viñeta clínica (arquetipo compuesto):** hombre de 55 años, conductor profesional, obesidad grado II, hipertensión y apnea del sueño sin tratar, que aparece en cuatro momentos de la misma jornada: consulta, informe para renovación del permiso de conducir, coordinación con enfermería y sesión del centro. Se combinan rasgos de varios pacientes con trabajo sedentario y horarios rotatorios; se modifican profesión concreta, empresa y edad.

**Dependencias:** capítulos 4 a 9. Es el capítulo que los integra.

**Extensión objetivo:** 4.000 palabras.

---

## Capítulo 11 · Agentes y automatizaciones realistas

**Subtítulo:** Qué es un agente, qué puede hacer hoy en un centro de salud y las cinco preguntas antes de encenderlo.

**Gancho:** "Me presentaron un agente que 'hacía el seguimiento de los pacientes solo'. Pregunté quién firmaba. Silencio."

**Los 3 aprendizajes clave**
1. Un LLM responde; un agente actúa: cerebro, memoria y herramientas. Tipologías (RAG, ReAct, multiagente) en lenguaje llano.
2. Las cinco preguntas éticas antes de cualquier agente: autonomía, responsabilidad, supervisión, consentimiento, equidad. Si una no tiene respuesta, no se enciende.
3. Automatizaciones realistas en AP: las que no tocan datos de pacientes hoy, y las que solo pueden existir dentro del sistema del servicio de salud.

**Casos de uso (7)**
1. **Agente de revisión de literatura semanal** · Deep Research programado o flujo n8n con Scite · docencia. Una página cada lunes sobre obesidad en AP.
2. **Recordatorios del taller grupal de obesidad** · n8n o automatización de la agenda del centro, sin datos clínicos · seguimiento de crónicos · [AP]. Fecha, lugar y qué traer; nunca diagnóstico ni tratamiento.
3. **Triaje de correo administrativo** · agente sobre el buzón no clínico · administración · [AP]. Clasificar lo de inspección, lo de gerencia y lo de formación; nunca mensajes de pacientes.
4. **Tres agentes para una sesión** · explorador, integrador y auditor en asistentes separados · docencia. Pensamiento crítico sintético aplicado a un tema controvertido (por ejemplo, objetivos de pérdida de peso en mayores).
5. **Diseñar en papel un agente de seguimiento** · sin herramienta · seguimiento de crónicos · [AP]. Ejercicio: qué haría, qué datos necesitaría, quién supervisa, y por qué hoy no se puede construir fuera del sistema del servicio de salud.
6. **RAG sobre los protocolos del centro** · NotebookLM o asistente con documentos internos no clínicos · consulta · [AP]. "¿Cuál es nuestro circuito para derivar a la unidad de obesidad?"
7. **Cuándo no usar un agente** · lista en papel · administración. Siete situaciones en las que el automatismo cuesta más de lo que ahorra.

**Viñeta clínica (arquetipo compuesto):** mujer de 35 años, obesidad grado I, con reloj inteligente y tres aplicaciones de seguimiento, que pide una herramienta que "la vigile" y le diga qué comer cada día. Se combinan varias pacientes con alta demanda tecnológica; se modifican profesión, aplicaciones concretas y situación familiar. Sirve para las cinco preguntas éticas desde la consulta.

**Dependencias:** capítulos 8 y 10.

**Extensión objetivo:** 4.000 palabras.

---

## Capítulo 12 · Construye tu proyecto en siete puntos

**Subtítulo:** Problema, herramienta, datos, solución, validación, impacto, escalabilidad.

**Gancho:** "Mi proyecto empezó con una queja: 'no tengo veinte minutos para esto'. Terminó con una herramienta que hoy usan otros compañeros. En medio hubo ocho semanas, muchos errores y una plantilla de siete puntos."

**Los 3 aprendizajes clave**
1. La plantilla de siete puntos: problema, herramienta, datos, solución, validación, impacto, escalabilidad. Cabe en una página y evita el 80 % de los proyectos que no sirven.
2. Validación honesta: lo que has comprobado y lo que todavía no. Presentar una herramienta sin sus límites es el exceso de seguridad que el capítulo 2 enseñó a detectar.
3. Compartir: código abierto, docencia a otros médicos de familia, comunidad de práctica. Un proyecto de AP escala cuando otro cupo lo usa.

**Casos de uso (7)**
1. **La calculadora funcional, punto por punto** · Streamlit, asistentes de IA para código, fuentes publicadas · consulta y seguimiento de crónicos · [AP]. Hilo conductor del capítulo: cómo se recorrieron los siete puntos, qué se corrigió tras la auditoría y qué queda por medir. Cero datos de pacientes en la herramienta.
2. **Hoja de preparación de visita para tratamiento con agonistas del receptor de GLP-1** · asistente conversacional + plantilla · seguimiento de crónicos · [AP]. Proyecto de una semana.
3. **Escuela de pacientes del centro** · materiales validados de los capítulos 6 y 9 · divulgación · [AP]. Proyecto de un trimestre con enfermería.
4. **Panel de indicadores del programa de obesidad** · intérprete de código o hoja de cálculo sobre datos agregados · administración · [AP]. Sin identificadores, con actualización mensual.
5. **Biblioteca de prompts del equipo** · repositorio Markdown compartido · docencia. Proyecto de un mes, con dueño y versión.
6. **Cuestionario digital de cribado de sarcopenia** · formulario determinista construido con IA · seguimiento de crónicos · [AP]. Versión mínima en dos tardes.
7. **Presentarlo en siete diapositivas** · asistente conversacional · docencia. Del documento de siete puntos a la sesión de 10 minutos.

**Viñeta clínica (arquetipo compuesto):** mujer de 70 años, obesidad grado I con pérdida de fuerza, que en tres meses pasa de naranja a verde en la prueba de la silla mientras su peso baja dos kilos. Se combinan rasgos de personas evaluadas con la calculadora; se modifican edad exacta, cifras y contexto. Es el caso que muestra que "la función mejora antes que el peso, y ahora lo puedo enseñar".

**Dependencias:** capítulos 8, 10 y 11.

**Extensión objetivo:** 4.000 palabras.

---

# PARTE IV · CUIDAR

## Capítulo 13 · Seguridad, responsabilidad y estigma de peso en la era de la IA

**Subtítulo:** Lo que puede salir mal y cómo pararlo antes de que llegue al paciente.

**Gancho:** "Una salida de IA me propuso 'motivar' a una paciente recordándole los riesgos de su peso. Era exactamente lo que llevaba veinte años haciéndole daño. Lo vi porque lo leí; si hubiera pulsado enviar, no."

**Los 3 aprendizajes clave**
1. Taxonomía de lo que sale mal: alucinación, omisión, sesgo, exceso de seguridad, respuesta individualizada disfrazada de general. Cada una con su ejemplo y su antídoto.
2. El sesgo de peso vive en los datos de entrenamiento: los modelos moralizan, culpan y asumen. Se detecta, se corrige en el prompt y se revisa en la salida.
3. Firmas tú: responsabilidad profesional, farmacovigilancia (la IA ayuda a preparar la notificación, no la sustituye) y qué hacer cuando el paciente trae un plan generado por IA.

**Casos de uso (7)**
1. **Auditoría de sesgo de peso en cinco prompts** · tres asistentes en paralelo · consulta. Los mismos cinco prompts, tres modelos, una tabla de frases estigmatizantes detectadas.
2. **La checklist de seguridad, aplicada** · Anexo B sobre tres salidas reales del libro · consulta. Qué se descarta, qué se corrige, qué pasa.
3. **Poner a prueba tu asistente** · casos sintéticos adversariales · docencia. Preguntas trampa: pedir dosis, pedir diagnóstico cerrado, pedir "dieta milagro".
4. **Preparar una notificación de reacción adversa** · asistente conversacional con datos mínimos y principio activo · seguimiento de crónicos · [AP]. Borrador estructurado para el sistema oficial de farmacovigilancia; nunca datos identificables en la herramienta.
5. **"Me lo ha hecho una IA"** · sin herramienta · consulta · [AP]. Guion para revisar con la persona un plan de alimentación o ejercicio generado por un chat, sin ridiculizar ni prohibir.
6. **Política de uso de IA del centro** · asistente conversacional · administración · [AP]. Una página: qué herramientas, qué datos, quién revisa, cómo se registra.
7. **Reescribir sin estigma los textos que ya tenemos** · asistente conversacional · divulgación · [AP]. Hojas, carteles y plantillas del centro, pasados por un prompt de lenguaje centrado en la persona.

**Viñeta clínica (arquetipo compuesto):** mujer de 28 años, obesidad grado I, antecedente de trastorno de la conducta alimentaria en la adolescencia, que recibe por error una hoja generada con IA sin revisar, con lenguaje de culpa y un objetivo de peso concreto. Se combinan situaciones de varias pacientes jóvenes; se modifican edad, profesión y circunstancias del error. Es la continuación de la viñeta del capítulo 3 y la razón de ser de "Nadie te va a decir cuánto tienes que pesar".

**Dependencias:** capítulos 3, 6 y 8.

**Extensión objetivo:** 4.000 palabras.

---

## Capítulo 14 · Tu hoja de ruta y lo que viene

**Subtítulo:** Un plan de 90 días y una mirada honesta al futuro.

**Gancho:** "No hace falta que lo hagas todo. Hace falta que el lunes hagas una cosa. La mía fue una hoja de recomendaciones de 200 palabras. La segunda fue una calculadora."

**Los 3 aprendizajes clave**
1. Hoja de ruta personal a 30, 60 y 90 días: un caso de uso por momento, medido en minutos ahorrados y en algo que antes no hacías.
2. Lo que viene (wearables, genómica, medicina predictiva, agentes autónomos) contado con el mismo escepticismo que el resto del libro: qué es real hoy en AP y qué es promesa.
3. Nadie aprende esto solo: comunidad de práctica en el centro, en el área y en las sociedades científicas.

**Casos de uso (6)**
1. **Mi hoja de ruta con la IA como planificadora** · asistente conversacional · administración. Prompt que convierte el inventario de tiempo del capítulo 1 en un plan de 90 días.
2. **Los datos que trae el paciente** · sin herramienta de IA o asistente con datos agregados que la persona comparte voluntariamente · seguimiento de crónicos · [AP]. Pasos, sueño, frecuencia cardiaca: qué mirar, qué ignorar, qué no meter en ningún chat.
3. **Comunidad de práctica del área** · asistente conversacional para el diseño · docencia · [AP]. Reunión mensual de 45 minutos, tres casos de uso, un proyecto compartido.
4. **Evaluar una herramienta nueva en 15 minutos** · el contrato mental del capítulo 2 · administración. Modelo, versión, plan, contexto, herramientas, coste de error, acuerdo de tratamiento de datos.
5. **Medir mi impacto** · hoja de cálculo · administración · [AP]. Tiempos antes y después, y una variable clínica del programa de obesidad que quieres mover.
6. **La conversación sobre medicina predictiva** · asistente conversacional · consulta. Cómo explicar a una persona con obesidad qué significa un riesgo estimado sin convertirlo en sentencia.

**Viñeta clínica (arquetipo compuesto):** la mujer del capítulo 1, un año después. Mismo arquetipo compuesto, con las mismas modificaciones. Cambia lo que ocurre en la consulta: hoja en su idioma de lectura, calculadora funcional en verde, un mensaje entre visitas y una conversación de siete minutos que no empieza por la báscula.

**Dependencias:** todos los anteriores; cierra el arco abierto en el capítulo 1.

**Extensión objetivo:** 3.500 palabras.

---

# ANEXOS

## Anexo A · Biblioteca de 50 prompts para Atención Primaria en obesidad
Cincuenta prompts organizados por los cinco momentos (diez por momento): nombre, momento, herramienta recomendada y por qué, texto literal en bloque de código con estructura rol · contexto · tarea · formato, variables entre corchetes, nivel de riesgo (bajo / medio / alto) y qué revisar antes de usar la salida. Todos incluyen la instrucción de anonimización; ninguno admite datos identificables. Los prompts de los capítulos se recogen aquí en su versión final. Extensión: 7.000 palabras.

## Anexo B · Checklist de seguridad antes de usar una salida de IA con un paciente
Una página imprimible con diez comprobaciones en cuatro bloques: datos (qué entró y en qué herramienta), contenido (fidelidad, calibración, ausencias, sesgo de peso), forma (nivel de lectura, idioma verificado, disclaimer estándar) y firma (quién revisa, dónde se registra). Incluye la "regla del minuto" y la puntuación de auditoría. Extensión: 800 palabras.

## Anexo C · Glosario
Los términos técnicos del libro definidos en una o dos frases, con el capítulo donde aparecen: IA generativa, LLM, prompt, token, ventana de contexto, alucinación, multimodalidad, modelo de razonamiento, few-shot, cadena de prompts, RAG, agente, acuerdo de tratamiento de datos, anonimización, arquetipo compuesto, disclaimer estándar. Hereda y amplía el glosario de `biblia.md`. Extensión: 1.200 palabras.

## Anexo D · Plantilla de proyecto en siete puntos y recursos
La plantilla de una página (problema, herramienta, datos, solución, validación, impacto, escalabilidad) con preguntas guía para cada punto, el ejemplo rellenado de la calculadora funcional y una lista comentada de recursos: guías (SEEDO, GIRO, ADA/EASD), normativa (RGPD, LOPDGDD, AI Act, RD 1416/1994), herramientas de evidencia y repositorio de código abierto de la calculadora. Todo recurso citado se verifica o se marca [VERIFICAR]. Extensión: 3.000 palabras.

---

# Título elegido por la autora (11-09-2026)

**IA en la consulta: la revolución que cabe en diez minutos.** *Aplicación práctica para el médico de familia ante la obesidad.*

# Títulos alternativos considerados

1. **Diez minutos y una IA.** *Guía práctica de inteligencia artificial para el médico de familia ante la obesidad.*
2. **Es biología, no falta de voluntad.** *Inteligencia artificial en la consulta de Atención Primaria para tratar la obesidad como lo que es.*
3. **Copiloto en consulta.** *Inteligencia artificial para abordar la obesidad desde Atención Primaria.*

**Elección argumentada: el título 1, "Diez minutos y una IA".**

- Nombra a la audiencia desde la primera palabra: "diez minutos" es la consulta de AP, y ningún endocrinólogo hospitalario se reconocería en ella. El libro se distingue en el estante de los manuales genéricos de IA en medicina por su contexto, y el título lo dice antes que el subtítulo.
- Es honesto con el contenido: el libro trata de IA y de tiempo. La frase eje, "Es biología, no falta de voluntad", es la tesis clínica, pero como título de portada anuncia un libro de fisiopatología de la obesidad y desorientaría al lector que busca herramientas. Su sitio está en el título del capítulo 1, en la contraportada y como epígrafe de apertura, donde gana fuerza porque la lectora ya sabe de qué va el libro.
- "Copiloto en consulta" es la metáfora del curso de origen ("la IA es copiloto, no piloto"), y además coincide con el nombre comercial de un producto de software. Ambas cosas restan originalidad y pueden leerse como derivadas.
- El título 1 tiene ritmo, cabe en una portada y en una diapositiva, se recuerda y admite el subtítulo largo que explica el resto. Se recomienda mantener el título de trabajo actual como subtítulo alternativo si la editorial pide más literalidad.
