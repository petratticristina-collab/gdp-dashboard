"""Historia de Instagram (1080x1920) a partir de la portada de "Obesidad sin rodeos".

Uso:
    python historia_portada.py --portada portada.png --salida historia-youtube.png
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

W, H = 1080, 1920
HERE = Path(__file__).parent
FONTS = HERE / "fonts"

# Colores tomados de la portada
TEAL = (3, 52, 67)
TEAL_DEEP = (0, 28, 37)
GOLD = (226, 190, 98)
CREAM = (250, 244, 232)
RED = (229, 45, 39)


def font(size, weight):
    f = ImageFont.truetype(str(FONTS / "Montserrat.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def centered(d, y, text, fnt, fill):
    d.text(((W - d.textlength(text, font=fnt)) / 2, y), text, font=fnt, fill=fill)


def build(portada, salida, linea1, linea2):
    cover = Image.open(portada).convert("RGB")

    # Fondo: la propia portada, desenfocada y oscurecida, con degradado teal
    bg = cover.resize((H, H)).crop(((H - W) // 2, 0, (H + W) // 2, H))
    bg = ImageEnhance.Brightness(bg.filter(ImageFilter.GaussianBlur(60))).enhance(0.55)
    grad = Image.new("RGB", (W, H))
    gd = ImageDraw.Draw(grad)
    for y in range(H):
        t = y / H
        gd.line([(0, y), (W, y)], fill=tuple(int(TEAL[i] * (1 - t) + TEAL_DEEP[i] * t) for i in range(3)))
    canvas = Image.blend(bg, grad, 0.6)
    d = ImageDraw.Draw(canvas)

    # Cabecera con filetes dorados, como en la portada
    f_kicker = font(32, 700)
    kicker = "N U E V O   E P I S O D I O"
    kw = d.textlength(kicker, font=f_kicker)
    ky = 250
    centered(d, ky, kicker, f_kicker, GOLD)
    d.line([(90, ky + 20), ((W - kw) / 2 - 30, ky + 20)], fill=GOLD, width=3)
    d.line([((W + kw) / 2 + 30, ky + 20), (W - 90, ky + 20)], fill=GOLD, width=3)

    f_head = font(60, 800)
    centered(d, 318, linea1, f_head, CREAM)

    # Portada con sombra y marco dorado
    size, x, y = 940, (W - 940) // 2, 430
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle([x, y + 24, x + size, y + size + 24], 40, fill=(0, 0, 0, 170))
    shadow = shadow.filter(ImageFilter.GaussianBlur(30))
    canvas.paste(shadow, (0, 0), shadow)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], 36, fill=255)
    canvas.paste(cover.resize((size, size), Image.LANCZOS), (x, y), mask)
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([x - 8, y - 8, x + size + 8, y + size + 8], 44, outline=GOLD, width=3)

    # Botón YouTube
    f_btn = font(38, 700)
    btn = "Míralo completo en YouTube"
    bw = d.textlength(btn, font=f_btn) + 104 + 48
    bx, by = (W - bw) / 2, y + size + 80
    d.rounded_rectangle([bx, by, bx + bw, by + 92], 46, fill=CREAM)
    d.rounded_rectangle([bx + 24, by + 22, bx + 88, by + 70], 13, fill=RED)
    d.polygon([(bx + 47, by + 33), (bx + 47, by + 59), (bx + 69, by + 46)], fill=CREAM)
    d.text((bx + 104, by + 24), btn, font=f_btn, fill=TEAL_DEEP)

    # Indicación para el sticker de enlace
    centered(d, by + 130, linea2, font(30, 500), GOLD)

    canvas.save(salida)
    print(f"Guardado: {salida}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--portada", default=str(HERE / "portada.png"))
    p.add_argument("--salida", default=str(HERE / "historia-youtube.png"))
    p.add_argument("--linea1", default="Ya disponible en YouTube")
    p.add_argument("--linea2", default="Toca el enlace para verlo ↓")
    a = p.parse_args()
    build(a.portada, a.salida, a.linea1, a.linea2)
