document.addEventListener('DOMContentLoaded', () => {

  const safe = (name, fn) => {
    try { fn(); } catch (err) { console.error('[art-detailing]', name, err); }
  };

  /* ---------- sticky header shrink ---------- */
  safe('header-scroll', () => {
    const header = document.querySelector('.site-header');
    if (!header) return;
    const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 12);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  });

  /* ---------- mobile nav ---------- */
  safe('mobile-nav', () => {
    const burger = document.querySelector('.burger');
    const mobileNav = document.querySelector('.mobile-nav');
    const mobileClose = document.querySelector('.mobile-nav-close');
    if (!mobileNav) return;
    const openMobile = () => { mobileNav.classList.add('is-open'); document.body.style.overflow = 'hidden'; };
    const closeMobile = () => { mobileNav.classList.remove('is-open'); document.body.style.overflow = ''; };
    if (burger) burger.addEventListener('click', openMobile);
    if (mobileClose) mobileClose.addEventListener('click', closeMobile);
    mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMobile));
  });

  /* ---------- active nav link by current page ---------- */
  safe('active-nav', () => {
    const path = (window.location.pathname.split('/').pop() || 'index.html').split('#')[0] || 'index.html';
    document.querySelectorAll('nav.main-nav a, .mobile-nav a').forEach(a => {
      const href = a.getAttribute('href');
      if (!href) return;
      const hrefFile = href.split('/').pop().split('#')[0];
      if (hrefFile === path) a.classList.add('active');
    });
  });

  /* ---------- reveal on scroll (sparingly applied via .reveal class) ---------- */
  safe('reveal', () => {
    const revealEls = document.querySelectorAll('.reveal');
    if (!revealEls.length) return;
    if (!('IntersectionObserver' in window)) {
      revealEls.forEach(el => el.classList.add('is-visible'));
      return;
    }
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(el => io.observe(el));
  });

  /* ---------- animated counters ---------- */
  safe('counters', () => {
    const counters = document.querySelectorAll('.js-count');
    if (!counters.length) return;
    const animate = (el) => {
      const target = parseFloat(el.dataset.count);
      if (isNaN(target)) return;
      const duration = 1400;
      const start = performance.now();
      const step = (now) => {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        const val = target * eased;
        el.textContent = (target % 1 === 0) ? Math.round(val) : val.toFixed(1);
        if (p < 1) requestAnimationFrame(step);
        else el.textContent = target % 1 === 0 ? target : target.toFixed(1);
      };
      requestAnimationFrame(step);
    };
    if (!('IntersectionObserver' in window)) {
      counters.forEach(animate);
      return;
    }
    const cio = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) { animate(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(el => cio.observe(el));
  });

  /* ---------- services tabs ---------- */
  safe('service-tabs', () => {
    const tabs = document.querySelectorAll('.svc-tab');
    const panels = document.querySelectorAll('.svc-panel');
    if (!tabs.length) return;
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const id = tab.dataset.target;
        tabs.forEach(t => t.classList.remove('is-active'));
        panels.forEach(p => p.classList.remove('is-active'));
        tab.classList.add('is-active');
        const panel = document.getElementById(id);
        if (panel) panel.classList.add('is-active');
      });
    });
  });

  /* ---------- FAQ accordion ---------- */
  safe('faq', () => {
    document.querySelectorAll('.faq-item').forEach(item => {
      const q = item.querySelector('.faq-q');
      const a = item.querySelector('.faq-a');
      if (!q || !a) return;
      q.addEventListener('click', () => {
        const isOpen = item.classList.contains('is-open');
        const list = item.parentElement ? item.parentElement.querySelectorAll('.faq-item') : [item];
        list.forEach(other => {
          other.classList.remove('is-open');
          const oa = other.querySelector('.faq-a');
          if (oa) oa.style.maxHeight = null;
        });
        if (!isOpen) {
          item.classList.add('is-open');
          a.style.maxHeight = a.scrollHeight + 'px';
        }
      });
    });
  });

  /* ---------- gallery filter ---------- */
  safe('gallery-filter', () => {
    const chips = document.querySelectorAll('.chip[data-filter]');
    const cells = document.querySelectorAll('.gallery-cell');
    if (!chips.length) return;
    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        chips.forEach(c => c.classList.remove('is-active'));
        chip.classList.add('is-active');
        const f = chip.dataset.filter;
        cells.forEach(cell => {
          const show = f === 'all' || cell.dataset.cat === f;
          cell.style.display = show ? '' : 'none';
        });
      });
    });
  });

  /* ---------- before / after slider ---------- */
  safe('before-after', () => {
    document.querySelectorAll('.ba').forEach(ba => {
      const after = ba.querySelector('.ba-after');
      const line = ba.querySelector('.ba-line');
      const handle = ba.querySelector('.ba-handle');
      if (!after || !line || !handle) return;
      let dragging = false;

      const setPos = (clientX) => {
        const rect = ba.getBoundingClientRect();
        let pct = ((clientX - rect.left) / rect.width) * 100;
        pct = Math.max(2, Math.min(98, pct));
        after.style.clipPath = `inset(0 0 0 ${pct}%)`;
        line.style.left = pct + '%';
        handle.style.left = pct + '%';
      };

      handle.addEventListener('pointerdown', (e) => {
        dragging = true;
        if (handle.setPointerCapture) handle.setPointerCapture(e.pointerId);
      });
      window.addEventListener('pointerup', () => dragging = false);
      ba.addEventListener('pointermove', (e) => { if (dragging) setPos(e.clientX); });
      ba.addEventListener('click', (e) => setPos(e.clientX));
    });
  });

  /* ---------- contact form (front-end only demo) ---------- */
  safe('contact-form', () => {
    const form = document.querySelector('.js-contact-form');
    if (!form) return;
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      form.style.display = 'none';
      const success = document.querySelector('.form-success');
      if (success) success.classList.add('is-visible');
    });
  });

});
