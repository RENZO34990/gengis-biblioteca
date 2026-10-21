from visgen import *
PATH='milagro-rio-han'
V=[
 stats('Un país agrario que vivía de la ayuda y que el mundo daba por perdido.',
  [S('+80%','de la población en subsistencia rural o pobreza urbana extrema',to=80,pre='+',suf='%'),S('70 US$','PIB per cápita en 1954',to=70,suf=' US$'),S('"Caso desesperado"','como lo catalogaban los organismos internacionales',to=None)]),
 press('Sin divisas y sin crédito, Park negoció con los dos lados a la vez.',
  ('Estados Unidos','Créditos condicionados a devaluar el won y a generar divisas propias'),'1963',
  ('Los empresarios','Arrestados por "acumulación ilícita de riqueza"'),
  'Park no les confiscó los activos: los obligó a <b>construir fábricas exportadoras</b> bajo supervisión del Estado.',core_small='<100 M US$'),
 flow('Un superministerio, un crédito condicionado y un solo criterio: exportar.',
  [('1961','EPB','Unificó el presupuesto, el capital extranjero y los planes quinquenales.'),('Crédito','Bancos nacionalizados y KDB','Créditos muy subsidiados a quien cumpliera metas de exportación.'),('Condición','Exportar para recibir','El desempeño exportador era el único criterio de subsidio.'),('1973','Industria Pesada y Química','Seis sectores: acero, astilleros, maquinaria, electrónica, petroquímica y metales no ferrosos.')]),
 stats('Una modernización comprimida: de zapatos y textiles a acero, barcos y camiones.',
  [S('9,7%','crecimiento del PIB en el Segundo Plan (1967–1971)',to=9.7,dec=1,suf='%'),S('10,1%','crecimiento del PIB en el Tercer Plan (1972–1976)',to=10.1,dec=1,suf='%'),S('10.000 M','dólares exportados en 1977, desde 55 M en 1962',to=None)]),
 versus('El milagro dejó un núcleo exportador y una lección sobre sus límites.',
  ['Samsung, Hyundai y SK, pilares del PIB y de la I+D','Política industrial por misiones: IA y baterías de litio'],
  ['Endeudamiento masivo en los años 70','Vulnerabilidad ante los choques petroleros'],labels=('Lo que dejó','Lo que enseñó'),neutral=True),
]
T=[('GARIOA y ECA','Programas de ayuda económica de Estados Unidos en la posguerra.'),
 ('Ley Especial sobre Acumulación Ilícita de Riqueza','Ley de 1961 con la que Park arrestó a los grandes empresarios acusándolos de corrupción.'),
 ('EPB','Junta de Planificación Económica: el superministerio que unificó presupuesto y planes.'),
 ('KDB','Banco de Desarrollo de Corea: daba créditos subsidiados a quien cumplía metas de exportación.'),
 ('Saemaul Undong','Movimiento de 1970 que llevó cemento y acero a los pueblos para caminos, electricidad y techos.'),
 ('KIST','Instituto tecnológico creado en 1966.')]
