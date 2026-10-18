from visgen import *
PATH='fundacion-rpc'
V=[
 stats('Un país arruinado: la fundación de 1949 partió de la parálisis.',
  [S('−30%','de la producción agrícola frente a su pico prebélico',to=None),S('≈½','de la maquinaria industrial de Manchuria, desmantelada por tropas soviéticas',to=None),S('10–30','años que el PCCh esperaba mantener la "Nueva Democracia"',to=None)]),
 steps('En tres años se apagó la hiperinflación, y luego se abandonó el gradualismo.',
  [('Mayo 1949','Renminbi','Se unifica el sistema monetario.'),('Jun 1950','Reforma Agraria','≈45% de la tierra cultivable a 300 millones de campesinos sin tierra.'),('1952','Transición directa','Mao deja la Nueva Democracia y apunta a la propiedad pública.')]),
 stats('Un plan, una constitución y un Partido-Estado.',
  [S('156','grandes proyectos industriales del Primer Plan Quinquenal',to=156),S('3,000+','expertos soviéticos asesoraron esos proyectos',to=None),S('96.3%','de los hogares campesinos, en cooperativas avanzadas a fines de 1956',to=96.3,dec=1,suf='%')]),
 bars('El costo quedó oculto bajo las cifras de crecimiento: la industria pesada se llevó casi todo.',
  [('Industria pesada (inversión estatal fija)','45–58.2%',58),('Agricultura','menos de 8%',8,True)],
  note='La brecha entre ciudad y campo tensionaría el suministro de alimentos.'),
 timeline('El molde de 1953 sigue vigente: planes, empresas estatales y centralización.',
  [('1953','El Primer Plan Quinquenal inaugura la herramienta.'),('2017','Xi redefine la "contradicción principal" del 8º Congreso de 1956.'),('2026–2030','El 15º Plan Quinquenal mantiene el instrumento.')]),
]
T=[('Programa Común','Documento de septiembre de 1949 que sirvió de constitución provisional.'),
 ('Nueva Democracia','Etapa inicial con economía de varios sectores, que el PCCh pensaba mantener entre 10 y 30 años.'),
 ('Tonggou tongxiao','Monopolio estatal de compras y ventas obligatorias de grano, establecido en 1953.'),
 ('Nomenklatura','Sistema por el que el Departamento de Organización del PCCh nombra a todos los cuadros dirigentes.'),
 ('Hukou','Registro de residencia que frenaba la migración del campo a la ciudad.'),
 ('Danwei','Unidad de trabajo a la que quedaba atado cada trabajador urbano, con empleo, vivienda y salud.'),
 ('SASAC','Organismo que supervisa a las empresas estatales.')]
