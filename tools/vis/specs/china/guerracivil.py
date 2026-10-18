from visgen import *
PATH='guerra-civil-invasion-japonesa'
V=[
 flow('Una alianza para unificar China se rompió a sangre en Shanghái.',
  [('1923','Primer Frente Unido','PCCh y Kuomintang, con la Internacional Comunista.'),('Siguiente','Expedición al Norte','Contra los caudillos del Norte.'),('Abr 1927','Purga en Shanghái','Chiang Kai-shek rompe la alianza y masacra a comunistas.')]),
 steps('El Partido fue perseguido por dentro mientras Japón invadía por fuera.',
  [('Ago 1927','Nanchang y Cosecha de Otoño','Nace el Ejército Rojo de Obreros y Campesinos.'),('Sep 1931','Invasión de Manchuria','Japón crea el régimen títere de Manchukuo.'),('1936','Incidente de Xi\'an','Generales del KMT apresan a Chiang y lo fuerzan a un Segundo Frente Unido.')]),
 rings('Una guerra que se gana desde el campo, rodeando las ciudades.','村',
  [('El campo','Guerrillas y zonas liberadas en el norte y centro.'),('Las ciudades','Ocupadas por Japón: se rodean, no se atacan primero.'),('Yan\'an','Base del "tres tercios", la Nueva Democracia y la Línea de Masas.')],
  note='Esquema de la "Guerra Prolongada" formulada por Mao tras julio de 1937.',aria='Círculos concéntricos: el campo al centro y las ciudades alrededor.'),
 steps('Tres campañas bastaron para destruir al ejército nacionalista.',
  [('1946','Guerra de Liberación','Tras fracasar las Negociaciones de Chongqing.'),('Sep 1948 – Ene 1949','Tres Grandes Campañas','Liaoxi-Shenyang, Huaihai y Beiping-Tianjin.'),('1 oct 1949','Nace la RPC','El KMT se repliega a Taiwán.')]),
 timeline('Lo que nació en la guerra sigue vigente: el Partido dirige al fusil.',
  [('1927','Sanwan: filiales del Partido en cada compañía.'),('1949','El fin del "Siglo de la Humillación" funda la legitimidad.'),('Hoy','"Democracia Popular en Todo el Proceso", heredera de la Nueva Democracia.')]),
]
T=[('Primer Frente Unido','Alianza de 1923 entre el Partido Comunista y el Kuomintang para unificar China.'),
 ('Reorganización de Sanwan','Reforma que puso una filial del Partido en cada compañía militar: el Partido manda sobre el ejército.'),
 ('Manchukuo','Régimen títere que Japón estableció en Manchuria tras 1931.'),
 ('Guerra Prolongada','Teoría de Mao: resistir a Japón con guerrillas y cercar las ciudades desde el campo.'),
 ('Nueva Democracia','Doctrina formulada por Mao en 1940 para las bases regionales como Yan\'an.'),
 ('Programa Común','Documento aprobado en septiembre de 1949 que sirvió de constitución provisional.')]
