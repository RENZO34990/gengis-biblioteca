from visgen import *
PATH='liberacion-division'
V=[
 rings('Un país libre de Japón, pero decidido desde afuera.','38°',
  [('Los coreanos','Sindicatos, asociaciones campesinas y movimientos estudiantiles querían fundar un Estado soberano.'),('Estados Unidos y la URSS','Dividen temporalmente la península en el paralelo 38.'),('El resultado','Lo provisional duró para siempre.')],
  note='Esquema de las capas de decisión. No es un mapa.',
  aria='Tres círculos concéntricos: los coreanos al centro, las superpotencias alrededor y la división afuera.'),
 flow('Sin acuerdo entre las potencias, la ONU autorizó elecciones solo en el sur.',
  [('1947','Comisión Mixta','Estados Unidos y la URSS se estancan.'),('ONU','UNTCOK','Washington lleva el caso a la ONU; la URSS no deja entrar al norte.'),('Decisión','Elecciones solo en el sur','Se hace irreversible un Estado dividido.')]),
 timeline('Cuatro fechas separaron una península en dos Estados.',
  [('10 may 1948','Elecciones solo en el sur.'),('17 jul 1948','Primera Constitución de la República de Corea.'),('15 ago 1948','Nace la República de Corea.'),('9 sep 1948','Kim Il-sung proclama la RPDC en el norte.')]),
 versus('Un Estado nacido contra el comunismo con hombres del aparato colonial.',
  ['Presidencialismo centralizado','Fin declarado: contener a la izquierda'],
  ['Policía y burocracia con funcionarios coloniales','Crisis de legitimidad desde el origen'],labels=('Lo que se fundó','Con quién se fundó'),neutral=True),
 versus('Dos lecturas siguen en disputa.',
  ['Bruce Cumings: la división fue una imposición de la Guerra Fría','El USAMGIK sofocó los órganos populares de autogobierno'],
  ['Lectura tradicional: crear la ROK fue una acción defensiva','Salvaba al menos la mitad de la península de la órbita soviética'],labels=('Lectura revisionista','Lectura tradicional'),neutral=True),
]
T=[('USAMGIK','Gobierno militar estadounidense en el sur de Corea tras 1945.'),
 ('paralelo 38','Línea que dividió la península entre las zonas de ocupación estadounidense y soviética.'),
 ('UNTCOK','Comisión Temporal de la ONU para Corea.'),
 ('Masacre de la Isla de Jeju','Represión de 1948 contra insurgentes y civiles en la isla de Jeju.'),
 ('Ley de Seguridad Nacional','Ley de 1948 usada durante décadas para regular el disenso político.'),
 ('Gobierno Provisional','Gobierno de la resistencia creado en el exilio en 1919.')]
