from visgen import *
PATH='omc-potencia-manufacturera'
V=[
 stats('Un mercado abierto a medias, con una urgencia: dar empleo y entrar a las cadenas globales.',
  [S('16.6%','arancel general promedio en 2001',to=16.6,dec=1,suf='%'),S('21 M+','trabajadores urbanos despedidos tras 1997–98',to=None),S('Cuotas','textiles estrictas en Europa y Norteamérica',to=None)]),
 steps('Una firma cambió las reglas con más de 140 países a la vez.',
  [('Oct 2000','PNTR en EE. UU.','Fin de la incertidumbre anual sobre el estatus comercial de China.'),('11 dic 2001','Adhesión a la OMC','Acceso sin discriminación a los mercados de más de 140 países.'),('Desde 2001','Marco legal','El Estado ajusta sus normas a estándares internacionales.')]),
 bars('Los aranceles cayeron y las cuotas textiles desaparecieron.',
  [('Arancel industrial promedio, 2001','16.6%',100),('Arancel industrial promedio, 2005','8.9%',54,True)],
  note='En 2005 se abolieron las restricciones cuantitativas y el monopolio estatal de licencias.'),
 timeline('De tercera a segunda economía del mundo.',
  [('2007','Supera a Alemania: tercera economía.'),('2010','Primer exportador mundial; supera a Japón.'),('2012','Exportaciones de más de 2,000 mil millones de dólares.')]),
 stats('Escala que sostiene el liderazgo de hoy.',
  [S('≈30%','de la producción manufacturera mundial',to=None),S('120+','países para los que es el principal socio comercial',to=None),S('4 billones','de yuanes de estímulo ante la crisis de 2008',to=None)]),
]
T=[('Acuerdo sobre los Textiles y el Vestido','Acuerdo multilateral cuyos beneficios no alcanzaban a China antes de 2001.'),
 ('PNTR','Ley de Relaciones Comerciales Permanentes Normales de EE. UU., promulgada en octubre de 2000.'),
 ('nongmingong','Trabajadores migrantes rurales que se mueven a clusters industriales costeros.'),
 ('Ir al Exterior','Estrategia "Going Out" para que las empresas chinas se internacionalicen.'),
 ('friend-shoring','Relocalización de cadenas de suministro hacia países aliados.')]
