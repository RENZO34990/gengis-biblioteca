from visgen import *
PATH='politica-del-sol'
V=[
 press('Con el Norte al borde del colapso, el Sur no podía permitirse un vecino roto.',
  ('Un Sur que necesitaba financiamiento','Tras el rescate del FMI, "Riesgo Corea" alto'),'38',
  ('Un Norte en la Ardua Marcha','Hambruna y colapso económico'),
  'Un derrumbe caótico del régimen le habría impuesto al Sur un <b>costo fiscal inasumible</b>.',core_small='1998'),
 rings('Tres principios para convivir sin absorber al vecino.','陽',
  [('Cero tolerancia','a la provocación armada del Norte.'),('Sin absorción','ni apoyo al colapso del régimen.'),('Coexistencia pacífica','con cooperación económica e intercambio humano.')],
  note='Los tres principios de Kim Dae-jung, 1998.',aria='Tres círculos concéntricos con los tres principios de la Política del Sol.'),
 timeline('Una distensión que se construyó con cumbres, fábricas y tratados.',
  [('1998','Hyundai abre el turismo al Monte Kumgang.'),('2000','Cumbre de Pionyang; Nobel de la Paz para Kim Dae-jung.'),('2003','Kaesong: más de 120 empresas y 50.000 trabajadores norcoreanos.'),('2004–07','TLCs con Chile, Singapur y EE. UU. (KORUS).')]),
 versus('Los dos veredictos sobre la distensión.',
  ['Erosionó el monopolio informativo del Norte con soft power','Comercio intercoreano de más de 1.800 millones de dólares anuales hacia 2007–2008'],
  ['Subsidió a Pionyang y le permitió armarse sin reformarse','Primer ensayo nuclear norcoreano en 2006'],labels=('Para unos','Para otros'),neutral=True),
 stats('Lo que quedó: más comercio abierto, el Norte cerrado y partidos divididos.',
  [S('+70%','del comercio de mercancías cubierto por TLCs',to=70,pre='+',suf='%'),S('2016','Kaesong cierra',to=None),S('30×','PIB per cápita del Sur frente al del Norte',to=30,suf='×')],
  note='Los TLCs cubren más de 70% del comercio de mercancías.'),
]
T=[('Haetbyeot Jeongchaek','Nombre coreano de la Política del Sol.'),
 ('Ardua Marcha','Nombre oficial norcoreano de la hambruna de los años 90.'),
 ('Kaesong','Complejo industrial al norte de la Zona Desmilitarizada, con capital del Sur y mano de obra del Norte.'),
 ('KORUS','Tratado de libre comercio entre Corea del Sur y Estados Unidos, firmado en 2007.'),
 ('peojugi','Crítica conservadora: "política de generosidad indiscriminada" hacia el Norte.'),
 ('Iniciativa END','Marco de Lee Jae-myung: Exchange, Normalization, Denuclearization.')]
