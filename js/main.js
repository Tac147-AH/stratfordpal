/* =============================================
   STRATFORD PAL — MAIN JAVASCRIPT
   ============================================= */

'use strict';

// ── Nav: scroll behavior & mobile toggle ──────────────────
(function initNav() {
  const nav = document.querySelector('.nav');
  const hamburger = document.querySelector('.nav-hamburger');
  const mobileNav = document.querySelector('.nav-mobile');
  if (!nav) return;

  // Scroll: add .scrolled class
  function onScroll() {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Hamburger toggle
  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      const open = mobileNav.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', open);
      hamburger.querySelectorAll('span')[0].style.transform = open ? 'rotate(45deg) translate(5px, 5px)' : '';
      hamburger.querySelectorAll('span')[1].style.opacity  = open ? '0' : '';
      hamburger.querySelectorAll('span')[2].style.transform = open ? 'rotate(-45deg) translate(5px, -5px)' : '';
    });
  }

  // Active link highlight
  const currentPath = window.location.pathname.replace(/\/$/, '').split('/').pop() || 'index';
  document.querySelectorAll('.nav-links a, .nav-mobile a').forEach(link => {
    const href = link.getAttribute('href') || '';
    const page = href.replace(/\/$/, '').split('/').pop() || 'index';
    if (page === currentPath || (currentPath === '' && page === 'index')) {
      link.classList.add('active');
    }
  });
})();

// ── Smooth scroll for anchor links ────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ── Counter animation ─────────────────────────────────────
function animateCounter(el, target, duration = 1800) {
  const isPlus = String(target).includes('+');
  const num = parseInt(String(target).replace(/[^0-9]/g, ''));
  let start = null;
  function step(ts) {
    if (!start) start = ts;
    const progress = Math.min((ts - start) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(ease * num);
    el.textContent = current.toLocaleString() + (isPlus ? '+' : '');
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

// ── Intersection Observer for animations ─────────────────
const observerOptions = { threshold: 0.15, rootMargin: '0px 0px -40px 0px' };
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      // Counter animation
      if (entry.target.dataset.count !== undefined) {
        animateCounter(entry.target, entry.target.dataset.count);
      }
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.animate-on-scroll, [data-count]').forEach(el => observer.observe(el));

// ── Program filter (programs page) ───────────────────────
(function initProgramFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.program-card[data-category]');
  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filter;
      cards.forEach(card => {
        const match = cat === 'all' || card.dataset.category === cat;
        card.style.display = match ? '' : 'none';
      });
    });
  });
})();

// ── Contact form handling ─────────────────────────────────
(function initContactForm() {
  const form = document.querySelector('#contact-form');
  if (!form) return;
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.textContent;
    btn.textContent = 'Sending…';
    btn.disabled = true;
    // Simulate send (replace with actual backend/formspree)
    setTimeout(() => {
      const success = document.querySelector('#form-success');
      if (success) {
        form.style.display = 'none';
        success.style.display = 'block';
      } else {
        btn.textContent = '✓ Message Sent!';
        btn.style.background = 'var(--success)';
      }
    }, 1200);
  });
})();

// ── Sticky CTA bar for mobile (homepage) ─────────────────
(function initStickyMobileCTA() {
  const bar = document.querySelector('.mobile-cta-bar');
  if (!bar) return;
  window.addEventListener('scroll', () => {
    bar.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });
})();
