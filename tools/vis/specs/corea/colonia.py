from visgen import *
PATH='colonialismo-japones'
V=[
 press('Antes de 1910, el Estado coreano estaba atrapado entre un orden feudal y un banco extranjero.',
  ('Orden confuciano','Aristocracia yangban, sin registro de tierras ni moneda nacional'),'朝鮮',
  ('Capital japonés','Dai-Ichi cumple de hecho funciones de banco central desde 1905'),
  'Resultado: un Estado sin capacidad <b>fiscal, monetaria ni militar</b> para resistir.',core_small='ANTES DE 1910'),
 switches('La anexión de 1910 le quitó a Corea el control de su economía y su Estado.','Qué seguía en manos coreanas',
  [('主','Soberanía','El Imperio Coreano se disuelve'),('官','Cargos directivos','Reservados a ciudadanos japoneses'),('業','Grandes empresas','Propiedad reservada a japoneses')],
  on='En manos coreanas',off='En manos japonesas'),
 flow('El Gobierno General reorganizó la península como proveedor del imperio.',
  [('Catastro','Registro de tierras','Formaliza la propiedad privada y deja al Estado las tierras comunales.'),('Sur','Granero de Japón','Jeolla y otras provincias se especializan en arroz de exportación.'),('Norte','Retaguardia militar','Minería e industria pesada para las operaciones en China y Manchuria.')],
  note='Esquema del reparto de funciones.'),
 stats('Treinta y cinco años de extracción dejaron una infraestructura moderna y un pueblo empobrecido.',
  [S('35','años de dominio colonial (1910–1945)',to=35),S('1939','año en que se obligó a adoptar nombres japoneses',to=None),S('1945','Corea es liberada en pobreza severa',to=None)]),
 versus('Lo que 1945 no desmontó explica parte de la Corea del Sur de hoy.',
  ['Policía y burocracia con colaboradores (chinil)','Leyes de control político, modelo de la Ley de Seguridad Nacional de 1948'],
  ['3.551 propiedades japonesas vendidas a empresarios conectados','Base de los grandes chaebols'],labels=('Lo que se heredó del Estado colonial','Lo que se privatizó')),
]
T=[('Dai-Ichi','Banco privado japonés que cumplía de hecho funciones de banco central en Corea.'),
 ('Gobierno General','Régimen colonial absolutista dirigido por un gobernador general militar.'),
 ('Primero de Marzo','Movimiento de independencia de 1919, reprimido con dureza por Japón.'),
 ('Bunka Seiji','La "política cultural" que Japón adoptó tras 1919: control social y policial más sutil.'),
 ('chinil','Colaborador pro-japonés durante el periodo colonial.'),
 ('USAMGIK','Gobierno militar estadounidense en el sur de Corea tras 1945.'),
 ('zaibatsu','Conglomerados familiares japoneses; modelo de los chaebols.')]
