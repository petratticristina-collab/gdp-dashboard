# Índice v2 · Capítulos 8, 9 y 10 (ARQUITECTO, 15-09-2026)

> Decisión de la autora del 15-09-2026: el libro tiene 10 capítulos y 4 anexos. Los capítulos 1-7 se mantienen como en `indice.md` (v1). Este documento sustituye a las entradas 8-14 de la v1 y las reagrupa en tres capítulos. Equivalencias para la pasada final: antiguos 8 y 12 → 8; antiguos 9, 10 y 11 → 9; antiguos 13 y 14 → 10. Partes: I · Entender (1-3); II · Usar (4-8); III · Integrar y cuidar (9-10). Los compromisos registrados en `biblia.md` con los antiguos 8, 9, 12, 13 y 14 se leen con esa tabla. Regla 20, opción (a): capítulos de la parte II de hasta 10.000 palabras; 350 palabras por prompt como práctica recomendada, no obligatoria.

---

# PARTE II · USAR (continuación)

## Capítulo 8 · Apoyo a la decisión, asistentes propios y tu proyecto en siete puntos

**Subtítulo:** De la calculadora de veinte minutos a la de veinte segundos, y de un chat a un asistente con tus guías.

**Gancho:** "Durante años dejé de hacer la prueba de la silla porque interpretar el resultado me costaba más que hacerla. Tres tablas, tres artículos, interpolar a mano. Hoy tardo veinte segundos y la hago en todas las visitas. En medio hubo ocho semanas, muchos errores y una plantilla de siete puntos."

**Los 3 aprendizajes clave**
1. El ciclo clínico con IA: representar, hipotetizar, contrastar, falsar, actualizar y auditar. El modelo abre hipótesis; tú las cierras. Máquinas no deterministas creando máquinas deterministas: la determinación no vive en el modelo, vive en el proceso que le obligas a seguir.
2. Un asistente propio (Gema, Project, GPT personalizado) con las guías como base de conocimiento: cómo se construye, cómo se prueba con casos sintéticos y cuándo no fiarse. Y una herramienta propia, la calculadora, construida sin contrato de datos y sin ningún dato de paciente dentro de la IA.
3. La plantilla de siete puntos (problema, herramienta, datos, solución, validación, impacto, escalabilidad) cabe en una página y evita la mayoría de los proyectos que no sirven; la validación honesta incluye lo que la auditoría destapó y lo que aún no se ha medido.

