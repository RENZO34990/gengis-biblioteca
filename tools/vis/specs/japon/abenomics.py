from visgen import *
PATH='abenomics'
V=[
 press('A fines de 2012 la política monetaria ya no tenía herramientas: el yen caro y la deflación se reforzaban entre sí.',
  ('Yen en récord','Cerca de 70 yenes por dólar: la industria se deslocaliza'),'0%',
  ('Deflación','La tasa nominal de 0% era real positiva: conviene guardar efectivo'),
  'Resultado: una economía <b>2% por debajo de su potencial</b> y sin palancas convencionales.',core_small='LÍMITE'),
 steps('Cuatro meses bastaron para cambiar el régimen de política económica.',
  [('Dic 2012','Abe vuelve al poder','Victoria aplastante del PLD con el compromiso de erradicar la deflación.'),
   ('Ene 2013','Declaración conjunta','Gobierno y BOJ fijan por primera vez una meta de inflación de 2%.'),
   ('Abr 2013','Kuroda al BOJ','Compra masiva de bonos para duplicar la base monetaria.')]),
 switches('Tres flechas disparadas a la vez, no una medida aislada.','Flechas en marcha',
  [('金','Monetaria','QQE desde abril de 2013 y tasa de -0.1% en 2016'),('財','Fiscal','Estímulo flexible e impuesto al consumo de 5% a 8% en 2014'),('改','Reformas','Womenomics, gobernanza corporativa, CPTPP y Society 5.0')],
  on='Disparada',off='Pendiente'),
 stats('El pleno empleo llegó antes que el aumento de sueldos.',
  [S('5.4 M','empleos nuevos, más de 2 millones regulares',to=5.4,dec=1,suf=' M'),S('2.8–3%','desempleo en mínimos históricos',to=None),S('100–120','yenes por dólar, desde 70',to=None)],
  note='Los salarios reales cayeron por los precios importados y el impuesto al consumo.'),
 timeline('De salvar la demanda a crear oferta: la normalización monetaria más larga de su historia reciente.',
  [('2013','Meta de inflación de 2% y QQE.'),('Mar 2024','El BOJ termina la política de tasas negativas.'),('Jun 2026','La tasa llega a 1%.'),('Hoy','Takaichi dirige inversión a 17 sectores prioritarios para ampliar la capacidad productiva.')]),
]
T=[('Flexibilización Monetaria Cuantitativa y Cualitativa','Programa del Banco de Japón desde 2013: comprar bonos a gran escala para ampliar el dinero en circulación.'),
 ('Womenomics','Política para incorporar a más mujeres a la fuerza laboral.'),
 ('CPTPP','Acuerdo comercial transpacífico del que Japón es parte.'),
 ('Society 5.0','Estrategia para integrar robótica e IA ante el colapso demográfico.'),
 ('límite inferior de cero','Punto en que el banco central ya no puede bajar más la tasa de interés nominal.'),
 ('Economía de Oferta Moderna','Enfoque que busca aumentar la capacidad productiva del país, no su demanda.')]
