# Pikmin Bloom Guide

Personal notes and guides for Pikmin Bloom, kept as plain Markdown.

## Contents

- [Storage management](guide/storage.md) — what to keep and release with the 300-Pikmin cap, no real money

- [Handbook skeleton](guide/handbook-skeleton.md) — restructure of overview.md with confidence tags (✅ confirmed / 🟡 probable / ❓ unconfirmed / 🕰️ outdated)
- [Discord #faq, verbatim](guide/discord-faq.md) — all 36 threads from the Pikmin Bloom! Discord FAQ forum (copied 2026-11-01)

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
