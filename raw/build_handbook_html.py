#!/usr/bin/env python3
"""Render guide/handbook-skeleton.md as an artifact-ready HTML page.

The output has no doctype/head wrapper (the Artifact tool adds it at publish time).
Every claim keeps its ✅ 🟡 ❓ 🕰️ tag, shown as a small pill, and the page can dim
lines by confidence. Content is converted verbatim from the Markdown, so edit the
Markdown and rebuild rather than editing the HTML.

Usage: python3 raw/build_handbook_html.py guide/handbook-skeleton.md OUT.html
"""
import datetime
import html
import re
import sys

SOURCES = {
    "D": "Discord #faq",
    "H": "Official Help Center / news",
    "W": "Pikipedia wiki",
    "R": "Reddit notes in overview.md",
    "S": "Other web guides (community forum, bnext, nownews)",
    "L": "lizz's own testing",
    "C": "Calculated here",
}
# emoji -> (css class, label, pill text, data-c kind)
CONF = {
    "✅": ("t-ok", "Confirmed", "✓", "ok"),
    "🟡": ("t-prob", "Probable", "~", "prob"),
    "❓": ("t-unk", "Unconfirmed", "?", "check"),
    "🕰": ("t-old", "Possibly outdated", "old", "check"),
}
TAG_RE = re.compile(r"(✅|🟡|❓|🕰️?)([A-Z](?:/[A-Z])*)?(?![A-Za-z])")
LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")
HEAD_RE = re.compile(r"^(#{1,4})\s+(.*)$")


