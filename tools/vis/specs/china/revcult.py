from visgen import *
PATH='revolucion-cultural'
V=[
 versus('Mao temía que el Partido se aburguesara; el aparato pragmático temía su voluntad.',
  ['Liu Shaoqi: presidente','Deng Xiaoping: secretario general','Gestión cotidiana pragmática'],
  ['Mao teme el "revisionismo" de estilo soviético','Luchas de facciones en la cúpula','1962: purga de Xi Zhongxun'],labels=('El aparato','La desconfianza'),neutral=True),
 flow('Mao saltó por encima del Partido y llamó a los jóvenes.',
  [('May 1966','Circular del 16 de Mayo','Con el Grupo Central de la Revolución Cultural.'),('Llamado','Bombardear los Cuarteles Generales','Contra los "autócratas capitalistas".'),('Guardias Rojos','Contra las "Cuatro Viejas"','Universidades paralizadas y una ola de iconoclasia.')]),
 stats('Se destruyó el aparato de justicia y se desterró a una generación.',
  [S('10 M+','jóvenes urbanos enviados a aldeas remotas',to=None),S('1969','Liu Shaoqi muere en prisión y Deng es desterrado',to=None),S('7 años','de trabajo manual de Xi Jinping en Liangjiahe, Shaanxi',to=None)]),
 steps('El ejército puso orden y una banda de cuatro heredó el caos.',
  [('1969','Lin Biao, sucesor','El EPL asume el control administrativo.'),('Sep 1971','Muere Lin Biao','Su avión se estrella en Mongolia.'),('Oct 1976','Cae la Banda de los Cuatro','Un mes después de la muerte de Mao.')]),
 versus('El mismo trauma produjo dos respuestas opuestas.',
  ['Liderazgo colectivo','Límites de mandato y retiro obligatorio','Separación entre Partido y gobierno'],
  ['Poder concentrado en el centro','Disciplina leninista férrea','Autoridad jerárquica, no movilización de masas'],labels=('Deng: dispersar','Xi: concentrar'),neutral=True),
]
T=[('revisionismo','Acusación de desviarse hacia el modelo soviético y alejarse del marxismo revolucionario.'),
 ('Guardias Rojos','Cuadrillas de jóvenes movilizados por Mao (Hongweibing) contra los "autócratas capitalistas".'),
 ('Cuatro Viejas','Viejas ideas, cultura, costumbres y hábitos: el blanco de la campaña.'),
 ('Comités Revolucionarios','Organismos que reemplazaron a los comités locales del Partido.'),
 ('Movimiento de Rusticación','Envío de jóvenes urbanos al campo para ser "reeducados".'),
 ('guanxi','Redes de lealtad personal.')]
