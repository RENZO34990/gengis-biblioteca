/* Triveni · Transiciones entre páginas (humo y puerta)
   Un solo archivo, copiado en Triveni, Nalanda, Forja y Alma. Va en el <head>, sin defer,
   para que la página de llegada nazca ya cubierta y no parpadee.

   Reglas (se pueden forzar con data-tv="humo" | "puerta" | "none" en el enlace):
     - Entrar a algo más profundo (de Triveni a un volumen, del portal a un cuaderno): HUMO.
     - Volver o ir de lado (volumen a Triveni, cuaderno al portal, entre volúmenes): PUERTA.
     - Entre cuadernos consecutivos no se toca: ya usan View Transitions.

   HUMO     Se abre desde donde hiciste clic. Brota rápido y frena al llegar a los bordes, como el
            humo de verdad. El borde es blando y deshilachado, se mueve mientras crece y no se asienta
            nunca en una forma perfecta. La página nueva sube desde abajo mientras el humo se abre.
   PUERTA   Un cuadrado oscuro entra girando sobre la esquina inferior izquierda, cubre la página, se
            queda un instante y sale girando sobre la esquina inferior derecha. Gira alrededor de las
            esquinas de la pantalla, no de su centro, así que se mueve como una puerta que barre. Es lo
            bastante grande para que su borde despeje toda la pantalla (en un móvil alto llega más lejos).
            La página de abajo se oscurece al entrar y se aclara al salir.

   Ajustes: el objeto CFG de abajo. Color del humo y de la puerta: data-ink en la etiqueta <script>.
   Con movimiento reducido no se intercepta nada: se navega normal.
   API: window.TvT.go(modo, url, x, y), window.TvT.onTitles(fn) para que los titulares suban cuando toca. */
