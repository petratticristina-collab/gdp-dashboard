"""Genera tapa.pdf, contratapa.pdf, tapas_completas.pdf y previsualizaciones PNG.
Formato 15 x 23 cm. Lomo estimado 20 mm [POR ACLARAR]. Logo real incrustado desde logo_metodo_petratti.png / logo_mariposa.png. Uso: python3 build_tapas.py"""
import subprocess, pathlib
d = pathlib.Path(__file__).parent
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
W, H, LOMO = 150, 230, 20  # mm
import base64
def uri(name):
    return 'data:image/png;base64,' + base64.b64encode((d / name).read_bytes()).decode()
LOGO_FULL, LOGO_MARIPOSA = uri('logo_metodo_petratti.png'), uri('logo_mariposa.png')
FOTO = 'data:image/jpeg;base64,' + base64.b64encode((d / 'foto_autora_4x5.jpg').read_bytes()).decode()

CSS = '''
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Source+Serif+4:ital,wght@0,400;0,600;1,400;1,600&display=swap');
:root { --teal:#1AA5A5; --deep:#0E5F63; --deeper:#083F42; --green:#8DC63F; --light:#C5D96B; --grey:#8A9299; --ink:#1c2228; }
* { box-sizing: border-box; }
body { margin:0; font-family: Inter, Arial, sans-serif; color: var(--ink); -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: %(w)smm; height: %(h)smm; position: relative; overflow: hidden; }
/* TAPA */
.tapa { background: linear-gradient(160deg, var(--deep) 0%%, var(--deeper) 100%%); color:#fff; padding: 16mm 14mm 14mm; display:flex; flex-direction:column; }
.tapa .kicker { font-size: 7.5pt; letter-spacing: 3px; text-transform: uppercase; color: var(--light); font-weight:600; }
.tapa h1 { font-family: 'Source Serif 4', Georgia, serif; font-weight: 600; font-size: 46pt; line-height: 0.98; margin: 10mm 0 4mm; letter-spacing: -0.5px; }
.tapa h1 span { display:block; }
.tapa h2 { font-family: 'Source Serif 4', Georgia, serif; font-style: italic; font-weight: 400; font-size: 19pt; line-height: 1.15; margin: 0 0 6mm; color: #EAF6F6; }
.tapa h2 b { font-style: italic; font-weight: 600; color: var(--light); }
.tapa .pos { font-size: 8.5pt; letter-spacing: 2.2px; text-transform: uppercase; color: var(--green); font-weight: 600; max-width: 80mm; line-height: 1.5; }
.reloj { position:absolute; right: -8mm; top: 100mm; width: 104mm; height: 104mm; opacity: .95; }
.tapa .autor { margin-top:auto; }
.tapa .autor .dra { font-weight:300; font-size: 12pt; letter-spacing: 1px; color:#DDEFEF; }
.tapa .autor .nombre { font-weight: 800; font-size: 20pt; letter-spacing: .3px; line-height: 1.05; }
.tapa .autor .desc { font-size: 8.5pt; letter-spacing: 1.6px; text-transform: uppercase; color: var(--light); margin-top: 2mm; font-weight:600; }
.tapa .mariposa { position:absolute; right: 13mm; bottom: 13mm; width: 13mm; height:auto; }
.tapa .pie { margin-top: 5mm; font-size: 7.5pt; color: #B9D8D9; line-height: 1.5; border-top: 1px solid rgba(255,255,255,.25); padding-top: 3mm; padding-right: 20mm; }
/* CONTRATAPA */
.contra { background:#fff; padding: 12mm 13mm 10mm; display:flex; flex-direction:column; border-left: 6mm solid var(--teal); }
.contra .apertura { font-family: 'Source Serif 4', Georgia, serif; font-size: 12.5pt; line-height: 1.28; color: var(--deep); font-weight: 600; margin: 0 0 4.5mm; }
.contra .sin { font-family: 'Source Serif 4', Georgia, serif; font-size: 9.1pt; line-height: 1.4; }
.contra .sin p { margin: 0 0 3mm; }
.contra .sin em { color: var(--deep); }
.contra ul { margin: 1.5mm 0 4mm; padding-left: 5mm; font-size: 8.5pt; line-height: 1.35; }
.contra li { margin-bottom: 1.2mm; }
.contra li::marker { color: var(--green); }
.contra .bio { display:flex; gap: 5mm; align-items:flex-start; border-top: 1px solid #d7dde3; padding-top: 3mm; margin-top:auto; }
.contra .foto { width: 24mm; height: 30mm; object-fit: cover; border-radius: 1.5mm; flex-shrink:0; }
.contra .bio p { font-size: 7.4pt; line-height: 1.38; margin:0; }
.contra .bio b { color: var(--deep); }
.contra .tecnico { display:flex; justify-content:space-between; align-items:flex-end; margin-top: 4mm; }
.contra .decl { font-size: 6.4pt; color: var(--grey); max-width: 70mm; line-height: 1.35; }
.contra .isbn { width: 38mm; height: 22mm; border: 1px dashed var(--grey); font-size: 6.5pt; color: var(--grey); display:flex; align-items:center; justify-content:center; text-align:center; }
.contra .marca { font-size: 8pt; font-weight: 800; color: var(--teal); letter-spacing: .5px; }
.contra .marca img { width: 34mm; height:auto; display:block; margin-bottom: 1mm; }
.contra .marca small { display:block; font-weight:400; color: var(--grey); letter-spacing: 1.5px; font-size: 5.8pt; text-transform: uppercase; }
/* LOMO */
.lomo { width: %(l)smm; height: %(h)smm; background: var(--deeper); color:#fff; position:relative; }
.lomo .txt { position:absolute; left:50%%; top:50%%; transform: translate(-50%%,-50%%) rotate(90deg); white-space:nowrap; font-size: 10pt; letter-spacing: 1px; }
.lomo .txt b { font-family: 'Source Serif 4', Georgia, serif; font-weight:600; margin-right: 8mm; }
.lomo .logo { position:absolute; bottom: 7mm; left: 50%%; transform: translateX(-50%%); width: 10mm; height:auto; }
.spread { display:flex; }
''' % dict(w=W, h=H, l=LOMO)

