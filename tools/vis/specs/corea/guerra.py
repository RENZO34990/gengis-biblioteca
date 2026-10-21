from visgen import *
PATH='guerra-de-corea'
V=[
 press('Una república con menos de dos años, sin insumos y sin fuerzas para sostenerse sola.',
  ('Un Estado frágil','Legitimidad cuestionada, unos 120.000 soldados mal equipados'),'南',
  ('Una economía sin base','Sin energía ni industria básica: el Norte se las había quedado'),
  'Resultado: dependencia de la <b>ayuda estadounidense</b> para comer y producir.',core_small='1948–50'),
 stats('Tres años que arrasaron el aparato productivo del Sur.',
  [S('70%','de la industria textil destruida',to=70,suf='%'),S('70%','de la industria química destruida',to=70,suf='%'),S('1.453','puentes en ruinas',to=1453)]),
 flow('Con las fábricas destruidas, el Estado decidió quién sería empresario.',
  [('Granos','Impuestos en arroz','Los campesinos pagaban el 150% del producto anual promedio; la carga subió de 15% a 28%.'),('Subasta','3.551 empresas japonesas','Se vendieron a exterratenientes con bonos devaluados.'),('Emisión','Dinero × 24','El gasto de guerra se financió imprimiendo moneda.')]),
 bars('El ejército creció a toda velocidad y se volvió la institución más organizada.',
  [('Fuerzas Armadas antes de la guerra','120.000',18),('Fuerzas Armadas después','más de 650.000',100,True)],
  note='Soldados; la segunda barra es un mínimo.'),
 versus('Dos tesis explican qué dejó la guerra.',
  ['Bruce Cumings y Hagen Koo: la guerra erradicó a la izquierda','Se impuso un Estado de seguridad nacional'],
  ['Lectura modernizadora: obligó a crear una burocracia profesional','Un ejército moderno, base del Milagro del Río Han'],labels=('Tesis crítica','Tesis modernizadora'),neutral=True),
]
T=[('GARIOA','Programa de socorro estadounidense que aportaba alimentos, fertilizantes y combustible.'),
 ('Panmunjom','Lugar del armisticio del 27 de julio de 1953, sin tratado de paz.'),
 ('DMZ','Zona Desmilitarizada que fija la partición de la península.'),
 ('Crisis Política de Busan','Maniobra de Rhee en 1952 para forzar la elección presidencial directa.'),
 ('KDB','Banco de Desarrollo de Corea, creado en 1954 para canalizar crédito de largo plazo.'),
 ('Tratado de Defensa Mutua','Acuerdo de 1953 con Washington que garantiza tropas estadounidenses permanentes.')]
