"""Build the colors page (docs/index.html) from palettes.json and the theme roles.

    python tools/build_page.py

GitHub Pages serves docs/ from the main branch.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import make_themes  # noqa: E402  (shares the role mapping so previews match the real themes)


def main() -> None:
    data = json.loads((ROOT / "palettes.json").read_text(encoding="utf-8"))
    roles = make_themes.palettes()
    payload = {
        "grays": data["grays"],
        "colors": data["colors"],
        "oklch": data["oklch"],
        "themes": {name: {k: r[k] for k in ("bg", "card", "surface", "primary")} for name, r in roles.items()},
    }
    template = (ROOT / "tools" / "page_template.html").read_text(encoding="utf-8")
    html = template.replace("/*__DATA__*/null", json.dumps(payload, separators=(",", ":")))
    out = ROOT / "docs" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    (ROOT / "docs" / ".nojekyll").write_text("", encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
