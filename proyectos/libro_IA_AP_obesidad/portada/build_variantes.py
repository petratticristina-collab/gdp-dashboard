"""Dos variantes de tapa (B: clara y editorial; C: tipográfica con el 10) a 15 x 23 cm. Uso: python3 build_variantes.py"""
import subprocess, pathlib
d = pathlib.Path(__file__).parent
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
W, H = 150, 230

BASE = '''
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap');
:root { --teal:#1AA5A5; --deep:#0E5F63; --deeper:#083F42; --green:#8DC63F; --light:#C5D96B; --grey:#8A9299; --ink:#1c2228; }
* { box-sizing:border-box; } body { margin:0; font-family: Inter, Arial, sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { width: %(w)smm; height: %(h)smm; position:relative; overflow:hidden; }
@page { size: %(w)smm %(h)smm; margin:0; }
''' % dict(w=W, h=H)

# Variante B: fondo claro, franja verde azulado, mariposa abstracta de cuatro hojas (guiño al logo), tipografía serif
CSS_B = BASE + '''
.b { background:#FBFCFA; color: var(--ink); padding: 14mm 14mm 12mm; display:flex; flex-direction:column; }
.b .franja { position:absolute; left:0; top:0; width: 9mm; height:100%%; background: linear-gradient(180deg, var(--teal), var(--green)); }
.b .kicker { font-size:7.5pt; letter-spacing:3px; text-transform:uppercase; color: var(--teal); font-weight:600; margin-left: 4mm; }
.b h1 { font-family:'Source Serif 4', Georgia, serif; font-weight:700; font-size: 44pt; line-height: 1; margin: 12mm 0 4mm 4mm; color: var(--deeper); }
.b h1 span { display:block; }
.b h2 { font-family:'Source Serif 4', Georgia, serif; font-style:italic; font-weight:400; font-size:18pt; line-height:1.15; margin: 0 0 0 4mm; color: var(--deep); }
.b h2 b { font-weight:600; color: var(--teal); }
.b .pos { font-size: 8pt; letter-spacing:2px; text-transform:uppercase; color: var(--grey); margin: 7mm 0 0 4mm; max-width: 78mm; line-height:1.5; }
.b .alas { position:absolute; right: 8mm; top: 112mm; width: 78mm; height: 78mm; }
.b .autor { margin-top:auto; margin-left:4mm; }
.b .dra { font-weight:300; font-size:11pt; color: var(--grey); letter-spacing:1px; }
.b .nombre { font-weight:800; font-size:19pt; color: var(--deeper); line-height:1.05; }
.b .desc { font-size:8pt; letter-spacing:1.6px; text-transform:uppercase; color: var(--teal); font-weight:600; margin-top:2mm; }
.b .pie { margin: 5mm 0 0 4mm; font-size:7.3pt; color: var(--grey); border-top:1px solid #dfe6e6; padding-top:3mm; line-height:1.5; }
'''
ALAS = '''<svg class="alas" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
<path d="M100 100 C 70 30, 20 40, 30 90 C 40 120, 80 115, 100 100 Z" fill="#8DC63F" opacity=".95"/>
<path d="M100 100 C 130 25, 190 45, 175 95 C 165 125, 120 118, 100 100 Z" fill="#1AA5A5" opacity=".95"/>
<path d="M100 100 C 60 130, 40 180, 85 180 C 105 178, 105 130, 100 100 Z" fill="#C5D96B" opacity=".95"/>
<path d="M100 100 C 140 128, 165 175, 120 182 C 100 184, 98 135, 100 100 Z" fill="#0E5F63" opacity=".9"/>
<circle cx="100" cy="100" r="6" fill="#fff" stroke="#083F42" stroke-width="2"/>
<path d="M100 94 A 22 22 0 0 1 119 106" fill="none" stroke="#083F42" stroke-width="3" stroke-linecap="round"/>
</svg>'''
TAPA_B = f'''<div class="page b"><div class="franja"></div>
<div class="kicker">Continuación profesional de <i>Obesidades sin culpa</i></div>
<h1><span>IA en</span><span>la consulta</span></h1>
<h2>la revolución que cabe<br>en <b>diez minutos</b></h2>
<div class="pos">Aplicación práctica para el médico de familia ante la obesidad</div>
{ALAS}
<div class="autor"><div class="dra">Dra.</div><div class="nombre">Cristina B. Petratti</div><div class="desc">Médica de familia · Especialista en obesidad</div></div>
<div class="pie">Prólogo de [POR ACLARAR] · Más de setenta casos de uso con prompts listos para pegar, sin datos de ningún paciente</div>
</div>'''

