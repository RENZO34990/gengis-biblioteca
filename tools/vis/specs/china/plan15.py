from visgen import *
PATH='15-plan-quinquenal'
V=[
 flow('El crecimiento de antes ya no alcanzaba: había desequilibrios adentro y bloqueos afuera.',
  [('Adentro','Crisis inmobiliaria','Deuda opaca de los gobiernos locales y consumo rezagado.'),('Adentro','Empleo juvenil','Presión sobre el desempleo urbano.'),('Afuera','Contención tecnológica','Proteccionismo y límites a los semiconductores.')]),
 versus('Del volumen de producción a la resiliencia: así cambió el plan.',
  ['Meta de crecimiento rígida','Enfoque en el volumen bruto'],
  ['Meta flexible de 4.5%–5%','Resiliencia, soberanía tecnológica y control de riesgos'],labels=('Antes','Desde las Dos Sesiones, 12 mar 2026')),
 stats('Menos PIB, más laboratorio.',
  [S('4.5–5%','objetivo de crecimiento anual, por debajo del 5% anterior',to=None),S('>7%','de I+D anual como meta central',to=None),S('1.3 billones','de yuanes en bonos especiales del tesoro a ultra largo plazo',to=None)]),
 stats('El capital migra de los ladrillos a los laboratorios.',
  [S('30%','del consumo eléctrico, de energías limpias, en 2030',to=30,suf='%'),S('725 M t','de capacidad anual de producción de grano',to=None),S('14,600+','PYMEs "Pequeños Gigantes" especializadas',to=None)]),
 timeline('El quinquenio 2026–2030 es la plataforma para el objetivo de 2035.',
  [('2020','Punto de partida: duplicar la economía.'),('2026–2030','El 15º Plan, con la seguridad como eje ordenador.'),('2035','Meta de Xi: país moderadamente desarrollado.')]),
]
T=[('Dos Sesiones','Reuniones anuales de marzo de la Asamblea Popular Nacional y su órgano consultivo.'),
 ('LGFV','Plataformas de Financiamiento de los Gobiernos Locales: vehículos con deuda opaca.'),
 ('Nuevas Fuerzas Productivas de Calidad','Meta de ruptura científica para elevar la productividad, con I+D y política "AI Plus".'),
 ('SASAC','Organismo que supervisa a las empresas estatales (SOE).'),
 ('Franja y la Ruta','Iniciativa china de infraestructura y comercio hacia otros países.')]
