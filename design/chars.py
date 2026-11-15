"""Space Garden "Sunny Orbit" character library -> inline SVG strings.
Every character shares one face so the cast reads as a family."""
import math

INK = '#2B2240'
CHEEK = '#FF8FA8'
CREAM = '#FFF6E6'


def f(v):
    return f'{v:.1f}'


def face(cx, cy, s, mood='smile', eye=INK):
    """s = face width scale. mood: smile | open | hungry | wow"""
    ex, ey, rx, ry = s * .27, cy, s * .085, s * .11
    out = []
    for sx in (-1, 1):
        x = cx + sx * ex
        out.append(f'<ellipse cx="{f(x)}" cy="{f(ey)}" rx="{f(rx)}" ry="{f(ry)}" fill="{eye}"></ellipse>')
        out.append(f'<circle cx="{f(x - rx * .3)}" cy="{f(ey - ry * .4)}" r="{f(rx * .38)}" fill="#fff"></circle>')
        out.append(f'<circle cx="{f(x + rx * .35)}" cy="{f(ey + ry * .35)}" r="{f(rx * .16)}" fill="#fff"></circle>')
        out.append(f'<ellipse cx="{f(cx + sx * s * .43)}" cy="{f(cy + s * .17)}" rx="{f(s * .085)}" ry="{f(s * .06)}" fill="{CHEEK}" opacity=".6"></ellipse>')
    my = cy + s * .14
    w = s * .13
    if mood == 'smile':
        out.append(f'<path d="M{f(cx - w)} {f(my)} Q{f(cx)} {f(my + s * .16)} {f(cx + w)} {f(my)}" fill="none" stroke="{eye}" stroke-width="{f(s * .045)}" stroke-linecap="round"></path>')
    elif mood in ('open', 'hungry'):
        h = s * (.2 if mood == 'open' else .24)
        out.append(f'<path d="M{f(cx - w * 1.1)} {f(my)} Q{f(cx)} {f(my + h * 1.5)} {f(cx + w * 1.1)} {f(my)} Z" fill="#7A2E4A"></path>')
        out.append(f'<ellipse cx="{f(cx)}" cy="{f(my + h * .55)}" rx="{f(w * .55)}" ry="{f(h * .25)}" fill="#FF7A8F"></ellipse>')
    elif mood == 'wow':
        out.append(f'<ellipse cx="{f(cx)}" cy="{f(my + s * .05)}" rx="{f(s * .06)}" ry="{f(s * .08)}" fill="#7A2E4A"></ellipse>')
    return ''.join(out)


def svg(inner, w=200, h=200, label='', size=None, style=''):
    sz = f' width="{size}" height="{size}"' if size else ''
    return (f'<svg viewBox="0 0 {w} {h}"{sz} role="img" aria-label="{label}" '
            f'style="display:block;overflow:visible;{style}">{inner}</svg>')


def ball(uid, cx, cy, r, main, dark, hi=True, extra=''):
    """Shaded round body: dark base, main color offset up-left, highlight. `extra` drawn clipped."""
    cid = f'c-{uid}'
    o = [f'<defs><clipPath id="{cid}"><circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}"></circle></clipPath></defs>',
         f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{dark}"></circle>',
         f'<g clip-path="url(#{cid})"><circle cx="{f(cx - r * .1)}" cy="{f(cy - r * .12)}" r="{f(r * .97)}" fill="{main}"></circle>{extra}</g>']
    if hi:
        o.append(f'<ellipse cx="{f(cx - r * .45)}" cy="{f(cy - r * .5)}" rx="{f(r * .2)}" ry="{f(r * .12)}" fill="#fff" opacity=".55" transform="rotate(-35 {f(cx - r * .45)} {f(cy - r * .5)})"></ellipse>')
    return ''.join(o)


