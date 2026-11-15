from page import page
from ui import *
from chars import fruit2
sprout = '<path d="M50 70 Q50 52 50 44" stroke="#3DAE5A" stroke-width="6" stroke-linecap="round" fill="none"></path><path d="M50 50 Q36 40 30 46 Q38 56 50 52 Z" fill="#46C46A"></path>'
leaves = '<path d="M50 70 Q50 40 50 26" stroke="#3DAE5A" stroke-width="6" stroke-linecap="round" fill="none"></path><path d="M50 44 Q30 30 22 38 Q32 52 50 48 Z M50 34 Q70 20 78 28 Q68 42 50 38 Z" fill="#46C46A"></path>'
# 12 spots: mix of stages and ripe crops
layout = [['Watermelon','leaves','Cherry','sprout'],
          ['','Avocado','leaves','Lemon'],
          ['Strawberry','sprout','Blueberry','']]
def plot(kind, s, i):
    w = int(80 * s)
    if kind in ('', 'sprout', 'leaves'):
        inner = {'': '', 'sprout': sprout, 'leaves': leaves}[kind]
        plant = f'<svg viewBox="0 0 100 80" width="{int(70*s)}" height="{int(56*s)}" aria-hidden="true" style="display:block;overflow:visible">{inner}</svg>'
        label = {'': 'empty, tap to plant', 'sprout': 'sprout', 'leaves': 'leaves'}[kind]
    else:
        plant = svg(fruit2(kind, f'gp{i}'), label=f'Ripe {kind.lower()}', size=int(62*s)); label = f'{kind} ready to pick'
    return f'''<button aria-label="Garden spot {i+1}: {label}" style="width: {w}px; border: 0; background: transparent; padding: 0; display: flex; flex-direction: column; align-items: center">
<div style="height: {int(62*s)}px; display: flex; align-items: flex-end; justify-content: center">{plant}</div>
<div style="width: {w}px; height: {int(26*s)}px; border-radius: 50%; background: #7A4E36; box-shadow: inset 0 -{int(6*s)}px 0 #5E3A28"></div>
</button>'''
rows = ''
for r, (top, s, pad) in enumerate([(402, .78, 46), (488, .88, 28), (586, 1.0, 12)]):
    rows += f'<div style="position: absolute; left: {pad}px; right: {pad}px; top: {top}px; display: flex; justify-content: space-between; z-index: 2">{"".join(plot(k, s, r*4+j) for j,k in enumerate(layout[r]))}</div>'
body = phone(f'''
<div style="position: absolute; left: 272px; top: 168px">{svg(planet('Mars','gm'), label='Mars in the sky', size=72)}</div>
{topbar(rbtn('pencil','Drawing pad') + rbtn('scope','Telescope game'), rbtn('basket','Basket, 7 fruits', badge='7') + rbtn('gear','Grown-ups (hold)', size=48, bg='rgba(255,246,230,.18)', color='#FFF6E6'))}
<div style="position: absolute; top: 96px; left: 0; right: 0; display: flex; justify-content: center; z-index: 2"><div style="background: #FFF6E6; color: #2B2240; font-size: 26px; font-weight: 800; padding: 4px 22px; border-radius: 22px">Earth</div></div>
<div style="position: absolute; left: -330px; top: 360px; width: 1050px; height: 1050px; border-radius: 50%; background: #3FB85A"></div>
<div style="position: absolute; left: -320px; top: 374px; width: 1030px; height: 1030px; border-radius: 50%; background: #5FD068"></div>
<div style="position: absolute; left: 18px; top: 176px">{svg(rocket('smile', flame=False), label='Rocket, parked', size=120)}</div>
<div style="position: absolute; left: 140px; top: 196px; width: 150px; background: #FFF6E6; color: #2B2240; border-radius: 24px 24px 24px 6px; padding: 8px 14px; font-size: 19px; font-weight: 700; line-height: 1.2">12 spots to grow!</div>
{rows}
{tray(['Apple','Watermelon','Cherry','Avocado','Lemon','Kiwi'], 'Cherry')}
''', seed=4)
page('Screen-Garden.dc.html', 'Garden on Earth', 390, 844, body)
