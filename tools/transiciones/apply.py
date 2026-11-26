"""Instala assets/transiciones.js (humo y puerta entre paginas) en el portal y en todos los cuadernos.
Va justo tras <meta charset>, sin defer, para que la pagina de llegada nazca cubierta. Idempotente.
Uso: python3 tools/transiciones/apply.py"""
import re,glob,os
ROOT=os.path.normpath(os.path.join(os.path.dirname(__file__),'..','..','docs'))
n=0
for f in sorted(glob.glob(os.path.join(ROOT,'**','index.html'),recursive=True)):
    h=open(f,encoding='utf-8').read()
    if '<!--tv-->' in h: continue
    rel=os.path.relpath(os.path.join(ROOT,'assets'),os.path.dirname(f)).replace(os.sep,'/')
    tag=f'<!--tv--><script src="{rel}/assets/transiciones.js" data-ink="#161310"></script><!--/tv-->'.replace('/assets/','/',1) if False else f'<!--tv--><script src="{rel}/transiciones.js" data-ink="#161310"></script><!--/tv-->'
    m=re.search(r'<meta charset="[^"]*"\s*/?>',h,re.I)
    if not m: print('sin charset:',f); continue
    h=h[:m.end()]+'\n'+tag+h[m.end():]
    open(f,'w',encoding='utf-8').write(h); n+=1
print('paginas actualizadas:',n)
