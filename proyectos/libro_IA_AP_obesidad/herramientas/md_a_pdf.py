#!/usr/bin/env python3
"""Convierte un capítulo en Markdown al HTML y PDF de lectura del libro.
Uso: python3 md_a_pdf.py capitulos/cap04_v3_estilo.md 4 "versión de estilo v3 (12-09-2026)"
Requiere: pip install markdown; Chromium de Playwright en /opt/pw-browsers (Node playwright global).
"""
import sys, subprocess, pathlib, markdown, json, glob, os
src = pathlib.Path(sys.argv[1]); num = sys.argv[2]; etiqueta = sys.argv[3] if len(sys.argv) > 3 else "borrador"
cuerpo = markdown.markdown(src.read_text(encoding="utf-8"), extensions=["tables", "fenced_code", "sane_lists"])
head = ("IA en la consulta: la revolución que cabe en diez minutos · Aplicación práctica para el médico de familia "
        f"ante la obesidad · Dra. Cristina Petratti · Capítulo {num}, {etiqueta} · Borrador para revisión de la autora")
css = """@page{size:A4;margin:20mm 19mm 22mm 19mm}
body{font-family:Georgia,"Times New Roman",serif;font-size:11pt;line-height:1.5;color:#1b2a34;margin:0}
h1{font-size:22pt;color:#0d7377;margin:0 0 6px} h2{font-size:15pt;color:#0d7377;margin:22px 0 6px;page-break-after:avoid} h3{font-size:12.5pt;color:#163a3f;margin:16px 0 4px;page-break-after:avoid}
p{margin:0 0 9px;text-align:justify} li{margin:0 0 3px} blockquote{border-left:3px solid #0d7377;margin:8px 0;padding:6px 14px;background:#f3f7f7}
pre{background:#f3f7f7;border:1px solid #d9e3e4;border-radius:6px;padding:10px 12px;font-size:9pt;white-space:pre-wrap;font-family:"Courier New",monospace;page-break-inside:avoid}
code{font-family:"Courier New",monospace;font-size:9.5pt} table{border-collapse:collapse;width:100%;font-size:9.5pt;margin:6px 0 10px} th,td{border:1px solid #d9e3e4;padding:4px 8px;text-align:left} th{background:#f3f7f7}
hr{border:0;border-top:1px solid #d9e3e4;margin:18px 0}
.head{font-size:9pt;color:#7d9490;margin-bottom:14px}"""
html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Capítulo {num}</title><style>{css}</style></head>'
        f'<body><div class="head">{head}</div>{cuerpo}</body></html>')
out_html = src.parent / f"Capitulo_{num}_v3_borrador.html"; out_pdf = out_html.with_suffix(".pdf")
out_html.write_text(html, encoding="utf-8")
exe = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))[-1]
subprocess.run([exe, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                f"--print-to-pdf={out_pdf.resolve()}", out_html.resolve().as_uri()], check=True, capture_output=True)
print(out_html, out_pdf, out_pdf.stat().st_size, "bytes")
