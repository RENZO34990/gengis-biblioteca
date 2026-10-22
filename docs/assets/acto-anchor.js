/* Al pulsar un acto mientras otro (arriba) está abierto, el acto pulsado se queda donde está durante
   la contracción del anterior y después se acomoda a una altura cómoda de lectura. */
(function(){
  function setScroll(y, smooth){
    var L = window.__lenis;
    if(L && L.scrollTo){ L.scrollTo(y, smooth ? {duration:.7} : {immediate:true, force:true}); }
    else window.scrollTo({top:y, behavior: smooth ? 'smooth' : 'auto'});
  }
  function cur(){ return window.__lenis ? window.__lenis.scroll : window.scrollY; }
  document.addEventListener('click', function(e){
    var head = e.target.closest && e.target.closest('.acto-head');
    if(!head) return;
    var acto = head.closest('.acto');
    if(!acto || acto.classList.contains('active')) return;
    if(!document.querySelector('.acto.active')) return;
    var y0 = head.getBoundingClientRect().top, t0 = performance.now();
    (function loop(){
      var d = head.getBoundingClientRect().top - y0;
      if(Math.abs(d) > 0.5) setScroll(cur() + d, false);
      if(performance.now() - t0 < 900) requestAnimationFrame(loop);
      else {
        var top = head.getBoundingClientRect().top, vh = window.innerHeight;
        if(top > vh * .45 || top < 70) setScroll(cur() + top - vh * .2, true);
      }
    })();
  }, true);
})();
