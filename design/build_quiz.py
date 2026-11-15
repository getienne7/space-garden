from page import page
from ui import *
prog = ''.join(f'<path d="{star_path(20+i*44, 20, 18)}" fill="{"#FFC93C" if i<1 else "rgba(255,246,230,.2)"}"></path>' for i in range(3))
choices = ''.join(f'''<button aria-label="{n}" style="width: 100%; height: 140px; border: 0; border-radius: 36px; background: #FFF6E6; display: flex; align-items: center; justify-content: center; padding: 0; box-shadow: 0 8px 0 rgba(0,0,0,.25)">{svg(shape(n), 100, 100, label=n, size=110)}</button>''' for n in ['Rhombus','Trapezoid','Parallelogram'])
body = phone(f'''
{topbar(rbtn('back','Back to the garden'), f'<svg viewBox="0 0 128 40" width="128" height="40" role="img" aria-label="1 of 3 stars">{prog}</svg>')}
<div style="position: absolute; left: 24px; right: 24px; top: 112px; display: flex; align-items: center; gap: 14px">
{svg(pip('smile','stand'), label='Pip', size=96)}
<div style="flex: 1; background: #FFF6E6; color: #2B2240; border-radius: 28px 28px 28px 8px; padding: 12px 16px; display: flex; align-items: center; gap: 10px">
<div style="font-size: 26px; font-weight: 800; line-height: 1.1">Find the trapezoid!</div>
<button aria-label="Say it again" style="flex: none; width: 48px; height: 48px; border-radius: 50%; border: 0; background: #FFC93C; display: flex; align-items: center; justify-content: center; padding: 0">{icon('sound', 26)}</button>
</div>
</div>
<div style="position: absolute; left: 28px; right: 28px; top: 270px; display: flex; flex-direction: column; gap: 24px">{choices}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 34px; text-align: center; font-size: 18px; font-weight: 600; color: #C9C6F2">Next time: “Where’s Saturn?” with planet cards</div>
''', seed=15)
page('Screen-Quiz.dc.html', 'Telescope quiz', 390, 844, body)