# ---------------- Planets ----------------
def planet(name, uid, mood='smile'):
    cx = cy = 100
    if name == 'Sun':
        rays = ''.join(
            f'<path d="M{f(100 + 70 * math.cos(a - .16))} {f(100 + 70 * math.sin(a - .16))} L{f(100 + 96 * math.cos(a))} {f(100 + 96 * math.sin(a))} L{f(100 + 70 * math.cos(a + .16))} {f(100 + 70 * math.sin(a + .16))} Z" fill="#FFB020" stroke="#FFB020" stroke-width="6" stroke-linejoin="round"></path>'
            for a in [i * math.pi / 6 for i in range(12)])
        return rays + ball(uid, 100, 100, 66, '#FFD84A', '#FFB020') + face(100, 98, 92, mood)
    spec = {
        'Mercury': (52, '#C9C3BD', '#8F8780'),
        'Venus': (66, '#F7D488', '#D9A64A'),
        'Earth': (68, '#4FB6F5', '#2A86D1'),
        'Mars': (58, '#FF8457', '#D9542C'),
        'Jupiter': (88, '#F2D2A4', '#D09A62'),
        'Saturn': (70, '#F6DC8E', '#D8B25A'),
        'Uranus': (70, '#93E6EC', '#4FBCC8'),
        'Neptune': (70, '#6E8DF2', '#4562D6'),
    }[name]
    r, main, dark = spec
    extra, back, front = '', '', ''
    if name == 'Mercury':
        extra = ''.join(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="#A79F98"></circle>' for x, y, rr in [(72, 72, 8), (128, 70, 6), (132, 128, 9), (70, 126, 5)])
    if name == 'Venus':
        extra = f'<path d="M30 80 Q100 60 170 82 L170 92 Q100 72 30 92 Z" fill="#FFE9B5" opacity=".8"></path><path d="M30 122 Q100 104 170 124 L170 132 Q100 114 30 132 Z" fill="#E8B861" opacity=".7"></path>'
    if name == 'Earth':
        extra = ('<path d="M46 70 Q62 48 86 58 Q96 74 80 84 Q74 100 56 96 Q40 88 46 70 Z" fill="#5FD068"></path>'
                 '<path d="M118 112 Q140 100 158 118 Q160 140 140 150 Q120 156 112 140 Q106 124 118 112 Z" fill="#5FD068"></path>'
                 '<path d="M120 46 Q136 40 148 50 Q140 58 126 56 Z" fill="#fff" opacity=".85"></path>')
    if name == 'Mars':
        extra = ''.join(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="#E0623A"></circle>' for x, y, rr in [(70, 76, 9), (134, 80, 7), (124, 132, 10), (76, 130, 6)])
    if name == 'Jupiter':
        extra = ''.join(f'<rect x="0" y="{y}" width="200" height="{h}" fill="{c}"></rect>' for y, h, c in [(36, 14, '#D9A46C'), (66, 18, '#C98552'), (122, 16, '#C98552'), (150, 14, '#D9A46C')])
        extra += '<ellipse cx="138" cy="132" rx="16" ry="10" fill="#E2603F"></ellipse>'
    if name == 'Saturn':
        extra = '<rect x="0" y="70" width="200" height="12" fill="#E8C46F"></rect><rect x="0" y="118" width="200" height="10" fill="#E8C46F"></rect>'
        back = '<ellipse cx="100" cy="104" rx="104" ry="26" fill="none" stroke="#C9A3F0" stroke-width="12" transform="rotate(-12 100 104)"></ellipse>'
        front = '<path d="M-2 116 A104 26 0 0 0 202 92" fill="none" stroke="#C9A3F0" stroke-width="12" stroke-linecap="round" transform="rotate(-12 100 104) rotate(12 100 104)" ></path>'
        front = '<path d="M-2.4 125.2 A104 26 0 0 0 202.4 82.8" fill="none" stroke="#B88BEA" stroke-width="12" stroke-linecap="round"></path>'
    if name == 'Uranus':
        back = '<ellipse cx="100" cy="100" rx="16" ry="96" fill="none" stroke="#CFF7F8" stroke-width="6" opacity=".9"></ellipse>'
        front = '<path d="M84 100 A16 96 0 0 0 116 100" fill="none" stroke="#CFF7F8" stroke-width="6" opacity=".9"></path>'
    if name == 'Neptune':
        extra = '<path d="M40 124 Q90 110 150 130" fill="none" stroke="#9DB3FF" stroke-width="8" stroke-linecap="round"></path><ellipse cx="66" cy="76" rx="14" ry="8" fill="#3550C0"></ellipse>'
    fs = r * 1.3
    return back + ball(uid, cx, cy, r, main, dark, extra=extra) + front + face(cx, cy + r * .02, fs, mood)


# ---------------- Fruits & veg ----------------
def fruit(name, uid, mood='smile'):
    if name == 'Apple':
        return ('<path d="M100 54 Q104 34 112 24" fill="none" stroke="#7A4A2A" stroke-width="8" stroke-linecap="round"></path>'
                '<path d="M106 40 Q130 22 150 34 Q134 54 106 46 Z" fill="#46C46A"></path>'
                '<path d="M100 60 C70 40 28 56 32 104 C36 150 70 176 100 162 C130 176 164 150 168 104 C172 56 130 40 100 60 Z" fill="#E23B48"></path>'
                '<path d="M100 66 C74 48 40 62 42 102 C44 140 72 162 98 152 C126 162 152 140 156 104 C160 64 128 50 100 66 Z" fill="#FF5560"></path>'
                '<ellipse cx="62" cy="84" rx="12" ry="7" fill="#fff" opacity=".55" transform="rotate(-40 62 84)"></ellipse>'
                + face(100, 106, 92, mood))
    if name == 'Banana':
        return ('<path d="M40 54 Q30 130 100 156 Q160 172 178 120 Q150 140 110 128 Q62 112 58 54 Z" fill="#F2B51C"></path>'
                '<path d="M46 54 Q40 122 102 146 Q150 160 170 126 Q144 134 110 122 Q68 106 60 54 Z" fill="#FFD43B"></path>'
                '<rect x="40" y="38" width="16" height="20" rx="5" fill="#7A5A2A"></rect>'
                '<circle cx="176" cy="122" r="5" fill="#7A5A2A"></circle>'
                + face(102, 116, 70, mood))
    if name == 'Grapes':
        pts = [(70, 70), (100, 66), (130, 70), (56, 100), (86, 98), (116, 98), (146, 100), (72, 128), (102, 128), (132, 128), (88, 156), (118, 156), (103, 180)]
        g = ''.join(f'<circle cx="{x}" cy="{y}" r="20" fill="#8A4FD8"></circle><circle cx="{x - 3}" cy="{y - 3}" r="17" fill="#A86BF0"></circle><circle cx="{x - 8}" cy="{y - 8}" r="4" fill="#fff" opacity=".5"></circle>' for x, y in pts)
        return ('<path d="M100 48 Q104 30 114 22" fill="none" stroke="#7A4A2A" stroke-width="7" stroke-linecap="round"></path>'
                '<path d="M104 40 Q126 26 146 38 Q128 54 104 46 Z" fill="#46C46A"></path>' + g
                + '<ellipse cx="101" cy="112" rx="40" ry="32" fill="#A86BF0"></ellipse>' + face(101, 108, 70, mood))
    if name == 'Orange':
        dots = ''.join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#E8781E" opacity=".7"></circle>' for x, y in [(60, 120), (140, 126), (130, 70), (70, 74), (100, 150), (150, 96)])
        return (ball(uid, 100, 108, 68, '#FFA23A', '#F07E1A', extra=dots)
                + '<path d="M100 42 Q118 22 142 30 Q126 50 100 46 Z" fill="#46C46A"></path><circle cx="100" cy="42" r="5" fill="#7A4A2A"></circle>'
                + face(100, 106, 90, mood))
    if name == 'Broccoli':
        fl = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"></circle>' for x, y, r, c in [
            (62, 74, 30, '#2E9E4F'), (100, 56, 34, '#2E9E4F'), (140, 74, 30, '#2E9E4F'), (80, 92, 30, '#2E9E4F'), (122, 92, 30, '#2E9E4F'),
            (60, 70, 24, '#3DBE5E'), (98, 52, 28, '#3DBE5E'), (138, 70, 24, '#3DBE5E'), (82, 88, 22, '#3DBE5E'), (120, 88, 22, '#3DBE5E')])
        return ('<path d="M74 100 L126 100 L120 178 Q100 188 80 178 Z" fill="#A6DB7A"></path>'
                '<path d="M80 100 L120 100 L116 172 Q100 180 84 172 Z" fill="#BDE894"></path>' + fl
                + face(100, 136, 56, mood))
    if name == 'Carrot':
        return ('<path d="M100 46 Q82 20 74 30 Q80 44 96 52 Z" fill="#46C46A"></path><path d="M100 46 Q106 14 118 18 Q116 38 104 52 Z" fill="#3DAE5A"></path><path d="M100 48 Q128 24 138 34 Q126 48 106 56 Z" fill="#46C46A"></path>'
                '<path d="M58 66 Q100 40 142 66 Q132 120 104 184 Q100 190 96 184 Q68 120 58 66 Z" fill="#F07A1E"></path>'
                '<path d="M66 68 Q100 48 134 68 Q124 118 100 172 Q76 118 66 68 Z" fill="#FF9433"></path>'
                '<path d="M76 130 L90 128 M110 150 L122 148 M82 156 L92 155" stroke="#E0661A" stroke-width="5" stroke-linecap="round"></path>'
                + face(100, 90, 64, mood))
    if name == 'Strawberry':
        seeds = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="2.5" ry="4" fill="#FFE27A"></ellipse>' for x, y in [(64, 86), (136, 86), (58, 116), (142, 116), (76, 146), (124, 146), (100, 166), (92, 150), (110, 132), (70, 130), (130, 128)])
        return ('<path d="M100 58 C60 50 30 70 40 112 C48 146 80 176 100 182 C120 176 152 146 160 112 C170 70 140 50 100 58 Z" fill="#E8324A"></path>'
                '<path d="M100 64 C66 58 42 74 50 110 C58 140 84 166 100 172 C116 166 142 140 150 110 C158 74 134 58 100 64 Z" fill="#FF4F63"></path>' + seeds
                + '<path d="M62 60 Q80 70 100 50 Q120 70 138 60 Q130 46 114 44 Q106 30 100 32 Q94 30 86 44 Q70 46 62 60 Z" fill="#46C46A"></path>'
                + face(100, 104, 80, mood))
    if name == 'Pineapple':
        grid = ''.join(f'<path d="M{40 + i * 20} 70 L{i * 20 - 10} 190" stroke="#E0A21E" stroke-width="3" opacity=".7"></path><path d="M{i * 20 - 10} 70 L{40 + i * 20} 190" stroke="#E0A21E" stroke-width="3" opacity=".7"></path>' for i in range(0, 10))
        return ('<path d="M100 64 L78 20 L96 40 L100 8 L106 40 L124 20 Z" fill="#3DAE5A"></path><path d="M100 66 L66 34 L92 50 Z M100 66 L134 34 L108 50 Z" fill="#46C46A"></path>'
                f'<defs><clipPath id="c-{uid}"><ellipse cx="100" cy="124" rx="54" ry="64"></ellipse></clipPath></defs>'
                '<ellipse cx="100" cy="124" rx="54" ry="64" fill="#F2B51C"></ellipse>'
                f'<g clip-path="url(#c-{uid})"><ellipse cx="94" cy="118" rx="52" ry="62" fill="#FFCF3F"></ellipse>{grid}</g>'
                '<ellipse cx="100" cy="126" rx="34" ry="26" fill="#FFCF3F"></ellipse>'
                + face(100, 122, 70, mood))
    raise KeyError(name)


