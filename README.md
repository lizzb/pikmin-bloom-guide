# Pikmin Bloom Guide

Personal notes and guides for Pikmin Bloom, kept as plain Markdown.

## Contents

- [Storage management](guide/storage.md) — what to keep and release with the 300-Pikmin cap, no real money

- [Handbook skeleton](guide/handbook-skeleton.md) — restructure of overview.md with confidence tags (✅ confirmed / 🟡 probable / ❓ unconfirmed / 🕰️ outdated)
- [Discord #faq, verbatim](guide/discord-faq.md) — all 36 threads from the Pikmin Bloom! Discord FAQ forum (copied 2026-11-01)

## Big Flower bloom planner

[tools/bloom-planner.html](tools/bloom-planner.html) is a single-file, phone-friendly page. Pick a flower and colour, enter your petals and nectar, and it writes a short planting guide from the Pikipedia blooming flowchart, with sliders to fine-tune the mix. The guide includes a schedule of visits: which squad size to use, which petals to select, how long to stay, and when to wait 5 minutes because the circle has run out of fresh ground. An optional picture shows the ground your squad covers. Units switch between metric and imperial, entries are saved in the browser between visits, and nectar and petal pictures are linked from the Pikmin wiki's image host. Open it in a browser, or serve it with `python3 -m http.server --directory tools`. Logic tests: `node tools/test_bloom_engine.js`.

## Rebuilding the handbook page

The handbook is also published as a private, searchable HTML page (a Claude artifact) for reading on a phone. The page is generated from `guide/handbook-skeleton.md`, so edit the Markdown, not the HTML:

```bash
python3 raw/build_handbook_html.py guide/handbook-skeleton.md OUT.html
```

- The script renders the sections from `## 0.` onward. The page header (title, key-number tiles, tag legend, section index) is written in the script itself.
- Keep the confidence tags and source letters in the Markdown; the page turns them into pills and uses them for the Highlight filter.
- The published page does not update by itself. After rebuilding, republish `OUT.html` to the same artifact link.

## Conventions

- Each guide notes its sources and which claims are community opinion versus official.
- Discord and Reddit advice is marked "to verify" until someone has read those threads directly.
