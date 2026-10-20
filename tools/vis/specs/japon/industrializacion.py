from visgen import *
PATH='industrializacion-meiji'
V=[
 stats('Un país de arroz y de impuestos pesados frente a la Revolución Industrial.',
  [S('~40%','de la cosecha se iba en impuestos',to=None),S('260+','años de dictadura militar feudal',to=None)]),
 versus('La apertura forzada dejó a Japón sin defensas.',
  ['Más de 250 años de aislamiento casi total','Control de sus propios aranceles'],
  ['Tratados desiguales','Industrias nacientes sin protección'],labels=('Antes de Perry','Después de Perry')),
 flow('Dos giros en nueve años: primero el Estado fabricaba, luego soltó las fábricas.',
  [('1871','Giro mental','La élite vuelve convencida: el poder militar nace de la fuerza industrial.'),('~1880','Fábricas "modelo"','Inflación y déficits por operarlas directamente.'),('1880','Matsukata vende','Las fábricas pasan a Mitsui y Mitsubishi, futuros zaibatsu.')]),
 stats('En cinco años se rehizo el Estado, y empezó el ferrocarril.',
  [S('3,000+','expertos extranjeros (o-yatoi gaikokujin) contratados',to=3000,pre='',suf='+'),S('107','funcionarios en la Misión Iwakura',to=107),S('18 mi','de vía férrea en 1872',to=18,suf=' mi')]),
 timeline('Del Estado Meiji al METI: el mismo método, otras industrias.',
  [('1880','El giro de Matsukata define el ADN económico.'),('1945','Los zaibatsu se desmantelan y evolucionan hacia keiretsu.'),('Hoy','El METI formula "visiones" industriales para semiconductores e IA.'),('Sanaenomics','Regreso deliberado a esa estrategia.')]),
]
T=[('sakoku','Los más de dos siglos de aislamiento casi total de Japón.'),
 ('o-yatoi gaikokujin','Expertos extranjeros contratados para enseñar ciencia y tecnología.'),
 ('Matsukata Masayoshi','Ministro que vendió las fábricas estatales al sector privado en 1880.'),
 ('zaibatsu','Grandes conglomerados familiares como Mitsui y Mitsubishi.'),
 ('keiretsu','Redes de empresas que priorizan estabilidad sobre ganancia trimestral.'),
 ('Sociedad 5.0','Sociedad ultra-tecnológica que integra IA en la vida cotidiana.')]
