from visgen import *
PATH='semiconductores-ia'
V=[
 steps('De la crisis de 1997 a la memoria: liderazgo de Corea con tecnología ajena.',
  [('1999','Big Deals','El Estado fusiona LG Semicon con Hyundai Electronics y nace Hynix.'),
   ('2000–2017','Líder en DRAM y NAND','Samsung y Hynix ocupan posiciones de liderazgo mundial.'),
   ('Siempre','Máquinas y químicos importados','Litografía de Japón, Europa y EE. UU.; ingresos atados al precio de la DRAM.')],
  note='Orden de los hechos, de arriba abajo. Esquema, no a escala.'),
 press('Atrapada entre dos potencias, y con una nueva pared de memoria.',
  ('Estados Unidos','Controles de exportación y CHIPS Act: tope a las plantas en China'),'칩',
  ('China','Restringe galio, germanio y grafito'),
  'La IA exigía <b>HBM</b>, memoria apilada de alto ancho de banda que la DRAM común no daba.',core_small='2018–23'),
 switches('Tres pilares y una apuesta: el Estado blindó los chips por ley.','Piezas ya en marcha',
  [('法','K-Chips Act','Crédito fiscal de 15% a 20%, hasta 30% para pymes'),('帶','K-Semiconductor Belt','622 billones de wones hasta 2047, en Gyeonggi'),('機','Estrategia AI G3','10,1 billones de wones en 2026, 35.000 GPUs')],
  on='En marcha',off='Pendiente'),
 stats('Un solo producto, la memoria para IA, sostiene casi un tercio de las exportaciones.',
  [S('20.540 M','de dólares exportados en chips en enero de 2026',to=None),S('+102,7%','interanual',to=102.7,dec=1,pre='+',suf='%'),S('31%','de las exportaciones totales',to=31,suf='%')]),
 versus('Salir de la trampa del ensamble: competir por tecnología, no por costos.',
  ['Memoria estándar y guerras de precios','Dependencia de equipos importados'],
  ['HBM4, CXL, PIM y fotónica','Ley Especial de Semiconductores (2026–2036)'],labels=('El punto de partida','El rumbo')),
]
T=[('HBM','Memoria de alto ancho de banda, apilada verticalmente, que usan las GPU de IA.'),
 ('DRAM','Memoria de acceso rápido de los computadores, estándar durante décadas.'),
 ('NAND flash','Memoria de almacenamiento que conserva los datos sin energía.'),
 ('CHIPS and Science Act','Ley de EE. UU. de 2022 que subsidia chips y limita inversiones en China.'),
 ('K-Chips Act','Ley coreana de créditos fiscales para semiconductores, IA y baterías.'),
 ('NPUs','Procesadores diseñados para tareas de inteligencia artificial.')]
