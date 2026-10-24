import sys, re, html, urllib.parse, os
sys.path.insert(0, os.path.dirname(__file__))
import importlib
COUNTRY = sys.argv[1] if len(sys.argv) > 1 else 'china'
_d = importlib.import_module(COUNTRY + '_data')
S, CUADERNOS, URL = _d.S, _d.CUADERNOS, getattr(_d, 'URL', {})
CONF = {
 'china': dict(hfg='var(--paper)', hdek='rgba(242,239,233,.9)', hkj='rgba(242,239,233,.06)', dw='700', nombre='China', dir='china', acc='--vermillion', acc2='--vermillion-deep', hero_eye='var(--gold)',
   root=':root{--paper:#F2EFE9; --paper-warm:#E9E2D4; --ink:#1A1A1A; --ink-soft:#544F47; --accent:#9E2B25; --accent-deep:#7A211C; --gold:#C9A63E; --hero-eye:#C9A63E; --line:rgba(26,26,26,0.14);}',
   grad='linear-gradient(155deg,#7A211C 0%,#9E2B25 62%,#8A2620 100%)',
   fonts='family=Noto+Serif+SC:wght@500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500',
   body="'Hanken Grotesk'", disp="'Noto Serif SC'", zh='参考文献', title='参考文献 — Baúl de fuentes · China', article='los 17 cuadernos de China', serie='la serie China', nota=''),
 'corea': dict(hfg='var(--paper)', hdek='rgba(242,239,233,.9)', hkj='rgba(242,239,233,.06)', dw='700', nombre='Corea', dir='corea', acc='--terracota-deep', acc2='--terracota', hero_eye='#FAE6D9',
   root=':root{--paper:#F5F3EE; --paper-warm:#EAE6DC; --ink:#1C1C1C; --ink-soft:#5C5A54; --accent:#8E4B2C; --accent-deep:#6F3A22; --gold:#B5623B; --hero-eye:#FAE6D9; --line:rgba(28,28,28,0.13);}',
   grad='linear-gradient(160deg,#16201C 0%,#4F6F61 68%,#3E5A4E 100%)',
   fonts='family=Gothic+A1:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500',
   body="'Gothic A1'", disp="'Gothic A1'", zh='참고문헌', title='참고문헌 — Baúl de fuentes · Corea', article='los cuadernos de Corea', serie='la serie Corea',
   nota='<p><strong>Asignación provisional.</strong> El baúl de Corea reúne los catálogos económico y político. Los cuadernos aparecen asignados <em>por tema</em>, no porque se haya confirmado su uso en cada texto; las fuentes sin cuaderno esperan asignación.</p>'),
 'japon': dict(hfg='var(--ink)', hdek='var(--ink-soft)', hkj='rgba(43,42,40,.06)', dw='500', nombre='Japón', dir='japon', acc='--vermillion', acc2='--vermillion-deep', hero_eye='#A13D2C',
   root=':root{--paper:#F5F1E8; --paper-warm:#EDE6D6; --ink:#2B2A28; --ink-soft:#5A5650; --accent:#A13D2C; --accent-deep:#7E2E20; --gold:#A8863C; --hero-eye:#A13D2C; --line:rgba(43,42,40,0.14);}',
   grad='linear-gradient(160deg,#EDE6D6 0%,#F5F1E8 70%,#EFE8D8 100%)',
   fonts='family=Zen+Kaku+Gothic+New:wght@300;400;500;700&family=Shippori+Mincho:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500',
   body="'Zen Kaku Gothic New'", disp="'Shippori Mincho'", zh='参考文献', title='参考文献 — Baúl de fuentes · Japón', article='los cuadernos de Japón', serie='la serie Japón',
   nota='<p><strong>Asignación provisional.</strong> El baúl de Japón reúne los catálogos político y económico. Los cuadernos aparecen asignados <em>por tema</em>, no porque se haya confirmado su uso en cada texto; las fuentes sin cuaderno esperan asignación.</p>'),
}
CF = CONF[COUNTRY]
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'docs', CONF[COUNTRY]['dir']))
esc = html.escape
NAME = {k: (n, z) for k, n, z in CUADERNOS}
TIER = {'Académico':1,'Institucional':1,'Libro':1,'Oficial':2,'Análisis':2,'Prensa':2,'Referencia':3,'Otro':3}
LENTE = {'E':'Economía','P':'Política','EP':'Economía y política'}
TIPOS = ['Académico','Institucional','Libro','Oficial','Análisis','Prensa','Referencia','Otro']

