import re, html as _h

import os
REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs') + '/'

TOKENS = {
 'china': ':root{--v-accent:var(--vermillion); --v-accent-deep:var(--vermillion-deep); --v-accent2:var(--gold); --v-accent-soft:rgba(201,166,62,.22); --v-soft:var(--paper-warm); --v-paper:var(--paper); --v-line:var(--line); --v-ink:var(--ink); --v-ink-soft:var(--ink-soft); --v-head:\'Noto Serif SC\', serif; --v-body:\'Hanken Grotesk\', sans-serif; --v-mono:\'IBM Plex Mono\', monospace;}',

 'japon': ':root{--v-accent:var(--vermillion); --v-accent-deep:var(--vermillion-deep); --v-accent2:var(--gold); --v-accent-soft:rgba(168,134,60,.22); --v-soft:var(--paper-warm); --v-paper:var(--paper); --v-line:var(--line); --v-ink:var(--ink); --v-ink-soft:var(--ink-soft); --v-head:\'Shippori Mincho\', serif; --v-body:\'Zen Kaku Gothic New\', sans-serif; --v-mono:\'IBM Plex Mono\', monospace;}',
 'corea': ':root{--v-accent:var(--terracota); --v-accent-deep:var(--terracota-deep); --v-accent2:var(--celadon-deep); --v-accent-soft:rgba(79,111,97,.2); --v-soft:var(--paper-warm); --v-paper:var(--paper); --v-line:var(--line); --v-ink:var(--ink); --v-ink-soft:var(--ink-soft); --v-head:\'Gothic A1\', sans-serif; --v-body:\'Gothic A1\', sans-serif; --v-mono:\'IBM Plex Mono\', monospace;}',
}

SHIP = '<svg class="v-ship" viewBox="0 0 26 26" aria-hidden="true"><path d="M3 15h20l-3 6H6z" fill="currentColor"/><path d="M13 3v11M13 4l6 8h-6M12 6l-5 7h5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
ARR = '<svg class="v-arrow" viewBox="0 0 54 24" aria-hidden="true"><path d="M2 12h44M36 3l12 9-12 9" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARR_S = '<svg class="v-arr" viewBox="0 0 22 22" aria-hidden="true"><path d="M2 11h16M12 5l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARR_V = '<svg class="v-vs" viewBox="0 0 34 24" aria-hidden="true"><path d="M2 12h26M20 4l10 8-10 8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def esc(s):
    return s

def wrap(kind, one, inner, note=None, attrs=''):
    n = f'\n            <p class="vis-note">{note}</p>' if note else ''
    return (f'<!--vis--><div class="vis" data-vis="{kind}"{attrs}>\n'
            f'          <p class="vis-one"><small>En una frase</small>{one}</p>\n'
            f'          <div class="vis-card">\n{inner}{n}\n          </div>\n        </div><!--/vis-->\n        ')

def rings(one, center, legend, note=None, aria=''):
    lis = ''.join(f'                <li><i class="k{i+1}"></i><span><b>{t}</b>{d}</span></li>\n' for i, (t, d) in enumerate(legend))
    inner = (f'            <div class="v-rings-wrap">\n'
             f'              <div class="v-rings" role="img" aria-label="{aria}"><div class="v-ring r3"></div><div class="v-ring r2"></div><div class="v-ring r1">{center}</div></div>\n'
             f'              <ul class="v-legend">\n{lis}              </ul>\n            </div>')
    return wrap('rings', one, inner, note)

def steps(one, items, note=None, ship=False, up=False):
    """items en orden de lectura (arriba->abajo): (marca, titulo, texto)"""
    st = ''.join(f'              <div class="v-stop" role="listitem"><span class="v-yr">{y}</span><h4>{t}</h4><p>{d}</p></div>\n' for y, t, d in items)
    inner = (f'            <div class="v-steps" role="list"{" data-up" if up else ""}>\n'
             f'              <div class="v-rail"><div class="v-fill"></div></div>\n{SHIP if ship else ""}{st}            </div>')
    return wrap('steps', one, inner, note)

def switches(one, head, rows, on='En manos del Estado', off='Perdido', note=None):
    rs = ''.join(f'            <div class="v-sw off"><span class="v-sw-mark">{m}</span><span><b>{t}</b><em>{d}</em></span><span class="to-end"><span class="v-sw-state"><span class="st-on">{on}</span><span class="st-off">{off}</span></span><span class="v-sw-track"></span></span></div>\n' for m, t, d in rows)
    inner = f'            <div class="v-sov-head"><span>{head}</span><span class="v-sov-count" aria-live="polite"><b class="n">0</b> / {len(rows)}</span></div>\n{rs.rstrip()}'
    return wrap('switches', one, inner, note)

