from visgen import *
PATH='acuerdo-del-plaza'
V=[
 press('El éxito exportador de Japón se volvió un problema político en Washington.',
  ('Superávit con EE. UU.','Autos, acero y electrónica competitivos; dólar 50% más fuerte entre 1980 y 1985'),'日米',
  ('Congreso de EE. UU.','Debate seriamente aranceles proteccionistas'),
  'Respuesta: un pacto para <b>abaratar el dólar frente al yen</b>.',core_small='1985'),
 flow('Cinco ministros de finanzas, un hotel y una sola dirección para el dólar.',
  [('22 sep 1985','Hotel Plaza, Nueva York','EE. UU., Japón, Alemania Occidental, Francia y Reino Unido firman el pacto.'),
   ('Mecanismo','Intervención coordinada','Los bancos centrales actúan en los mercados cambiarios.'),
   ('Efecto','Recesión del Yen Alto','El PIB crece 3.3% en 1986, frente a 5.2% en 1985.')],
  note='Esquema del encadenamiento, no a escala.'),
 steps('El dinero barato salió de la industria y se fue a la tierra.',
  [('1986–87','Cinco recortes de tasa','El BOJ baja la tasa de descuento hasta 2.5% en febrero de 1987.'),
   ('1987–89','Tasa congelada','Se mantiene en el mínimo hasta mayo de 1989.'),
   ('Bancos','Crédito a la tierra','Pequeñas empresas y préstamos especulativos con terrenos como garantía.'),
   ('Impuestos','Distorsión fiscal','Sucesiones de 75%, con la tierra valorada a la mitad: endeudarse para comprar evadía impuestos.')]),
 stats('Una burbuja de proporciones inéditas.',
  [S('122%','alza en zonas comerciales de Tokio en 1986',to=122,suf='%'),S('30 M','yenes por metro cuadrado en Ginza, 1989',to=None),S('2.5% → 6.0%','la tasa que subió el BOJ hasta agosto de 1990',to=None)],
  note='Los terrenos del Palacio Imperial llegaron a valer más que todo California.'),
 timeline('Una sola burbuja explica tres décadas de herencia.',
  [('1990','El Nikkei pierde 35% de su valor.'),('1999–2001','ZIRP y QE: política no convencional décadas antes que Occidente.'),('2001','Sumitomo y Mitsui forman SMBC.'),('Hoy','Deuda pública de más de 250% del PIB, frente a 65% en 1989.')]),
]
T=[('endaka fukyō','"Recesión del Yen Alto": la caída del crecimiento tras la fuerte apreciación del yen.'),
 ('keiretsu','Redes de empresas con participaciones cruzadas y un banco principal.'),
 ('empresas zombi','Compañías insolventes que sobreviven porque los bancos refinancian sus deudas.'),
 ('Décadas Perdidas','Largo periodo de crecimiento casi nulo y deflación que siguió al estallido.'),
 ('ZIRP','Política de tasa de interés cero.'),
 ('SMBC','Sumitomo Mitsui Banking Corporation, fusión bancaria de 2001.')]
