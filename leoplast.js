// =============================================
// LEOPLAST — Shared JavaScript v2
// =============================================

document.addEventListener('DOMContentLoaded', () => {
    initLoader();
    initNavbar();
    initMobileMenu();
    initScrollReveal();
    initVideoPlayer();
    initSlider();
    initCounters();
    initActiveLinks();
    initMoveToTop();
    lucide.createIcons();
});

// ========================
// MOVE TO TOP BUTTON
// ========================
function initMoveToTop() {
    const btn = document.getElementById('move-to-top');
    if (!btn) return;
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            btn.classList.add('show');
        } else {
            btn.classList.remove('show');
        }
    }, { passive: true });
    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// ========================
// ACTIVE LINK HANDLER
// ========================
function initActiveLinks() {
    let currentPath = window.location.pathname.split('/').pop();
    if (!currentPath || currentPath === '') currentPath = 'index.html';

    const links = document.querySelectorAll('.nav-link');
    links.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            // Add active state class for CSS styling
            link.classList.add('active-page');
            if (currentPath === 'roofing.html') {
                link.classList.add('roofing-active');
            }
            link.addEventListener('click', (e) => {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
    });
}

// ========================
// LOADER
// ========================
function initLoader() {
    const loader = document.getElementById('loader');
    if (!loader) return;
    window.addEventListener('load', () => {
        setTimeout(() => {
            loader.classList.add('hidden');
            setTimeout(() => { loader.style.display = 'none'; }, 700);
        }, 1400);
    });
}

// ========================
// NAVBAR — sticky scroll
// ========================
function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;
    const update = () => {
        if (window.scrollY > 60) navbar.classList.add('scrolled');
        else navbar.classList.remove('scrolled');
    };
    window.addEventListener('scroll', update, { passive: true });
    update();
}

// ========================
// MOBILE MENU — fixed
// ========================
function initMobileMenu() {
    const btn = document.getElementById('menu-btn');
    const menu = document.getElementById('mobile-menu');
    if (!btn || !menu) return;

    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = menu.classList.toggle('active');
        btn.setAttribute('aria-expanded', isOpen);
        // swap icon
        btn.innerHTML = isOpen
            ? '<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
            : '<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
    });

    // close when a menu link is clicked
    menu.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
            menu.classList.remove('active');
            btn.setAttribute('aria-expanded', 'false');
            btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
        });
    });

    // close on outside click
    document.addEventListener('click', (e) => {
        if (!menu.contains(e.target) && !btn.contains(e.target)) {
            menu.classList.remove('active');
            btn.setAttribute('aria-expanded', 'false');
        }
    });
}

// ========================
// HERO SLIDESHOW
// ========================
let slideIndex = 0;
let slideInterval = null;

function initSlider() {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.slider-dot');
    if (!slides.length) return;

    function goTo(n) {
        slides[slideIndex].classList.remove('active');
        dots[slideIndex]?.classList.remove('active');
        slideIndex = ((n % slides.length) + slides.length) % slides.length;
        slides[slideIndex].classList.add('active');
        dots[slideIndex]?.classList.add('active');
    }

    function resetInterval() {
        clearInterval(slideInterval);
        slideInterval = setInterval(() => goTo(slideIndex + 1), 4500);
    }

    document.querySelector('.slider-prev')?.addEventListener('click', () => { resetInterval(); goTo(slideIndex - 1); });
    document.querySelector('.slider-next')?.addEventListener('click', () => { resetInterval(); goTo(slideIndex + 1); });
    dots.forEach((dot, i) => dot.addEventListener('click', () => { resetInterval(); goTo(i); }));

    // Touch/swipe support for slideshow
    let touchStartX = 0;
    const hero = document.querySelector('.hero-slider');
    if (hero) {
        hero.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].clientX; }, { passive: true });
        hero.addEventListener('touchend', e => {
            const diff = touchStartX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 50) { resetInterval(); goTo(slideIndex + (diff > 0 ? 1 : -1)); }
        }, { passive: true });
    }

    slideInterval = setInterval(() => goTo(slideIndex + 1), 4500);
}

// ========================
// SCROLL REVEAL
// ========================
function initScrollReveal() {
    const els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });
    els.forEach(el => observer.observe(el));
}

