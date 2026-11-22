/* Identidad por pais para Nalanda: ambiente propio (petalos / linternas / ondas),
   titulos con gesto propio y respuesta al abrir cada acto. Respeta movimiento reducido. */
(function(){
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var dpr = Math.min(window.devicePixelRatio || 1, 2);

  function ambient(kind, host, fixed){
    if(reduce || !host) return null;
    var cv = document.createElement('canvas');
    cv.className = 'id-amb'; cv.setAttribute('aria-hidden', 'true');
    cv.style.cssText = 'position:' + (fixed ? 'fixed' : 'absolute') + ';left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:' + (fixed ? 6 : -1);
    host.appendChild(cv);
    var ctx = cv.getContext('2d'), W = 0, H = 0, P = [], R = [], S = [], lastX = -99, lastY = -99, on = !!fixed, raf = 0, nextR = 0;
    function mk(init){
      if(kind === 'jp') return { x: Math.random()*W, y: init ? Math.random()*H : -12, s: 4 + Math.random()*5, vy: .28 + Math.random()*.4, vx: .12 + Math.random()*.32, r: Math.random()*6.28, vr: (Math.random()-.5)*.04, ph: Math.random()*6.28, a: .35 + Math.random()*.4 };
      return { x: Math.random()*W, y: init ? Math.random()*H : H + 40, s: 9 + Math.random()*8, vy: -(.2 + Math.random()*.28), ph: Math.random()*6.28, a: .6 + Math.random()*.3 };
    }
    function size(){
      W = cv.clientWidth; H = cv.clientHeight; if(!W || !H) return;
      cv.width = W*dpr; cv.height = H*dpr; ctx.setTransform(dpr,0,0,dpr,0,0);
      var n = kind === 'jp' ? (fixed ? 9 : 8) : kind === 'cn' ? (fixed ? 7 : 6) : 0;
      if(W < 700) n = Math.ceil(n*.6);
      while(P.length < n) P.push(mk(true)); P.length = Math.min(P.length, n);
    }
    function ripple(x, y, max){ if(R.length < 9) R.push({ x: x, y: y, r: 2, max: max, a: .55 }); }
    function tick(t){
      raf = 0; if(!on) return;
      if(!W || !H){ size(); }
      ctx.clearRect(0, 0, W, H);
      var i, p;
      if(kind === 'jp'){
        for(i = 0; i < P.length; i++){
          p = P[i]; p.ph += .02; p.y += p.vy; p.x += p.vx + Math.sin(p.ph)*.35; p.r += p.vr;
          if(p.y > H + 14 || p.x > W + 14){ P[i] = mk(false); P[i].x = Math.random()*W*.8; continue; }
          ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.r);
          ctx.fillStyle = 'rgba(232,166,182,' + p.a + ')';
          ctx.beginPath(); ctx.ellipse(0, 0, p.s, p.s*.56, 0, 0, 6.283); ctx.fill();
          ctx.fillStyle = 'rgba(250,214,222,' + (p.a*.8) + ')';
          ctx.beginPath(); ctx.ellipse(-p.s*.2, -p.s*.08, p.s*.5, p.s*.22, 0, 0, 6.283); ctx.fill();
          ctx.restore();
        }
      } else if(kind === 'cn'){
        for(i = 0; i < P.length; i++){
          p = P[i]; p.ph += .012; p.y += p.vy; p.x += Math.sin(p.ph)*.28;
          if(p.y < -p.s*3){ P[i] = mk(false); continue; }
          var fl = .85 + .15*Math.sin(p.ph*5), edge = Math.min(1, Math.max(0, (p.y + 30) / 90)) * Math.min(1, Math.max(0, (H - p.y + 30) / 90)), al = p.a * fl * (edge || 0), sz = p.s;
          ctx.save(); ctx.translate(p.x, p.y);
          var halo = ctx.createRadialGradient(0, 0, 0, 0, 0, sz*3);
          halo.addColorStop(0, 'rgba(255,184,70,' + (al*.5) + ')'); halo.addColorStop(1, 'rgba(255,150,40,0)');
          ctx.fillStyle = halo; ctx.beginPath(); ctx.arc(0, 0, sz*3, 0, 6.283); ctx.fill();
          ctx.strokeStyle = 'rgba(201,166,62,' + (al*.8) + ')'; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(0, -sz*.8); ctx.lineTo(0, -sz*1.5); ctx.moveTo(0, sz*.8); ctx.lineTo(0, sz*1.45); ctx.stroke();
          var body = ctx.createRadialGradient(0, -sz*.1, 0, 0, 0, sz);
          body.addColorStop(0, 'rgba(255,150,70,' + al + ')'); body.addColorStop(1, 'rgba(196,48,36,' + al + ')');
          ctx.fillStyle = body; ctx.beginPath(); ctx.ellipse(0, 0, sz*.66, sz*.82, 0, 0, 6.283); ctx.fill();
          ctx.strokeStyle = 'rgba(233,196,92,' + (al*.7) + ')'; ctx.lineWidth = .8;
          ctx.beginPath(); ctx.ellipse(0, 0, sz*.3, sz*.82, 0, 0, 6.283); ctx.stroke();
          ctx.fillStyle = 'rgba(214,176,70,' + al + ')';
          ctx.fillRect(-sz*.3, -sz*.9, sz*.6, sz*.16); ctx.fillRect(-sz*.3, sz*.74, sz*.6, sz*.16);
          ctx.restore();
        }
        for(i = 0; i < S.length; i++){
          var sp = S[i]; sp.x += sp.vx; sp.y += sp.vy; sp.vy -= .012; sp.vx *= .985; sp.l--;
          if(sp.l <= 0){ S.splice(i, 1); i--; continue; }
          var la = sp.l / sp.m;
          ctx.fillStyle = 'rgba(' + (sp.h ? '255,226,140' : '240,176,70') + ',' + (la*.9) + ')';
          ctx.beginPath(); ctx.arc(sp.x, sp.y, sp.s*(.4 + .6*la), 0, 6.283); ctx.fill();
        }
      } else {
        if(t > nextR){ ripple(Math.random()*W, Math.random()*H, 60 + Math.random()*70); nextR = t + 1300 + Math.random()*1700; }
        for(i = 0; i < R.length; i++){
          var q = R[i]; q.r += .6; var al2 = q.a * (1 - q.r/q.max);
          if(al2 <= 0){ R.splice(i, 1); i--; continue; }
          ctx.strokeStyle = 'rgba(122,158,142,' + al2 + ')'; ctx.lineWidth = 1.3;
          ctx.beginPath(); ctx.arc(q.x, q.y, q.r, 0, 6.283); ctx.stroke();
          ctx.strokeStyle = 'rgba(122,158,142,' + (al2*.6) + ')';
          ctx.beginPath(); ctx.arc(q.x, q.y, q.r*.62, 0, 6.283); ctx.stroke();
        }
      }
      raf = requestAnimationFrame(tick);
    }
    function kick(){ if(on && !raf) raf = requestAnimationFrame(tick); }
    size();
    if(fixed){
      document.addEventListener('visibilitychange', function(){ on = !document.hidden; kick(); });
    } else if('IntersectionObserver' in window){
      new IntersectionObserver(function(e){ on = e[0].isIntersecting; kick(); }).observe(host);
    } else { on = true; }
    if('ResizeObserver' in window) new ResizeObserver(size).observe(fixed ? document.documentElement : host); else window.addEventListener('resize', size);
    if(kind === 'cn' && !(window.matchMedia && window.matchMedia('(pointer:coarse)').matches)){
      document.addEventListener('pointermove', function(e){
        if(!on) return;
        var r = cv.getBoundingClientRect();
        if(e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) return;
        var x = e.clientX - r.left, y = e.clientY - r.top;
        if(Math.abs(x - lastX) + Math.abs(y - lastY) < 9) return;
        lastX = x; lastY = y;
        for(var k = 0; k < 2 && S.length < 70; k++){ var m = 34 + Math.random()*34; S.push({ x: x + (Math.random()-.5)*6, y: y + (Math.random()-.5)*6, vx: (Math.random()-.5)*1.1, vy: -.3 - Math.random()*.9, s: 1.2 + Math.random()*2, l: m, m: m, h: Math.random() < .35 }); }
        kick();
      }, { passive: true });
    }
    if(kind === 'kr'){
      document.addEventListener('pointerdown', function(e){
        if(!on) return;
        var r = cv.getBoundingClientRect();
        if(e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) return;
        ripple(e.clientX - r.left, e.clientY - r.top, 130); kick();
      }, { passive: true });
    }
    kick();
    return cv;
  }
  window.NalandaId = { ambient: ambient };

  var pais = document.documentElement.getAttribute('data-pais');
  if(!pais) return;

  function esc(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function split(el){
    if(!el || !el.textContent.trim()) return false;
    var nodes = [].slice.call(el.childNodes);
    for(var q = 0; q < nodes.length; q++){ if(nodes[q].nodeType !== 3 && nodes[q].nodeName !== 'BR') return false; }
    var full = el.textContent.trim().replace(/\s+/g, ' '), n = 0;
    var html = nodes.map(function(nd){
      if(nd.nodeName === 'BR') return '<br>';
      var t = nd.textContent.replace(/\s+/g, ' ').trim(); if(!t) return '';
      return t.split(' ').map(function(w){
        var chars = Array.from(w);
        return '<span class="id-wd' + (chars.length > 9 ? ' id-long' : '') + '">' + chars.map(function(c){ return '<span class="id-l" style="--i:' + (n++) + '">' + esc(c) + '</span>'; }).join('') + '</span>';
      }).join(' ');
    }).join('');
    el.innerHTML = '<span class="id-sr">' + esc(full) + '</span><span aria-hidden="true">' + html + '</span>';
    el.classList.add('id-on');
    return true;
  }
  function init(){
    var root = document.documentElement;
    split(document.querySelector('header.hero h1'));
    var heads = [].slice.call(document.querySelectorAll('.section-head'));
    heads.forEach(function(h){ split(h.querySelector('h2')); });
    if('IntersectionObserver' in window){
      var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('id-in'); io.unobserve(e.target); } }); }, { rootMargin: '0px 0px -12% 0px', threshold: .2 });
      heads.forEach(function(h){ io.observe(h); });
    } else { heads.forEach(function(h){ h.classList.add('id-in'); }); }
    setTimeout(function(){ root.classList.add('id-go'); }, 160);
    ambient(pais, document.body, true);
  }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
