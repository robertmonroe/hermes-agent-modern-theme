# Hermes Agent Modern Theme

![Hermes Agent Modern Theme: stacked dashboard screens, each in a different color theme](docs/hermes-agent-modern-theme.webp)

A modern, flat look for the [Hermes Agent](https://hermes-agent.nousresearch.com) web dashboard, in all 26 [Tailwind CSS](https://tailwindcss.com) color palettes.

**[Browse the colors](https://robertmonroe.github.io/hermes-agent-modern-theme/):** every palette and shade, copyable as HEX, RGB, HSL, OKLCH, a Tailwind class or a CSS variable, with a preview of each palette's dashboard theme.

Hermes ships its dashboard with a retro look: pixel display fonts, ALL-CAPS labels, beveled buttons and square boxes. These themes keep everything working the same and change how it looks:

- Geist for all interface text, Geist Mono for code
- Sentence-case labels with normal letter spacing
- Rounded sidebar items with filled hover and active states
- Flat outline buttons, pill-style tab toggles, small rounded badges
- Rounded cards on a slightly lighter surface, hairline borders
- Muted secondary text and a visible focus ring

Only the web dashboard changes. The chat terminal inside it, the CLI and the TUI keep whatever Hermes skin you use.

## The themes

Each palette is its own theme, named `Modern <Palette>`, the same way Hermes ships one theme per look.

**Grays** use the palette's darkest shades for the background, cards and surfaces:
Neutral, Stone, Zinc, Slate, Gray, Mauve, Olive, Mist, Taupe

**Colors** use a near-black background tinted with the color, and the color itself for the active sidebar item, primary buttons, focus rings and text selection:
Red, Orange, Amber, Yellow, Lime, Green, Emerald, Teal, Cyan, Sky, Blue, Indigo, Violet, Purple, Fuchsia, Pink, Rose

## Install

Copy the theme files you want from [`themes/`](themes) into the `dashboard-themes` folder of your Hermes home:

| System | Folder |
|---|---|
| macOS / Linux | `~/.hermes/dashboard-themes/` |
| Windows | `%HERMES_HOME%\dashboard-themes\` (the Windows installer sets `HERMES_HOME`, usually `%LOCALAPPDATA%\hermes`) |

Create the folder if it doesn't exist. Then refresh the dashboard and pick a theme from the theme switcher at the bottom of the sidebar, or set it from a terminal:

```bash
hermes config set dashboard.theme modern-slate
```

With Python 3.9 or newer you can install from a clone instead:

```bash
python make_themes.py --install              # all 26
python make_themes.py --install slate zinc   # just these
```

To remove a theme, delete its file from `dashboard-themes`.

## Customize

| File | What it controls |
|---|---|
| `style.css` | The look shared by every theme: fonts, spacing, shapes, controls |
| `palettes.json` | The colors: every shade of every palette |
| `make_themes.py` | Which shade does which job (background, cards, text, accent), and builds the theme files |
| `tools/import_tailwind.py` | Rebuilds `palettes.json` from a Tailwind CSS v4 `theme.css` |
| `tools/build_page.py` | Rebuilds the colors page in `docs/` from `palettes.json` |

After editing, run `python make_themes.py` to rebuild `themes/` and `python tools/build_page.py` to rebuild the colors page, then `--install` (or copy) the themes you want.

## Compatibility

Built and tested against Hermes Agent v0.23.0. Hermes themes allow raw CSS, and this theme uses it to reach parts of the dashboard that theme colors alone can't change. If a future Hermes release renames those parts, some of the styling may stop applying. The theme still loads, it just looks closer to the default.

## Credits

- Colors: the [Tailwind CSS](https://tailwindcss.com) v4 palette (MIT). Values are converted from Tailwind's OKLCH definitions to hex.
- Fonts: [Geist and Geist Mono](https://vercel.com/font) by Vercel, loaded from Google Fonts.

Not affiliated with or endorsed by Nous Research, Tailwind Labs or Vercel.

## License

MIT. See [LICENSE](LICENSE).
