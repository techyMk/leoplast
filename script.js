// DOM Elements
const navbar = document.getElementById('navbar');
const loader = document.getElementById('loader');

// Loader
window.addEventListener('load', () => {
    setTimeout(() => {
        loader.style.opacity = '0';
        setTimeout(() => {
            loader.style.display = 'none';
        }, 500);
    }, 1000);
});

// Sticky Navbar Transition
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('bg-white/90', 'backdrop-blur-md', 'shadow-md', 'py-2');
        navbar.classList.remove('bg-transparent', 'py-4', 'text-white');
        navbar.classList.add('text-brand-blue-900');

        // Update Logo/Button colors if needed via CSS classes, 
        // but for now relying on text color inheritance
    } else {
        navbar.classList.remove('bg-white/90', 'backdrop-blur-md', 'shadow-md', 'py-2', 'text-brand-blue-900');
        navbar.classList.add('bg-transparent', 'py-4', 'text-white');
    }
});

// Mobile Menu Toggle
const menuBtn = document.getElementById('menu-btn');
// Simple mobile menu logic (expand later if needed)
menuBtn.addEventListener('click', () => {
    // Toggle mobile menu visibility
    alert('Mobile menu clicked - To be implemented fully');
});


// Intersection Observer for Scroll Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-fade-in-up');
            entry.target.style.opacity = '1';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Add animation classes to elements
document.querySelectorAll('section h2, section p, .group').forEach(el => {
    el.classList.add('opacity-0', 'transition-all', 'duration-700', 'transform', 'translate-y-10');
    observer.observe(el);
});

// Custom Animation Class Helper
// We use a simple class toggle for the observer, but Tailwind handles the transition.
// The initial state is opacity-0 and translate-y-10.
// When 'animate-fade-in-up' (or similar) is added, we reset those.
// Actually, let's define the 'active' state in CSS or via class removal.

// Better approach:
const revealElements = document.querySelectorAll('section h2, section p, .group, .glass-dark');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.remove('opacity-0', 'translate-y-10');
            entry.target.classList.add('opacity-100', 'translate-y-0');
            revealObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

revealElements.forEach(el => {
    el.classList.add('opacity-0', 'translate-y-10', 'transition-all', 'duration-1000', 'ease-out');
    revealObserver.observe(el);
});