# ---------------- Shapes (same paths as the game, 100x100 box) ----------------
def _pts(arr):
    return 'M' + ' L '.join(f'{x:.1f} {y:.1f}' for x, y in arr) + ' Z'


def _poly(n, rot=-90, r=44):
    return _pts([(50 + r * math.cos(math.radians(rot + 360 * i / n)), 50 + r * math.sin(math.radians(rot + 360 * i / n))) for i in range(n)])


SHAPES = [
    ('Circle', 'M6 50 A44 44 0 1 0 94 50 A44 44 0 1 0 6 50 Z', '#FF5560', (50, 50, 40)),
    ('Oval', 'M4 50 A46 30 0 1 0 96 50 A46 30 0 1 0 4 50 Z', '#FF9433', (50, 50, 36)),
    ('Triangle', _pts([(50, 8), (94, 88), (6, 88)]), '#FFC93C', (50, 64, 30)),
    ('Square', _pts([(12, 12), (88, 12), (88, 88), (12, 88)]), '#44D9B0', (50, 50, 40)),
    ('Rectangle', _pts([(4, 24), (96, 24), (96, 76), (4, 76)]), '#4FB6F5', (50, 50, 36)),
    ('Rhombus', _pts([(50, 4), (86, 50), (50, 96), (14, 50)]), '#A86BF0', (50, 50, 30)),
    ('Trapezoid', _pts([(28, 22), (72, 22), (96, 80), (4, 80)]), '#FF7AC8', (50, 52, 34)),
    ('Parallelogram', _pts([(28, 24), (98, 24), (72, 78), (2, 78)]), '#FF5560', (50, 51, 32)),
    ('Pentagon', _poly(5), '#FF9433', (50, 54, 38)),
    ('Hexagon', _poly(6, 0), '#FFC93C', (50, 50, 40)),
    ('Heptagon', _poly(7), '#44D9B0', (50, 52, 38)),
    ('Octagon', _poly(8, -67.5), '#4FB6F5', (50, 50, 40)),
    ('Star', _pts([(50 + (19 if i % 2 else 46) * math.cos(math.radians(-90 + 36 * i)), 52 + (19 if i % 2 else 46) * math.sin(math.radians(-90 + 36 * i))) for i in range(10)]), '#FFC93C', (50, 54, 26)),
    ('Heart', 'M50 88 C10 60 4 38 18 22 C32 8 48 16 50 30 C52 16 68 8 82 22 C96 38 90 60 50 88 Z', '#FF5560', (50, 44, 34)),
    ('Crescent', 'M58 6 A44 44 0 0 0 58 94 A30 44 0 0 1 58 6 Z', '#FFE27A', (36, 50, 20)),
    ('Cross', _pts([(36, 6), (64, 6), (64, 36), (94, 36), (94, 64), (64, 64), (64, 94), (36, 94), (36, 64), (6, 64), (6, 36), (36, 36)]), '#A86BF0', (50, 50, 26)),
]
SIDES = {'Triangle': 3, 'Square': 4, 'Rectangle': 4, 'Rhombus': 4, 'Trapezoid': 4, 'Parallelogram': 4, 'Pentagon': 5, 'Hexagon': 6, 'Heptagon': 7, 'Octagon': 8}


