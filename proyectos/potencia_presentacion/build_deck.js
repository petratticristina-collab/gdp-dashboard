const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");
const fs = require("fs");

// ---------- palette ----------
const NAVY = "0F2B3C", TEAL = "0E7C86", CYAN = "22B8CF", CORAL = "E4572E";
const LIGHT = "F2F6F7", INK = "1B2A34", MUTED = "5C6B73", WHITE = "FFFFFF", GREEN = "388E3C";
const HFONT = "Cambria", BFONT = "Calibri";

async function icon(name, color, size = 256) {
  const el = React.createElement(fa[name], { color: "#" + color, size });
  const svg = ReactDOMServer.renderToStaticMarkup(el);
  const buf = await sharp(Buffer.from(svg)).resize(size, size).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  pres.author = "Dra. Cristina Petratti";
  pres.title = "De 20 minutos a 20 segundos · potencIA 2026";

  const W = 13.33, H = 7.5;
  const ic = {};
  for (const [k, n, c] of [
    ["clock", "FaClock", CORAL], ["robot", "FaRobot", CYAN], ["db", "FaDatabase", TEAL],
    ["check", "FaCheckCircle", TEAL], ["chart", "FaChartLine", TEAL], ["rocket", "FaRocket", CYAN],
    ["shield", "FaShieldAlt", TEAL], ["doc", "FaUserMd", CYAN], ["chat", "FaComments", TEAL],
    ["cogs", "FaCogs", TEAL], ["walk", "FaWalking", TEAL], ["grip", "FaHandRock", TEAL],
    ["chair", "FaChair", TEAL], ["book", "FaBook", TEAL], ["mega", "FaBullhorn", TEAL],
    ["list", "FaClipboardList", TEAL], ["search", "FaSearch", TEAL], ["code", "FaCode", CYAN],
    ["layers", "FaLayerGroup", CYAN], ["quote", "FaQuoteLeft", CYAN], ["heart", "FaHeartbeat", TEAL],
    ["file", "FaFileMedical", TEAL], ["users", "FaUsers", TEAL], ["bolt", "FaBolt", CYAN],
    ["lock", "FaLock", TEAL], ["eye", "FaEye", TEAL], ["sitemap", "FaSitemap", CYAN],
    ["ban", "FaBan", CORAL], ["lightbulb", "FaLightbulb", CYAN], ["stairs", "FaSortAmountUp", CYAN],
    ["clockW", "FaClock", WHITE], ["boltW", "FaBolt", WHITE],
  ]) ic[k] = await icon(n, c);

  const notes = (s, t) => s.addNotes(t);

  // helpers
  function title(s, txt, opts = {}) {
    s.addText(txt, { x: 0.6, y: 0.3, w: W - 1.2, h: 1.1, fontFace: HFONT, fontSize: 28, bold: true,
      color: opts.color || NAVY, isTextBox: true, margin: 0, valign: "middle" });
  }
  function circleIcon(s, key, x, y, d = 0.7, fill = LIGHT) {
    s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill } });
    s.addImage({ data: ic[key], x: x + d * 0.22, y: y + d * 0.22, w: d * 0.56, h: d * 0.56 });
  }
  function card(s, x, y, w, h, fill = WHITE) {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: fill },
      line: { color: "E1E8EB", width: 0.75 }, shadow: { type: "outer", blur: 6, offset: 2, angle: 90, color: "000000", opacity: 0.10 } });
  }
  function footer(s, dark = false) {
    s.addText("Dra. Cristina Petratti · potencIA 2026 · Proyecto final", { x: 0.6, y: H - 0.45, w: 8, h: 0.3,
      fontFace: BFONT, fontSize: 10, color: dark ? "8FA6B2" : MUTED, isTextBox: true, margin: 0 });
  }

  // ---------- 1. Portada ----------
  {
    const s = pres.addSlide();
    s.background = { color: NAVY };
    s.addShape(pres.shapes.OVAL, { x: 9.2, y: -1.6, w: 6.2, h: 6.2, fill: { color: TEAL, transparency: 70 }, line: { color: TEAL, transparency: 70 } });
    s.addShape(pres.shapes.OVAL, { x: 10.6, y: 3.4, w: 4.4, h: 4.4, fill: { color: CYAN, transparency: 80 }, line: { color: CYAN, transparency: 80 } });
    s.addText("Proyecto final · potencIA 2026 · Impulsa tu práctica asistencial con IA", { x: 0.7, y: 0.7, w: 9, h: 0.4, fontFace: BFONT, fontSize: 14, color: CYAN, isTextBox: true, margin: 0 });
    s.addText("De 20 minutos\na 20 segundos", { x: 0.7, y: 1.5, w: 9.5, h: 2.6, fontFace: HFONT, fontSize: 60, bold: true, color: WHITE, isTextBox: true, margin: 0, valign: "top", lineSpacingMultiple: 0.95 });
    s.addText("Cómo, para qué y con qué uso la inteligencia artificial en mi consulta de obesidad", { x: 0.7, y: 4.25, w: 8.6, h: 0.9, fontFace: BFONT, fontSize: 20, color: "CADCE3", isTextBox: true, margin: 0 });
    s.addText([
      { text: "Dra. Cristina Petratti", options: { bold: true, breakLine: true } },
      { text: "Médica de familia · Especialista en obesidad · SEEDO · Alicante", options: {} },
    ], { x: 0.7, y: 5.6, w: 9, h: 0.9, fontFace: BFONT, fontSize: 16, color: WHITE, isTextBox: true, margin: 0 });
    notes(s, "Buenos días. Soy Cristina Petratti, médica de familia, especialista en obesidad. Este es mi proyecto final: una herramienta que convirtió una tarea de veinte minutos en una de veinte segundos. Pero más que la herramienta, quiero contaros cómo he cambiado mi forma de trabajar con la IA durante estas ocho semanas.");
  }

  // ---------- 2. Desde dónde hablo ----------
  {
    const s = pres.addSlide();
    title(s, "Desde dónde hablo");
    // left: bio
    circleIcon(s, "doc", 0.6, 1.6);
    s.addText([
      { text: "Más de 25 años de consulta", options: { bold: true, breakLine: true } },
      { text: "Médica de familia. Especialista en obesidad y salud metabólica. Miembro de la SEEDO. Consulta en El Campello, Alicante.", options: {} },
    ], { x: 1.5, y: 1.5, w: 5.4, h: 1.2, fontFace: BFONT, fontSize: 14, color: INK, isTextBox: true, margin: 0, valign: "top" });
    circleIcon(s, "heart", 0.6, 3.0);
    s.addText([
      { text: "Mi frase de cabecera", options: { bold: true, breakLine: true } },
      { text: "“Es biología, no falta de voluntad.” La obesidad es una enfermedad crónica, compleja y con biología detrás. Eso cambia cómo se mide, cómo se trata y cómo se habla con la persona.", options: {} },
    ], { x: 1.5, y: 2.9, w: 5.4, h: 1.5, fontFace: BFONT, fontSize: 14, color: INK, isTextBox: true, margin: 0, valign: "top" });
    circleIcon(s, "walk", 0.6, 4.6);
    s.addText([
      { text: "Por qué me importa la función física", options: { bold: true, breakLine: true } },
      { text: "En obesidad, el peso cuenta poco si no sé cómo camina, cuánta fuerza tiene y si puede levantarse de una silla. La capacidad funcional predice más que el IMC.", options: {} },
    ], { x: 1.5, y: 4.5, w: 5.4, h: 1.5, fontFace: BFONT, fontSize: 14, color: INK, isTextBox: true, margin: 0, valign: "top" });
    // right: transparency card
    card(s, 7.6, 1.5, 5.1, 4.6, LIGHT);
    s.addImage({ data: ic["shield"], x: 7.95, y: 1.85, w: 0.5, h: 0.5 });
    s.addText("Transparencia", { x: 8.6, y: 1.8, w: 3.8, h: 0.6, fontFace: HFONT, fontSize: 20, bold: true, color: NAVY, isTextBox: true, margin: 0, valign: "middle" });
    s.addText([
      { text: "Declaro conflicto de interés con Novo Nordisk: he recibido formación en programas patrocinados por la compañía, entre ellos este.", options: { breakLine: true, paraSpaceAfter: 8 } },
      { text: "Esta presentación es formativa e independiente. No menciona nombres comerciales de medicamentos de prescripción: los fármacos se citan por principio activo o clase terapéutica.", options: { breakLine: true, paraSpaceAfter: 8 } },
      { text: "Ningún dato de esta charla procede de pacientes reales.", options: { bold: true } },
    ], { x: 7.95, y: 2.55, w: 4.45, h: 3.3, fontFace: BFONT, fontSize: 13, color: INK, isTextBox: true, margin: 0, valign: "top" });
    footer(s);
    notes(s, "Antes de nada, transparencia: tengo conflicto de interés con Novo Nordisk, patrocinador de este programa. Lo digo al principio porque es lo que aprendimos en el módulo de compliance: declarar de más no cuesta nada; declarar de menos, mucho. Y una segunda cosa: nada de lo que veréis viene de pacientes reales.");
  }

  // ---------- 3. Para qué uso la IA ----------
  {
    const s = pres.addSlide();
    title(s, "Para qué uso la IA: los cinco momentos de mi jornada");
    const items = [
      ["chat", "Consulta", "Ordenar el caso antes de decidir. Convertir notas sueltas en una nota estructurada sin inventar huecos."],
      ["heart", "Seguimiento de crónicos", "Ver la tendencia, no la foto: peso, cintura, HbA1c, función. Y ahora, percentiles funcionales al instante."],
      ["list", "Administración", "Cartas a especializada, informes, hojas de paciente en el idioma de cada persona."],
      ["book", "Docencia y evidencia", "Buscar con Consensus, Elicit, Scite y OpenEvidence. Leer papers con espíritu crítico, no con fe."],
      ["mega", "Divulgación", "Reels y posts con guion, disclaimer y checklist de compliance antes de publicar."],
    ];
    const cw = 2.36, gap = 0.2, x0 = 0.6, y0 = 1.6, ch = 4.3;
    items.forEach(([k, h, d], i) => {
      const x = x0 + i * (cw + gap);
      card(s, x, y0, cw, ch);
      circleIcon(s, k, x + 0.25, y0 + 0.3, 0.7, LIGHT);
      s.addText(h, { x: x + 0.2, y: y0 + 1.15, w: cw - 0.4, h: 0.7, fontFace: HFONT, fontSize: 16, bold: true, color: NAVY, isTextBox: true, margin: 0, valign: "top" });
      s.addText(d, { x: x + 0.2, y: y0 + 1.9, w: cw - 0.4, h: 2.2, fontFace: BFONT, fontSize: 12.5, color: INK, isTextBox: true, margin: 0, valign: "top" });
    });
    s.addText("La IA es copiloto, no piloto. El modelo razona, estructura y redacta; yo verifico y firmo.", { x: 0.6, y: 6.15, w: 12, h: 0.5, fontFace: BFONT, fontSize: 14, italic: true, color: TEAL, isTextBox: true, margin: 0 });
    footer(s);
    notes(s, "El módulo siete nos pidió mapear nuestra jornada en cinco momentos y cruzarla con herramientas. Este es mi mapa. Lo importante no es la lista de herramientas, sino la frase de abajo, que es la regla de oro del módulo dos: copiloto, no piloto. Todo lo que sale del modelo pasa por mí antes de llegar a un paciente.");
  }

  // ---------- 4. Cómo la uso: la escalera ----------
  {
    const s = pres.addSlide();
    title(s, "Cómo la uso: subir la escalera sin saltarse peldaños");
    const steps = [
      ["chat", "1 · Chatbot", "Pregunto, resumo, redacto. Prompt estructurado: rol, contexto, tarea, formato. Few-shot con mis propios documentos anonimizados.", LIGHT],
      ["lightbulb", "2 · Razonador", "Le pido que separe hechos, inferencias, dudas y datos que faltan. Que no cierre el diagnóstico. Que se audite a sí mismo.", LIGHT],
      ["sitemap", "3 · Agente", "Le doy un objetivo y herramientas: leer mis tablas, escribir código, probarlo, corregirlo y desplegarlo. Yo superviso cada paso.", LIGHT],
      ["cogs", "4 · Herramienta", "El resultado ya no es un chat: es una calculadora determinista que siempre responde lo mismo al mismo dato.", "E3F4F6"],
    ];
    const sw = 2.9, gap = 0.22, x0 = 0.6;
    steps.forEach(([k, h, d, f], i) => {
      const x = x0 + i * (sw + gap), y = 3.4 - i * 0.4, hh = 2.8 + i * 0.4;
      card(s, x, y, sw, hh, f);
      circleIcon(s, k, x + 0.25, y + 0.25, 0.6, WHITE);
      s.addText(h, { x: x + 0.95, y: y + 0.25, w: sw - 1.15, h: 0.6, fontFace: HFONT, fontSize: 16, bold: true, color: NAVY, isTextBox: true, margin: 0, valign: "middle" });
      s.addText(d, { x: x + 0.25, y: y + 0.95, w: sw - 0.5, h: hh - 1.1, fontFace: BFONT, fontSize: 12, color: INK, isTextBox: true, margin: 0, valign: "top" });
    });
    s.addText("Lo hice con chatbots y con agentes. Y aprendí que el peldaño 4 solo existe si has hecho bien el 1 y el 2.", { x: 0.6, y: 6.5, w: 12, h: 0.45, fontFace: BFONT, fontSize: 14, italic: true, color: TEAL, isTextBox: true, margin: 0 });
    footer(s);
    notes(s, "El curso nos enseñó una escalera: chatbots, razonadores, agentes. Mi proyecto la sube entera. Empecé preguntando a un chat, pasé a pedirle que razonara y se auditara, y terminé dándole herramientas a un agente para que escribiera y probara el código. El cuarto peldaño es el que me interesa como clínica: una herramienta que no opina, calcula.");
  }

  // ---------- 5. El problema ----------
  {
    const s = pres.addSlide();
    title(s, "1 · El problema: veinte minutos que nadie tenía");
    card(s, 0.6, 1.5, 6.2, 4.7, LIGHT);
    s.addText("Evaluar la condición física en consulta de obesidad", { x: 0.9, y: 1.65, w: 5.7, h: 0.7, fontFace: HFONT, fontSize: 17, bold: true, color: NAVY, isTextBox: true, margin: 0 });
    const rows = [
      ["walk", "Caminata de 6 minutos", "tabla por edad y talla"],
      ["grip", "Fuerza de prensión", "tabla por sexo y rango de edad"],
      ["chair", "Levantarse de la silla", "tabla por sexo y grupo etario"],
    ];
    rows.forEach(([k, h, d], i) => {
      const y = 2.4 + i * 0.85;
      circleIcon(s, k, 0.9, y, 0.6, WHITE);
      s.addText([{ text: h, options: { bold: true, breakLine: true } }, { text: d, options: { color: MUTED } }], { x: 1.65, y, w: 4.9, h: 0.65, fontFace: BFONT, fontSize: 13, color: INK, isTextBox: true, margin: 0, valign: "middle" });
    });
    s.addText([
      { text: "Tres pruebas, tres artículos, tres tablas distintas. Buscar la fila, interpolar el percentil a mano, apuntarlo, interpretarlo. Y repetirlo en la siguiente visita.", options: { breakLine: true, paraSpaceAfter: 6 } },
      { text: "Consecuencia real: se hacía poco, o se hacía a ojo.", options: { bold: true, color: CORAL } },
    ], { x: 0.9, y: 5.0, w: 5.7, h: 1.1, fontFace: BFONT, fontSize: 13, color: INK, isTextBox: true, margin: 0, valign: "top" });
    // right: big stat
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.3, y: 1.5, w: 5.4, h: 4.7, rectRadius: 0.12, fill: { color: NAVY }, line: { color: NAVY } });
    s.addImage({ data: ic["clockW"], x: 7.8, y: 1.9, w: 0.7, h: 0.7 });
    s.addText("≈ 20 min", { x: 7.8, y: 2.6, w: 4.5, h: 1.4, fontFace: HFONT, fontSize: 66, bold: true, color: WHITE, isTextBox: true, margin: 0 });
    s.addText("por paciente, solo en consultar tablas y calcular percentiles. En una consulta de 10 minutos, sencillamente no cabía.", { x: 7.8, y: 4.05, w: 4.4, h: 1.2, fontFace: BFONT, fontSize: 14, color: "CADCE3", isTextBox: true, margin: 0 });
    s.addText("Estimación propia sobre mi práctica", { x: 7.8, y: 5.55, w: 4.4, h: 0.4, fontFace: BFONT, fontSize: 10, italic: true, color: "8FA6B2", isTextBox: true, margin: 0 });
    footer(s);
    notes(s, "Primer punto de la plantilla: el problema. En obesidad quiero saber cómo funciona el cuerpo, no solo cuánto pesa. Tres pruebas sencillas de hacer, pero interpretarlas era un suplicio: tres artículos, tres tablas, interpolar a mano. Unos veinte minutos por paciente que en una consulta de diez no existen. Así que, siendo honesta, se hacía poco.");
  }

  // ---------- 6. Herramienta ----------
  {
    const s = pres.addSlide();
    title(s, "2 · La herramienta: lo no determinista construye lo determinista");
    const cols = [
      ["chat", "Chat frontera", "Diseño, dudas y primer código", "Prompt estructurado con rol, contexto, tarea, formato y restricciones. Cadena de prompts: estructurar, generar, criticar, corregir."],
      ["sitemap", "Agente de código", "Iterar hasta que funcione", "Lee las tablas, escribe la app, la ejecuta, ve el error y lo corrige. Yo apruebo cada cambio y pruebo con casos sintéticos."],
      ["code", "Streamlit + GitHub", "Publicar sin ser programadora", "Código en Python abierto. La app se despliega sola desde el repositorio. Cualquier colega puede usarla desde el navegador."],
    ];
    cols.forEach(([k, h, sub, d], i) => {
      const x = 0.6 + i * 4.12;
      card(s, x, 1.5, 3.92, 3.5);
      circleIcon(s, k, x + 0.25, 1.75, 0.7, LIGHT);
      s.addText(h, { x: x + 1.05, y: 1.75, w: 2.7, h: 0.4, fontFace: HFONT, fontSize: 17, bold: true, color: NAVY, isTextBox: true, margin: 0, valign: "middle" });
      s.addText(sub, { x: x + 1.05, y: 2.15, w: 2.7, h: 0.35, fontFace: BFONT, fontSize: 11, italic: true, color: MUTED, isTextBox: true, margin: 0 });
      s.addText(d, { x: x + 0.25, y: 2.7, w: 3.4, h: 2.1, fontFace: BFONT, fontSize: 12.5, color: INK, isTextBox: true, margin: 0, valign: "top" });
    });
    card(s, 0.6, 5.25, 12.13, 1.2, "E3F4F6");
    s.addImage({ data: ic["quote"], x: 0.9, y: 5.5, w: 0.45, h: 0.45 });
    s.addText("La determinación no vive dentro del modelo. Vive en el proceso que le obligas a seguir. El modelo escribe el código; la calculadora, una vez escrita, no opina: al mismo dato responde siempre lo mismo.", { x: 1.5, y: 5.35, w: 11, h: 1.0, fontFace: BFONT, fontSize: 13.5, italic: true, color: NAVY, isTextBox: true, margin: 0, valign: "middle" });
    footer(s);
    notes(s, "Segundo punto: la herramienta. Aquí está la idea que más me marcó del módulo cuatro: usar una máquina probabilística para construir una determinista. El chat y el agente son no deterministas; cambian con cada prompt. Pero lo que producen es una calculadora que siempre da el mismo percentil al mismo dato. Eso es lo que puedo llevar a consulta con tranquilidad.");
  }

  // ---------- 7. Datos ----------
  {
    const s = pres.addSlide();
    title(s, "3 · Los datos: tres fuentes verificadas, cero pacientes");
    const src = [
      ["walk", "Caminata 6 min", "Cohorte STAAB, Würzburg. 2.762 adultos de 30 a 79 años. Percentiles por edad y talla, subgrupo sin factores de riesgo cardiovascular, pasillo de 15 m.", "Morbach et al., Clin Res Cardiol 2024 · doi 10.1007/s00392-023-02373-3"],
      ["grip", "Fuerza de prensión", "Normas internacionales: 100 estudios, 2,4 millones de adultos, 69 países. Percentiles 5 a 95 por sexo y edad, de 20 a más de 100 años.", "Tomkinson et al., J Sport Health Sci 2024 · doi 10.1016/j.jshs.2024.101014"],
      ["chair", "Levantarse de la silla", "Estudio EXERNET: 3.136 mayores de 65 años no institucionalizados de seis regiones de España. Valores normativos por sexo y grupo de edad.", "Pedrero-Chamizo et al., Arch Gerontol Geriatr 2012 · doi 10.1016/j.archger.2012.02.004"],
    ];
    src.forEach(([k, h, d, ref], i) => {
      const y = 1.5 + i * 1.45;
      card(s, 0.6, y, 8.4, 1.3);
      circleIcon(s, k, 0.85, y + 0.3, 0.7, LIGHT);
      s.addText(h, { x: 1.75, y: y + 0.12, w: 7, h: 0.35, fontFace: HFONT, fontSize: 15, bold: true, color: NAVY, isTextBox: true, margin: 0 });
      s.addText(d, { x: 1.75, y: y + 0.47, w: 7.05, h: 0.55, fontFace: BFONT, fontSize: 11, color: INK, isTextBox: true, margin: 0, valign: "top" });
      s.addText(ref, { x: 1.75, y: y + 0.98, w: 7.05, h: 0.28, fontFace: BFONT, fontSize: 9, color: MUTED, isTextBox: true, margin: 0 });
    });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 9.3, y: 1.5, w: 3.43, h: 4.2, rectRadius: 0.12, fill: { color: NAVY }, line: { color: NAVY } });
    s.addImage({ data: await icon("FaLock", CYAN), x: 9.65, y: 1.85, w: 0.55, h: 0.55 });
    s.addText("RGPD por diseño", { x: 9.65, y: 2.5, w: 2.8, h: 0.45, fontFace: HFONT, fontSize: 17, bold: true, color: WHITE, isTextBox: true, margin: 0 });
    s.addText([
      { text: "La app no guarda nada. No pide nombre, ni fecha de nacimiento, ni historia.", options: { breakLine: true, paraSpaceAfter: 6 } },
      { text: "Solo tres números: sexo o talla, edad y el valor medido. Salen del despacho y no vuelven a ningún servidor.", options: { breakLine: true, paraSpaceAfter: 6 } },
      { text: "Las tablas son datos publicados, abiertos y citables.", options: {} },
    ], { x: 9.65, y: 3.0, w: 2.85, h: 2.6, fontFace: BFONT, fontSize: 11.5, color: "CADCE3", isTextBox: true, margin: 0, valign: "top" });
    s.addText("Fuentes verificadas en PubMed el 11-09-2026.", { x: 0.6, y: 5.95, w: 8, h: 0.3, fontFace: BFONT, fontSize: 10, italic: true, color: MUTED, isTextBox: true, margin: 0 });
    footer(s);
    notes(s, "Tercer punto: los datos. Tres publicaciones, verificadas una a una en PubMed, no aceptadas porque las dijera el chat. Ojo con la primera: es población alemana sana; lo digo porque ese matiz importa al interpretar a una persona con obesidad y hay que tenerlo visible. Y lo más importante: la app no almacena ningún dato del paciente. RGPD por diseño, como aprendimos en el módulo uno.");
  }

  // ---------- 8. Solución (screenshots) ----------
  {
    const s = pres.addSlide();
    title(s, "4 · La solución: tres números dentro, un semáforo fuera");
    const shots = [["app_caminata.png", "Caminata 6 minutos"], ["app_prension.png", "Fuerza de prensión"], ["app_silla.png", "Levantarse de la silla"]];
    shots.forEach(([f, cap], i) => {
      const x = 0.6 + i * 4.12;
      card(s, x, 1.45, 3.92, 4.75);
      s.addImage({ path: f, x: x + 0.16, y: 1.6, w: 3.6, h: 3.53 });
      s.addText(cap, { x: x + 0.16, y: 5.2, w: 3.6, h: 0.35, fontFace: HFONT, fontSize: 13, bold: true, color: NAVY, isTextBox: true, margin: 0, align: "center" });
      s.addText("Percentil estimado, rango, referencia P50 e interpretación clínica", { x: x + 0.16, y: 5.55, w: 3.6, h: 0.5, fontFace: BFONT, fontSize: 10, color: MUTED, isTextBox: true, margin: 0, align: "center" });
    });
    s.addText("evaluacion-funcional-pro.streamlit.app · abierta, gratuita, desde cualquier navegador", { x: 0.6, y: 6.35, w: 12, h: 0.35, fontFace: BFONT, fontSize: 12, color: TEAL, isTextBox: true, margin: 0 });
    footer(s);
    notes(s, "Cuarto punto: la solución, tal cual la veo yo en consulta. Elijo la prueba, meto sexo o talla, edad y el valor medido, y en el mismo segundo tengo el percentil interpolado, el rango, la referencia del percentil cincuenta y una frase de interpretación. El semáforo lo entiende el paciente sin que yo traduzca nada. Rojo, naranja, verde, azul.");
  }

  // ---------- 9. Cómo la construí ----------
  {
    const s = pres.addSlide();
    title(s, "Cómo la construí: el prompt es la especificación");
    const steps = [
      ["1", "Estructurar", "Rol, contexto, tarea, formato y restricciones. Le pasé las tres tablas en CSV y le pedí que no inventara ningún valor."],
      ["2", "Generar", "Primer prototipo en Streamlit. Interpolación lineal entre percentiles, semáforo y frases de interpretación."],
      ["3", "Criticar", "Cambio de papel: “ahora eres un revisor exigente”. Encontró que no manejaba edades fuera de tabla."],
      ["4", "Probar", "Casos sintéticos con resultado conocido: el valor P50 de la tabla tiene que devolver exactamente P50."],
      ["5", "Desplegar", "GitHub y Streamlit Cloud. Desde entonces, cada corrección se publica sola."],
    ];
    steps.forEach(([n, h, d], i) => {
      const x = 0.6 + i * 2.46;
      s.addShape(pres.shapes.OVAL, { x: x + 0.85, y: 1.5, w: 0.7, h: 0.7, fill: { color: TEAL }, line: { color: TEAL } });
      s.addText(n, { x: x + 0.85, y: 1.5, w: 0.7, h: 0.7, fontFace: HFONT, fontSize: 22, bold: true, color: WHITE, isTextBox: true, margin: 0, align: "center", valign: "middle" });
      s.addText(h, { x, y: 2.3, w: 2.4, h: 0.4, fontFace: HFONT, fontSize: 15, bold: true, color: NAVY, isTextBox: true, margin: 0, align: "center" });
      s.addText(d, { x, y: 2.75, w: 2.4, h: 1.5, fontFace: BFONT, fontSize: 11.5, color: INK, isTextBox: true, margin: 0, align: "center", valign: "top" });
      if (i < 4) s.addShape(pres.shapes.LINE, { x: x + 1.6, y: 1.85, w: 0.8, h: 0, line: { color: "B8C9CF", width: 1.5, endArrowType: "triangle" } });
    });
    // prompt box
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 4.35, w: 12.13, h: 2.25, rectRadius: 0.1, fill: { color: NAVY }, line: { color: NAVY } });
    s.addText("El prompt de arranque, resumido", { x: 0.9, y: 4.45, w: 6, h: 0.35, fontFace: BFONT, fontSize: 11, bold: true, color: CYAN, isTextBox: true, margin: 0 });
    s.addText(
      "Actúa como desarrollador de herramientas clínicas. CONTEXTO: consulta de obesidad en Atención Primaria; tres tablas de percentiles adjuntas en CSV con su fuente. TAREA: una app web sencilla que, dados sexo o talla, edad y valor medido, estime el percentil por interpolación lineal y lo clasifique. FORMATO: Python + Streamlit, un solo archivo, sin base de datos. RESTRICCIONES: usa solo los valores de las tablas, nunca inventes ni extrapoles; si la combinación no existe, dilo; no guardes ningún dato del usuario; muestra siempre la referencia P50 y la fuente.",
      { x: 0.9, y: 4.8, w: 11.5, h: 1.7, fontFace: "Courier New", fontSize: 10.5, color: "E6EEF1", isTextBox: true, margin: 0, valign: "top" });
    footer(s);
    notes(s, "Cómo la construí, con la cadena de prompts del módulo dos: estructurar, generar, criticar, comunicar. Añadí un paso que para mí es el más importante: probar con casos donde sé la respuesta. Si meto el valor exacto del percentil cincuenta de la tabla, la app tiene que decir cincuenta. Si no, algo está mal. Abajo tenéis el prompt de arranque resumido: fijaos en las restricciones, que son la parte que de verdad protege.");
  }

  // ---------- 10. Validación ----------
  {
    const s = pres.addSlide();
    title(s, "5 · Validación: lo que comprobé y lo que todavía no");
    card(s, 0.6, 1.5, 5.95, 4.8);
    s.addImage({ data: ic["check"], x: 0.9, y: 1.75, w: 0.5, h: 0.5 });
    s.addText("Lo que sí he verificado", { x: 1.55, y: 1.7, w: 4.8, h: 0.6, fontFace: HFONT, fontSize: 18, bold: true, color: NAVY, isTextBox: true, margin: 0, valign: "middle" });
    s.addText([
      { text: "Fidelidad: cada valor de la tabla devuelve su percentil exacto. Ni un dato inventado.", options: { bullet: true, breakLine: true, paraSpaceAfter: 6 } },
      { text: "Interpolación: valores intermedios caen dentro del rango correcto y en orden.", options: { bullet: true, breakLine: true, paraSpaceAfter: 6 } },
      { text: "Fuentes: las tres publicaciones existen, dicen lo que la app dice y están citadas.", options: { bullet: true, breakLine: true, paraSpaceAfter: 6 } },
      { text: "Casos sintéticos extremos: valores por debajo y por encima de la tabla se anuncian como tales.", options: { bullet: true, breakLine: true, paraSpaceAfter: 6 } },
      { text: "Rúbrica del módulo 4: fidelidad, priorización, calibración, confusores y acción segura.", options: { bullet: true } },
    ], { x: 0.9, y: 2.45, w: 5.4, h: 3.7, fontFace: BFONT, fontSize: 12.5, color: INK, isTextBox: true, margin: 0, valign: "top" });
    card(s, 6.78, 1.5, 5.95, 4.8, "FDF1EC");
    s.addImage({ data: ic["eye"], x: 7.08, y: 1.75, w: 0.5, h: 0.5 });
    s.addText("Límites que conozco y estoy corrigiendo", { x: 7.73, y: 1.7, w: 4.8, h: 0.6, fontFace: HFONT, fontSize: 18, bold: true, color: CORAL, isTextBox: true, margin: 0, valign: "middle" });
    s.addText([
      { text: "Caminata: edad y talla solo por décadas. Una persona de 64 años y 163 cm se evalúa con la tabla de 60 o 70. Solución: interpolación en dos dimensiones.", options: { bullet: true, breakLine: true, paraSpaceAfter: 6 } },
      { text: "Silla: la tabla empieza en P10; quien rinde por debajo aparece como “Bajo” y no como “Muy bajo”. Es justo la población que más quiero detectar.", options: { bullet: true, breakLine: true, paraSpaceAfter: 6 } },
      { text: "Población de referencia: la de caminata es alemana y sin factores de riesgo. Hay que mostrarlo en pantalla.", options: { bullet: true, breakLine: true, paraSpaceAfter: 6 } },
      { text: "No es un producto sanitario certificado: es apoyo a la decisión, y así debe decirlo la propia app.", options: { bullet: true } },
    ], { x: 7.08, y: 2.45, w: 5.4, h: 3.7, fontFace: BFONT, fontSize: 12.5, color: INK, isTextBox: true, margin: 0, valign: "top" });
    footer(s);
    notes(s, "Quinto punto: validación. Y aquí quiero ser especialmente honesta, porque es lo que el curso nos pidió: el modelo debe saber decir no lo sé, y yo también. A la izquierda, lo que he comprobado. A la derecha, tres límites reales que encontré al auditar la app con el mismo espíritu crítico que usamos con los razonadores. Los estoy corrigiendo. Presentar una herramienta sin sus límites sería exactamente el exceso de seguridad que aprendimos a detectar.");
  }

  // ---------- 11. Impacto ----------
  {
    const s = pres.addSlide();
    title(s, "6 · Impacto: lo que hago con el tiempo que ya no gasto");
    // stat row
    const stats = [["≈ 20 min", "antes, por paciente", CORAL], ["< 1 min", "ahora, las tres pruebas", TEAL], ["3 de 3", "pruebas en todas las visitas de seguimiento", NAVY]];
    stats.forEach(([n, l, c], i) => {
      const x = 0.6 + i * 4.12;
      card(s, x, 1.5, 3.92, 1.9);
      s.addText(n, { x: x + 0.25, y: 1.6, w: 3.5, h: 1.0, fontFace: HFONT, fontSize: 44, bold: true, color: c, isTextBox: true, margin: 0, valign: "middle" });
      s.addText(l, { x: x + 0.25, y: 2.6, w: 3.5, h: 0.6, fontFace: BFONT, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });
    });
    const gains = [
      ["users", "Más tiempo con la persona", "Los minutos que no gasto en tablas los gasto en escuchar, explicar y pactar objetivos."],
      ["chart", "Seguimiento objetivo", "Un percentil hoy y otro dentro de tres meses. La función mejora antes que el peso, y ahora lo puedo enseñar."],
      ["mega", "Un lenguaje común", "El semáforo lo entiende cualquiera. “Estás en naranja, vamos a por el verde” sustituye a la báscula como conversación."],
    ];
    gains.forEach(([k, h, d], i) => {
      const x = 0.6 + i * 4.12;
      circleIcon(s, k, x, 3.75, 0.65, LIGHT);
      s.addText(h, { x: x + 0.8, y: 3.72, w: 3.1, h: 0.7, fontFace: HFONT, fontSize: 15, bold: true, color: NAVY, isTextBox: true, margin: 0, valign: "middle" });
      s.addText(d, { x, y: 4.55, w: 3.92, h: 1.5, fontFace: BFONT, fontSize: 12.5, color: INK, isTextBox: true, margin: 0, valign: "top" });
    });
    s.addText("Los tiempos son estimaciones propias sobre mi consulta; el impacto clínico está por medir y es el siguiente paso.", { x: 0.6, y: 6.25, w: 12, h: 0.35, fontFace: BFONT, fontSize: 10.5, italic: true, color: MUTED, isTextBox: true, margin: 0 });
    footer(s);
    notes(s, "Sexto punto: impacto. De veinte minutos a menos de uno. Pero el número que más me importa es el tercero: ahora hago las tres pruebas en todas las visitas de seguimiento, cuando antes las hacía cuando podía. Y eso cambia la conversación con la persona: la función mejora antes que el peso, y ahora tengo un semáforo para enseñárselo. Sed conscientes de que los tiempos son estimación mía; medir el impacto clínico es lo siguiente.");
  }

  // ---------- 12. Escalabilidad ----------
  {
    const s = pres.addSlide();
    title(s, "7 · Escalabilidad: de mi consulta a la de cualquiera");
    const next = [
      ["walk", "Más pruebas del mismo EXERNET", "Velocidad de la marcha, equilibrio monopodal, flexión de brazo y up-and-go. Las tablas ya existen y están validadas en población española."],
      ["file", "Informe en un clic", "PDF con los percentiles, la interpretación y las fuentes, para la historia clínica y para entregar a la persona."],
      ["grip", "Prensión normalizada por talla", "La fuente internacional ya la ofrece. En obesidad, la fuerza relativa dice más que la absoluta."],
      ["cogs", "Interpolación completa y avisos", "Edad y talla continuas en la caminata, etiqueta correcta en los extremos, población de referencia visible."],
      ["rocket", "Abierta a otros centros", "Código abierto en GitHub. Cualquier equipo de Atención Primaria puede usarla hoy o adaptarla a sus propias tablas."],
      ["book", "Puente a la docencia", "Caso de uso real para enseñar a médicos de familia cómo construir herramientas con IA sin delegar la medicina."],
    ];
    next.forEach(([k, h, d], i) => {
      const col = i % 3, row = Math.floor(i / 3);
      const x = 0.6 + col * 4.12, y = 1.5 + row * 2.45;
      card(s, x, y, 3.92, 2.25);
      circleIcon(s, k, x + 0.2, y + 0.2, 0.6, LIGHT);
      s.addText(h, { x: x + 0.95, y: y + 0.15, w: 2.85, h: 0.7, fontFace: HFONT, fontSize: 14, bold: true, color: NAVY, isTextBox: true, margin: 0, valign: "middle" });
      s.addText(d, { x: x + 0.2, y: y + 0.95, w: 3.5, h: 1.2, fontFace: BFONT, fontSize: 11.5, color: INK, isTextBox: true, margin: 0, valign: "top" });
    });
    footer(s);
    notes(s, "Séptimo punto: escalabilidad. La app es de código abierto; cualquier compañero puede usarla hoy. Lo siguiente: más pruebas del mismo estudio español, informe en PDF, prensión normalizada por talla, que en obesidad es más informativa, y las correcciones que he mencionado. Y, para mí, lo más bonito: convertirla en material docente para enseñar a otros médicos de familia a hacer lo mismo.");
  }

  // ---------- 13. Técnicas del curso ----------
  {
    const s = pres.addSlide();
    title(s, "Lo que me llevo del curso, y dónde lo apliqué");
    const tech = [
      ["Prompt estructurado", "Rol, contexto, tarea, formato, restricciones. Sin él, el chat me daba código genérico y opiniones clínicas que no le pedí.", "M2"],
      ["Few-shot con mis documentos", "Cartas y hojas de paciente con mi estilo, a partir de dos ejemplos anonimizados. Ahora suenan a mí.", "M2"],
      ["Cadena de prompts y autocrítica", "Estructurar, generar, criticar, corregir. Pedirle que cambie de papel y busque sus propios errores.", "M2 · M4"],
      ["Separar hechos, inferencias y dudas", "“No cierres el diagnóstico.” El modelo debe saber decir no lo sé; yo aprendí a exigírselo.", "M4"],
      ["Búsqueda de evidencia", "Consensus, Elicit, Scite y OpenEvidence para encontrar y verificar las fuentes. Ninguna cita sin comprobar.", "M3"],
      ["Ventana de contexto", "“Lost in the middle”: si el dato está enterrado, dirijo la atención al día concreto. Lo aplico a evoluciones largas.", "M2"],
      ["Agentes con supervisión", "Objetivo, herramientas y memoria, pero cada acción pasa por mí. Las cinco preguntas éticas: autonomía, responsabilidad, supervisión, consentimiento, equidad.", "M6"],
      ["Qué nivel de IA exige la tarea", "Gratuita para redactar; frontera para razonar; local si el dato es sensible. No todo es “la IA”.", "M4"],
    ];
    tech.forEach(([h, d, m], i) => {
      const col = i % 4, row = Math.floor(i / 4);
      const x = 0.6 + col * 3.08, y = 1.5 + row * 2.45;
      card(s, x, y, 2.9, 2.25, row === 0 ? WHITE : LIGHT);
      s.addText(m, { x: x + 0.2, y: y + 0.15, w: 1.2, h: 0.3, fontFace: BFONT, fontSize: 10, bold: true, color: CYAN, isTextBox: true, margin: 0 });
      s.addText(h, { x: x + 0.2, y: y + 0.45, w: 2.55, h: 0.6, fontFace: HFONT, fontSize: 13.5, bold: true, color: NAVY, isTextBox: true, margin: 0, valign: "top" });
      s.addText(d, { x: x + 0.2, y: y + 1.05, w: 2.55, h: 1.15, fontFace: BFONT, fontSize: 10.5, color: INK, isTextBox: true, margin: 0, valign: "top" });
    });
    footer(s);
    notes(s, "Estas son las ocho técnicas del programa que uso de verdad, con el módulo del que salen. No las cuento como teoría: cada una tiene un sitio en la calculadora o en mi consulta. Si tuviera que quedarme con dos: el prompt estructurado, porque es la especificación de todo lo demás, y la autocrítica del modelo, porque es lo que convierte una respuesta bonita en una respuesta útil.");
  }

  // ---------- 14. Compliance y seguridad ----------
  {
    const s = pres.addSlide();
    title(s, "Mis reglas de seguridad, en una sola pantalla");
    const rules = [
      ["ban", "Nunca datos identificables en herramientas de consumo. Anonimizo, elimino metadatos y, si dudo, no subo.", CORAL],
      ["ban", "Nunca un nombre comercial de prescripción, ni en la app ni en un reel. Principio activo y mecanismo.", CORAL],
      ["ban", "Nunca una salida del modelo llega a un paciente sin mi revisión y sin disclaimer.", CORAL],
      ["check", "Siempre digo qué población de referencia hay detrás de un número y qué límites tiene.", TEAL],
      ["check", "Siempre declaro mis vínculos con industria antes de hablar del tema, no después.", TEAL],
      ["check", "Siempre pruebo con casos sintéticos de resultado conocido antes de usar algo en consulta.", TEAL],
    ];
    rules.forEach(([k, t, c], i) => {
      const col = i < 3 ? 0 : 1, row = i % 3;
      const x = 0.6 + col * 6.2, y = 1.55 + row * 1.4;
      card(s, x, y, 5.93, 1.2, col === 0 ? "FDF1EC" : "E3F4F6");
      s.addImage({ data: ic[k], x: x + 0.3, y: y + 0.35, w: 0.5, h: 0.5 });
      s.addText(t, { x: x + 1.0, y: y + 0.15, w: 4.75, h: 0.9, fontFace: BFONT, fontSize: 13, color: INK, isTextBox: true, margin: 0, valign: "middle" });
    });
    s.addText("Marco: RGPD y LOPDGDD · AI Act · RD 1416/1994 · Código de Deontología OMC 2022 · Código de Buenas Prácticas de Farmaindustria", { x: 0.6, y: 5.85, w: 12.1, h: 0.4, fontFace: BFONT, fontSize: 10.5, color: MUTED, isTextBox: true, margin: 0 });
    footer(s);
    notes(s, "Tres nuncas y tres siempres. Son las reglas con las que trabajo con IA desde el módulo de compliance. La que más me costó interiorizar es la tercera: la tentación de reenviar una hoja de paciente generada por el modelo sin releerla es enorme cuando vas con prisa. Y la prisa, como aprendimos, es la causa de casi todos los problemas.");
  }

  // ---------- 15. Cierre ----------
  {
    const s = pres.addSlide();
    s.background = { color: NAVY };
    s.addShape(pres.shapes.OVAL, { x: -2.2, y: 3.6, w: 6.5, h: 6.5, fill: { color: TEAL, transparency: 70 }, line: { color: TEAL, transparency: 70 } });
    s.addImage({ data: ic["quote"], x: 0.8, y: 1.2, w: 0.8, h: 0.8 });
    s.addText("La IA no me devolvió certezas.\nMe devolvió tiempo.\nY el tiempo, en obesidad, se lo debo a la persona que tengo delante.", { x: 0.8, y: 2.1, w: 11.5, h: 2.6, fontFace: HFONT, fontSize: 34, bold: true, color: WHITE, isTextBox: true, margin: 0, valign: "top", lineSpacingMultiple: 1.05 });
    s.addText("Es biología, no falta de voluntad. Y ahora también es un percentil que puedo enseñar.", { x: 0.8, y: 4.8, w: 11, h: 0.5, fontFace: BFONT, fontSize: 18, italic: true, color: CYAN, isTextBox: true, margin: 0 });
    s.addText([
      { text: "evaluacion-funcional-pro.streamlit.app", options: { bold: true, breakLine: true } },
      { text: "Dra. Cristina Petratti · Médica de familia · Especialista en obesidad", options: {} },
    ], { x: 0.8, y: 5.8, w: 11, h: 0.9, fontFace: BFONT, fontSize: 15, color: "CADCE3", isTextBox: true, margin: 0 });
    notes(s, "Termino con lo que de verdad me llevo. La IA no me ha dado certezas, y desconfío de quien diga que se las da. Me ha dado tiempo. Y en una consulta de obesidad el tiempo es lo más terapéutico que tengo. Gracias.");
  }

  const out = "/home/user/gdp-dashboard/proyectos/potencia_presentacion/Petratti_potencIA_proyecto_final.pptx";
  await pres.writeFile({ fileName: out });
  console.log("written", out);
})();
