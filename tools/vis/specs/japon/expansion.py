from visgen import *
PATH='expansion-imperial'
V=[
 rings('El Ejército respondía solo al Emperador, y eso lo ponía fuera del alcance del gabinete.','天皇',
  [('El Emperador','Mando supremo directo de Ejército y Armada (Tosuiken, Artículo 11).'),('Los militares','Estado mayor independiente y veto: sin ministro de Guerra o Marina, el gabinete cae.'),('El gabinete civil','Gobierno sin poder para disciplinar a las fuerzas armadas.')],
  note='Esquema del reparto de poder bajo la Constitución Meiji. No es un organigrama oficial.',
  aria='Tres círculos concéntricos: el Emperador al centro, los militares alrededor y el gabinete civil afuera.'),
 timeline('Cuatro golpes seguidos rompieron la estabilidad liberal y dejaron a la autoridad civil sin respuesta.',
  [('1920','Recesión de posguerra: las exportaciones caen a la mitad.'),('1923','Gran Terremoto de Kantō.'),('1927','Pánico financiero Shōwa: quiebra el 25% de los bancos.'),('1930','Vuelta fallida al patrón oro, en plena Gran Depresión.'),('1931','Mukden: el Ejército de Kwantung invade sin permiso de Tokio.')]),
 flow('Takahashi sacó a Japón de la Depresión, pero el gasto fue a las armas.',
  [('1931','Embargo de oro','Takahashi devalúa el yen.'),('Gasto','Bonos al Banco de Japón','Se financia el gasto en armamentos.'),('1936','Golpe del 26 de febrero','Jóvenes oficiales asesinan ministros; el gobierno cede.')],
  note='Esquema de la secuencia, no una cronología exacta.'),
 bars('La industria pesada pasó de un tercio de la producción a casi dos tercios.',
  [('Industria pesada, 1930','35%',35),('Industria pesada, 1940','63%',63,True)],
  note='Porcentaje de la producción manufacturera. Hacia agosto de 1938 unas 390,000 pymes civiles habían quebrado o se habían reconvertido.'),
 versus('Un legado que dura: lo que se disolvió y lo que sobrevivió.',
  ['Zaibatsu disueltos por el SCAP','Ejército y partidos de guerra'],
  ['Burocracia reformista que heredó el MITI','Subcontratación vertical, matriz de los keiretsu'],labels=('Lo que se disolvió','Lo que sobrevivió')),
]
T=[('Tosuiken','El mando supremo directo del Emperador sobre Ejército y Armada, fuera del control del gabinete.'),
 ('genrō','Oligarquía de asesores imperiales con poder real bajo la Constitución Meiji.'),
 ('Kempeitai','Policía militar japonesa; reprimía a opositores e intelectuales.'),
 ('Manchukuo','Estado títere creado por Japón en Manchuria en 1932.'),
 ('kokutai','Idea de una identidad nacional unida en torno al Emperador.'),
 ('Burocracia Reformista','Tecnócratas del Ministerio de Comercio e Industria que planificaron la economía de guerra.')]
