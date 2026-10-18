"""Regenera la capa visual de un país: python3 tools/vis/run.py china canton opio ...
Cada spec en specs/<país>/<nombre>.py define PATH (carpeta del cuaderno), V (5 visuales) y T (glosario). Idempotente."""
import sys, os, importlib
here = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [here]
import visgen
country = sys.argv[1]; sys.path.insert(0, os.path.join(here, 'specs', country))
for n in sys.argv[2:]:
    m = importlib.import_module(n)
    visgen.apply(f'{visgen.REPO}{country}/{m.PATH}/index.html', country, m.V, m.T)
    print('ok', n)
