from visgen import *
PATH='republica-senores-guerra'
V=[
 steps('La república heredó una economía que otros controlaban y un presidente que quiso ser emperador.',
  [('Oct 1911','Revolución de Wuchang','Cae la dinastía Qing tras más de 2,000 años de monarquía.'),('1912','Nace la república','Con banca, ferrocarriles y minas en manos extranjeras.'),('1911–16','Yuan Shikai','Reprime al Kuomintang y termina intentando proclamarse emperador.')]),
 stats('Con el Estado partido en feudos, la guerra mundial le dio aire al empresariado chino.',
  [S('×2','precio mundial de la plata, 1914–1919: maquinaria importada más barata',to=2,pre='×'),S('3','clanes rivales: Zhihli, Anhui y Fengtien',to=3),S('145 M','de yenes en los préstamos de Nishihara de 1918',to=None)]),
 flow('Una indignación nacional terminó en un frente unido y en una traición.',
  [('1919','Movimiento del 4 de Mayo','Protesta por entregar Shandong a Japón.'),('1921','Nace el PCCh','El marxismo se une al movimiento obrero.'),('1923–27','Primer Frente Unido','Expedición al Norte contra los caudillos.'),('12 abr 1927','Masacre de Shanghái','Chiang Kai-shek rompe la alianza.')]),
 versus('Un país unificado en el papel, partido en dos economías.',
  ['Costa urbana dinámica y monetizada','Industria y comercio en auge'],
  ['Campo abandonado y explotado','Extracción de los caudillos y arriendos de tierra'],labels=('Ciudad','Campo'),neutral=True),
 timeline('Dos herencias del caos: el poder nace del fusil y el mercado tiene vida propia.',
  [('1927','Mao: "el poder político nace del cañón de un fusil".'),('Hoy','El Ejército Popular de Liberación está subordinado al Partido.'),('Revisión de Rawski','El sector privado chino tuvo vitalidad aun sin Estado fuerte.')]),
]
T=[('señores de la guerra','Jefes militares regionales que controlaron cada uno su territorio tras la muerte de Yuan Shikai en 1916.'),
 ('Préstamos de Nishihara','145 millones de yenes que Japón prestó a Pekín en 1918 a cambio de financiamiento militar interno.'),
 ('Movimiento del 4 de Mayo','Protesta estudiantil y obrera de 1919 contra la entrega de las concesiones de Shandong a Japón.'),
 ('Expedición al Norte','Campaña militar de 1926–27 para eliminar a los señores de la guerra del norte.'),
 ('Kuomintang','Partido nacionalista fundado por Sun Yat-sen.'),
 ('dualismo económico','Convivencia de un sector urbano costero dinámico con un campo agrario atrasado.')]