**Casos de uso (7)**
1. **La calculadora de condición física, punto por punto** · construida con asistentes de IA (código generado y auditado), publicada como app de código abierto · consulta y seguimiento de crónicos · [AP]. Caso destacado y ejemplo rellenado de la plantilla: tres pruebas (marcha de seis minutos, prensión, silla) con percentiles de tres fuentes publicadas; cero datos de pacientes en la herramienta; lo que la auditoría destapó (interpolación por décadas, etiqueta errónea bajo el percentil 10, población de referencia no visible, disclaimer ausente) y qué se corrigió; lo que queda por medir. Cifras de tiempo como estimación de la autora.
2. **Mi asistente de derivación y tratamiento** · Gema, Project o GPT personalizado con GIRO 2024, Wharton 2020 y NICE NG246 como fuentes · consulta · [AP]. Responde a un perfil sintético con cita a la guía; distingue derivación programada y la que no espera (sospecha de causa secundaria o complicación); la decisión la firma la médica. Continúa el caso 2 del capítulo 7 y cumple la regla 13.
3. **Analítica de seguimiento en tratamiento farmacológico** · asistente conversacional con caso sintético · seguimiento de crónicos. Qué mirar en la analítica de una persona en tratamiento con un fármaco para la obesidad por mecanismo: lo esperable, lo que alerta, lo que se deriva; los compromisos heredados: intensificación con HbA1c 7,6 % y metformina (capítulo 4), ajuste de sulfonilurea o insulina, embarazo y anticoncepción (capítulos 6 y 7), valoración de respuesta a los meses y retirada sin culpa, días de enfermedad. Nota de transparencia (regla 12).
4. **Cribado de sarcopenia en obesidad: función antes que masa** · calculadora determinista o asistente con rúbrica · seguimiento de crónicos · [AP]. Fuerza de prensión, levantarse de la silla, velocidad de la marcha, SARC-F: un semáforo, no un diagnóstico (EWGSOP2). Responde a la pregunta del músculo del capítulo 7.
5. **Probar el asistente antes de usarlo** · diez casos sintéticos, preguntas trampa (pedir dosis, pedir diagnóstico cerrado, pedir "dieta milagro") y la rúbrica del capítulo 4 · docencia. Protocolo de testing en una hora, con registro de fallos; nada se usa con una persona sin pasar por aquí. Absorbe el antiguo caso 13.3.
6. **De la calculadora a un formulario determinista** · asistente que escribe código o formulario, fuentes publicadas · seguimiento de crónicos · [AP]. Cómo se pide código que al mismo dato responde siempre lo mismo; el cuestionario de cribado como versión mínima en dos tardes; qué se le pide al modelo, qué sale mal, cómo se audita. Absorbe el antiguo caso 12.6.
7. **Presentarlo en siete diapositivas y compartirlo** · asistente conversacional · docencia. Del documento de siete puntos a la sesión de diez minutos; código abierto, docencia a otros médicos de familia, comunidad de práctica: un proyecto de Atención Primaria escala cuando otro cupo lo usa. Absorbe los antiguos 12.5 y 12.7.

**Viñeta clínica (arquetipo compuesto):** hombre de 65-70 años, obesidad de grado II con pérdida de masa muscular, dolor lumbar y miedo a caerse, cuyos percentiles funcionales están en naranja o rojo en las tres pruebas mientras el peso apenas cambia; tres meses después, la silla en verde con el peso casi igual. Se combinan rasgos de personas evaluadas con la calculadora en su fase inicial; se modifican edad exacta, talla, resultados numéricos y circunstancias. Enseña por qué la función importa más que la báscula y por qué "la función mejora antes que el peso, y ahora lo puedo enseñar".

**Dependencias:** capítulos 4 y 7. Prepara el 9 (automatizaciones) y el 10 (validación honesta como antídoto del exceso de seguridad).

**Extensión objetivo:** 7.500 palabras (tope 10.000).

---

# PARTE III · INTEGRAR Y CUIDAR

## Capítulo 9 · La jornada del médico de familia: momentos, contenido audiovisual y automatizaciones realistas

**Subtítulo:** Los cinco momentos, la matriz herramienta × momento, lo que se ve y se escucha, y las cinco preguntas antes de encender un agente.

**Gancho:** "A las ocho abro la agenda: treinta y cuatro pacientes, seis huecos de urgencias, dos domicilios, una sesión y el correo de la inspección. Aquí es donde la IA tiene que caber. Si no cabe aquí, no sirve."

**Los 3 aprendizajes clave**
1. Los cinco momentos del médico de familia (consulta, seguimiento de crónicos, administración, docencia, divulgación) y la matriz herramienta × momento: una página que resume el libro y se pega en el corcho. Regla del coste de error: cuanto más cerca de la persona, más verificación y menos automatismo.
2. Cada mensaje tiene su formato: audio para quien no lee, vídeo de 60 segundos para lo que se explica con manos, infografía para lo que se recuerda con los ojos. Las herramientas producen; la validación clínica, el disclaimer, los derechos de imagen y la representación sin estigma los pones tú.
3. Un modelo responde; un agente actúa: cerebro, memoria y herramientas. Las cinco preguntas antes de encenderlo (autonomía, responsabilidad, supervisión, consentimiento, equidad); las automatizaciones realistas hoy son las que no tocan datos de pacientes, y las demás solo dentro del sistema del servicio de salud.

