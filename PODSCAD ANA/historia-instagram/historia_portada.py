"""Historia de Instagram (1080x1920) a partir de la portada de "Obesidad sin rodeos".

Uso:
    python historia_portada.py --portada portada.png --salida historia-youtube.png
"""
import argparse
import io
from pathlib import Path

import cairosvg
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


# (archivo del icono, color de marca, etiqueta). iVoox no tiene icono en simple-icons: insignia con texto.
PLATAFORMAS = [
    ("youtube.svg", (255, 0, 0), "YouTube"),
    ("spotify.svg", (30, 215, 96), "Spotify"),
    ("applepodcasts.svg", (153, 51, 204), "Apple"),
    ("amazonmusic.svg", (37, 209, 218), "Amazon"),
    (None, (244, 90, 0), "iVoox"),
]


def icono(nombre, px):
    svg = (HERE / "iconos" / nombre).read_text().replace("<path ", '<path fill="#ffffff" ')
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=px, output_height=px)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def fila_plataformas(canvas, y):
    d = ImageDraw.Draw(canvas)
    r, paso = 52, 190
    x0 = (W - paso * (len(PLATAFORMAS) - 1)) / 2
    f_lab = font(26, 600)
    for i, (archivo, color, etiqueta) in enumerate(PLATAFORMAS):
        cx = x0 + i * paso
        d.ellipse([cx - r, y, cx + r, y + 2 * r], fill=color, outline=CREAM, width=3)
        if archivo:
            ic = icono(archivo, 54)
            canvas.paste(ic, (int(cx - 27), int(y + r - 27)), ic)
        else:
            f_iv = font(25, 800)
            d.text((cx - d.textlength("iVoox", font=f_iv) / 2, y + r - 17), "iVoox", font=f_iv, fill=(255, 255, 255))
        d.text((cx - d.textlength(etiqueta, font=f_lab) / 2, y + 2 * r + 14), etiqueta, font=f_lab, fill=CREAM)


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

    size_head = 60
    while d.textlength(linea1, font=font(size_head, 800)) > 960:
        size_head -= 2
    centered(d, 318 + (60 - size_head) // 2, linea1, font(size_head, 800), CREAM)

    # Portada con sombra y marco dorado
    size, x, y = 860, (W - 860) // 2, 420
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle([x, y + 24, x + size, y + size + 24], 40, fill=(0, 0, 0, 170))
    shadow = shadow.filter(ImageFilter.GaussianBlur(30))
    canvas.paste(shadow, (0, 0), shadow)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], 36, fill=255)
    canvas.paste(cover.resize((size, size), Image.LANCZOS), (x, y), mask)
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([x - 8, y - 8, x + size + 8, y + size + 8], 44, outline=GOLD, width=3)

    # Plataformas
    ky2 = y + size + 48
    f_k2 = font(28, 700)
    k2 = "D I S P O N I B L E   E N"
    k2w = d.textlength(k2, font=f_k2)
    centered(d, ky2, k2, f_k2, GOLD)
    d.line([(150, ky2 + 17), ((W - k2w) / 2 - 26, ky2 + 17)], fill=GOLD, width=2)
    d.line([((W + k2w) / 2 + 26, ky2 + 17), (W - 150, ky2 + 17)], fill=GOLD, width=2)
    fila_plataformas(canvas, ky2 + 62)
    d = ImageDraw.Draw(canvas)

    # Botón YouTube
    f_btn = font(38, 700)
    btn = "Míralo completo en YouTube"
    bw = d.textlength(btn, font=f_btn) + 104 + 48
    bx, by = (W - bw) / 2, ky2 + 270
    d.rounded_rectangle([bx, by, bx + bw, by + 92], 46, fill=CREAM)
    d.rounded_rectangle([bx + 24, by + 22, bx + 88, by + 70], 13, fill=RED)
    d.polygon([(bx + 47, by + 33), (bx + 47, by + 59), (bx + 69, by + 46)], fill=CREAM)
    d.text((bx + 104, by + 24), btn, font=f_btn, fill=TEAL_DEEP)

    # Indicación para el sticker de enlace
    centered(d, by + 116, linea2, font(30, 500), GOLD)

    canvas.save(salida)
    print(f"Guardado: {salida}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--portada", default=str(HERE / "portada.png"))
    p.add_argument("--salida", default=str(HERE / "historia-youtube.png"))
    p.add_argument("--linea1", default="Ya disponible para ver y escuchar")
    p.add_argument("--linea2", default="Toca el enlace para verlo ↓")
    a = p.parse_args()
    build(a.portada, a.salida, a.linea1, a.linea2)
