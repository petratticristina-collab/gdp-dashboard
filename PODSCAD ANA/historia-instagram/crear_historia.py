"""Genera una historia de Instagram (1080x1920) para promocionar el episodio en YouTube.

Uso:
    python crear_historia.py --foto foto.jpg --titulo "Título del episodio" --con "Cristina & Ana"
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

W, H = 1080, 1920
HERE = Path(__file__).parent
FONTS = HERE / "fonts"

# Paleta: verde petróleo profundo + rubor cálido
INK = (16, 46, 52)
INK_2 = (24, 66, 72)
BLUSH = (242, 196, 182)
CREAM = (250, 244, 238)
RED = (230, 58, 52)  # rojo YouTube suavizado


def font(name, size, weight=None):
    f = ImageFont.truetype(str(FONTS / name), size)
    if weight is not None:
        f.set_variation_by_axes([weight])
    return f


def wrap(draw, text, fnt, max_w):
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=fnt) <= max_w:
            line = test
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def placeholder(size):
    w, h = size
    img = Image.new("RGB", size, INK_2)
    d = ImageDraw.Draw(img)
    f = font("Montserrat.ttf", 44, 600)
    msg = "AQUÍ VA VUESTRA FOTO"
    d.text(((w - d.textlength(msg, font=f)) / 2, h / 2 - 22), msg, font=f, fill=BLUSH)
    return img


def rounded(img, radius):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, *img.size], radius, fill=255)
    out = Image.new("RGBA", img.size)
    out.paste(img, (0, 0), mask)
    return out


def build(foto, titulo, con, salida):
    canvas = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(canvas)

    # Halo suave detrás de la foto
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([90, 300, 990, 1300], fill=(*BLUSH, 70))
    canvas.paste(glow.filter(ImageFilter.GaussianBlur(140)), (0, 0), glow.filter(ImageFilter.GaussianBlur(140)))
    d = ImageDraw.Draw(canvas)

    # Cabecera (fuera de la zona que tapa la interfaz de Instagram)
    f_label = font("Montserrat.ttf", 30, 700)
    label = "P O D S C A D   A N A"
    d.text(((W - d.textlength(label, font=f_label)) / 2, 230), label, font=f_label, fill=BLUSH)
    f_new = font("Montserrat.ttf", 26, 500)
    new = "NUEVO EPISODIO"
    tw = d.textlength(new, font=f_new)
    d.rounded_rectangle([(W - tw) / 2 - 26, 286, (W + tw) / 2 + 26, 336], 25, outline=BLUSH, width=2)
    d.text(((W - tw) / 2, 296), new, font=f_new, fill=CREAM)

    # Foto de las dos
    box = (900, 860)
    photo = ImageOps.fit(Image.open(foto).convert("RGB"), box, centering=(0.5, 0.4)) if foto else placeholder(box)
    photo = rounded(photo, 48)
    x, y = (W - box[0]) // 2, 390
    d.rounded_rectangle([x - 10, y - 10, x + box[0] + 10, y + box[1] + 10], 56, outline=BLUSH, width=3)
    canvas.paste(photo, (x, y), photo)

    # Título
    f_title = font("PlayfairDisplay.ttf", 72, 700)
    lines = wrap(d, titulo, f_title, 900)[:3]
    ty = y + box[1] + 50
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f_title)) / 2, ty), ln, font=f_title, fill=CREAM)
        ty += 84

    f_con = font("PlayfairDisplay-Italic.ttf", 44, 400)
    con_txt = f"con {con}"
    d.text(((W - d.textlength(con_txt, font=f_con)) / 2, ty + 10), con_txt, font=f_con, fill=BLUSH)

    # Botón YouTube (deja debajo espacio para el sticker de enlace)
    f_btn = font("Montserrat.ttf", 36, 700)
    btn = "Míralo completo en YouTube"
    bw = d.textlength(btn, font=f_btn) + 100 + 44
    bx, by = (W - bw) / 2, max(ty + 90, 1580)
    d.rounded_rectangle([bx, by, bx + bw, by + 84], 42, fill=CREAM)
    d.rounded_rectangle([bx + 22, by + 20, bx + 82, by + 64], 12, fill=RED)
    d.polygon([(bx + 44, by + 30), (bx + 44, by + 54), (bx + 64, by + 42)], fill=CREAM)
    d.text((bx + 100, by + 22), btn, font=f_btn, fill=INK)

    canvas.save(salida, quality=95)
    print(f"Guardado: {salida}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--foto", help="Foto de las dos (jpg/png). Sin ella se usa un hueco de muestra.")
    p.add_argument("--titulo", default="Obesidad: lo que la ciencia sabe hoy")
    p.add_argument("--con", default="Dra. Cristina Petratti & Ana")
    p.add_argument("--salida", default=str(HERE / "historia.png"))
    a = p.parse_args()
    build(a.foto, a.titulo, a.con, a.salida)
