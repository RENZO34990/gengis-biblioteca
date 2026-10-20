from visgen import *
PATH='meiji'
V=[
 rings('Un mosaico de dominios con el shogun al centro: ni nación, ni defensa común.','幕',
  [('El shogunato','El bakufu Tokugawa, sin poder para proteger fronteras ni recursos.'),('Los dominios','Un mosaico de feudos casi independientes.'),('El Emperador','En segundo plano, deliberadamente.')],
  note='Esquema del orden político antes de 1853. No es un mapa.',
  aria='Tres círculos concéntricos: el shogunato al centro, los dominios alrededor y el Emperador afuera.'),
 steps('Un solo golpe de cañón abrió un país cerrado desde 1635.',
  [('1858','Tratados desiguales','Las potencias extraen recursos y la soberanía se erosiona.'),('1853','Los barcos negros de Perry','Exige apertura bajo amenaza de fuerza.'),('1808','El Phaeton en Nagasaki','Primera señal de que Japón no podía responder.')],
  note='De abajo hacia arriba, en orden cronológico. Esquema, no a escala.',ship=True,up=True),
 switches('Meiji borró lo viejo antes de construir lo nuevo.','Pilares del orden feudal',
  [('藩','Dominios feudales','Reemplazados por prefecturas'),('士','Clase samurái','Sin estipendios ni espadas'),('幕','Shogunato','Devolvió el poder al Emperador')],
  on='En pie',off='Abolido'),
 flow('Cinco años para pasar de dominios a Estado central.',
  [('1869','Capital','Edo pasa a ser Tokio.'),('1871','Prefecturas','Abolición total de los dominios (han).'),('1871–73','Misión Iwakura','Estudia sistemas industriales, legales y educativos.'),('1873','Seikanron','Ganan la reforma interna sobre invadir Corea.')]),
 versus('Hoy siguen vivos el Triángulo de Hierro y el debate sobre el Artículo 9.',
  ['1868: burocracia meritocrática de élite','Emperador como gobernante absoluto'],
  ['Hoy: sei-kan-zai y amakudari','1947: Emperador como símbolo, Artículo 9 en debate'],labels=('Lo que creó Meiji','Lo que queda')),
]
T=[('sakoku','Política de aislamiento de Japón, estricta desde 1635.'),
 ('Fukoku Kyōhei','Lema Meiji: "nación rica y ejército fuerte".'),
 ('Seikanron','Debate de 1873 sobre invadir Corea.'),
 ('Daijōkan','Sistema de gobierno de 1868 que mezcla la burocracia de la era Nara con división de poderes occidental.'),
 ('amakudari','"Descenso del cielo": burócratas retirados pasan a dirigir empresas privadas.'),
 ('Triángulo de Hierro','Alianza entre burocracia, políticos y grandes empresas (sei-kan-zai).')]