**Casos de uso (8)**
1. **La burocracia de Atención Primaria en plantillas** · asistente conversacional sobre plantillas · administración · [AP]. Justificantes, correos al hospital, respuestas a gerencia; continúa el capítulo 5 (lo que ya se hizo allí se remite).
2. **El calendario mensual de divulgación y el guion de un reel sanitario** · asistente conversacional · divulgación · [AP]. Cuatro piezas al mes con disclosure y checklist; el guion con las siete líneas rojas como restricciones del prompt. Fuente: el protocolo de reels y posts de la memoria.
3. **Audio para quien no lee** · voz del asistente o herramienta de voz sobre texto validado · consulta · [AP]. La hoja del capítulo 6 en voz, en el idioma de la persona; la cuidadora que escucha mientras cocina.
4. **Vídeo de 60 segundos "qué es la adaptación metabólica"** · guion con asistente y vídeo propio o avatar · divulgación. Con la checklist de compliance antes de publicar; derechos de imagen; el texto del capítulo 1 (caso 2) como base.
5. **Imágenes sin estigma y la infografía de sala de espera** · generador de imagen y herramienta de diseño · divulgación · [AP]. Prompt para representar personas con obesidad en actividad, vestidas, con rostro y contexto; el cartel del capítulo 6 diseñado.
6. **Automatizaciones sin datos clínicos** · automatización de agenda o flujo sencillo · seguimiento de crónicos y administración · [AP]. Recordatorios del taller grupal (fecha, lugar, qué traer; nunca diagnóstico ni tratamiento); triaje del buzón administrativo no clínico; búsquedas programadas de evidencia (capítulo 7).
7. **Diseñar en papel un agente de seguimiento, y cuándo no usar ninguno** · sin herramienta · seguimiento de crónicos · [AP]. Qué haría, qué datos necesitaría, quién supervisa, por qué hoy no se construye fuera del sistema del servicio de salud; siete situaciones en las que el automatismo cuesta más de lo que ahorra.
8. **Antes del domicilio** · asistente conversacional con caso sintético · consulta · [AP]. Qué explorar, qué preguntar, qué llevar a una visita domiciliaria a una persona con obesidad y movilidad reducida.

**Viñeta clínica (arquetipo compuesto):** hombre de 55 años, conductor profesional, obesidad de grado II, hipertensión y apnea del sueño sin tratar, que aparece en cuatro momentos de la misma jornada: consulta, informe para la renovación del permiso de conducir, coordinación con enfermería y sesión del centro; y una mujer de 35 años, obesidad de grado I, con reloj inteligente y tres aplicaciones, que pide una herramienta que "la vigile" (las cinco preguntas éticas desde la consulta). Se combinan rasgos de varias personas; se modifican profesión concreta, empresa, aplicaciones y edad.

**Dependencias:** capítulos 3, 5, 6, 7 y 8. Es el capítulo que integra.

**Extensión objetivo:** 8.000 palabras (tope 10.000).

---

## Capítulo 10 · Cuidar: seguridad, estigma y tu hoja de ruta

**Subtítulo:** Lo que puede salir mal y cómo pararlo antes de que llegue a la persona; un plan de 90 días y una mirada honesta al futuro.

**Gancho:** "Una salida de IA me propuso 'motivar' a una paciente recordándole los riesgos de su peso. Era exactamente lo que llevaba veinte años haciéndole daño. Lo vi porque lo leí; si hubiera pulsado enviar, no."

**Los 3 aprendizajes clave**
1. Taxonomía de lo que sale mal: alucinación, omisión, sesgo, exceso de seguridad, respuesta individualizada disfrazada de general. Cada una con su ejemplo del propio libro y su antídoto. El sesgo de peso vive en los datos de entrenamiento: se detecta, se corrige en el prompt y se revisa en la salida.
2. Firmas tú: responsabilidad profesional, farmacovigilancia (la IA ayuda a preparar la notificación, no la sustituye), qué hacer cuando la persona trae un plan generado por IA, y la política de uso del centro.
3. Hoja de ruta personal a 30, 60 y 90 días: un caso de uso por momento, medido en minutos ahorrados y en algo que antes no hacías. Lo que viene (wearables, genómica, medicina predictiva, agentes) con el mismo escepticismo que el resto del libro; nadie aprende esto solo.

