"""Build the GitHub Pages site into _site/.

    python3 tools/build_site.py

Pages (all relative links, so the site works under /pikmin-bloom-guide/):
    /                     index.html          written below
    /big-flower-helper/   tools/bloom-planner.html, copied as is
    /handbook/            guide/handbook-skeleton.md via raw/build_handbook_html.py

To add a page: write its HTML or build step in main(), add a card to CARDS.
The .github/workflows/pages.yml workflow runs this on every push to main.
"""
import datetime
import html
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / '_site'
REPO_URL = 'https://github.com/lizzb/pikmin-bloom-guide'

BACK_LINK = ('<p style="margin:0;padding:10px max(16px,env(safe-area-inset-left));'
             'font:500 14px/1.2 system-ui,sans-serif"><a href="../" '
             'style="color:inherit;opacity:.75">&larr; Pikmin Bloom guide</a></p>\n')

# (href, title, description)
CARDS = [
    ('big-flower-helper/', 'Big Flower helper',
     'Pick a flower and colour, enter your petals and nectar, and get a visit-by-visit planting guide.'),
    ('handbook/', 'Handbook (work in progress)',
     'Searchable free-to-play notes. Every claim is tagged confirmed, probable, unconfirmed or possibly outdated.'),
]

INDEX = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-title" content="Pikmin Bloom guide">
<title>Pikmin Bloom guide</title>
<style>
:root { --bg:#f4f6f5; --fg:#17211c; --muted:#5a6a62; --card:#fff; --line:#d6ded9; --accent:#1d7a53; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#111815; --fg:#e8efeb; --muted:#9bada2; --card:#1a2420; --line:#2c3a34; --accent:#5cc79a; }
}
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg);
  font:400 17px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif; }
main { max-width:640px; margin:0 auto;
  padding:max(28px,env(safe-area-inset-top)) max(16px,env(safe-area-inset-right)) 40px max(16px,env(safe-area-inset-left)); }
.eyebrow { margin:0 0 4px; font-size:13px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--accent); }
h1 { margin:0 0 8px; font-size:32px; line-height:1.15; }
.lede { margin:0 0 24px; color:var(--muted); }
.cards { display:grid; gap:12px; padding:0; margin:0; list-style:none; }
.card { display:block; padding:16px 18px; background:var(--card); border:1px solid var(--line);
  border-radius:14px; color:inherit; text-decoration:none; }
.card:active, .card:hover { border-color:var(--accent); }
.card h2 { margin:0 0 4px; font-size:19px; }
.card p { margin:0; font-size:15px; color:var(--muted); }
footer { margin-top:28px; font-size:13px; color:var(--muted); }
footer a { color:inherit; }
</style>
</head>
<body>
<main>
<p class="eyebrow">Free to play</p>
<h1>Pikmin Bloom guide</h1>
<p class="lede">Personal notes and tools for playing Pikmin Bloom without spending money. Unofficial: not affiliated with Niantic or Nintendo.</p>
<ul class="cards">
%(cards)s</ul>
<footer>Updated %(date)s &middot; <a href="%(repo)s">Source on GitHub</a></footer>
</main>
</body>
</html>
"""


def as_document(fragment, back_link=True):
    """Wrap a head-and-body fragment (no doctype) in a full document.

    Everything up to the first </style> is the head; the rest is the body.
    """
    if fragment.lstrip().lower().startswith('<!doctype'):
        return fragment
    head, sep, body = fragment.partition('</style>')
    if not sep:
        sys.exit('no </style> found; cannot split head from body')
    meta = ''
    if 'charset' not in head:
        meta += '<meta charset="utf-8">\n'
    if 'name="viewport"' not in head:
        meta += '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    return ('<!doctype html>\n<html lang="en">\n<head>\n' + meta + head + sep + '\n</head>\n<body>\n'
            + (BACK_LINK if back_link else '') + body + '\n</body>\n</html>\n')


def write(rel, text):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
    print(f'wrote {rel} ({len(text.encode()):,} bytes)')


def main():
    OUT.mkdir(exist_ok=True)

    cards = ''.join(
        f'<li><a class="card" href="{html.escape(href)}"><h2>{html.escape(title)}</h2>'
        f'<p>{html.escape(desc)}</p></a></li>\n'
        for href, title, desc in CARDS)
    write('index.html', INDEX % {'cards': cards, 'repo': REPO_URL,
                                  'date': datetime.date.today().isoformat()})

    write('big-flower-helper/index.html',
          as_document((ROOT / 'tools/bloom-planner.html').read_text(encoding='utf-8')))

    handbook = OUT / '.handbook-fragment.html'
    subprocess.run([sys.executable, str(ROOT / 'raw/build_handbook_html.py'),
                    str(ROOT / 'guide/handbook-skeleton.md'), str(handbook)], check=True)
    write('handbook/index.html', as_document(handbook.read_text(encoding='utf-8')))
    handbook.unlink()

    write('.nojekyll', '')


if __name__ == '__main__':
    main()
