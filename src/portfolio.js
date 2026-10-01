/* ===== NAVBAR SCROLL ===== */
const navbar = document.getElementById('navbar');
const backToTop = document.getElementById('back-to-top');

window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    navbar.classList.add('scrolled');
    backToTop.classList.add('show');
  } else {
    navbar.classList.remove('scrolled');
    backToTop.classList.remove('show');
  }
  highlightNav();
  revealOnScroll();
  animateSkillBars();
});

backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

/* ===== HAMBURGER MENU ===== */
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  navLinks.classList.toggle('open');
});

navLinks.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('open');
    navLinks.classList.remove('open');
  });
});

/* ===== ACTIVE NAV HIGHLIGHT ===== */
function highlightNav() {
  const sections = document.querySelectorAll('section[id]');
  const scrollPos = window.scrollY + 100;
  sections.forEach(section => {
    const top = section.offsetTop;
    const height = section.offsetHeight;
    const id = section.getAttribute('id');
    const link = document.querySelector(`.nav-link[href="#${id}"]`);
    if (link) {
      if (scrollPos >= top && scrollPos < top + height) {
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
      }
    }
  });
}

/* ===== TYPEWRITER EFFECT ===== */
const roles = ['Aspiring Software Engineer', 'Full-Stack Developer', 'Computer Science Student'];
let roleIndex = 0, charIndex = 0, isDeleting = false;
const roleText = document.getElementById('role-text');

function typeWriter() {
  const current = roles[roleIndex];
  if (isDeleting) {
    roleText.textContent = current.substring(0, charIndex--);
  } else {
    roleText.textContent = current.substring(0, charIndex++);
  }
  let speed = isDeleting ? 60 : 110;
  if (!isDeleting && charIndex === current.length + 1) {
    speed = 1800;
    isDeleting = true;
  } else if (isDeleting && charIndex === -1) {
    isDeleting = false;
    charIndex = 0;
    roleIndex = (roleIndex + 1) % roles.length;
    speed = 300;
  }
  setTimeout(typeWriter, speed);
}
typeWriter();

/* ===== SKILL BAR ANIMATION ===== */
let skillsAnimated = false;
function animateSkillBars() {
  if (skillsAnimated) return;
  const skillsSection = document.getElementById('skills');
  if (!skillsSection) return;
  const top = skillsSection.offsetTop;
  if (window.scrollY + window.innerHeight > top + 100) {
    skillsAnimated = true;
    document.querySelectorAll('.skill-fill').forEach(bar => {
      const target = bar.getAttribute('data-width');
      bar.style.width = target + '%';
    });
  }
}

/* ===== PROJECT FILTER ===== */
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.getAttribute('data-filter');
    projectCards.forEach(card => {
      const cat = card.getAttribute('data-cat');
      if (filter === 'all' || cat === filter) {
        card.classList.remove('hidden');
        card.style.animation = 'fadeIn .4s ease forwards';
      } else {
        card.classList.add('hidden');
      }
    });
  });
});



/* ===== CONTACT FORM ===== */
const contactForm = document.getElementById('contact-form');
const formSuccess = document.getElementById('form-success');

if (contactForm) {
  contactForm.addEventListener('submit', async (e) => { 
    e.preventDefault();
    const btn = contactForm.querySelector('button[type="submit"]');
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
    btn.disabled = true;

    const formData = new FormData(contactForm);

    try {
      const response = await fetch(contactForm.action, {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      });

      if (response.ok) {
        contactForm.reset();
        if (formSuccess) {
          formSuccess.classList.add('show');
          setTimeout(() => formSuccess.classList.remove('show'), 5000);
        }
      } else {
        // Fallback to direct mailto if form service fails
        const name = formData.get('name') || '';
        const email = formData.get('email') || '';
        const subject = formData.get('subject') || 'Portfolio Contact Inquiry';
        const message = formData.get('message') || '';
        window.location.href = `mailto:amanprasad38649@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(`From: ${name} (${email})\n\n${message}`)}`;
        contactForm.reset();
        if (formSuccess) {
          formSuccess.classList.add('show');
          setTimeout(() => formSuccess.classList.remove('show'), 5000);
        }
      }
    } catch (err) {
      const name = formData.get('name') || '';
      const email = formData.get('email') || '';
      const subject = formData.get('subject') || 'Portfolio Contact Inquiry';
      const message = formData.get('message') || '';
      window.location.href = `mailto:amanprasad38649@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(`From: ${name} (${email})\n\n${message}`)}`;
      contactForm.reset();
      if (formSuccess) {
        formSuccess.classList.add('show');
        setTimeout(() => formSuccess.classList.remove('show'), 5000);
      }
    } finally {
      btn.innerHTML = '<i class="fas fa-paper-plane"></i> Send Message';
      btn.disabled = false;
    }
  });
}

/* ===== SCROLL REVEAL ===== */
function revealOnScroll() {
  document.querySelectorAll('.reveal').forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight - 80) {
      el.classList.add('visible');
    }
  });
}

// Add reveal class dynamically
document.querySelectorAll('.skill-card, .project-card, .about-content, .about-image-wrap, .timeline-content, .contact-info, .contact-form, .testimonial-slider, .section-header, .skill-category-card').forEach(el => {
  el.classList.add('reveal');
});

// Initial checks on load
window.dispatchEvent(new Event('scroll'));
revealOnScroll();
animateSkillBars();

/* ===== EXTERNAL LINK FIX ===== */
// This ensures links to sites like LinkedIn, GitHub, etc. open in a clean new tab
// bypassing common "blocked by response" iframe errors in preview environments
document.querySelectorAll('a[target="_blank"]').forEach(link => {
  link.addEventListener('click', (e) => {
    const url = link.getAttribute('href');
    if (url && url !== '#') {
      e.preventDefault();
      // Use window.open with 'noopener,noreferrer' for maximum compatibility and security
      const newWindow = window.open(url, '_blank', 'noopener,noreferrer');
      if (newWindow) {
        newWindow.opener = null;
      }
    }
  });
});
