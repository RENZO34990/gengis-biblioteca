from visgen import *
PATH='gwangju-junio-1987'
V=[
 flow('La dictadura no terminó con Park: cambió de general.',
  [('Oct 1979','Primavera de Seúl','Breve esperanza tras el asesinato de Park.'),('12 dic 1979','Golpe de Chun Doo-hwan','Con la facción Hanahoe neutraliza al presidente interino.'),('1980','Quinta República','Presidencia indirecta, decretos y libertades suspendidas.')]),
 press('Lo que el régimen quiso borrar se volvió su acusación más difícil de responder.',
  ('Paracaidistas','Disparos y bayonetas contra estudiantes y civiles'),'光州',
  ('Autogobierno ciudadano','Comités que dirigieron la ciudad'),
  'Ocultada como "motín comunista", la masacre se volvió el <b>hito moral</b> contra la dictadura.',core_small='18–27 MAYO'),
 timeline('Una insurrección pacífica que el ejército no pudo reprimir.',
  [('Ene 1987','Muere Park Jong-chul bajo tortura y el Estado lo encubre.'),('13 abr','Chun congela la reforma constitucional y designa sucesor a Roh Tae-woo.'),('Junio','La coalición Guk-bon suma a más de 1,5 millones de ciudadanos.'),('29 jun','Declaración del 29 de Junio: elecciones directas, libertades y amnistía.')]),
 stats('La democracia llegó, pero el candidato del régimen aún ganó la primera elección.',
  [S('93%','aprobó la enmienda constitucional de octubre de 1987',to=93,suf='%'),S('+3.400','disputas laborales entre julio y septiembre de 1987',to=3400,pre='+'),S('36,6%','votos de Roh Tae-woo, con Kim Young-sam (28%) y Kim Dae-jung (27%) divididos',to=36.6,dec=1,suf='%')]),
 versus('Dos explicaciones de cómo llegó la democracia.',
  ['Katsiaficas y Namhee Lee','Fruto de la resistencia acumulada desde Gwangju'],
  ['Huntington, Adesnik y Sunhyuk Kim','Cálculo de los moderados ante los Juegos Olímpicos y una oposición dividida'],labels=('Resistencia popular','Cálculo de los moderados'),neutral=True),
]
T=[('Primavera de Seúl','Breve fase de esperanza democrática tras la muerte de Park.'),
 ('Hanahoe','Facción militar que respaldó a Chun Doo-hwan.'),
 ('Minjung','Movimiento popular de estudiantes, sindicatos e instituciones religiosas.'),
 ('CPAJ','Asociación de Sacerdotes Católicos por la Justicia.'),
 ('Declaración del 29 de Junio','Anuncio de Roh Tae-woo que aceptó elecciones directas, libertades civiles y amnistía.'),
 ('KCTU','Confederación sindical independiente nacida del auge laboral de 1987.')]
