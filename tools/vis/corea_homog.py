"""Alinea la composición de los cuadernos de Corea con la de China, manteniendo su identidad (idempotente)."""
import glob,os
REPO=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
MARK='/* ---------- Homogeneización con China ---------- */'
BLOCK=MARK+'''
  header.hero{ min-height:96vh; }
  h1.title-kr{ font-size:clamp(2.2rem, 5vw, 3.8rem); line-height:1.25; }
  .flat-grid > div:not(:first-child){ padding-left:3rem; }
  .nav-adjacent > *:not(:first-child){ padding-left:3rem; }
  .chart-block{margin:1.8rem 0; border-top:1px solid var(--line); padding-top:1.6rem; max-width:640px;}
  @media(max-width:820px){
    .flat-grid > div:not(:first-child){ padding-left:0; }
    .nav-adjacent > *:not(:first-child){ padding-left:0; }
    header.hero{ min-height:88vh; }
  }
'''
def run():
    n=0
    for p in sorted(glob.glob(os.path.join(REPO,'docs','corea','*','index.html'))):
        if 'bts-hallyu' in p: continue
        s=open(p,encoding='utf8').read()
        if MARK in s: continue
        i=s.index('</style>'); s=s[:i]+BLOCK+s[i:]; open(p,'w',encoding='utf8').write(s); n+=1
    return n
if __name__=='__main__': print(run(),'archivos')
