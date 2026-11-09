#!/usr/bin/env python3
"""Cifras del héroe como lista editorial vertical que llevan al pasaje donde se explican.
Cada cifra busca su número (y palabras de su etiqueta) en los actos del cuaderno; si no lo halla,
lleva al inicio del primer acto (donde empieza el tema). Idempotente. Escribe tools/stats/mapeo.md.
Uso: python3 tools/stats/link_stats.py"""
import re, glob, os, sys, unicodedata
from html.parser import HTMLParser
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','docs')
MARK='/* ---------- HERO: cifras como lista vertical con destino ---------- */'
EXCLUDE={'fuentes','bts-hallyu'}
THEME={ # borde, acento barra/flecha, tinte hover, color de destello
 'japon':('var(--line)','var(--vermillion)','rgba(161,61,44,.05)','161,61,44'),
 'china':('rgba(242,239,233,.2)','var(--gold)','rgba(242,239,233,.07)','158,43,37'),
 'corea':('rgba(245,243,238,.2)','var(--terracota-light)','rgba(245,243,238,.07)','181,98,59'),
}
def css(country,maxlen=4):
    br,ac,hv,fl=THEME[country]
    long=maxlen>6
    col='5.4rem' if not long else f'{max(5.4,round(0.72*maxlen+0.6,1))}rem'
    nfs='1.75rem' if not long else '1.5rem'
    mob='grid-template-columns:4.2rem 1fr; column-gap:1.1rem;' if not long else 'grid-template-columns:1fr; row-gap:.35rem;'
    return f'''  {MARK}
  .hero .hero-stats{{display:block; max-width:560px; margin-top:3rem; border-top:1px solid {br};}}
  .hero .hero-stats > div{{position:relative; display:grid; grid-template-columns:{col} 1fr; align-items:center; column-gap:1.6rem; margin:0; padding:1.05rem 2.4rem 1.05rem 1.1rem; border-right:none; border-bottom:1px solid {br}; transition:background-color .35s cubic-bezier(0.23,1,0.32,1), padding-left .35s cubic-bezier(0.23,1,0.32,1);}}
  .hero .hero-stats > div:last-child{{padding-right:2.4rem;}}
  .hero .hero-stats .num{{font-size:{nfs}; line-height:1; width:max-content;}}
  .hero .hero-stats .lbl{{margin:0; max-width:none; font-size:.82rem; line-height:1.5;}}
  .hero .hero-stats > div::before{{content:""; position:absolute; left:0; top:.9rem; bottom:.9rem; width:2px; background:{ac}; transform-origin:top; transform:scaleY(0); animation:statBar .9s cubic-bezier(0.23,1,0.32,1) both;}}
  .hero .hero-stats > div:nth-child(1)::before{{animation-delay:1.5s;}}
  .hero .hero-stats > div:nth-child(2)::before{{animation-delay:1.7s;}}
  .hero .hero-stats > div:nth-child(3)::before{{animation-delay:1.9s;}}
  .hero .hero-stats > div:hover{{background:{hv}; padding-left:1.4rem;}}
  .hero .hero-stats > div[data-go]{{cursor:pointer;}}
  .hero .hero-stats > div[data-go]::after{{content:"\\2193"; position:absolute; right:1rem; top:50%; transform:translate(-4px,-50%); opacity:0; font-family:'IBM Plex Mono', monospace; font-size:.95rem; color:{ac}; transition:opacity .3s, transform .3s cubic-bezier(0.23,1,0.32,1);}}
  .hero .hero-stats > div[data-go]:hover::after,.hero .hero-stats > div[data-go]:focus-visible::after{{opacity:1; transform:translate(0,-50%);}}
  .hero .hero-stats > div[data-go]:focus-visible{{outline:2px solid {ac}; outline-offset:2px;}}
  .hero .hero-stats > div[data-go]:active{{transform:scale(0.985);}}
  [id^="go-"]{{scroll-margin-top:110px;}}
  .go-flash{{animation:goFlash 2s cubic-bezier(0.23,1,0.32,1) both;}}
  @keyframes statBar{{to{{transform:scaleY(1);}}}}
  @keyframes goFlash{{0%{{background-color:rgba({fl},.14); box-shadow:0 0 0 8px rgba({fl},.14);}} 100%{{background-color:rgba({fl},0); box-shadow:0 0 0 8px rgba({fl},0);}}}}
  @media (prefers-reduced-motion:reduce){{
    .hero .hero-stats > div::before{{animation:none; transform:scaleY(1);}}
    .hero .hero-stats > div{{transition:none;}}
    .go-flash{{animation:none; outline:2px solid rgb({fl}); outline-offset:6px;}}
  }}
  @media (max-width:560px){{
    .hero .hero-stats > div{{{mob}}}
    .hero .hero-stats .num{{font-size:1.4rem;}}
  }}
'''
JS='''  // Cifras del héroe: llevan al pasaje donde se explican (abre el acto si hace falta)
  document.querySelectorAll('.hero-stats [data-go]').forEach(function(row){
    function go(){
      var el = document.getElementById(row.getAttribute('data-go')); if(!el) return;
      var acto = el.closest('.acto'), wait = 0;
      if(acto && !acto.classList.contains('active')){
        document.querySelectorAll('.acto.active').forEach(function(a){ a.classList.remove('active'); closeActo(a); });
        acto.classList.add('active'); openActo(acto); wait = reduceMotion ? 60 : 420;
      }
      setTimeout(function(){
        if(window.__lenis){ window.__lenis.scrollTo(el, { offset: -110, duration: 1.0 }); }
        else { el.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' }); }
        el.classList.remove('go-flash'); void el.offsetWidth;
        setTimeout(function(){ el.classList.add('go-flash'); }, reduceMotion ? 0 : 300);
      }, wait);
    }
    row.addEventListener('click', go);
    row.addEventListener('keydown', function(e){ if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); go(); } });
  });

'''
ANCHOR="  if(!reduceMotion){\n    actos.forEach(function(acto){"
def norm(t): return ''.join(c for c in unicodedata.normalize('NFD',t.lower()) if unicodedata.category(c)!='Mn')
class P(HTMLParser):
    def __init__(s,src):
        super().__init__(convert_charrefs=True); s.src=src
        s.lines=[0]
        for l in src.split('\n'): s.lines.append(s.lines[-1]+len(l)+1)
        s.stack=[]; s.cands=[]; s.first_acto=None; s.in_hero=False
    def off(s): l,c=s.getpos(); return s.lines[l-1]+c
    def handle_starttag(s,tag,attrs):
        if tag in('br','img','meta','link','input','hr'): return
        a=dict(attrs); cls=(a.get('class') or '').split()
        o=s.off(); txt=s.get_starttag_text()
        s.stack.append(dict(tag=tag,cls=cls,id=a.get('id'),start=o,tlen=len(txt),text=[],gl=0))
        if tag=='div' and 'acto' in cls and 'data-i' in a and s.first_acto is None:
            s.first_acto=dict(start=o,tlen=len(txt),id=a.get('id'),tag=tag)
    def handle_data(s,d):
        if not s.stack: return
        if any(e['gl'] or 'gl-def' in e['cls'] for e in s.stack): return
        for e in s.stack: e['text'].append(d)
    def handle_endtag(s,tag):
        for i in range(len(s.stack)-1,-1,-1):
            if s.stack[i]['tag']==tag:
                e=s.stack.pop(i)
                for _ in s.stack[i:]: pass
                s.stack=s.stack[:i]
                inbody=any('acto-body' in x['cls'] for x in s.stack)
                kind=None
                if tag=='p' and 'acto-teaser' not in e['cls'] and inbody: kind='p'
                elif tag=='div' and ('chart-block' in e['cls'] or 'v-stat' in e['cls']) and inbody: kind='blk'
                elif tag=='li' and inbody: kind='li'
                if kind: s.cands.append(dict(e,text=' '.join(''.join(e['text']).split())))
                break
