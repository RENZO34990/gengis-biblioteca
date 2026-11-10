#!/usr/bin/env python3
"""Aplica los pendientes de la auditoría (taste-skill + Emil Kowalski) a docs/**/index.html.
Idempotente. Uso: python3 tools/auditoria/aplicar_pendientes.py [--dry]
"""
import re, glob, os, sys, html
from PIL import Image

ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'docs')
os.chdir(ROOT)
DRY = '--dry' in sys.argv
MARK_CSS = '/* ---------- AUDITORIA: tipografia y accesibilidad ---------- */'
FAV = {'china': '9E2B25', 'japon': 'A13D2C', 'corea': 'B5623B', '': '1A1A1A'}
UP = 'A-ZÁÉÍÓÚÑ'
stats = {'em_pair': 0, 'em_single': 0, 'em_other': 0, 'en': 0, 'dot': 0}


# ---------------------------------------------------------------- texto
def fix_attr_tag(tag):
    def one(m):
        v = m.group(2)
        v = v.replace(' — ', ' - ').replace('—', '-').replace('–', '-').replace('·', '/')
        return m.group(1) + '"' + v + '"'
    return re.sub(r'(\s[\w:-]+=)"([^"]*)"', one, tag)


LINK = {'lo', 'una', 'un', 'y', 'e', 'pero', 'que', 'cuya', 'cuyo', 'cuyos', 'donde', 'con', 'como', 'el', 'la',
        'los', 'las', 'incluyendo', 'incluida', 'incluido', 'sin', 'aunque', 'mientras'}


def fix_orphans(t):
    # raya de apertura sin cierre: "X  - texto" -> coma o dos puntos
    def f(m):
        nxt = m.group(1)
        w = re.match(r'[\wáéíóúñÁÉÍÓÚ]+', nxt)
        if nxt[0] in '"\u201c\u00ab' or nxt[0].isdigit() or (w and w.group(0).lower() not in LINK):
            return ': ' + nxt
        return ', ' + nxt
    return re.sub(r'(?<=\S)  - (?=\S)(.)', f, t) if False else re.sub(r'(?<=\S)  - (\S.*?)(?=\s|$)', lambda m: f(re.match(r'(.*)', m.group(1))), t)


def fix_text(t):
    # t: texto con etiquetas sustituidas por \x00N\x00
    def pair(m):
        stats['em_pair'] += 1
        return ' (' + m.group(1) + ')'
    t = re.sub(r'—,', ',', t)
    t = re.sub(r'\s?—(?=[^\s—])([^—\n]{1,320}?)(?<=[^\s—])—(?![^\s,.;:)])', pair, t)

    def single(m):
        stats['em_single'] += 1
        nxt = m.group(1)
        return ('. ' if re.match('[' + UP + ']', nxt) else ', ') + nxt
    t = re.sub(r'\s+—\s+(.)', single, t, flags=re.S)
    if '—' in t:
        stats['em_other'] += t.count('—')
        t = t.replace('—', ' - ')
    t = fix_orphans(t)
    n = len(re.findall('–', t))
    stats['en'] += n
    t = re.sub(r'(?<=\d)\s?–\s?(?=\d)', '-', t)
    t = re.sub(r'(?<=[\wÁÉÍÓÚáéíóúñ])\s–\s(?=[\wÁÉÍÓÚáéíóúñ])', ' - ', t)
    t = t.replace('–', '-')
    return t


def fix_dots(chunk):
    def inner(m):
        stats['dot'] += m.group(2).count('·')
        return m.group(1) + re.sub(r'\s*·\s*', ', ', m.group(2)) + m.group(3)
    chunk = re.sub(r'(<span class="credit">)(.*?)(</span>)', inner, chunk, flags=re.S)
    chunk = re.sub(r'(<span class="card-ref">)(.*?)(</span>)',
                   lambda m: m.group(1) + m.group(2).replace('·', '-') + m.group(3), chunk, flags=re.S)
    return chunk


def fix_title_subs(chunk):
    def f(m):
        stats['em_single'] += 1
        return m.group(1) + m.group(2).replace(' — ', ': ', 1) + m.group(3)
    chunk = re.sub(r'(<(?:div|p|span|h\d)[^>]*class="title-[^"]*"[^>]*>)([^<]*)(</)', f, chunk)
    chunk = re.sub(r'(<title>)([^<]*)(</title>)', f, chunk)
    return chunk