def shape(name, mood='smile'):
    for n, d, c, (fx, fy, fs) in SHAPES:
        if n == name:
            return (f'<path d="{d}" fill="{c}" stroke="{c}" stroke-width="6" stroke-linejoin="round"></path>'
                    f'<path d="{d}" fill="#fff" opacity=".18" transform="translate(-3 -3)" clip-path="none"></path>'
                    + face(fx, fy, fs, mood))
    raise KeyError(name)


# ---------------- Pip the alien, UFO, rocket ----------------
def pip(mood='smile', pose='stand'):
    arms = {
        'stand': '<path d="M52 128 Q34 136 32 150" fill="none" stroke="#3FCF8E" stroke-width="14" stroke-linecap="round"></path><path d="M148 128 Q166 136 168 150" fill="none" stroke="#3FCF8E" stroke-width="14" stroke-linecap="round"></path>',
        'hungry': '<path d="M54 126 Q60 150 84 150" fill="none" stroke="#3FCF8E" stroke-width="14" stroke-linecap="round"></path><path d="M146 126 Q140 150 116 150" fill="none" stroke="#3FCF8E" stroke-width="14" stroke-linecap="round"></path>',
        'dance': '<path d="M52 120 Q30 98 26 72" fill="none" stroke="#3FCF8E" stroke-width="14" stroke-linecap="round"></path><path d="M148 120 Q170 98 174 72" fill="none" stroke="#3FCF8E" stroke-width="14" stroke-linecap="round"></path>',
        'wave': '<path d="M52 128 Q34 136 32 150" fill="none" stroke="#3FCF8E" stroke-width="14" stroke-linecap="round"></path><path d="M148 120 Q172 104 172 76" fill="none" stroke="#3FCF8E" stroke-width="14" stroke-linecap="round"></path>',
    }[pose]
    feet = '<ellipse cx="80" cy="186" rx="18" ry="9" fill="#2FB377"></ellipse><ellipse cx="120" cy="186" rx="18" ry="9" fill="#2FB377"></ellipse>'
    ant = ('<path d="M78 46 Q70 22 58 16" fill="none" stroke="#3FCF8E" stroke-width="7" stroke-linecap="round"></path><circle cx="56" cy="14" r="10" fill="#FFC93C"></circle>'
           '<path d="M122 46 Q130 22 142 16" fill="none" stroke="#3FCF8E" stroke-width="7" stroke-linecap="round"></path><circle cx="144" cy="14" r="10" fill="#FF7AC8"></circle>')
    body = ('<path d="M100 40 C150 40 162 90 160 130 C158 170 134 184 100 184 C66 184 42 170 40 130 C38 90 50 40 100 40 Z" fill="#2FB377"></path>'
            '<path d="M96 44 C142 44 152 90 150 128 C148 164 126 176 96 176 C66 176 46 164 46 128 C44 90 54 44 96 44 Z" fill="#3FCF8E"></path>'
            '<ellipse cx="100" cy="150" rx="32" ry="24" fill="#A9F0CC"></ellipse>'
            '<ellipse cx="66" cy="68" rx="12" ry="7" fill="#fff" opacity=".5" transform="rotate(-40 66 68)"></ellipse>')
    extra = ''
    if pose == 'dance':
        extra = ''.join(f'<path d="{star_path(x, y, r)}" fill="#FFC93C"></path>' for x, y, r in [(18, 50, 10), (184, 46, 12), (170, 176, 8), (24, 172, 7)])
    return ant + arms + feet + body + face(100, 100, 100, mood) + extra


