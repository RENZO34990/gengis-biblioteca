/* Capa visual de los cuadernos Nalanda: una animación por acto, solo al abrirlo.
   Requiere GSAP y ScrollTrigger cargados antes. Sin movimiento (prefers-reduced-motion)
   cada visual se queda en su estado final. */
(function(){
  var RM = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var narrow = window.matchMedia('(max-width:640px)');
  function q(el, s){ return el.querySelector(s); }
  function qa(el, s){ return Array.prototype.slice.call(el.querySelectorAll(s)); }

  function fmt(n, dec){
    var eu = document.documentElement.getAttribute('data-num') === 'eu';
    var s = Math.abs(n).toFixed(dec).split('.');
    s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, eu ? '.' : ',');
    return (n < 0 ? '-' : '') + s.join(eu ? ',' : '.');
  }

  var VIS = {
    rings: function(el){
      return gsap.timeline()
        .from(qa(el, '.v-ring'), {scale:.15, opacity:0, duration:.9, ease:'power2.out', stagger:.28, transformOrigin:'50% 50%'})
        .from(qa(el, '.v-legend li'), {opacity:0, x:-12, duration:.5, stagger:.25}, 0.3);
    },
    steps: function(el){
      var box = q(el, '.v-steps'), up = box.hasAttribute('data-up'), ship = q(el, '.v-ship');
      var stops = qa(el, '.v-stop'); if(up) stops.reverse();
      var tl = gsap.timeline(), dur = Math.max(2.2, stops.length * 1.0);
      tl.fromTo(q(el, '.v-fill'), {scaleY:0}, {scaleY:1, duration:dur, ease:'none'}, 0);
      if(ship) tl.fromTo(ship, {top: up ? '96%' : '4%'}, {top: up ? '4%' : '96%', duration:dur, ease:'none'}, 0);
      stops.forEach(function(s, i){ tl.from(s, {opacity:.15, x:10, duration:.5, ease:'power1.out'}, i * (dur / stops.length)); });
      return tl;
    },
    switches: function(el){
      var sws = qa(el, '.v-sw'), n = q(el, '.n');
      sws.forEach(function(s){ s.classList.remove('off'); }); n.textContent = String(sws.length);
      var tl = gsap.timeline({delay:.4});
      sws.forEach(function(s, i){
        tl.call(function(){ s.classList.add('off'); n.textContent = String(sws.length - 1 - i); }, null, i * 1.1);
      });
      return tl;
    },
    press: function(el){
      var core = q(el, '.v-press-core');
      return gsap.timeline()
        .from(q(el, '.v-press-l'), {x:-30, opacity:0, duration:.8, ease:'power2.out'})
        .from(q(el, '.v-press-r'), {x:30, opacity:0, duration:.8, ease:'power2.out'}, 0)
        .from(core, {scale:1.15, opacity:0, duration:.6}, 0)
        .to(core, {scale:.9, duration:1.2, ease:'power1.in'})
        .from(q(el, '.v-crack path'), {opacity:0, duration:.3}, '-=0.2')
        .to(core, {x:'+=3', duration:.06, yoyo:true, repeat:5})
        .to(core, {scale:1, duration:.5}, '+=0.1')
        .from(q(el, '.v-press-out'), {opacity:0, y:8, duration:.6});
    },
    timeline: function(el){
      var fill = q(el, '.v-tline-fill'), v = narrow.matches, tl = gsap.timeline();
      tl.fromTo(fill, v ? {scaleY:0} : {scaleX:0}, v ? {scaleY:1, duration:3, ease:'none'} : {scaleX:1, duration:3, ease:'none'}, 0);
      qa(el, '.v-tl').forEach(function(s, i){ tl.from(s, {opacity:.15, y:8, duration:.6, ease:'power1.out'}, i * (3 / Math.max(1, qa(el, '.v-tl').length))); });
      return tl;
    },
    flow: function(el){
      var tl = gsap.timeline();
      qa(el, '.v-node').forEach(function(n, i){ tl.from(n, {opacity:0, y:12, duration:.55, ease:'power2.out'}, i * .55); });
      qa(el, '.v-arr').forEach(function(a, i){ tl.from(a, {opacity:0, x:-8, duration:.4}, i * .55 + .35); });
      return tl;
    },
    stats: function(el){
      var tl = gsap.timeline();
      qa(el, '.v-stat').forEach(function(s, i){
        tl.from(s, {opacity:0, y:12, duration:.6, ease:'power2.out'}, i * .25);
        var n = q(s, '.v-num'), to = parseFloat(n.getAttribute('data-to'));
        if(isNaN(to)) return;
        var dec = parseInt(n.getAttribute('data-dec') || '0', 10), pre = n.getAttribute('data-pre') || '', suf = n.getAttribute('data-suf') || '', o = {v:0};
        n.textContent = pre + fmt(0, dec) + suf;
        tl.to(o, {v:to, duration:1.4, ease:'power2.out', onUpdate:function(){ n.textContent = pre + fmt(o.v, dec) + suf; }}, i * .25);
      });
      return tl;
    },
    bars: function(el){
      var tl = gsap.timeline();
      qa(el, '.v-bar').forEach(function(b, i){
        tl.from(q(b, '.v-bfill'), {scaleX:0, duration:1.1, ease:'power2.out'}, i * .35)
          .from(q(b, '.v-bv'), {opacity:0, duration:.5}, i * .35 + .6);
      });
      return tl;
    },
    versus: function(el){
      return gsap.timeline()
        .from(q(el, '.v-col.before'), {opacity:0, x:-14, duration:.7, ease:'power2.out'})
        .from(q(el, '.v-vs'), {opacity:0, scale:.5, duration:.4}, '-=0.1')
        .from(q(el, '.v-col.after'), {opacity:0, x:14, duration:.7, ease:'power2.out'}, '-=0.1');
    }
  };

  var played = {};
  window.playVis = function(acto){
    if(RM || !window.gsap) return;
    var el = acto.querySelector('.vis'); if(!el) return;
    var fn = VIS[el.getAttribute('data-vis')]; if(!fn) return;
    var k = acto.getAttribute('data-i');
    if(played[k]) played[k].kill();
    played[k] = fn(el);
  };

  /* glosario: mantiene el globo dentro de la pantalla */
  qa(document, '.gl').forEach(function(g){
    var d = g.querySelector('.gl-def'); if(!d) return;
    function fit(){
      d.style.setProperty('--sx', '0px');
      var r = d.getBoundingClientRect(), m = 12, sx = 0;
      if(r.left < m) sx = m - r.left;
      else if(r.right > window.innerWidth - m) sx = (window.innerWidth - m) - r.right;
      d.style.setProperty('--sx', sx + 'px');
    }
    g.addEventListener('mouseenter', fit); g.addEventListener('focus', fit);
  });

  /* el acto abierto al cargar anima cuando entra en pantalla */
  if(window.ScrollTrigger){
    var first = document.querySelector('.acto.active');
    if(first) ScrollTrigger.create({trigger:first, start:'top 75%', once:true, onEnter:function(){ window.playVis(first); }});
  }
})();
