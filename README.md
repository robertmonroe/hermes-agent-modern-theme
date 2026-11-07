# Hermes Agent Modern Theme

A modern, flat look for the [Hermes Agent](https://hermes-agent.nousresearch.com) web dashboard, in all 26 Tailwind color palettes shown on [ui.shadcn.com/colors](https://ui.shadcn.com/colors).

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

**Grays** use the palette's dark shades for the background, cards and surfaces, the way shadcn/ui builds its dark mode:
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

After editing, run `python make_themes.py` to rebuild `themes/`, then `--install` (or copy) the ones you want.

## Compatibility

Built and tested against Hermes Agent v0.23.0. Hermes themes allow raw CSS, and this theme uses it to reach parts of the dashboard that theme colors alone can't change. If a future Hermes release renames those parts, some of the styling may stop applying. The theme still loads, it just looks closer to the default.

## Credits

- Colors: the [Tailwind CSS](https://tailwindcss.com) v4 palette (MIT), as presented on [ui.shadcn.com/colors](https://ui.shadcn.com/colors). Values are converted from Tailwind's OKLCH definitions to hex.
- Fonts: [Geist and Geist Mono](https://vercel.com/font) by Vercel, loaded from Google Fonts.
- Visual direction inspired by [shadcn/ui](https://ui.shadcn.com).

Not affiliated with or endorsed by Nous Research, shadcn/ui, Tailwind Labs or Vercel.

## License

MIT. See [LICENSE](LICENSE).
