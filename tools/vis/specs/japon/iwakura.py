from visgen import *
PATH='iwakura'
V=[
 stats('No era una delegación cualquiera: era casi el gabinete entero, de viaje durante dos años.',
  [S('~50','funcionarios de alto rango',to=50,pre='~'),S('~60','estudiantes y asistentes',to=60,pre='~'),S('US$1 M','costo estimado de la época',to=None)]),
 flow('Washington fue la primera lección: el reconocimiento se gana antes de exigirlo.',
  [('Ene–ago 1872','Intentan renegociar','Piden revisar los tratados desiguales impuestos a Japón.'),
   ('Resultado','Fracasan','Es demasiado pronto para exigir un trato de igual a igual.'),
   ('Lección','Primero, ganarse el lugar','Esa idea los acompaña el resto del viaje.')]),
 bars('Dónde creyeron que estaba el modelo a estudiar con más detalle.',
  [('Reino Unido en el Jikki','20 de 100 fascículos',20),('EE. UU. y Reino Unido juntos','40% del libro',40,True)],
  note='Proporción del texto del Jikki, el relato oficial del viaje.'),
 versus('Cada capital dejó una pieza para el Japón que venía.',
  ['Prusia: sistema educativo centralizado','Prusia: estructura militar eficiente'],
  ['Francia: informes sobre industria','Francia: derecho, insumo para Nakae Chōmin'],labels=('Prusia','Francia'),neutral=True),
 press('De vuelta, vieron a Asia con ojos nuevos: territorios bajo dominio colonial.',
  ('Estética europea','Oro y perlas'),'港',('Estética china','Bermellón'),
  'Kume los compara conscientemente en la arquitectura colonial de <b>Hong Kong</b>, el 27 de agosto de 1873.',core_small='HK'),
 timeline('Casi dos años de viaje terminaron en una fractura interna.',
  [('23 dic 1871','Zarpan de Yokohama.'),('1872','Fracasa la renegociación en Washington.'),('13 sep 1873','Vuelven con un plan maestro para el Estado.'),('1873','Debate Seikanron: ¿invadir Corea? Primera gran fractura del gobierno Meiji.')]),
]
T=[('tratados desiguales','Acuerdos que Japón firmó bajo presión y que le quitaban control sobre sus aduanas y su justicia.'),
 ('Jikki','El relato oficial de la misión, en 100 fascículos.'),
 ('Saltaire','Pueblo-modelo textil de Titus Salt, cerca de Bradford.'),
 ('Nakae Chōmin','Pensador japonés que estudió derecho francés y difundió ideas de gobierno representativo.'),
 ('Noh','Teatro japonés clásico, con máscaras y movimiento lento.'),
 ('Seikanron','Debate de 1873 sobre invadir Corea.')]
