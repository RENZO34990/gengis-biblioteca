/* Mantiene en su sitio el acto que se acaba de pulsar cuando el acto abierto (que está arriba) se contrae,
   para no perder el hilo de lectura. Funciona en cualquier cuaderno con .acto > .acto-head. */
(function(){
  document.addEventListener('click', function(e){
    var head = e.target.closest && e.target.closest('.acto-head');
    if(!head) return;
    var acto = head.closest('.acto');
    if(!acto || acto.classList.contains('active')) return;
    if(!document.querySelector('.acto.active')) return;
    var y0 = head.getBoundingClientRect().top, t0 = performance.now();
    (function loop(){
      var d = head.getBoundingClientRect().top - y0;
      if(Math.abs(d) > 0.5) window.scrollBy(0, d);
      if(performance.now() - t0 < 1100) requestAnimationFrame(loop);
    })();
  }, true);
})();
