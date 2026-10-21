from visgen import *
PATH='crisis-gobernanza-ley-marcial'
V=[
 stats('Una democracia donde los rivales dejaron de verse como legítimos.',
  [S('5 años','mandato presidencial único',to=None),S('+90%','percibe conflicto agudo entre PPP y DPK',to=90,pre='+',suf='%'),S('2017','destitución de Park Geun-hye',to=None)]),
 versus('Un Ejecutivo sin mayoría contra un Legislativo hostil.',
  ['Yoon Suk-yeol ganó en 2022 por 0,73%','33 vetos contra proyectos opositores'],
  ['DPK con 175 de 300 escaños desde abril de 2024','29 mociones de censura e impeachment'],labels=('Presidente','Parlamento'),neutral=True),
 timeline('El autogolpe duró seis horas, pero el proceso llegó hasta cadena perpetua.',
  [('3 dic 2024','Yoon decreta la ley marcial.'),('4 dic','La Asamblea la anula por 190 a 0.'),('4 abr 2025','El Tribunal Constitucional confirma su destitución.'),('Feb 2026','Condena a cadena perpetua.')]),
 flow('La respuesta fue arreglar la regla, no solo castigar a quien la usó.',
  [('3 jun 2025','Elección anticipada','Gana Lee Jae-myung (DPK).'),('Tribunales','Condenas al gabinete','Kim Yong-hyun y Han Duck-soo reciben severas penas.'),('Jul 2025','Enmienda','Prohíbe que las fuerzas armadas bloqueen el ingreso de legisladores.')]),
 versus('Dos lecturas del autogolpe.',
  ['Consecuencia de décadas de normas rotas por ambos partidos','"El partido primero, la democracia después"'],
  ['Reacción eficaz de instituciones y ciudadanía','La cultura democrática de 1987 está arraigada'],labels=('Yul Sohn y Won-Taek Kang','Otros investigadores'),neutral=True),
]
T=[('presidencialismo imperial','Presidencia con muchas atribuciones y pocos contrapesos.'),
 ('PPP','Partido del Poder Popular, conservador.'),
 ('DPK','Partido Demócrata de Corea, progresista.'),
 ('impeachment','Juicio político para destituir a un alto cargo.'),
 ('autogolpe','Golpe de Estado dado desde el propio gobierno.'),
 ('Revolución de la Luz','Nombre con que se presentó la administración de Lee Jae-myung.')]
