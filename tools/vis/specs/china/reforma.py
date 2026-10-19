from visgen import *
PATH='reforma-apertura'
V=[
 stats('Antes de 1978: igualdad en la pobreza, y todo por cuotas.',
  [S('>80%','de los artículos de primera necesidad dependía del racionamiento',to=None),S('100%','de la industria urbana era empresa estatal',to=None),S('0','mecanismos de mercado: precios, salarios e insumos asignados',to=None)]),
 steps('Un acuerdo secreto en una aldea cambió el campo; luego se abrió la costa.',
  [('Nov 1978','Xiaogang, Anhui','Campesinos arriendan en secreto la tierra colectiva por hogares.'),('Dic 1978','Tercer Pleno','El Partido respalda el pragmatismo de Deng.'),('1979–80','Cuatro ZEE','Shenzhen, Zhuhai, Shantou y Xiamen.')]),
 steps('Un jubilado sin cargo formal salvó la reforma con un viaje.',
  [('1988–89','Inflación y Tiananmen','Las reformas se paralizan entre 1989 y 1991.'),('Ene–feb 1992','Inspección del Sur','Deng recorre Shenzhen, Zhuhai y Guangzhou.'),('1992','14º Congreso','Primera meta oficial: "Economía de Mercado Socialista".')]),
 stats('De villa pesquera a metrópolis: la apertura se multiplicó por la costa.',
  [S('14','ciudades costeras abiertas en 1984, y Pudong en 1989',to=14),S('38%','de la producción industrial en manos de las TVE en 1993',to=38,suf='%'),S('1990–91','reabren las Bolsas de Shanghái y Shenzhen',to=None)]),
 versus('Gradualismo frente a terapia de choque.',
  ['Reforma local primero','Estabilidad macro y doble vía','Instituciones de mercado sin destruir la producción'],
  ['Colapso de la Unión Soviética y Europa del Este','Terapia de choque en los noventa'],labels=('China','Otros'),neutral=True),
]
T=[('Baogan taohu','Nombre chino del Sistema de Responsabilidad Familiar: tierra gestionada por hogares.'),
 ('Zonas Económicas Especiales','Áreas abiertas al capital y la tecnología, cerca de Hong Kong, Macao y Taiwán.'),
 ('jaula de pájaros','Idea conservadora: el mercado puede volar, pero solo dentro de los límites del plan.'),
 ('evolución pacífica','Temor conservador a un deslizamiento gradual hacia el capitalismo.'),
 ('TVE','Empresas de Pueblo y Aldea: industrias rurales que absorbieron la mano de obra excedente.')]
