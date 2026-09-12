# De 20 minutos a segundos
## Ponencia de 10 minutos · Construyendo un asistente clínico web con IA (sin saber programar)

**Autora:** Dra. Cristina Petratti
**Contexto:** presentación final ante el cuerpo docente del curso *Building Clinical AI Without Code*
**Formato:** 12 diapositivas · 10 minutos · 4 actos · ~1.050 palabras habladas (ritmo tranquilo, 130 palabras/min, más pausas)

---

## Estructura en cuatro actos

| Acto | Diapositivas | Tiempo | Función dramática |
|---|---|---|---|
| I · El problema | 1 – 3 | 0:00 – 2:30 | Que el jurado *sienta* las 20 minutos perdidos |
| II · La construcción | 4 – 7 | 2:30 – 6:30 | Mostrar el método del curso aplicado a un caso real |
| III · Las grietas | 8 – 9 | 6:30 – 8:10 | Honestidad científica: lo que salió mal |
| IV · Lecciones y cierre | 10 – 12 | 8:10 – 10:00 | Convertir el error en criterio |

Regla de oro del guion: **una idea por diapositiva, un dato por idea, una pausa por dato.**

---

## Guion palabra por palabra

### Diapositiva 1 · Portada — *De 20 minutos a segundos* (0:00 – 0:45)

**Puesta en escena:** entrás con la diapositiva ya proyectada. No la leas. Mirá al jurado, esperá dos segundos de silencio y arrancá con la cifra.

> Buenas tardes. Veinte minutos. Ese era el tiempo que yo dedicaba, por paciente, a cruzar datos en Excel *antes* de empezar a hablar con esa persona. Hoy tarda tres segundos.
>
> Lo que voy a presentar es un estudio de caso: mi consultorio, mis pacientes, mi planilla. Cómo construí un asistente clínico web con inteligencia artificial sin saber programar, aplicando lo que aprendimos en este curso. Y, sobre todo, qué grietas descubrí después, porque de esos errores aprendí más que del éxito.

**Animación sugerida:** el reloj digital pasa de 20:00 a 00:03 al hacer clic (efecto *Aparecer* sobre el reloj verde).

---

### Diapositiva 2 · El laberinto de Excel (0:45 – 1:45)

**Puesta en escena:** señalá el diagrama de flechas. Dejá que el caos visual hable; vos aportás el contexto clínico.

> En medicina de la obesidad no alcanza con pesar y medir. Evaluamos condición física: antropometría, fuerza de prensión manual con dinamómetro, test de levantarse de la silla y caminata de seis minutos.
>
> Cada resultado tiene que ubicarse en su tabla de percentiles, y esas tablas dependen del sexo, la edad y la talla. Para cada persona yo tenía que evaluar, buscar cada valor en su tabla, cruzarlo, interpretarlo, redactar el informe y compararlo con la visita anterior. Todo a mano.
>
> Este diagrama no es una exageración: es un mapa fiel de mi Excel. Evaluar la condición física me consumía más tiempo que la consulta médica en sí.

**Animación sugerida:** que las flechas rojas y grises aparezcan en dos tandas (*Fundido de entrada*), para que el "laberinto" se construya delante del jurado.

---

### Diapositiva 3 · El costo real del método manual (1:45 – 2:30)

**Puesta en escena:** tres cifras, tres pausas. Marcá cada número con la mano. La tercera es la que importa: bajá la voz.

> Traducido a costo: veinte minutos por paciente invertidos únicamente en cruzar datos. Cien por ciento del trabajo hecho a mano y repetido, idéntico, en cada visita.
>
> Y el dato más grave: cero seguimiento longitudinal. Todo ese esfuerzo no generaba un historial evolutivo. Con la obesidad, una enfermedad crónica, lo que importa es la trayectoria del paciente, y mi método la borraba en cada consulta.

**Animación sugerida:** los tres paneles aparecen de a uno, de izquierda a derecha, al ritmo de tu voz.

---

### Diapositiva 4 · La pregunta (2:30 – 3:00)

**Puesta en escena:** este es el punto de giro. Una sola frase, lenta. Podés dar un paso hacia el jurado.

> Y entonces apareció la pregunta que da origen a este curso: ¿y si construyo una calculadora web… sin saber programar?
>
> Ese es el salto que se nos propuso: dejar de ser consumidoras de Excel para convertirnos en creadoras de software asistido por inteligencia artificial.

**Animación sugerida:** el cursor verde parpadeando; la frase aparece como si se tipeara (*Máquina de escribir* o entrada por caracteres).

---

### Diapositiva 5 · La arquitectura del asistente (3:00 – 4:15)

**Puesta en escena:** recorré el círculo en sentido horario, empezando por Claude. Usá las metáforas del curso; el jurado las conoce y valora que las hayas internalizado.

