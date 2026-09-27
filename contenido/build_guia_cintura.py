"""Genera la guía PDF «Tu cintura, tu riesgo» (entrega por DM para la palabra clave CINTURA).
Uso: python3 build_guia_cintura.py [nombre]  → sin nombre genera la versión genérica."""
import os, sys
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, Image, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.graphics.shapes import Drawing, Ellipse, Rect, Line, String, Circle
from reportlab.lib import colors

HERE = os.path.dirname(os.path.abspath(__file__))
NOMBRE = sys.argv[1] if len(sys.argv) > 1 else ""
suffix = ("-" + NOMBRE.lower()) if NOMBRE else ""
OUT = os.path.join(HERE, f"guia-cintura-dra-petratti{suffix}.pdf")
CAL = "https://calendly.com/metodopetratti-info/30min"
LOGO = os.path.join(HERE, "logo-cristina-petratti.png")

TURQ, LIMA, VERDE, GRIS, GRIS_OSC = (HexColor("#00A8A4"), HexColor("#94C01C"),
                                     HexColor("#D0E08C"), HexColor("#88888C"), HexColor("#3F4548"))
CLARO = HexColor("#E6F5F4")

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
W, H = A4
M = 18 * mm

s_h1 = ParagraphStyle("h1", fontName="DVB", fontSize=24, leading=29, textColor=TURQ, spaceAfter=4)
s_h2 = ParagraphStyle("h2", fontName="DVB", fontSize=14, leading=18, textColor=TURQ, spaceBefore=8, spaceAfter=4)
s_body = ParagraphStyle("b", fontName="DV", fontSize=10.2, leading=14.5, textColor=GRIS_OSC)
s_lead = ParagraphStyle("lead", fontName="DV", fontSize=11.5, leading=16.5, textColor=GRIS_OSC)
s_small = ParagraphStyle("sm", fontName="DV", fontSize=8, leading=10.5, textColor=GRIS)
s_step_n = ParagraphStyle("n", fontName="DVB", fontSize=18, leading=20, textColor=white, alignment=TA_CENTER)
s_step = ParagraphStyle("st", fontName="DV", fontSize=10, leading=13.5, textColor=GRIS_OSC)
s_big = ParagraphStyle("big", fontName="DVB", fontSize=20, leading=24, textColor=TURQ, alignment=TA_CENTER)
s_cta = ParagraphStyle("cta", fontName="DVB", fontSize=13.5, leading=17, textColor=white, alignment=TA_CENTER)
s_cta2 = ParagraphStyle("cta2", fontName="DV", fontSize=10, leading=13.5, textColor=white, alignment=TA_CENTER)
s_ref = ParagraphStyle("ref", fontName="DV", fontSize=9, leading=12.5, textColor=GRIS_OSC, leftIndent=10, spaceAfter=4)
s_th = ParagraphStyle("th", fontName="DVB", fontSize=9.5, leading=12, textColor=white, alignment=TA_CENTER)
s_td = ParagraphStyle("td", fontName="DV", fontSize=9.5, leading=12, textColor=GRIS_OSC, alignment=TA_CENTER)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(VERDE); canvas.setLineWidth(0.8)
    canvas.line(M, 16 * mm, W - M, 16 * mm)
    canvas.setFont("DV", 7.2); canvas.setFillColor(GRIS)
    canvas.drawString(M, 11.5 * mm, "Contenido divulgativo. No sustituye la valoración de tu médico/a. "
                      "Si te reconoces en esto, llévalo a tu consulta.")
    canvas.drawString(M, 8 * mm, "La Dra. Petratti participa en un programa formativo financiado por Novo Nordisk. "
                      "Esta guía no está pagada por nadie y no menciona marcas.")
    canvas.setFont("DVB", 7.2); canvas.setFillColor(TURQ)
    canvas.drawRightString(W - M, 18.5 * mm, f"Dra. Cristina Petratti · @crispetratti · {doc.page}")
    if os.path.exists(LOGO):
        canvas.drawImage(LOGO, W - M - 36 * mm, H - 19 * mm, width=36 * mm, height=13 * mm,
                         preserveAspectRatio=True, mask="auto", anchor="ne")
    canvas.restoreState()


