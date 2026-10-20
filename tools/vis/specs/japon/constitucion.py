from visgen import *
PATH='constitucion-meiji'
V=[
 press('Sin constitución, la oligarquía gobernaba a medias entre el pueblo que exigía voz y Occidente que exigía "civilización".',
  ('Movimiento por la Libertad','Pide constitución y asamblea electa'),'寡頭',
  ('Occidente','Exige un Estado "civilizado" para renegociar los tratados desiguales'),
  'La oligarquía respondió con <b>censura (1875) y límites a las asambleas (1880)</b>.',core_small='1868–89'),
 steps('Un solo rescripto fijó la fecha y cambió la pregunta.',
  [('1881','Ōkuma propone el modelo británico','La facción de Iwakura Tomomi lo destituye.'),
   ('Oct 1881','Rescripto imperial','Promesa formal de una asamblea nacional para 1890.'),
   ('Después','Qué tipo de constitución','Ya no importa si habrá una, sino cuál.')]),
 versus('Itō descartó todo lo liberal y eligió el modelo alemán.',
  ['EE. UU.: demasiado liberal','Francia y España: tendencia al despotismo','Gran Bretaña: demasiado poder al parlamento'],
  ['Estructuras autoritarias del Imperio alemán','Kokutai: la identidad nacional en torno al trono'],labels=('Lo que descartó','Lo que adoptó')),
 stats('Una dieta con poder, pero con pocos votantes.',
  [S('1.1%','de la población podía votar',to=1.1,dec=1,suf='%'),S('15 yenes','de impuestos mínimos para votar',to=None),S('1890','se constituye la Dieta Imperial bicameral',to=None)],
  note='Los militares quedaron fuera del control civil por el Artículo 11.'),
 switches('Una herencia con dos caras: estabilidad y un vacío de control.','Rasgos que siguen vivos',
  [('憲','Constitución 1947','Se promulgó como enmienda al Artículo 73 de 1889'),('官','Burocracia de Kasumigaseki','Hereda a la meritocracia Meiji sobre los partidos'),('軍','Control civil del ejército','Su ausencia fue explotada en los años 30')],
  on='Continuidad',off='Ruptura'),
]
T=[('Jiyū Minken Undō','Movimiento por la Libertad y los Derechos del Pueblo, que pedía constitución y asamblea.'),
 ('kokutai','Identidad nacional aglutinada en torno a la dinastía imperial.'),
 ('Consejo Privado','Órgano creado en 1888 para ratificar el borrador de la constitución en secreto.'),
 ('tosuiken','Mando militar supremo, reservado al Emperador por el Artículo 11.'),
 ('genrō','Los viejos líderes de la oligarquía Meiji que decidían de modo informal.'),
 ('Kasumigaseki','Barrio de Tokio donde están los ministerios: sinónimo de la burocracia.')]
