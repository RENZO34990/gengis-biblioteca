from visgen import *
PATH='gran-salto-adelante'
V=[
 versus('Una industria que crece y un campo que se queda atrás.',
  ['Industria pesada: más de 18% anual','Propiedad privada urbana estatizada','Más del 50% de la inversión pública'],
  ['Campo en cooperativas (93.5% de los hogares)','Agricultura: menos de 8% de la inversión','Grano per cápita estancado en subsistencia'],labels=('Ciudad e industria','Campo'),neutral=True),
 stats('En unos meses, el campo entero quedó reorganizado por la voluntad.',
  [S('740,000 → 26,000','cooperativas fusionadas en Comunas Populares',to=None),S('≈500 M','de personas en las comunas, más del 98% del campo',to=None),S('600,000','hornos rústicos para duplicar el acero de 5.3 a 10.7 millones de toneladas')]),
 flow('Una carta honesta se pagó con una purga y el colapso siguió.',
  [('Ago 1959','Carta de P\'eng Te-huai','Denuncia el "fanatismo de izquierda".'),('Respuesta','Mao lo destituye','Lo llama "oportunista de derecha".'),('1959–60','Segunda fase','Más requisas de grano.'),('1959–61','Gran Hambruna','Muertes por inanición de decenas de millones.')]),
 bars('Cayó el grano, y buena parte del acero era chatarra.',
  [('Grano 1958','200 M t',100),('Grano 1959','165 M t',82),('Grano 1960','160 M t',80,True)],
  note='Producción de grano en China, millones de toneladas.'),
 timeline('La hambruna dejó reglas que Pekín no ha vuelto a romper.',
  [('1959–61','Nace el principio de proteger la tierra y las reservas de grano.'),('1978–83','Se disuelven las comunas y llega el Sistema de Responsabilidad Familiar.'),('Hoy','Mantener 1,800 millones de mou de tierra cultivable.')]),
]
T=[('Dayuejin','Nombre chino del Gran Salto Adelante.'),
 ('Comunas Populares','Grandes unidades rurales que fusionaron cooperativas y confiscaron parcelas, herramientas y ganado.'),
 ('Sputniks de producción','Informes de cosecha falsificados por los cuadros locales para cumplir la presión política.'),
 ('Conferencia de Lushan','Reunión de agosto de 1959 donde Mao rechazó la crítica de P\'eng Te-huai.'),
 ('Sanzi Yibao','Política pragmática posterior al desastre: parcelas privadas y mercados libres rurales.'),
 ('shishi qiushi','Máxima de "buscar la verdad en los hechos": pragmatismo frente al dogma.')]
