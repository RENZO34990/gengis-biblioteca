"""Homogeneiza la composición de los cuadernos de Japón con la de China (idempotente)."""
import glob,os,re
REPO=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
MARK='/* ---------- Homogeneización con China ---------- */'
BLOCK=MARK+'''
  :root{ --vermillion-deep:#7E2E20; }
  body{ line-height:1.7; }
  header.hero{ min-height:96vh; padding:14vh 8vw 12vh; overflow:hidden; }
  .hero-kanji{ right:5vw; font-size:clamp(8rem, 22vw, 17rem); }
  h1.title-jp{ font-size:clamp(2.2rem, 5vw, 3.8rem); line-height:1.25; margin:.4rem 0 .5rem; }
  .title-romaji{ font-size:.85rem; margin-bottom:2rem; line-height:1.6; }
  .hero-dek{ font-size:1.08rem; max-width:560px; line-height:1.85; }
  .hero-stats{ margin-top:3.2rem; }
  .acto-body p{ line-height:1.85; }
  .flat-grid > div:not(:first-child){ padding-left:3rem; }
  .nav-adjacent > *:not(:first-child){ padding-left:3rem; }
  .acto-figure[hidden]{display:none;}
  .acto-figure{margin:1.8rem 0; border:1px solid var(--line); max-width:640px; background:var(--ink);}
  .acto-figure img{width:100%; display:block; filter:sepia(.12) contrast(1.03); opacity:.94;}
  .acto-figure figcaption{padding:.85rem 1.1rem; font-family:'IBM Plex Mono', monospace; font-size:.76rem; color:var(--ink-soft); border-top:1px solid var(--line); background:var(--paper);}
  .acto-figure figcaption .credit{display:block; margin-top:.3rem; color:#8A8478; font-size:.76rem;}
  .chart-block{margin:1.8rem 0; border-top:1px solid var(--line); padding-top:1.6rem; max-width:640px;}
  @media(max-width:820px){
    .flat-grid > div:not(:first-child){ padding-left:0; }
    .nav-adjacent > *:not(:first-child){ padding-left:0; }
    .nav-adjacent .next{ padding-left:0; }
    header.hero{ min-height:88vh; padding:12vh 7vw 10vh; }
  }
'''
def run(paths=None):
    paths=paths or sorted(glob.glob(os.path.join(REPO,'docs','japon','*','index.html')))
    n=0
    for p in paths:
        s=open(p,encoding='utf8').read()
        if MARK in s: continue
        i=s.index('</style>')
        # insertar antes del bloque TOKENS/vis si existe, sino al final del primer <style>
        s=s[:i]+BLOCK+s[i:]; open(p,'w',encoding='utf8').write(s); n+=1
    return n
if __name__=='__main__': print(run(),'archivos')