def silueta():
    d = Drawing(150, 190)
    # cuerpo esquemático
    d.add(Circle(75, 168, 14, fillColor=CLARO, strokeColor=TURQ, strokeWidth=1.2))
    d.add(Rect(45, 60, 60, 92, rx=22, ry=22, fillColor=CLARO, strokeColor=TURQ, strokeWidth=1.2))
    d.add(Rect(50, 10, 20, 55, rx=8, ry=8, fillColor=CLARO, strokeColor=TURQ, strokeWidth=1.2))
    d.add(Rect(80, 10, 20, 55, rx=8, ry=8, fillColor=CLARO, strokeColor=TURQ, strokeWidth=1.2))
    # referencias: costilla y cadera
    d.add(Line(30, 128, 120, 128, strokeColor=GRIS, strokeWidth=0.8, strokeDashArray=[3, 2]))
    d.add(String(122, 125, "última costilla", fontName="DV", fontSize=7.5, fillColor=GRIS))
    d.add(Line(30, 84, 120, 84, strokeColor=GRIS, strokeWidth=0.8, strokeDashArray=[3, 2]))
    d.add(String(122, 81, "hueso de la cadera", fontName="DV", fontSize=7.5, fillColor=GRIS))
    # cinta
    d.add(Ellipse(75, 106, 34, 7, fillColor=None, strokeColor=LIMA, strokeWidth=3))
    d.add(String(0, 103, "AQUÍ", fontName="DVB", fontSize=9, fillColor=LIMA))
    return d


def cta_block():
    qr = qrcode.QRCode(box_size=6, border=1); qr.add_data(CAL); qr.make(fit=True)
    p = os.path.join(HERE, "_qr_cintura.png"); qr.make_image(fill_color="#3F4548", back_color="white").save(p)
    img = Image(p, 30 * mm, 30 * mm)
    txt = [Paragraph("¿Quieres una cita? Escríbeme.", s_cta), Spacer(1, 3),
           Paragraph("Por mensaje directo en Instagram (@crispetratti) o reservando directamente aquí. "
                     "Consulta presencial en Alicante y online.", s_cta2), Spacer(1, 3),
           Paragraph(f"<link href='{CAL}'><u>{CAL}</u></link>", s_cta2), Spacer(1, 3),
           Paragraph("Por deontología no valoro casos por mensaje: en consulta miramos tu historia completa.", s_cta2)]
    t = Table([[txt, img]], colWidths=[W - 2 * M - 40 * mm, 40 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TURQ), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 12), ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                           ("ROUNDEDCORNERS", [8, 8, 8, 8])]))
    return t


def tabla_alturas():
    rows = [[Paragraph("Tu altura", s_th), Paragraph("Cintura objetivo (menos de 0,5)", s_th),
             Paragraph("Riesgo alto (0,6 o más)", s_th)]]
    for h in range(150, 195, 5):
        rows.append([Paragraph(f"{h} cm", s_td), Paragraph(f"menos de {h/2:.0f} cm", s_td),
                     Paragraph(f"desde {h*0.6:.0f} cm", s_td)])
    t = Table(rows, colWidths=[(W - 2 * M) / 3] * 3)
    st = [("BACKGROUND", (0, 0), (-1, 0), TURQ), ("GRID", (0, 0), (-1, -1), 0.4, VERDE),
          ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            st.append(("BACKGROUND", (0, i), (-1, i), CLARO))
    t.setStyle(TableStyle(st))
    return t


def pasos():
    P = [("De pie, relajada", "Sin ropa en la zona de la cintura, pies juntos, brazos a los lados. Por la mañana y en ayunas, para que cada mes midas en las mismas condiciones."),
         ("Busca el punto", "Localiza tu última costilla y el hueso de la cadera. La cinta va en el punto medio entre los dos; suele quedar un poco por encima del ombligo."),
         ("Cinta paralela al suelo", "Rodea la cintura sin que la cinta se tuerza por detrás. Ajustada a la piel, sin apretar."),
         ("Suelta el aire", "Espira con normalidad y lee la cifra al final de esa espiración. Sin meter tripa: nadie te examina, te estás cuidando."),
         ("Divide entre tu altura", "Cintura ÷ altura, las dos en centímetros. Por debajo de 0,5 es el objetivo. Apunta la cifra y repite dentro de un mes: lo que importa es la tendencia.")]
    rows = []
    for i, (t, d) in enumerate(P, 1):
        rows.append([Paragraph(str(i), s_step_n), [Paragraph(f"<b>{t}</b>", s_step), Paragraph(d, s_step)]])
    t = Table(rows, colWidths=[11 * mm, W - 2 * M - 62 * mm - 11 * mm])
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (0, -1), TURQ),
          ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
          ("LINEBELOW", (0, 0), (-1, -2), 0.4, VERDE)]
    t.setStyle(TableStyle(st))
    return t


