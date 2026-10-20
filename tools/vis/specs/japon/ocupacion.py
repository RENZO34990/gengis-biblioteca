from visgen import *
PATH='ocupacion-estadounidense'
V=[
 press('El mando militar escapaba al gabinete y la economía financiaba la guerra.',
  ('Artículo 11 de 1889','El mando supremo solo del soberano: el Ejército eludía a la Dieta'),'日本',
  ('Zaibatsu y campo','Mitsui, Mitsubishi, Sumitomo y Yasuda; campesinos como reclutas'),
  'En 1945 los cultivos habían caído a <b>menos de la mitad</b>: millones al borde de la hambruna.',core_small='1889–1945'),
 stats('Evitar el caos antes de reformar: la "política del pan".',
  [S('~1/3','del grano consumido llegó a ser distribuido por el SCAP',to=None),S('2 sep 1945','rendición incondicional',to=None),S('MacArthur','al frente del SCAP',to=None)]),
 switches('La Constitución de 1947 cambió quién manda.','Poderes del orden antiguo',
  [('神','Soberanía imperial','Pasa al pueblo'),('爵','Títulos aristocráticos','Abolidos'),('戦','Derecho a la guerra','Renuncia permanente (Art. 9)')],
  on='En pie',off='Cambiado'),
 timeline('Siete años de ocupación en cuatro movimientos.',
  [('1947','Constitución, sufragio femenino y reforma agraria.'),('1950','Estalla la Guerra de Corea: nace la Reserva Policial de 75,000.'),('1951','Tratado de San Francisco y Tratado de Seguridad.'),('1952','28 de abril: fin de la ocupación.')]),
 flow('La herencia: ministerios intactos, un partido y un artículo ambiguo.',
  [('SCAP','Purgas','La burocracia económica quedó casi intacta.'),('1955','LDP','Unificación conservadora; gobierna 38 años.'),('Hoy','Artículo 9','Su reforma sigue sin resolverse.')]),
]
T=[('SCAP','Supremo Comandante de las Potencias Aliadas, a cargo de la ocupación.'),
 ('tosuiken','Mando militar supremo, que la Constitución de 1889 daba solo al Emperador.'),
 ('zaibatsu','Conglomerados familiares que dominaban la economía japonesa.'),
 ('Reverse Course','Giro estadounidense hacia el anticomunismo, que frenó las reformas a finales de los 40.'),
 ('keiretsu','Grupos de empresas con participaciones cruzadas, sucesores de los zaibatsu.'),
 ('amakudari','"Descenso del cielo": funcionarios retirados pasan a cargos ejecutivos en empresas.')]