// ========================
// VIDEO PLAYER
// ========================
function initVideoPlayer() {
    const thumb = document.getElementById('video-thumb');
    const iframe = document.getElementById('video-iframe');
    const playBtn = document.getElementById('play-btn');
    if (!thumb || !iframe) return;
    const activate = () => {
        thumb.classList.add('hidden');
        iframe.classList.add('active');
        iframe.style.display = 'block';
        if (iframe.tagName.toLowerCase() === 'video') {
            iframe.play();
        } else if (iframe.dataset.src) {
            iframe.src = iframe.dataset.src;
        }
    };
    thumb.addEventListener('click', activate);
    playBtn?.addEventListener('click', activate);
}

// ========================
// COUNTER ANIMATION
// ========================
function initCounters() {
    const statsSection = document.getElementById('stats-section');
    if (!statsSection) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                document.querySelectorAll('[data-count]').forEach(el => {
                    const target = parseInt(el.dataset.count);
                    const suffix = el.dataset.suffix || '';
                    let current = 0;
                    const step = Math.ceil(target / 60);
                    const timer = setInterval(() => {
                        current = Math.min(current + step, target);
                        el.textContent = current + suffix;
                        if (current >= target) clearInterval(timer);
                    }, 25);
                });
                observer.disconnect();
            }
        });
    }, { threshold: 0.3 });
    observer.observe(statsSection);
}

// ========================
// TOAST NOTIFICATION
// ========================
function showToast(message, type = 'success') {
    // Remove existing toast
    document.querySelectorAll('.lp-toast').forEach(t => t.remove());

    const toast = document.createElement('div');
    toast.className = 'lp-toast';
    const icon = type === 'success' ? '✅' : type === 'error' ? '❌' : 'ℹ️';
    const color = type === 'success' ? '#065f46' : type === 'error' ? '#7f1d1d' : '#1e40af';
    const bg = type === 'success' ? '#d1fae5' : type === 'error' ? '#fee2e2' : '#dbeafe';

    toast.innerHTML = `
        <div style="display:flex;align-items:center;gap:0.75rem;">
            <span style="font-size:1.25rem;">${icon}</span>
            <span style="flex:1;font-size:0.9rem;font-weight:600;color:${color};">${message}</span>
            <button onclick="this.parentElement.parentElement.remove()" style="background:none;border:none;cursor:pointer;font-size:1.1rem;color:${color};padding:0;line-height:1;">×</button>
        </div>`;

    Object.assign(toast.style, {
        position: 'fixed', bottom: '1.5rem', right: '1.5rem', zIndex: '99998',
        background: bg, border: `1.5px solid ${color}20`, borderRadius: '1rem',
        padding: '1rem 1.25rem', minWidth: '280px', maxWidth: '90vw',
        boxShadow: '0 8px 30px rgba(0,0,0,0.15)',
        fontFamily: "'Outfit', sans-serif",
        transform: 'translateY(20px)', opacity: '0',
        transition: 'all 0.35s ease'
    });

    document.body.appendChild(toast);
    requestAnimationFrame(() => {
        toast.style.transform = 'translateY(0)';
        toast.style.opacity = '1';
    });
    setTimeout(() => {
        toast.style.transform = 'translateY(20px)';
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 400);
    }, 5000);
}

