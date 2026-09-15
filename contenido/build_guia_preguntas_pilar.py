"""Guía de preguntas en PDF para que una paciente cuente su experiencia en sus propias palabras."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "guia-preguntas-testimonio-pilar.pdf")
LOGO = os.path.join(HERE, "logo-metodo-petratti.png")
TURQ, LIMA, VERDE, GRIS, GRIS_OSC = (HexColor("#00A8A4"), HexColor("#94C01C"), HexColor("#D0E08C"),
                                     HexColor("#88888C"), HexColor("#3F4548"))
SUAVE = HexColor("#F1F8F0")
pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
W, H = A4
M = 20 * mm

sT = ParagraphStyle("T", fontName="DVB", fontSize=20, leading=25, textColor=TURQ, spaceAfter=4)
sSub = ParagraphStyle("Sub", fontName="DV", fontSize=11, leading=15.5, textColor=GRIS_OSC, spaceAfter=10)
sH = ParagraphStyle("H", fontName="DVB", fontSize=12.5, leading=16, textColor=TURQ, spaceBefore=10, spaceAfter=3)
sB = ParagraphStyle("B", fontName="DV", fontSize=10.2, leading=14.5, textColor=GRIS_OSC, spaceAfter=4)
sQ = ParagraphStyle("Q", fontName="DVB", fontSize=10.5, leading=14.5, textColor=GRIS_OSC, spaceAfter=1)
sQn = ParagraphStyle("Qn", fontName="DV", fontSize=9.2, leading=12.5, textColor=GRIS, leftIndent=14, spaceAfter=7)
sS = ParagraphStyle("S", fontName="DV", fontSize=8, leading=10.5, textColor=GRIS, spaceAfter=2)
sBox = ParagraphStyle("Box", fontName="DV", fontSize=10, leading=14, textColor=GRIS_OSC)


def P(t, s=sB): return Paragraph(t, s)


def q(n, pregunta, nota):
    return [Paragraph(f"<font color='#94C01C'>{n}.</font>&nbsp; {pregunta}", sQ), Paragraph(nota, sQn)]


def box(title, lines, bg=SUAVE):
    inner = [Paragraph(f"<b><font color='#00A8A4'>{title}</font></b>", sBox)]
    inner += [Paragraph(f"<font color='#94C01C'>■</font>&nbsp; {l}", sBox) for l in lines]
    t = Table([[inner]], colWidths=[W - 2 * M])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 12),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 10),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 10), ("ROUNDEDCORNERS", [8, 8, 8, 8])]))
    return t


def deco(canvas, doc):
    canvas.saveState()
    if os.path.exists(LOGO):
        canvas.drawImage(LOGO, W - M - 36 * mm, H - 16 * mm, width=36 * mm, height=12 * mm,
                         preserveAspectRatio=True, mask="auto", anchor="ne")
    canvas.setStrokeColor(VERDE); canvas.setLineWidth(0.8)
    canvas.line(M, 14 * mm, W - M, 14 * mm)
    canvas.setFont("DV", 7); canvas.setFillColor(GRIS)
    canvas.drawString(M, 9.5 * mm, "Tu historia es tuya. Esta guía solo te ayuda a ordenarla. "
                      "Puedes cambiar, saltar o quitar cualquier pregunta.")
    canvas.drawRightString(W - M, 9.5 * mm, f"Dra. Cristina Petratti · pág. {doc.page}")
    canvas.restoreState()


S = [Spacer(1, 8),
     P("Para Pilar", sT),
     P("Preguntas para contar tu historia con tus palabras", sSub),
     P("Gracias por querer contarlo. Lo que tú viviste puede ayudar a muchas mujeres que hoy se sienten como tú te "
       "sentías. No hace falta que sea perfecto ni que sigas un guion: son preguntas para ayudarte a ordenar lo que "
       "ya sabes. Respóndelas en voz alta, como si se lo contaras a una amiga, y quédate con lo que te salga "
       "natural."),
     P("Puedes grabar un vídeo hablando a cámara, un audio, o escribirlo. Lo que te resulte más cómodo."),

     P("Bloque 1 · Dónde estabas", sH)]
S += q(1, "¿Cómo era tu día a día con el peso antes de empezar? ¿Qué hacías?",
       "Cuenta lo que hacías de verdad: el entrenamiento, la comida, el tratamiento. Sin justificarte.")
S += q(2, "¿Qué esperabas que pasara y qué pasaba en realidad?",
       "Aquí está tu frustración. Nómbrala. «Hacía todo y la barriga seguía ahí.»")
S += q(3, "¿Cómo te hacía sentir eso contigo misma?",
       "Esto es lo que más va a conectar con quien te escuche. Culpa, rabia, cansancio, vergüenza… lo que fuera.")
S += q(4, "¿Qué te decías a ti misma en ese momento?",
       "Una frase literal, si la recuerdas. «A mí no me funciona nada.»")

S += [P("Bloque 2 · Lo que nadie te había explicado", sH)]
S += q(5, "¿Qué fue lo primero que te sorprendió cuando alguien miró tu caso entero?",
       "La menopausia y la grasa del abdomen, la cintura en vez de la báscula, el sueño, la fuerza… Elige lo que "
       "a ti te cambió la mirada, no todo.")
S += q(6, "¿Hubo algo que llevabas años haciendo y que resultó no ser lo que tocaba?",
       "No es un fallo tuyo: es lo que te habían dicho. Cuéntalo así.")
S += q(7, "¿Qué sentiste al entender por fin lo que te pasaba?",
       "Alivio, enfado por no saberlo antes, esperanza. Lo que sea real.")

S += [P("Bloque 3 · Lo que cambiaste", sH)]
S += q(8, "¿Qué cambiaste concretamente en tu rutina?",
       "Cosas concretas y tuyas: «empecé a hacer fuerza», «dejé de pesarme», «me mido la cintura», «duermo siete "
       "horas», «bajé el vino».")
S += q(9, "¿Qué fue lo más difícil de cambiar y qué te ayudó?",
       "Esto da credibilidad. Nadie se cree un cambio sin esfuerzo.")
S += q(10, "¿Cómo encaja el tratamiento en todo esto?",
       "Puedes decir que llevas «tratamiento para la obesidad» y que no sustituye lo demás. No hace falta decir "
       "cuál ni cuánto: eso es tuyo y de tu médica.")

S += [PageBreak(), P("Bloque 4 · Cómo estás hoy", sH)]
S += q(11, "¿Qué es distinto hoy en tu relación con tu cuerpo?",
       "Sin cifras. Lo que importa es cómo te sientes y cómo te miras.")
S += q(12, "¿Qué haces hoy que antes no hacías, y qué has dejado de hacer?",
       "Por ejemplo: «he dejado de pelearme con la báscula».")
S += q(13, "Si pudieras hablar con la Pilar de hace dos años, ¿qué le dirías?",
       "Suele ser la frase más bonita del testimonio. Tómate tu tiempo.")

S += [P("Bloque 5 · Para quién lo cuentas", sH)]
S += q(14, "¿A quién le gustaría que le llegara tu historia?",
       "«A las mujeres de mi edad que hacen todo y sienten que nada cambia.»")
S += q(15, "¿Qué querrías que esa persona supiera después de escucharte?",
       "Una sola idea. «No es tu culpa. Es que nadie te ha mirado entera.»")
S += q(16, "¿Quieres mencionar a alguien que te ayudó? ¿Cómo lo dirías?",
       "Es opcional y es decisión tuya. Si lo haces, mejor «me ayudó a entender» que «con ella se baja la grasa». "
       "Lo primero es verdad y es tuyo; lo segundo es una promesa que nadie puede hacer.")

S += [Spacer(1, 8),
      box("Para grabarlo cómoda", [
          "Entre 60 y 90 segundos si es vídeo. Si te sale más largo, no pasa nada: se puede cortar.",
          "Luz de una ventana de frente, móvil a la altura de los ojos, sin música de fondo.",
          "Habla como hablas. Si te equivocas, respira y sigue; no hace falta empezar de cero.",
          "Graba dos o tres tomas y elige la que más se parezca a ti, no la más «perfecta».",
          "Si prefieres no salir con la cara, vale igual: voz sobre una foto tuya o un paisaje funciona.",
      ]),
      Spacer(1, 8),
      box("Lo que te protege a ti (por eso te lo pido)", [
          "No digas el nombre del medicamento ni la dosis. «Tratamiento para la obesidad» es suficiente.",
          "No des kilos, centímetros ni resultados de analíticas. Invitan a comparaciones que no te sirven.",
          "Evita fotos de antes y después. Tu historia vale por lo que entendiste, no por lo que pesabas.",
          "No hables de otras personas (familia, amigas) sin su permiso.",
          "Si en algún momento no quieres que siga publicado, me lo dices y lo retiro. Sin explicaciones.",
      ], bg=HexColor("#EAF6F6")),
      Spacer(1, 10),
      P("Cuando lo tengas, mándamelo si quieres que lo vea antes de publicarlo, o publícalo directamente en tu "
        "cuenta. Es tu historia. Gracias por contarla."),
      Spacer(1, 4),
      P("Dra. Cristina Petratti", sQ),
      P("Este documento es una guía personal para ordenar tu experiencia. No contiene ni sustituye indicaciones "
        "médicas; cualquier duda sobre tu tratamiento la vemos en consulta.", sS)]

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=20 * mm, bottomMargin=18 * mm,
                        title="Preguntas para contar tu historia", author="Dra. Cristina Petratti")
doc.build(S, onFirstPage=deco, onLaterPages=deco)
print("OK", OUT)
