# Renders tools/cover.html to 3X-UI-Sub-Theme.png (1280x640). Run tools/shoot.ps1 first (the cover uses its screenshots).
# Serve the repo root first: python -m http.server 8766 --bind 127.0.0.1
param([string]$Base = "http://127.0.0.1:8766")

$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$root = Split-Path $PSScriptRoot -Parent
$profile = Join-Path $env:TEMP ("subtheme-cover-" + [guid]::NewGuid())
$out = Join-Path $root "3X-UI-Sub-Theme.png"
& $chrome --headless=new --disable-gpu --hide-scrollbars --no-first-run "--user-data-dir=$profile" `
    --window-size=1280,640 --virtual-time-budget=6000 "--screenshot=$out" "$Base/tools/cover.html" 2>$null | Out-Null
Remove-Item -Recurse -Force $profile -ErrorAction SilentlyContinue
Copy-Item $out (Join-Path $root "docs/img/cover.png") -Force
Write-Output "3X-UI-Sub-Theme.png: $((Get-Item $out).Length) bytes"
