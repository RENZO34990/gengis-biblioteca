from visgen import *
PATH='estado-desarrollista'
V=[
 bars('Antes del milagro, Japón vendía lo barato y seguía siendo un país de campesinos.',
  [('Plantas industriales destruidas','~40%',40),('Población activa en el campo, 1955','40–42%',42,True),('Exportaciones de textil y ligera, preguerra','80%',80,True)],
  note='Cifras del texto, escala de 0 a 100%.'),
 press('Abrirse sin preparación habría arrasado a las industrias jóvenes: la apertura llegaba por los dos lados.',
  ('Presión de Washington','Liberalizar el comercio y entrar al Artículo 8 del FMI'),'日本',
  ('Industrias jóvenes','Pequeñas, caras y sin escala para competir'),
  'Respuesta: en vez de proteger pasivamente, <b>reestructurar la industria por adelantado</b>.',core_small='1955–60'),
 flow('El Estado no fabricó: orientó. Cada pieza empujaba hacia la industria pesada.',
  [('1960','Ikeda','Plan de Duplicación de Ingresos: inversión privada, rebajas de impuestos, industria pesada y química.'),
   ('MITI','Orientación administrativa','Protege acero, astilleros, autos y electrónica; compra patentes y autoriza "carteles de racionalización".'),
   ('Keiretsu','Redes con banco principal','Participaciones cruzadas que protegen del accionista cortoplacista.')],
  note='Esquema del mecanismo, no un organigrama.'),
 stats('Una década de crecimiento sin precedentes.',
  [S('10.8%','crecimiento real del PIB, primera mitad de los 60',to=10.8,dec=1,suf='%'),S('12.8%','crecimiento anual entre 1965 y 1970',to=12.8,dec=1,suf='%'),S('1968','Japón supera a Alemania Occidental',to=None)]),
 versus('El mismo Estado que fabricó el milagro hoy administra sus costos.',
  ['1960: "picking winners" con el MITI','Un país joven, empleo de por vida'],
  ['2025: 17 sectores estratégicos de "Sanaenomics"','Deuda sobre 200% del PIB y escasez de mano de obra'],labels=('El modelo original','Su herencia')),
]
T=[('Doctrina Yoshida','Línea de posguerra: seguridad a cargo de Estados Unidos y energía puesta en la economía, no en el gasto militar.'),
 ('MITI','Ministerio de Comercio Internacional e Industria: el organismo que guiaba la política industrial.'),
 ('keiretsu','Grupos de empresas unidos por participaciones accionarias cruzadas y un banco principal.'),
 ('zaibatsu','Conglomerados familiares anteriores a la guerra, disueltos durante la ocupación.'),
 ('orientación administrativa','Instrucciones informales del ministerio, sin respaldo de ley, que las empresas seguían.'),
 ('METI','Ministerio de Economía, Comercio e Industria: el sucesor del MITI desde 2001.')]
