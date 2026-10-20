from visgen import *
PATH='fragmentacion-politica'
V=[
 press('Cada candidato del LDP competía contra su propio partido, y sobrevivía con facciones y redes personales.',
  ('Un solo voto','El ciudadano elige entre varios candidatos del mismo partido'),'SNTV',
  ('Facciones (habatsu)','Financian campañas y reparten cargos a puerta cerrada'),
  'Resultado: <b>campañas personalistas</b> y escándalos como Recruit (1988) y Sagawa Kyūbin (1992).',core_small='1955–93'),
 steps('Una escisión bastó para sacar al LDP del poder por primera vez en 38 años.',
  [('1993','Ozawa y Hata rompen el partido','Fundan el Shinseitō con 44 partidarios.'),('1993','El LDP pierde la mayoría','Elecciones generales de 1993.'),('1993','Gobierno de ocho partidos','Coalición de oposición con Hosokawa como primer ministro.')],
  note='Orden cronológico de arriba hacia abajo.'),
 versus('La ley del 29 de enero de 1994 cambió el sistema electoral entero.',
  ['Voto único no transferible (SNTV/MMD)','Competencia entre candidatos del mismo partido'],
  ['300 distritos uninominales','200 escaños proporcionales (luego 180)'],labels=('Antes','Después de 1994')),
 stats('Las nuevas reglas dieron al líder nacional el poder de nominar candidatos.',
  [S('10 meses','y el LDP vuelve al gobierno en 1994',to=None),S('2005','Koizumi niega la nominación a los rebeldes de la privatización postal',to=None),S('308 / 480','escaños del DPJ en 2009',to=None)]),
 timeline('El bipartidismo duró poco; las facciones, en cambio, sobrevivieron hasta 2023-2024.',
  [('2009','El DPJ gana con 308 escaños.'),('2011','Fukushima y el desgaste del DPJ.'),('2012','Abe vuelve y la oposición queda fragmentada.'),('2023-24','Escándalo de fondos ilícitos: Kishida disuelve casi todas las facciones.')]),
]
T=[('SNTV/MMD','Voto único no transferible en distritos con varios escaños: cada elector emite un solo voto.'),
 ('habatsu','Facciones internas del LDP que negocian financiamiento y cargos.'),
 ('koenkai','Redes de apoyo local de cada político, centradas en su persona y no en el partido.'),
 ('Shinseitō','Partido de la Renovación, fundado en 1993 por Ozawa y Hata tras escindirse del LDP.'),
 ('Komeito','Partido budista que se alió con el LDP desde 1999.'),
 ('políticos hereditarios','Candidatos que heredan la maquinaria electoral de un familiar.')]
