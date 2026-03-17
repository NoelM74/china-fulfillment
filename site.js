/* ═══════════════════════════════════════
   CHINA-FULFILLMENT.COM — SCROLL REVEAL
   Lightweight IntersectionObserver-based
   scroll animation. Zero impact on initial
   page load — runs after DOM ready.
   ═══════════════════════════════════════ */
(function () {
  'use strict';

  /* Bail out for users who prefer reduced motion */
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion:reduce)').matches) return;

  /* IntersectionObserver — marks elements visible as they scroll into view */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('vis');
        io.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -32px 0px'
  });

  /*
   * Selectors that get the scroll-reveal treatment.
   * These match class names used across all pages.
   * Elements already visible on page load get instant
   * .vis because they intersect immediately.
   */
  var SEL = [
    /* Service / feature cards */
    '.sc', '.hc', '.ch', '.feat-card', '.sol-card', '.serv-card',
    '.pkg-card', '.kit-card', '.proc-step', '.why-card', '.step-card',
    /* Blog / post cards */
    '.post',
    /* Testimonials */
    '.test',
    /* Credentials / awards */
    '.cred', '.award-card',
    /* Stats */
    '.num', '.stat-card', '.proof-item',
    /* Timeline items */
    '.tl-item',
    /* Team */
    '.team-card',
    /* FAQ */
    '.faq-q',
    /* Misc content blocks */
    '.detail-card', '.qs-card', '.story-card',
    '.sce-item', '.flow-step', '.rp', '.cost-card',
    '.review-card', '.check-item'
  ].join(',');

  /* Track parent → sibling index for stagger delays */
  var parentMap = new Map();

  document.querySelectorAll(SEL).forEach(function (el) {
    var parent = el.parentNode;
    var idx = parentMap.has(parent) ? parentMap.get(parent) : 0;
    parentMap.set(parent, idx + 1);

    el.classList.add('rev');
    /* Stagger up to 5 siblings; 90ms step */
    el.style.transitionDelay = (Math.min(idx, 4) * 0.09) + 's';

    io.observe(el);
  });

})();
