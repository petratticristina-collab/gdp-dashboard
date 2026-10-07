// Charla 4.º ESO (Biology in English) · Healthy habits & physical activity · Dra. Cristina Petratti
const pptxgen = require("pptxgenjs");
const path = require("path");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const icons = require("react-icons/fa6");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const THEME = { name: "SixtyMinuteQuestion", headFontFace: "Calibri", bodyFontFace: "Calibri",
  colors: { dk1: "0B2E3A", lt1: "FFFFFF", dk2: "0F4C5C", lt2: "EEF5F3", accent1: "C8F23D", accent2: "FF6B57",
            accent3: "2EC4B6", accent4: "FFD166", accent5: "9BB8C2", accent6: "5C7C86", hlink: "0F4C5C", folHlink: "5C7C86" } };
const HX = THEME.colors;

async function icon(name, hex, px = 320) {
  const el = React.createElement(icons[name], { color: "#" + hex, size: px });
  const svg = ReactDOMServer.renderToStaticMarkup(el);
  const buf = await sharp(Buffer.from(svg)).resize(px, px).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10 x 5.625
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.author = "Dra. Cristina Petratti"; pres.title = "La pregunta de los 60 minutos";
  const C = pres.SchemeColor;

  // Layouts
  pres.defineSlideMaster({ title: "DARK", background: { color: HX.dk1 },
    objects: [{ text: { text: "Dra. Cristina Petratti · Médica de familia · Especialista en obesidad", options: { x: 0.5, y: 5.22, w: 6.5, h: 0.3, fontSize: 9, color: HX.accent5, isTextBox: true, margin: 0 } } }],
    slideNumber: { x: 9.2, y: 5.22, w: 0.4, h: 0.3, fontSize: 9, color: HX.accent5 } });
  pres.defineSlideMaster({ title: "LIGHT", background: { color: HX.lt1 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.35, w: 9, h: 0.8, fontSize: 28, bold: true, color: HX.dk1, margin: 0, valign: "middle", align: "left" }, text: "" } },
      { text: { text: "Dra. Cristina Petratti · Médica de familia · Especialista en obesidad", options: { x: 0.5, y: 5.22, w: 6.5, h: 0.3, fontSize: 9, color: HX.accent6, isTextBox: true, margin: 0 } } }],
    slideNumber: { x: 9.2, y: 5.22, w: 0.4, h: 0.3, fontSize: 9, color: HX.accent6 } });
  pres.defineSlideMaster({ title: "ACTIVITY", background: { color: HX.dk2 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.35, w: 9, h: 0.8, fontSize: 28, bold: true, color: HX.accent1, margin: 0, valign: "middle", align: "left" }, text: "" } },
      { text: { text: "Dra. Cristina Petratti · Médica de familia · Especialista en obesidad", options: { x: 0.5, y: 5.22, w: 6.5, h: 0.3, fontSize: 9, color: HX.accent5, isTextBox: true, margin: 0 } } }],
    slideNumber: { x: 9.2, y: 5.22, w: 0.4, h: 0.3, fontSize: 9, color: HX.accent5 } });

  const ic = {};
  for (const [k, n, col] of [["bolt","FaBolt",HX.dk1],["brain","FaBrain",HX.dk1],["bed","FaBed",HX.dk1],["mobile","FaMobileScreen",HX.dk1],
      ["apple","FaAppleWhole",HX.dk1],["heart","FaHeartPulse",HX.dk1],["bone","FaBone",HX.dk1],["smile","FaFaceSmile",HX.dk1],
      ["run","FaPersonRunning",HX.dk1],["dumb","FaDumbbell",HX.dk1],["hand","FaHand",HX.dk1],["question","FaCircleQuestion",HX.dk1],
      ["check","FaCheck",HX.dk1],["x","FaXmark",HX.dk1],["clock","FaClock",HX.dk1],["medal","FaMedal",HX.dk1],["moon","FaMoon",HX.dk1],
      ["stairs","FaStairs",HX.dk1],["bike","FaPersonBiking",HX.dk1],["water","FaGlassWater",HX.dk1],["fire","FaFire",HX.dk1],["flag","FaFlagCheckered",HX.dk1]]) {
    ic[k] = await icon(n, col);
  }

  // helpers
  function iconCircle(slide, img, x, y, d = 0.75, fill = C.accent1) {
    slide.addShape(pres.ShapeType.ellipse, { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill } , objectName: "icon circle"});
    slide.addImage({ data: img, x: x + d * 0.22, y: y + d * 0.22, w: d * 0.56, h: d * 0.56, objectName: "icon" });
  }
  function stat(slide, big, label, x, y, w, bigColor = C.accent1, labelColor = C.background1, bigSize = 60) {
    slide.addText(big, { x, y, w, h: 1.1, fontSize: bigSize, bold: true, color: bigColor, align: "center", isTextBox: true, margin: 0, objectName: "stat" });
    slide.addText(label, { x, y: y + 1.1, w, h: 0.9, fontSize: 14, color: labelColor, align: "center", isTextBox: true, margin: 0, objectName: "stat label", valign: "top" });
  }
  function card(slide, x, y, w, h, img, head, body, dark = false) {
    slide.addShape(pres.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.12, fill: { color: dark ? C.text2 : C.background2 }, line: { color: dark ? C.text2 : C.background2 }, objectName: "card" });
    iconCircle(slide, img, x + 0.2, y + 0.2, 0.6);
    slide.addText(head, { x: x + 0.95, y: y + 0.18, w: w - 1.1, h: 0.62, fontSize: 16, bold: true, color: dark ? C.background1 : C.text1, valign: "middle", isTextBox: true, margin: 0, objectName: "card head" });
    slide.addText(body, { x: x + 0.2, y: y + 0.95, w: w - 0.4, h: h - 1.1, fontSize: 13, color: dark ? C.background2 : C.text1, valign: "top", isTextBox: true, margin: 0, objectName: "card body" });
  }
  function bullets(items, size = 16, color = C.text1) {
    return items.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < items.length - 1, fontSize: size, color, paraSpaceAfter: 6 } }));
  }
  function note(slide, s) { slide.addNotes(s); }

  // ───────────────── 1. TITLE
  pres.addSection({ title: "Opening" });
  let s = pres.addSlide({ masterName: "DARK", sectionTitle: "Opening" });
  s.addText("LA PREGUNTA DE LOS 60 MINUTOS", { x: 0.5, y: 0.9, w: 7.4, h: 1.5, fontSize: 40, bold: true, color: C.accent1, isTextBox: true, margin: 0, objectName: "title" });
  s.addText("Lo que tu cuerpo necesita de verdad a los 15 (y lo que dice la ciencia)", { x: 0.5, y: 2.6, w: 7.4, h: 0.9, fontSize: 20, color: C.background1, isTextBox: true, margin: 0, objectName: "subtitle" });
  s.addText("Biología · 4.º ESO · Una sesión de 50 minutos con la Dra. Cristina Petratti, médica de familia y especialista en obesidad", { x: 0.5, y: 3.7, w: 7.4, h: 0.6, fontSize: 13, color: C.accent5, isTextBox: true, margin: 0, objectName: "meta" });
  iconCircle(s, ic.bolt, 8.3, 0.9, 1.1);
  note(s, `[0:00-0:03] Gancho, sin leer la diapositiva. Entra y no te presentes todavía. Pregunta: "Mano arriba quien ayer movió el cuerpo al menos 60 minutos. No cuenta Educación Física: digo sudar un poco." Cuenta en voz alta. Luego: "Mantén la mano quien durmió 8 horas anoche." Caen casi todas. "Hoy vamos a ver por qué importa, y no va de peso. Va de tu cerebro, tu humor y tus notas."
Después preséntate en dos líneas: médica de familia, 25 años de consulta, especialista en obesidad, el año pasado corrí la maratón de Londres después de tres mudanzas. "Si yo pude volver a empezar a mi edad, vosotros podéis empezar esta semana."`);

  // ───────────────── 2. HANDS-UP POLL
  s = pres.addSlide({ masterName: "ACTIVITY", sectionTitle: "Opening" });
  s.addText("Manos arriba: 4 preguntas honestas", { placeholder: "title" });
  const polls = [["clock", "¿Ayer te moviste al menos 60 minutos?"], ["moon", "¿Anoche dormiste 8 horas o más?"], ["mobile", "¿Más de 3 horas de pantalla ayer (sin contar deberes)?"], ["apple", "¿Has desayunado hoy?"]];
  polls.forEach(([k, t], i) => {
    const x = 0.5 + (i % 2) * 4.6, y = 1.4 + Math.floor(i / 2) * 1.75;
    s.addShape(pres.ShapeType.roundRect, { x, y, w: 4.4, h: 1.5, rectRadius: 0.12, fill: { color: C.text1 }, line: { color: C.text1 }, objectName: "poll card" });
    iconCircle(s, ic[k], x + 0.2, y + 0.38, 0.75);
    s.addText(t, { x: x + 1.15, y: y + 0.2, w: 3.1, h: 1.1, fontSize: 17, bold: true, color: C.background1, valign: "middle", isTextBox: true, margin: 0, objectName: "poll text" });
  });
  s.addText("Sin juicios. Estamos recogiendo datos, como biólogos.", { x: 0.5, y: 4.85, w: 9, h: 0.35, fontSize: 13, italic: true, color: C.accent5, isTextBox: true, margin: 0, objectName: "caption" });
  note(s, `[0:03-0:06] Pregunta de una en una; pide a un voluntario que cuente manos y escriba los cuatro números en la pizarra. Volverás a ellos al final (diapositiva 15). Di: "Este es el conjunto de datos de la clase. España también tiene el suyo. Vamos a comparar."`);

  // ───────────────── 3. GUESS THE NUMBER
  pres.addSection({ title: "The data" });
  s = pres.addSlide({ masterName: "DARK", sectionTitle: "The data" });
  s.addText("Adivina el número", { x: 0.5, y: 0.35, w: 9, h: 0.8, fontSize: 28, bold: true, color: C.accent1, isTextBox: true, margin: 0, objectName: "title" });
  s.addText("De cada 100 adolescentes del mundo de 11 a 17 años, ¿cuántos NO llegan a una hora de actividad física al día?", { x: 0.5, y: 1.3, w: 5.6, h: 1.4, fontSize: 20, color: C.background1, isTextBox: true, margin: 0, objectName: "question" });
  s.addText("A) 25      B) 50      C) 65      D) 81", { x: 0.5, y: 2.9, w: 5.6, h: 0.6, fontSize: 22, bold: true, color: C.accent4, isTextBox: true, margin: 0, objectName: "options" });
  s.addText("Levántate y ve a tu respuesta: A pared izquierda, B frente, C pared derecha, D fondo.", { x: 0.5, y: 3.7, w: 5.6, h: 0.8, fontSize: 14, italic: true, color: C.accent5, isTextBox: true, margin: 0, objectName: "instruction" });
  iconCircle(s, ic.question, 7.2, 1.6, 1.6);
  note(s, `[0:06-0:09] Juego de las cuatro esquinas: se mueven físicamente a la esquina de su respuesta. Ya son 30 segundos de movimiento. La respuesta se revela en la siguiente diapositiva: D, 81 % (Guthold et al., Lancet Child & Adolescent Health 2020; 1,6 millones de estudiantes, 146 países, 2001-2016). Chicas 85 %, chicos 78 %. Pregunta: "¿Por qué creéis que en las chicas es mayor?" Dos respuestas y seguimos, sin sermón.`);

  // ───────────────── 4. REVEAL: world + Spain (native chart)
  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "The data" });
  s.addText("La mayoría no llegamos a la hora", { placeholder: "title" });
  s.addChart(pres.ChartType.bar, [{ name: "% que no llega a 60 min/día", labels: ["Mundo, 11-17 años (2016)", "Chicas, mundo", "Chicos, mundo", "España, 8-16 años (2022)", "España, adolescentes (2022)"], values: [81, 85, 78, 70, 77] }],
    { x: 0.5, y: 1.3, w: 5.6, h: 3.7, barDir: "bar", chartColors: [HX.dk2], showValue: true, dataLabelPosition: "outEnd", dataLabelColor: HX.dk1, dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt", dataLabelFormatCode: "0\"%\"",
      showLegend: false, showTitle: false, catAxisLabelColor: HX.dk1, catAxisLabelFontSize: 11, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" }, valAxisMaxVal: 100, objectName: "chart inactivity" });
  s.addShape(pres.ShapeType.roundRect, { x: 6.4, y: 1.3, w: 3.1, h: 3.7, rectRadius: 0.12, fill: { color: C.background2 }, line: { color: C.background2 }, objectName: "side card" });
  s.addText([{ text: "España, estudio PASOS 2022", options: { bold: true, fontSize: 15, color: C.text1, breakLine: true } },
    { text: "3.201 estudiantes, 245 centros, las 17 comunidades.", options: { fontSize: 12, color: C.text1, breakLine: true, paraSpaceAfter: 8 } },
    { text: "~200 min", options: { bold: true, fontSize: 30, color: C.text2, breakLine: true } },
    { text: "de pantalla al día entre semana. El máximo recomendado es 120.", options: { fontSize: 12, color: C.text1, breakLine: true, paraSpaceAfter: 8 } },
    { text: "19.5% → 32.2%", options: { bold: true, fontSize: 22, color: C.accent2, breakLine: true } },
    { text: "estudiantes que se sentían tristes, preocupados o infelices, de 2019 a 2022.", options: { fontSize: 12, color: C.text1 } }],
    { x: 6.6, y: 1.45, w: 2.7, h: 3.4, valign: "top", isTextBox: true, margin: 0, objectName: "side text" });
  s.addText("Fuentes: Guthold R et al. Lancet Child Adolesc Health 2020. Gasol Foundation, estudio PASOS 2022.", { x: 0.5, y: 5.0, w: 9, h: 0.25, fontSize: 9, color: C.accent6, isTextBox: true, margin: 0, objectName: "source" });
  note(s, `[0:09-0:12] "El problema no sois vosotros. Es un patrón de toda una generación, en todos los países." Señala España: 7 de cada 10. Los adolescentes peor que los niños: la actividad cae justo a vuestra edad. Pregunta: "¿Qué pasa a los 13-14 para que la gente deje de moverse?" (más deberes, móvil, dejar el equipo, vergüenza). Valida todas. Luego: "¿Y qué es exactamente esa hora? Definámosla como científicos."`);

  // ───────────────── 5. WHAT COUNTS (WHO 2020)
  pres.addSection({ title: "What the body needs" });
  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "What the body needs" });
  s.addText("¿Qué cuenta? La receta de la OMS (2020)", { placeholder: "title" });
  card(s, 0.5, 1.3, 2.9, 3.5, ic.clock, "60 minutos al día", "Actividad moderada o vigorosa, de media a lo largo de la semana. Ir rápido al instituto, bailar, fútbol en el patio, bici: todo suma. 10 + 10 + 20 + 20 cuenta.");
  card(s, 3.55, 1.3, 2.9, 3.5, ic.dumb, "3 días a la semana", "Actividad vigorosa y algo que cargue músculos y huesos: sprints, saltos, trepar, flexiones, cargar peso, gimnasio con supervisión. Ahora es cuando se construye el hueso.");
  card(s, 6.6, 1.3, 2.9, 3.5, ic.mobile, "Menos tiempo sentado", "Limita la pantalla de ocio. Un entrenamiento no cancela todo el día sentado: levántate cada hora.");
  s.addText("La prueba del habla: moderado = puedes hablar pero no cantar. Vigoroso = solo te salen unas palabras.", { x: 0.5, y: 4.9, w: 9, h: 0.3, fontSize: 12, italic: true, color: C.accent6, isTextBox: true, margin: 0, objectName: "caption" });
  note(s, `[0:12-0:15] Directrices de la OMS sobre actividad física y comportamiento sedentario, 2020 (5-17 años). Mensaje clave: "algo es mejor que nada". Pregunta: "¿Cuenta ir andando al instituto?" Sí, si vas lo bastante rápido para pasar la prueba del habla. "¿Cuenta Educación Física?" Sí. "¿Cuentan los videojuegos?" Solo si quien se mueve eres tú. Comprobación rápida: que nombren una actividad de cada columna que ya hagan.`);

  // ───────────────── 6. WHY: NOT ABOUT WEIGHT
  s = pres.addSlide({ masterName: "DARK", sectionTitle: "What the body needs" });
  s.addText("¿Por qué? No va de peso", { x: 0.5, y: 0.35, w: 9, h: 0.8, fontSize: 28, bold: true, color: C.accent1, isTextBox: true, margin: 0, objectName: "title" });
  const whys = [["brain", "Cerebro", "Más atención, memoria y mejores notas. El ejercicio libera BDNF, un factor de crecimiento para las neuronas."], ["smile", "Ánimo", "Menos ansiedad y menos síntomas depresivos; en adolescentes, un efecto comparable al de algunos tratamientos."],
    ["bone", "Huesos", "Cerca del 90 % de tu masa ósea adulta se construye antes de los 18-20. Saltar ahora es el plan de pensiones de tu esqueleto."], ["heart", "Corazón y metabolismo", "Corazón más eficiente, mejor sensibilidad a la insulina, tensión más baja, sea cual sea tu talla."],
    ["moon", "Sueño", "Los días activos dan un sueño más profundo. El sueño profundo da días más activos. Un círculo virtuoso."], ["fire", "Regulación de la energía", "El movimiento afina las hormonas que regulan el apetito: leptina, grelina, insulina. Es biología, no fuerza de voluntad."]];
  whys.forEach(([k, h, b], i) => {
    const x = 0.5 + (i % 3) * 3.05, y = 1.35 + Math.floor(i / 3) * 1.85;
    iconCircle(s, ic[k], x, y, 0.65);
    s.addText(h, { x: x + 0.8, y: y - 0.02, w: 2.2, h: 0.4, fontSize: 16, bold: true, color: C.accent1, isTextBox: true, margin: 0, objectName: "why head" });
    s.addText(b, { x: x, y: y + 0.72, w: 2.85, h: 1.0, fontSize: 12, color: C.background1, isTextBox: true, margin: 0, valign: "top", objectName: "why body" });
  });
  s.addText("Fuentes: OMS 2020; Álvarez-Bueno C et al. Pediatrics 2017 (metaanálisis, rendimiento académico); Erickson KI et al. Med Sci Sports Exerc 2019 (cognición).", { x: 0.5, y: 4.95, w: 9, h: 0.25, fontSize: 9, color: C.accent5, isTextBox: true, margin: 0, objectName: "source" });
  note(s, `[0:15-0:19] La diapositiva de biología: tu terreno. Dilo explícitamente: "Soy médica de obesidad y hoy NO voy a hablar de adelgazar. El tamaño de tu cuerpo no es una conducta. Moverte sí lo es, y cambia tu cerebro sea cual sea tu talla." BDNF: factor neurotrófico derivado del cerebro, "abono para las neuronas". Hueso: el pico de masa ósea se alcanza a los veintipocos; la carga que haces ahora decide tu esqueleto a los 70. Hormonas: enlaza con tu campo en una sola frase. Pregunta: "¿Cuál de las seis os sorprende más?"`);

  // ───────────────── 7. MOVEMENT BREAK
  s = pres.addSlide({ masterName: "ACTIVITY", sectionTitle: "What the body needs" });
  s.addText("Laboratorio: 2 minutos con tu corazón", { placeholder: "title" });
  const steps = [["1", "Busca tu pulso (muñeca o cuello). Cuenta 15 segundos y multiplica por 4. Apúntalo."], ["2", "De pie. 30 segundos de sentadillas y 30 segundos de saltos o marcha rápida."], ["3", "Pulso otra vez, 15 segundos × 4. ¿Cuánto ha subido?"], ["4", "¿Puedes hablar pero no cantar? Eso es moderado. ¿Solo unas palabras? Eso es vigoroso."]];
  steps.forEach(([n, t], i) => {
    const y = 1.35 + i * 0.85;
    s.addShape(pres.ShapeType.ellipse, { x: 0.5, y, w: 0.65, h: 0.65, fill: { color: C.accent1 }, line: { color: C.accent1 }, objectName: "step circle" });
    s.addText(n, { x: 0.5, y, w: 0.65, h: 0.65, fontSize: 22, bold: true, color: C.text1, align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "step number" });
    s.addText(t, { x: 1.35, y, w: 5.2, h: 0.65, fontSize: 15, color: C.background1, valign: "middle", isTextBox: true, margin: 0, objectName: "step text" });
  });
  s.addShape(pres.ShapeType.roundRect, { x: 6.9, y: 1.35, w: 2.6, h: 3.3, rectRadius: 0.12, fill: { color: C.text1 }, line: { color: C.text1 }, objectName: "hr card" });
  s.addText([{ text: "Referencia", options: { bold: true, fontSize: 14, color: C.accent1, breakLine: true, paraSpaceAfter: 6 } },
    { text: "En reposo: 60-100 lpm", options: { fontSize: 13, color: C.background1, breakLine: true } },
    { text: "Moderado: ~ 64-76 % del máximo", options: { fontSize: 13, color: C.background1, breakLine: true } },
    { text: "Vigoroso: ~ 77-95 % del máximo", options: { fontSize: 13, color: C.background1, breakLine: true, paraSpaceAfter: 6 } },
    { text: "Máximo ≈ 220 − edad ≈ 205 lpm a los 15 (fórmula aproximada, con mucha variación individual)", options: { fontSize: 11, italic: true, color: C.accent5 } }],
    { x: 7.05, y: 1.5, w: 2.3, h: 3.0, valign: "top", isTextBox: true, margin: 0, objectName: "hr text" });
  iconCircle(s, ic.heart, 7.75, 4.7, 0.5);
  note(s, `[0:19-0:23] Todo el mundo de pie. Quien tenga un motivo médico para no hacer ejercicio es el "cronometrador" y cuenta en voz alta. Seguridad: rodillas blandas, sin competir. Después: recoge tres pares antes/después de voluntarios y escríbelos en la pizarra. Idea: "Vuestro corazón os acaba de enseñar qué se siente con moderado y con vigoroso. Sin app." Rangos de referencia de la clasificación del ACSM por porcentaje del máximo; 220 − edad es una aproximación, dilo.`);

  // ───────────────── 8. MYTH OR FACT
  pres.addSection({ title: "Myth or fact" });
  s = pres.addSlide({ masterName: "DARK", sectionTitle: "Myth or fact" });
  s.addText("¿Mito o realidad? De pie = REALIDAD, sentados = MITO", { x: 0.5, y: 0.35, w: 9, h: 0.8, fontSize: 28, bold: true, color: C.accent1, isTextBox: true, margin: 0, objectName: "title" });
  const myths = ["1 · Para estar en forma necesitas un gimnasio.", "2 · Una hora de deporte cancela un día entero sentado.", "3 · Las bebidas energéticas mejoran el rendimiento deportivo.", "4 · Entrenar fuerza frena el crecimiento.", "5 · Las pantallas antes de dormir cambian la calidad del sueño.", "6 · Saltarse el desayuno adelgaza."];
  s.addText(myths.map((t, i) => ({ text: t, options: { fontSize: 17, color: C.background1, breakLine: i < myths.length - 1, paraSpaceAfter: 8 } })), { x: 0.5, y: 1.3, w: 6.4, h: 3.7, valign: "top", isTextBox: true, margin: 0, objectName: "myths list" });
  iconCircle(s, ic.hand, 7.6, 1.8, 1.5);
  note(s, `[0:23-0:29] Lee de una en una; que se levanten o se queden sentados; pide a una persona de cada lado que defienda su postura en una frase; luego revela (las respuestas están en la siguiente diapositiva). Ritmo: un minuto por afirmación.`);

  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "Myth or fact" });
  s.addText("Las respuestas", { placeholder: "title" });
  const ans = [["x", "MITO", "Gimnasio obligatorio", "Tu cuerpo es el gimnasio: escaleras, flexiones, saltos, cargar bolsas, bailar. La OMS lo cuenta todo."], ["x", "CASI MITO", "Deporte contra sofá", "Entrenar ayuda mucho, pero estar sentado muchas horas seguidas tiene efectos propios. Levántate cada hora."],
    ["x", "MITO", "Bebidas energéticas", "Cafeína + azúcar: corazón acelerado, peor sueño y ninguna mejora probada en adolescentes. Varias comunidades prohíben venderlas a menores."], ["x", "MITO", "Fuerza y crecimiento", "El entrenamiento de fuerza supervisado es seguro y recomendado desde la infancia. Fortalece el hueso; no cierra las placas de crecimiento."],
    ["check", "REALIDAD", "Pantallas y sueño", "La luz y el estímulo retrasan la melatonina y acortan el sueño. El móvil fuera de la habitación es el cambio más eficaz."], ["x", "MITO", "Saltarse el desayuno", "Saltarse comidas suele acabar en compensar después y en peor atención en clase. La comida no es el enemigo; la regularidad es la aliada."]];
  ans.forEach(([k, v, h, b], i) => {
    const x = 0.5 + (i % 3) * 3.05, y = 1.3 + Math.floor(i / 3) * 1.85;
    const col = k === "check" ? C.accent3 : C.accent2;
    iconCircle(s, ic[k], x, y, 0.55, col);
    s.addText(v, { x: x + 0.65, y: y - 0.06, w: 2.3, h: 0.26, fontSize: 10, bold: true, color: k === "check" ? C.accent3 : C.accent2, isTextBox: true, margin: 0, objectName: "verdict" });
    s.addText(h, { x: x + 0.65, y: y + 0.2, w: 2.3, h: 0.36, fontSize: 14, bold: true, color: C.text1, isTextBox: true, margin: 0, objectName: "answer head" });
    s.addText(b, { x, y: y + 0.68, w: 2.85, h: 1.1, fontSize: 11, color: C.text1, isTextBox: true, margin: 0, valign: "top", objectName: "answer body" });
  });
  note(s, `[0:29-0:31] Dedica más tiempo a las bebidas energéticas (muy presentes a los 15-16) y a las pantallas. Fuerza: los posicionamientos de las sociedades de medicina deportiva pediátrica avalan el entrenamiento de fuerza supervisado en niños y adolescentes. Bebidas energéticas: suelen llevar 80-160 mg de cafeína por lata; Galicia aprobó prohibir su venta a menores de 16 y otras comunidades lo siguen; comprueba el estado actual antes de la charla.`);

  // ───────────────── 10. SCREENS & SLEEP (biology of the teenage clock)
  pres.addSection({ title: "Sleep, screens, food" });
  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "Sleep, screens, food" });
  s.addText("Sueño: tu reloj es distinto", { placeholder: "title" });
  stat(s, "8-10 h", "de sueño recomendadas por noche a los 13-18 (Academia Americana de Medicina del Sueño, 2016)", 0.5, 1.3, 2.9, C.text2, C.text1, 44);
  stat(s, "~ 2 h", "más tarde se libera la melatonina en la adolescencia: tus 23:00 son las 21:00 de un adulto", 3.55, 1.3, 2.9, C.text2, C.text1, 44);
  stat(s, "200 min", "de pantalla al día entre semana en España, 8-16 años (PASOS 2022). Máximo recomendado: 120.", 6.6, 1.3, 2.9, C.accent2, C.text1, 44);
  s.addShape(pres.ShapeType.roundRect, { x: 0.5, y: 3.5, w: 9, h: 1.3, rectRadius: 0.12, fill: { color: C.background2 }, line: { color: C.background2 }, objectName: "sleep card" });
  s.addText([{ text: "Piensa, comparte en pareja, cuenta (2 min): ", options: { bold: true, fontSize: 15, color: C.text1 } },
    { text: "¿Qué te hace una noche corta al día siguiente? Atención, humor, hambre, deporte. Luego os cuento qué hacen las hormonas: dormir poco sube la grelina (hambre) y baja la leptina (saciedad). Un cerebro cansado pide azúcar. Es biología, no debilidad.", options: { fontSize: 14, color: C.text1 } }],
    { x: 0.7, y: 3.6, w: 8.6, h: 1.1, valign: "middle", isTextBox: true, margin: 0, objectName: "sleep text" });
  note(s, `[0:31-0:36] El retraso circadiano adolescente es real (trabajos de Carskadon): la melatonina se libera más tarde y el horario escolar temprano choca con la biología. No significa "trasnocha": significa proteger la mañana y sacar el móvil de la habitación. Parejas 2 minutos, recoge 3 respuestas. Sueño y apetito: Spiegel 2004 (Ann Intern Med) y estudios posteriores; basta una frase.`);

  // ───────────────── 11. FOOD WITHOUT DIETS
  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "Sleep, screens, food" });
  s.addText("Comida: sin dietas, tres hábitos", { placeholder: "title" });
  card(s, 0.5, 1.3, 2.9, 2.5, ic.apple, "Come como un atleta mediterráneo", "Fruta, verdura, legumbres, cereales integrales, aceite de oliva, pescado, frutos secos. PASOS muestra que la adherencia cae en la adolescencia. Dale la vuelta una comida a la vez.");
  card(s, 3.55, 1.3, 2.9, 2.5, ic.water, "Bebe agua", "Las bebidas azucaradas y energéticas son el cambio más fácil con el mayor efecto sobre el azúcar que tomas. Agua, y leche si te gusta.");
  card(s, 6.6, 1.3, 2.9, 2.5, ic.clock, "Comidas regulares", "Desayuno, comida, merienda, cena, más o menos a su hora. La regularidad gana a la restricción. Nunca te saltes una comida para compensar.");
  s.addShape(pres.ShapeType.roundRect, { x: 0.5, y: 4.0, w: 9, h: 0.85, rectRadius: 0.12, fill: { color: C.text1 }, line: { color: C.text1 }, objectName: "food banner" });
  s.addText("Votación rápida: ¿cuál de los tres te sería más fácil cambiar esta semana? Puño para el 1, dos dedos para el 2, tres para el 3.", { x: 0.7, y: 4.05, w: 8.6, h: 0.75, fontSize: 15, bold: true, color: C.accent1, valign: "middle", isTextBox: true, margin: 0, objectName: "food vote" });
  note(s, `[0:36-0:39] Sin calorías, sin "alimentos buenos y malos", sin hablar de cuerpos. Si alguien saca el peso: "El tamaño del cuerpo no es un hábito. Los hábitos son cosas que haces. Hoy hablamos de lo que haces." Ultraprocesados en una frase: diseñados para comerse rápido y a menudo; el problema es la frecuencia, no una fiesta. Votación con dedos, cuenta y sigue.`);

  // ───────────────── 12. THE ENVIRONMENT (ALADINO, not blame)
  s = pres.addSlide({ masterName: "DARK", sectionTitle: "Sleep, screens, food" });
  s.addText("No es tu culpa. Es el entorno", { x: 0.5, y: 0.35, w: 9, h: 0.8, fontSize: 28, bold: true, color: C.accent1, isTextBox: true, margin: 0, objectName: "title" });
  stat(s, "36%", "de los niños y niñas españoles de 6 a 9 años viven con sobrepeso u obesidad (ALADINO 2023; era el 40,6 % en 2019)", 0.5, 1.3, 2.9);
  stat(s, "81 %", "de los adolescentes del mundo no llegan a la actividad recomendada (Guthold 2020)", 3.55, 1.3, 2.9);
  stat(s, "1 de 3", "estudiantes españoles se sentían tristes, preocupados o infelices en 2022 (PASOS); en 2019 era 1 de 5", 6.6, 1.3, 2.9);
  s.addText("Pantallas que no se acaban, comida diseñada para comerse rápido, ciudades hechas para coches, horarios que ignoran tu reloj de sueño. El entorno empuja hacia un lado. Los hábitos son tu manera de empujar hacia el otro. Sin culpa. Con estrategia.", { x: 0.5, y: 3.75, w: 9, h: 1.2, fontSize: 15, color: C.background1, isTextBox: true, margin: 0, valign: "top", objectName: "env text" });
  note(s, `[0:39-0:42] Tu mensaje central de "Obesidades sin culpa", adaptado: el entorno obesogénico. La mejora del 40,6 % al 36,1 % demuestra que se puede cambiar, pero no ocurrió en las familias con ingresos por debajo de 18.000 euros: la desigualdad pesa. No mires a ningún alumno en concreto. Mantenlo estructural. Transición: "Así que diseñemos la estrategia. La vuestra."`);

  // ───────────────── 13. DESIGN YOUR WEEK (pairs)
  pres.addSection({ title: "Your plan" });
  s = pres.addSlide({ masterName: "ACTIVITY", sectionTitle: "Your plan" });
  s.addText("Diseña tu semana (parejas, 5 minutos)", { placeholder: "title" });
  const rows = [[{ text: "Hábito", options: { bold: true, color: HX.accent1, fill: { color: HX.dk1 } } }, { text: "Objetivo", options: { bold: true, color: HX.accent1, fill: { color: HX.dk1 } } }, { text: "Mi plan (escríbelo)", options: { bold: true, color: HX.accent1, fill: { color: HX.dk1 } } }],
    ["Moverme", "60 min/día, en trozos (10 + 10 + 20 + 20)", "L ____  M ____  X ____  J ____  V ____  Finde ____"],
    ["Cargar músculos y huesos", "3 días/semana: saltos, escaleras, flexiones, deporte", "¿Qué días? ______  ¿Qué actividad? ______"],
    ["Pantallas", "Apagar 60 min antes de dormir; el móvil carga fuera de la habitación", "Mi hora límite: ____:____   Dónde duerme el móvil: ______"],
    ["Sueño", "8-10 h; misma hora de levantarse (± 1 h el finde)", "Luces fuera: ____   Me levanto: ____"],
    ["Comida", "Agua en vez de bebidas azucaradas; desayuno; una verdura más", "Mi único cambio: ____________________"]];
  s.addTable(rows, { x: 0.5, y: 1.3, w: 9, colW: [1.8, 3.2, 4.0], fontSize: 12, color: HX.lt1, fill: { color: HX.dk1 }, border: { type: "solid", pt: 1, color: HX.dk2 }, rowH: 0.5, valign: "middle", margin: 0.06, objectName: "plan table" });
  s.addText("Regla: un plan que puedas cumplir en una semana mala. Pequeño y seguro gana a grande e imaginario.", { x: 0.5, y: 4.55, w: 9, h: 0.4, fontSize: 13, italic: true, color: C.accent5, isTextBox: true, margin: 0, objectName: "caption" });
  note(s, `[0:42-0:47] Reparte la hoja impresa (la misma tabla). En parejas: cada uno rellena la suya, el compañero pregunta "¿qué te lo impediría?" y ajustan. Pasea entre las mesas; busca planes demasiado grandes ("gimnasio todos los días") y hazlos más pequeños. Recoge dos ejemplos en voz alta.`);

  // ───────────────── 14. LIGHTNING QUIZ
  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "Your plan" });
  s.addText("Quiz relámpago: dedos arriba", { placeholder: "title" });
  const quiz = [["¿Cuántos minutos al día recomienda la OMS?", "A) 20   B) 30   C) 60   D) 90", "C"], ["¿Cuántos días a la semana hay que cargar músculos y huesos?", "A) 1   B) 3   C) 5   D) 7", "B"],
    ["¿Horas de sueño recomendadas a tu edad?", "A) 6-7   B) 7-8   C) 8-10   D) 10-12", "C"], ["¿Porcentaje de estudiantes españoles que no llegan a la hora?", "A) 30   B) 50   C) 70   D) 90", "C"],
    ["¿Qué hormona sube cuando duermes poco y te da más hambre?", "A) Leptina   B) Grelina   C) Insulina   D) Melatonina", "B"]];
  quiz.forEach(([q, o, a], i) => {
    const y = 1.3 + i * 0.72;
    s.addShape(pres.ShapeType.roundRect, { x: 0.5, y, w: 9, h: 0.62, rectRadius: 0.1, fill: { color: C.background2 }, line: { color: C.background2 }, objectName: "quiz row" });
    s.addText([{ text: `${i + 1}. ${q}  `, options: { bold: true, fontSize: 13, color: C.text1 } }, { text: o, options: { fontSize: 13, color: C.text2 } }], { x: 0.7, y, w: 8.0, h: 0.62, valign: "middle", isTextBox: true, margin: 0, objectName: "quiz text" });
    s.addText(a, { x: 8.75, y: y + 0.08, w: 0.6, h: 0.46, fontSize: 16, bold: true, color: C.background1, fill: { color: C.accent2 }, align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "quiz answer" });
  });
  note(s, `[0:47-0:49] Tapa la columna de respuestas con la mano o usa la vista del presentador; las respuestas están en los recuadros rojos. Dedos arriba para A/B/C/D (1-4 dedos). Rápido, alto, divertido. Respuestas: C, B, C, C, B.`);

  // ───────────────── 15. CLOSE: back to the class data + pledge
  s = pres.addSlide({ masterName: "DARK", sectionTitle: "Your plan" });
  s.addText("Nuestros datos. Una cosa, esta semana", { x: 0.5, y: 0.35, w: 9, h: 0.8, fontSize: 30, bold: true, color: C.accent1, isTextBox: true, margin: 0, objectName: "title" });
  s.addText([{ text: "Al empezar contamos manos: 60 min de movimiento, 8 h de sueño, 3+ horas de pantalla, desayuno.", options: { fontSize: 14, color: C.background1, breakLine: true, paraSpaceAfter: 8 } },
    { text: "Si cada uno cambia UNA de esas cuatro cosas esta semana, ¿cómo serían nuestros números dentro de un mes?", options: { fontSize: 14, color: C.background1, breakLine: true, paraSpaceAfter: 8 } },
    { text: "Escribe tu única cosa en la tarjeta. Concreta: qué, cuándo, dónde. No \"hacer más ejercicio\". \"Ir andando al instituto de lunes a jueves, salir a las 7:50.\"", options: { fontSize: 14, color: C.background1 } }],
    { x: 0.5, y: 1.3, w: 5.9, h: 2.8, valign: "top", isTextBox: true, margin: 0, objectName: "close text" });
  s.addShape(pres.ShapeType.roundRect, { x: 6.7, y: 1.35, w: 2.8, h: 2.6, rectRadius: 0.12, fill: { color: C.accent1 }, line: { color: C.accent1 }, objectName: "pledge card" });
  s.addText([{ text: "MI ÚNICA COSA", options: { bold: true, fontSize: 16, color: C.text1, breakLine: true, paraSpaceAfter: 10 } }, { text: "Qué: __________", options: { fontSize: 14, color: C.text1, breakLine: true, paraSpaceAfter: 6 } }, { text: "Cuándo: __________", options: { fontSize: 14, color: C.text1, breakLine: true, paraSpaceAfter: 6 } }, { text: "Dónde: __________", options: { fontSize: 14, color: C.text1 } }],
    { x: 6.9, y: 1.5, w: 2.4, h: 2.3, valign: "top", isTextBox: true, margin: 0, objectName: "pledge text" });
  s.addText("Es biología, no fuerza de voluntad. Y la biología responde a lo que haces, desde la primera semana.", { x: 0.5, y: 4.3, w: 8.1, h: 0.8, fontSize: 16, bold: true, italic: true, color: C.accent4, isTextBox: true, margin: 0, objectName: "closing line" });
  iconCircle(s, ic.medal, 8.9, 4.45, 0.6);
  note(s, `[0:49-0:52] Cierra con tu historia en 60 segundos: tres mudanzas, dos cambios de trabajo y la maratón de Londres 2025 con la camiseta de Argentina; la caja de medallas. No para impresionar: para mostrar que volver a empezar es normal. Última frase, despacio: "Es biología, no fuerza de voluntad. Y la biología responde a lo que haces, desde la primera semana." Agradece al profesor. Ofrece: que repita el recuento de manos dentro de un mes y te cuente los números.`);

  // ───────────────── 16. REFERENCES
  pres.addSection({ title: "References" });
  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "References" });
  s.addText("Referencias (para el profesorado)", { placeholder: "title" });
  const refs = ["World Health Organization. WHO guidelines on physical activity and sedentary behaviour. Geneva: WHO; 2020.",
    "Guthold R, Stevens GA, Riley LM, Bull FC. Global trends in insufficient physical activity among adolescents: a pooled analysis of 298 population-based surveys with 1.6 million participants. Lancet Child Adolesc Health. 2020;4(1):23-35.",
    "Gasol Foundation. Estudio PASOS 2022: actividad física, sedentarismo, estilos de vida y obesidad en la población infantil y adolescente española. Barcelona; 2023.",
    "AESAN. Estudio ALADINO 2023: vigilancia del crecimiento, alimentación, actividad física, desarrollo infantil y obesidad en España. Madrid: Ministerio de Derechos Sociales, Consumo y Agenda 2030; 2024.",
    "Paruthi S, et al. Recommended amount of sleep for pediatric populations: a consensus statement of the American Academy of Sleep Medicine. J Clin Sleep Med. 2016;12(6):785-6.",
    "Álvarez-Bueno C, et al. Academic achievement and physical activity: a meta-analysis. Pediatrics. 2017;140(6):e20171498.",
    "Erickson KI, et al. Physical activity, cognition, and brain outcomes: a review of the 2018 Physical Activity Guidelines. Med Sci Sports Exerc. 2019;51(6):1242-51.",
    "Spiegel K, Tasali E, Penev P, Van Cauter E. Brief communication: sleep curtailment in healthy young men is associated with decreased leptin levels, elevated ghrelin levels, and increased hunger and appetite. Ann Intern Med. 2004;141(11):846-50."];
  s.addText(bullets(refs, 10.5, C.text1), { x: 0.5, y: 1.3, w: 9, h: 3.8, valign: "top", isTextBox: true, margin: 0, objectName: "refs" });
  note(s, `Deja esta diapositiva al profesorado. Todas las cifras de la presentación salen de estas fuentes; las zonas de frecuencia cardiaca son de las clasificaciones del ACSM y la fórmula 220 − edad es una aproximación.`);

  const out = path.join(__dirname, "La_pregunta_de_los_60_minutos_4ESO.pptx");
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("written", out);
})().catch(e => { console.error(e); process.exit(1); });
