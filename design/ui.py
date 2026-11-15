from chars import *
from chars import fruit2
ICON = {
 'pencil': '<path d="M5 19l2-6L16 4l4 4-9 9-6 2z M14 6l4 4"></path>',
 'scope': '<path d="M3 14l11-6 2 4-11 6z M16 12l4-2 M9 17l-2 4 M11 16l2 5"></path>',
 'gear': '<circle cx="12" cy="12" r="3.5"></circle><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"></path>',
 'basket': '<path d="M3 10h18l-2 10H5z M7 10l5-6 5 6"></path>',
 'back': '<path d="M15 5l-7 7 7 7"></path>',
 'sound': '<path d="M4 9h4l5-4v14l-5-4H4z M16 9a4 4 0 010 6 M18.5 6.5a7.5 7.5 0 010 11"></path>',
 'starsave': '<path d="M12 3l2.7 5.6 6.1.8-4.4 4.3 1 6.1L12 17l-5.4 2.8 1-6.1L3.2 9.4l6.1-.8z"></path>',
 'sponge': '<rect x="4" y="7" width="16" height="11" rx="3"></rect><path d="M8 11h.01M12 13h.01M16 11h.01"></path>',
 'none': '<circle cx="12" cy="12" r="8"></circle><path d="M6.5 17.5l11-11"></path>',
}
def icon(name, size=30, color='#2B2240'):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="display:block">{ICON[name]}</svg>'
def rbtn(name, label, size=64, bg='#FFF6E6', color='#2B2240', badge=None):
    b = f'<span style="position: absolute; top: -6px; right: -6px; min-width: 30px; height: 30px; border-radius: 15px; background: #FF5560; color: #fff; font-size: 18px; font-weight: 800; display: flex; align-items: center; justify-content: center; line-height: 1">{badge}</span>' if badge else ''
    return f'<button aria-label="{label}" style="position: relative; width: {size}px; height: {size}px; border-radius: 50%; border: 0; background: {bg}; display: flex; align-items: center; justify-content: center; padding: 0; box-shadow: 0 6px 0 rgba(0,0,0,.22); cursor: pointer">{icon(name, int(size*.47), color)}{b}</button>'
def topbar(left, right):
    return f'<div style="position: absolute; top: 20px; left: 16px; right: 16px; display: flex; justify-content: space-between; align-items: center; z-index: 3"><div style="display: flex; gap: 12px">{left}</div><div style="display: flex; gap: 12px">{right}</div></div>'
def tray(items, active=None):
    btns = ''.join(f'<button aria-label="{n}" style="flex: none; width: 76px; height: 76px; border-radius: 26px; border: 0; background: {"#FFC93C" if n==active else "#FFF6E6"}; display: flex; align-items: center; justify-content: center; padding: 0; box-shadow: 0 6px 0 rgba(0,0,0,.22)">{svg(fruit2(n, f"t{i}{n}"), label=n, size=60)}</button>' for i,n in enumerate(items))
    return f'<div style="position: absolute; left: 0; right: 0; bottom: 0; padding: 18px 16px 30px; background: #2B2F73; border-radius: 36px 36px 0 0; display: flex; gap: 12px; overflow: hidden; z-index: 3">{btns}</div>'
def phone(inner, bg='#1E2156', seed=1):
    return f'''<div style="width: 390px; height: 844px; position: relative; overflow: hidden; background: {bg}; font-family: 'Baloo 2', system-ui, sans-serif; color: #FFF6E6">
{stars_bg(390, 844, 45, seed)}
{inner}
</div>'''
FRUITS8 = ['Apple','Banana','Grapes','Orange','Broccoli','Carrot','Strawberry','Pineapple']
