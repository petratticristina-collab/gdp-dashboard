"""Genera la guía PDF «No fracasaste» (lead magnet para la palabra clave MÉTODO)."""
import os
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, Image, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "guia-no-fracasaste-dra-petratti.pdf")
CAL = "https://calendly.com/metodopetratti-info/30min"
LOGO = os.path.join(HERE, "logo-metodo-petratti.png")  # logo oficial; si existe, sustituye al dibujo

# Paleta exacta medida sobre el logo oficial (Drive: «Critina Petratti-color.png»)
TURQ, LIMA, VERDE, GRIS, GRIS_OSC = (HexColor("#00A8A4"), HexColor("#94C01C"),
                                     HexColor("#D0E08C"), HexColor("#88888C"), HexColor("#3F4548"))

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))

W, H = A4
M = 20 * mm

s_h1 = ParagraphStyle("h1", fontName="DVB", fontSize=26, leading=32, textColor=TURQ, spaceAfter=6)
s_h2 = ParagraphStyle("h2", fontName="DVB", fontSize=15, leading=19, textColor=TURQ, spaceBefore=10, spaceAfter=4)
s_body = ParagraphStyle("b", fontName="DV", fontSize=10.5, leading=15.5, textColor=GRIS_OSC)
s_lead = ParagraphStyle("lead", fontName="DV", fontSize=12.5, leading=18, textColor=GRIS_OSC)
s_small = ParagraphStyle("sm", fontName="DV", fontSize=8, leading=10.5, textColor=GRIS)
s_bul = ParagraphStyle("bul", parent=s_body, leftIndent=12, bulletIndent=0, spaceAfter=3)
s_quote = ParagraphStyle("q", fontName="DVI", fontSize=13, leading=18, textColor=TURQ, leftIndent=10)
s_cta = ParagraphStyle("cta", fontName="DVB", fontSize=13, leading=17, textColor=white, alignment=TA_CENTER)
s_cta2 = ParagraphStyle("cta2", fontName="DV", fontSize=10.5, leading=14, textColor=white, alignment=TA_CENTER)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(VERDE)
    canvas.setLineWidth(0.8)
    canvas.line(M, 16 * mm, W - M, 16 * mm)
    canvas.setFont("DV", 7.2)
    canvas.setFillColor(GRIS)
    canvas.drawString(M, 11.5 * mm, "Contenido divulgativo. No sustituye la valoración de tu médico/a. "
                      "Si te reconoces en esto, llévalo a tu consulta.")
    canvas.drawString(M, 8 * mm, "La Dra. Petratti participa en un programa formativo financiado por Novo Nordisk. "
                      "Esta guía no está pagada por nadie y no menciona marcas.")
    canvas.setFont("DVB", 7.2)
    canvas.setFillColor(TURQ)
    canvas.drawRightString(W - M, 18.5 * mm, f"Dra. Cristina Petratti · @crispetratti · {doc.page}")
    if os.path.exists(LOGO):
        if doc.page > 1:
            canvas.drawImage(LOGO, W - M - 34 * mm, H - 17 * mm, width=34 * mm, height=12 * mm,
                             preserveAspectRatio=True, mask="auto", anchor="ne")
    else:
        canvas.setFillColor(HexColor("#DDF0EF"))
        cx, cy = W - M - 6 * mm, H - 12 * mm
        for dx, dy, r in ((-3.2, 1.8, 2.6), (3.2, 1.8, 2.6), (-2.4, -1.8, 1.9), (2.4, -1.8, 1.9)):
            canvas.circle(cx + dx * mm, cy + dy * mm, r * mm, stroke=0, fill=1)
    canvas.restoreState()


