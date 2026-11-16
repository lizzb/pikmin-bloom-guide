# Pikmin Bloom Guide

Personal notes and guides for Pikmin Bloom, kept as plain Markdown.

**Live site:** https://lizzb.github.io/pikmin-bloom-guide/ (index, [Big Flower helper](https://lizzb.github.io/pikmin-bloom-guide/big-flower-helper/), [handbook](https://lizzb.github.io/pikmin-bloom-guide/handbook/)). Unofficial; not affiliated with Niantic or Nintendo.

## Contents

- [Storage management](guide/storage.md) — what to keep and release with the 300-Pikmin cap, no real money

- [Handbook skeleton](guide/handbook-skeleton.md) — restructure of overview.md with confidence tags (✅ confirmed / 🟡 probable / ❓ unconfirmed / 🕰️ outdated)

## Big Flower bloom planner

[tools/bloom-planner.html](tools/bloom-planner.html) is a single-file, phone-friendly page. Pick a flower and colour, enter your petals and nectar, and it writes a short planting guide from the Pikipedia blooming flowchart, with sliders to fine-tune the mix. The guide includes a schedule of visits: which squad size to use, which petals to select, how long to stay, and when to wait 5 minutes because the circle has run out of fresh ground. An optional picture shows the ground your squad covers. Units switch between metric and imperial, entries are saved in the browser between visits, and nectar and petal pictures are linked from the Pikmin wiki's image host. Open it in a browser, or serve it with `python3 -m http.server --directory tools`. Logic tests: `node tools/test_bloom_engine.js`.

## Publishing

Everything on the site is built from this repo by `tools/build_site.py` and deployed by `.github/workflows/pages.yml` on every push to `main`. Edit the source, commit, push; the site updates in about a minute.

| Site page | Source |
| --- | --- |
| `/` (index) | written in `tools/build_site.py` (add a card to `CARDS` for a new page) |
| `/big-flower-helper/` | `tools/bloom-planner.html` |
| `/handbook/` | `guide/handbook-skeleton.md`, rendered by `raw/build_handbook_html.py` |

Preview locally: `python3 tools/build_site.py && python3 -m http.server --directory _site`. The handbook header (title, key-number tiles, tag legend, section index) is written in `raw/build_handbook_html.py`; the sections come from the Markdown, and its confidence tags and source letters become the page's pills and Highlight filter.

## Conventions

- Each guide notes its sources and which claims are community opinion versus official.
- Discord and Reddit advice is marked "to verify" until someone has read those threads directly.