def variants(num):
    m=re.search(r'(?<!\d)(?:1[5-9]\d\d|20\d\d)(?!\d)',num) or re.search(r'\d[\d.,]*\d|\d',num)
    if not m: return []
    t=m.group(0); v={t}
    v.add(t.replace('.',',')); v.add(t.replace(',','.'))
    d=re.sub(r'[.,]','',t)
    if len(d)>=4 and re.fullmatch(r'\d{1,3}([.,]\d{3})+',t): v|={d, t.replace(',',' ').replace('.',' ')}
    return sorted(v,key=len,reverse=True)
def score(c,vs,kws):
    t=c['text']; hit=False
    for v in vs:
        if re.search(r'(?<![\d.,])'+re.escape(v)+r'(?!\d|[.,]\d)',t): hit=True; break
    if not hit: return 0
    n=norm(t); return 1+min(3,sum(1 for k in kws if k in n))
def process(f,country):
    s=open(f,encoding='utf-8').read()
    if MARK in s: return None
    m=re.search(r'<div class="hero-stats">(.*?)</header>',s,re.S)
    cells=list(re.finditer(r'<div><span class="num">(.*?)</span><span class="lbl">(.*?)</span></div>',m.group(1))) if m else []
    if not cells: return 'sin cifras'
    if ANCHOR not in s or 'function openActo(' not in s: return 'estructura distinta'
    p=P(s); p.feed(s)
    if not p.first_acto: return 'sin actos'
    edits=[]  # (pos, texto) inserciones
    ids={}; report=[]; n=0
    hs=m.start(1)
    for k,c in enumerate(cells):
        num=re.sub(r'<[^>]+>','',c.group(1)); lbl=re.sub(r'<[^>]+>','',c.group(2))
        vs=variants(num); kws=[w for w in re.findall(r'[a-z]{5,}',norm(lbl))]
        best=None;bs=0
        for cd in p.cands:
            sc=score(cd,vs,kws)
            if sc>bs: best,bs=cd,sc
        if best is None:
            tid='go-inicio'; why='inicio del tema (no se halló la cifra exacta)'
            if tid not in ids: ids[tid]=p.first_acto
        else:
            key=best['start']
            if key in ids.get('_m',{}): tid=ids['_m'][key]
            else:
                n+=1; tid=best['id'] or f'go-{n}'
                ids.setdefault('_m',{})[key]=tid
                if not best['id']: ids[tid]=best
            why=f"«{best['text'][:70]}…» (puntaje {bs})"
        report.append((num,lbl,tid,why))
        a=hs+c.start()
        edits.append((a+len('<div'),f' data-go="{tid}" role="link" tabindex="0" aria-label="Ir al pasaje donde se explica: {lbl.replace(chr(34),"")}"'))
    for tid,e in ids.items():
        if tid=='_m' or e.get('id'): continue
        edits.append((e['start']+len('<'+e['tag']),f' id="{tid}"'))
    for pos,t in sorted(edits,key=lambda x:-x[0]): s=s[:pos]+t+s[pos:]
    i=s.index('</style>'); maxlen=max(len(re.sub(r'<[^>]+>','',c.group(1))) for c in cells)
    s=s[:i]+css(country,maxlen)+s[i:]
    i=s.index(ANCHOR); s=s[:i]+JS+s[i:]
    open(f,'w',encoding='utf-8').write(s)
    return report
out=['# Mapeo de cifras del héroe → destino\n','Revisar: «inicio» = no se halló la cifra exacta, lleva al inicio del primer acto.\n']
ok=ini=0; skipped=[]
for country in ('china','japon','corea'):
    for f in sorted(glob.glob(f'{ROOT}/{country}/*/index.html')):
        slug=f.split('/')[-2]
        if slug in EXCLUDE: continue
        r=process(f,country)
        if r is None: continue
        if isinstance(r,str): skipped.append((country,slug,r)); continue
        out.append(f'\n## {country} · {slug}\n')
        for num,lbl,tid,why in r:
            out.append(f'- **{num}** — {lbl} → `{tid}`: {why}\n')
            if tid=='go-inicio': ini+=1
            else: ok+=1
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'mapeo.md'),'w',encoding='utf-8').write(''.join(out))
print('cifras con destino exacto:',ok,'· al inicio del tema:',ini,'· páginas omitidas:',skipped)
