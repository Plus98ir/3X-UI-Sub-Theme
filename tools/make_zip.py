"""Build the site downloads: docs/download/3X-UI-Sub-Theme.zip and docs/download/sub.html.

Run from anywhere:  python tools/make_zip.py
Run it after every change to sub.html (the website's Download buttons point at these files).
The zip is reproducible (fixed timestamps), so it only changes when its contents change.
"""
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "docs" / "download"
ZIP = OUT_DIR / "3X-UI-Sub-Theme.zip"
FILES = ["sub.html", "README.md", "README.fa.md", "LICENSE"]
STAMP = (2026, 1, 1, 0, 0, 0)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name in FILES:
            info = zipfile.ZipInfo(f"3X-UI-Sub-Theme/{name}", STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, (ROOT / name).read_bytes())
    shutil.copyfile(ROOT / "sub.html", OUT_DIR / "sub.html")
    print(f"{ZIP.relative_to(ROOT)}: {ZIP.stat().st_size / 1024:.0f} KB")
    print(f"docs/download/sub.html: {(OUT_DIR / 'sub.html').stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
