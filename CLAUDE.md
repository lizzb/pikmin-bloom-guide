# Pikmin Bloom guide: working rules

- **Publishing:** the only published copy is the GitHub Pages site (https://lizzb.github.io/pikmin-bloom-guide/). `tools/build_site.py` builds it and `.github/workflows/pages.yml` deploys it on every push to `main`. Add new pages to that build; do not publish standalone artifacts (Claude artifacts, gists, other hosts) of the Big Flower planner, the handbook or anything else from here. Finish a change by committing and pushing it so the site updates.
- **Big Flower helper:** edit `tools/bloom-planner.html` and run `node tools/test_bloom_engine.js` (the deploy runs it too). It is served at `/big-flower-helper/`.
- **Never push the local Discord #faq files:** `guide/discord-faq.md`, `raw/discord-faq.json` and `raw/build_faq.py` are gitignored and stay local. `guide/overview.md` is gitignored too, because it contains a pasted copy of that FAQ.
- Keep everything in history; never delete, archive instead.
