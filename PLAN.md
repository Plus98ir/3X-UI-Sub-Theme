# 3X-UI-Sub-Theme — PLAN.md
_Updated 2026-11-11_

## Goal
A modern one-file subscription page (`sub.html`) for 3x-ui panels that anyone can drop into the panel's "Sub Theme Directory". Free, open source, shared on GitHub + corenetbase.com.

## Architecture
- `sub.html` — the product (Go `html/template`, no external requests).
- `tools/make_demo.py` → `docs/demo/` (fake data); `tools/make_zip.py` → `docs/download/` (ZIP + sub.html for the site).
- `tools/shoot.ps1`, `tools/shoot-cover.ps1` — screenshots and cover.
- `docs/` — bilingual project page on GitHub Pages (corenetbase.com/3X-UI-Sub-Theme/).

## Decisions
- 2026-11-11: the site's Download must really download and must offer a ZIP; Live demo must open something visible.

## Roadmap
- GitHub Release with the ZIP (pending Sadeq's OK).
