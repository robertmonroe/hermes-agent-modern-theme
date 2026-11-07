"""Regenerate palettes.json from a Tailwind CSS v4 theme.css.

Tailwind defines its palette in OKLCH; Hermes dashboard themes want hex, so this
converts each shade to sRGB hex (clipped to the sRGB gamut).

    python tools/import_tailwind.py path/to/node_modules/tailwindcss/theme.css
"""
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The order ui.shadcn.com/colors lists them in.
GRAYS = ["neutral", "stone", "zinc", "slate", "gray", "mauve", "olive", "mist", "taupe"]
COLORS = ["red", "orange", "amber", "yellow", "lime", "green", "emerald", "teal", "cyan",
          "sky", "blue", "indigo", "violet", "purple", "fuchsia", "pink", "rose"]
SHADES = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]

VAR = re.compile(r"--color-([a-z]+)-(\d+):\s*oklch\(([\d.]+)%?\s+([\d.]+)\s+([\d.]+|none)\)")


def oklch_to_hex(l: float, c: float, h: float) -> str:
    a, b = c * math.cos(math.radians(h)), c * math.sin(math.radians(h))
    l_ = (l + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (l - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (l - 0.0894841775 * a - 1.2914855480 * b) ** 3
    lin = (
        4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
        -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
        -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_,
    )

    def encode(x: float) -> int:
        x = min(max(x, 0.0), 1.0)
        x = 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
        return round(x * 255)

    return "#" + "".join(f"{encode(x):02x}" for x in lin)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    css = Path(sys.argv[1]).read_text(encoding="utf-8")
    found: dict[str, dict[str, str]] = {}
    for name, shade, l, c, h in VAR.findall(css):
        l_val = float(l) / 100 if float(l) > 1 else float(l)
        hue = 0.0 if h == "none" else float(h)  # achromatic grays have no hue
        found.setdefault(name, {})[shade] = oklch_to_hex(l_val, float(c), hue)

    out = {"grays": {}, "colors": {}}
    for group, names in (("grays", GRAYS), ("colors", COLORS)):
        for name in names:
            shades = found.get(name, {})
            missing = [s for s in SHADES if s not in shades]
            if missing:
                raise SystemExit(f"{name}: missing shades {missing} in {sys.argv[1]}")
            out[group][name] = {s: shades[s] for s in SHADES}

    target = ROOT / "palettes.json"
    target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(out['grays'])} grays, {len(out['colors'])} colors)")


if __name__ == "__main__":
    main()
