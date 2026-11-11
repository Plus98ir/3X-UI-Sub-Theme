"""Build docs/demo/index.html: sub.html with the Go template filled with fake demo data.

Run from the repo root:  python tools/make_demo.py
Query options on the demo page: ?lang=fa|en  ?theme=dark|light  ?tab=apps|links|configs  ?plat=android|ios|windows|macos
"""
import base64
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "sub.html"
OUT = ROOT / "docs" / "demo" / "index.html"

UUID = "3f1c2a8e-5b7d-4e9a-a1c4-7d2e9b0f6a13"
HOST = "sub.example.com"
SID = "demo-7f3a9c"


def b64(s: str) -> str:
    return base64.b64encode(s.encode()).decode()


vmess = {
    "v": "2", "ps": "🇳🇱 Netherlands · gRPC", "add": "nl1.example.com", "port": "8443",
    "id": UUID, "net": "grpc", "type": "none", "tls": "tls", "sni": "nl1.example.com",
}

LINKS = [
    f"vless://{UUID}@de1.example.com:443?type=tcp&security=reality&sni=www.example.com&fp=chrome&pbk=demo&sid=6a#🇩🇪 Germany · Reality",
    f"vless://{UUID}@cdn.example.com:443?type=ws&security=tls&host=cdn.example.com&path=%2Fws#🌐 CDN · WebSocket",
    f"vless://{UUID}@uk1.example.com:443?type=xhttp&security=tls&sni=uk1.example.com#🇬🇧 UK · XHTTP",
    "vmess://" + b64(json.dumps(vmess, ensure_ascii=False)),
    "trojan://demo-pass@fi1.example.com:443?type=tcp&security=tls&sni=fi1.example.com#🇫🇮 Finland · Trojan",
    "hysteria2://demo-pass@tr1.example.com:8443?sni=tr1.example.com#🇹🇷 Turkey · Hysteria2",
    "ss://" + b64("2022-blake3-aes-128-gcm:demo-pass") + "@us1.example.com:8388#🇺🇸 USA · Shadowsocks",
]

DATA = {
    "sId": SID,
    "enabled": True,
    "isOnline": True,
    "download": "15.2 GB",
    "upload": "3.2 GB",
    "total": "50 GB",
    "used": "18.4 GB",
    "remained": "31.6 GB",
    "expire": 0,
    "lastOnline": 0,
    "downloadByte": 16320875724,
    "uploadByte": 3435973837,
    "totalByte": 53687091200,
    "subUrl": f"https://{HOST}/sub/{SID}",
    "subJsonUrl": f"https://{HOST}/json/{SID}",
    "subClashUrl": f"https://{HOST}/clash/{SID}",
    "subTitle": "Nova VPN",
    "subSupportUrl": "https://example.com/support",
    "subUpdates": 12,
    "links": LINKS,
    "emails": ["demo-user"],
    "datepicker": "gregorian",
    "announce": "سرور جدید ترکیه اضافه شد 🎉  ·  New Turkey server added",
}

# Runs before the theme script: live dates, ?lang/?theme, and a fetch stub (no panel behind the demo).
STUB = """
(function () {
  var d = window.__SUB_DATA__, now = Date.now();
  d.expire = Math.floor(now / 1000) + 23 * 86400;
  d.lastOnline = now - 4 * 60000;
  var q = new URLSearchParams(location.search);
  try {
    if (q.get("lang")) localStorage.setItem("xui_custom_sub_lang", q.get("lang"));
    if (q.get("theme")) localStorage.setItem("xui_custom_sub_theme", q.get("theme"));
  } catch (e) {}
  window.fetch = function (url) {
    if (/hwid-status/.test(String(url))) {
      return Promise.resolve(new Response(JSON.stringify({ active: true, registered: 2, limit: 3, full: false }),
        { headers: { "Content-Type": "application/json" } }));
    }
    return Promise.resolve(new Response("", { status: 404 }));
  };
})();
"""

AFTER = """
  <script>
    (function () {
      var q = new URLSearchParams(location.search);
      var plat = q.get("plat"), tab = q.get("tab");
      if (plat) { var p = document.querySelector('[data-plat="' + plat + '"]'); if (p) p.click(); }
      if (tab) { var t = document.querySelector('[data-tab="' + tab + '"]'); if (t) t.click(); }
    })();
  </script>
</body>"""


def main() -> int:
    html = SRC.read_text(encoding="utf-8")
    title_tpl = "{{ if .subTitle }}{{ .subTitle }}{{ else }}Subscription{{ end }}"
    if html.count(title_tpl) != 2:
        print("unexpected template: title block count changed", file=sys.stderr)
        return 1
    html = html.replace(title_tpl, DATA["subTitle"])
    html, n = re.subn(r"<noscript>.*?</noscript>",
                      "<noscript><div class=\"card\">Demo needs JavaScript.</div></noscript>",
                      html, count=1, flags=re.S)
    if n != 1:
        print("unexpected template: <noscript> block not found", file=sys.stderr)
        return 1
    data_js = json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace("window.__SUB_DATA__ = {{ . }};", "window.__SUB_DATA__ = " + data_js + ";" + STUB, 1)
    html = html.replace("</body>", AFTER, 1)
    html = html.replace("<head>", "<head>\n  <meta name=\"robots\" content=\"noindex\" />", 1)
    if "{{" in html:
        print("template tags left in demo: " + html[html.index("{{"):][:60], file=sys.stderr)
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8", newline="\n")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(html)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
