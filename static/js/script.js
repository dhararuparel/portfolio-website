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
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // Navbar background on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        const isLight = document.body.classList.contains('light-mode');
        if (window.scrollY > 50) {
            navbar.style.background = isLight
                ? 'rgba(244, 244, 248, 0.99)'
                : 'rgba(10, 10, 10, 0.98)';
        } else {
            navbar.style.background = '';
        }
    });

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
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? 'rgba(40, 167, 69, 0.9)' : 'rgba(220, 53, 69, 0.9)'};
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
            border: 1px solid ${type === 'success' ? 'rgba(40, 167, 69, 0.3)' : 'rgba(220, 53, 69, 0.3)'};
            z-index: 10000;
            animation: slideInRight 0.3s ease-out;
            max-width: 400px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        `;
        
        // Add animation styles
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideInRight {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            
            .notification-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 15px;
            }
            
            .notification-close {
                background: none;
                border: none;
                color: white;
                font-size: 20px;
                cursor: pointer;
                padding: 0;
                width: 20px;
                height: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .notification-close:hover {
                opacity: 0.7;
            }
        `;
        
        document.head.appendChild(style);
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

    // Trigger hero elements immediately (they're in viewport on load)
    document.querySelectorAll('.hero-content, .hero-image').forEach(el => {
        setTimeout(() => el.classList.add('sa-visible'), 100);
    });

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

    // Hero title displays immediately - no typing effect needed
});

// Add mobile menu styles
const mobileMenuStyles = `
    @media (max-width: 768px) {
        .nav-menu {
            position: fixed;
            left: -100%;
            top: 70px;
            flex-direction: column;
            background: rgba(10, 10, 10, 0.98);
            backdrop-filter: blur(10px);
            width: 100%;
            text-align: center;
            transition: 0.3s;
            box-shadow: 0 10px 27px rgba(0, 0, 0, 0.05);
            padding: 20px 0;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .nav-menu.active {
            left: 0;
        }

        .nav-menu .nav-link {
            padding: 15px;
            display: block;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .hamburger.active span:nth-child(2) {
            opacity: 0;
        }

        .hamburger.active span:nth-child(1) {
            transform: translateY(8px) rotate(45deg);
        }

        .hamburger.active span:nth-child(3) {
            transform: translateY(-8px) rotate(-45deg);
        }
    }
`;

// Add the mobile menu styles to the document
const styleSheet = document.createElement('style');
styleSheet.textContent = mobileMenuStyles;
document.head.appendChild(styleSheet);

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