from visgen import *
PATH='hegemonia-ldp'
V=[
 versus('Con la izquierda reunificada, la derecha dejó de pelearse entre sí.',
  ['Partido Liberal','Partido Democrático'],
  ['Partido Liberal Democrático (LDP)','Un solo bloque conservador'],labels=('Hasta 1955','Noviembre de 1955')),
 stats('Una fusión de 1955 que duraría casi cuatro décadas.',
  [S('38 años','de control ininterrumpido de la Cámara de Representantes',to=38),S('1955','fusión conservadora (hoshu gōdō)',to=None),S('1 y 1/2','partidos: el LDP y una oposición atomizada',to=None)]),
 flow('El Triángulo de Hierro: cada lado le daba algo a los otros dos.',
  [('Políticos','LDP','Reelección con fondos públicos y obras en sus distritos.'),('Burócratas','Ministerios','Dirigen el milagro con "guía administrativa".'),('Empresas','Conglomerados','Keidanren aporta fondos al LDP.')],
  note='Esquema de intercambios, no un organigrama.'),
 press('El primer ministro se decidía entre facciones, y el LDP se sostenía con dinero de fuera.',
  ('Facciones (habatsu)','Eligen al primer ministro a puerta cerrada'),'LDP',
  ('Dinero encubierto de la CIA','Millones de yenes durante toda esta fase'),
  'En 1960 las protestas por el <b>Anpo</b> rodean la Dieta bajo el gabinete de Kishi.',core_small='1955–60'),
 switches('Se prohibió el amakudari, pero otros hilos del sistema siguen en pie.','Herencias del Sistema de 1955',
  [('天','Amakudari','Prohibido por ley en 2007'),('官','Peso técnico de Kasumigaseki','Siguió incluso con el DPJ (2009-2012)'),('派','Facciones del LDP','Casi todas disueltas en 2023-24 por el escándalo de fondos')],
  on='Sigue vigente',off='Superado'),
]
T=[('hoshu gōdō','La "fusión conservadora" de noviembre de 1955 que creó el LDP.'),
 ('Triángulo de Hierro','Alianza entre políticos del LDP, burócratas y grandes empresas (Sei-Kan-Zai).'),
 ('amakudari','"Descenso del cielo": burócratas que se retiran a cargos en las empresas que regulaban.'),
 ('FILP','Programa de inversión fiscal alimentado por los ahorros postales.'),
 ('Keidanren','Federación patronal que financia al LDP.'),
 ('Anpo','Tratado de Seguridad con Estados Unidos, cuya renovación provocó las protestas de 1960.')]
