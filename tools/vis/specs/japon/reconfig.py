from visgen import *
PATH='reconfiguracion-estrategica'
V=[
 press('Un Estado pasivo en un Indo-Pacífico cada vez más inestable.',
  ('Fukushima y la parálisis','Terremoto, tsunami y desastre nuclear de 2011'),'日本',
  ('Modelo agotado','METI con fracasos de planificación; Art. 9 restrictivo'),
  'El gobierno del PDJ (2009-2012) colapsó y volvió a apoyarse en la <b>burocracia tradicional</b>.',core_small='2011–12'),
 flow('Una restricción comercial convirtió la tecnología en seguridad nacional.',
  [('Jul 2019','Tres químicos','METI restringe su exportación a Corea del Sur sin consulta.'),('Disputa','OMC','Conflicto comercial bilateral.'),('2023–24','Escándalo LDP','Las facciones tradicionales se disuelven casi por completo.')]),
 steps('De la defensa colectiva a la primera ministra Takaichi.',
  [('2014–15','Leyes de seguridad','Permiten la defensa colectiva bajo Abe.'),('2021–25','Seguridad económica','Nuevo ministerio y Buró de Comercio y Seguridad Económica en METI.'),('21 oct 2025','Takaichi','Primera mujer primera ministra.'),('Feb 2026','Supermayoría','316 escaños tras disolver la Dieta.')]),
 stats('Dinero y poder concentrados en 17 sectores.',
  [S('17','industrias prioritarias del Cuartel General de Estrategia de Crecimiento',to=17),S('20%','deducción tributaria máxima, aprobada por METI en 2023',to=20,suf='%'),S('$3,500 M+','en subsidios para JASM en Kumamoto',to=None)]),
 versus('Con 316 escaños, enmendar el Artículo 9 está a un voto.',
  ['Gobierno de Takaichi: 316 escaños','Posible enmienda del Artículo 9'],
  ['CRA (CDP + Komeito): 173 escaños','Dique laico y pacifista'],labels=('Gobierno','Oposición'),neutral=True),
]
T=[('METI','Ministerio de Economía, Comercio e Industria.'),
 ('Triángulo de Hierro','Alianza entre políticos, burocracia y grandes empresas.'),
 ('Rapidus','Empresa estatal-privada que avanza hacia chips de 2 nanómetros con IBM.'),
 ('JASM','Megafábrica de TSMC, Sony y Denso en Kumamoto.'),
 ('Kantei','Oficina del Primer Ministro, donde se concentra hoy el control.'),
 ('Keidanren','Federación empresarial japonesa.')]