**Casos de uso (8)**
1. **Auditoría de sesgo de peso en cinco prompts y tres modelos** · tres asistentes en paralelo · consulta. Los mismos cinco prompts, una tabla de frases estigmatizantes detectadas; continúa el caso 4 del capítulo 3.
2. **La checklist de seguridad, aplicada a tres salidas del libro** · anexo B sobre la hoja del capítulo 1, el texto (B) del capítulo 4 y la carta del capítulo 5 · consulta. Qué se descarta, qué se corrige, qué pasa; la hoja que sustituye "no es culpa suya" por "no depende de usted" (capítulo 6).
3. **Preparar una notificación de reacción adversa** · asistente conversacional con caso inventado y principio activo · seguimiento de crónicos · [AP]. Borrador para ensayar el formulario; los datos reales van directos a notificaRAM.es, nunca por un chat (regla 17).
4. **"Me lo ha hecho una IA"** · sin herramienta · consulta · [AP]. Guion para revisar con la persona un plan de alimentación o ejercicio generado por un chat, sin ridiculizar ni prohibir; los datos que trae del reloj: qué mirar, qué ignorar, qué no meter en ningún chat.
5. **Política de uso de IA del centro y cómo evaluar una herramienta nueva en quince minutos** · asistente conversacional · administración · [AP]. Una página: qué herramientas, qué datos, quién revisa, cómo se registra; el contrato mental del capítulo 2 aplicado a una herramienta nueva.
6. **Reescribir sin estigma los textos que ya tenemos** · asistente conversacional · divulgación · [AP]. Hojas, carteles y plantillas del centro pasados por un prompt de lenguaje centrado en la persona (regla 27).
7. **Mi hoja de ruta de 90 días, con la IA como planificadora, y cómo medir mi impacto** · asistente conversacional y hoja de cálculo · administración · [AP]. Del inventario de tiempo del capítulo 1 a un plan de 30, 60 y 90 días; tiempos antes y después, y una variable clínica del programa que quieres mover (con lo que el capítulo 7 enseñó sobre lo que no se puede concluir).
8. **La conversación sobre riesgo y medicina predictiva** · asistente conversacional · consulta. Cómo explicar a una persona con obesidad qué significa un riesgo estimado sin convertirlo en sentencia; y la comunidad de práctica del área: reunión mensual, tres casos de uso, un proyecto compartido.

**Viñeta clínica (arquetipo compuesto):** la mujer del capítulo 1, un año después. Mismo arquetipo compuesto, con las mismas modificaciones. Cambia lo que ocurre en la consulta: hoja en su idioma de lectura, calculadora funcional en verde, un mensaje entre visitas y una conversación de siete minutos que no empieza por la báscula. La mujer joven del capítulo 3 reaparece en el caso 2 como situación (la hoja sin revisar que llegó a la persona equivocada). Cierre del libro: la maratón de Londres 2025 y la caja de medallas, con la misma función que en el libro anterior: proceso y constancia.

**Dependencias:** todos los anteriores; cierra el arco abierto en el capítulo 1.

**Extensión objetivo:** 8.000 palabras (tope 10.000).

---

# ANEXOS (sin cambios respecto a la v1)

A · Biblioteca de prompts para Atención Primaria en obesidad (los de los capítulos en su versión final, con la ficha del capítulo 4 y las etiquetas de la regla 33). B · Checklist de seguridad antes de usar una salida de IA con un paciente (las diez preguntas del capítulo 3 con las precisiones de las reglas 19, 23, 27 y 28). C · Glosario (hereda y amplía el de `biblia.md`). D · Plantilla de proyecto en siete puntos, el ejemplo rellenado de la calculadora y recursos.