# Variante C: tipográfica, el número 10 enorme, fondo verde azulado medio, texto blanco
CSS_C = BASE + '''
.c { background: var(--teal); color:#fff; padding: 14mm; display:flex; flex-direction:column; }
.c .diez { position:absolute; right: 4mm; top: 92mm; font-weight:900; font-size: 190pt; line-height: .8; color: rgba(255,255,255,.16); letter-spacing:-8px; }
.c .min { position:absolute; right: 16mm; top: 150mm; font-family:'Source Serif 4', Georgia, serif; font-style:italic; font-size: 22pt; color: var(--light); }
.c .kicker { font-size:7.5pt; letter-spacing:3px; text-transform:uppercase; color: var(--light); font-weight:600; }
.c h1 { font-weight:900; font-size: 40pt; line-height:.98; margin: 12mm 0 5mm; letter-spacing:-1px; }
.c h1 span { display:block; }
.c h2 { font-family:'Source Serif 4', Georgia, serif; font-style:italic; font-weight:400; font-size:17pt; line-height:1.15; margin:0; max-width: 90mm; }
.c h2 b { font-weight:600; color: var(--light); }
.c .pos { font-size:8pt; letter-spacing:2px; text-transform:uppercase; color:#E8F5F5; margin-top:7mm; max-width:80mm; line-height:1.5; font-weight:600; }
.c .bloque { margin-top:auto; background: var(--deeper); margin-left:-14mm; margin-right:-14mm; margin-bottom:-14mm; padding: 9mm 14mm 11mm; }
.c .dra { font-weight:300; font-size:11pt; color:#B9D8D9; letter-spacing:1px; }
.c .nombre { font-weight:800; font-size:19pt; line-height:1.05; }
.c .desc { font-size:8pt; letter-spacing:1.6px; text-transform:uppercase; color: var(--green); font-weight:600; margin-top:2mm; }
.c .pie { margin-top:4mm; font-size:7.3pt; color:#B9D8D9; line-height:1.5; }
'''
TAPA_C = '''<div class="page c">
<div class="diez">10</div><div class="min">minutos</div>
<div class="kicker">Continuación profesional de <i>Obesidades sin culpa</i></div>
<h1><span>IA en</span><span>la consulta</span></h1>
<h2>la revolución que cabe en <b>diez minutos</b></h2>
<div class="pos">Aplicación práctica para el médico de familia ante la obesidad</div>
<div class="bloque"><div class="dra">Dra.</div><div class="nombre">Cristina B. Petratti</div><div class="desc">Médica de familia · Especialista en obesidad</div>
<div class="pie">Prólogo de [POR ACLARAR] · Más de setenta casos de uso con prompts listos para pegar, sin datos de ningún paciente</div></div>
</div>'''

def render(name, css, body):
    src = d / f'{name}.html'
    src.write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>', encoding='utf-8')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer', f'--print-to-pdf={d / (name + ".pdf")}', '--virtual-time-budget=10000', str(src)], check=True, capture_output=True)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', f'--screenshot={d / (name + ".png")}', f'--window-size={W*4},{H*4}', '--virtual-time-budget=10000', str(src)], check=True, capture_output=True)
    print(name, 'ok')

render('tapa_variante_B_clara', CSS_B, TAPA_B)
render('tapa_variante_C_tipografica', CSS_C, TAPA_C)
