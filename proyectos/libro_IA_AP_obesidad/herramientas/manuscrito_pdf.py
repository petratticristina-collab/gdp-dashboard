#!/usr/bin/env python3
"""Compila el manuscrito completo (portada, créditos, índice, declaración de transparencia, diez capítulos y anexos) en un PDF.
Uso: python3 herramientas/manuscrito_pdf.py  → manuscrito/IA_en_la_consulta_manuscrito_borrador.pdf
Requiere: pip install markdown; Chromium de Playwright."""
import subprocess, pathlib, markdown, glob, re, datetime
root = pathlib.Path(__file__).resolve().parent.parent
out_dir = root / "manuscrito"; out_dir.mkdir(exist_ok=True)
hoy = datetime.date.today().strftime("%d-%m-%Y")

def md(path):
    return markdown.markdown(pathlib.Path(path).read_text(encoding="utf-8"), extensions=["tables", "fenced_code", "sane_lists"])

caps = [root / "capitulos" / f"cap{n:02d}_v3_estilo.md" for n in range(1, 11)]
anexos = [root / "anexos" / n for n in ("anexo_A_prompts.md", "anexo_B_checklist.md", "anexo_C_glosario.md", "anexo_D_plantilla_y_recursos.md")]
anexos = [a for a in anexos if a.exists()]

# Declaración de transparencia (biblia)
biblia = (root / "biblia.md").read_text(encoding="utf-8")
m = re.search(r"## Declaración de transparencia \(va al inicio del libro\)\n(.+?)\n\n", biblia, re.S)
declaracion = m.group(1).strip() if m else "[FALTA: declaración de transparencia]"
declaracion = re.sub(r"\(incluidos los dos citados arriba\)", "", declaracion)

def titulo_cap(p):
    for line in pathlib.Path(p).read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return p.name

indice_items = "".join(f'<li><a href="#cap{i+1}">{titulo_cap(p)}</a></li>' for i, p in enumerate(caps))
indice_anexos = "".join(f'<li><a href="#anx{i}">{titulo_cap(p)}</a></li>' for i, p in enumerate(anexos))

partes = {1: "Parte I · Entender", 4: "Parte II · Usar", 9: "Parte III · Integrar y cuidar"}

cuerpo = []
for i, p in enumerate(caps, 1):
    if i in partes:
        cuerpo.append(f'<section class="parte"><h1>{partes[i]}</h1></section>')
    cuerpo.append(f'<section class="cap" id="cap{i}">{md(p)}</section>')
for i, p in enumerate(anexos):
    cuerpo.append(f'<section class="cap anexo" id="anx{i}">{md(p)}</section>')

css = """@page{size:A4;margin:20mm 19mm 22mm 19mm}
body{font-family:Georgia,"Times New Roman",serif;font-size:11pt;line-height:1.5;color:#1b2a34;margin:0}
h1{font-size:22pt;color:#0d7377;margin:0 0 6px} h2{font-size:15pt;color:#0d7377;margin:22px 0 6px;page-break-after:avoid} h3{font-size:12.5pt;color:#163a3f;margin:16px 0 4px;page-break-after:avoid}
p{margin:0 0 9px;text-align:justify} li{margin:0 0 3px} blockquote{border-left:3px solid #0d7377;margin:8px 0;padding:6px 14px;background:#f3f7f7}
pre{background:#f3f7f7;border:1px solid #d9e3e4;border-radius:6px;padding:10px 12px;font-size:9pt;white-space:pre-wrap;font-family:"Courier New",monospace;page-break-inside:avoid}
code{font-family:"Courier New",monospace;font-size:9.5pt} table{border-collapse:collapse;width:100%;font-size:9.5pt;margin:6px 0 10px} th,td{border:1px solid #d9e3e4;padding:4px 8px;text-align:left} th{background:#f3f7f7}
hr{border:0;border-top:1px solid #d9e3e4;margin:18px 0}
section.cap,section.parte,section.portada,section.creditos,section.indice,section.decl{page-break-before:always}
section.portada{page-break-before:auto;height:240mm;display:flex;flex-direction:column;justify-content:center;text-align:center}
section.portada .t{font-size:34pt;color:#0d7377;line-height:1.1;margin:0 0 10px} section.portada .s{font-size:18pt;font-style:italic;color:#163a3f;margin:0 0 30px}
section.portada .pos{font-family:Arial,sans-serif;font-size:10pt;letter-spacing:2px;text-transform:uppercase;color:#7d9490;margin-bottom:60px}
section.portada .a{font-size:16pt;color:#1b2a34} section.portada .b{font-family:Arial,sans-serif;font-size:9pt;color:#7d9490;margin-top:80px}
section.parte{height:240mm;display:flex;align-items:center;justify-content:center} section.parte h1{font-size:30pt}
section.indice ul{list-style:none;padding:0} section.indice li{margin:0 0 6px;font-size:11.5pt} section.indice a{color:#1b2a34;text-decoration:none}
section.creditos{font-family:Arial,sans-serif;font-size:9pt;color:#4a5a60;line-height:1.6}
.aviso{font-family:Arial,sans-serif;font-size:8.5pt;color:#7d9490;border:1px dashed #b9c9c9;padding:6px 10px;margin-bottom:14px}"""

