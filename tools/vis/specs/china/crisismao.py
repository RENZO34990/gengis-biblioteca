from visgen import *
PATH='crisis-maoismo'
V=[
 steps('1976: tres líderes muertos en nueve meses y un terremoto en medio.',
  [('Ene 1976','Muere Zhou Enlai','Su muerte desencadena el Incidente de Tiananmen de abril.'),('Jul 1976','Muere Zhu De y el terremoto de Tangshan','Una ciudad industrial destruida.'),('Sep 1976','Muere Mao Zedong','El Partido-Estado queda paralizado por las facciones.')]),
 versus('Hua Guofeng arrestó a la Banda de los Cuatro, pero quiso repetir el Gran Salto.',
  ['6 oct 1976: arresto de la Banda de los Cuatro','Doctrina de los "Dos Cualquier"'],
  ['Plan Decenal: 120 grandes complejos industriales','Importación apresurada de plantas, sin divisas'],labels=('Política','Economía'),neutral=True),
 steps('Un debate sobre la verdad decidió el rumbo del país.',
  [('Jul 1977','Deng es rehabilitado','Empieza a erosionar la base doctrinal de Hua.'),('May 1978','Criterio de la Verdad','"La práctica es el único criterio para probar la verdad".'),('18–22 dic 1978','Tercer Pleno','Se abandona la "lucha de clases" y se adopta la Reforma y Apertura.')]),
 stats('En menos de un año: del campo clandestino a las primeras zonas especiales.',
  [S('4,800+','proyectos pesados cancelados o suspendidos en abril de 1979',to=None),S('4','primeras ZEE: Shenzhen, Zhuhai, Shantou y Xiamen',to=4),S('6.5 M','jóvenes que regresaron del campo y recibieron negocios privados legales',to=None)]),
 flow('Del trauma del maoísmo tardío salieron un método, un lema y una regla de sucesión.',
  [('Lema','Teoría del Gato','Lo importante es cazar ratones, no el color del gato.'),('Método','Tocar las piedras','Probar en lo local antes de aplicar a nivel nacional.'),('Regla','Liderazgo colectivo','Sucesión ordenada; Xi hoy lo recentraliza en el "líder núcleo".')]),
]
T=[('Banda de los Cuatro','Jiang Qing, Zhang Chunqiao, Yao Wenyuan y Wang Hongwen, detenidos el 6 de octubre de 1976.'),
 ('Dos Cualquier','Doctrina de Hua Guofeng: defender cualquier decisión de Mao y seguir cualquier instrucción suya.'),
 ('Gaige Kaifang','Nombre chino de la política de Reforma y Apertura.'),
 ('getihu','Pequeños negocios privados individuales, legalizados en 1978.'),
 ('ZEE','Zonas Económicas Especiales: áreas abiertas a la inversión y al mercado, la primera frente a Hong Kong.'),
 ('líder núcleo','Figura que concentra el poder en la cúpula del Partido, según Xi Jinping.')]
