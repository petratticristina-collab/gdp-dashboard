"""Versión PDF (imprimible / firmable) del consentimiento de imagen, voz y testimonio."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "consentimiento-imagen-testimonio-metodo-petratti.pdf")
LOGO = os.path.join(HERE, "logo-metodo-petratti.png")
TURQ, GRIS, GRIS_OSC = HexColor("#00A8A4"), HexColor("#88888C"), HexColor("#3F4548")
pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
W, H = A4
M = 20 * mm

sT = ParagraphStyle("T", fontName="DVB", fontSize=13, leading=17, textColor=TURQ, alignment=TA_CENTER, spaceAfter=4)
sL = ParagraphStyle("L", fontName="DV", fontSize=7.5, leading=10, textColor=GRIS, alignment=TA_CENTER, spaceAfter=8)
sH = ParagraphStyle("H", fontName="DVB", fontSize=10.5, leading=13, textColor=TURQ, spaceBefore=7, spaceAfter=2)
sB = ParagraphStyle("B", fontName="DV", fontSize=9.2, leading=12.5, textColor=GRIS_OSC, spaceAfter=3)
sC = ParagraphStyle("C", parent=sB, leftIndent=10, spaceAfter=1.5)
sS = ParagraphStyle("S", fontName="DV", fontSize=8, leading=10.5, textColor=GRIS, spaceAfter=2)
BOX = "☐"


def P(t, s=sB): return Paragraph(t, s)
def C(t): return Paragraph(f"{BOX}&nbsp;&nbsp;{t}", sC)


def deco(canvas, doc):
    canvas.saveState()
    if os.path.exists(LOGO):
        canvas.drawImage(LOGO, W - M - 36 * mm, H - 16 * mm, width=36 * mm, height=12 * mm,
                         preserveAspectRatio=True, mask="auto", anchor="ne")
    canvas.setFont("DV", 7); canvas.setFillColor(GRIS)
    canvas.drawCentredString(W / 2, 10 * mm, "Dra. Cristina Petratti · Método Petratti · Consentimiento de imagen, "
                             f"voz y testimonio · v1 · 2026 · pág. {doc.page}")
    canvas.restoreState()


S = [Spacer(1, 6),
     P("CONSENTIMIENTO INFORMADO PARA LA CAPTACIÓN, USO Y DIFUSIÓN<br/>DE IMAGEN, VOZ Y TESTIMONIO", sT),
     P("Ley Orgánica 1/1982, de protección civil del derecho al honor, a la intimidad personal y familiar y a la "
       "propia imagen · Reglamento (UE) 2016/679 (RGPD), arts. 6.1.a, 7 y 9.2.a · Ley Orgánica 3/2018 (LOPDGDD)", sL),

     P("1. Responsable del tratamiento", sH),
     P("Dra. Cristina Petratti · Médica de familia, especialista en obesidad · Nº de colegiada: ____________ · "
       "NIF: ____________ · Domicilio profesional: ______________________________________ · Correo para el "
       "ejercicio de derechos: ______________________________ · Delegado/a de protección de datos (si procede): "
       "______________________________"),

     P("2. Persona que otorga el consentimiento", sH),
     P("<b>Nombre y apellidos:</b> ______________________________________________________________"),
     P("<b>DNI / NIE / Pasaporte:</b> ____________________ &nbsp;&nbsp; <b>Teléfono:</b> ____________________"),
     P("<b>Correo electrónico:</b> ______________________________________________"),
     P("La persona firmante es mayor de edad y otorga este consentimiento de forma libre, específica, informada e "
       "inequívoca. Es independiente de la relación asistencial: negarse a firmarlo o revocarlo no afecta en nada a "
       "la atención médica recibida."),

     P("3. Objeto", sH),
     P("Autorizo a la Dra. Cristina Petratti a captar, fijar, reproducir y difundir mi imagen, mi voz y mi "
       "testimonio sobre mi experiencia personal en relación con mi salud y mi proceso de tratamiento, en los "
       "términos, canales y con los límites que marco a continuación."),
     P("Descripción del contenido concreto (fecha, formato, duración, tema): "
       "________________________________________________________________"),
     P("____________________________________________________________________________________________"),

     P("4. Elementos que autorizo (marcar solo los que procedan)", sH),
     C("Imagen fija (fotografía)"), C("Imagen en movimiento (vídeo)"), C("Voz (audio)"),
     C("Mi nombre de pila"), C("Mi nombre y apellidos"), C("Mi edad aproximada"),
     C("Mención a mi diagnóstico o categoría de tratamiento (p. ej. «tratamiento para la obesidad»), sin nombres de "
       "fármacos, dosis, cifras de peso ni resultados analíticos"),
     C("Uso de mi imagen con el rostro visible (si no se marca, se pixelará o se usará plano sin rostro)"),

     P("5. Canales y finalidad (marcar los que procedan)", sH),
     P("Finalidad: divulgación en salud y comunicación de la actividad profesional de la Dra. Petratti. El contenido "
       "no se asociará a promesas de resultados, cifras de pérdida de peso ni a la promoción de medicamentos."),
     C("Instagram (@crispetratti) y Threads"), C("YouTube (@dra.cristinapetratti)"), C("TikTok"),
     C("Página web y boletín por correo electrónico"),
     C("Presentaciones docentes, congresos y formación a profesionales"),
     C("Medios de comunicación (prensa, radio, televisión), previa comunicación a la persona firmante"),
     P("Si el contenido lo publica la propia persona en sus redes sociales:"),
     C("Autorizo a la Dra. Petratti a compartir en sus canales (stories, repost, cita) el contenido que yo publique "
       "voluntariamente en mis propias redes sobre mi experiencia, sin modificarlo"),
     C("Autorizo a la Dra. Petratti a responder públicamente a comentarios o preguntas sobre mi caso, únicamente "
       "sobre lo que yo haya hecho público, sin añadir datos clínicos"),
     C("Declaro que no recibo ninguna contraprestación (descuento, sesiones, regalo) por publicar en mis redes. "
       "Si la recibiera, identificaré la publicación como colaboración (#publi)"),
     P(f"Ámbito territorial: internacional, por la naturaleza de internet. Duración: {BOX} 2 años · {BOX} 5 años · "
       f"{BOX} indefinida, desde la firma; en todos los casos revocable."),

     P("6. Garantías que asume la Dra. Petratti", sH),
     C(f"Podré revisar el contenido final antes de su publicación y pedir cambios o retirarme, sin justificarlo. "
       f"&nbsp;{BOX} Sí, quiero revisarlo &nbsp;&nbsp;{BOX} No es necesario"),
     P("• No se editará mi testimonio de forma que altere su sentido."),
     P("• No se difundirán datos clínicos concretos (analíticas, kilos, dosis, nombres de fármacos) salvo que yo lo "
       "autorice expresamente por escrito para un contenido concreto."),
     P("• El contenido se publicará indicando que es una experiencia personal y no sustituye la valoración médica "
       "individual."),
     P("• Mis datos identificativos no se cederán a terceros, salvo a las plataformas necesarias para la publicación, "
       "que actúan con sus propias condiciones de servicio."),

     P("7. Contraprestación", sH),
     P(f"{BOX} Esta cesión es gratuita. &nbsp;&nbsp; {BOX} Se acuerda una contraprestación de ______________ "
       "(describir). En ningún caso se condiciona al contenido del testimonio ni a resultados clínicos."),

     P("8. Revocación y ejercicio de derechos", sH),
     P("Puedo revocar este consentimiento en cualquier momento, sin justificación, mediante escrito al correo del "
       "apartado 1. La Dra. Petratti retirará el contenido de los canales bajo su control en un plazo máximo de 15 "
       "días desde la recepción. La revocación no tiene efectos retroactivos sobre difusiones ya realizadas ni sobre "
       "copias efectuadas por terceros ajenos a su control."),
     P("Puedo ejercer los derechos de acceso, rectificación, supresión, limitación, oposición y portabilidad ante el "
       "responsable, y reclamar ante la Agencia Española de Protección de Datos (www.aepd.es). Los datos se "
       "conservarán mientras el contenido esté publicado y, después, bloqueados durante los plazos de prescripción "
       "legal."),

     P("9. Declaración y firma", sH),
     P("Declaro que he leído y comprendido este documento, que he podido hacer preguntas y que han sido resueltas, y "
       "que otorgo mi consentimiento de forma libre. Recibo una copia firmada."),
     Spacer(1, 6)]

sig = Table([[P("Firma de la persona que consiente<br/><br/><br/><br/>_____________________________<br/>"
                "Nombre:<br/>Fecha y lugar:"),
              P("Firma de la Dra. Cristina Petratti<br/><br/><br/><br/>_____________________________<br/>"
                "Nº colegiada:<br/>Fecha y lugar:")]],
            colWidths=[(W - 2 * M) / 2] * 2)
sig.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
S += [KeepTogether([sig]), Spacer(1, 8),
      P("Anexo opcional · Autorización específica de datos clínicos para un contenido concreto: autorizo la mención "
        "de ______________________________________ en el contenido descrito en el apartado 3. "
        "Firma: __________________ Fecha: __________", sS)]

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=20 * mm, bottomMargin=16 * mm,
                        title="Consentimiento de imagen, voz y testimonio", author="Dra. Cristina Petratti")
doc.build(S, onFirstPage=deco, onLaterPages=deco)
print("OK", OUT)