> La solución tiene cuatro piezas, y ninguna la programé yo.
>
> Primero, el arquitecto: Claude. Yo describo en castellano lo que necesito, usando chat y agentes, y el modelo escribe el código.
>
> Segundo, el escaparate: Streamlit. Publica la aplicación en internet y la hace usable desde el celular, en el consultorio, sin instalar nada.
>
> Tercero, el archivo: Supabase, una base de datos. Guarda pacientes y evaluaciones, y eso es lo que finalmente permite ver la evolución histórica que Excel me negaba.
>
> Cuarto, la máquina del tiempo: GitHub. Guarda el código y cada versión; si algo se rompe, puedo volver atrás.
>
> Este es el *stack* completo que nos enseñó el curso: modelo de lenguaje, interfaz, base de datos y control de versiones.

**Animación sugerida:** cada nodo se enciende al hacer clic, en orden 1 → 4, con su texto.

---

### Diapositiva 6 · Anatomía de un prompt exitoso (4:15 – 5:30)

**Puesta en escena:** esta es la diapositiva más "técnica" y la que más valoran los docentes. Señalá cada color mientras nombrás su función. Es tu demostración de método.

> ¿Cómo se le habla a la IA para que el resultado sirva en una consulta? Este es el prompt real que usé, y tiene cinco componentes que aprendimos a exigir.
>
> En azul, asignación de rol y tecnología: "Sos un desarrollador senior de Python y Streamlit".
>
> En naranja, contexto clínico y variables: sexo, edad y el resultado de la prueba de fuerza de prensión en kilogramos.
>
> En rojo, rigor matemático explícito: buscá el percentil en esta tabla, e interpolá si el valor cae entre dos filas. Si no lo pido, el modelo redondea, y en clínica redondear es equivocarse.
>
> En verde, la lógica de visualización clínica: un semáforo. Rojo por debajo del percentil 10, naranja por debajo del 25, verde hasta el 75, azul por encima.
>
> Y en amarillo, formato de salida estricto: código completo, listo para pegar, sin explicaciones.
>
> La lección: un buen prompt se escribe igual que una buena indicación médica. Quién, para qué, con qué datos, con qué criterios y en qué formato.

**Animación sugerida:** los recuadros de color se iluminan uno por uno en el orden azul → naranja → rojo → verde → amarillo.

---

### Diapositiva 7 · El resultado (5:30 – 6:30)

**Puesta en escena:** mirá primero a la izquierda ("el pasado"), después a la derecha ("el presente"). Es la diapositiva de la satisfacción; permitite sonreír.

> El resultado. A la izquierda, el pasado: veinte minutos por paciente, múltiples hojas de Excel, cruce manual propenso a errores, datos aislados.
>
> A la derecha, el presente: quince pacientes evaluados con el asistente desde abril. Un informe en PDF generado en segundos. Interpretación visual por semáforos, que el paciente entiende de un vistazo. Y datos estructurados, listos para análisis estadístico.
>
> Pasamos de datos aislados a información clínica accionable. Y si mi historia terminara acá, sería una historia de éxito. Pero no termina acá.

**Animación sugerida:** el semáforo central se enciende de arriba a abajo; después aparecen las cuatro tarjetas verdes.

---

### Diapositiva 8 · Funciona a diario, pero tenía grietas (6:30 – 7:20)

**Puesta en escena:** cambio de tono. Más pausado, más grave. Este acto es el que te distingue como profesional científica: reportar lo que salió mal.

> La aplicación funciona a diario. Pero tenía grietas críticas que yo no veía.
>
> Primera grieta: seguridad. La aplicación quedó abierta en internet, sin contraseña, durante meses. Datos de pacientes. Yo no lo pensé porque estaba concentrada en que funcionara.
>
> Segunda grieta: trazabilidad. Las tablas de referencia clínica quedaron incrustadas dentro del código, "hardcodeadas", sin citar la fuente ni el número de versión. Si mañana se publica una nueva tabla de percentiles, ¿cómo sé cuál está usando mi calculadora? No lo sé.

**Animación sugerida:** las grietas rojas del bloque de concreto aparecen con *Fundido* al mencionar cada una; los dos recuadros rojos entran después.

---

### Diapositiva 9 · El espejismo del código (7:20 – 8:10)

**Puesta en escena:** es la tesis central de la ponencia. Decila mirando al jurado, sin mirar la pantalla.

> Y la tercera grieta es la más importante, porque es conceptual. El espejismo del código: que "funcione" no significa que esté "bien".
>
> El código corría perfectamente. La pantalla decía "ejecutado con éxito". Pero no había forma de saber si el cálculo de un percentil era correcto sin recalcularlo a mano. Es decir, sin volver al método que quería reemplazar.
>
> El insight clínico es este: sin casos de prueba automatizados que validen la lógica matemática, la IA es un riesgo clínico inaceptable. Un fármaco se aprueba con ensayos. Un cálculo clínico también necesita los suyos.

