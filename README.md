# Conor's Bandon Blog

Hugo source for https://conoroneill.com, using the existing CleanWhite theme.

```sh
hugo serve   # local preview
hugo         # production build into docs, for GitHub Pages
```

Hugo 0.170.0 writes previews to disk by default. The two-line development configuration directs them to the ignored `.hugo-preview` folder, so plain `hugo serve` cannot overwrite the production files in `docs`. No wrapper or extra command is needed.

Post navigation, canonical links and local assets use site-relative URLs. The original theme directory structure is retained; compatibility fixes cover removed Hugo APIs, pagination, services and old tweet embeds.

The automated check rejects localhost URLs and live-reload scripts in published HTML/XML. The custom domain remains in `docs/CNAME`.