def star_path(cx, cy, r):
    return _pts([(cx + (r * .45 if i % 2 else r) * math.cos(math.radians(-90 + 36 * i)), cy + (r * .45 if i % 2 else r) * math.sin(math.radians(-90 + 36 * i))) for i in range(10)])


def ufo(with_pip=True):
    peek = ''
    if with_pip:
        peek = ('<circle cx="100" cy="74" r="30" fill="#3FCF8E"></circle>' + face(100, 72, 46, 'smile')
                + '<path d="M86 46 Q80 32 72 28" fill="none" stroke="#3FCF8E" stroke-width="5" stroke-linecap="round"></path><circle cx="71" cy="27" r="6" fill="#FFC93C"></circle>'
                '<path d="M114 46 Q120 32 128 28" fill="none" stroke="#3FCF8E" stroke-width="5" stroke-linecap="round"></path><circle cx="129" cy="27" r="6" fill="#FF7AC8"></circle>')
    lights = ''.join(f'<circle cx="{x}" cy="124" r="7" fill="{c}"></circle>' for x, c in [(46, '#FFC93C'), (74, '#FF7AC8'), (100, '#44D9B0'), (126, '#FFC93C'), (154, '#FF7AC8')])
    return ('<path d="M60 96 A40 40 0 0 1 140 96 Z" fill="#CDEBFF" opacity=".55"></path>' + peek
            + '<path d="M60 96 A40 40 0 0 1 140 96" fill="none" stroke="#fff" stroke-width="4" opacity=".8"></path>'
            '<ellipse cx="100" cy="114" rx="88" ry="26" fill="#8E86D8"></ellipse>'
            '<ellipse cx="100" cy="106" rx="80" ry="18" fill="#B3ACF2"></ellipse>' + lights
            + '<path d="M70 140 L56 168 M130 140 L144 168" stroke="#8E86D8" stroke-width="7" stroke-linecap="round"></path>')


def rocket(mood='smile', flame=True):
    fl = ('<path d="M84 160 Q100 206 116 160 Z" fill="#FFC93C"></path><path d="M92 160 Q100 186 108 160 Z" fill="#FF7A3B"></path>') if flame else ''
    return (fl
            + '<path d="M70 120 L42 156 L72 150 Z" fill="#4FB6F5"></path><path d="M130 120 L158 156 L128 150 Z" fill="#4FB6F5"></path>'
            '<path d="M100 14 C136 40 140 110 130 160 L70 160 C60 110 64 40 100 14 Z" fill="#F2E6D2"></path>'
            '<path d="M100 18 C130 44 134 108 124 156 L76 156 C66 108 70 44 100 18 Z" fill="#FFF6E6"></path>'
            '<path d="M100 14 C114 24 122 36 127 50 L73 50 C78 36 86 24 100 14 Z" fill="#FF5560"></path>'
            '<rect x="70" y="150" width="60" height="12" rx="6" fill="#FF5560"></rect>'
            '<circle cx="100" cy="98" r="26" fill="#4FB6F5"></circle><circle cx="100" cy="98" r="20" fill="#1E2156"></circle>'
            + face(100, 96, 34, mood, eye='#FFF6E6')
            + '<ellipse cx="88" cy="86" rx="6" ry="3.5" fill="#fff" opacity=".6" transform="rotate(-35 88 86)"></ellipse>')