def process_chunk(chunk):
    chunk = fix_title_subs(chunk)
    chunk = fix_dots(chunk)
    toks = []

    def tok(m):
        toks.append(fix_attr_tag(m.group(0)))
        return '\x00%d\x00' % (len(toks) - 1)
    t = re.sub(r'<[^>]+>', tok, chunk)
    t = fix_text(t)
    chunk_dots = len(re.findall('·', t))
    stats['dot'] += chunk_dots
    t = re.sub(r'\s*·\s*', ' / ', t)
    return re.sub(r'\x00(\d+)\x00', lambda m: toks[int(m.group(1))], t)


def fix_all_text(s):
    parts = re.split(r'(<style.*?</style>|<script.*?</script>|<!--.*?-->)', s, flags=re.S)
    return ''.join(p if i % 2 else process_chunk(p) for i, p in enumerate(parts))


# ---------------------------------------------------------------- estructura
def meta_block(s, rel):
    if 'name="description"' in s:
        return s
    title = re.search(r'<title>([^<]*)</title>', s).group(1).strip()
    m = re.search(r'class="hero-dek"[^>]*>(.*?)</p>', s, re.S)
    if m:
        desc = re.sub(r'<[^>]+>', '', m.group(1))
    elif rel == 'index.html':
        desc = ('Biblioteca Nalanda: cuadernos de historia, política y economía de China, Japón y Corea. '
                'Club Kongzhi UNMSM, Departamento de Investigación.')
    else:
        desc = title + '. Biblioteca Nalanda, Club Kongzhi UNMSM.'
    desc = html.unescape(re.sub(r'\s+', ' ', desc)).strip()
    if len(desc) > 158:
        cut = desc[:158]
        k = max(cut.rfind('. '), cut.rfind(', '), cut.rfind(' '))
        desc = cut[:k].rstrip(' ,;:') + '.' if cut.rfind('. ') < 60 else cut[:cut.rfind('. ') + 1]
    d = html.escape(desc, quote=True)
    t = html.escape(html.unescape(title), quote=True)
    country = rel.split('/')[0] if '/' in rel else ''
    col = FAV.get(country, FAV[''])
    svg = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' "
           "height='32' rx='6' fill='%23" + col + "'/%3E%3Ctext x='16' y='23' font-size='20' text-anchor='middle' "
           "fill='%23F2EFE9' font-family='Georgia,serif'%3EN%3C/text%3E%3C/svg%3E")
    block = ('<meta name="description" content="%s">\n<meta name="theme-color" content="#%s">\n'
             '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Biblioteca Nalanda">\n'
             '<meta property="og:locale" content="es_PE">\n<meta property="og:title" content="%s">\n'
             '<meta property="og:description" content="%s">\n<link rel="icon" href="%s">\n') % (d, col, t, d, svg)
    return re.sub(r'(<title>[^<]*</title>\n?)', lambda m: m.group(1) + block, s, count=1)


SKIP_CSS = (".skip-link{position:absolute; left:1rem; top:-4rem; z-index:200; background:#1A1A1A; color:#F2EFE9; "
            "padding:.7rem 1.1rem; font:500 .85rem/1 sans-serif; text-decoration:none; "
            "transition:top .25s cubic-bezier(0.23,1,0.32,1);}\n.skip-link:focus{top:1rem;}\n")
TYPO_CSS = (MARK_CSS + "\n"
            ".num,.acto-date,.v-yr,.v-k,.when,td,th{font-variant-numeric:tabular-nums;}\n"
            "h1,h2,h3,.acto-title,.title-cn{text-wrap:balance;}\n"
            "p,li,.lbl{text-wrap:pretty;}\n"
            "h1,h2,h3,.acto-title,.title-pinyin,.title-romaji,.title-romaja,p,li,.lbl{overflow-wrap:break-word;}\n"
            ".acto-figure img{height:auto;}\n")


def structure(s, rel):
    is_cuaderno = '<header class="hero"' in s
    if '<a class="skip-link"' not in s and 'class="skip' not in s:
        s = re.sub(r'(<body[^>]*>)', r'\1\n<a class="skip-link" href="#contenido">Saltar al contenido</a>', s, count=1)
        s = s.replace('</style>', SKIP_CSS + '</style>', 1) if False else s
    if '.skip-link{' not in s:
        i = s.rindex('</style>')
        s = s[:i] + SKIP_CSS + s[i:]
    if is_cuaderno and '<main' not in s:
        s = s.replace('</header>', '</header>\n<main id="contenido">', 1)
        s = re.sub(r'(<footer)', r'</main>\n\1', s, count=1)
    elif '<main' in s and 'id="contenido"' not in s:
        s = re.sub(r'<main(?![^>]*\bid=)', '<main id="contenido"', s, count=1)
        if 'id="contenido"' not in s:
            s = re.sub(r'<main\b', '<main id="contenido"', s, count=1) if '<main id=' not in s else s
    s = s.replace('<div class="nav-adjacent">', '<div class="nav-adjacent" role="navigation" aria-label="Cuadernos relacionados">')
    if MARK_CSS not in s:
        i = s.rindex('</style>')
        s = s[:i] + TYPO_CSS + s[i:]
    s = s.replace('scrub: 1.2', 'scrub: 0.6')
    if rel == 'index.html':
        s = s.replace('z-index:999;', 'z-index:100;')
    return s