def press(one, left, core, right, out, core_small='', note=None):
    crack = '<svg class="v-crack" viewBox="0 0 96 96" aria-hidden="true"><path d="M48 0l-8 22 12 14-14 20 10 14-6 26" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--v-paper)"/></svg>'
    sm = f'<small>{core_small}</small>' if core_small else ''
    inner = (f'            <div class="v-press">\n'
             f'              <div class="v-press-side v-press-l"><b>{left[0]}</b><em>{left[1]}</em>{ARR}</div>\n'
             f'              <div class="v-press-core">{core}{sm}{crack}</div>\n'
             f'              <div class="v-press-side v-press-r"><b>{right[0]}</b><em>{right[1]}</em>{ARR}</div>\n'
             f'            </div>\n            <div class="v-press-out">{out}</div>')
    return wrap('press', one, inner, note)

def timeline(one, items, note=None):
    its = ''.join(f'              <div class="v-tl"><span class="v-tl-yr">{y}</span><p>{t}</p></div>\n' for y, t in items)
    inner = (f'            <div class="v-tline" style="--n:{len(items)}">\n'
             f'              <div class="v-tline-rail"><div class="v-tline-fill"></div></div>\n{its}            </div>')
    return wrap('timeline', one, inner, note)

def flow(one, nodes, note=None):
    """nodes: (etiqueta, titulo, texto)"""
    parts = []
    for i, (k, t, d) in enumerate(nodes):
        if i: parts.append(f'              {ARR_S}\n')
        parts.append(f'              <div class="v-node"><span class="v-k">{k}</span><h4>{t}</h4><p>{d}</p></div>\n')
    inner = f'            <div class="v-flow">\n{"".join(parts)}            </div>'
    return wrap('flow', one, inner, note)

def S(display, label, to=None, dec=0, pre='', suf=''):
    return dict(display=display, label=label, to=to, dec=dec, pre=pre, suf=suf)

def stats(one, items, note=None):
    out = ''
    for s in items:
        a = f' data-to="{s["to"]}" data-dec="{s["dec"]}" data-pre="{s["pre"]}" data-suf="{s["suf"]}"' if s['to'] is not None else ''
        out += f'              <div class="v-stat"><span class="v-num"{a}>{s["display"]}</span><span class="v-lbl">{s["label"]}</span></div>\n'
    inner = f'            <div class="v-stats" style="--n:{len(items)}">\n{out}            </div>'
    return wrap('stats', one, inner, note)

def bars(one, items, note=None):
    """items: (etiqueta, valor_texto, porcentaje_ancho, alt)"""
    out = ''
    for lab, val, pct, *alt in items:
        cl = ' alt' if alt and alt[0] else ''
        out += f'              <div class="v-bar{cl}"><span class="v-bl">{lab}</span><div class="v-btrack"><div class="v-bfill" style="--w:{pct}%"></div></div><span class="v-bv">{val}</span></div>\n'
    inner = f'            <div class="v-bars">\n{out}            </div>'
    return wrap('bars', one, inner, note)

def versus(one, before, after, labels=('Antes', 'Después'), note=None, neutral=False):
    lb = ''.join(f'<li>{x}</li>' for x in before)
    la = ''.join(f'<li>{x}</li>' for x in after)
    mid = '<span class="v-vs v-vs-t">vs</span>' if neutral else ARR_V
    inner = (f'            <div class="v-versus{" neutral" if neutral else ""}">\n'
             f'              <div class="v-col before"><h4>{labels[0]}</h4><ul>{lb}</ul></div>\n              {mid}\n'
             f'              <div class="v-col after"><h4>{labels[1]}</h4><ul>{la}</ul></div>\n            </div>')
    return wrap('versus', one, inner, note)

# ---------------- integración (idempotente) ----------------
GL_RE = re.compile(r'<span class="gl" tabindex="0">(.*?)<span class="gl-def" role="note">.*?</span></span>', re.S)
VIS_RE = re.compile(r'<!--vis-->.*?<!--/vis-->\s*', re.S)

def strip(t):
    t = VIS_RE.sub('', t)
    t = GL_RE.sub(r'\1', t)
    return t

def in_tag(t, i):
    return t.rfind('<', 0, i) > t.rfind('>', 0, i)

