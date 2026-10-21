from visgen import *
PATH='democratizacion-apertura'
V=[
 press('El crecimiento autoritario ya no cabía en la sociedad que había producido.',
  ('Sindicatos reprimidos','Salarios contenidos y jornadas extensas'),'1987',
  ('Una clase media urbana','En rápida expansión'),
  'Un modelo <b>socialmente insostenible</b> para quienes ya no lo toleraban.',core_small='HASTA'),
 stats('La democracia liberó las demandas salariales que el Estado había reprimido.',
  [S('46,6%','alza de los salarios medios en manufactura, 1987–1989',to=46.6,dec=1,suf='%'),S('36,6%','votos de Roh Tae-woo en diciembre de 1987',to=36.6,dec=1,suf='%'),S('16 años','desde las últimas elecciones presidenciales directas',to=16,suf=' años')]),
 steps('Tres frentes a la vez: Constitución, gobierno civil y mercado abierto.',
  [('Oct 1987','Constitución de la Sexta República','Mandato único de 5 años y fin de la disolución de la Asamblea.'),('1988','Tribunal Constitucional y NEC','Órganos independientes; llegan salario mínimo y pensiones.'),('1993','Nombre real y fin de Hanahoe','Kim Young-sam desarticula la red secreta de oficiales.'),('1994–95','Fin del plan y elecciones locales','Se desmantela la EPB y vuelve la elección de alcaldes.'),('1996','Segyehwa y la OCDE','Se liberan capitales sin un supervisor prudencial.')],
  note='Orden cronológico, de arriba abajo.'),
 flow('Una democracia que juzgó a los dictadores no había regulado todavía a los bancos.',
  [('1997','Doble descalce','Dólares a corto plazo prestados a largo plazo en wones.'),('Chaebols','Deuda sobre patrimonio de más de 500%','Promedio entre los 30 mayores.'),('1997','Quiebras en cadena','Caen Hanbo Steel, Sanmi y Kia.'),('Dic 1997','Rescate del FMI','58.400 millones de dólares.')]),
 versus('Dos lecturas de la democracia que nació en 1987.',
  ['Alternancia pacífica','Vigencia del marco de 1987'],
  ['Democratización incompleta','Poder hiperconcentrado y un nexo Estado-chaebol que no evitó la crisis'],labels=('Consolidación democrática','Presidencialismo imperial'),neutral=True),
]
T=[('tres bajas','Petróleo barato, tasas de interés globales bajas y un won depreciado frente al yen.'),
 ('Segyehwa','Estrategia de globalización que abrió el mercado surcoreano.'),
 ('merchant banks','Financieras que tomaban dólares a corto plazo y los prestaban a largo plazo a los chaebols.'),
 ('Hanahoe','Red secreta de oficiales militares, desarticulada en 1993.'),
 ('Sistema de Nombre Real','Obligó a usar el nombre real en cuentas bancarias y eliminó las cuentas fantasma.'),
 ('Basilea','Estándares internacionales de supervisión bancaria.')]
