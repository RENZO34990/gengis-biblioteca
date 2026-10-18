from visgen import *
PATH='guerras-opio'

V=[
 rings('Pekín creía ser el centro del mundo, y que los demás venían a pedir permiso.','中',
  [('El emperador','El "Hijo del Cielo": el centro del orden.'),('Estados tributarios','Corea, Vietnam, Ryukyu: enviaban tributo y recibían reconocimiento.'),('El resto del mundo','Europa incluida: llegaba como suplicante al puerto de Cantón.')],
  note='Esquema de cómo veía la corte Qing el mundo. No es un mapa.',
  aria='Tres círculos concéntricos: el emperador al centro, los Estados tributarios alrededor y el resto del mundo afuera.'),
 steps('Una flota de vapor contra una de madera: cada derrota probó que China no podía decir que no.',
  [('1860 · Pekín','Las convenciones llegan a la capital','La última ronda de agresiones termina con nuevos papeles firmados.'),
   ('1858 · Tianjin','Segunda guerra, nuevos tratados','Varias potencias occidentales exigen más puertos y más derechos.'),
   ('1842 · Nankín','El primer tratado desigual','La flota británica llega al Yangtsé y la corte firma a bordo del HMS Cornwallis.'),
   ('1839–41 · Cantón','Humen y la respuesta británica','Lin Zexu destruye el opio; Gran Bretaña contesta con la flota.')],
  note='De sur a norte, en el orden en que avanzó la presión. Esquema, no a escala.',ship=True,up=True),
 switches('Las armas ganaron las batallas; los tratados le quitaron al Estado tres poderes.','Competencias que aún controla Pekín',
  [('海','Aduanas y puertos','Qué entra y qué sale del país'),('兵','Tropas en el territorio','Quién puede mantener fuerzas armadas'),('法','Justicia propia','Quién juzga a los extranjeros')],
  on='En manos de Pekín',off='Cedido a las potencias'),
 press('Presión de afuera y de adentro a la vez: el imperio sobrevivió, pero ya no era dueño de su casa.',
  ('Imperialismo extranjero','Capitales y mercancías que rompen la economía del campo'),'清',
  ('Estructuras feudales intactas','Una sociedad que no sabe absorber a los nuevos grupos'),
  'Resultado: la <b>Rebelión Taiping</b> (1850–1864), que casi derriba a la dinastía.',core_small='QING'),
 timeline('Lo que empezó en 1839 es hoy el argumento con el que Pekín explica su política.',
  [('1842','Nankín: el primer tratado desigual.'),('1912','Cae la última dinastía imperial.'),('1949','Nace la República Popular y declara cerrado el "siglo de la humillación".'),('2012','Xi Jinping presenta el "Sueño Chino" como la reparación de esa historia.')]),
]
T=[('Sistema de Cantón','El régimen anterior: los extranjeros solo podían comerciar en el puerto de Cantón, bajo reglas chinas.'),
 ('monarquía autocrática','Gobierno en el que una sola persona, el emperador, concentra todo el poder y nadie puede limitarlo.'),
 ('Humen','Puerto del río de las Perlas, cerca de Cantón, donde en 1839 se destruyó el opio confiscado.'),
 ('Nanjing (1842)','Primer tratado desigual, firmado el 29 de agosto de 1842: abrió cinco puertos y cedió Hong Kong a Gran Bretaña.'),
 ('La extraterritorialidad judicial','Un extranjero que comete un delito en China lo juzga su propio país, no un tribunal chino.'),
 ('Rebelión del Reino Celestial Taiping','Rebelión campesina (1850–1864) dirigida por Hong Xiuquan, con un cristianismo propio. Una de las guerras más mortíferas de la historia.'),
 ('PCCh','Partido Comunista de China, en el poder desde 1949.'),
 ('Sueño Chino','Lema de Xi Jinping desde 2012: el "gran rejuvenecimiento" de la nación china.')]
