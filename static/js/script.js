// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 70;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    const navRight  = document.querySelector('.nav-right');
    
    if (hamburger && navRight) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navRight.classList.toggle('active');
        });
    }

    // Scroll progress, navbar, back-to-top, active nav
    const navbar = document.querySelector('.navbar');
    const scrollProgress = document.getElementById('scrollProgress');
    const backToTop = document.getElementById('backToTop');
    const sections = document.querySelectorAll('section[id]');

    function onScroll() {
        const scrollY = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;

        if (scrollProgress && docHeight > 0) {
            scrollProgress.style.width = (scrollY / docHeight) * 100 + '%';
        }

        if (navbar) {
            navbar.classList.toggle('scrolled', scrollY > 50);
        }

        if (backToTop) {
            backToTop.classList.toggle('visible', scrollY > 400);
        }

        let current = '';
        sections.forEach(section => {
            if (scrollY >= section.offsetTop - 120) {
                current = section.getAttribute('id');
            }
        });
        navLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === '#' + current);
        });
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Skills section - no animation needed for tag-style skills

    // Contact form handling
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            const formData = new FormData(this);
            const data = Object.fromEntries(formData);

            if (!data.name || !data.email || !data.subject || !data.message) {
                showNotification('Please fill in all fields', 'error');
                return;
            }

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(data.email)) {
                showNotification('Please enter a valid email address', 'error');
                return;
            }

            const btn = this.querySelector('button[type="submit"]');
            btn.disabled = true;
            btn.textContent = 'Sending...';

            try {
                const response = await fetch('/api/contact/send', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                if (response.ok) {
                    showNotification("Message sent successfully! I'll get back to you soon.", 'success');
                    this.reset();
                } else {
                    showNotification('Error: ' + (result.error || 'Could not send message.'), 'error');
                }
            } catch (err) {
                showNotification('Something went wrong. Please try again.', 'error');
            } finally {
                btn.disabled = false;
                btn.textContent = 'Send Message';
            }
        });
    }

    // Notification system
    function showNotification(message, type = 'info') {
        // Remove existing notifications
        const existingNotifications = document.querySelectorAll('.notification');
        existingNotifications.forEach(notification => notification.remove());
        
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span class="notification-message">${message}</span>
                <button class="notification-close">&times;</button>
            </div>
        `;
        
        // Add styles
        document.body.appendChild(notification);
        
        // Close button functionality
        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            notification.remove();
        });
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }

    // ===== SCROLL ANIMATIONS =====
    // Assign animation types to elements before observing
    const animationMap = [
        // fade up — general cards
        { selector: '.project-card',        anim: 'fade-up',    stagger: true },
        { selector: '.certification-card',  anim: 'fade-up',    stagger: true },
        { selector: '.internship-card',     anim: 'fade-up',    stagger: true },
        // fade in from left
        { selector: '.about-text',          anim: 'fade-left',  stagger: false },
        { selector: '.contact-info',        anim: 'fade-left',  stagger: false },
        // fade in from right
        { selector: '.about-image',         anim: 'fade-right', stagger: false },
        { selector: '.contact-form',        anim: 'fade-right', stagger: false },
        // zoom in
        { selector: '.skill-category',      anim: 'zoom-in',    stagger: true },
        { selector: '.stat',                anim: 'zoom-in',    stagger: true },
        // slide up with stagger
        { selector: '.education-item',      anim: 'slide-up',   stagger: true },
        // section titles
        { selector: '.section-title',       anim: 'fade-up',    stagger: false },
        // hero elements
        { selector: '.hero-content',        anim: 'fade-left',  stagger: false },
        { selector: '.hero-image',          anim: 'fade-right', stagger: false },
    ];

    // Add CSS for scroll animations
    const scrollAnimCSS = document.createElement('style');
    scrollAnimCSS.textContent = `
        /* Base hidden state */
        .sa-hidden {
            opacity: 0;
            will-change: transform, opacity;
        }
        .sa-fade-up    { transform: translateY(50px); }
        .sa-fade-left  { transform: translateX(-50px); }
        .sa-fade-right { transform: translateX(50px); }
        .sa-zoom-in    { transform: scale(0.85); }
        .sa-slide-up   { transform: translateY(70px); }

        /* Visible state */
        .sa-visible {
            opacity: 1 !important;
            transform: none !important;
            transition: opacity 0.7s cubic-bezier(0.22,1,0.36,1),
                        transform 0.7s cubic-bezier(0.22,1,0.36,1);
        }

        /* Stagger delays */
        .sa-delay-1 { transition-delay: 0.05s !important; }
        .sa-delay-2 { transition-delay: 0.15s !important; }
        .sa-delay-3 { transition-delay: 0.25s !important; }
        .sa-delay-4 { transition-delay: 0.35s !important; }
        .sa-delay-5 { transition-delay: 0.45s !important; }
        .sa-delay-6 { transition-delay: 0.55s !important; }

        /* Parallax subtle layer */
        .hero::before {
            will-change: transform;
        }
    `;
    document.head.appendChild(scrollAnimCSS);

    // Apply hidden classes
    animationMap.forEach(({ selector, anim, stagger }) => {
        const els = document.querySelectorAll(selector);
        els.forEach((el, i) => {
            // Skip if already in viewport on load (hero elements)
            el.classList.add('sa-hidden', `sa-${anim}`);
            if (stagger) {
                const delay = (i % 6) + 1;
                el.classList.add(`sa-delay-${delay}`);
            }
        });
    });

    // IntersectionObserver
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('sa-visible');
                scrollObserver.unobserve(entry.target); // animate once
            }
        });
    }, {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
    });

    document.querySelectorAll('.sa-hidden').forEach(el => scrollObserver.observe(el));

    // Hero text block is animated via CSS keyframe (heroFadeUp) — no JS needed

    // ── Hero video controls ──────────────────────────────────
    const heroBgVideo  = document.getElementById('heroBgVideo');
    const heroPlayBtn  = document.getElementById('heroPlayBtn');
    const heroPlayIcon = document.getElementById('heroPlayIcon');
    const heroMuteBtn  = document.getElementById('heroMuteBtn');
    const heroMuteIcon = document.getElementById('heroMuteIcon');

    if (heroBgVideo && heroPlayBtn) {
        heroPlayBtn.addEventListener('click', () => {
            if (heroBgVideo.paused) {
                heroBgVideo.play();
                heroPlayIcon.classList.replace('fa-play', 'fa-pause');
                heroPlayBtn.setAttribute('aria-label', 'Pause video');
            } else {
                heroBgVideo.pause();
                heroPlayIcon.classList.replace('fa-pause', 'fa-play');
                heroPlayBtn.setAttribute('aria-label', 'Play video');
            }
        });
    }

    if (heroBgVideo && heroMuteBtn) {
        heroMuteBtn.addEventListener('click', () => {
            heroBgVideo.muted = !heroBgVideo.muted;
            if (heroBgVideo.muted) {
                heroMuteIcon.classList.replace('fa-volume-up', 'fa-volume-mute');
                heroMuteBtn.setAttribute('aria-label', 'Unmute video');
            } else {
                heroMuteIcon.classList.replace('fa-volume-mute', 'fa-volume-up');
                heroMuteBtn.setAttribute('aria-label', 'Mute video');
            }
        });
    }

    // Scroll indicator click — scroll to next section
    const heroScroll = document.querySelector('.hero-scroll');
    if (heroScroll) {
        heroScroll.addEventListener('click', () => {
            const nextSection = document.querySelector('#about') || document.querySelector('section:nth-of-type(2)');
            if (nextSection) nextSection.scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Subtle parallax on hero background grid only (no layout shift)
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            if (scrolled < window.innerHeight) {
                heroSection.style.backgroundPositionY = `${scrolled * 0.3}px`;
            }
        }, { passive: true });
    }

    // Click-to-copy email functionality
    const copyEmailBtn = document.getElementById('copy-email-btn');
    if (copyEmailBtn) {
        copyEmailBtn.addEventListener('click', function() {
            const emailSpan = document.getElementById('contact-email');
            if (emailSpan) {
                const emailText = emailSpan.textContent.trim();
                navigator.clipboard.writeText(emailText).then(() => {
                    const icon = document.getElementById('copy-email-icon');
                    if (icon) {
                        icon.className = 'fas fa-check';
                        copyEmailBtn.classList.add('copied');
                        setTimeout(() => {
                            icon.className = 'far fa-copy';
                            copyEmailBtn.classList.remove('copied');
                        }, 2000);
                    }
                }).catch(err => {
                    console.error('Failed to copy text: ', err);
                });
            }
        });
    }

    // Hero title displays immediately - no typing effect needed
});

// Mobile menu styles (injected once)
if (!document.getElementById('mobile-nav-styles')) {
    const styleSheet = document.createElement('style');
    styleSheet.id = 'mobile-nav-styles';
    styleSheet.textContent = `
        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        @media (max-width: 768px) {
            .nav-right {
                display: none;
            }
            .nav-right.active {
                display: flex;
                flex-direction: column;
                position: fixed;
                left: 0;
                top: 70px;
                width: 100%;
                background: rgba(10, 10, 10, 0.98);
                backdrop-filter: blur(12px);
                padding: 16px 0 20px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
                z-index: 999;
                align-items: center;
                gap: 0;
            }
            .nav-right.active .nav-menu {
                display: flex !important;
                flex-direction: column;
                width: 100%;
                text-align: center;
                gap: 0;
            }
            .nav-right.active .nav-menu .nav-link {
                padding: 14px 20px;
                display: block;
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            }
            .nav-right.active .nav-actions {
                margin-top: 16px;
                margin-left: 0;
                justify-content: center;
                padding-bottom: 4px;
            }
            .hamburger.active span:nth-child(2) { opacity: 0; }
            .hamburger.active span:nth-child(1) { transform: translateY(8px) rotate(45deg); }
            .hamburger.active span:nth-child(3) { transform: translateY(-8px) rotate(-45deg); }
        }
    `;
    document.head.appendChild(styleSheet);
}

// ===== LIGHT / DARK MODE TOGGLE =====
(function () {
    const btn  = document.getElementById('theme-toggle');
    const icon = document.getElementById('theme-icon');
    if (!btn) return;

    // Restore saved preference
    const saved = localStorage.getItem('theme');
    if (saved === 'light') {
        document.body.classList.add('light-mode');
        icon.classList.replace('fa-sun', 'fa-moon');
    }

    btn.addEventListener('click', function () {
        const isLight = document.body.classList.toggle('light-mode');
        if (isLight) {
            icon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('theme', 'light');
        } else {
            icon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('theme', 'dark');
        }
    });
})();