from visgen import *
PATH='sistema-canton'
V=[
 steps('Pekín quiso ordenar una costa caótica; un solo incidente le hizo cerrarla a casi todos.',
  [('Siglo XVII','Koxinga y la costa evacuada','Un rebelde leal a los Ming financia sus ataques con comercio marítimo; el emperador manda evacuar a la población costera.'),
   ('1683','Los puertos reabren','Pero el miedo a que los extranjeros se aliaran con "nativos traidores" nunca desapareció.'),
   ('Antes del Cohong','Comerciantes del Emperador','Uno pagó 42,000 taels por el puesto sin capital ni mercancía: los sobornos se volvieron la norma.'),
   ('1759','Incidente de James Flint','Un comerciante británico se queja ante el emperador y termina preso: Pekín da por fracasado el experimento.')]),
 flow('Un comercio de un solo sentido, un contrabando para equilibrarlo y un funcionario que dijo basta.',
  [('1','Té y seda','Europa los quiere; China no necesita nada de vuelta.'),('2','Solo plata','China exige que se le pague únicamente en plata.'),('3','Opio de contrabando','Los británicos lo meten desde la India para equilibrar las cuentas.'),('4','Lin Zexu, 1839','Encierra a 350 personas y destruye más de 20,000 cofres.')]),
 versus('Elliot no salvó la mercancía: convirtió un problema de contrabandistas en uno de Estado.',
  ['El opio es de mercaderes privados','Si se pierde, lo pierden ellos','Un asunto de contrabando'],
  ['Elliot ordena entregarlo "en nombre de la Corona"','Londres promete reembolsar las pérdidas','Una cuestión de soberanía estatal'],labels=('Antes del 27 de marzo de 1839','Después')),
 stats('El tratado abrió puertos, disolvió un monopolio y cambió el centro del comercio.',
  [S('5','puertos de tratado: Cantón, Amoy, Fuzhou, Ningbo y Shanghái',to=5),S('21 M','de dólares de indemnización, más la cesión de Hong Kong',to=21,suf=' M'),S('×3','la exportación de seda de Shanghái en solo dos años (1845–1847)',to=3,pre='×')]),
 timeline('Los puertos donde China perdió en 1842 son hoy donde se conecta con el mundo.',
  [('1842','Cinco puertos de tratado y el siglo de la humillación.'),('1979–80','Las Zonas Económicas Especiales se levantan, muchas, sobre antiguos puertos de tratado.'),('Hoy','El delta del río Perla genera más del 23% de las exportaciones nacionales.')]),
]
T=[('Cohong','Gremio de comerciantes chinos que controlaba el comercio de té y seda con los extranjeros en Cantón.'),
 ('Lin Zexu','Funcionario enviado por el emperador a Cantón en 1839 para frenar el opio; apodado "Lin el Cielo Azul".'),
 ('puertos de tratado','Puertos donde los extranjeros podían residir y comerciar por tratado, fuera del viejo sistema de Cantón.'),
 ('siglo de la humillación','Nombre con que China recuerda el periodo que empieza con las derrotas ante las potencias en 1842.'),
 ('Doble Circulación','Estrategia económica actual de Pekín que prioriza la seguridad económica y la autosuficiencia tecnológica.')]
