from visgen import *
PATH='shogunato-tokugawa'
V=[
 rings('Japón se cerraba, pero el cañón ya llegaba hasta Nagasaki.','鎖',
  [('El shogunato','Edicto de Sakoku de 1635: nadie sale ni entra.'),('Nagasaki','Único puerto, solo con holandeses y chinos.'),('Rusia y Gran Bretaña','Presionan desde el norte y desde el sur.')],
  note='Esquema del aislamiento, no un mapa.',
  aria='Tres círculos concéntricos: el shogunato al centro, Nagasaki alrededor y las potencias afuera.'),
 steps('Dos amenazas, 45 años: el sistema ya estaba roto antes de Perry.',
  [('Jul 1853','Perry en la bahía de Tokio','Abre los puertos a cañonazos.'),('1825','Edicto de Expulsión','Disparar contra todo barco occidental.'),('1808','HMS Phaeton','Amenaza a Nagasaki y nadie puede detenerlo.')],
  note='De abajo hacia arriba. Esquema, no a escala.',ship=True,up=True),
 flow('Adoptar métodos occidentales para mantener fuera a Occidente.',
  [('Norte','Mapas','Expediciones como la de Mamiya Rinzō fijan límites.'),('Estudio','Leyes y técnica','La élite traduce modelos occidentales.'),('1867–68','Satsuma y Chōshū','Deponen al bakufu y restituyen al Emperador.')]),
 switches('1868 desmontó el orden Tokugawa en tres frentes.','Pilares del régimen',
  [('藩','Dominios feudales','Abolidos'),('身','Distinciones hereditarias','Abolidas'),('帝','Soberanía del Emperador','Símbolo sagrado e inviolable')],
  on='En pie',off='Cambiado'),
 versus('Japón sigue sin decidir si 1868 fue ruptura o continuidad.',
  ['Despotismo superado por la "luz" imperial','Lectura oficial Meiji'],
  ['250 años de estabilidad y primeras misiones diplomáticas','Katsu Kaishū: legado Tokugawa'],labels=('Narrativa oficial','Contralectura'),neutral=True),
]
T=[('sakoku','Política de aislamiento internacional de los Tokugawa.'),
 ('bakufu','Gobierno militar del shogun.'),
 ('Edicto de Expulsión','Decreto de 1825: disparar de inmediato contra embarcaciones occidentales sospechosas.'),
 ('escuela de Mito','Corriente de intelectuales nacionalistas, como Aizawa Seishisai.'),
 ('Misión Iwakura','Delegación (1871-1873) que estudió Estados Unidos y Europa.'),
 ('Kokutai','La esencia tradicional japonesa.')]
