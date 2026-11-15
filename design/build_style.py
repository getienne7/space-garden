from page import page
from chars import *
COLS = [('Night','#1E2156','sky'),('Dusk','#2B2F73','panels'),('Cream','#FFF6E6','cards, buttons'),('Ink','#2B2240','eyes, text'),
 ('Sun','#FFC93C','highlight, stars'),('Coral','#FF5560','red, badges'),('Tangerine','#FF9433','orange'),('Mint','#44D9B0','green, Pip'),
 ('Sky','#4FB6F5','blue'),('Grape','#A86BF0','purple'),('Bubblegum','#FF7AC8','pink'),('Cheek','#FF8FA8','every face')]
sw = ''.join(f'''<div style="display: flex; align-items: center; gap: 12px"><div style="flex: none; width: 52px; height: 52px; border-radius: 18px; background: {h}; box-shadow: inset 0 0 0 2px rgba(255,255,255,.12)"></div><div style="display: flex; flex-direction: column"><div style="font-size: 20px; font-weight: 800; line-height: 1.1">{n}</div><div style="font-size: 14px; font-weight: 500; color: #C9C6F2">{h} · {u}</div></div></div>''' for n,h,u in COLS)
facebig = svg('<circle cx="100" cy="100" r="92" fill="#44D9B0"></circle>' + face(100, 96, 130, 'smile'), label='The shared face', size=230)
lab = lambda t, top, left: f'<div style="position: absolute; top: {top}px; left: {left}px; font-size: 16px; font-weight: 700; color: #FFC93C; white-space: nowrap">{t}</div>'
rules = ''.join(f'<li style="margin: 0 0 10px">{r}</li>' for r in [
 'Tap targets 64 px or bigger; nothing smaller than 48 px.',
 'Chunky buttons: rounded 26–36 px corners with a 6 px drop shadow so they look pressable.',
 'No outlines. Two tones per character: a darker base and a lighter top, plus a white shine.',
 'Every character gets the same face. Faces turn happy on a right answer, never sad on a wrong one.',
 'Pictures and voice instead of words. Text is only for grown-ups and for reading aloud.',
 'Calm mode: same characters with fewer stars and slower motion.'])
body = f'''<div style="width: 1280px; height: 844px; box-sizing: border-box; position: relative; overflow: hidden; background: #1E2156; font-family: 'Baloo 2', system-ui, sans-serif; color: #FFF6E6; padding: 56px 64px; display: flex; flex-direction: column; gap: 32px">
<div style="display: flex; flex-direction: column; gap: 2px">
<div style="font-size: 18px; font-weight: 700; letter-spacing: 3px; color: #FFC93C">STYLE · SUNNY ORBIT</div>
<h1 style="margin: 0; font-size: 56px; font-weight: 800; line-height: 1">Bright fruit colors on a soft night sky</h1>
</div>
<div style="display: flex; gap: 56px; align-items: flex-start">
<div style="flex: none; width: 440px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px 20px">{sw}</div>
<div style="flex: none; width: 300px; display: flex; flex-direction: column; gap: 22px">
<div style="position: relative; width: 300px; height: 260px; display: flex; justify-content: center">{facebig}{lab('shiny eyes', 54, -6)}{lab('rosy cheeks', 150, 218)}{lab('small smile', 226, 112)}</div>
<div style="display: flex; flex-direction: column; gap: 4px">
<div style="font-size: 44px; font-weight: 800; line-height: 1">Baloo 2</div>
<div style="font-size: 20px; font-weight: 600; color: #C9C6F2">Round, friendly letters. ExtraBold for titles, SemiBold for labels.</div>
</div>
</div>
<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 12px">
<div style="font-size: 24px; font-weight: 800">Rules for the whole game</div>
<ul style="margin: 0; padding-left: 22px; font-size: 19px; font-weight: 500; line-height: 1.35; color: #E9E6FF">{rules}</ul>
</div>
</div>
</div>'''
page('Style.dc.html', 'Sunny Orbit style', 1280, 844, body)
