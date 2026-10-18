from visgen import *
PATH='autofortalecimiento'
V=[
 flow('Tras dos guerras y una rebelión, el imperio buscó copiar la técnica de Occidente para sobrevivir.',
  [('1856–64','Golpes seguidos','Segunda Guerra del Opio y Rebelión Taiping dejan al imperio exhausto.'),('1861','Tsungli Yamen','Nace la oficina para tratar con el extranjero.'),('1865–66','Arsenales','Arsenal de Kiangnan y Astillero de Foochow.')]),
 rings('Sabiduría china por dentro, técnica occidental por fuera: la estructura no se tocaba.','道',
  [('Fundamento (Ti)','Instituciones políticas, jurídicas y sociales confucianas, sin cambios.'),('Uso práctico (Yong)','Tecnología y aprendizaje occidental, injertados encima.'),('El problema','Nuevas fábricas sobre un Estado agrario y sin capital.')],
  note='El lema del movimiento: "sabiduría china como fundamento, aprendizaje occidental para uso práctico".',aria='Círculos concéntricos: el fundamento chino al centro, la técnica occidental alrededor.'),
 steps('Una flota de arsenales perdió contra un vecino que sí había cambiado sus instituciones.',
  [('1888','Flota de Peiyang','Tres décadas de inversión en arsenales.'),('1894–95','Guerra Sino-Japonesa','La Flota de Nanyang se declara "neutral" y Peiyang pelea sola.'),('17 abr 1895','Tratado de Shimonoseki','Corea independiente; Taiwán, Pescadores y Liaotung a Japón.')]),
 bars('Lo que la corte gastó en su placer pesó poco frente a lo que pagó a Japón.',
  [('Desviado del presupuesto naval al Palacio de Verano','≈30 M de taeles',15),('Indemnización de Shimonoseki','200 M de taeles',100,True)],
  note='El desvío equivale a cerca de una séptima parte de la indemnización.'),
 timeline('Las empresas estatales de hoy repiten una tensión que nació en los arsenales.',
  [('1861–95','Shanghái, Tianjin, Hankow y Guangzhou se vuelven metrópolis modernas.'),('Modelo kuan-tu shang-pan','El Estado supervisa, el mercado gestiona: antecedente de las actuales SOE.'),('Hoy','"Made in China 2025" y la autonomía tecnológica, para no depender de nadie.')]),
]
T=[('Tsungli Yamen','Oficina creada en 1861 para manejar la diplomacia con las potencias extranjeras.'),
 ('kuan-tu shang-pan','Fórmula de "supervisión oficial y gestión mercantil": el Estado vigila, los comerciantes administran.'),
 ('Ti-Yong','Lema: "sabiduría china como fundamento (ti), aprendizaje occidental para uso práctico (yong)".'),
 ('Tratado de Shimonoseki','Tratado de 1895 que cerró la guerra con Japón: Taiwán, Pescadores y Liaotung cedidos y 200 millones de taeles de indemnización.'),
 ('reparto del melón','Nombre con que se conoce la división de China en esferas de influencia entre las potencias.'),
 ('SOE','Siglas en inglés de las empresas estatales (State-Owned Enterprises).')]
