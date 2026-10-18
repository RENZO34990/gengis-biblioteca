from visgen import *
PATH='tiananmen-recentralizacion'
V=[
 versus('Una década de apertura que también destapó grietas.',
  ['Hu Yaobang y Zhao Ziyang','Diálogo social e institucionalización'],
  ['Chen Yun y los ancianos','Mercado subordinado a la planificación y al Partido'],labels=('Reformistas','Conservadores'),neutral=True),
 steps('Una muerte encendió la plaza y la cúpula se dividió.',
  [('Abr 1989','Muere Hu Yaobang','Marchas estudiantiles en Tiananmen y más de 130 ciudades.'),('Mayo 1989','Zhao negocia, Li Peng no','El Partido se divide ante la crisis.'),('4 jun 1989','Intervención militar','Tras imponer la ley marcial.')]),
 flow('Se purgó al reformista y el Partido volvió a mandar sobre el Estado.',
  [('1989','Cae Zhao Ziyang','Se frena la liberalización política.'),('1989','Jiang Zemin','Reúne Secretaría General, Presidencia y Comisión Militar.'),('Después','Partido sobre Estado','Se revierte la separación de funciones.')]),
 stats('Estabilidad como precio de entrada al mercado.',
  [S('×2','presupuestos de seguridad pública',to=2,pre='×'),S('1990','reabren las bolsas de Shanghái y Shenzhen',to=None),S('Disciplina','lealtad ideológica y centralismo democrático como regla de sucesión: "evitar otro Gorbachov"',to=None)]),
 timeline('El pacto de 1989 se sigue aplicando: mercado a cambio de control político.',
  [('1989','Desarrollo de mercado a cambio del control político del Partido.'),('2012','Xi hereda la lógica: ministerios bajo comisiones centrales del Partido.'),('Hoy','Solo un Partido-Estado fuerte garantiza estabilidad y prosperidad.')]),
]
T=[('Reforma y Apertura','Política iniciada por Deng Xiaoping en 1978 para abrir y liberalizar la economía.'),
 ('jaula de pájaro','Idea conservadora: el mercado subordinado a la planificación.'),
 ('evolución pacífica','Idea de que potencias extranjeras buscan derrocar al régimen sin guerra.'),
 ('ley marcial','Régimen de excepción que impuso Deng Xiaoping antes de la intervención del 4 de junio.'),
 ('Gira al Sur','Viaje de Deng a principios de 1992 para romper el estancamiento de las reformas.'),
 ('weiwen','"Mantención de la estabilidad": prioridad de seguridad y control policial.')]
