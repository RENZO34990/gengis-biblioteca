from visgen import *
PATH='colapso-qing'
V=[
 rings('La dinastía seguía en el trono, pero gobernaba un país cada vez más pequeño dentro de su propio país.','清',
  [('La corte Qing','Un trono que ya no decidía casi nada.'),('Potencias y feudales','Tratados desiguales por fuera, fuerzas feudales por dentro.'),('Algo nuevo en los márgenes','Una burguesía y unos intelectuales que leían sobre repúblicas.')],
  note='Esquema del cerco sobre la corte entre 1860 y 1894.',aria='Círculos concéntricos: la corte al centro, rodeada de potencias y fuerzas feudales y, afuera, nuevos grupos.'),
 steps('La corte tuvo cien días para reformarse y eligió quedarse igual.',
  [('1894–95','Derrota ante Japón','Ningún golpe anterior había dolido igual.'),('1898','Reforma de los Cien Días','Kang Youwei y Liang Qichao intentan modernizar el imperio.'),('Poco después','Cixi la sofoca','La facción conservadora la aplasta antes de que se asiente.')],
  note='Elegir quedarse igual le costó trece años más de vida.'),
 stats('Un gabinete de "reforma" dominado por el clan imperial convenció a todos de lo contrario.',
  [S('7 de 13','miembros del gabinete de 1911 eran del clan imperial manchú',to=None),S('1911','Levantamiento de Wuchang y Revolución de Xinhai'),S('Mar 1912','abdicación del último emperador, Puyi',to=None)]),
 versus('China dejó de tener emperador, pero no de tener amos.',
  ['Monarquía imperial','Nobleza manchú con privilegios','Concesiones extranjeras'],
  ['República sin ejército central','Caudillos regionales con Yuan Shikai','Las mismas concesiones, negociadas con los señores de la guerra'],labels=('Hasta 1911','Desde 1912')),
 timeline('Para el Partido, 1911 es el punto cero de la búsqueda de soberanía.',
  [('1911','La Revolución de Xinhai: un paso necesario pero incompleto.'),('1921','El PCCh se presenta como quien terminará el trabajo.'),('Hoy','Sun Yat-sen es conmemorado en la República Popular y en Taiwán.')]),
]
T=[('Wuxu bianfa','Nombre chino de la Reforma de los Cien Días de 1898.'),
 ('Cixi','Emperatriz viuda y figura central de la facción conservadora de la corte.'),
 ('Levantamiento de Wuchang','Alzamiento de noviembre de 1911 que desencadenó la Revolución de Xinhai.'),
 ('Ejército de Beiyang','Poderoso ejército moderno que comandaba Yuan Shikai.'),
 ('Puyi','Último emperador de China; abdicó en marzo de 1912.')]
