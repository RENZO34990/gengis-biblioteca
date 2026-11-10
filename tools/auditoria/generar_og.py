#!/usr/bin/env python3
"""Genera una imagen og:image 1200x630 por página (fuentes autoalojadas) y agrega las metaetiquetas.
Requiere servidor local en :8765 sirviendo docs/ y Playwright. Idempotente."""
import re, os, glob, html
from playwright.sync_api import sync_playwright

DOCS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs'))
BASE = os.environ.get('NALANDA_URL', 'https://renzo34990.github.io/gengis-biblioteca/')  # confirmar la URL real de Pages
TH = {  # fondo, texto, acento, tipografía grande, tipografía de texto, css de fuentes
    'china': ('linear-gradient(155deg,#6F1D19 0%,#9E2B25 62%,#8A2620 100%)', '#F2EFE9', '#C9A63E', "'Noto Serif SC'", "'Hanken Grotesk'", ['noto-serif-sc', 'hanken-grotesk']),
    'japon': ('#F5F1E8', '#2B2A28', '#A13D2C', "'Shippori Mincho'", "'Zen Kaku Gothic New'", ['shippori-mincho', 'zen-kaku-gothic-new']),
    'corea': ('linear-gradient(160deg,#16201C 0%,#4F6F61 68%,#3E5A4E 100%)', '#F5F3EE', '#E9A882', "'Gothic A1'", "'Gothic A1'", ['gothic-a1']),
    '': ('#1A1A1A', '#F2EFE9', '#C9A63E', "'Source Serif 4'", "'Source Sans 3'", ['source-serif-4', 'source-sans-3']),
}
pages = sorted(glob.glob(DOCS + '/*/*/index.html')) + [DOCS + '/index.html']
os.makedirs(DOCS + '/assets/og', exist_ok=True)
TMP = DOCS + '/_og_tmp.html'
jobs = []
for p in pages:
    rel = os.path.relpath(p, DOCS)
    s = open(p, encoding='utf-8').read()
    title = html.unescape(re.search(r'<title>([^<]*)</title>', s).group(1))
    country = rel.split('/')[0] if '/' in rel else ''
    key = rel[:-len('/index.html')].replace('/', '-') if '/' in rel else 'portal'
    if ': ' in title: big, small = title.split(': ', 1)
    else: big, small = ('Biblioteca Nalanda', 'Historia, política y economía de China, Japón y Corea') if not country else (title, '')
    jobs.append((p, rel, s, country, key, big, small))

with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630})
    for p, rel, s, country, key, big, small in jobs:
        bg, fg, ac, f1, f2, css = TH[country]
        links = ''.join('<link rel="stylesheet" href="assets/fonts/%s.css">' % c for c in css + ['ibm-plex-mono'])
        label = {'china': 'China', 'japon': 'Japón', 'corea': 'Corea', '': 'Club Kongzhi UNMSM'}[country]
        doc = '''<!DOCTYPE html><meta charset="utf-8">%s<style>
        *{box-sizing:border-box;margin:0} body{width:1200px;height:630px;background:%s;color:%s;display:flex;flex-direction:column;justify-content:space-between;padding:64px 72px;font-family:%s,sans-serif;position:relative;overflow:hidden}
        .top{font-family:'IBM Plex Mono',monospace;font-size:22px;letter-spacing:.16em;text-transform:uppercase;color:%s}
        .big{font-family:%s,serif;font-weight:700;font-size:%dpx;line-height:1.08;max-width:1000px}
        .small{margin-top:22px;font-size:34px;line-height:1.3;opacity:.82;max-width:960px}
        .bar{width:84px;height:4px;background:%s;margin-bottom:28px}
        .bot{font-family:'IBM Plex Mono',monospace;font-size:20px;letter-spacing:.12em;text-transform:uppercase;opacity:.7}
        </style><div class="top">Biblioteca Nalanda / %s</div>
        <div><div class="bar"></div><div class="big">%s</div><div class="small">%s</div></div>
        <div class="bot">Club Kongzhi UNMSM / Departamento de Investigación</div>''' % (
            links, bg, fg, f2, ac, f1, 88 if len(big) <= 10 else 64 if len(big) <= 26 else 52, ac, label, html.escape(big), html.escape(small))
        open(TMP, 'w', encoding='utf-8').write(doc)
        pg.goto('http://localhost:8765/_og_tmp.html'); pg.wait_for_timeout(700)
        pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        out = DOCS + '/assets/og/%s.jpg' % key
        pg.screenshot(path=out, type='jpeg', quality=84)
        if 'og:image' not in s:
            url = BASE + 'assets/og/%s.jpg' % key
            tags = ('<meta property="og:image" content="%s">\n<meta property="og:image:width" content="1200">\n'
                    '<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="%s">\n'
                    '<meta name="twitter:card" content="summary_large_image">\n') % (url, html.escape(big + (': ' + small if small else ''), quote=True))
            s = re.sub(r'(<meta property="og:description"[^>]*>\n)', lambda m: m.group(1) + tags, s, count=1)
            open(p, 'w', encoding='utf-8').write(s)
    b.close()
os.remove(TMP)
print('og generadas:', len(jobs))
