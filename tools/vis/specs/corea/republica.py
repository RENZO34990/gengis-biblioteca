from visgen import *
PATH='primera-republica'
V=[
 rings('Un campo feudal: pocos dueños de la tierra y un Estado sin recursos para sostener a nadie.','田',
  [('Terratenientes y yangban','Concentraban la tierra fértil; muchos habían colaborado con el régimen colonial.'),('Campesinos arrendatarios','Más del 80% de la población vivía de la agricultura de subsistencia, en extrema pobreza.'),('El Estado','Sin burocracia técnica, sin capacidad fiscal y sin divisas; el Sur no tenía fertilizantes ni electricidad.')],
  note='Esquema de la estructura agraria. No es un mapa.',
  aria='Tres círculos concéntricos: los terratenientes al centro, los campesinos alrededor y el Estado afuera.'),
 bars('La guerra hundió el comercio exterior y obligó a repartir la tierra.',
  [('Comercio exterior, 1948','208 millones de dólares',100),('Comercio exterior, 1950','2,9 millones de dólares',3,True)],
  note='Millones de dólares.'),
 flow('Dos reformas definieron quién sería rico en la Corea que venía.',
  [('Jun 1949','Reforma agraria','Tope de unas 3 hectáreas por explotación; los latifundios se redistribuyen.'),('Jeok-san','Bienes japoneses','3.551 plantas subastadas al 25–30% de su valor, pago a 15 años.'),('Ayuda','Licencias y divisas','Cerca del 50% del presupuesto y más del 70% de las importaciones, 1953–61.')]),
 flow('De la acumulación originaria a la caída del régimen.',
  [('1953–54','Samsung','Cheil Sugar y Cheil Industries.'),('1958','LG','GoldStar, con las primeras radios nacionales.'),('Abr 1960','Revolución del 19 de abril','Fraude electoral y corrupción; Rhee renuncia y se exilia.')]),
 versus('Dos lecturas se disputan el periodo.',
  ['Gregory Henderson: una etapa perdida','Corrupción y parasitismo político'],
  ['Lectura revisionista: se construyeron cimientos','Equidad agraria, capital humano e instituciones'],labels=('Lectura crítica','Lectura revisionista'),neutral=True),
]
T=[('chongbo','Unidad de superficie coreana; 3 chongbo equivalen a unas 3 hectáreas.'),
 ('yangban','Aristocracia terrateniente tradicional de Corea.'),
 ('Ley de Reforma Agraria','Ley de junio de 1949 que limitó la propiedad de tierra y redistribuyó los latifundios.'),
 ('Jeok-san','Los bienes que dejaron los japoneses y que el Estado subastó.'),
 ('GARIOA','Programa de ayuda estadounidense de posguerra.'),
 ('Partido Liberal','Partido de Syngman Rhee, vinculado a los empresarios favorecidos.'),
 ('Revolución del 19 de Abril','Levantamiento de 1960 contra el fraude electoral; derribó a Rhee.')]