def cover(canvas, doc):
    canvas.saveState()
    if os.path.exists(LOGO):
        canvas.drawImage(LOGO, M, H * 0.66, width=W - 2 * M, height=H * 0.28,
                         preserveAspectRatio=True, mask="auto", anchor="c")
        canvas.setFillColor(TURQ)
        canvas.rect(0, H * 0.58, W, H * 0.06, stroke=0, fill=1)
        canvas.setFont("DVB", 10)
        canvas.setFillColor(white)
        canvas.drawCentredString(W / 2, H * 0.605, "GUÍA GRATUITA")
        canvas.restoreState()
        footer(canvas, doc)
        return
    canvas.setFillColor(TURQ)
    canvas.rect(0, H * 0.58, W, H * 0.42, stroke=0, fill=1)
    # mariposa grande
    cx, cy = W * 0.5, H * 0.79
    for col, dx, dy, r in ((LIMA, -14, 8, 12), (VERDE, -10, -9, 9), (white, 13, 9, 14), (LIMA, 11, -9, 10)):
        canvas.setFillColor(col)
        canvas.circle(cx + dx * mm, cy + dy * mm, r * mm, stroke=0, fill=1)
    canvas.setFillColor(GRIS)
    canvas.roundRect(cx - 1.4 * mm, cy - 9 * mm, 2.8 * mm, 19 * mm, 1.4 * mm, stroke=0, fill=1)
    canvas.setFont("DVB", 10)
    canvas.setFillColor(white)
    canvas.drawCentredString(W / 2, H * 0.61, "MÉTODO DRA. PETRATTI  ·  GUÍA GRATUITA")
    canvas.restoreState()
    footer(canvas, doc)


def bullets(items):
    return [Paragraph(f"<font color='#94C01C'>■</font>&nbsp;&nbsp;{t}", s_bul) for t in items]


def cta_block():
    qr = qrcode.QRCode(box_size=6, border=1)
    qr.add_data(CAL)
    qr.make(fit=True)
    img_path = os.path.join(HERE, "_qr.png")
    qr.make_image(fill_color="#00A8A4", back_color="white").save(img_path)
    qr_img = Image(img_path, 30 * mm, 30 * mm)
    txt = [Paragraph("Reserva tu Sesión de valoración", s_cta),
           Spacer(1, 4),
           Paragraph("45 minutos · online · sin coste", s_cta2),
           Spacer(1, 4),
           Paragraph("Miramos tu historia completa, con historia clínica, y sales con un plan.", s_cta2),
           Spacer(1, 4),
           Paragraph(f"<link href='{CAL}'><u>{CAL}</u></link>", s_cta2)]
    t = Table([[txt, qr_img]], colWidths=[W - 2 * M - 42 * mm, 42 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TURQ),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                           ("TOPPADDING", (0, 0), (-1, -1), 12), ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                           ("ROUNDEDCORNERS", [8, 8, 8, 8])]))
    return t


