from visgen import *
PATH='demografia-sostenibilidad-fiscal'
V=[
 bars('El modelo funcionó mientras había jóvenes y familias que cuidaban.',
  [('Fecundidad en 1960','6,33',100),('Fecundidad en 1983','< 2,1',33,True),('Fecundidad en 2023','0,72',11,True)],
  note='Hijos por mujer. Ancho proporcional a 6,33.'),
 stats('La natalidad y las cuentas públicas empezaron a empeorar a la vez.',
  [S('0,72','hijos por mujer en 2023, el mínimo mundial',to=0.72,dec=2),S('2020','la población tocó su pico: 51,8 millones',to=None),S('+35%','pérdida proyectada de fuerza laboral para 2050',to=35,pre='+',suf='%')]),
 flow('Cuatro frentes de reforma a la vez.',
  [('Regla fiscal','Déficit de 3% o menos','Tope propuesto por ley; el presupuesto 2026 apunta a cerca de 4,0%.'),
   ('Pensiones','De 9% a 13%','Cotización al alza y tasa de reemplazo de 43%.'),
   ('Natalidad','Emergencia demográfica','1 millón de wones al mes por lactante.'),
   ('Impuestos','Corporativo a 25%','Más Fondo de Crecimiento Nacional y reforma de la Ley Comercial.')]),
 stats('Por primera vez, el bienestar es la mayor partida del presupuesto.',
  [S('269,1 B','billones de wones en bienestar, salud y empleo (2026)',to=None),S('51,6%','deuda del gobierno central en 2026, desde 48,1%',to=51.6,dec=1,suf='%'),S('69,9%','empleo entre 55 y 64 años',to=69.9,dec=1,suf='%')]),
 versus('Dos lecturas de por qué cae la natalidad.',
  ['El éxito meritocrático priorizó la inversión personal','La "fiebre educativa" desplazó a la familia'],
  ['Los incentivos económicos no bastan','Hacen falta apertura migratoria, igualdad salarial y jornadas flexibles'],labels=('Anderson y Kohler','Economistas de la OCDE'),neutral=True),
]
T=[('fecundidad','Número promedio de hijos por mujer.'),
 ('dividendo demográfico','Ventaja económica de tener muchos trabajadores jóvenes y pocos dependientes.'),
 ('balance fiscal gestionado','Medida de déficit del gobierno que excluye algunos fondos de seguridad social.'),
 ('Fondo Nacional de Pensiones','Fondo de reservas de la pensión pública.'),
 ('descuento coreano','Menor valoración de las empresas coreanas por problemas de gobernanza.'),
 ('fiebre educativa','Presión social extrema por la inversión en educación.')]
