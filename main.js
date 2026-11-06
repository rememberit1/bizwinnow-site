(function () {
  'use strict';

  // Year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Sticky nav shadow
  var nav = document.querySelector('.nav');
  function onScroll() { if (nav) nav.classList.toggle('scrolled', window.scrollY > 10); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Contact form -> mailto
  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (el) {
        var bad = !el.value.trim();
        el.classList.toggle('invalid', bad);
        if (bad) ok = false;
      });
      var note = document.getElementById('formNote');
      if (!ok) { if (note) note.textContent = 'Please add your name and business name.'; return; }
      var d = new FormData(form);
      var to = form.getAttribute('data-email') || '[EMAIL]';
      var subject = 'Website request: ' + d.get('business');
      var body = [
        'Name: ' + d.get('name'),
        'Business: ' + d.get('business'),
        'Phone: ' + (d.get('phone') || '-'),
        'Business type: ' + d.get('type'),
        '',
        (d.get('message') || '')
      ].join('\n');
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      if (note) note.textContent = 'Opening your email app...';
    });
  }

  // Animations
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!window.gsap || reduce) return;
  gsap.registerPlugin(ScrollTrigger);
  document.documentElement.classList.add('js-anim');

  // Hero intro
  var heroItems = document.querySelectorAll('.hero .reveal');
  gsap.to(heroItems, { opacity: 1, y: 0, duration: 0.9, ease: 'power3.out', stagger: 0.09, delay: 0.1 });

  // Scroll reveals, batched for grids
  ScrollTrigger.batch('main section:not(.hero) .reveal', {
    start: 'top 88%',
    onEnter: function (batch) {
      gsap.to(batch, { opacity: 1, y: 0, duration: 0.8, ease: 'power3.out', stagger: 0.08, overwrite: true });
    }
  });

  // Price counter pop
  var bigPrices = document.querySelectorAll('.price-big');
  ScrollTrigger.create({
    trigger: '.price-card', start: 'top 80%', once: true,
    onEnter: function () {
      gsap.from(bigPrices, { scale: 0.6, opacity: 0, duration: 0.8, ease: 'back.out(2)', stagger: 0.15, delay: 0.25 });
    }
  });

  // Subtle parallax on hero visual
  gsap.to('.hero-visual', {
    yPercent: -8, ease: 'none',
    scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
  });

  // Safety: reveal anything still hidden after load (e.g. jump links)
  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
