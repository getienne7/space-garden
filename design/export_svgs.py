"""Write each character as a standalone SVG into ../assets/ for index.html.
Usage: python3 design/export_svgs.py   (from the repo root or design/)"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chars import pip, ufo, rocket, fruit2

OUT = os.path.join(HERE, '..', 'assets')


def write(name, inner, box=(-12, -6, 224, 212)):
    x, y, w, h = box
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}">{inner}</svg>\n')
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name + '.svg'), 'w') as fh:
        fh.write(svg)
    return name


ASSETS = [
    write('pip-wave', pip('smile', 'wave')),
    write('pip-hungry', pip('hungry', 'hungry')),
    write('pip-dance', pip('open', 'dance')),
    write('ufo', ufo(False), (-2, 40, 204, 134)),
    write('ufo-pip', ufo(True), (-2, 10, 204, 164)),
]

# Fruit order = the order of the game's FRUITS list (his favourites first)
FRUIT_ORDER = ['Apple', 'Banana', 'Watermelon', 'Avocado', 'Strawberry', 'Cherry', 'Grapes', 'Orange',
               'Lemon', 'Lime', 'Blackberry', 'Blueberry', 'Pineapple', 'Carrot', 'Broccoli', 'Kiwi',
               'Pear', 'Peach', 'Mango', 'Coconut', 'Tomato', 'Corn', 'Peas', 'Eggplant']
# Wide/flat fruits get a tighter frame so they don't look tiny next to round ones
FRAME = {'Watermelon': (5, 12, 190, 190), 'Banana': (30, 24, 160, 160)}
for n in FRUIT_ORDER:
    ASSETS.append(write('fruit-' + n.lower(), fruit2(n, 'f'), FRAME.get(n, (-6, -6, 212, 212))))

if __name__ == '__main__':
    print('\n'.join(f'assets/{a}.svg' for a in ASSETS))
