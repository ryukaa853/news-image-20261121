#!/usr/bin/env python3
"""Draw the front page of Saturday 21 November 2026 as a 1024x1024 PNG.

Every pixel is drawn with code (Pillow): gradients, polygons, silhouettes.
No photos, no external assets, no network, no randomness, no timestamps,
so every run writes exactly the same bytes.

    python3 draw.py            # writes entry.png beside this file
    python3 main.py            # copies entry.png to /output/entry.png
"""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
HERE = Path(__file__).resolve().parent
OUT = HERE / "entry.png"

PAPER = (248, 244, 233)
INK = (22, 22, 26)
RED = (176, 32, 32)
NAVY = (16, 34, 62)
GREY = (90, 86, 78)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def vgrad(draw, box, top, bottom):
    """Vertical gradient fill of box (x0, y0, x1, y1)."""
    x0, y0, x1, y1 = box
    span = max(1, y1 - y0)
    for y in range(y0, y1):
        t = (y - y0) / span
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line([(x0, y), (x1, y)], fill=c)


def hgrad(draw, box, left, right):
    x0, y0, x1, y1 = box
    span = max(1, x1 - x0)
    for x in range(x0, x1):
        t = (x - x0) / span
        c = tuple(int(left[i] + (right[i] - left[i]) * t) for i in range(3))
        draw.line([(x, y0), (x, y1)], fill=c)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width`."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, width, fill=INK, leading=1.25):
    lines = wrap(draw, text, fnt, width)
    lh = int(fnt.size * leading)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def rule(draw, x0, x1, y, fill=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- illustrations

def ill_hero(draw, box):
    """Night over the Gulf: missile streaks, a naval base, fire glow."""
    x0, y0, x1, y1 = box
    vgrad(draw, box, (12, 20, 48), (120, 52, 30))
    # stars
    for sx, sy, r in [(60, 18, 2), (150, 30, 1), (260, 12, 2), (380, 26, 1),
                      (520, 14, 2), (640, 32, 1), (760, 16, 2), (880, 28, 1),
                      (920, 10, 2), (330, 40, 1), (700, 44, 1)]:
        draw.ellipse([x0 + sx - r, y0 + sy - r, x0 + sx + r, y0 + sy + r],
                     fill=(235, 235, 220))
    # horizon glow (kept inside the box: bottom edge is y1)
    draw.ellipse([x0 + 330, y0 + 78, x0 + 660, y0 + 168], fill=(214, 110, 40))
    draw.ellipse([x0 + 380, y0 + 96, x0 + 610, y0 + 152], fill=(240, 160, 60))
    # sea
    draw.rectangle([x0, y0 + 118, x1, y1], fill=(20, 48, 78))
    for wy in (128, 140, 154):
        for wx in range(0, 976, 46):
            draw.line([(x0 + wx, y0 + wy), (x0 + wx + 22, y0 + wy)],
                      fill=(70, 120, 160), width=2)
    # missile arcs
    draw.line([(x0 + 90, y0 + 108), (x0 + 300, y0 + 30)], fill=(255, 210, 90), width=4)
    draw.line([(x0 + 130, y0 + 112), (x0 + 330, y0 + 44)], fill=(255, 170, 60), width=3)
    draw.line([(x0 + 700, y0 + 110), (x0 + 560, y0 + 26)], fill=(255, 210, 90), width=4)
    for bx, by in [(300, 30), (330, 44), (560, 26)]:
        draw.ellipse([x0 + bx - 6, y0 + by - 6, x0 + bx + 6, y0 + by + 6],
                     fill=(255, 240, 180))
    # base silhouette: hangars, radar dome, mast
    base = y0 + 118
    draw.rectangle([x0 + 40, base - 34, x0 + 150, base], fill=(10, 14, 26))
    draw.rectangle([x0 + 170, base - 22, x0 + 260, base], fill=(10, 14, 26))
    draw.polygon([(x0 + 40, base - 34), (x0 + 95, base - 52), (x0 + 150, base - 34)],
                 fill=(10, 14, 26))
    draw.ellipse([x0 + 285, base - 34, x0 + 325, base], fill=(10, 14, 26))
    draw.line([(x0 + 305, base - 34), (x0 + 305, base - 62)], fill=(10, 14, 26), width=4)
    draw.ellipse([x0 + 300, base - 68, x0 + 310, base - 58], fill=(255, 80, 60))
    # fire at the industrial site, right side
    for fx, fh, col in [(830, 46, (255, 120, 30)), (860, 62, (255, 170, 40)),
                        (895, 40, (255, 110, 30))]:
        draw.polygon([(x0 + fx - 16, base), (x0 + fx, base - fh),
                      (x0 + fx + 16, base)], fill=col)
    draw.rectangle([x0 + 800, base - 18, x0 + 920, base], fill=(12, 12, 20))
    # smoke
    for cx, cy, r in [(845, 62, 14), (860, 44, 18), (880, 26, 15)]:
        draw.ellipse([x0 + cx - r, y0 + cy - r, x0 + cx + r, y0 + cy + r],
                     fill=(120, 118, 112))


def ill_mexico(draw, box):
    """Desert sunset, cacti, mountains, flashing patrol lights."""
    x0, y0, x1, y1 = box
    vgrad(draw, box, (250, 150, 60), (150, 40, 60))
    draw.ellipse([x0 + 330, y0 + 6, x0 + 400, y0 + 76], fill=(255, 220, 130))
    draw.polygon([(x0, y0 + 62), (x0 + 120, y0 + 18), (x0 + 240, y0 + 62),
                  (x0 + 360, y0 + 26), (x0 + 476, y0 + 62), (x0 + 476, y0 + 78),
                  (x0, y0 + 78)], fill=(96, 44, 66))
    draw.rectangle([x0, y0 + 62, x1, y1], fill=(58, 28, 40))
    # cacti
    for cx, cy, s in [(60, 78, 1.0), (410, 78, 0.8)]:
        draw.rectangle([x0 + cx - 4 * s, y0 + cy - 42 * s, x0 + cx + 4 * s, y0 + cy],
                       fill=(30, 70, 40))
        draw.rectangle([x0 + cx - 16 * s, y0 + cy - 30 * s, x0 + cx - 8 * s, y0 + cy - 12 * s],
                       fill=(30, 70, 40))
        draw.rectangle([x0 + cx + 8 * s, y0 + cy - 24 * s, x0 + cx + 16 * s, y0 + cy - 8 * s],
                       fill=(30, 70, 40))
    # patrol car with lights
    draw.rectangle([x0 + 180, y0 + 62, x0 + 300, y0 + 78], fill=(52, 52, 62))
    draw.rectangle([x0 + 205, y0 + 50, x0 + 275, y0 + 62], fill=(52, 52, 62))
    draw.ellipse([x0 + 195, y0 + 74, x0 + 213, y0 + 78], fill=(40, 40, 44))
    draw.ellipse([x0 + 267, y0 + 74, x0 + 285, y0 + 78], fill=(40, 40, 44))
    draw.ellipse([x0 + 228, y0 + 42, x0 + 242, y0 + 50], fill=(255, 60, 60))
    draw.ellipse([x0 + 248, y0 + 42, x0 + 262, y0 + 50], fill=(60, 120, 255))


def ill_cop(draw, box):
    """Climate summit: globe, sun, wind turbines over green hills."""
    x0, y0, x1, y1 = box
    vgrad(draw, box, (140, 200, 235), (220, 240, 245))
    draw.ellipse([x0 + 380, y0 + 8, x0 + 440, y0 + 68], fill=(255, 205, 80))
    # globe
    gx, gy, gr = x0 + 110, y0 + 48, 34
    draw.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(40, 110, 190))
    draw.ellipse([gx - gr + 8, gy - gr + 10, gx - 6, gy - 4], fill=(60, 160, 90))
    draw.ellipse([gx + 2, gy + 6, gx + gr - 6, gy + gr - 8], fill=(60, 160, 90))
    draw.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=(20, 60, 110), width=2)
    # hills
    draw.polygon([(x0, y0 + 66), (x0 + 150, y0 + 44), (x0 + 320, y0 + 66),
                  (x0 + 476, y0 + 50), (x0 + 476, y0 + 78), (x0, y0 + 78)],
                 fill=(70, 150, 80))
    # wind turbines
    for tx in (300, 380, 440):
        draw.line([(x0 + tx, y0 + 66), (x0 + tx, y0 + 30)], fill=(250, 250, 250), width=3)
        for ang in (0, 120, 240):
            import math
            a = math.radians(ang - 90)
            draw.line([(x0 + tx, y0 + 30),
                       (x0 + tx + int(16 * math.cos(a)), y0 + 30 + int(16 * math.sin(a)))],
                      fill=(250, 250, 250), width=3)


def ill_ship(draw, box):
    """Burning cargo ship in a grey Baltic sea."""
    x0, y0, x1, y1 = box
    vgrad(draw, box, (150, 160, 170), (200, 205, 205))
    draw.ellipse([x0 + 380, y0 + 6, x0 + 430, y0 + 56], fill=(235, 230, 200))
    # sea
    draw.rectangle([x0, y0 + 52, x1, y1], fill=(52, 92, 118))
    for wy in (58, 66, 74):
        for wx in range(0, 476, 40):
            draw.line([(x0 + wx, y0 + wy), (x0 + wx + 18, y0 + wy)],
                      fill=(120, 170, 200), width=2)
    # hull
    draw.polygon([(x0 + 60, y0 + 52), (x0 + 420, y0 + 52), (x0 + 395, y0 + 72),
                  (x0 + 85, y0 + 72)], fill=(30, 30, 36))
    draw.rectangle([x0 + 90, y0 + 36, x0 + 160, y0 + 52], fill=(140, 40, 36))
    draw.rectangle([x0 + 170, y0 + 36, x0 + 240, y0 + 52], fill=(40, 90, 130))
    draw.rectangle([x0 + 250, y0 + 36, x0 + 320, y0 + 52], fill=(180, 140, 50))
    draw.rectangle([x0 + 330, y0 + 30, x0 + 360, y0 + 52], fill=(220, 220, 215))
    # flames + smoke
    for fx, fh, col in [(200, 26, (255, 120, 30)), (225, 36, (255, 170, 40)),
                        (250, 24, (255, 110, 30))]:
        draw.polygon([(x0 + fx - 10, y0 + 38), (x0 + fx, y0 + 38 - fh),
                      (x0 + fx + 10, y0 + 38)], fill=col)
    for cx, cy, r in [(215, 8, 9), (230, 0, 11)]:
        draw.ellipse([x0 + cx - r, y0 + cy - r, x0 + cx + r, y0 + cy + r],
                     fill=(90, 90, 92))
    # lifeboat
    draw.polygon([(x0 + 400, y0 + 66), (x0 + 440, y0 + 66), (x0 + 432, y0 + 74),
                  (x0 + 408, y0 + 74)], fill=(255, 140, 40))


def ill_f1(draw, box):
    """Night street circuit: neon track, race car, skyline."""
    x0, y0, x1, y1 = box
    vgrad(draw, box, (14, 14, 34), (60, 30, 80))
    # skyline
    for bx, bw, bh in [(0, 46, 30), (52, 38, 44), (96, 52, 26), (154, 40, 40),
                       (200, 46, 30), (252, 38, 46), (296, 44, 28), (344, 40, 38),
                       (390, 46, 30), (436, 40, 34)]:
        draw.rectangle([x0 + bx, y0 + 62 - bh, x0 + bx + bw, y0 + 62],
                       fill=(24, 24, 48))
        for wy in range(y0 + 66 - bh, y0 + 58, 9):
            for wx in range(x0 + bx + 5, x0 + bx + bw - 4, 10):
                draw.rectangle([wx, wy, wx + 4, wy + 4], fill=(255, 210, 90))
    # track
    draw.rectangle([x0, y0 + 62, x1, y1], fill=(28, 28, 34))
    draw.line([(x0, y0 + 66), (x1, y0 + 66)], fill=(255, 60, 90), width=2)
    draw.line([(x0, y0 + 74), (x1, y0 + 74)], fill=(240, 240, 240), width=2)
    # checkered flag
    for r in range(3):
        for c in range(4):
            col = (20, 20, 20) if (r + c) % 2 == 0 else (245, 245, 245)
            draw.rectangle([x0 + 420 + c * 8, y0 + 10 + r * 8,
                            x0 + 428 + c * 8, y0 + 18 + r * 8], fill=col)
    draw.line([(x0 + 420, y0 + 10), (x0 + 420, y0 + 44)], fill=(200, 200, 200), width=2)
    # race car silhouette
    cx, cy = x0 + 150, y0 + 54
    draw.polygon([(cx - 95, cy + 12), (cx - 75, cy + 0), (cx - 25, cy - 6),
                  (cx + 30, cy - 4), (cx + 85, cy + 4), (cx + 95, cy + 12),
                  (cx + 60, cy + 14), (cx - 60, cy + 14)], fill=(200, 30, 40))
    draw.polygon([(cx - 32, cy - 6), (cx - 12, cy - 16), (cx + 18, cy - 16),
                  (cx + 28, cy - 6)], fill=(20, 20, 26))
    for wx in (-55, 55):
        draw.ellipse([cx + wx - 13, cy + 2, cx + wx + 13, cy + 16], fill=(12, 12, 14))
        draw.ellipse([cx + wx - 5, cy + 5, cx + wx + 5, cy + 13], fill=(120, 120, 125))
    # speed lines
    for sy in (30, 40, 50):
        draw.line([(x0 + 260, y0 + sy), (x0 + 330, y0 + sy)], fill=(255, 220, 90), width=3)


def ill_dengue(draw, box):
    """Mosquito under a shield: science beats dengue."""
    x0, y0, x1, y1 = box
    vgrad(draw, box, (190, 235, 190), (150, 210, 150))
    # leaves (kept inside the box: bottom edge is y1)
    draw.ellipse([x0 + 8, y0 + 96, x0 + 90, y0 + 108], fill=(90, 170, 90))
    draw.ellipse([x0 + 200, y0 + 104, x0 + 268, y0 + 108], fill=(110, 185, 100))
    # mosquito: body, wings, legs, antennae
    mx, my = x0 + 150, y0 + 76
    draw.ellipse([mx - 52, my - 16, mx - 6, my + 8], fill=(255, 255, 255))  # wing
    draw.ellipse([mx - 30, my - 26, mx + 16, my - 2], fill=(240, 240, 240))  # wing
    draw.ellipse([mx - 26, my - 8, mx + 34, my + 10], fill=(40, 40, 46))   # body
    draw.ellipse([mx + 30, my - 6, mx + 44, my + 6], fill=(40, 40, 46))    # head
    draw.line([(mx + 42, my - 4), (mx + 58, my - 16)], fill=(40, 40, 46), width=2)
    draw.line([(mx + 42, my + 2), (mx + 58, my + 12)], fill=(40, 40, 46), width=2)
    for lx in (-16, 0, 16):
        draw.line([(mx + lx, my + 8), (mx + lx - 8, my + 30)], fill=(40, 40, 46), width=2)
        draw.line([(mx + lx, my + 8), (mx + lx + 10, my + 30)], fill=(40, 40, 46), width=2)
    # shield with check
    sx, sy = x0 + 214, y0 + 30
    draw.polygon([(sx, sy), (sx + 52, sy), (sx + 52, sy + 30), (sx + 26, sy + 52),
                  (sx, sy + 30)], fill=(30, 120, 60))
    draw.line([(sx + 12, sy + 26), (sx + 22, sy + 36), (sx + 40, sy + 14)],
              fill=(255, 255, 255), width=5)
    # big "69%"
    draw.text((x0 + 12, y0 + 8), "69%", font=font(SANS_B, 44), fill=(24, 90, 40))


# ---------------------------------------------------------------- page

def story_cell(draw, x, y, w, h, kicker, headline, standfirst, ill):
    draw.text((x, y), kicker, font=font(SANS_B, 13), fill=RED)
    iy = y + 20
    draw.rectangle([x, iy, x + w, iy + 78], outline=(180, 175, 160), width=1)
    ill(draw, (x, iy, x + w, iy + 78))
    hy = iy + 84
    hy = text_block(draw, x, hy, headline, font(SANS_B, 21), w, leading=1.12)
    text_block(draw, x, hy + 4, standfirst, font(SANS, 14), w, fill=(50, 48, 44),
               leading=1.22)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    # frame
    draw.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

    # ---- masthead
    title = "THE WORLD IN ONE DAY"
    tf = font(SERIF_B, 58)
    draw.text(((W - draw.textlength(title, font=tf)) / 2, 16), title,
              font=tf, fill=INK)
    rule(draw, 24, 1000, 92)
    date = "SATURDAY, 21 NOVEMBER 2026"
    df = font(SANS_B, 21)
    draw.text(((W - draw.textlength(date, font=df)) / 2, 98), date,
              font=df, fill=RED)
    sub = "SIX STORIES  •  ONE DAY  •  AROUND THE GLOBE"
    sf = font(SANS, 13)
    draw.text(((W - draw.textlength(sub, font=sf)) / 2, 126), sub,
              font=sf, fill=GREY)
    rule(draw, 24, 1000, 150, width=2)

    # ---- hero
    draw.text((24, 158), "MIDDLE EAST  •  MANAMA, BAHRAIN",
              font=font(SANS_B, 15), fill=RED)
    draw.rectangle([24, 182, 1000, 352], outline=(180, 175, 160), width=1)
    ill_hero(draw, (24, 182, 1000, 352))
    hy = text_block(draw, 24, 362, "IRAN STRIKES AT U.S. BASES IN BAHRAIN",
                    font(SANS_B, 40), 976, leading=1.05)
    text_block(draw, 24, hy + 6,
               "Tehran says its Revolutionary Guards hit two American positions; "
               "Bahrain reports a fire at an industrial site, no injuries, and says "
               "its air defences intercepted other attacks.",
               font(SANS, 16), 976, fill=(50, 48, 44), leading=1.25)
    rule(draw, 24, 1000, 470, width=2)

    # ---- five more stories
    col_w = 476
    story_cell(draw, 24, 484, col_w, 180,
               "MEXICO  •  SINALOA",
               "MEXICO CAPTURES \u2018EL CHAPO ISIDRO\u2019",
               "Troops seize FBI most-wanted cartel boss Fausto Isidro Meza "
               "Flores; at least 11 people die in the violence that follows.",
               ill_mexico)
    story_cell(draw, 524, 484, col_w, 180,
               "CLIMATE  •  ANTALYA, TURKEY",
               "COP31 TALKS RUN PAST DEADLINE",
               "Negotiators work through Saturday into the night as the summit "
               "nears a final deal \u2014 with fossil fuels the sticking point.",
               ill_cop)
    story_cell(draw, 24, 676, col_w, 180,
               "BALTIC SEA  •  GULF OF FINLAND",
               "DRONE STRIKE SETS RUSSIAN SHIP ABLAZE",
               "The sanctioned cargo vessel Sparta II burns after two drones "
               "hit it; its 16 crew evacuate as Finland blames Ukraine.",
               ill_ship)
    story_cell(draw, 524, 676, col_w, 180,
               "SPORT  •  LAS VEGAS",
               "ANTONELLI FASTEST, VERSTAPPEN ON POLE",
               "Kimi Antonelli tops Las Vegas GP qualifying in 1:33.893, but a "
               "five-place grid penalty hands pole to Max Verstappen.",
               ill_f1)

    # ---- bottom story, full width
    rule(draw, 24, 1000, 868, width=2)
    draw.text((316, 882), "HEALTH  •  BELO HORIZONTE, BRAZIL",
              font=font(SANS_B, 13), fill=RED)
    draw.rectangle([24, 882, 300, 990], outline=(180, 175, 160), width=1)
    ill_dengue(draw, (24, 882, 300, 990))
    text_block(draw, 316, 906, "BRED MOSQUITOES CUT DENGUE BY 69%",
               font(SANS_B, 22), 684, leading=1.1)
    text_block(draw, 316, 940,
               "A four-year Brazil trial of 5,700 children finds Wolbachia-carrying "
               "mosquitoes cut dengue and chikungunya infections by about 69%.",
               font(SANS, 15), 684, fill=(50, 48, 44), leading=1.25)

    # ---- footer
    foot = "Sources: Reuters  •  Associated Press  •  CNN  •  FIA  —  All events reported on 21 November 2026"
    ff = font(SANS, 10)
    draw.text(((W - draw.textlength(foot, font=ff)) / 2, 996), foot,
              font=ff, fill=GREY)

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
