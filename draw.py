#!/usr/bin/env python3
"""Draw entry.png for the make.fun news-image bounty, Monday 23 November 2026.

Cream-paper broadsheet: masthead, lead story, schematic world map, UTC timeline,
40 sourced stories in five columns, and an explicit date-check box.
Deterministic: fixed data, fixed fonts, no timestamps, no randomness.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from stories import STORIES, LEAD, TIMELINE, MAP_POINTS, DATE_CHECK, CONTINENTS

W, H = 1024, 1024
CREAM = (247, 241, 227)
PAPER_EDGE = (232, 222, 200)
INK = (26, 26, 26)
MUTED = (90, 82, 70)
RED = (139, 26, 26)
BLUE = (31, 78, 121)
RULE = (120, 105, 80)
LAND = (214, 200, 168)
LAND_EDGE = (150, 132, 95)
BOX_BG = (252, 248, 238)

FDIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(f"{FDIR}/{name}", size)

F_SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
F_SANS = lambda s: font("DejaVuSans.ttf", s)
F_SANS_O = lambda s: font("DejaVuSans.ttf", s)

def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width` px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    # subtle paper border
    d.rectangle([6, 6, W - 7, H - 7], outline=PAPER_EDGE, width=2)
    d.rectangle([10, 10, W - 11, H - 11], outline=(210, 196, 168), width=1)

    # ---------- Masthead ----------
    y = 18
    title = "THE WORLD IN ONE DAY"
    tf = F_SERIF_B(42)
    d.text(((W - d.textlength(title, font=tf)) / 2, y), title, font=tf, fill=INK)
    y += 56
    d.line([(28, y), (W - 28, y)], fill=RULE, width=2)
    y += 6
    sub = "MONDAY, 23 NOVEMBER 2026   ·   40 STORIES   ·   EVERY STORY DATED 23 NOV 2026   ·   SOURCES NAMED"
    sf = F_SANS_B(12)
    d.text(((W - d.textlength(sub, font=sf)) / 2, y), sub, font=sf, fill=RED)
    y += 20
    d.line([(28, y), (W - 28, y)], fill=RULE, width=1)

    # ---------- Lead story ----------
    ly = y + 8
    d.rectangle([28, ly, W - 28, ly + 82], fill=BOX_BG, outline=RULE, width=1)
    kf = F_SANS_B(10)
    d.text((40, ly + 7), LEAD["kicker"], font=kf, fill=RED)
    hf = F_SERIF_B(20)
    d.text((40, ly + 24), LEAD["headline"], font=hf, fill=INK)
    bf = F_SANS(12)
    for i, line in enumerate(wrap(d, LEAD["summary"], bf, W - 80)):
        d.text((40, ly + 50 + i * 15), line, font=bf, fill=INK)
    sf2 = F_SANS_O(9)
    d.text((W - 40 - d.textlength(LEAD["source"], font=sf2), ly + 7),
           LEAD["source"], font=sf2, fill=MUTED)

    # ---------- Map + timeline row ----------
    my = ly + 92
    mh = 132
    # --- schematic world map (left) ---
    mx0, mw = 28, 468
    d.text((mx0, my), "WHERE IT HAPPENED", font=F_SANS_B(11), fill=INK)
    d.text((mx0 + 150, my), "schematic map — dots mark story places",
           font=F_SANS_O(9), fill=MUTED)
    map_box = (mx0, my + 16, mx0 + mw, my + mh)
    d.rectangle(map_box, fill=(238, 230, 208), outline=RULE, width=1)
    lon0, lon1, lat0, lat1 = -170, 190, -58, 85
    def proj(lon, lat):
        x = map_box[0] + (lon - lon0) / (lon1 - lon0) * (map_box[2] - map_box[0])
        yy = map_box[1] + (lat1 - lat) / (lat1 - lat0) * (map_box[3] - map_box[1])
        return x, yy
    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=LAND_EDGE)
    # graticule hint
    for lon in range(-150, 181, 30):
        x, _ = proj(lon, 0)
        d.line([(x, map_box[1]), (x, map_box[3])], fill=(226, 216, 190), width=1)
    lab_f = F_SANS_B(8)
    # Labels only where they fit; Istanbul and Hodeida keep dots, no labels.
    overrides = {
        "Kyiv": (4, -11), "Brussels": (-52, 2), "Benghazi": (4, -9),
        "Khartoum": (-52, 1), "Riyadh": (4, 1), "Seoul": (4, -9),
        "Jakarta": (4, 1), "Taipei": (-34, -9), "Mexico City": (4, 1),
        "Washington": (4, 1), "Brasilia": (4, 1),
    }
    for lon, lat, label in MAP_POINTS:
        x, yy = proj(lon, lat)
        d.ellipse([x - 3, yy - 3, x + 3, yy + 3], fill=RED, outline=(255, 255, 255), width=1)
        if label in overrides:
            dx, dy = overrides[label]
            d.text((x + dx, yy + dy), label, font=lab_f, fill=INK)

    # --- UTC timeline (right) ---
    tx0, tw = 512, W - 28 - 512
    d.text((tx0, my), "THE DAY IN UTC", font=F_SANS_B(11), fill=INK)
    d.text((tx0 + 118, my), "Monday 23 November 2026",
           font=F_SANS_O(9), fill=MUTED)
    ty = my + 16
    d.rectangle([tx0, ty, tx0 + tw, my + mh], fill=BOX_BG, outline=RULE, width=1)
    tf_t = F_SANS_B(10)
    tf_x = F_SANS(10)
    row_h = (mh - 16) // len(TIMELINE)
    for i, (t, text) in enumerate(TIMELINE):
        ry = ty + i * row_h + 3
        d.text((tx0 + 8, ry), t, font=tf_t, fill=RED)
        lines = wrap(d, text, tf_x, tw - 62)
        assert len(lines) == 1, f"timeline wraps: {text!r}"
        d.text((tx0 + 52, ry), lines[0], font=tf_x, fill=INK)
        if i < len(TIMELINE) - 1:
            d.line([(tx0 + 8, ty + (i + 1) * row_h - 2),
                    (tx0 + tw - 8, ty + (i + 1) * row_h - 2)],
                   fill=(226, 216, 190), width=1)

    # ---------- Stories grid: 5 columns x 8 ----------
    sy = my + mh + 10
    bot = 958
    ncol, gap = 5, 10
    col_w = (W - 56 - gap * (ncol - 1)) // ncol
    head_f, sum_f, src_f = F_SANS_B(11), F_SANS(9), F_SANS(8)
    grp_f = F_SANS_B(10)
    per_col = 8
    for c in range(ncol):
        x0 = 28 + c * (col_w + gap)
        yy = sy
        group = None
        for s in STORIES[c * per_col:(c + 1) * per_col]:
            g, headline, summary, source, conf = s
            if g != group:
                group = g
                d.text((x0, yy), g, font=grp_f, fill=RED)
                d.line([(x0, yy + 13), (x0 + col_w, yy + 13)], fill=RULE, width=1)
                yy += 17
            hl = wrap(d, headline, head_f, col_w)[:2]
            for line in hl:
                d.text((x0, yy), line, font=head_f, fill=INK)
                yy += 14
            sl = wrap(d, summary, sum_f, col_w)[:2]
            assert len(wrap(d, summary, sum_f, col_w)) <= 2, f"summary wraps 3 lines: {summary!r}"
            for line in sl:
                d.text((x0, yy), line, font=sum_f, fill=(52, 48, 42))
                yy += 11
            tag = f"{source} · {conf}"
            d.text((x0, yy), tag, font=src_f, fill=MUTED)
            yy += 11
            yy += 4  # gap between stories
            if yy > bot:
                raise SystemExit(f"OVERFLOW col {c}: y={yy} > {bot}")
        # column divider
        if c < ncol - 1:
            d.line([(x0 + col_w + gap // 2, sy), (x0 + col_w + gap // 2, bot)],
                   fill=(226, 216, 190), width=1)

    # ---------- Date-check box ----------
    dy = bot + 6
    d.rectangle([28, dy, W - 28, dy + 52], fill=(255, 252, 240), outline=RED, width=2)
    dcf = F_SANS(10)
    lines = wrap(d, DATE_CHECK, dcf, W - 72)
    assert len(lines) <= 4, f"date-check too long: {len(lines)} lines"
    ly2 = dy + 6
    for i, line in enumerate(lines):
        d.text((40, ly2 + i * 12), line, font=dcf,
               fill=RED if i == 0 else INK)

    out = Path(__file__).resolve().parent / "entry.png"
    img.save(out, format="PNG", optimize=True)
    print(f"wrote {out} {out.stat().st_size} bytes")

if __name__ == "__main__":
    main()
