"""Logo "Cristina Petratti": mariposa original intacta + texto nuevo en el mismo color y composición.

Uso: python logo_cristina.py [--fuente SquarePeg-Regular.ttf]
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
FONTS = HERE.parent / "historia-instagram" / "fonts"
TEAL = (29, 166, 165)  # color exacto del texto original
BUTTERFLY_RIGHT = 430  # la mariposa ocupa x < 416; a partir de aquí solo hay texto
TEXT_BOX = (478, 200, 952, 534)  # caja que ocupaba "Método Dra. Petratti"


def fit(draw, text, path, max_w, max_h):
    size = 300
    while size > 20:
        f = ImageFont.truetype(str(path), size)
        l, t, r, b = draw.textbbox((0, 0), text, font=f)
        if r - l <= max_w and b - t <= max_h:
            return f
        size -= 2
    return f


def build(fuente, salida, grosor):
    logo = Image.open(HERE / "logo-original.jpg").convert("RGB")
    out = logo.copy()
    d = ImageDraw.Draw(out)
    d.rectangle([BUTTERFLY_RIGHT, 0, out.width, out.height], fill="white")  # solo se borra el texto

    x0, y0, x1, y1 = TEXT_BOX
    w = x1 - x0
    gap = 24
    h_line = (y1 - y0 - gap) / 2
    fpath = FONTS / fuente
    f = min((fit(d, s, fpath, w, h_line) for s in ("Cristina", "Petratti")), key=lambda f: f.size)

    y = y0
    for s in ("Cristina", "Petratti"):
        l, t, r, b = d.textbbox((0, 0), s, font=f)
        d.text((x0 - l, y - t), s, font=f, fill=TEAL, stroke_width=grosor, stroke_fill=TEAL)
        y += (b - t) + gap
    out.save(salida)
    print(f"Guardado: {salida}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--fuente", default="SquarePeg-Regular.ttf")
    p.add_argument("--grosor", type=int, default=2, help="engrosa el trazo para igualar el original")
    p.add_argument("--salida", default=str(HERE / "logo-cristina-petratti.png"))
    a = p.parse_args()
    build(a.fuente, a.salida, a.grosor)
