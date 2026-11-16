# Conor's Bandon Blog

Hugo source for https://conoroneill.com, using the vendored CleanWhite theme. Tested with **Hugo 0.170.0** (standard Linux binary); Extended Hugo is not required by this theme.

## Preview and build

The wrapper finds `hugo` on PATH, then `~/bin/hugo`. Set `HUGO_BIN` to select a different executable.

```bash
./scripts/hugo version
./scripts/hugo server --buildDrafts --disableFastRender --renderToMemory
```

Open the local URL printed by Hugo. Photo Revival is a draft at `/2026/11/16/photo-revival/`; edit `content/post/photo-revival.md`. Its four approved photographic derivatives live in `static/images/2026/11/photo-revival/`. Add the personal introduction before setting `draft = false`.

```bash
python3 scripts/check-build.py
./scripts/hugo --panicOnWarning
```

The check builds both production and drafts into temporary directories, verifies every published content route, archive/pagination routes, XML feeds, the new article's canonical/repository links and its assets. The normal build writes to the existing `docs` publish directory. This directory contains tracked historical output; review a production build's changes before committing it. Do not build drafts into `docs` for publication.

## Hugo compatibility changes

- Modern template layout names: `home.html`, `single.html`, `section.html`, `taxonomy.html`, `term.html`, `_partials` and `_shortcodes`.
- Separate archive and taxonomy rendering, preserving the dated post permalink pattern.
- `pagination.pagerSize`, `locale` and `services` configuration replace removed keys/APIs.
- Canonical URLs and neighbouring-post links use supported page permalink methods.
- Analytics is configured once through Hugo's embedded template. Disqus uses the current services API.
- Historical `tweet` shortcodes retain their IDs and link/embed in the browser, without calling a social-media API during a build. Deleted tweets may remain unavailable.

Reference: [Hugo template lookup](https://gohugo.io/templates/lookup-order/), [pagination](https://gohugo.io/configuration/pagination/) and [services](https://gohugo.io/configuration/services/).

The GitHub workflow runs the same checks with a checksum-verified Hugo 0.170.0 binary. It does not deploy. The old root-level `circle.yml` is a historical deployment configuration, not the active compatibility workflow; review its cloud tooling separately before reusing it.
