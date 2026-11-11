# Screenshots of the demo page with headless Chrome.
# First: python tools/make_demo.py, then serve docs/: python -m http.server 8765 --bind 127.0.0.1 --directory docs
param([string]$Base = "http://127.0.0.1:8765")

$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$root = Split-Path $PSScriptRoot -Parent
$shots = @(
    @{ out = "screenshots/desktop-dark-fa.png";  url = "demo/?lang=fa&theme=dark&plat=android";  size = "1600,1180"; scale = 1 },
    @{ out = "screenshots/desktop-light-en.png"; url = "demo/?lang=en&theme=light&plat=android"; size = "1600,1180"; scale = 1 },
    @{ out = "screenshots/configs-dark-en.png";  url = "demo/?lang=en&theme=dark&tab=configs";   size = "1600,1000"; scale = 1 },
    @{ out = "screenshots/links-dark-fa.png";    url = "demo/?lang=fa&theme=dark&tab=links";     size = "1600,960";  scale = 1 },
    @{ out = "screenshots/mobile-dark-fa.png";   url = "demo/phone.html?lang=fa&theme=dark&plat=android";  size = "600,1500"; scale = 2; crop = 390 },
    @{ out = "screenshots/mobile-light-en.png";  url = "demo/phone.html?lang=en&theme=light&plat=ios";     size = "600,1500"; scale = 2; crop = 390 }
)
foreach ($s in $shots) {
    $profile = Join-Path $env:TEMP ("subtheme-shot-" + [guid]::NewGuid())
    $out = Join-Path $root $s.out
    & $chrome --headless=new --disable-gpu --hide-scrollbars --no-first-run "--user-data-dir=$profile" `
        "--window-size=$($s.size)" "--force-device-scale-factor=$($s.scale)" --virtual-time-budget=4000 `
        "--screenshot=$out" "$Base/$($s.url)" 2>$null | Out-Null
    Remove-Item -Recurse -Force $profile -ErrorAction SilentlyContinue
    if ($s.crop) {
        python -c "import sys; from PIL import Image; p=sys.argv[1]; w=int(sys.argv[2]); im=Image.open(p); im.crop((0,0,w,im.height)).save(p, optimize=True)" $out ($s.crop * $s.scale)
    }
    Write-Output "$($s.out): $((Get-Item $out).Length) bytes"
}