**Animación sugerida:** la X roja aparece sobre la ventana "Ejecutado con éxito" con *Aparecer*, un golpe seco, sin transición suave.

---

### Diapositiva 10 · Lecciones de la trinchera clínica (8:10 – 8:55)

**Puesta en escena:** tres semáforos, tres frases cortas. Ritmo ágil.

> Lecciones de la trinchera clínica, en tres colores.
>
> Verde, lo que repito: usar la calculadora en cada consulta, y exigirle siempre a la IA el código completo, nunca fragmentos aislados que después no sé dónde pegar.
>
> Rojo, lo que descarto: confiar ciegamente en que "corre". Si no hay casos de prueba con resultados conocidos, el código no sirve para la práctica médica.
>
> Naranja, lo que me falta: control de usuarios y contraseñas, copias de seguridad, y aprender a auditar los cambios antes de publicarlos.

**Animación sugerida:** cada fila entra desde la izquierda con *Desplazar*, en orden verde → rojo → naranja.

---

### Diapositiva 11 · Si empezara hoy de nuevo (8:55 – 9:35)

**Puesta en escena:** señalá la pirámide de la izquierda, después la de la derecha. La clave es la palabra "invertidas".

> Si empezara hoy de nuevo, invertiría las prioridades.
>
> Cómo lo hice: primero el PDF bonito, después la interfaz, después la lógica matemática y, al final, seguridad y casos de prueba… que quedaron olvidados.
>
> Cómo lo haría hoy, y cómo el curso nos enseñó a hacerlo: primero seguridad, contraseñas y accesos. Segundo, casos de prueba con validación clínica garantizada. Tercero, la lógica matemática. Y recién al final la interfaz y el PDF bonito.

**Animación sugerida:** la pirámide de la izquierda se desmorona (bloques que caen con *Salida flotante*); la de la derecha se construye desde la base, bloque por bloque.

---

### Diapositiva 12 · Cierre — *La estética es el final, no el principio* (9:35 – 10:00)

**Puesta en escena:** frase final de memoria. Pausa. Agradecé. No digas "y eso es todo".

> La estética es el final, no el principio.
>
> La inteligencia artificial no reemplaza la validación clínica. Pero cuando se la audita correctamente, nos devuelve el tiempo necesario para ejercerla. Veinte minutos que hoy vuelven a ser de mi paciente.
>
> Muchas gracias.

**Animación sugerida:** ninguna. La imagen de la consulta a la izquierda y el código a la derecha ya dicen todo; que la frase quede quieta.

---

## Preguntas probables del jurado y respuestas breves

1. **¿De dónde salen las tablas de percentiles y cómo garantizás que sean las correctas?**
   Hoy están incrustadas en el código sin cita ni versión: es la grieta de trazabilidad que reconozco. El próximo paso es moverlas a un archivo de datos separado, con fuente bibliográfica, año y versión, y cargar en el prompt la referencia exacta.

2. **¿Validaste los cálculos?**
   Solo por recálculo manual en casos aislados. La prioridad inmediata es un banco de casos de prueba: valores de entrada con percentil esperado conocido, incluidos los bordes (valor exactamente en una fila, valor entre dos filas, extremos de la tabla), que se ejecute automáticamente cada vez que la IA modifica el código.

3. **¿Y la protección de datos de los pacientes?**
   La aplicación estuvo abierta sin contraseña; ya lo corregí como prioridad uno. Además, corresponde: autenticación, cifrado, consentimiento informado para el registro digital, minimización de datos identificatorios y copias de seguridad, de acuerdo con la normativa de protección de datos de salud que aplique en la jurisdicción.

4. **¿Cuánto tiempo real ahorrás?**
   El cruce de datos pasó de unos 20 minutos a segundos. Lo que no se elimina, y no debe eliminarse, es el tiempo de interpretación clínica y la conversación con el paciente.

5. **¿La IA puede introducir errores silenciosos al modificar el código?**
   Sí, y ese es el argumento central de la ponencia. Por eso: casos de prueba antes de cada publicación, control de versiones en GitHub para poder volver atrás y auditoría del cambio antes de desplegarlo.

6. **¿Es reproducible por otro colega?**
   Sí: el stack es gratuito y el prompt está documentado. La condición es que ese colega aplique el orden de prioridades invertidas desde el día uno.

---

## Checklist de ensayo

- Cronometrá tres pasadas completas. Objetivo: 9:30 – 10:00. Si te pasás, recortá en la diapositiva 5 (arquitectura), nunca en la 9 (tesis).
- Memorizá de corrido las tres frases ancla: *"Veinte minutos"* (inicio), *"Que funcione no significa que esté bien"* (centro), *"La estética es el final, no el principio"* (cierre).
- Tené una impresión del prompt de la diapositiva 6 por si preguntan por los detalles del texto.
- Llevá un caso de ejemplo (sexo, edad, kilos de prensión y percentil resultante) para responder con un número concreto si piden una demostración.