(function(){
  'use strict';
  var doc = document.documentElement, me = document.currentScript;
  var INK = (me && me.getAttribute('data-ink')) || '#10090D';
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  var CFG = {
    smokeOut: 1150,        /* ms que tarda el humo en cubrir al salir */
    smokeIn: 1800,        /* ms que tarda el humo en abrirse al llegar */
    smokeTitles: .5,      /* fracción de la apertura a la que empiezan a subir los titulares */
    doorIn: 700,          /* ms que tarda la puerta en entrar */
    doorHold: 280,        /* ms que se queda cubriendo */
    doorOut: 800,         /* ms que tarda en salir */
    doorTitles: .42,      /* fracción de la salida a la que empiezan a subir los titulares */
    dim: .55,             /* cuánto se oscurece la página de abajo con la puerta */
    scale: .6,            /* resolución del humo respecto a la pantalla */
        puffRatio: 1.6       /* radio final respecto a la esquina más lejana */
  };
  var KEY = 'tv_t', MAXAGE = 9000;
  var T = window.TvT = { holding: false, go: go, onTitles: onTitles, cfg: CFG };
  var waiting = [];
  function onTitles(fn){ if(T.holding) waiting.push(fn); else fn(); }
  function releaseTitles(){ if(!T.holding) return; T.holding = false; doc.classList.add('tv-go'); doc.classList.remove('tv-hold'); var q = waiting.splice(0); q.forEach(function(f){ try{ f(); }catch(e){} }); }

  function clamp(x,a,b){ return x<a?a:x>b?b:x; }
  function hex2rgb(h){ h = h.replace('#',''); if(h.length === 3) h = h.replace(/(.)/g,'$1$1'); var n = parseInt(h,16); return [n>>16&255, n>>8&255, n&255]; }
  function rgbs(c,a){ return 'rgba(' + (c[0]|0) + ',' + (c[1]|0) + ',' + (c[2]|0) + ',' + a + ')'; }

  /* ---------- estilos ---------- */
  var css = document.createElement('style');
  css.textContent =
    '.tv-ov{position:fixed;inset:0;z-index:2147483000;pointer-events:none}' +
    '.tv-ov canvas{position:absolute;inset:0;width:100%;height:100%;display:block}' +
    '.tv-dim{background:#000;opacity:0}' +
    '.tv-door{position:fixed;bottom:0;z-index:2147483001;pointer-events:none;will-change:transform;' +
      'background:linear-gradient(135deg,var(--tv-ink) 0%,var(--tv-ink) 46%,var(--tv-ink2) 100%);' +
      'box-shadow:0 0 120px rgba(0,0,0,.65)}' +
    '.tv-door.l{left:0;transform-origin:0 100%}.tv-door.r{right:0;transform-origin:100% 100%}' +
    '.tv-door.l::after,.tv-door.r::after{content:"";position:absolute;top:0;bottom:0;width:1px;background:linear-gradient(transparent,rgba(255,255,255,.28),transparent)}' +
    '.tv-door.l::after{right:0}.tv-door.r::after{left:0}' +
    '.tv-mark{position:absolute;display:flex;flex-direction:column;align-items:center;gap:18px;transform:translate(-50%,50%);color:rgba(244,231,229,.86)}' +
    '.tv-mark svg{width:112px;height:auto;overflow:visible}' +
    '.tv-mark span{font:500 11px/1 Georgia,"Cormorant Garamond",serif;letter-spacing:.5em;padding-left:.5em;text-transform:uppercase;opacity:.8}' +
    'html.tv-arr main{transform-origin:50% 100%;animation:tvRise ' + CFG.smokeIn + 'ms cubic-bezier(.16,1,.3,1) both}' +
    '@keyframes tvRise{from{transform:translateY(7vh) scale(.955)}to{transform:none}}' +
    'html.tv-hold *:not(main),html.tv-hold *::before,html.tv-hold *::after{animation-play-state:paused!important}';
  (document.head || doc).appendChild(css);

  /* ---------- humo: nubes blandas superpuestas ----------
     Muchas manchas con degradado radial cuyos centros derivan con el tiempo. La suma da un borde
     blando, abultado y deshilachado que no se asienta nunca en una forma perfecta. */
  var BL = [];
  (function(){
    var s = 5, r = function(){ s = (s*16807) % 2147483647; return s/2147483647; }, i;
    BL.push({ a:0, d:0, z:.8, o:1, sp:0, w:0 });
    for(i=0;i<64;i++) BL.push({ a:(i + r()*.9)/64*6.2832, d:.5 + r()*.42, z:.15 + r()*.15, o:1, sp:r()-.5, w:r()*6.28 });
    for(i=0;i<56;i++) BL.push({ a:r()*6.2832, d:.86 + r()*.26, z:.035 + r()*.06, o:.55, sp:r()-.5, w:r()*6.28 });
  })();
  function puff(ctx, cx, cy, R, tau, color, erase){
    var i, c = erase ? [0,0,0] : color, wc = erase ? [0,0,0] : color.map(function(v){ return Math.min(255, v + 20); });
    for(i=0;i<BL.length;i++){
      var b = BL[i], ang = b.a + .16*Math.sin(tau*.8 + b.w) + b.sp*tau*.08;
      var d = R*b.d*(1 + .09*Math.sin(tau*.9*(1 + b.sp) + b.w*2)), z = R*b.z*(1 + .12*Math.sin(tau*1.3 + b.w));
      var x = cx + Math.cos(ang)*d, y = cy + Math.sin(ang)*d, k = b.o > .9 ? c : wc;
      var g = ctx.createRadialGradient(x,y,0,x,y,z);
      g.addColorStop(0, rgbs(k,b.o)); g.addColorStop(b.o > .9 ? .55 : .3, rgbs(k,b.o*(b.o > .9 ? .9 : .6))); g.addColorStop(1, rgbs(k,0));
      ctx.fillStyle = g; ctx.fillRect(x - z, y - z, z*2, z*2);
    }
  }
  function ease(t){ return 1 - Math.pow(1 - t, 3); }       /* brota rápido y frena hacia los bordes */

  function makeCanvas(){
    var ov = document.createElement('div'); ov.className = 'tv-ov'; ov.setAttribute('aria-hidden','true');
    var cv = document.createElement('canvas'), W = window.innerWidth, H = window.innerHeight;
    cv.width = Math.max(8, Math.ceil(W*CFG.scale)); cv.height = Math.max(8, Math.ceil(H*CFG.scale));
    ov.appendChild(cv); doc.appendChild(ov);
    return { ov: ov, cv: cv, ctx: cv.getContext('2d'), W: W, H: H };
  }
  function farthest(x, y, W, H){ return Math.max(Math.hypot(x,y), Math.hypot(W-x,y), Math.hypot(x,H-y), Math.hypot(W-x,H-y)); }

  function smokeOut(x, y, color, done){
    var o = makeCanvas(), ctx = o.ctx, k = CFG.scale, Rm = farthest(x,y,o.W,o.H)*CFG.puffRatio*k, t0 = 0;
    (function step(now){
      if(!t0) t0 = now;
      var t = clamp((now - t0)/CFG.smokeOut, 0, 1);
      ctx.clearRect(0,0,o.cv.width,o.cv.height);
      puff(ctx, x*k, y*k, Rm*ease(t) + 2, now/900, color, false);
      if(t < 1) requestAnimationFrame(step);
      else { ctx.fillStyle = rgbs(color,1); ctx.fillRect(0,0,o.cv.width,o.cv.height); done(); }
    })(performance.now());
    return o;
  }

  function smokeIn(x, y, color){
    var o = makeCanvas(), ctx = o.ctx, k = CFG.scale, Rm = farthest(x,y,o.W,o.H)*CFG.puffRatio*k, t0 = 0, fired = false;
    doc.classList.add('tv-arr');
    function paint(t, now){
      ctx.globalCompositeOperation = 'source-over';
      ctx.clearRect(0,0,o.cv.width,o.cv.height);
      ctx.fillStyle = rgbs(color,1); ctx.fillRect(0,0,o.cv.width,o.cv.height);
      ctx.globalCompositeOperation = 'destination-out';
      puff(ctx, x*k, y*k, Rm*ease(t) + 1, now/900, color, true);
    }
    paint(0, 0);
    requestAnimationFrame(function step(now){
      if(!t0) t0 = now;
      var t = clamp((now - t0)/CFG.smokeIn, 0, 1);
      paint(t, now);
      if(t >= CFG.smokeTitles && !fired){ fired = true; releaseTitles(); }
      if(t < 1) requestAnimationFrame(step);
      else { o.ov.remove(); doc.classList.remove('tv-arr'); doc.classList.remove('tv-hold'); releaseTitles(); }
    });
  }

  /* ---------- puerta ---------- */
  var MARK = '<svg viewBox="0 0 120 70" fill="none" stroke-linecap="round" stroke-width="1.6" aria-hidden="true">' +
    '<path d="M4 4C22 34 46 58 60 64" stroke="#E4B65F"/><path d="M60 8V64" stroke="#E8803F"/><path d="M116 4C98 34 74 58 60 64" stroke="#5DB5A4"/>' +
    '<circle cx="60" cy="64" r="3.2" fill="#F6E2B0" stroke="none"/></svg><span>Triveni</span>';
  function lighten(c,n){ return c.map(function(v){ return Math.min(255, v+n); }); }

  function makeDoor(side, color){
    var W = window.innerWidth, H = window.innerHeight, L = Math.ceil(Math.hypot(W,H)*1.06);
    var d = document.createElement('div'); d.className = 'tv-door ' + side; d.setAttribute('aria-hidden','true');
    d.style.cssText = 'width:' + L + 'px;height:' + L + 'px;--tv-ink:' + rgbs(color,1) + ';--tv-ink2:' + rgbs(lighten(color,22),1);
    var m = document.createElement('div'); m.className = 'tv-mark'; m.innerHTML = MARK;
    /* la marca queda en el centro de la pantalla cuando la puerta cubre */
    if(side === 'l') m.style.cssText = 'left:' + (W/2) + 'px;bottom:' + (H/2) + 'px';
    else m.style.cssText = 'right:' + (W/2) + 'px;bottom:' + (H/2) + 'px;transform:translate(50%,50%)';
    d.appendChild(m); doc.appendChild(d); return d;
  }
  function makeDim(){ var d = document.createElement('div'); d.className = 'tv-ov tv-dim'; d.setAttribute('aria-hidden','true'); doc.appendChild(d); return d; }

  function doorOut(color, done){
    var door = makeDoor('l', color), dim = makeDim(), EASE = 'cubic-bezier(.76,0,.2,1)';
    door.animate([{ transform:'rotate(-90deg)' }, { transform:'rotate(0deg)' }], { duration: CFG.doorIn, easing: EASE, fill:'forwards' });
    var a = dim.animate([{ opacity:0 }, { opacity:CFG.dim }], { duration: CFG.doorIn, easing:'ease-out', fill:'forwards' });
    a.onfinish = done;
    return { door: door, dim: dim };
  }
  function doorIn(color){
    var door = makeDoor('r', color), dim = makeDim(), EASE = 'cubic-bezier(.76,0,.2,1)', fired = false;
    dim.style.opacity = CFG.dim; doc.classList.add('tv-arr');
    door.animate([{ transform:'rotate(0deg)' }, { transform:'rotate(0deg)', offset:CFG.doorHold/(CFG.doorHold+CFG.doorOut) }, { transform:'rotate(90deg)' }],
      { duration: CFG.doorHold + CFG.doorOut, easing: EASE, fill:'forwards' });
    dim.animate([{ opacity:CFG.dim }, { opacity:CFG.dim, offset:CFG.doorHold/(CFG.doorHold+CFG.doorOut) }, { opacity:0 }],
      { duration: CFG.doorHold + CFG.doorOut, easing:'ease-in', fill:'forwards' });
    setTimeout(releaseTitles, CFG.doorHold + CFG.doorOut*CFG.doorTitles);
    setTimeout(function(){ door.remove(); dim.remove(); doc.classList.remove('tv-arr'); doc.classList.remove('tv-hold'); releaseTitles(); }, CFG.doorHold + CFG.doorOut + 60);
  }

  /* ---------- salida ---------- */
  var leaving = false;
  function go(mode, href, x, y){
    if(leaving || reduce) { location.href = href; return; }
    leaving = true;
    var color = hex2rgb(INK);
    var save = { m: mode, x: x/window.innerWidth, y: y/window.innerHeight, c: INK, t: Date.now() };
    try{ sessionStorage.setItem(KEY, JSON.stringify(save)); }catch(e){}
    var nav = function(){ location.href = href; };
    if(mode === 'puerta') doorOut(color, nav); else smokeOut(x, y, color, nav);
    setTimeout(nav, 4000);
  }

  function base(p){ var s = p.split('/').filter(Boolean); if(s.length && /\.html?$/.test(s[s.length-1])) s.pop(); return s; }
  function pick(a, b){
    var A = base(a.pathname), B = base(b.pathname), triveni = 'pr-landing';
    if(A[0] !== B[0]){ return B[0] === triveni ? 'puerta' : A[0] === triveni ? 'humo' : 'puerta'; }
    return B.length > A.length ? 'humo' : 'puerta';
  }

  document.addEventListener('click', function(e){
    if(reduce || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null; if(!a) return;
    if((a.target && a.target !== '_self') || a.hasAttribute('download')) return;
    var mode = a.getAttribute('data-tv'); if(mode === 'none') return;
    var u; try{ u = new URL(a.href, location.href); }catch(err){ return; }
    if(u.origin !== location.origin || !/^https?:$/.test(u.protocol)) return;
    if(u.pathname === location.pathname && u.search === location.search) return;
    if(a.closest('.nav-adjacent')) return;
    if(mode !== 'humo' && mode !== 'puerta') mode = pick(location, u);
    e.preventDefault();
    var x = e.clientX, y = e.clientY;
    if(!e.detail || (!x && !y)){ var r = a.getBoundingClientRect(); x = r.left + r.width/2; y = r.top + r.height/2; }
    go(mode, u.href, x, y);
  }, true);

  window.addEventListener('pageshow', function(e){
    if(e.persisted){ leaving = false; Array.prototype.forEach.call(document.querySelectorAll('.tv-ov,.tv-door'), function(n){ n.remove(); }); }
  });

  /* ---------- llegada ---------- */
  (function arrive(){
    if(reduce) return;
    var s = null;
    try{ s = JSON.parse(sessionStorage.getItem(KEY) || 'null'); sessionStorage.removeItem(KEY); }catch(e){}
    if(!s || Date.now() - s.t > MAXAGE) return;
    try{ if(document.referrer && new URL(document.referrer).origin !== location.origin) return; }catch(e){}
    var color = hex2rgb(s.c || INK);
    T.holding = true; doc.classList.add('tv-hold');
    setTimeout(releaseTitles, 6000);
    if(s.m === 'puerta') doorIn(color);
    else smokeIn(s.x*window.innerWidth, s.y*window.innerHeight, color);
  })();
})();
