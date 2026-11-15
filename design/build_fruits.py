from page import page
from chars import *
info = [('Apple','Red'),('Banana','Yellow'),('Grapes','Purple'),('Orange','Orange'),('Broccoli','Green'),('Carrot','Orange'),('Strawberry','Red'),('Pineapple','Yellow'),
 ('Avocado','Green'),('Cherry','Red'),('Watermelon','Red'),('Lime','Green'),('Lemon','Yellow'),('Blackberry','Purple'),
 ('Blueberry','Blue'),('Kiwi','Green'),('Pear','Green'),('Peach','Orange'),('Mango','Orange'),('Coconut','Brown'),
 ('Tomato','Red'),('Corn','Yellow'),('Peas','Green'),('Eggplant','Purple')]
NEW = {'Avocado','Cherry','Watermelon','Lime','Lemon','Blackberry'}
HEX = {'Red':'#FF5560','Yellow':'#FFC93C','Purple':'#A86BF0','Orange':'#FF9433','Green':'#44D9B0','Blue':'#4F8CF5','Brown':'#9A5B32'}
def card(n, col, i):
    mood = 'open' if i % 3 == 1 else 'smile'
    tag = '<div style="position: absolute; top: 10px; right: 10px; background: #FF5560; color: #fff; font-size: 13px; font-weight: 800; padding: 1px 10px; border-radius: 10px">ASKED FOR</div>' if n in NEW else ''
    return f'''<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #FFF6E6; border-radius: 32px; padding: 18px 8px 16px">{tag}
<div style="width: 136px; height: 130px; display: flex; align-items: center; justify-content: center">{svg(fruit2(n, f"f{i}", mood), label=n, size=124)}</div>
<div style="font-size: 24px; font-weight: 800; color: #2B2240; line-height: 1">{n}</div>
<div style="display: flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 600; color: #5B5275"><span style="width: 14px; height: 14px; border-radius: 50%; background: {HEX[col]}; display: inline-block"></span>{col}</div>
</div>'''
grid = ''.join(card(n,c,i) for i,(n,c) in enumerate(info))
body = f'''<div style="width: 1280px; height: 1120px; box-sizing: border-box; position: relative; overflow: hidden; background: #2B2F73; font-family: 'Baloo 2', system-ui, sans-serif">
{stars_bg(1280, 1120, 60, 11)}
<div style="position: relative; display: flex; flex-direction: column; gap: 28px; padding: 52px 64px">
<div style="display: flex; flex-direction: column; gap: 2px">
<div style="font-size: 18px; font-weight: 700; letter-spacing: 3px; color: #FFC93C">FRUIT &amp; VEGGIE FRIENDS · 24 TO GROW</div>
<h1 style="margin: 0; font-size: 56px; font-weight: 800; line-height: 1; color: #FFF6E6">Everything he knows from his videos</h1>
</div>
<div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 18px">{grid}</div>
</div>
</div>'''
page('Fruits.dc.html', 'Fruit and veggie friends', 1280, 1120, body)