RELOJ = '''
<svg class="reloj" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="84" fill="none" stroke="rgba(255,255,255,0.14)" stroke-width="10"/>
  <path d="M100 16 A84 84 0 0 1 172.7 58" fill="none" stroke="#8DC63F" stroke-width="10" stroke-linecap="round"/>
  <path d="M100 16 A84 84 0 0 1 172.7 58 L100 100 Z" fill="rgba(197,217,107,0.18)"/>
  <g stroke="rgba(255,255,255,0.45)" stroke-width="2">
    <line x1="100" y1="22" x2="100" y2="30"/><line x1="178" y1="100" x2="170" y2="100"/>
    <line x1="100" y1="178" x2="100" y2="170"/><line x1="22" y1="100" x2="30" y2="100"/>
  </g>
  <line x1="100" y1="100" x2="100" y2="34" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
  <line x1="100" y1="100" x2="160" y2="65" stroke="#C5D96B" stroke-width="4" stroke-linecap="round"/>
  <circle cx="100" cy="100" r="5" fill="#fff"/>
  <text x="118" y="14" font-family="Inter, Arial" font-size="11" font-weight="700" fill="#C5D96B">10 min</text>
</svg>'''

TAPA = f'''<div class="page tapa">
  <div class="kicker">Continuación profesional de <i>Obesidades sin culpa</i></div>
  <h1><span>IA en</span><span>la consulta</span></h1>
  <h2>la revolución que cabe<br>en <b>diez minutos</b></h2>
  <div class="pos">Aplicación práctica para el médico de familia ante la obesidad</div>
  {RELOJ}
  <div class="autor"><div class="dra">Dra.</div><div class="nombre">Cristina B. Petratti</div><div class="desc">Médica de familia · Especialista en obesidad</div></div>
  <div class="pie">Prólogo de [POR ACLARAR: nombre y cargo] · Más de setenta casos de uso con prompts listos para pegar, sin datos de ningún paciente</div>
  <img class="mariposa" src="{LOGO_MARIPOSA}" alt="">
</div>'''