def stars_bg(w, h, n=40, seed=7):
    import random
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h)
        if rnd.random() < .2:
            out.append(f'<path d="{star_path(x, y, rnd.uniform(4, 7))}" fill="#FFE9A8" opacity=".9"></path>')
        else:
            out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(1, 2.4))}" fill="#fff" opacity="{rnd.uniform(.4, .9):.2f}"></circle>')
    return f'<svg viewBox="0 0 {w} {h}" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" aria-hidden="true" style="position:absolute;inset:0;display:block">{"".join(out)}</svg>'


# ---------------- More fruits & veg (round 2) ----------------
LEAF = '#46C46A'
STEM = '#7A4A2A'


def leaf(x, y, dx=26, dy=-10):
    return f'<path d="M{x} {y} Q{x + dx * .5} {y + dy - 12} {x + dx} {y + dy} Q{x + dx * .5} {y + dy + 10} {x} {y} Z" fill="{LEAF}"></path>'


def fruit2(name, uid, mood='smile'):
    if name == 'Avocado':
        return ('<path d="M100 18 C130 18 140 60 154 104 C170 156 140 190 100 190 C60 190 30 156 46 104 C60 60 70 18 100 18 Z" fill="#2F7A3A"></path>'
                '<path d="M100 30 C124 30 132 66 144 106 C158 150 132 178 100 178 C68 178 42 150 56 106 C68 66 76 30 100 30 Z" fill="#CDEB8B"></path>'
                '<circle cx="100" cy="138" r="28" fill="#9A5B32"></circle><circle cx="94" cy="132" r="22" fill="#B36D3E"></circle><circle cx="86" cy="124" r="5" fill="#fff" opacity=".5"></circle>'
                + face(100, 84, 62, mood))
    if name == 'Cherry':
        c = lambda x, y, u: (f'<circle cx="{x}" cy="{y}" r="40" fill="#B5102B"></circle><circle cx="{x - 5}" cy="{y - 5}" r="35" fill="#E8203F"></circle>'
                             f'<ellipse cx="{x - 18}" cy="{y - 18}" rx="9" ry="5" fill="#fff" opacity=".55" transform="rotate(-40 {x - 18} {y - 18})"></ellipse>')
        return ('<path d="M66 116 Q80 60 116 26 M136 120 Q124 70 116 26" fill="none" stroke="#5E8C2A" stroke-width="7" stroke-linecap="round"></path>'
                + leaf(116, 28, 40, -2) + c(64, 140, 'a') + c(138, 142, 'b') + face(64, 140, 50, mood) + face(138, 142, 50, 'smile'))
    if name == 'Watermelon':
        seeds = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="6.5" fill="#2B2240" transform="rotate({r} {x} {y})"></ellipse>' for x, y, r in [(50, 76, -30), (150, 76, 30), (66, 104, -20), (134, 104, 20), (100, 70, 0), (82, 130, -10), (118, 130, 10)])
        return ('<path d="M10 60 A90 90 0 0 0 190 60 Z" fill="#2E9E4F"></path>'
                '<path d="M20 60 A80 80 0 0 0 180 60 Z" fill="#D9F2B8"></path>'
                '<path d="M28 60 A72 72 0 0 0 172 60 Z" fill="#FF5A6E"></path>' + seeds
                + face(100, 96, 64, mood))
    if name == 'Lime':
        return (ball(uid, 100, 106, 66, '#7BD84A', '#4FB52E') + '<circle cx="168" cy="100" r="6" fill="#4FB52E"></circle>'
                + leaf(100, 42, 30, -14) + face(100, 104, 88, mood))
    if name == 'Lemon':
        return ('<path d="M24 104 Q30 84 44 76 C70 36 130 36 156 76 Q170 84 176 104 Q170 124 156 132 C130 172 70 172 44 132 Q30 124 24 104 Z" fill="#F2C81C"></path>'
                '<path d="M32 102 Q38 84 50 78 C74 44 126 44 150 78 Q160 86 164 98 C150 140 60 150 32 102 Z" fill="#FFE04A"></path>'
                '<ellipse cx="70" cy="76" rx="12" ry="6" fill="#fff" opacity=".55" transform="rotate(-30 70 76)"></ellipse>'
                + face(100, 100, 86, mood))
    if name == 'Blackberry':
        pts = [(78, 72), (100, 66), (122, 72), (66, 96), (88, 92), (112, 92), (134, 96), (70, 120), (92, 118), (114, 118), (132, 120), (80, 144), (102, 144), (122, 144), (92, 166), (112, 166)]
        g = ''.join(f'<circle cx="{x}" cy="{y}" r="15" fill="#3A1F5C"></circle><circle cx="{x - 2}" cy="{y - 2}" r="12" fill="#5A3290"></circle><circle cx="{x - 5}" cy="{y - 5}" r="3" fill="#fff" opacity=".5"></circle>' for x, y in pts)
        return ('<path d="M70 58 Q86 40 100 52 Q114 40 130 58 Q116 62 100 60 Q84 62 70 58 Z" fill="' + LEAF + '"></path>' + g
                + '<ellipse cx="101" cy="112" rx="38" ry="30" fill="#5A3290"></ellipse>' + face(101, 108, 66, mood))
    if name == 'Blueberry':
        crown = star_path(100, 56, 18)
        return (ball(uid, 100, 106, 66, '#5A7CF0', '#3A56C8') + f'<path d="{crown}" fill="#2A3E9A"></path><circle cx="100" cy="56" r="6" fill="#1E2C70"></circle>'
                + face(100, 112, 86, mood))
    if name == 'Kiwi':
        seeds = ''.join(f'<ellipse cx="{f(100 + 34 * math.cos(a))}" cy="{f(104 + 34 * math.sin(a))}" rx="2.6" ry="5" fill="#2B2240" transform="rotate({f(math.degrees(a) + 90)} {f(100 + 34 * math.cos(a))} {f(104 + 34 * math.sin(a))})"></ellipse>' for a in [i * math.pi / 8 for i in range(16)])
        return ('<circle cx="100" cy="104" r="76" fill="#8A6236"></circle><circle cx="100" cy="104" r="66" fill="#7CCB3A"></circle><circle cx="96" cy="100" r="60" fill="#94DB52"></circle>'
                + seeds + '<ellipse cx="100" cy="104" rx="24" ry="20" fill="#F2F7D6"></ellipse>' + face(100, 102, 44, mood))
    if name == 'Pear':
        return (f'<path d="M100 38 Q104 22 112 14" fill="none" stroke="{STEM}" stroke-width="7" stroke-linecap="round"></path>' + leaf(106, 26, 30, -6)
                + '<path d="M100 36 C124 36 124 74 140 100 C168 140 150 186 100 186 C50 186 32 140 60 100 C76 74 76 36 100 36 Z" fill="#9BCB3A"></path>'
                '<path d="M98 42 C118 42 118 76 132 100 C156 136 140 174 98 174 C58 174 42 136 66 100 C80 76 78 42 98 42 Z" fill="#C2E25A"></path>'
                '<ellipse cx="78" cy="94" rx="10" ry="6" fill="#fff" opacity=".5" transform="rotate(-50 78 94)"></ellipse>'
                + face(100, 128, 76, mood))
    if name == 'Peach':
        return (ball(uid, 100, 110, 68, '#FFB07A', '#FF8A5C') + '<path d="M100 46 Q84 100 104 176" fill="none" stroke="#F07A50" stroke-width="5" stroke-linecap="round" opacity=".7"></path>'
                + leaf(100, 44, 32, -12) + face(112, 112, 80, mood))
    if name == 'Mango':
        return ('<path d="M40 120 C30 60 90 26 140 44 C180 60 184 120 150 154 C116 188 50 176 40 120 Z" fill="#F07A1E"></path>'
                '<path d="M48 116 C42 66 92 36 136 52 C170 66 174 116 144 144 C114 172 56 162 48 116 Z" fill="#FFB52E"></path>'
                '<path d="M60 70 C80 42 120 40 146 60 C130 54 90 56 60 70 Z" fill="#FF5A4E" opacity=".75"></path>'
                + leaf(132, 44, 34, -14) + face(104, 108, 84, mood))
    if name == 'Coconut':
        dots = ''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#4A2A16"></circle>' for x, y in [(86, 58), (114, 58), (100, 76)])
        return ball(uid, 100, 104, 72, '#9A5B32', '#6E3C1E', extra=dots) + face(100, 116, 90, mood)
    if name == 'Tomato':
        calyx = _pts([(100 + (8 if i % 2 else 30) * math.cos(math.radians(-90 + 36 * i)), 52 + (8 if i % 2 else 22) * math.sin(math.radians(-90 + 36 * i))) for i in range(10)])
        return (ball(uid, 100, 110, 70, '#FF4A4A', '#D9262E') + f'<path d="{calyx}" fill="{LEAF}"></path><rect x="96" y="30" width="8" height="18" rx="4" fill="#3DAE5A"></rect>'
                + face(100, 112, 90, mood))
    if name == 'Corn':
        kern = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="6" fill="#FFE27A"></ellipse>' for y in range(52, 180, 14) for x in range(78, 128, 14) if (x - 100) ** 2 / 30 ** 2 + (y - 116) ** 2 / 68 ** 2 < 1)
        return ('<path d="M100 34 C130 34 134 90 132 130 C130 170 116 190 100 190 C84 190 70 170 68 130 C66 90 70 34 100 34 Z" fill="#F2B51C"></path>' + kern
                + '<path d="M70 196 C40 170 36 120 54 80 C60 130 76 160 100 186 Z" fill="#3DAE5A"></path><path d="M130 196 C160 170 164 120 146 80 C140 130 124 160 100 186 Z" fill="#46C46A"></path>'
                + '<ellipse cx="100" cy="98" rx="26" ry="22" fill="#FFD43B"></ellipse>' + face(100, 96, 48, mood))
    if name == 'Peas':
        peas = ''.join(f'<circle cx="{x}" cy="104" r="22" fill="#5FC93A"></circle><circle cx="{x - 4}" cy="100" r="18" fill="#7BE04E"></circle>' for x in (56, 100, 144))
        return ('<path d="M10 100 Q100 40 190 100 Q100 170 10 100 Z" fill="#3DA84E"></path><path d="M24 100 Q100 66 176 100 Q100 136 24 100 Z" fill="#B6EB8A"></path>'
                + peas + face(56, 102, 30, 'smile') + face(100, 102, 30, mood) + face(144, 102, 30, 'smile')
                + f'<path d="M186 96 Q196 84 192 70" fill="none" stroke="#3DA84E" stroke-width="6" stroke-linecap="round"></path>')
    if name == 'Eggplant':
        return ('<path d="M110 52 C150 60 164 110 150 150 C136 190 76 196 56 160 C40 130 60 104 76 84 C88 68 92 50 110 52 Z" fill="#6A2C8C"></path>'
                '<path d="M108 60 C142 68 154 110 142 144 C130 178 80 184 64 156 C50 132 68 108 82 90 C92 76 94 58 108 60 Z" fill="#8A44B4"></path>'
                '<path d="M84 72 Q96 40 124 50 Q130 70 120 70 Q110 58 100 72 Q92 82 84 72 Z" fill="' + LEAF + '"></path><path d="M112 52 Q118 32 130 24" fill="none" stroke="#3DAE5A" stroke-width="7" stroke-linecap="round"></path>'
                + face(108, 124, 74, mood))
    return fruit(name, uid, mood)


