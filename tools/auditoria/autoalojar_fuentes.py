#!/usr/bin/env python3
"""Autoaloja las fuentes de Google que usa Nalanda (fontsource) y reescribe los <link> de cada página.
Requiere: npm install @fontsource/<paquete> en FONTSOURCE_DIR (por defecto /tmp/fonttest).
CJK: solo copia los fragmentos (slices) que contienen caracteres realmente usados en el sitio.
Idempotente.
"""
import re, os, glob, shutil, sys
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, '..', '..', 'docs'))
FS = os.environ.get('FONTSOURCE_DIR', '/tmp/fonttest') + '/node_modules/@fontsource/'
OUT = os.path.join(DOCS, 'assets', 'fonts')
FAM = {  # nombre Google -> (paquete, pesos normales, pesos itálica)
    'IBM Plex Mono': ('ibm-plex-mono', [400, 500], []),
    'Hanken Grotesk': ('hanken-grotesk', [400, 500, 600, 700], []),
    'Noto Serif SC': ('noto-serif-sc', [500, 600, 700], []),
    'Zen Kaku Gothic New': ('zen-kaku-gothic-new', [300, 400, 500, 700], []),
    'Gothic A1': ('gothic-a1', [400, 500, 600, 700], []),
    'Shippori Mincho': ('shippori-mincho', [400, 500, 700], []),
    'Noto Serif KR': ('noto-serif-kr', [500, 600, 700], []),
    'Source Serif 4': ('source-serif-4', [400, 500, 600], [400]),
    'Source Sans 3': ('source-sans-3', [300, 400, 500, 600], []),
    'Figtree': ('figtree', [300, 400, 500, 600, 700], []),
    'Crimson Pro': ('crimson-pro', [400, 500, 600], [400, 500]),
    'Atkinson Hyperlegible': ('atkinson-hyperlegible', [400, 700], []),
    'Cormorant Garamond': ('cormorant-garamond', [400, 500, 600], [400]),
    'DM Sans': ('dm-sans', [300, 400, 500, 600], []),
}
ONLY = [x for x in os.environ.get('SOLO', '').split(',') if x]  # SOLO='DM Sans,Cormorant Garamond' procesa solo esas familias y no toca las páginas
slug = lambda n: n.lower().replace(' ', '-')

pages = sorted(glob.glob(os.path.join(DOCS, '*/*/index.html'))) + [os.path.join(DOCS, 'index.html'), os.path.join(DOCS, '404.html')]

# caracteres no latinos realmente usados, por familia (solo páginas que la cargan) y por escritura propia de la fuente
SCRIPT = {
    'Noto Serif SC': [(0x3000, 0x303F), (0x3400, 0x9FFF), (0xFF00, 0xFFEF)],
    'Zen Kaku Gothic New': [(0x3000, 0x30FF), (0x3400, 0x9FFF), (0xFF00, 0xFFEF)],
    'Shippori Mincho': [(0x3000, 0x30FF), (0x3400, 0x9FFF), (0xFF00, 0xFFEF)],
    'Gothic A1': [(0x1100, 0x11FF), (0x3130, 0x318F), (0xAC00, 0xD7AF)],
    'Noto Serif KR': [(0x1100, 0x11FF), (0x3130, 0x318F), (0xAC00, 0xD7AF), (0x4E00, 0x9FFF)],
}
used_by = {}
for p in pages:
    s_ = open(p, encoding='utf-8').read()
    m = re.search(r'<link href="https://fonts\.googleapis\.com/css2\?([^"]+)" rel="stylesheet">', s_)
    if not m: continue
    t = re.sub(r'<style.*?</style>|<script.*?</script>', '', s_, flags=re.S)
    cs = {ord(ch) for ch in t if ord(ch) >= 0x2E80}
    for f in [unquote(x.split(':')[0]).replace('+', ' ') for x in re.findall(r'family=([^&]+)', m.group(1))]:
        used_by.setdefault(f, set()).update(cs)
for f in list(used_by):
    if f in SCRIPT:
        used_by[f] = {c for c in used_by[f] if any(a <= c <= b for a, b in SCRIPT[f])}
    else:
        used_by[f] = set()
used = set()


def ranges(s):
    out = []
    for tok in s.split(','):
        tok = tok.strip().replace('U+', '')
        if '-' in tok:
            a, b = tok.split('-'); out.append((int(a, 16), int(b, 16)))
        elif '?' in tok:
            out.append((int(tok.replace('?', '0'), 16), int(tok.replace('?', 'F'), 16)))
        else:
            out.append((int(tok, 16),) * 2)
    return out


def keep(name, ur, used):
    if re.search(r'-(latin|latin-ext)-', name): return True
    if re.search(r'-(cyrillic|cyrillic-ext|greek|greek-ext|vietnamese)-', name): return False
    return any(a <= c <= b for a, b in ranges(ur) for c in used)


os.makedirs(OUT + '/files', exist_ok=True)
tot = 0
for gname, (pkg, wn, wi) in FAM.items():
    if ONLY and gname not in ONLY: continue
    css_out = []
    for style, weights in (('normal', wn), ('italic', wi)):
        for w in weights:
            src = FS + pkg + '/%d%s.css' % (w, '-italic' if style == 'italic' else '')
            if not os.path.exists(src): print('FALTA', src); continue
            for blk in re.findall(r'/\*.*?\*/\s*@font-face\s*\{.*?\}', open(src, encoding='utf-8').read(), re.S):
                name = re.search(r'/\*\s*(.*?)\s*\*/', blk).group(1)
                ur = re.search(r'unicode-range:\s*([^;]+);', blk).group(1)
                if not keep(name, ur, used_by.get(gname, set())): continue
                f = re.search(r'url\(\./files/([^)]+\.woff2)\)', blk).group(1)
                dst = os.path.join(OUT, 'files', f)
                if not os.path.exists(dst):
                    shutil.copy(FS + pkg + '/files/' + f, dst)
                tot += os.path.getsize(dst)
                css_out.append("@font-face{font-family:'%s';font-style:%s;font-display:swap;font-weight:%d;src:url(files/%s) format('woff2');unicode-range:%s;}" % (gname, style, w, f, ur))
    open(os.path.join(OUT, slug(gname) + '.css'), 'w', encoding='utf-8').write('\n'.join(css_out) + '\n')
print('woff2 copiados (MB aprox):', round(tot / 1e6, 1))

# páginas
changed = 0
if ONLY: pages = []
for p in pages:
    s = open(p, encoding='utf-8').read(); o = s
    m = re.search(r'<link href="https://fonts\.googleapis\.com/css2\?([^"]+)" rel="stylesheet">\n?', s)
    if not m: continue
    fams = [unquote(x.split(':')[0]).replace('+', ' ') for x in re.findall(r'family=([^&]+)', m.group(1))]
    depth = os.path.relpath(p, DOCS).count('/')
    pre = '../' * depth
    links = ''
    for f in fams:
        if f not in FAM: print('familia sin mapa', f, p); continue
        links += '<link rel="stylesheet" href="%sassets/fonts/%s.css">\n' % (pre, slug(f))
    s = s.replace(m.group(0), links)
    s = re.sub(r'<link rel="preconnect" href="https://fonts\.(googleapis|gstatic)\.com"[^>]*>\n?', '', s)
    if s != o:
        open(p, 'w', encoding='utf-8').write(s); changed += 1
print('páginas actualizadas:', changed)
