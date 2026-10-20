from visgen import *
PATH='apertura-forzada'
V=[
 rings('El shogunato Tokugawa dejaba entrar solo lo que podía controlar.','徳川',
  [('El shogun','Linaje hereditario como única fuente de poder.'),('Nagasaki','El único puerto abierto al comercio extranjero, bajo control estatal.'),('El mundo exterior','Edicto de 1635: ningún súbdito podía salir, y los barcos extranjeros se repelían.')],
  note='Esquema del sakoku, no un mapa.',aria='Tres círculos concéntricos: el shogun al centro, Nagasaki alrededor y el mundo exterior afuera.'),
 steps('De los cañones de Perry al colapso de la autoridad del shogun.',
  [('Jul 1853','Perry en la bahía','Barcos de guerra exigen abrir Japón al comercio.'),
   ('1858','Tratados desiguales','El bakufu cede y rompe el sakoku.'),
   ('1858–68','Bakumatsu','Década y media de violenta agitación interna.')],ship=True),
 flow('Occidentalizar para resistir a Occidente: la paradoja que fundó el Estado Meiji.',
  [('Nov 1867','El shogun renuncia','Yoshinobu devuelve el poder a la Corte Imperial.'),
   ('1868','Golpe en Kioto','Satsuma y Chōshū deponen el bakufu y proclaman la Restauración.'),
   ('Carta 1868','Modernizar','Unificar el país y adoptar tecnologías e instituciones occidentales.')]),
 stats('En cinco años se desmontó el orden feudal.',
  [S('1869','la capital pasa a Edo, rebautizada Tokio',to=None),S('1871','abolición de los dominios, reemplazados por prefecturas',to=None),S('1871–73','la Misión Iwakura recorre EE. UU. y Europa',to=None)]),
 versus('El debate sigue abierto: ¿ruptura súbita en 1868 o asimilación continua?',
  ['Una modernidad impuesta en 1868','Dos siglos y medio de aislamiento superados de golpe'],
  ['Un proceso gradual de asimilación bajo los Tokugawa','Rangaku: estudio occidental ya antes de Perry'],labels=('Tesis de la ruptura','Tesis de la continuidad'),neutral=True),
]
T=[('sakoku','Política de aislamiento internacional del shogunato Tokugawa.'),
 ('bakufu','El gobierno militar del shogun.'),
 ('rangaku','"Estudios holandeses": el estudio de ciencia y política occidentales durante el aislamiento.'),
 ('Bakumatsu','Los últimos años del shogunato, de 1853 a 1868.'),
 ('Satsuma','Dominio del sur de Japón, uno de los que derribaron al shogunato.'),
 ('Juramento de la Carta','Declaración de principios de 1868 de la nueva élite Meiji.')]
