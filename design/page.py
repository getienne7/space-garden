import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))

ROOT = os.environ.get('CANVAS_ROOT', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'))  # local output folder for the artboard files
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""><link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&amp;display=swap" rel="stylesheet">'
BASE_CSS = "body{margin:0}a{color:#FFC93C}a:hover{color:#FFE27A}button{font-family:inherit}"


def page(path, title, w, h, body, props=None, css=''):
    props = dict(props or {})
    props['$preview'] = {'width': w, 'height': h}
    dp = json.dumps(props).replace('&', '&amp;').replace("'", '&#39;')
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT}
<style>{BASE_CSS}{css}</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{dp}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    p = os.path.join(ROOT, 'project', path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(html)
    print(p, len(html))