portada = f"""<section class="portada">
<div class="t">IA en la consulta:<br>la revolución que cabe en diez minutos</div>
<div class="s">Aplicación práctica para el médico de familia ante la obesidad</div>
<div class="pos">Continuación profesional de <i>Obesidades sin culpa</i></div>
<div class="a">Dra. Cristina B. Petratti</div>
<div class="b">Manuscrito completo · borrador para revisión de la autora · compilado el {hoy}</div>
</section>"""

creditos = f"""<section class="creditos">
<div class="aviso">Borrador de trabajo. Los capítulos 4, 6, 7, 8, 9 y 10 están pendientes de aprobación de la autora; las marcas [VERIFICAR] y [POR ACLARAR] señalan lo que se comprueba o decide antes de imprimir. Los prompts se pegan en la herramienta vigente cuando se lea; ninguna salida de IA de este libro sustituye la valoración clínica.</div>
<p>© Cristina B. Petratti, 2026. [POR ACLARAR: editorial, ISBN, depósito legal, edición.]</p>
<p>Título: <i>IA en la consulta: la revolución que cabe en diez minutos. Aplicación práctica para el médico de familia ante la obesidad.</i></p>
<p>Prólogo: [POR ACLARAR]. Diseño de cubierta: propuesta del orquestador editorial (carpeta <code>portada/</code>).</p>
<p>Los casos clínicos de este libro son composiciones de varias personas (arquetipos compuestos) o casos sintéticos creados de cero; ninguno corresponde a una persona real. Los fármacos se citan por clase o principio activo, nunca por nombre comercial.</p>
</section>
<section class="decl"><h1>Declaración de transparencia</h1><p>{declaracion}</p></section>
<section class="indice"><h1>Índice</h1><ul>
<li><b>Parte I · Entender</b></li>{"".join(f'<li><a href="#cap{i}">{titulo_cap(caps[i-1])}</a></li>' for i in (1,2,3))}
<li style="margin-top:10px"><b>Parte II · Usar</b></li>{"".join(f'<li><a href="#cap{i}">{titulo_cap(caps[i-1])}</a></li>' for i in (4,5,6,7,8))}
<li style="margin-top:10px"><b>Parte III · Integrar y cuidar</b></li>{"".join(f'<li><a href="#cap{i}">{titulo_cap(caps[i-1])}</a></li>' for i in (9,10))}
<li style="margin-top:10px"><b>Anexos</b></li>{indice_anexos or '<li>[FALTA: anexos A-D]</li>'}
</ul></section>"""

html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>IA en la consulta · manuscrito</title><style>{css}</style></head>'
        f'<body>{portada}{creditos}{"".join(cuerpo)}</body></html>')
out_html = out_dir / "IA_en_la_consulta_manuscrito_borrador.html"; out_pdf = out_html.with_suffix(".pdf")
out_html.write_text(html, encoding="utf-8")
exe = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))[-1]
subprocess.run([exe, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                f"--print-to-pdf={out_pdf.resolve()}", out_html.resolve().as_uri()], check=True, capture_output=True)
palabras = sum(len(pathlib.Path(p).read_text(encoding="utf-8").split()) for p in caps + anexos)
print(out_pdf, out_pdf.stat().st_size, "bytes;", len(caps), "capítulos,", len(anexos), "anexos,", palabras, "palabras")