# ---------------- More shapes (round 2) + 3D ----------------
SHAPES2 = [
    ('Semicircle', 'M6 72 A44 44 0 0 1 94 72 Z', '#44D9B0', (50, 54, 32)),
    ('Quarter circle', 'M14 88 L14 14 A74 74 0 0 1 88 88 Z', '#FF9433', (38, 62, 28)),
    ('Right triangle', _pts([(12, 10), (12, 90), (90, 90)]), '#4FB6F5', (34, 68, 24)),
    ('Kite', _pts([(50, 4), (84, 38), (50, 96), (16, 38)]), '#FF7AC8', (50, 40, 30)),
    ('Arrow', _pts([(4, 36), (56, 36), (56, 12), (96, 50), (56, 88), (56, 64), (4, 64)]), '#FFC93C', (40, 50, 24)),
    ('Nonagon', _poly(9), '#A86BF0', (50, 52, 40)),
    ('Decagon', _poly(10), '#FF5560', (50, 50, 40)),
    ('Ring', 'M6 50 A44 44 0 1 0 94 50 A44 44 0 1 0 6 50 Z M32 50 A18 18 0 1 1 68 50 A18 18 0 1 1 32 50 Z', '#FFC93C', (50, 82, 16)),
    ('Teardrop', 'M50 4 C66 30 86 46 86 62 A36 36 0 0 1 14 62 C14 46 34 30 50 4 Z', '#4FB6F5', (50, 64, 34)),
    ('Cloud', 'M24 80 A18 18 0 0 1 20 44 A22 22 0 0 1 60 30 A20 20 0 0 1 90 56 A14 14 0 0 1 80 80 Z', '#E9E6FF', (54, 60, 30)),
    ('Pill', 'M30 26 L70 26 A24 24 0 0 1 70 74 L30 74 A24 24 0 0 1 30 26 Z', '#44D9B0', (50, 50, 34)),
]
SIDES.update({'Right triangle': 3, 'Kite': 4, 'Nonagon': 9, 'Decagon': 10})
SOLIDS = ['Sphere', 'Cube', 'Cylinder', 'Cone', 'Pyramid']


