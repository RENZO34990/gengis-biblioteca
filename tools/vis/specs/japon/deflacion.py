from visgen import *
PATH='deflacion-decadas-perdidas'
V=[
 versus('Detrás de la burbuja había un pacto social rígido y una trampa especulativa.',
  ['Empleo de por vida y salarios por antigüedad','Corporaciones keiretsu con participaciones cruzadas'],
  ['Operaciones especulativas de cartera (zaitech)','Suelo de Tokio: precios triplicados entre 1985 y 1989'],labels=('El pacto de posguerra','La burbuja'),neutral=True),
 press('Cuando el suelo cayó, también cayeron las garantías de todo el crédito.',
  ('Precio del suelo','Caídas anuales de 19% en terrenos residenciales'),'担保',
  ('Balances bancarios','Préstamos no realizables en bancos y aseguradoras'),
  'Resultado: un sistema financiero <b>expuesto de inmediato</b>.',core_small='1991'),
 flow('Rescatar en vez de liquidar: el origen de las empresas zombi.',
  [('1998–99','Capital público','9.3 billones de yenes a los grandes bancos, con permiso para posponer pérdidas.'),
   ('Bancos','Refinanciar insolventes','Corporaciones "demasiado grandes para caer" siguen vivas.'),
   ('1999 y 2001','ZIRP y QE','La tasa cero y la flexibilización cuantitativa llegan primero a Japón.')]),
 steps('Un año de quiebras en cadena y una generación sin empleos estables.',
  [('Nov 1997','Quiebras en cascada','Sanyo Securities, Hokkaido Takushoku y Yamaichi.'),
   ('1998','Nacionalización','El Long-Term Credit Bank of Japan pasa al Estado.'),
   ('2002','Desempleo récord de 5.4%','Los graduados viven el "Glaciar del Empleo".')]),
 stats('Tres décadas de estancamiento dejan cifras que no se mueven.',
  [S('1.14%','crecimiento anual del PIB, 1991–2003',to=1.14,dec=2,suf='%'),S('250%+','deuda pública sobre el PIB',to=None),S('11–13%','caída de salarios reales desde el pico de 1997',to=None)],
  note='Más de un tercio de la fuerza laboral tiene hoy contratos temporales o no tradicionales.'),
]
T=[('zaitech','Operaciones especulativas de cartera con que las empresas disfrazaban su debilidad operativa.'),
 ('recesión de balance','Cuando las empresas, con deudas por encima de su valor neto, dejan de invertir y solo pagan deuda.'),
 ('ZIRP','Política de tasa de interés cero.'),
 ('Glaciar del Empleo','Los años en que los jóvenes graduados no lograban empleos regulares estables.'),
 ('empresas zombi','Compañías insolventes mantenidas vivas por refinanciamientos de los bancos.'),
 ('MUFG','Uno de los tres megabancos que dominan hoy el sector, junto con SMBC y Mizuho.')]