def sid(i): return 'f%02d' % (i+1)
srcs = sorted(range(len(S)), key=lambda i: S[i][0].lower().lstrip('"'))

def q(r):
    return 'https://www.google.com/search?q=' + urllib.parse.quote_plus('"%s" %s' % (r[0], r[1]))

# ------------------------------------------------------------ página baúl
def entry(n, i):
    t, via, tipo, lente, cuads, aviso = S[i]
    chips = ''.join('<a class="cq" href="../%s/index.html">%s</a>' % (k, esc(NAME[k][0])) for k in cuads)
    avi = '<span class="aviso">%s</span>' % esc(aviso) if aviso else ''
    u = URL.get(t)
    ab = ''
    if u:
        ab = '<a href="%s" target="_blank" rel="noopener">%s ↗</a>' % (esc(u[1], quote=True), 'Abrir fuente' if u[0] == 'd' else 'Sitio de la fuente')
    if not cuads: chips = '<span class="cq cq0">Aún sin cuaderno asignado</span>'
    return ('<li class="src" data-tipo="%s" data-lente="%s" data-c="%s" data-t="%s">'
            '<span class="n">%02d</span><div class="body">'
            '<p class="t">%s</p><p class="m">%s<span class="tp tp-%d">%s</span>%s</p>'
            '<p class="c">%s</p>'
            '<p class="a">%s<a href="%s" target="_blank" rel="noopener">Buscar en la web ↗</a>'
            '<button type="button" class="copy" data-cita="%s">Copiar referencia</button></p>'
            '</div></li>') % (
        esc(tipo), lente, ' '.join(cuads), esc((t + ' ' + via).lower()), n,
        esc(t), (esc(via) + ' · ') if via else '', TIER[tipo], esc(tipo), (' · ' + avi) if avi else '',
        chips, ab, esc(q(S[i]), quote=True), esc((t + (' — ' + via if via else '')), quote=True))

items = ''.join(entry(n + 1, i) for n, i in enumerate(srcs))
opts = ''.join('<option value="%s">%s</option>' % (k, esc(n)) for k, n, z in CUADERNOS)
tipo_chips = ''.join('<button type="button" class="chip" data-tipo="%s">%s</button>' % (t, t) for t in TIPOS)

PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@</title>
<meta name="description" content="Baúl bibliográfico de @@SERIE@@ de la Biblioteca Nalanda: todas las fuentes consultadas, filtrables por cuaderno y tipo.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?@@FONTS@@&display=swap" rel="stylesheet">
<style>
  @@ROOT@@
  *{box-sizing:border-box;}
  body{margin:0; background:var(--paper); color:var(--ink); font-family:@@BODY@@,sans-serif; font-size:17px; line-height:1.7;}
  ::selection{background:var(--accent); color:var(--paper);}
  a{color:var(--ink);}
  .eyebrow{font-family:'IBM Plex Mono',monospace; letter-spacing:.1em; text-transform:uppercase; font-size:.72rem; color:var(--hero-eye); font-weight:500;}
  .top-return{position:fixed; top:1.4rem; left:1.4rem; z-index:50; background:var(--paper); color:var(--ink-soft); border:1px solid var(--line); padding:.5rem 1rem; font-family:'IBM Plex Mono',monospace; font-size:.72rem; text-decoration:none; display:inline-flex; gap:.5rem; transition:border-color .3s, color .3s;}
  .top-return:hover{border-color:var(--gold); color:var(--ink);}
  header.hero{position:relative; overflow:hidden; padding:15vh 8vw 9vh; background:@@GRAD@@; color:@@HFG@@;}
  .hero-kanji{position:absolute; right:5vw; top:50%; transform:translateY(-50%); font-family:@@DISP@@,serif; font-weight:@@DW@@; font-size:clamp(5rem,13vw,10rem); color:@@HKJ@@; user-select:none; line-height:1; white-space:nowrap;}
  .hero-in{position:relative; max-width:1080px; margin:0 auto;}
  .hero-rule{width:48px; height:2px; background:var(--hero-eye); margin-bottom:1.6rem;}
  h1{font-family:@@DISP@@,serif; font-weight:@@DW@@; font-size:clamp(2rem,4.6vw,3.2rem); line-height:1.25; margin:.4rem 0 .6rem; max-width:620px;}
  .dek{max-width:600px; color:@@HDEK@@; font-size:1.05rem; line-height:1.85; margin:0;}
  main{max-width:1080px; margin:0 auto; padding:5vh 8vw 8vh;}
  .tools{position:sticky; top:0; z-index:20; background:var(--paper); border-bottom:1px solid var(--line); padding:1rem 0 .9rem; margin-bottom:1.6rem;}
  .row{display:flex; flex-wrap:wrap; gap:.7rem; align-items:center;}
  .row + .row{margin-top:.7rem;}
  input[type=search], select{font-family:'IBM Plex Mono',monospace; font-size:.8rem; padding:.55rem .8rem; border:1px solid var(--line); background:#fff8; color:var(--ink); border-radius:0; min-width:0;}
  input[type=search]{flex:1 1 240px;}
  select{flex:0 1 270px;}
  input:focus-visible, select:focus-visible, button:focus-visible, a:focus-visible{outline:2px solid var(--accent); outline-offset:2px;}
  .chip{font-family:'IBM Plex Mono',monospace; font-size:.72rem; padding:.3rem .7rem; border:1px solid var(--line); background:transparent; color:var(--ink-soft); cursor:pointer; transition:all .25s;}
  .chip:hover{border-color:var(--gold); color:var(--ink);}
  .chip[aria-pressed=true]{background:var(--accent); border-color:var(--accent); color:var(--paper);}
  .lbl{font-family:'IBM Plex Mono',monospace; font-size:.7rem; color:var(--ink-soft); text-transform:uppercase; letter-spacing:.06em; margin-right:.2rem;}
  .count{font-family:'IBM Plex Mono',monospace; font-size:.76rem; color:var(--ink-soft); margin:0 0 1rem;}
  ol.list{list-style:none; margin:0; padding:0; border-top:1px solid var(--line);}
  .src{display:grid; grid-template-columns:3rem 1fr; gap:1rem; padding:1.4rem 0; border-bottom:1px solid var(--line);}
  .src[hidden]{display:none;}
  .n{font-family:@@DISP@@,serif; font-weight:@@DW@@; font-size:1.1rem; color:var(--accent); opacity:.45; line-height:1.5;}
  .t{margin:0; font-weight:600; font-size:1.02rem; line-height:1.45; max-width:760px;}
  .m{margin:.3rem 0 0; font-family:'IBM Plex Mono',monospace; font-size:.76rem; color:var(--ink-soft); line-height:1.6;}
  .tp{color:var(--accent); font-weight:500;}
  .tp-3{color:#8A8478;}
  .aviso{color:var(--ink-soft); font-style:normal;}
  .c{margin:.7rem 0 0; display:flex; flex-wrap:wrap; gap:.4rem;}
  .cq{font-family:'IBM Plex Mono',monospace; font-size:.68rem; color:var(--ink-soft); text-decoration:none; border:1px solid var(--line); padding:.15rem .55rem; transition:all .25s;}
  .cq0{border-style:dashed; opacity:.8;}
  .cq:hover{border-color:var(--accent); color:var(--accent);}
  .a{margin:.7rem 0 0; display:flex; flex-wrap:wrap; gap:1.2rem; font-family:'IBM Plex Mono',monospace; font-size:.72rem;}
  .a a{color:var(--accent); text-decoration:none; border-bottom:1px solid currentColor; padding-bottom:1px;}
  .copy{font:inherit; background:none; border:none; padding:0; color:var(--ink-soft); cursor:pointer; border-bottom:1px solid var(--line);}
  .copy:hover{color:var(--ink);}
  .empty{display:none; padding:3rem 0; color:var(--ink-soft);}
  .legend{margin-top:3.4rem; padding-top:2rem; border-top:1px solid var(--line); font-size:.9rem; color:var(--ink-soft); max-width:700px;}
  .legend p{margin:0 0 .8rem;}
  .legend strong{color:var(--ink);}
  footer{padding:3rem 8vw; text-align:center; font-family:'IBM Plex Mono',monospace; font-size:.74rem; color:var(--ink-soft); border-top:1px solid var(--line);}
  @media (max-width:640px){ body{font-size:16px;} .src{grid-template-columns:2.2rem 1fr; gap:.7rem;} header.hero{padding:13vh 6vw 7vh;} main{padding:4vh 6vw 6vh;} .top-return{left:.8rem; top:.8rem;} select{flex:1 1 100%;} }
</style>
</head>
<body>
<a class="top-return" href="../../index.html"><span>←</span> Biblioteca Nalanda</a>
<header class="hero">
  <div class="hero-kanji" aria-hidden="true">@@ZH@@</div>
  <div class="hero-in">
    <div class="hero-rule"></div>
    <span class="eyebrow">Baúl de fuentes · @@NOMBRE@@</span>
    <h1>Fuentes de @@SERIE@@</h1>
    <p class="dek">Todo lo que sostiene @@ARTICLE@@, en un solo lugar. Busca por título, filtra por cuaderno o por tipo de fuente y copia la referencia para tus propios trabajos.</p>
  </div>
</header>
<main>
  <div class="tools" role="search">
    <div class="row">
      <input type="search" id="q" placeholder="Buscar por título o institución" aria-label="Buscar fuentes">
      <select id="cuad" aria-label="Filtrar por cuaderno"><option value="">Todos los cuadernos</option>@@OPTS@@</select>
    </div>
    <div class="row" id="tipos"><span class="lbl">Tipo</span>@@TIPOS@@</div>
    <div class="row" id="lentes"><span class="lbl">Lente</span>
      <button type="button" class="chip" data-lente="E">Economía</button>
      <button type="button" class="chip" data-lente="P">Política</button>
    </div>
  </div>
  <p class="count" id="count" aria-live="polite"></p>
  <ol class="list" id="list">@@ITEMS@@</ol>
  <p class="empty" id="empty">Ninguna fuente coincide con esos filtros.</p>
  <div class="legend">
    <p><strong>Cómo leer los tipos.</strong> <em>Académico</em> son artículos, documentos de trabajo y libros universitarios. <em>Institucional</em> reúne bancos centrales, organismos multilaterales y centros de investigación. <em>Oficial</em> son documentos del Estado o del Partido: documentan su posición, no la verifican. <em>Análisis</em> y <em>Prensa</em> son útiles para contexto y cifras recientes. <em>Referencia</em> (Wikipedia, cronologías) sirve para ubicarte; para citar, busca la fuente primaria que traen al pie.</p>
    <p><strong>Sobre los enlaces.</strong> Los títulos están como figuran en nuestro registro de investigación. «Abrir fuente» lleva al documento; «Sitio de la fuente» solo a la página general de quien lo publica, porque no tenemos aún el enlace exacto. «Buscar en la web» busca el título exacto. Algunas fuentes no traen todavía institución o autor.</p>
    @@NOTA@@<p>Curado por el equipo de Club Kongzhi UNMSM. Las fuentes metodológicas internas del equipo no se listan aquí.</p>
  </div>
</main>
<footer>Club Kongzhi UNMSM · <a href="../../index.html#departamento-de-investigacion" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">Departamento de Investigación</a> · Biblioteca Nalanda</footer>
<script>
(function(){
  var items=[].slice.call(document.querySelectorAll('.src'));
  var q=document.getElementById('q'), cuad=document.getElementById('cuad');
  var tipo='', lente='';
  var count=document.getElementById('count'), empty=document.getElementById('empty');
  function apply(){
    var s=q.value.trim().toLowerCase(), c=cuad.value, n=0;
    items.forEach(function(el){
      var ok=(!s||el.dataset.t.indexOf(s)>-1)
        &&(!c||(' '+el.dataset.c+' ').indexOf(' '+c+' ')>-1)
        &&(!tipo||el.dataset.tipo===tipo)
        &&(!lente||el.dataset.lente===lente||el.dataset.lente==='EP');
      el.hidden=!ok; if(ok) n++;
    });
    count.textContent=n+' de '+items.length+' fuentes';
    empty.style.display=n?'none':'block';
  }
  function chips(boxId,key,set){
    var box=document.getElementById(boxId);
    box.addEventListener('click',function(e){
      var b=e.target.closest('.chip'); if(!b) return;
      var v=b.dataset[key], on=b.getAttribute('aria-pressed')==='true';
      [].forEach.call(box.querySelectorAll('.chip'),function(x){x.setAttribute('aria-pressed','false');});
      if(!on) b.setAttribute('aria-pressed','true');
      set(on?'':v); apply();
    });
  }
  chips('tipos','tipo',function(v){tipo=v;});
  chips('lentes','lente',function(v){lente=v;});
  q.addEventListener('input',apply); cuad.addEventListener('change',apply);
  document.getElementById('list').addEventListener('click',function(e){
    var b=e.target.closest('.copy'); if(!b) return;
    var t=b.dataset.cita, done=function(){var o=b.textContent; b.textContent='Copiada ✓'; setTimeout(function(){b.textContent=o;},1400);};
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(done,function(){});}
    else{var ta=document.createElement('textarea'); ta.value=t; document.body.appendChild(ta); ta.select(); try{document.execCommand('copy'); done();}catch(_){} ta.remove();}
  });
  try{var p=new URLSearchParams(location.search).get('c'); if(p&&NAME_OK(p)) cuad.value=p;}catch(_){}
  function NAME_OK(v){return [].some.call(cuad.options,function(o){return o.value===v;});}
  apply();
})();
</script>
</body>
</html>
'''
os.makedirs(os.path.join(ROOT, 'fuentes'), exist_ok=True)
for k, v in dict(TITLE=CF['title'], SERIE=CF['serie'], FONTS=CF['fonts'], ROOT=CF['root'], HFG=CF['hfg'], HDEK=CF['hdek'], HKJ=CF['hkj'], DW=CF['dw'], BODY=CF['body'], GRAD=CF['grad'], DISP=CF['disp'], ZH=CF['zh'], NOMBRE=CF['nombre'], ARTICLE=CF['article'], NOTA=CF['nota']).items():
    PAGE = PAGE.replace('@@%s@@' % k, v)
open(os.path.join(ROOT, 'fuentes', 'index.html'), 'w').write(
    PAGE.replace('@@OPTS@@', opts).replace('@@TIPOS@@', tipo_chips).replace('@@ITEMS@@', items))

# ------------------------------------------------------------ secciones por cuaderno
CSS_MARK = '/* ---------- FUENTES (baúl) ---------- */'
CSS = CSS_MARK + '''
  .src-intro{font-size:.92rem; color:var(--ink-soft); max-width:640px;}
  .src-list{list-style:none; margin:1.4rem 0 0; padding:0; border-top:1px solid var(--line); max-width:720px;}
  .src-list li{padding:.85rem 0; border-bottom:1px solid var(--line);}
  .src-list .st{display:block; font-size:.95rem; font-weight:500; color:var(--ink); line-height:1.5;}
  .src-list .sm{display:block; margin-top:.2rem; font-family:'IBM Plex Mono',monospace; font-size:.72rem; color:var(--ink-soft);}
  .src-list .sm b{font-weight:500; color:var(@@ACC@@);}
  .src-all{display:inline-block; margin-top:1.4rem; font-family:'IBM Plex Mono',monospace; font-size:.8rem; color:var(@@ACC@@); text-decoration:none; border-bottom:1px solid var(@@ACC@@); padding-bottom:1px;}
  .src-all:hover{color:var(@@ACC2@@); border-color:var(@@ACC2@@);}
'''
def main_for(slug, k=6):
    rows = [(i, S[i]) for i in range(len(S)) if slug in S[i][4]]
    rows.sort(key=lambda x: (TIER[x[1][2]], len(x[1][4]), x[1][0].lower()))
    return rows[:k], len(rows)

tot = 0
for slug, nm, zh in CUADERNOS:
    p = os.path.join(ROOT, slug, 'index.html')
    h = open(p).read()
    top, n = main_for(slug)
    lis = ''.join('<li><span class="st">%s</span><span class="sm">%s<b>%s</b></span></li>' % (
        esc(r[0]), (esc(r[1]) + ' · ') if r[1] else '', esc(r[2])) for _, r in top)
    prov = (COUNTRY in ('corea', 'japon'))
    if n == 0:
        intro = 'Las fuentes de este cuaderno se irán añadiendo al baúl.'
        link = 'Abrir el baúl de fuentes de %s →' % CF['nombre']
    else:
        intro = ('Fuentes afines a este cuaderno, asignadas por tema: de lo más sólido a lo más contextual.' if prov and n > len(top) else
                 'Fuentes afines a este cuaderno, asignadas por tema.' if prov else
                 'Las fuentes principales de este cuaderno, de lo más sólido a lo más contextual.' if n > len(top) else
                 'Las fuentes consultadas para este cuaderno.')
        link = 'Ver las %d fuentes de este cuaderno en el baúl →' % n if n > len(top) else 'Abrir el baúl de fuentes de %s →' % CF['nombre']
    newsrc = ('<div class="sources">\n    <span class="eyebrow">Fuentes</span>\n'
              '    <p class="src-intro">%s Curado por el equipo de Club Kongzhi.</p>\n'
              '    %s\n'
              '    <a class="src-all" href="../fuentes/index.html?c=%s">%s</a>\n  </div>') % (intro, ('<ol class="src-list">%s</ol>' % lis) if lis else '', slug, link)
    h2, k = re.subn(r'<div class="sources">.*?</div>', lambda m: newsrc, h, count=1, flags=re.S)
    assert k == 1, slug
    if CSS_MARK not in h2:
        h2 = h2.replace('</style>', CSS.replace('@@ACC@@', CF['acc']).replace('@@ACC2@@', CF['acc2']) + '</style>', 1)
    open(p, 'w').write(h2)
    tot += 1
    print(slug, n, 'fuentes;', len(top), 'visibles')
print(len(S), 'fuentes únicas;', tot, 'cuadernos')
