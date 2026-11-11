# 3X-UI-Sub-Theme — ARCHIVE.md

## 2026-11-11
- Saila (our own app) added as a featured card: Android = intent:// pinned to `ir.plus98.saila` (Saila shares the v2rayng:// scheme) with fallback to corenetbase.com/Saila/, plus download button; Windows = copy (Ctrl+V in Saila) + latest `Saila-windows-64.zip`. Pushed 3de9ebb, uploaded to the Turkey + Iran panels (`/etc/3x-ui/sub_templates/my-theme/sub.html`, backups `sub.html.bak-2026-11-11`), verified live, Sadeq OK'd it.
- Site Download fixed: the button pointed at raw.githubusercontent.com (cross-origin, so the browser opened the file instead of saving it). Now "Download ZIP" (`docs/download/3X-UI-Sub-Theme.zip`: sub.html + READMEs + LICENSE) and "or just sub.html" (`docs/download/sub.html`), both same-origin with `download`. Built by new `tools/make_zip.py`. READMEs link to them too.
- Live demo fixed: `#demo` id sat on the FA-only heading (hidden in EN), so nothing happened. Button now opens `demo/?lang=<lang>` in a new tab; `#demo` moved to a section wrapping the demo.
- Project created: sub.html, demo, screenshots, cover, bilingual page, READMEs, MIT, site `descriptions.json` entry.