// ========================
// CONTACT FORM (EmailJS)
// ========================
window.initContactForm = function () {
    const form = document.getElementById('contact-form');
    const btn = document.getElementById('submit-btn');
    if (!form || !btn) return;

    // Field references
    const fields = {
        fname: { el: document.getElementById('fname'), rule: v => v.trim().length >= 2, msg: 'Please enter your first name (min 2 characters).' },
        email: { el: document.getElementById('email'), rule: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v), msg: 'Please enter a valid email address.' },
        phone: { el: document.getElementById('phone'), rule: v => v.trim() === '' || /^[+\d\s\-()]{7,15}$/.test(v.trim()), msg: 'Please enter a valid phone number.' },
        message: { el: document.getElementById('message'), rule: v => v.trim().length >= 10, msg: 'Message must be at least 10 characters.' },
    };

    // Live error clearing
    Object.values(fields).forEach(({ el }) => {
        if (!el) return;
        el.addEventListener('input', () => clearError(el));
        el.addEventListener('focus', () => clearError(el));
    });

    function setError(el, msg) {
        clearError(el);
        el.style.borderColor = '#dc2626';
        const err = document.createElement('p');
        err.className = 'lp-field-error';
        err.textContent = msg;
        Object.assign(err.style, { color: '#dc2626', fontSize: '0.78rem', marginTop: '0.3rem', marginBottom: '0' });
        el.parentNode.appendChild(err);
    }

    function clearError(el) {
        el.style.borderColor = '#e5e7eb';
        const existing = el.parentNode.querySelector('.lp-field-error');
        if (existing) existing.remove();
    }

    function validate() {
        let valid = true;
        Object.entries(fields).forEach(([key, { el, rule, msg }]) => {
            if (!el) return;
            const val = el.value;
            if (!rule(val)) {
                setError(el, msg);
                valid = false;
            } else {
                clearError(el);
            }
        });
        return valid;
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!validate()) {
            showToast('Please fix the errors above before submitting.', 'error');
            return;
        }

        btn.disabled = true;
        btn.textContent = 'Sending…';

        const fname = fields.fname.el.value.trim();
        const lname = document.getElementById('lname')?.value.trim() || '';
        const email = fields.email.el.value.trim();
        const phone = fields.phone.el.value.trim() || 'Not provided';
        const subject = document.getElementById('subject')?.value || 'General Inquiry';
        const message = fields.message.el.value.trim();

        const templateParams = {
            from_name: `${fname} ${lname}`.trim(),
            from_email: email,
            phone,
            subject,
            message,
            reply_to: email,
            to_email: 'leoplastpipes@gmail.com'
        };

        try {
            // EmailJS send
            const result = await emailjs.send(
                'leoplast_service',    // Service ID — set in EmailJS dashboard
                'leoplast_template',   // Template ID — set in EmailJS dashboard
                templateParams
            );

            if (result.status === 200) {
                showModalSuccess(fname);
                form.reset();
            } else {
                throw new Error('Unexpected response');
            }
        } catch (err) {
            console.error('EmailJS error:', err);
            showToast('Something went wrong. Please try calling us directly or email leoplastpipes@gmail.com', 'error');
        } finally {
            btn.disabled = false;
            btn.textContent = 'Send Message →';
        }
    });
};

// ========================
// SUCCESS MODAL (popup)
// ========================
function showModalSuccess(name) {
    // Backdrop
    const backdrop = document.createElement('div');
    Object.assign(backdrop.style, {
        position: 'fixed', inset: '0', background: 'rgba(0,0,0,0.55)',
        zIndex: '99999', display: 'flex', alignItems: 'center', justifyContent: 'center',
        padding: '1.5rem', backdropFilter: 'blur(4px)', opacity: '0', transition: 'opacity 0.3s'
    });

    backdrop.innerHTML = `
        <div id="success-modal" style="
            background:white; border-radius:1.5rem; padding:2.5rem 2rem;
            max-width:420px; width:100%; text-align:center;
            box-shadow:0 25px 60px rgba(0,0,0,0.25);
            transform:translateY(30px); opacity:0; transition:all 0.35s ease;
            font-family:'Outfit',sans-serif;
        ">
            <div style="width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg,#d1fae5,#a7f3d0);display:flex;align-items:center;justify-content:center;margin:0 auto 1.25rem;font-size:2rem;">✅</div>
            <h2 style="font-size:1.5rem;font-weight:800;color:#0c1f3f;margin-bottom:0.75rem;">Message Sent!</h2>
            <p style="color:#6b7280;line-height:1.7;margin-bottom:0.5rem;">Thank you, <strong style="color:#0c1f3f;">${name}</strong>! We've received your message and will get back to you within <strong style="color:#2563eb;">24 hours</strong>.</p>
            <p style="color:#9ca3af;font-size:0.85rem;margin-bottom:1.75rem;">A copy will also be sent to <strong>leoplastpipes@gmail.com</strong></p>
            <button onclick="document.getElementById('lp-modal-backdrop').remove()" style="
                padding:0.75rem 2rem; background:linear-gradient(135deg,#1e4d8c,#0c1f3f);
                color:white; border:none; border-radius:9999px; font-family:'Outfit',sans-serif;
                font-size:1rem; font-weight:700; cursor:pointer; transition:transform 0.2s;
                box-shadow:0 4px 15px rgba(37,99,235,0.3);"
                onmouseover="this.style.transform='translateY(-2px)'"
                onmouseout="this.style.transform='translateY(0)'">
                Done 👍
            </button>
        </div>`;

    backdrop.id = 'lp-modal-backdrop';
    document.body.appendChild(backdrop);

    requestAnimationFrame(() => {
        backdrop.style.opacity = '1';
        const modal = document.getElementById('success-modal');
        if (modal) { modal.style.transform = 'translateY(0)'; modal.style.opacity = '1'; }
    });

    // Close on backdrop click
    backdrop.addEventListener('click', (e) => {
        if (e.target === backdrop) backdrop.remove();
    });
}
