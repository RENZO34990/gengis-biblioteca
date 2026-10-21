from visgen import *
PATH='industria-pesada-chaebols'
V=[
 press('El modelo de camisas y zapatos perdía su ventaja y no había industria pesada propia.',
  ('Salarios en alza','Y competencia del Sudeste Asiático'),'70%',
  ('Barreras proteccionistas','En los mercados occidentales'),
  'Sin acero, buques ni insumos químicos propios, <b>no había salida hacia arriba</b>.',core_small='INDUSTRIA LIGERA'),
 versus('Dos presiones convergieron: la seguridad y la economía.',
  ['Doctrina Nixon: se retiran 20.000 soldados de EE. UU.','1968: atentado contra Park y captura del USS Pueblo'],
  ['1973: el crudo cuadruplica su precio','Recesión, inflación y balanza de pagos deteriorada'],labels=('Geopolítica','Economía'),neutral=True),
 rings('El Estado escogió seis sectores y las familias que los construirían.','HCI',
  [('Seis sectores','Siderurgia, astilleros, electrónica, maquinaria pesada, petroquímica y metales no ferrosos.'),('Crédito dirigido','Tasas reales negativas y garantías estatales para la deuda externa.'),('Chaebols elegidos','Hyundai, Samsung, LG y Daewoo: licencias exclusivas, exenciones y terrenos.')],
  aria='Tres círculos concéntricos: los chaebols elegidos al centro, el crédito dirigido alrededor y los seis sectores afuera.'),
 bars('La industria pesada pasó de un tercio a más de la mitad de la manufactura y de las exportaciones.',
  [('Pesada y química en la manufactura, 1970','35,9%',60),('Pesada y química en la manufactura, 1981','más de 53%',88,True),('Pesados y químicos en las exportaciones, 1972','21,3%',36),('Pesados y químicos en las exportaciones, 1978','34,7%',58,True)],
  note='Porcentajes sobre el total. Escala de 0 a 60%.'),
 stats('Los sectores de 1973 siguen siendo la estructura del país, y sus dueños también.',
  [S('+60%','del valor exportado viene de los sectores del impulso HCI',to=60,pre='+',suf='%'),S('78,8%','del PIB nominal generan los grandes grupos (2020–2025)',to=78.8,dec=1,suf='%'),S('Korea Discount','el descuento que castiga a las participaciones cruzadas',to=None)]),
]
T=[('Doctrina Nixon','Anuncio de 1969–1971 de que Estados Unidos retiraría tropas de Asia, incluidas 20.000 de Corea.'),
 ('HCI Drive','Declaración de la Industria Pesada y Química, proclamada por Park el 12 de enero de 1973.'),
 ('Policy loans','Crédito dirigido por el Estado a tasas subsidiadas, a cambio de metas.'),
 ('chaebols','Conglomerados familiares surcoreanos, como Hyundai, Samsung, LG y Daewoo.'),
 ('KFTC','Comisión de Comercio Justo, creada en 1980 para limitar las garantías cruzadas de deuda.'),
 ('POSCO','Siderúrgica estatal de Pohang, inaugurada en 1973.')]
