from visgen import *
PATH='xi-jinping-recentralizacion'
V=[
 versus('Un equilibrio de facciones que degeneró en parálisis y corrupción.',
  ['Facción de Shanghái: Jiang Zemin y princelings'],
  ['Facción Tuanpai: Hu Jintao y la Liga de la Juventud'],labels=('"Un partido, dos coaliciones"','2002–2012'),neutral=True),
 steps('Un escándalo en Chongqing dio a Xi un mandato de mano dura.',
  [('2012–13','Escándalos','Bo Xilai, Ling Jihua y Zhou Yongkang.'),('2012','18º Congreso','Xi asume Secretaría General y Comisión Militar Central.'),('Después','Presidencia','Ofensiva contra las redes faccionales rivales.')]),
 stats('Diez años para desmontar el equilibrio de Deng.',
  [S('1.4 M+','miembros del Partido sancionados',to=1.4,dec=1,suf=' M+'),S('2018','se abole el límite de dos mandatos',to=None),S('2022','el 20º Congreso rompe "7 arriba, 8 abajo"',to=None)]),
 flow('El gobierno pasó de par del Partido a ejecutor de sus decisiones.',
  [('Principio','Fin de la separación','Se erradica "dang zheng fenkai".'),('2023','Reglas del Consejo de Estado','Bajo Li Qiang: mero ejecutor del Centro.'),('Obligatorio','Dos Establecimientos y Dos Salvaguardas','Xi como núcleo, su autoridad protegida.')]),
 versus('Tras Xi: mayor control, pero más incertidumbre sobre la sucesión.',
  ['"El Partido lidera todo"','Seguridad Nacional Holística','Control ideológico del sector privado y la sociedad civil'],
  ['Sin sucesor aparente en el Comité Permanente','Sin equilibrio de facciones','Riesgo de crisis de sucesión'],labels=('Lo que se concentra','Lo que se pierde'),neutral=True),
]
T=[('Facción de Shanghái','Grupo vinculado a Jiang Zemin y a los princelings, hijos de dirigentes históricos.'),
 ('Tuanpai','Facción vinculada a la Liga de la Juventud Comunista, liderada por Hu Jintao.'),
 ('Comisión Central de Inspección de la Disciplina','Organismo con el que Xi encabezó la campaña anticorrupción.'),
 ('Comisiones Centrales','Órganos del Partido creados y liderados por Xi, que respondían a él directamente.'),
 ('dang zheng fenkai','Principio de "separación entre Partido y Gobierno".'),
 ('Democracia Popular en Todo el Proceso','Concepto con el que Xi redefine la legitimidad política.')]
