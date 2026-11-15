from page import page
from chars import *
flat = [s[0] for s in SHAPES] + [s[0] for s in SHAPES2]
NEWS = {s[0] for s in SHAPES2} | set(SOLIDS)
def card(n):
    sub = f'{SIDES[n]} sides' if n in SIDES else ('3D' if n in SOLIDS else '&#160;')
    tag = '<span style="color: #FFC93C"> · new</span>' if n in NEWS else ''
    return f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 4px">
<div style="width: 116px; height: 112px; display: flex; align-items: center; justify-content: center">{svg(shape2(n), 100, 100, label=n, size=100)}</div>
<div style="font-size: 19px; font-weight: 800; color: #FFF6E6; line-height: 1.1; text-align: center">{n}</div>
<div style="font-size: 14px; font-weight: 600; color: #C9C6F2">{sub}{tag}</div>
</div>'''
g2 = ''.join(card(n) for n in flat)
g3 = ''.join(card(n) for n in SOLIDS)
body = f'''<div style="width: 1280px; height: 1000px; box-sizing: border-box; position: relative; overflow: hidden; background: #1E2156; font-family: 'Baloo 2', system-ui, sans-serif">
{stars_bg(1280, 1000, 70, 21)}
<div style="position: relative; display: flex; flex-direction: column; gap: 28px; padding: 52px 64px">
<div style="display: flex; flex-direction: column; gap: 2px">
<div style="font-size: 18px; font-weight: 700; letter-spacing: 3px; color: #FFC93C">SHAPE FRIENDS · 27 FLAT + 5 SOLID</div>
<h1 style="margin: 0; font-size: 56px; font-weight: 800; line-height: 1; color: #FFF6E6">“Yellow hexagon! It has 6 sides.”</h1>
</div>
<div style="display: grid; grid-template-columns: repeat(9, minmax(0, 1fr)); gap: 20px 6px">{g2}</div>
<div style="display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 22px; font-weight: 800; color: #FFF6E6">3D shapes <span style="font-weight: 500; color: #C9C6F2">— a ball is a sphere, a box is a cube</span></div>
<div style="display: grid; grid-template-columns: repeat(9, minmax(0, 1fr)); gap: 20px 6px">{g3}</div>
</div>
</div>
</div>'''
page('Shapes.dc.html', 'Shape friends', 1280, 1000, body)
