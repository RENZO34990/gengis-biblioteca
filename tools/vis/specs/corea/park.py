from visgen import *
PATH='park-yushin'
V=[
 press('Un Estado débil, un campo político dividido y una ayuda que se achicaba.',
  ('Ayuda de EE. UU. a la baja','Pasaba de donaciones a préstamos'),'1960',
  ('Una política fragmentada','Estudiantes en la calle, inflación y élite dividida'),
  'El terreno ideal para quien prometiera <b>orden</b>.',core_small='2.ª REP.'),
 switches('El 16 de mayo de 1961 el golpe suspendió el orden constitucional en tres frentes.','Lo que quedó en pie tras el golpe',
  [('議','Asamblea Nacional','Quién legisla'),('政','Actividad política','Quién puede organizarse'),('國','Control del Estado','Quién gobierna')],
  on='En pie',off='Suspendido'),
 flow('Dos arquitecturas para un mismo poder: el Estado técnico y la dictadura legal.',
  [('1961','EPB','Dirige los planes quinquenales y el presupuesto.'),('1961','KCIA','Vigilancia política interna y contención de disidentes.'),('Oct 1972','Constitución Yushin','Sin límite de mandatos, elección indirecta y decretos sin supervisión parlamentaria.')],
  note='Esquema de las instituciones, no un organigrama.'),
 timeline('La represión creció, la resistencia también, y el régimen terminó dentro de su propio círculo.',
  [('1972–79','Decretos de Emergencia 1, 4 y 9: criticar la Constitución es delito.'),('1975','Montaje del Partido Revolucionario del Pueblo y ejecuciones.'),('1976','Declaración por la Salvación Nacional.'),('26 oct 1979','Park es asesinado por el director de la KCIA, tras las protestas de Pusan-Masan.')]),
 versus('Cuarenta años después, Park sigue dividiendo la memoria.',
  ['Arquitecto del Milagro del Río Han','Garante de la seguridad nacional'],
  ['Símbolo de la opresión','Abusos contra los derechos humanos'],labels=('La derecha conservadora','Los sectores progresistas'),neutral=True),
]
T=[('Minjung','Movimiento popular de estudiantes, obreros e intelectuales por la democracia.'),
 ('SCNR','Consejo Supremo para la Reconstrucción Nacional: el organismo militar con que Park tomó el control del Estado.'),
 ('EPB','Junta de Planificación Económica: dirigía los planes quinquenales y el presupuesto.'),
 ('KCIA','Agencia Central de Inteligencia: vigilancia política interna y contención de disidentes.'),
 ('Decretos de Emergencia','Decretos con que el presidente gobernaba sin supervisión del Parlamento.'),
 ('Casa Azul','Sede de la Presidencia surcoreana.')]
