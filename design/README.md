# design/ — Sunny Orbit character art

Python (stdlib only) that draws every Space Garden character as inline SVG.
Source of the Claude Design canvas "Space Garden — Character & Screen Direction".

| File | What it holds |
|---|---|
| `chars.py` | The cast: `face()` (shared face), `planet()`, `fruit2()` (24 fruits/veg), `shape2()` (27 flat + 5 3D), `pip()`, `ufo()`, `rocket()`, `stars_bg()` |
| `ui.py` | Phone-screen pieces: icons, round buttons, fruit tray |
| `page.py` | Wraps a board in the canvas's `.dc.html` format |
| `build_*.py` | One script per canvas board |

## Use
```bash
cd design
python3 build_fruits.py        # writes out/project/Fruits.dc.html (or $CANVAS_ROOT/project/...)
```
Each `chars.py` function returns an SVG fragment; wrap it with `svg(fragment, label=...)` to get a standalone `<svg>`.

## Rules (keep the cast consistent)
- Every character uses `face()`. Moods: `smile`, `open` (happy), `hungry`, `wow`. No sad faces.
- Flat, no outlines: dark base + lighter top + white shine (`ball()`).
- Palette: Night #1E2156, Dusk #2B2F73, Cream #FFF6E6, Ink #2B2240, Cheek #FF8FA8, plus fruit colors.
- Clip-path ids come from the `uid` argument: pass a unique one per use on the same page.

## Next (Phase 2)
An `export_svgs.py` that writes `assets/*.svg` for `index.html` to replace the emoji.