def shape2(name, mood='smile'):
    for n, d, c, (fx, fy, fs) in SHAPES2:
        if n == name:
            return (f'<path d="{d}" fill="{c}" fill-rule="evenodd" stroke="{c}" stroke-width="6" stroke-linejoin="round"></path>' + face(fx, fy, fs, mood))
    if name == 'Sphere':
        return ball('sph', 50, 50, 44, '#FF7AC8', '#E0509E') + face(50, 52, 56, mood)
    if name == 'Cube':
        return ('<path d="M14 34 L34 14 L86 14 L66 34 Z" fill="#7FE6C8"></path><path d="M66 34 L86 14 L86 66 L66 86 Z" fill="#2FB38E"></path>'
                '<rect x="14" y="34" width="52" height="52" fill="#44D9B0"></rect>' + face(40, 60, 40, mood))
    if name == 'Cylinder':
        return ('<path d="M20 22 L20 80 A30 10 0 0 0 80 80 L80 22 Z" fill="#4FB6F5"></path><path d="M62 24 L80 22 L80 80 A30 10 0 0 1 62 89 Z" fill="#2A86D1"></path>'
                '<ellipse cx="50" cy="22" rx="30" ry="10" fill="#9ED8FA"></ellipse>' + face(46, 54, 40, mood))
    if name == 'Cone':
        return ('<path d="M50 6 L86 82 A36 12 0 0 1 14 82 Z" fill="#FF9433"></path><path d="M50 6 L86 82 A36 12 0 0 1 56 94 Z" fill="#E8741A"></path>'
                + face(46, 66, 32, mood))
    if name == 'Pyramid':
        return ('<path d="M50 6 L10 84 L62 94 Z" fill="#FFC93C"></path><path d="M50 6 L62 94 L92 76 Z" fill="#E8A61A"></path>' + face(42, 70, 28, mood))
    return shape(name, mood)