def tag_html(m):
    cls, label, text, _ = CONF[m.group(1)[0]]
    src = m.group(2)
    title = label
    shown = text
    if src:
        names = [SOURCES.get(s, s) for s in src.split("/")]
        title += " · " + " / ".join(names)
        shown += " " + src
    return f'<span class="tag {cls}" title="{html.escape(title)}">{shown}</span>'


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def inline(s):
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    s = re.sub(r"`([^`]+)`", stash, s)
    s = html.escape(s, quote=False)

    def link(m):
        text, url = m.group(1), m.group(2)
        if url.startswith("http"):
            return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
        if url.startswith("#"):
            return f'<a href="{url}">{text}</a>'
        return f"<code>{text}</code>"

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"§(\d+)", r'<a href="#s\1">§\1</a>', s)
    s = TAG_RE.sub(tag_html, s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{html.escape(codes[int(m.group(1))], quote=False)}</code>", s)
    return s


def conf_of(raw):
    kinds = {CONF[m.group(1)[0]][3] for m in TAG_RE.finditer(raw)}
    if "check" in kinds:
        return "check"
    if "prob" in kinds:
        return "prob"
    if "ok" in kinds:
        return "ok"
    return "none"


def line(raw):
    return f'<span class="ln" data-c="{conf_of(raw)}">{inline(raw)}</span>'


def render_list(items):
    parsed = []
    for ln in items:
        m = LIST_RE.match(ln)
        parsed.append((len(m.group(1)), m.group(2)[0].isdigit(), m.group(3)))

    def build(idx, indent):
        tag = "ol" if parsed[idx][1] else "ul"
        out = [f"<{tag}>"]
        while idx < len(parsed) and parsed[idx][0] >= indent:
            _, _, text = parsed[idx]
            idx += 1
            cls = ""
            cm = re.match(r"^\[( |x)\]\s+(.*)$", text)
            if cm:
                cls = ' class="q done"' if cm.group(1) == "x" else ' class="q"'
                text = cm.group(2)
            sub = ""
            if idx < len(parsed) and parsed[idx][0] > indent:
                sub, idx = build(idx, parsed[idx][0])
            out.append(f"<li{cls}>{line(text)}{sub}</li>")
        out.append(f"</{tag}>")
        return "".join(out), idx

    return build(0, parsed[0][0])[0]


def render_table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    head, body = cells[0], [r for r in cells[2:]]
    out = ['<div class="scroll"><table><thead><tr>']
    out += [f"<th>{inline(c)}</th>" for c in head]
    out.append("</tr></thead><tbody>")
    for r in body:
        c = conf_of(" ".join(r))
        out.append(f'<tr data-c="{c}">' + "".join(f"<td>{inline(x)}</td>" for x in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def parse(lines):
    nodes, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip() or ln.strip() == "---":
            i += 1
            continue
        m = HEAD_RE.match(ln)
        if m:
            nodes.append(("h", len(m.group(1)), m.group(2)))
            i += 1
            continue
        if ln.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(lines[i])
                i += 1
            nodes.append(("table", rows))
            continue
        if LIST_RE.match(ln):
            items = []
            while i < len(lines) and LIST_RE.match(lines[i]):
                items.append(lines[i])
                i += 1
            nodes.append(("list", items))
            continue
        buf = [ln.strip()]
        i += 1
        while (
            i < len(lines)
            and lines[i].strip()
            and lines[i].strip() != "---"
            and not HEAD_RE.match(lines[i])
            and not lines[i].lstrip().startswith("|")
            and not LIST_RE.match(lines[i])
        ):
            buf.append(lines[i].strip())
            i += 1
        nodes.append(("p", " ".join(buf)))
    return nodes


def render_nodes(nodes):
    """Returns (sections, toc, open_counts). sections is a list of html strings."""
    sections, toc = [], []
    cur = None  # dict(id, title, body[])
    counts = {"open": 0, "done": 0}

    def flush():
        nonlocal cur
        if not cur:
            return
        body = "".join(cur["body"])
        if cur["id"] == "s0":
            body = f'<div class="callout stack">{body}</div>'
        sections.append(
            f'<section id="{cur["id"]}" class="stack">'
            f'<h2>{cur["head"]}</h2>{body}</section>'
        )
        cur = None

    for n in nodes:
        if n[0] == "h":
            level, text = n[1], n[2]
            if level == 1:
                continue
            if level == 2:
                flush()
                m = re.match(r"^(\d+)\.\s+(.*)$", text)
                if m:
                    sid, num, title = f"s{m.group(1)}", f"§{m.group(1)}", m.group(2)
                    head = f'<span class="secnum">{num}</span> {inline(title)}'
                else:
                    sid, num, title = slug(text), "", text
                    head = inline(title)
                toc.append((sid, num, title))
                cur = {"id": sid, "head": head, "body": []}
            else:
                cur["body"].append(f'<h{level} id="{slug(text)}">{inline(text)}</h{level}>')
        elif n[0] == "p":
            t = n[1]
            if t.startswith("🚧 migrate:"):
                cur["body"].append(
                    '<p class="migrate"><span class="tag t-mig">to migrate</span> '
                    + inline(t.split(":", 1)[1].strip())
                    + "</p>"
                )
            elif re.fullmatch(r"\*\*[^*]+\*\*(\s.*)?", t) and len(re.sub(r"<[^>]+>", "", inline(t))) < 60:
                cur["body"].append(f'<p class="lbl" data-c="{conf_of(t)}">{inline(t)}</p>')
            else:
                cur["body"].append(f'<p data-c="{conf_of(t)}">{inline(t)}</p>')
        elif n[0] == "list":
            for ln in n[1]:
                cm = re.match(r"^\s*[-*]\s+\[( |x)\]", ln)
                if cm:
                    counts["done" if cm.group(1) == "x" else "open"] += 1
            cur["body"].append(render_list(n[1]))
        elif n[0] == "table":
            cur["body"].append(render_table(n[1]))
    flush()
    return sections, toc, counts


CSS = r"""
/* Layout: one reading column (~820px) with tables scrolling inside their own boxes; the audit page's palette and faces. */
:root {
  --bg: oklch(0.978 0.005 250);
  --fg: oklch(0.255 0.028 258);
  --muted: oklch(0.53 0.022 258);
  --card: oklch(1 0 0);
  --line: oklch(0.898 0.01 250);
  --soft: oklch(0.945 0.008 250);
  --accent: oklch(0.52 0.13 227);
  --accent-soft: oklch(0.945 0.03 227);
  --hi: oklch(0.56 0.19 22);
  --hi-soft: oklch(0.95 0.04 22);
  --mid: oklch(0.58 0.13 70);
  --mid-soft: oklch(0.96 0.04 80);
  --lo: oklch(0.55 0.11 155);
  --lo-soft: oklch(0.95 0.04 155);
  --f-display: "Outfit", "Avenir Next", "Segoe UI", system-ui, sans-serif;
  --f-body: "Hind", "Helvetica Neue", Arial, system-ui, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: oklch(0.235 0.018 255); --fg: oklch(0.938 0.01 255); --muted: oklch(0.715 0.018 255);
    --card: oklch(0.288 0.021 256); --line: oklch(0.365 0.022 256); --soft: oklch(0.32 0.02 256);
    --accent: oklch(0.79 0.125 222); --accent-soft: oklch(0.345 0.05 224);
    --hi: oklch(0.72 0.16 22); --hi-soft: oklch(0.34 0.06 22);
    --mid: oklch(0.8 0.12 80); --mid-soft: oklch(0.34 0.05 80);
    --lo: oklch(0.78 0.12 155); --lo-soft: oklch(0.33 0.05 155);
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: oklch(0.235 0.018 255); --fg: oklch(0.938 0.01 255); --muted: oklch(0.715 0.018 255);
  --card: oklch(0.288 0.021 256); --line: oklch(0.365 0.022 256); --soft: oklch(0.32 0.02 256);
  --accent: oklch(0.79 0.125 222); --accent-soft: oklch(0.345 0.05 224);
  --hi: oklch(0.72 0.16 22); --hi-soft: oklch(0.34 0.06 22);
  --mid: oklch(0.8 0.12 80); --mid-soft: oklch(0.34 0.05 80);
  --lo: oklch(0.78 0.12 155); --lo-soft: oklch(0.33 0.05 155);
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font-family: var(--f-body); font-size: 16px; line-height: 1.6;
  padding-block: 0 64px;
}
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--bg); }
.wrap {
  max-width: 860px; margin: 0 auto;
  padding-left: max(16px, env(safe-area-inset-left, 0px));
  padding-right: max(16px, env(safe-area-inset-right, 0px));
}
.top { padding-block: 32px 8px; }
h1, h2, h3, h4 { font-family: var(--f-display); line-height: 1.2; text-wrap: balance; margin: 0; }
h1 { font-size: clamp(30px, 6vw, 42px); font-weight: 700; letter-spacing: -0.01em; }
h2 { font-size: 24px; font-weight: 600; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line); scroll-margin-top: 64px; }
h3 { font-size: 18px; font-weight: 600; margin-top: 12px; scroll-margin-top: 64px; }
h4 { font-size: 16px; font-weight: 600; margin-top: 10px; scroll-margin-top: 64px; }
.secnum { font-family: var(--f-mono); font-size: 0.62em; font-weight: 600; color: var(--accent); background: var(--accent-soft); padding: 2px 8px; border-radius: 6px; margin-right: 8px; vertical-align: 3px; white-space: nowrap; }
p { margin: 0; max-width: 70ch; }
.stack { display: flex; flex-direction: column; gap: 14px; }
.eyebrow { font-family: var(--f-mono); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }
.lede { font-size: 18px; color: var(--muted); }
.meta { display: flex; flex-wrap: wrap; gap: 8px 18px; font-size: 14px; color: var(--muted); }
code { font-family: var(--f-mono); font-size: 0.88em; background: var(--soft); padding: 1px 5px; border-radius: 4px; overflow-wrap: anywhere; }
a { color: var(--accent); }
ul, ol { margin: 0; padding-left: 22px; }
li { margin: 5px 0; }
li > ul, li > ol { margin-top: 4px; }
li::marker { color: var(--muted); }
.callout { background: var(--accent-soft); border-radius: 10px; padding: 16px 18px; margin-top: 4px; }
.callout p, .callout li { max-width: none; }
.figures { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px; }
.fig { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; min-width: 0; }
.fig b { display: block; font-family: var(--f-display); font-size: 26px; font-weight: 600; font-variant-numeric: tabular-nums; }
.fig > span { font-size: 13px; color: var(--muted); line-height: 1.5; display: block; }
.scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; border: 1px solid var(--line); border-radius: 10px; background: var(--card); }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th, td { text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--line); vertical-align: top; font-variant-numeric: tabular-nums; }
th { font-family: var(--f-display); font-weight: 600; font-size: 13px; background: var(--soft); }
tr:last-child td { border-bottom: 0; }
td:first-child { font-weight: 500; }
.tag { display: inline-block; font-family: var(--f-mono); font-size: 11px; font-weight: 600; line-height: 1.55; padding: 0 6px; border-radius: 999px; margin-inline: 2px; vertical-align: 1px; white-space: nowrap; cursor: help; }
.t-ok { background: var(--lo-soft); color: var(--lo); }
.t-prob { background: var(--mid-soft); color: var(--mid); }
.t-unk { background: var(--hi-soft); color: var(--hi); }
.t-old, .t-mig { background: var(--soft); color: var(--muted); }
.t-mig { cursor: default; }
.lbl { font-family: var(--f-display); font-size: 15px; color: var(--muted); margin-top: 6px; }
.lbl strong { font-weight: 600; color: var(--fg); }
.migrate { font-size: 14px; color: var(--muted); }
.legend { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 10px; }
.legend > div { display: flex; flex-direction: column; gap: 4px; font-size: 14px; background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; min-width: 0; }
.legend .tag { align-self: flex-start; font-size: 12px; margin-inline: 0; cursor: default; }
.sources { display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: 14px; color: var(--muted); }
.sources b { font-family: var(--f-mono); color: var(--fg); }
.toc { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 6px 14px; }
.toc a { display: flex; gap: 8px; align-items: baseline; text-decoration: none; padding: 5px 8px; border-radius: 6px; color: var(--fg); font-size: 15px; }
.toc a:hover, .toc a:focus-visible { background: var(--accent-soft); outline: none; }
.toc small { font-family: var(--f-mono); font-size: 12px; color: var(--accent); min-width: 2.2em; }
.stickybar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); border-bottom: 1px solid var(--line); margin-top: 20px; }
.stickybar .wrap { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 12px; padding-block: 8px; }
.stickybar .cap { font-family: var(--f-mono); font-size: 12px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); }
.seg { display: inline-flex; border: 1px solid var(--line); border-radius: 8px; overflow: hidden; background: var(--card); }
.seg button { font: inherit; font-size: 14px; font-family: var(--f-body); color: var(--fg); background: transparent; border: 0; padding: 4px 12px; cursor: pointer; border-right: 1px solid var(--line); }
.seg button:last-child { border-right: 0; }
.seg button[aria-pressed="true"] { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
.seg button:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
li.q > .ln::before { content: ""; display: inline-block; width: 12px; height: 12px; border: 1.5px solid var(--muted); border-radius: 3px; margin-right: 8px; vertical-align: -1px; }
li.q.done > .ln::before { background: var(--lo); border-color: var(--lo); }
li.q { list-style: none; margin-left: -22px; }
.ln, p, tr { transition: opacity 0.15s; }
@media (prefers-reduced-motion: reduce) { .ln, p, tr { transition: none; } }
body[data-focus="ok"] [data-c="prob"], body[data-focus="ok"] [data-c="check"] { opacity: 0.3; }
body[data-focus="check"] [data-c="ok"], body[data-focus="check"] [data-c="prob"], body[data-focus="check"] [data-c="none"] { opacity: 0.3; }
.searchrow { display: flex; flex: 1 1 260px; align-items: center; gap: 6px; min-width: 0; }
.searchbox { position: relative; flex: 1 1 auto; min-width: 0; }
.searchbox input { width: 100%; font: inherit; font-size: 16px; font-family: var(--f-body); color: var(--fg); background: var(--card); border: 1px solid var(--line); border-radius: 8px; padding: 6px 34px 6px 12px; -webkit-appearance: none; appearance: none; }
.searchbox input::-webkit-search-cancel-button { -webkit-appearance: none; display: none; }
.searchbox input:focus-visible { outline: 2px solid var(--accent); outline-offset: -1px; }
.searchbox button { position: absolute; right: 2px; top: 50%; transform: translateY(-50%); font: inherit; font-size: 18px; line-height: 1; width: 30px; height: 30px; border: 0; border-radius: 6px; background: transparent; color: var(--muted); cursor: pointer; }
.searchbox button:focus-visible { outline: 2px solid var(--accent); }
.qcount { font-family: var(--f-mono); font-size: 12px; color: var(--muted); white-space: nowrap; min-width: 5.5em; }
#qnone { padding: 24px 0; color: var(--muted); }
main { scroll-margin-top: 120px; }
::highlight(hb) { background: var(--mid-soft); color: var(--fg); text-decoration: underline; text-decoration-color: var(--mid); }
.small { font-size: 14px; color: var(--muted); }
@media (max-width: 560px) { .stickybar .cap { display: none; } .stickybar .wrap { padding-block: 6px; } }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
"""

JS = r"""
(function () {
  var body = document.body;
  var btns = document.querySelectorAll('.seg button');
  function set(mode) {
    if (mode === 'all') body.removeAttribute('data-focus'); else body.setAttribute('data-focus', mode);
    btns.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.mode === mode)); });
    try { localStorage.setItem('handbook-focus', mode); } catch (e) {}
  }
  btns.forEach(function (b) { b.addEventListener('click', function () { set(b.dataset.mode); }); });
  var saved = 'all';
  try { saved = localStorage.getItem('handbook-focus') || 'all'; } catch (e) {}
  set(saved);
})();

(function () {
  var main = document.querySelector('main');
  var q = document.getElementById('q');
  var count = document.getElementById('qcount');
  var clear = document.getElementById('qclear');
  var none = document.getElementById('qnone');
  var secs = Array.prototype.slice.call(main.querySelectorAll('section'));
  var leaves = Array.prototype.slice.call(main.querySelectorAll('.ln, p:not(#qnone), tbody tr, h3, h4'));
  var text = new Map();
  leaves.forEach(function (el) { text.set(el, el.textContent.toLowerCase()); });
  var canMark = !!(window.CSS && CSS.highlights && window.Highlight);
  var active = false;

  function reset() {
    leaves.forEach(function (el) { el.classList.remove('hit'); });
    main.querySelectorAll('[hidden]').forEach(function (el) { if (el !== none) el.hidden = false; });
    none.hidden = true;
    count.textContent = '';
    if (canMark) CSS.highlights.delete('hb');
    active = false;
  }

  function mark(terms) {
    if (!canMark) return;
    var ranges = [];
    main.querySelectorAll('.hit').forEach(function (el) {
      if (ranges.length > 3000) return;
      var w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      var n;
      while ((n = w.nextNode())) {
        var low = n.data.toLowerCase();
        terms.forEach(function (t) {
          var i = low.indexOf(t);
          while (i > -1) {
            var r = new Range();
            r.setStart(n, i);
            r.setEnd(n, i + t.length);
            ranges.push(r);
            i = low.indexOf(t, i + t.length);
          }
        });
      }
    });
    CSS.highlights.set('hb', new Highlight(...ranges));
  }

  function run() {
    var terms = q.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    clear.hidden = !terms.length;
    if (!terms.length) { reset(); return; }
    var first = !active;
    active = true;
    var hits = 0;
    leaves.forEach(function (el) {
      var t = text.get(el);
      var ok = terms.every(function (w) { return t.indexOf(w) > -1; });
      el.classList.toggle('hit', ok);
      if (ok) hits++;
    });
    main.querySelectorAll('li').forEach(function (li) { li.hidden = !li.querySelector('.ln.hit'); });
    main.querySelectorAll('ul, ol').forEach(function (l) { l.hidden = !l.querySelector('li:not([hidden])'); });
    main.querySelectorAll('tbody tr').forEach(function (r) { r.hidden = !r.classList.contains('hit'); });
    main.querySelectorAll('.scroll').forEach(function (b) { b.hidden = !b.querySelector('tbody tr:not([hidden])'); });
    main.querySelectorAll('section p').forEach(function (p) { p.hidden = !p.classList.contains('hit'); });
    main.querySelectorAll('.callout').forEach(function (c) {
      c.hidden = !Array.prototype.some.call(c.children, function (k) { return !k.hidden; });
    });
    secs.forEach(function (sec) {
      var kids = Array.prototype.slice.call(sec.children).slice(1);
      var pend = [];
      var any = false;
      kids.forEach(function (k) {
        var head = /^H[34]$/.test(k.tagName) || k.classList.contains('lbl');
        if (head) {
          k.hidden = !k.classList.contains('hit');
          if (k.hidden) { if (k.tagName === 'H3') pend = []; pend.push(k); } else { any = true; pend = []; }
        } else if (!k.hidden) {
          any = true;
          pend.forEach(function (h) { h.hidden = false; });
          pend = [];
        }
      });
      sec.hidden = !any;
    });
    none.hidden = hits > 0;
    count.textContent = hits + (hits === 1 ? ' match' : ' matches');
    mark(terms);
    if (first) main.scrollIntoView({ block: 'start' });
  }

  q.addEventListener('input', run);
  q.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') q.blur();
    if (e.key === 'Escape') { q.value = ''; run(); }
  });
  clear.addEventListener('click', function () { q.value = ''; run(); q.focus(); });
})();
"""


def build(src_path):
    text = open(src_path, encoding="utf-8").read()
    body_md = text.split("\n## 0.", 1)[1]
    nodes = parse(("## 0." + body_md).split("\n"))
    sections, toc, counts = render_nodes(nodes)
    today = datetime.date.today().strftime("%-d %b %Y")

    legend = "".join(
        f'<div>{inline(sym)}<span>{html.escape(desc)}</span></div>'
        for sym, desc in [
            ("✅", "Discord FAQ, official Help Center or news, or tested by lizz"),
            ("🟡", "Wiki or recent community notes, not independently verified"),
            ("❓", "Unconfirmed, conflicting, or opinion"),
            ("🕰️", "Possibly outdated (2021 to 2024 sources)"),
        ]
    )
    sources = "".join(f"<span><b>{k}</b> {html.escape(v)}</span>" for k, v in SOURCES.items())
    figures = "".join(
        f"<div class=\"fig\"><b>{big}</b><span>{inline(cap)}</span></div>"
        for big, cap in [
            ("300 → 4,500", "Pikmin storage, default to shop maximum ✅H 🟡H"),
            ("10", "petals for releasing a Pikmin, plain colour ✅L ✅W"),
            ("212", "friendship points to reach 4 hearts 🟡W"),
            ("5 × 5 m", "planting cell, no replanting for 5 minutes ✅W"),
            ("12 h", "postcard trip, whatever the distance ✅D ✅W"),
            ("650", "friend cap across Niantic games ✅D"),
        ]
    )
    toc_html = "".join(
        f'<a href="#{sid}"><small>{num or "·"}</small><span>{html.escape(title)}</span></a>'
        for sid, num, title in toc
    )

    return f"""<title>Pikmin Bloom Handbook</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&family=Hind:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{CSS}</style>

<div class="top"><div class="wrap stack">
  <div class="eyebrow">Free-to-play guide · draft v0 · drafted 1 Nov 2026 · page built {today}</div>
  <h1>Pikmin Bloom Handbook</h1>
  <p class="lede">Storage, seedlings, rare decor, feeding, planting, mushrooms and social features for a player who does not spend real money. Every line carries a tag that shows how far to trust it.</p>
  <div class="meta"><span>Sources: Discord #faq (36 threads), Pikipedia, Help Center, Reddit notes</span><span>{counts["open"]} open questions · {counts["done"]} resolved</span></div>

  <div class="figures">{figures}</div>

  <h3>How to read the tags</h3>
  <div class="legend">{legend}</div>
  <div class="sources" aria-label="Source letters">{sources}</div>
  <p class="small">Tags sit at the end of a line. Trust order when sources disagree: <b>D &gt; H &gt; W &gt; R</b>, and newer beats older. Hover a tag for its source.</p>

  <h3>Sections</h3>
  <nav class="toc" aria-label="Sections">{toc_html}</nav>
</div></div>

<div class="stickybar"><div class="wrap">
  <div class="searchrow" role="search">
    <div class="searchbox">
      <input id="q" type="search" placeholder="Search the handbook" aria-label="Search the handbook" enterkeyhint="search" autocomplete="off" autocapitalize="off" spellcheck="false">
      <button id="qclear" type="button" aria-label="Clear search" hidden>&times;</button>
    </div>
    <span class="qcount" id="qcount" aria-live="polite"></span>
  </div>
  <span class="cap">Highlight</span>
  <div class="seg" role="group" aria-label="Highlight lines by confidence">
    <button type="button" data-mode="all" aria-pressed="true">All</button>
    <button type="button" data-mode="ok" aria-pressed="false">Confirmed only</button>
    <button type="button" data-mode="check" aria-pressed="false">Needs checking</button>
  </div>
</div></div>

<main class="wrap stack" style="padding-top:8px">
<p id="qnone" hidden>Nothing matches that search. Try fewer or shorter words.</p>
{''.join(sections)}
</main>

<script>{JS}</script>
"""


if __name__ == "__main__":
    out = build(sys.argv[1])
    open(sys.argv[2], "w", encoding="utf-8").write(out)
    print(f"wrote {sys.argv[2]} ({len(out):,} bytes)")