def build():
    doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=24 * mm, bottomMargin=24 * mm,
                          title="Tu cintura, tu riesgo · Dra. Cristina Petratti", author="Dra. Cristina Petratti")
    fr = Frame(M, 24 * mm, W - 2 * M, H - 48 * mm, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[fr], onPage=footer)])
    saludo = f"Hola, {NOMBRE}." if NOMBRE else "Hola."
    st = []
    st.append(Paragraph("Tu cintura, tu riesgo", s_h1))
    st.append(Paragraph("El número que la báscula no te da, en cinco pasos", s_lead))
    st.append(Spacer(1, 8))
    st.append(Paragraph(f"{saludo} Puedes pesar lo mismo que hace un año y tener más riesgo cardiovascular. La diferencia está en "
                        "dónde se guarda la grasa: la que rodea tus órganos, la visceral, no se ve en el espejo ni en la báscula, "
                        "pero inflama, sube la tensión y hace que la insulina funcione peor. Una cinta métrica la vigila mejor que "
                        "cualquier báscula. Esto no es fuerza de voluntad: es biología.", s_body))
    st.append(Spacer(1, 8))
    st.append(Paragraph("Cómo medirte bien", s_h2))
    t = Table([[pasos(), silueta()]], colWidths=[W - 2 * M - 60 * mm, 60 * mm])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    st.append(t)
    st.append(Spacer(1, 8))
    st.append(Paragraph("La regla", s_h2))
    st.append(Paragraph("Tu cintura, por debajo de la mitad de tu altura", s_big))
    st.append(Spacer(1, 4))
    st.append(Paragraph("Ejemplo: si mides 165 cm, tu cintura debería estar por debajo de 82 cm. Entre 0,5 y 0,59 la grasa abdominal "
                        "está aumentada; desde 0,6 el riesgo es alto. En consulta lo completamos con tu historia, la tensión y una analítica.", s_body))
    st.append(PageBreak())
    st.append(Paragraph("Tu cifra según tu altura", s_h2))
    st.append(tabla_alturas())
    st.append(Spacer(1, 4))
    st.append(Paragraph("Si tu cifra está por encima", s_h2))
    st.append(Paragraph("No es una sentencia: es información. La grasa visceral es la primera que responde cuando tocas lo que toca: "
                        "fuerza, sueño, menos alcohol, proteína suficiente y, cuando hace falta, tratamiento médico que prescribe y "
                        "controla un profesional. Lo que no funciona es pelearte con la báscula. Llévale esta hoja a tu médico/a o ven a verme.", s_body))
    st.append(Spacer(1, 8))
    st.append(cta_block())
    st.append(Spacer(1, 12))
    st.append(Paragraph("Para colegas: tres referencias", s_h2))
    st.append(Paragraph("Si eres profesional sanitario y quieres incorporar la razón cintura/altura a tu consulta, estas son las tres fuentes en las que se apoya esta guía.", s_body))
    refs = ["<b>1.</b> National Institute for Health and Care Excellence (NICE). <i>Overweight and obesity management.</i> NICE guideline NG246; enero de 2025 (la razón cintura/altura entró en la actualización de 2022 de CG189). Recomienda cintura/altura junto al IMC: 0,5-0,59 adiposidad central aumentada; 0,6 o más, alta.",
            "<b>2.</b> Ross R, Neeland IJ, Yamashita S, et al. Waist circumference as a vital sign in clinical practice: a Consensus Statement from the IAS and ICCR Working Group on Visceral Obesity. <i>Nat Rev Endocrinol.</i> 2020;16(3):177-189. La cintura añade información de riesgo cardiometabólico al IMC y debe medirse de forma rutinaria.",
            "<b>3.</b> Rubino F, Cummings DE, Eckel RH, et al. Definition and diagnostic criteria of clinical obesity. <i>Lancet Diabetes Endocrinol.</i> 2025;13(3):221-262. El IMC solo no basta: el exceso de adiposidad se confirma con cintura, cintura/altura o cintura/cadera."]
    for r in refs:
        st.append(Paragraph(r, s_ref))
    st.append(Spacer(1, 6))
    st.append(Paragraph("Técnica de medición: punto medio entre el borde inferior de la última costilla y la cresta ilíaca, al final de una espiración normal, cinta paralela al suelo (protocolo OMS, recogido en Ross 2020). Puntos de corte de circunferencia de cintura que uso en consulta como complemento: 102 cm en varones y 88 cm en mujeres.", s_small))
    st.append(Spacer(1, 4))
    st.append(Paragraph("Dra. Cristina B. Petratti · Médica de familia · Medicina de la obesidad y salud metabólica · Miembro de SEEDO · Autora de «Obesidades sin culpa» · cristinapetratti.com", s_small))
    doc.build(st)
    try:
        os.remove(os.path.join(HERE, "_qr_cintura.png"))
    except OSError:
        pass
    print("ok", OUT)


if __name__ == "__main__":
    build()