def build():
    doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=22 * mm,
                          title="No fracasaste · Guía tras dejar el tratamiento",
                          author="Dra. Cristina Petratti")
    fr = Frame(M, 22 * mm, W - 2 * M, H - M - 22 * mm, id="f")
    fr_cover = Frame(M, 22 * mm, W - 2 * M, H * 0.55 - 22 * mm, id="c")
    doc.addPageTemplates([PageTemplate(id="cover", frames=[fr_cover], onPage=cover),
                          PageTemplate(id="body", frames=[fr], onPage=footer)])
    S = []

    # ---------- Portada ----------
    S += [Spacer(1, 6),
          Paragraph("«Dejé la medicación y recuperé todo el peso. Fracasé.»", s_quote),
          Spacer(1, 6),
          Paragraph("No. No fracasaste.", s_h1),
          Paragraph("Lo que le pasa a tu cuerpo al dejar el tratamiento, por qué no es culpa tuya "
                    "y qué consolidar antes de decidir nada.", s_lead),
          Spacer(1, 10),
          Paragraph("Dra. Cristina Petratti · Médica de familia · Especialista en obesidad · SEEDO<br/>"
                    "Autora de «Obesidades sin culpa» · Creadora del Método Petratti", s_body),
          Spacer(1, 14),
          Paragraph("Esta guía es divulgativa y general. No sustituye a tu médico/a ni a quien te prescribe. "
                    "Cualquier decisión sobre continuar, reducir o retirar un tratamiento se toma con "
                    "historia clínica y supervisión.", s_small),
          PageBreak()]

    # ---------- 1. Qué midió el ensayo ----------
    S += [Paragraph("1 · Lo que midió un ensayo clínico cuando se retiró el tratamiento", s_h2),
          Paragraph("En un ensayo con un agonista del receptor GLP-1 (arGLP-1), 327 personas dejaron el "
                    "tratamiento tras 68 semanas y fueron seguidas un año más, hasta la semana 120. "
                    "Todo ello con dieta y ejercicio supervisados dentro del propio ensayo.", s_body),
          Spacer(1, 6)]
    s_th = ParagraphStyle("th", fontName="DVB", fontSize=9.5, leading=12, textColor=white)
    s_td = ParagraphStyle("td", fontName="DV", fontSize=9.5, leading=12.5, textColor=GRIS_OSC)
    raw = [["Momento", "Peso perdido (media)", "Qué pasó"],
           ["Semana 68 (con tratamiento)", "17,3 %", "Mejoraron presión arterial, glucosa y lípidos"],
           ["Semana 120 (un año sin tratamiento)", "5,6 %", "Se recuperaron dos tercios del peso perdido; "
                                                           "las mejoras cardiometabólicas revirtieron"]]
    data = [[Paragraph(c, s_th if r == 0 else s_td) for c in row] for r, row in enumerate(raw)]
    t = Table(data, colWidths=[50 * mm, 34 * mm, W - 2 * M - 84 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), TURQ), ("TEXTCOLOR", (0, 0), (-1, 0), white),
                           ("FONTNAME", (0, 0), (-1, 0), "DVB"), ("FONTNAME", (0, 1), (-1, -1), "DV"),
                           ("FONTSIZE", (0, 0), (-1, -1), 9.5), ("TEXTCOLOR", (0, 1), (-1, -1), GRIS_OSC),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#F3F8E9"), white]),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 6),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LINEBELOW", (0, 0), (-1, -1), 0.4, VERDE)]))
    S += [t, Spacer(1, 6),
          Paragraph("Fuente: Wilding JPH, et al. Weight regain and cardiometabolic effects after withdrawal of "
                    "semaglutide: the STEP 1 trial extension. Diabetes Obes Metab. 2022;24:1553-1564. "
                    "Se cita el principio activo por rigor científico, no como recomendación.", s_small),
          Spacer(1, 10),
          Paragraph("2 · Por qué vuelve el peso: no es carácter, es fisiología", s_h2),
          Paragraph("La obesidad es una enfermedad crónica en la que participan el cerebro, las hormonas, el "
                    "metabolismo, el entorno y las emociones. Cuando pierdes peso, tu cuerpo responde para "
                    "recuperarlo:", s_body)]
    S += bullets(["<b>Baja la leptina</b>, la hormona que avisa al cerebro de que hay reservas suficientes. "
                  "El cerebro interpreta escasez.",
                  "<b>Sube la grelina</b>, la hormona del hambre. Tienes más apetito y menos saciedad.",
                  "<b>Cae el gasto energético</b> por debajo del que corresponde a tu nuevo peso. Gastas menos "
                  "haciendo lo mismo.",
                  "Estas adaptaciones <b>persisten más de un año</b> después de la pérdida de peso."])
    S += [Paragraph("Un arGLP-1 actúa sobre parte de estas señales (saciedad, apetito). Al retirarlo, las "
                    "señales vuelven. Eso no es un fallo tuyo: es lo que hace una enfermedad crónica cuando se "
                    "retira un tratamiento sin haber consolidado lo que sostiene el resultado.", s_body),
          Spacer(1, 4),
          Paragraph("Fuentes: Sumithran P, et al. N Engl J Med. 2011;365:1597-604 · Fothergill E, et al. "
                    "Obesity. 2016;24:1612-9 · Comisión Lancet sobre obesidad clínica, 2025.", s_small),
          PageBreak()]

    # ---------- 3. Qué consolidar ----------
    S += [Paragraph("3 · Los cuatro pilares que sostienen el resultado", s_h2),
          Paragraph("El error no es dejar el tratamiento: hay casos en los que se valora. El error es dejarlo "
                    "de golpe, sin plan y sin haber construido esto. Son orientaciones generales para "
                    "población adulta; tu médico/a las adapta a tu caso.", s_body)]
    pil = [("Fuerza", "El músculo es el tejido que más protege el metabolismo tras perder peso. Las guías "
                      "recomiendan al menos dos sesiones semanales de fuerza para todos los adultos. "
                      "Empezar con el propio peso corporal cuenta."),
           ("Proteína", "Durante y después de la pérdida de peso, un aporte proteico suficiente y repartido "
                        "en las comidas ayuda a conservar masa muscular y a la saciedad. La cantidad exacta "
                        "depende de tu peso, tu riñón y tu situación: se calcula en consulta."),
           ("Sueño", "Dormir menos de siete horas altera leptina y grelina y aumenta el hambre al día "
                     "siguiente. Horario regular, luz de mañana y pantallas fuera de la cama son el primer "
                     "escalón."),
           ("Estrés y emociones", "El cortisol crónico y el hambre emocional no se resuelven con fuerza de "
                                  "voluntad. Se trabajan con herramientas concretas: identificar disparadores, "
                                  "pausas, apoyo. Es el pilar más olvidado y el que más sostiene.")]
    rows = [[Paragraph(f"<b><font color='#1FA8A6'>{a}</font></b>", s_body), Paragraph(b, s_body)] for a, b in pil]
    t2 = Table(rows, colWidths=[38 * mm, W - 2 * M - 38 * mm])
    t2.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 7),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                            ("LINEBELOW", (0, 0), (-1, -2), 0.5, VERDE)]))
    S += [t2, Spacer(1, 4),
          Paragraph("Fuentes: OMS, Directrices sobre actividad física, 2020 · Guía europea EASO de manejo de "
                    "la obesidad en adultos · Chaput JP, et al. Sleep and obesity, 2023.", s_small),
          Spacer(1, 10),
          Paragraph("4 · Antes de decidir nada sobre el tratamiento", s_h2)]
    S += bullets(["<b>No lo dejes por tu cuenta ni de golpe.</b> Cuándo y cómo lo decide quien te prescribe, "
                  "con tu historia clínica delante.",
                  "<b>No lo retomes por tu cuenta.</b> Tampoco con restos de dosis anteriores ni por internet.",
                  "<b>Si notas</b> vómitos persistentes, dolor abdominal intenso, mareo o desmayo, acude a "
                  "urgencias. Si sospechas una reacción a un medicamento, tu médico/a puede notificarla.",
                  "<b>Lleva a tu consulta</b> esta pregunta: «¿Qué tengo consolidado y qué me falta antes de "
                  "cambiar el tratamiento?»"])
    S += [PageBreak(),
          Paragraph("5 · Qué haría yo contigo en una Sesión de valoración", s_h2),
          Paragraph("Repasar tu historia del peso desde el principio, no desde el último intento. Los "
                    "tratamientos que has llevado y qué pasó al dejarlos. Tu sueño, tu cintura, tu relación con "
                    "la comida y tu analítica. Y salir con un diagnóstico de dónde estás y un plan con los tres "
                    "pilares del Método: alimentación flexible, ejercicio adaptado y gestión emocional. Con o "
                    "sin tratamiento farmacológico, porque el Método trabaja lo que el fármaco no hace.", s_body),
          Spacer(1, 10),
          KeepTogether([cta_block()]),
          Spacer(1, 8),
          Paragraph("No valoro casos ni analíticas por mensaje directo: es tu seguridad y mi deontología. "
                    "En la sesión sí, con historia clínica.", s_small),
          Spacer(1, 16),
          Paragraph("Si esta guía te ha servido, compártela con esa persona que dejó el tratamiento y se "
                    "está culpando. Necesita leer esto.", s_lead),
          Spacer(1, 10),
          Paragraph("Dra. Cristina Petratti · Médica de familia · Especialista en obesidad · Miembro de SEEDO · "
                    "Autora de «Pierde peso» y «Obesidades sin culpa» · Creadora del Método Petratti · "
                    "Instagram @crispetratti · YouTube @dra.cristinapetratti", s_small)]

    from reportlab.platypus import NextPageTemplate
    S.insert(0, NextPageTemplate("body"))
    doc.build(S)
    os.remove(os.path.join(HERE, "_qr.png"))
    print("OK", OUT)


if __name__ == "__main__":
    build()
