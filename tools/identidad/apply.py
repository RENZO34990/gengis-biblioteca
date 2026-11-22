"""Aplica la capa de identidad por pais (assets/identidad.css + identidad.js) a los cuadernos.
Idempotente. Excluye baules de fuentes y el cuaderno especial BTS. Uso: python3 tools/identidad/apply.py"""
import re,glob,os
ROOT=os.path.join(os.path.dirname(__file__),'..','..','docs')
PAIS={'japon':'jp','china':'cn','corea':'kr'}
SKIP={'fuentes','bts-hallyu'}
n=0
for pais,code in PAIS.items():
    for f in sorted(glob.glob(os.path.join(ROOT,pais,'*','index.html'))):
        if os.path.basename(os.path.dirname(f)) in SKIP: continue
        h=open(f,encoding='utf-8').read(); o=h
        if '<!--id-head-->' not in h:
            h=re.sub(r'<html lang="es"( data-num="eu")?( data-pais="\w+")?>',lambda m:f'<html lang="es"{m.group(1) or ""} data-pais="{code}">',h,count=1)
            a='<!--vis-head--><link rel="stylesheet" href="../../assets/vis.css">'
            assert a in h,f
            h=h.replace(a,a+'<!--id-head--><link rel="stylesheet" href="../../assets/identidad.css"><!--/id-head-->',1)
            b='<!--vis-js--><script src="../../assets/vis.js"></script><!--/vis-js-->'
            assert b in h,f
            h=h.replace(b,b+'<!--id-js--><script src="../../assets/identidad.js" defer></script><!--/id-js-->',1)
        if h!=o: open(f,'w',encoding='utf-8').write(h); n+=1
print('cuadernos actualizados:',n)
