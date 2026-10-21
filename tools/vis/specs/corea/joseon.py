from visgen import *
PATH='joseon-ganghwa-gabo'
V=[
 rings('Un reino cerrado: el rey al centro, los yangban alrededor y el campo que sostenía a todos.','王',
  [('El rey y la corte','Monarquía neoconfuciana, muy centralizada, fundada en 1392.'),('Los yangban','Aristocracia que ocupaba los cargos por exámenes confucianos y controlaba la tierra.'),('El campo','Más del 80% de la población vivía del arroz y los granos, pagando impuestos en especie y en trabajo.')],
  note='Esquema de cómo se organizaba Joseon. No es un mapa.',
  aria='Tres círculos concéntricos: el rey al centro, los yangban alrededor y los campesinos afuera.'),
 switches('Tres puertos y un tratado le quitaron al Estado el control de su propio comercio.','Poderes que aún controla Joseon',
  [('港','Puertos','Busan, Incheon y Wonsan quedan abiertos a Japón'),('稅','Aduanas','Exenciones temporales para el comercio japonés'),('法','Justicia propia','Los japoneses quedan fuera de los tribunales coreanos')],
  on='En manos de Joseon',off='Cedido a Japón'),
 steps('Dos choques en cadena abrieron paso a un paquete de reformas bajo vigilancia japonesa.',
  [('1894','Revolución Donghak','Insurrección campesina antifeudal; su represión trae a China y Japón.'),('1894–95','Guerra Sino-Japonesa','La victoria japonesa deja a Japón supervisando.'),('1894–96','Reformas Gabo','Fin del orden yangban, ministerios modernos, impuestos en dinero.'),('1897','Imperio Coreano','Gojong proclama el Daehan Jeguk para afirmar igualdad diplomática.')]),
 versus('Las reformas dieron instituciones modernas a un Estado sin finanzas propias.',
  ['Ministerios y un gabinete al estilo occidental','Impuestos pagados en moneda, no en grano'],
  ['El banco japonés Dai-Ichi como emisor de facto','Campesinos obligados a vender su cosecha para pagar'],labels=('Lo que se reformó','Lo que quedó fuera de control')),
 timeline('De la pérdida de soberanía a la memoria que aún divide.',
  [('1895','Agentes japoneses asesinan a la reina Min.'),('1905','Tratado de Eulsa: Corea es protectorado.'),('22 ago 1910','Japón anexa formalmente Corea.'),('1949','La reforma agraria de Rhee elimina el latifundio.')]),
]
T=[('yangban','Aristocracia de Joseon: ocupaba los cargos y controlaba la mayor parte de la tierra.'),
 ('gwageo','Los exámenes confucianos con que se accedía a los cargos del Estado.'),
 ('Reino Ermitaño','Nombre de la política exterior de Joseon: contactos mínimos fuera del tributo a China.'),
 ('Tratado de Ganghwa','Tratado de 1876, impuesto por la Armada japonesa; el primero desigual para Corea.'),
 ('extraterritorialidad','Derecho de los extranjeros a ser juzgados por sus propios tribunales y no por los locales.'),
 ('Gaehwapa','Grupo de reformistas coreanos inspirados en la Restauración Meiji.'),
 ('Dai-Ichi','Banco privado japonés que funcionó como emisor de facto en la península.')]
