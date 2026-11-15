from page import page
from ui import *
dots = ''.join(f'<span style="width: 26px; height: 26px; border-radius: 50%; background: {"#FF5560" if i<2 else "transparent"}; border: 4px solid #FF5560; box-sizing: border-box; display: inline-block"></span>' for i in range(4))
body = phone(f'''
{topbar(rbtn('back','Back to the garden'), rbtn('basket','Basket', badge='5'))}
<div style="position: absolute; right: -10px; top: 104px; transform: rotate(8deg)">{svg(ufo(False), label='Pip’s saucer, landed', size=150)}</div>
<div style="position: absolute; left: 22px; top: 150px; width: 230px; background: #FFF6E6; color: #2B2240; border-radius: 30px 30px 30px 8px; padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 10px; z-index: 2">
<div style="display: flex; align-items: center; gap: 10px">
<div style="font-size: 64px; font-weight: 800; line-height: .9; color: #FF5560">4</div>
{svg(fruit('Strawberry','ab'), label='Strawberries', size=62)}
<button aria-label="Hear Pip again" style="margin-left: auto; width: 48px; height: 48px; border-radius: 50%; border: 0; background: #FFC93C; display: flex; align-items: center; justify-content: center; padding: 0">{icon('sound', 26)}</button>
</div>
<div style="display: flex; gap: 8px">{dots}</div>
</div>
<div style="position: absolute; left: -80px; top: 600px; width: 560px; height: 400px; border-radius: 50%; background: #8E86D8"></div>
<div style="position: absolute; left: 40px; top: 630px; width: 46px; height: 18px; border-radius: 50%; background: #776FC4"></div>
<div style="position: absolute; left: 290px; top: 650px; width: 60px; height: 22px; border-radius: 50%; background: #776FC4"></div>
<div style="position: absolute; left: 60px; top: 330px">{svg(pip('hungry','hungry'), label='Pip, hungry', size=270)}</div>
<div style="position: absolute; left: 268px; top: 560px; display: flex; gap: 2px">{svg(fruit('Strawberry','a1'), label='strawberry 1', size=50)}{svg(fruit('Strawberry','a2'), label='strawberry 2', size=50)}</div>
<div style="position: absolute; left: 236px; top: 516px; width: 140px; text-align: center; font-size: 20px; font-weight: 600; color: #C9C6F2; z-index: 2">“One… two…”</div>
{tray(['Strawberry','Cherry','Watermelon','Avocado','Blackberry'], 'Strawberry')}
''', seed=9)
page('Screen-Alien.dc.html', 'Feed Pip', 390, 844, body)
