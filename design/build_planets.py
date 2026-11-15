from page import page
from chars import *
facts = {'Sun':'Our star — warm and bright','Mercury':'Closest to the Sun','Venus':'The hottest planet','Earth':'Our home!','Mars':'The red planet',
 'Jupiter':'The biggest planet','Saturn':'Beautiful rings','Uranus':'Spins on its side','Neptune':'Cold and windy'}
def card(n, i):
    size = 230 if n in ('Jupiter','Sun') else 200
    return f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 6px">
<div style="width: 220px; height: 200px; display: flex; align-items: center; justify-content: center">{svg(planet(n, f"p{i}"), label=n, size=size if n!='Jupiter' else 210)}</div>
<div style="font-size: 26px; font-weight: 800; color: #FFF6E6; line-height: 1">{n}</div>
<div style="font-size: 16px; font-weight: 500; color: #C9C6F2">{facts[n]}</div>
</div>'''
names = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
grid = ''.join(card(n,i) for i,n in enumerate(names))
body = f'''<div style="width: 1280px; height: 760px; box-sizing: border-box; position: relative; overflow: hidden; background: #1E2156; font-family: 'Baloo 2', system-ui, sans-serif">
{stars_bg(1280, 760, 80, 3)}
<div style="position: relative; display: flex; flex-direction: column; gap: 28px; padding: 56px 64px">
<div style="display: flex; flex-direction: column; gap: 2px">
<div style="font-size: 18px; font-weight: 700; letter-spacing: 3px; color: #FFC93C">PLANET FRIENDS · IN ORDER FROM THE SUN</div>
<h1 style="margin: 0; font-size: 56px; font-weight: 800; line-height: 1; color: #FFF6E6">The Sun and eight planets</h1>
</div>
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 18px 8px">{grid}</div>
</div>
</div>'''
page('Planets.dc.html', 'Planet friends', 1280, 760, body)
