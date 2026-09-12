# Prompt para el resumen en audio de NotebookLM

## Cómo usarlo

1. Creá un cuaderno nuevo en NotebookLM.
2. Subí como fuentes: el PDF de las diapositivas (*Building_Clinical_AI_Without_Code*) y el archivo `ponencia_10min.md`.
3. En **Resumen de audio → Personalizar**, pegá el prompt corto (versión A). Si el campo admite más texto, usá la versión B.
4. Idioma de salida: español. Duración sugerida: "Más corto" o "Predeterminada" (10–15 min).

---

## Versión A · Prompt corto (para el campo "Personalizar")

> Generá el audio en español rioplatense, tono profesional y cercano, como una conversación entre dos colegas de salud digital. Tema: el estudio de caso de la Dra. Cristina Petratti, médica endocrinóloga, que construyó un asistente clínico web con IA sin saber programar, aplicando el curso "Building Clinical AI Without Code". Seguí este orden: 1) el problema (20 minutos por paciente cruzando percentiles de condición física en Excel, sin seguimiento longitudinal); 2) el stack (Claude escribe el código, Streamlit publica, Supabase guarda, GitHub versiona); 3) la anatomía del prompt (rol, contexto clínico, rigor matemático con interpolación, semáforo por percentiles, formato estricto); 4) resultados (15 pacientes desde abril, PDF en segundos); 5) las grietas: app abierta sin contraseña, tablas hardcodeadas sin fuente, y la tesis central: "que el código funcione no significa que esté bien"; 6) las prioridades invertidas: seguridad, casos de prueba, lógica y recién al final la estética. Cerrá con la frase: "La IA no reemplaza la validación clínica, pero bien auditada nos devuelve el tiempo para ejercerla". No inventes datos ni cifras que no estén en las fuentes.

---

## Versión B · Prompt extendido (si el campo lo permite)

> **Rol y audiencia.** Sos el guionista de un podcast breve para docentes y profesionales de la salud interesados en IA aplicada. Los oyentes son médicos y formadores; no necesitan que les expliquen qué es un percentil, pero sí qué es un caso de prueba automatizado y por qué importa.
>
> **Idioma y tono.** Español rioplatense neutro (voseo suave, sin modismos excesivos). Registro profesional, científico y humano. Nada de entusiasmo publicitario: es un reporte honesto de un caso clínico-tecnológico, con sus errores incluidos.
>
> **Fuentes.** Basate únicamente en las diapositivas y el guion adjuntos. No agregues cifras, nombres de tablas, herramientas ni resultados que no aparezcan en ellos. Si algo no está en las fuentes, decí explícitamente que la autora no lo reporta.
>
> **Estructura obligatoria (en este orden).**
> 1. Gancho: "veinte minutos por paciente antes de empezar a hablar con el paciente" versus "tres segundos".
> 2. El laberinto de Excel: antropometría, prensión manual, levantarse de la silla, caminata de 6 minutos, cada una con tablas de percentiles por sexo, edad y talla. Cero seguimiento longitudinal.
> 3. La pregunta del curso: pasar de consumidora de Excel a creadora de software asistido por IA.
> 4. Arquitectura en cuatro piezas con sus metáforas: el arquitecto (Claude), el escaparate (Streamlit), el archivo (Supabase), la máquina del tiempo (GitHub).
> 5. Anatomía del prompt exitoso: rol y tecnología, contexto clínico y variables, rigor matemático explícito con interpolación, lógica de semáforo (rojo <P10, naranja <P25, verde hasta P75, azul >P75), formato de salida estricto. Comparalo con una buena indicación médica.
> 6. Resultados: 15 pacientes evaluados desde abril, informe PDF en segundos, semáforos, datos estructurados para análisis estadístico.
> 7. Las grietas: seguridad (app abierta en internet sin contraseña durante meses), trazabilidad (tablas de referencia hardcodeadas sin fuente ni versión) y el espejismo del código: "que funcione no significa que esté bien"; sin casos de prueba automatizados, la IA es un riesgo clínico inaceptable.
> 8. Lecciones: lo que repite, lo que descarta, lo que le falta (usuarios y contraseñas, backups, auditar cambios antes de publicar).
> 9. Prioridades invertidas: seguridad → casos de prueba → lógica matemática → interfaz y PDF.
> 10. Cierre textual: "La estética es el final, no el principio. La inteligencia artificial no reemplaza la validación clínica, pero cuando se la audita correctamente nos devuelve el tiempo necesario para ejercerla."
>
> **Duración.** Entre 8 y 12 minutos. Dedicá al menos un tercio del tiempo a las grietas y las lecciones: son el aporte científico del caso.
>
> **Estilo de diálogo.** Uno de los dos hablantes hace de "docente escéptico" que pregunta cómo se validaron los cálculos y qué pasó con la protección de datos; el otro responde con lo que dicen las fuentes, sin exagerar ni minimizar.
