from visgen import *
PATH='economia-mercado-zee'
V=[
 bars('El Estado central se había quedado casi sin ingresos propios.',
  [('Ingresos del gobierno central (antes)','35% del PIB',100),('Ingresos del gobierno central (1989–91)','11% del PIB',31,True),('Presupuesto central directo','3% del PIB',9,True)]),
 steps('Un anciano sin cargo rompió el estancamiento con un viaje.',
  [('Ene–feb 1992','Gira por el Sur','Deng, de 87 años, visita Shenzhen, Zhuhai y Guangzhou.'),('Sin cargo formal','"Mercado y planificación son herramientas"','Rompe el dogma de la ortodoxia.'),('Oct 1992','14º Congreso','Se declara la "Economía Socialista de Mercado".')]),
 flow('Zhu Rongji rediseñó el Estado desde los cimientos fiscales.',
  [('1994','Reforma fiscal','IVA de 17% y recaudación recentralizada en Pekín.'),('1994','Tipo de cambio','Unificado: 8.7 RMB por dólar.'),('1997–98','Agarrar lo grande','Más de 50,000 SOE pequeñas vendidas o liquidadas.'),('2001','OMC','Adhesión firmada el 11 de diciembre.')]),
 stats('Cambió el campo por la fábrica, pero con un costo social enorme.',
  [S('9–10%+','de crecimiento anual del PIB real; la economía se cuadruplicó entre 1978 y 2000',to=None),S('21 M+','trabajadores estatales despedidos',to=None),S('150 M','campesinos migraron a metrópolis costeras',to=None)]),
 versus('La reforma de 1994 explica tanto la fábrica del mundo como la deuda local de hoy.',
  ['Fábrica del mundo: más de 400 empresas Fortune 500','Estado dueño de las "alturas dominantes"'],
  ['Municipios con déficit estructural','Dependencia del mercado inmobiliario y LGFV'],labels=('Lo que se ganó','Lo que se heredó')),
]
T=[('doble vía','Sistema en que convivían precios fijados por el plan y precios de mercado, con distorsiones y especulación.'),
 ('Gira por el Sur','Viaje de Deng Xiaoping a las Zonas Económicas Especiales entre enero y febrero de 1992.'),
 ('Economía Socialista de Mercado','Objetivo de la reforma declarado en el 14º Congreso de 1992.'),
 ('Fenxieshi','Nombre chino de la reforma fiscal de 1994, que separó los impuestos entre Pekín y las provincias.'),
 ('tazón de arroz de hierro','Empleo estatal permanente con vivienda y salud.'),
 ('LGFV','Plataformas de inversión de los gobiernos locales, con deuda opaca.')]