def img_dims(s, rel):
    base = os.path.dirname(rel)

    def f(m):
        tag = m.group(0)
        if ' width=' in tag:
            return tag
        src = re.search(r'src="([^"]+)"', tag).group(1)
        p = os.path.normpath(os.path.join(base, src))
        if not os.path.exists(p):
            return tag
        w, h = Image.open(p).size
        return tag.replace('<img ', '<img width="%d" height="%d" ' % (w, h), 1)
    return re.sub(r'<img [^>]*>', f, s)


def cifras(s):
    if 'class="cifras"' in s or '<div class="hero-stats">' not in s:
        return s, 'ya' if 'class="cifras"' in s else 'sin-cifras'
    m = re.search(r'<div class="hero-stats">((?:\s*<div[^>]*>.*?</div>)+)\s*</div>', s, re.S)
    if not m:
        return s, 'no-match'
    block = m.group(0)
    s = s.replace(block, '', 1)
    sec = '\n<section class="cifras" aria-label="Cifras clave">\n' + block + '\n</section>'
    s = s.replace('</header>', '</header>' + sec, 1)
    # CSS
    s = s.replace('.hero .hero-stats', '.cifras .hero-stats')
    s = re.sub(r'\s*animation:statBar \.9s cubic-bezier\(0\.23,1,0\.32,1\) both;', '', s)
    s = re.sub(r'\n\s*\.cifras \.hero-stats > div:nth-child\(\d\)::before\{animation-delay:[\d.]+s;\}', '', s)
    s = s.replace('.cifras .hero-stats > div::before{animation:none; transform:scaleY(1);}',
                  '.cifras .hero-stats > div::before{animation:none !important; transform:scaleY(1);}')
    hero = re.search(r'header\.hero\{[^}]*\}', s, re.S).group(0)
    dark = 'color:var(--paper)' in hero
    if dark:
        stops = re.findall(r'(#[0-9A-Fa-f]{6}|var\(--[\w-]+\))\s+\d+%\s*\)', hero)
        bg = stops[-1] if stops else 'var(--ink)'
        wrap = '.cifras{max-width:none; margin:0; background:%s; color:var(--paper); padding:3rem 8vw 4.5rem;}\n' % bg
    else:
        wrap = '.cifras{max-width:none; margin:0; padding:3.5rem 8vw 3rem;}\n'
    wrap += ('.cifras .hero-stats{margin-top:0;}\n'
             '.cifras.in .hero-stats > div::before{animation:statBar .9s cubic-bezier(0.23,1,0.32,1) both;}\n'
             '.cifras.in .hero-stats > div:nth-child(1)::before{animation-delay:.1s;}\n'
             '.cifras.in .hero-stats > div:nth-child(2)::before{animation-delay:.25s;}\n'
             '.cifras.in .hero-stats > div:nth-child(3)::before{animation-delay:.4s;}\n')
    i = s.rindex('</style>')
    s = s[:i] + wrap + s[i:]
    js = ("<script>(function(){var s=document.querySelector('.cifras');if(!s)return;"
          "if(typeof reduceMotion!=='undefined'&&reduceMotion||!('IntersectionObserver' in window)){s.classList.add('in');return;}"
          "var io=new IntersectionObserver(function(e){if(e[0].isIntersecting){s.classList.add('in');io.disconnect();}},{threshold:.35});"
          "io.observe(s);})();</script>\n")
    s = s.replace('</body>', js + '</body>', 1)
    return s, 'ok'


files = sorted(glob.glob('*/*/index.html')) + ['index.html']
report = {}
for rel in files:
    s0 = open(rel, encoding='utf-8').read()
    s = fix_all_text(s0)
    s, st = cifras(s)
    s = structure(s, rel)
    s = img_dims(s, rel)
    s = meta_block(s, rel)  # al final: usa el texto ya corregido
    report[rel] = st
    if not DRY and s != s0:
        open(rel, 'w', encoding='utf-8').write(s)
print(stats)
bad = {k: v for k, v in report.items() if v not in ('ok', 'ya', 'sin-cifras')}
print('cifras:', {v: list(report.values()).count(v) for v in set(report.values())}, 'problemas:', bad)
