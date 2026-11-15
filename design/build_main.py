import json, os, datetime
from page import page, ROOT
from chars import *
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
phone = lambda x: {"x": x, "y": 2680, "w": 390, "h": 844}
boards = {
 "Main.dc.html": {"x":0,"y":0,"w":1280,"h":720,"title":"Pip, the hungry alien + rocket"},
 "Planets.dc.html": {"x":1360,"y":0,"w":1280,"h":760,"title":"Planet friends"},
 "Fruits.dc.html": {"x":0,"y":1160,"w":1280,"h":1120,"title":"Fruit & veggie friends (24)"},
 "Shapes.dc.html": {"x":1360,"y":1160,"w":1280,"h":1000,"title":"Shape friends (32)"},
 "Screen-Garden.dc.html": {**phone(0),"title":"Garden on a planet (12 spots)"},
 "Screen-Alien.dc.html": {**phone(470),"title":"Feed Pip"},
 "Screen-Quiz.dc.html": {**phone(940),"title":"Telescope quiz"},
 "Screen-Draw.dc.html": {**phone(1410),"title":"Drawing pad"},
 "Style.dc.html": {"x":1880,"y":2680,"w":1280,"h":844,"title":"Sunny Orbit style"},
}
canvas = {"v":3,"createdOnFiles":{"v":1,"at":now},"title":"Space Garden — Character & Screen Direction","launch":{"view":"canvas"},"pages":[],
 "boards":boards,"order":list(boards),
 "notes":{"t1":{"x":0,"y":-260,"text":"1 · The cast","kind":"title1","maxW":2640},
          "t2":{"x":0,"y":900,"text":"2 · Food & shape friends","kind":"title1","maxW":2640},
          "t3":{"x":0,"y":2420,"text":"3 · Game screens & style","kind":"title1","maxW":3160}},
 "designSystems":[]}
os.makedirs(ROOT+'/project', exist_ok=True)
json.dump(canvas, open(ROOT+'/project/canvas.json','w'), indent=1)

def card(inner, label, sub, size=210):
    return f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; width: {size}px">
<div style="width: {size}px; height: {size}px; display: flex; align-items: center; justify-content: center">{svg(inner, label=label, size=size-20)}</div>
<div style="font-size: 26px; font-weight: 800; color: #FFF6E6; line-height: 1">{label}</div>
<div style="font-size: 16px; font-weight: 500; color: #C9C6F2; text-align: center; line-height: 1.3">{sub}</div>
</div>'''

row = ''.join([
 card(pip('smile','wave'), 'Pip', 'Says hello'),
 card(pip('hungry','hungry'), 'Hungry', '“Can I have a pineapple?”'),
 card(pip('open','dance'), 'Yum yum!', 'Happy dance on a right answer'),
 card(ufo(), 'Pip’s saucer', 'Flies by — tap to land'),
 card(rocket('smile'), 'Rocket', 'Flies you to each planet'),
])
body = f'''<div style="width: 1280px; height: 720px; box-sizing: border-box; position: relative; overflow: hidden; background: #1E2156; font-family: 'Baloo 2', system-ui, sans-serif; color: #FFF6E6">
{stars_bg(1280, 720, 70)}
<div style="position: relative; display: flex; flex-direction: column; gap: 40px; padding: 64px 72px">
<div style="display: flex; flex-direction: column; gap: 4px">
<div style="font-size: 18px; font-weight: 700; letter-spacing: 3px; color: #FFC93C">SPACE GARDEN · MEET THE CAST</div>
<h1 style="margin: 0; font-size: 72px; font-weight: 800; line-height: 1">Hi, I’m Pip!</h1>
<p style="margin: 0; font-size: 22px; font-weight: 500; color: #C9C6F2; max-width: 760px">A round, friendly alien who is always a little bit hungry. Same face as every character: big shiny eyes, rosy cheeks, a small smile.</p>
</div>
<div style="display: flex; justify-content: space-between; align-items: flex-start">{row}</div>
</div>
</div>'''
page('Main.dc.html', 'Meet Pip', 1280, 720, body)
