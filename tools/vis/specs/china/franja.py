from visgen import *
PATH='franja-ruta-made-in-china-2025'
V=[
 stats('El motor de ladrillo y deuda empezaba a fallar.',
  [S('66 billones','de yuanes de deuda opaca de los gobiernos locales, ≈75% del PIB',to=None),S('2016','año en que la población en edad de trabajar empezó a contraerse',to=None),S('≈10%','de crecimiento anual promedio en tres décadas',to=None)]),
 versus('Dos planes paralelos: exportar infraestructura e importar menos tecnología.',
  ['Franja y la Ruta (2013): corredores logísticos y sobrecapacidad al exterior'],
  ['Made in China 2025 (mayo de 2015): potencia de alta tecnología en 10 sectores'],labels=('Hacia afuera','Hacia adentro')),
 flow('El Estado reasignó el capital hacia los "Nuevos Tres".',
  [('Vehículos','Nueva energía','Subsidios y créditos dirigidos.'),('Almacenamiento','Baterías de litio','Más del 70% de la cadena mundial.'),('Generación','Solar fotovoltaica','Más del 80% de los módulos.')]),
 bars('Cuota china de la producción mundial.',
  [('Baterías de litio','70%',70),('Módulos solares fotovoltaicos','80%',80,True)],
  note='En 2023 China exportó más de 4 millones de vehículos y superó a Japón como mayor exportador.'),
 timeline('De ensamblador de bajo costo a potencia industrial autónoma.',
  [('2013–2026','Se edifica la base industrial de alta tecnología.'),('2026–2030','El 15º Plan Quinquenal busca el pico de emisiones antes de 2030.'),('Hoy','Acusaciones de sobrecapacidad: aranceles, barreras y sanciones.')]),
]
T=[('Nueva Normalidad','Etapa de crecimiento más lento que sucedió a tres décadas de crecimiento cercano al 10%.'),
 ('Made in China 2025','Estrategia industrial de mayo de 2015 para pasar del ensamblaje barato a la alta tecnología.'),
 ('Doble Circulación','Estrategia de 2020 que fija el mercado interno como columna vertebral y busca autosuficiencia tecnológica.'),
 ('Xin San Yang','Los "Nuevos Tres": vehículos de nueva energía, baterías de litio y energía solar fotovoltaica.'),
 ('chain masters','"Directores de cadena": SOE centrales que aseguran el suministro nacional.'),
 ('Nuevas Fuerzas Productivas','Concepto de Xi Jinping desde 2023: productividad por innovaciones como IA y computación cuántica.')]
