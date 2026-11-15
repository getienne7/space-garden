from page import page
from ui import *
PAINTS = [('Red','#FF5560'),('Orange','#FF9433'),('Yellow','#FFC93C'),('Green','#44D9B0'),('Blue','#4F8CF5'),('Purple','#A86BF0'),('Pink','#FF7AC8'),('Brown','#8D5A3C'),('Black','#2B2240')]
pal = ''.join(f'<button aria-label="{n}" style="flex: none; width: {58 if n=="Blue" else 46}px; height: {58 if n=="Blue" else 46}px; border-radius: 50%; border: {"5px solid #FFF6E6" if n=="Blue" else "0"}; background: {h}; padding: 0; box-shadow: 0 4px 0 rgba(0,0,0,.25)"></button>' for n,h in PAINTS)
starp = star_path(50, 54, 44)
sten_items = [('none', icon('none', 30)), ('apple', svg(fruit('Apple','s1'), label='Apple stencil', size=44)), ('star', f'<svg viewBox="0 0 100 100" width="40" height="40" aria-hidden="true"><path d="{starp}" fill="#FFC93C"></path></svg>'), ('heart', f'<svg viewBox="0 0 100 100" width="40" height="40" aria-hidden="true"><path d="M50 88 C10 60 4 38 18 22 C32 8 48 16 50 30 C52 16 68 8 82 22 C96 38 90 60 50 88 Z" fill="#FF5560"></path></svg>'), ('banana', svg(fruit('Banana','s2'), label='Banana stencil', size=44))]
sten = ''.join(f'<button aria-label="{n} stencil" style="flex: none; width: 60px; height: 60px; border-radius: 20px; border: {"4px solid #FFC93C" if n=="star" else "0"}; background: #FFF6E6; display: flex; align-items: center; justify-content: center; padding: 0">{c}</button>' for n,c in sten_items)
paper = f'''<svg viewBox="0 0 100 100" width="270" height="270" role="img" aria-label="Star tracing with a blue scribble" style="display:block">
<path d="{starp}" fill="none" stroke="#D9CFE8" stroke-width="2.4" stroke-dasharray="4 4" stroke-linejoin="round"></path>
<path d="M50 10 L60 36 L94 38 L66 58 L76 92 L50 72 L26 90 L34 58 L8 40 L40 36" fill="none" stroke="#4F8CF5" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>'''
gal = ''.join(f'<div style="flex: none; width: 64px; height: 64px; border-radius: 16px; background: #FFF6E6; display: flex; align-items: center; justify-content: center">{c}</div>' for c in [
 svg(fruit('Apple','g1'), label='Saved drawing', size=46), f'<svg viewBox="0 0 100 100" width="44" height="44" aria-hidden="true"><path d="M20 70 Q40 20 60 50 T90 30" fill="none" stroke="#FF7AC8" stroke-width="8" stroke-linecap="round"></path></svg>', f'<svg viewBox="0 0 100 100" width="44" height="44" aria-hidden="true"><circle cx="50" cy="50" r="30" fill="none" stroke="#44D9B0" stroke-width="8"></circle></svg>'])
body = phone(f'''
{topbar(rbtn('back','Back to the garden'), rbtn('starsave','Save my drawing', bg='#FFC93C') + rbtn('sponge','Clear the page'))}
<div style="position: absolute; left: 16px; right: 16px; top: 100px; display: flex; gap: 10px; justify-content: center">{sten}</div>
<div style="position: absolute; left: 20px; right: 20px; top: 178px; height: 370px; border-radius: 34px; background: #FFFDF8; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px">
<div style="font-size: 22px; font-weight: 800; color: #2B2240">Let’s draw a star!</div>
{paper}
</div>
<div style="position: absolute; left: 12px; right: 12px; top: 566px; display: flex; flex-wrap: wrap; gap: 10px 14px; justify-content: center; align-items: center">{pal}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; padding: 16px 20px 28px; background: #2B2F73; border-radius: 32px 32px 0 0; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 17px; font-weight: 700; color: #C9C6F2">My drawings</div>
<div style="display: flex; gap: 12px">{gal}</div>
</div>
''', seed=27)
page('Screen-Draw.dc.html', 'Drawing pad', 390, 844, body)
