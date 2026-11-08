#!/usr/bin/env python3
"""Transición entre cuadernos consecutivos (View Transitions entre páginas).
El título nativo del enlace «anterior/siguiente» se convierte en el título del héroe del otro cuaderno.
Solo dentro de cada país. Idempotente. Uso: python3 tools/vt/apply_vt.py"""
import re, glob, os, sys
ROOT=os.path.join(os.path.dirname(__file__),'..','..','docs')
MARK='TRANSICIÓN ENTRE CUADERNOS'
EXCLUDE={'fuentes','bts-hallyu'}
CSS='''  /* ---------- TRANSICIÓN ENTRE CUADERNOS (piloto) ---------- */
  @view-transition{navigation:auto;}
  ::view-transition-group(nb-title){animation-duration:.8s; animation-timing-function:cubic-bezier(.77,0,.175,1);}
  ::view-transition-old(root),::view-transition-new(root){animation-duration:.45s;}
  @media (prefers-reduced-motion:reduce){@view-transition{navigation:none;}}
'''
JS='''<script>
/* Transición entre cuadernos consecutivos: el título del enlace "siguiente/anterior" se convierte en el título del héroe */
(function(){
  if(!('PageSwapEvent' in window)) return;
  window.addEventListener('pageswap',function(e){
    if(!e.viewTransition||!e.activation||!e.activation.entry) return;
    var to=new URL(e.activation.entry.url).pathname, t=null;
    document.querySelectorAll('.nav-adjacent a').forEach(function(a){ if(new URL(a.href).pathname===to) t=a.querySelector('.nb-cn'); });
    if(t){ t.style.viewTransitionName='nb-title'; } else { e.viewTransition.skipTransition(); }
  });
  window.addEventListener('pagereveal',function(e){
    if(!e.viewTransition) return;
    var h=document.querySelector('h1.title-cn,h1.title-jp,h1.title-kr'); if(!h) return;
    h.style.viewTransitionName='nb-title';
    e.viewTransition.finished.finally(function(){ h.style.viewTransitionName=''; });
  });
})();
</script>
'''
def rd(p): return open(p,encoding='utf-8').read()
def h1_text(slugdir):
    m=re.search(r'<h1 class="title-(?:cn|jp|kr)">(.*?)</h1>',rd(os.path.join(slugdir,'index.html')),re.S)
    return re.split(r'<',m.group(1))[0].strip() if m else None
def wrap_ttl(inner,country,target_dir):
    if 'nb-cn' in inner: return inner
    arrow=re.match(r'^(<span class="ttl-arrow">[^<]*</span>)(.*)$',inner,re.S)
    lead='';body=inner
    if arrow: lead,body=arrow.group(1),arrow.group(2)
    else:
        m=re.match(r'^([←‹]\s*)(.*)$',inner,re.S)
        if m: lead,body=m.group(1),m.group(2)
    if country=='japon':
        k=h1_text(target_dir)
        if not k: return inner
        return f'{lead}<span class="nb-cn">{k}</span> {body}'
    m=re.match(r'^([^A-Za-z←→<]+?)(\s+[A-Za-z].*)$',body.strip(),re.S)
    if not m: return inner
    trail=''
    return f'{lead}<span class="nb-cn">{m.group(1).strip()}</span>{m.group(2)}'
n=0
for country in ('china','japon','corea'):
    for f in sorted(glob.glob(f'{ROOT}/{country}/*/index.html')):
        slug=f.split('/')[-2]
        if slug in EXCLUDE: continue
        s=rd(f)
        had=MARK in s
        def fix(m):
            href=m.group(1)
            mm=re.match(r'\.\./([a-z0-9-]+)/index\.html$',href)
            if not mm or mm.group(1) in EXCLUDE: return m.group(0)
            tdir=os.path.join(ROOT,country,mm.group(1))
            return m.group(0).replace(m.group(2),wrap_ttl(m.group(2),country,tdir),1)
        s2=re.sub(r'<a\s+(?:class="[^"]*"\s+)?href="([^"]+)">(?:(?!</a>).)*?<span class="ttl">(.*?)</span>\s*</a>',fix,s,flags=re.S)
        if had:
            if s2!=s: open(f,'w',encoding='utf-8').write(s2); n+=1
            continue
        s2,c=re.subn(r"(\.from\('h1\.title-(?:cn|jp|kr)', \{) opacity: 0, ",r"\1 ",s2)
        if c!=1: print('AVISO h1 tween',f,c)
        if 'nb-cn' not in s2: print('SIN ENLACES',f); 
        i=s2.index('</style>'); s2=s2[:i]+CSS+s2[i:]
        i=s2.index('</head>'); s2=s2[:i]+JS+s2[i:]
        open(f,'w',encoding='utf-8').write(s2); n+=1
print('páginas modificadas:',n)