CONTRA = f'''<div class="page contra">
  <div class="apertura">Treinta y cuatro pacientes, seis huecos de urgencias, dos domicilios y siete minutos por persona. Ahí es donde la inteligencia artificial tiene que caber. Si no cabe ahí, no sirve.</div>
  <div class="sin">
    <p>Este libro no promete que una máquina vaya a ver a tus pacientes por ti. Promete algo más útil: devolverte minutos y enseñarte qué hacer con ellos cuando la persona que tienes delante lleva veinte años oyendo «coma menos y muévase más».</p>
    <p>En diez capítulos, una médica de familia con más de veinticinco años de consulta cuenta cómo usa hoy la IA generativa ante la obesidad, sin meter ningún dato de nadie en ninguna herramienta: la hoja para la paciente en su idioma, el asistente que cita las guías y no decide, la calculadora que construyó sin saber programar, el guion del reel que pasa una auditoría antes de publicarse, la notificación de un efecto adverso, la hoja de ruta de noventa días. Más de setenta casos de uso, cada uno con su prompt listo para pegar, su ejemplo, lo que hay que revisar antes de usarlo y el riesgo que conviene conocer.</p>
    <p>Todo con una idea en el centro, la misma que en <em>Obesidades sin culpa</em>: <em>no es falta de voluntad, es biología</em>. La máquina te devuelve los minutos. Lo que cabe en ellos, con la persona delante, lo haces tú.</p>
  </div>
  <ul>
    <li>Prompts para consulta, seguimiento, burocracia, docencia y divulgación, sin datos de pacientes.</li>
    <li>Lo que sale mal y cómo pararlo antes de que llegue a la persona: sesgo de peso, alucinaciones, exceso de seguridad.</li>
    <li>Un plan de noventa días y una comunidad de práctica para no aprender esto sola.</li>
  </ul>
  <div class="bio">
    <img class="foto" src="{FOTO}" alt="Cristina B. Petratti">
    <p><b>Cristina B. Petratti</b> es médica de familia, especialista en obesidad y salud metabólica, con más de veinticinco años de consulta. Miembro de la SEEDO (Grupo de Trabajo de Ejercicio Físico y Obesidad; coautora de SEEDO GO!), creadora del Método Petratti y autora de <i>Obesidades sin culpa</i> (2026). Se formó en 2026 en inteligencia artificial generativa para profesionales sanitarios y en compliance para la divulgación científica digital. Corrió la maratón de Londres en 2025. Ejerce en Alicante y, en consulta online, con pacientes de Argentina.</p>
  </div>
  <div class="tecnico">
    <div>
      <div class="marca"><img src="{LOGO_FULL}" alt="Método Dra. Petratti"><small>Medicina de la obesidad · Salud metabólica</small></div>
      <div class="decl" style="margin-top:2mm">La autora declara vínculos con la industria farmacéutica, detallados al inicio del libro. Ningún medicamento de prescripción aparece con nombre comercial.</div>
    </div>
    <div class="isbn">ISBN [POR ACLARAR]<br>código de barras<br>precio [POR ACLARAR]</div>
  </div>
</div>'''

LOMO_HTML = f'<div class="lomo"><div class="txt"><b>IA en la consulta</b> Dra. Cristina B. Petratti · Médica de familia, especialista en obesidad</div><img class="logo" src="{LOGO_MARIPOSA}" alt=""></div>'

def html(body, w, h):
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}
@page {{ size: {w}mm {h}mm; margin: 0; }}</style></head><body>{body}</body></html>'''

def render(name, body, w, h):
    src = d / f'{name}.html'
    src.write_text(html(body, w, h), encoding='utf-8')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
                    f'--print-to-pdf={d / (name + ".pdf")}', '--virtual-time-budget=10000', str(src)], check=True, capture_output=True)
    px_w, px_h = int(w * 4), int(h * 4)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', f'--screenshot={d / (name + ".png")}',
                    f'--window-size={px_w},{px_h}', '--force-device-scale-factor=1', '--virtual-time-budget=10000', str(src)], check=True, capture_output=True)
    print(name, (d / (name + '.pdf')).stat().st_size)

render('tapa', TAPA, W, H)
render('contratapa', CONTRA, W, H)
render('tapas_completas', f'<div class="spread">{CONTRA}{LOMO_HTML}{TAPA}</div>', 2 * W + LOMO, H)