def glossary(t, terms):
    m = re.search(r'<section id="(actos|ruta)">', t)
    start = m.start()
    for term, d in terms:
        pos = start
        while True:
            i = t.find(term, pos)
            if i < 0:
                raise SystemExit(f'termino no encontrado: {term}')
            ls = t.rfind('\n', 0, i) + 1
            line = t[ls:t.find('\n', i)]
            if in_tag(t, i) or 'acto-title"' in line or 'acto-teaser"' in line:
                pos = i + 1; continue
            break
        d = d.replace('"', '&quot;')
        t = t[:i] + f'<span class="gl" tabindex="0">{term}<span class="gl-def" role="note">{d}</span></span>' + t[i + len(term):]
    return t

def integrate(t, country, depth='../../'):
    # cabecera
    t = re.sub(r'<!--vis-head-->.*?<!--/vis-head-->\n?', '', t, flags=re.S)
    head = f'<!--vis-head--><link rel="stylesheet" href="{depth}assets/vis.css">\n<style>{TOKENS[country]}</style><!--/vis-head-->\n'
    t = t.replace('</head>', head + '</head>', 1)
    if country == 'corea' and 'data-num=' not in t:
        t = t.replace('<html lang="es">', '<html lang="es" data-num="eu">', 1)
    # script compartido al final
    t = re.sub(r'<!--vis-js--><script src="[^"]*vis\.js"></script><!--/vis-js-->\n?', '', t)
    t = t.replace('</body>', f'<!--vis-js--><script src="{depth}assets/vis.js"></script><!--/vis-js-->\n</body>', 1)
    # ganchos del acordeón
    if 'playVis' not in t:
        a = """    acto.querySelector('.acto-toggle').textContent = '－';
    gsap.to(acto.querySelector('.acto-body'), {
      height: 'auto', opacity: 1, duration: reduceMotion ? 0 : 0.65, ease: 'power1.inOut',
      onUpdate: function(){ ScrollTrigger.update(); },
      onComplete: function(){ ScrollTrigger.refresh(); }
    });"""
        a2 = """    acto.querySelector('.acto-toggle').textContent = '－';
    gsap.to(acto.querySelector('.acto-body'), {
      height: 'auto', opacity: 1, duration: reduceMotion ? 0 : 0.65, ease: 'power1.inOut',
      onUpdate: function(){ ScrollTrigger.update(); },
      onComplete: function(){ acto.querySelector('.acto-body').style.overflow = 'visible'; ScrollTrigger.refresh(); }
    });
    if(window.playVis) setTimeout(function(){ window.playVis(acto); }, reduceMotion ? 0 : 60);"""
        t = t.replace("height: 'auto', opacity: 1, duration: reduceMotion ? 0 : 0.7,", "height: 'auto', opacity: 1, duration: reduceMotion ? 0 : 0.65,")
        if a not in t:  # variante: duration en línea aparte y 0.7
            t = t.replace("height: 'auto', opacity: 1,\n      duration: reduceMotion ? 0 : 0.7, ease", "height: 'auto', opacity: 1, duration: reduceMotion ? 0 : 0.65, ease")
        assert a in t, 'openActo no coincide'
        t = t.replace(a, a2)
        b = """    acto.querySelector('.acto-toggle').textContent = '＋';
    gsap.to("""
        assert b in t, 'closeActo no coincide'
        t = t.replace(b, """    acto.querySelector('.acto-toggle').textContent = '＋';
    acto.querySelector('.acto-body').style.overflow = 'hidden';
    gsap.to(""")
        c = """    acto.addEventListener('click', function(){
      var wasActive"""
        assert c in t, 'click no coincide'
        t = t.replace(c, """    acto.addEventListener('click', function(e){
      if(e.target.closest('.acto-body')) return;
      var wasActive""")
        d = "gsap.set(firstActive, {height:'auto', opacity:1});"
        assert d in t, 'firstActive no coincide'
        t = t.replace(d, "gsap.set(firstActive, {height:'auto', opacity:1, overflow:'visible'});")
    return t

def apply(path, country, visuals, terms=(), depth='../../'):
    t = open(path, encoding='utf8').read()
    t = strip(t)
    parts = t.split('<div class="acto-body">')
    assert len(parts) - 1 == len(visuals), f'{path}: {len(parts)-1} actos, {len(visuals)} visuales'
    t = t
    t = glossary(t, terms) if terms else t
    parts = t.split('<div class="acto-body">')
    for i, v in enumerate(visuals, 1):
        parts[i] = '\n        ' + v + parts[i].lstrip('\n ')
    t = '<div class="acto-body">'.join(parts)
    t = integrate(t, country, depth)
    open(path, 'w', encoding='utf8').write(t)
