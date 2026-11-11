# 3X-UI-Sub-Theme — CLAUDE.md
_Updated 2026-11-11_

Custom subscription page template for 3x-ui panels. Repo: github.com/Plus98ir/3X-UI-Sub-Theme (public). Page: https://corenetbase.com/3X-UI-Sub-Theme/ (GitHub Pages from `/docs`), live demo at `/demo/`.

## Key facts
- `sub.html` = the product: one Go `html/template` file. The panel (3x-ui v3.10.0+, setting `subThemeDir`, "Sub Theme Directory") renders it with `window.__SUB_DATA__ = {{ . }}` (map from `internal/sub/controller.go` `subPageContext`). Template error → panel falls back to its default page. File is re-read when its mtime changes.
- Originally made in `H:\Cloude\3X-UI Sanai\sub_templates\my-theme\sub.html` (untracked there). This repo is now the source of truth.
- Live data: page polls `<subUrl>?format=info` and `<subUrl>/hwid-status` every 15 s while visible.
- No external requests on purpose (Iran: CDNs filtered). Don't add CDN scripts or web fonts to `sub.html`.
- Demo: `python tools/make_demo.py` fills the template with fake data → `docs/demo/index.html` (fetch is stubbed; `?lang ?theme ?tab ?plat`). Never use real panel data/links in the demo or screenshots.
- Screenshots: serve `docs/` on 8765, `tools/shoot.ps1` (headless Chrome; phones via `docs/demo/phone.html` iframe because headless Chrome won't go under 500 px wide). Cover: serve repo root on 8766, `tools/shoot-cover.ps1` → `3X-UI-Sub-Theme.png` + `docs/img/cover.png`. Copy screenshots used by the site into `docs/img/`.
- Downloads link to `releases/latest/download/sub.html`: after changing `sub.html`, make a new release with `sub.html` attached (ask before choosing the version number).

## Working rules (all projects)
- Every page full width — no narrow centered container.
- End-user pages bilingual FA + EN, dark, modern, mobile-ready.
- Tools must be universal — never hard-code Sadeq's own servers.
- Never bump a version number without asking.
