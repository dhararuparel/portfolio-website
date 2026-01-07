// API Configuration
const API_BASE_URL = 'https://your-backend-url.onrender.com'; // Will be updated after Render deployment

// DOM Elements
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Load portfolio data
    loadPortfolioData();

    // Contact form handler
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', handleContactForm);
    }
});

// Load all portfolio data from backend
async function loadPortfolioData() {
    try {
        // Load all data in parallel
        const [projects, skills, education, certifications, internships, contact] = await Promise.all([
            fetchData('/api/projects'),
            fetchData('/api/skills'),
            fetchData('/api/education'),
            fetchData('/api/certifications'),
            fetchData('/api/internships'),
            fetchData('/api/contact')
        ]);

        // Render all sections
        renderProjects(projects);
        renderSkills(skills);
        renderEducation(education);
        renderCertifications(certifications);
        renderInternships(internships);
        renderContact(contact);
        updateStats(projects, internships, certifications);
    } catch (error) {
        console.error('Error loading portfolio data:', error);
        // Fallback to static content if API fails
        loadFallbackData();
    }
}

// Fetch data from API
async function fetchData(endpoint) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`);
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
}

// Render projects
function renderProjects(projects) {
    const container = document.getElementById('projects-container');
    if (!container || !projects) return;

    container.innerHTML = projects.map(project => `
        <div class="project-card">
            <div class="project-header">
                <h3>${project.title}</h3>
                <div class="project-meta">
                    <span class="duration">${project.duration}</span>
                    <span class="team-size">Team: ${project.team_size}</span>
                </div>
            </div>
            <div class="project-content">
                <p class="project-description">${project.description}</p>
                <div class="project-role">
                    <strong>Role:</strong> ${project.role}
                </div>
                <div class="project-tech">
                    <h4>Technologies Used:</h4>
                    <div class="tech-tags">
                        ${project.technologies.split(', ').map(tech => 
                            `<span class="tech-tag">${tech}</span>`
                        ).join('')}
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

// Render skills
function renderSkills(skills) {
    const container = document.getElementById('skills-container');
    if (!container || !skills) return;

    // Group skills by category
    const skillsByCategory = skills.reduce((acc, skill) => {
        if (!acc[skill.category]) {
            acc[skill.category] = [];
        }
        acc[skill.category].push(skill);
        return acc;
    }, {});

    container.innerHTML = Object.entries(skillsByCategory).map(([category, categorySkills]) => `
        <div class="skill-category">
            <h3>${category}</h3>
            <div class="skills-list">
                ${categorySkills.map(skill => `
                    <div class="skill-item">
                        <span class="skill-name">${skill.name}</span>
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');
}

// Render education
function renderEducation(education) {
    const container = document.getElementById('education-container');
    if (!container || !education) return;

    container.innerHTML = education.map(edu => `
        <div class="education-item">
            <div class="education-year">${edu.year}</div>
            <div class="education-content">
                <h3>${edu.degree}</h3>
                <p class="institution">${edu.institution}</p>
                ${edu.percentage ? `<div class="percentage">${edu.percentage}</div>` : ''}
            </div>
        </div>
    `).join('');
}

// Render certifications
function renderCertifications(certifications) {
    const container = document.getElementById('certifications-container');
    if (!container || !certifications) return;

    container.innerHTML = certifications.map(cert => `
        <div class="certification-card">
            <div class="cert-icon">
                <i class="fas fa-certificate"></i>
            </div>
            <div class="cert-content">
                <h3>${cert.title}</h3>
                <p class="cert-issuer">${cert.issuer}</p>
                ${cert.percentage ? `<div class="cert-score">Score: ${cert.percentage}</div>` : ''}
                ${cert.date_range ? `<div class="cert-date">${cert.date_range}</div>` : ''}
            </div>
        </div>
    `).join('');
}

// Render internships
function renderInternships(internships) {
    const container = document.getElementById('internships-container');
    if (!container) return;

    if (!internships || internships.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-briefcase"></i>
                <p>No internships added yet.</p>
            </div>
        `;
        return;
    }

    container.innerHTML = internships.map(internship => `
        <div class="internship-card">
            <div class="internship-header">
                <h3>${internship.position}</h3>
                <div class="company-info">
                    <span class="company">${internship.company}</span>
                    <span class="location">${internship.location}</span>
                </div>
                <div class="duration">${internship.duration}</div>
            </div>
            <div class="internship-content">
                <p class="internship-description">${internship.description}</p>
                ${internship.technologies ? `
                    <div class="internship-tech">
                        <h4>Technologies Used:</h4>
                        <div class="tech-tags">
                            ${internship.technologies.split(', ').map(tech => 
                                `<span class="tech-tag">${tech}</span>`
                            ).join('')}
                        </div>
                    </div>
                ` : ''}
            </div>
        </div>
    `).join('');
}

// Render contact information
function renderContact(contact) {
    const container = document.getElementById('contact-details');
    if (!container || !contact) return;

    container.innerHTML = `
        <div class="contact-item">
            <i class="fas fa-phone"></i>
            <span>${contact.phone}</span>
        </div>
        <div class="contact-item">
            <i class="fas fa-envelope"></i>
            <span>${contact.email}</span>
        </div>
        <div class="contact-item">
            <i class="fas fa-map-marker-alt"></i>
            <span>${contact.location}</span>
        </div>
        <div class="contact-item social-media">
            <span class="social-label">Connect with me:</span>
            <div class="social-icons-inline">
                <a href="https://www.instagram.com/dhara_ruparel16?igsh=emRwZTJyc2h6cnN3" class="social-icon-small instagram" title="Instagram" target="_blank">
                    <i class="fab fa-instagram"></i>
                </a>
                <a href="https://www.linkedin.com/in/dhara-ruparel/" class="social-icon-small linkedin" title="LinkedIn" target="_blank">
                    <i class="fab fa-linkedin"></i>
                </a>
                <a href="https://github.com/dhararuparel" class="social-icon-small github" title="GitHub" target="_blank">
                    <i class="fab fa-github"></i>
                </a>
            </div>
        </div>
    `;
}

// Update statistics
function updateStats(projects, internships, certifications) {
    const projectsCount = document.getElementById('projects-count');
    const internshipsCount = document.getElementById('internships-count');
    const certificationsCount = document.getElementById('certifications-count');

    if (projectsCount) projectsCount.textContent = projects ? projects.length : 0;
    if (internshipsCount) internshipsCount.textContent = internships ? internships.length : 0;
    if (certificationsCount) certificationsCount.textContent = certifications ? certifications.length : 0;
}

// Handle contact form submission
async function handleContactForm(e) {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        subject: formData.get('subject'),
        message: formData.get('message')
    };

    try {
        // You can implement contact form submission to your backend here
        console.log('Contact form data:', data);
        alert('Thank you for your message! I will get back to you soon.');
        e.target.reset();
    } catch (error) {
        console.error('Error sending message:', error);
        alert('Sorry, there was an error sending your message. Please try again.');
    }
}

// Fallback data if API is not available
function loadFallbackData() {
    // Static fallback data
    const fallbackProjects = [
        {
            title: "CAMERA MOTION SENSING PROJECT",
            duration: "6 months",
            team_size: "4 persons",
            description: "A smart surveillance system that detects and responds to motion using real-time camera sensing and Python-based automation.",
            role: "Member",
            technologies: "HTML, CSS, Flask, Python, PostgreSQL"
        },
        {
            title: "HAND GESTURE RECOGNITION SYSTEM",
            duration: "1 Month",
            team_size: "1 person",
            description: "A real-time hand gesture recognition system that detects and classifies 5 distinct hand gestures using computer vision and Media Pipe.",
            role: "Individual",
            technologies: "Python, OpenCV, Media Pipe"
        },
        {
            title: "EMOTION DETECTION FROM TEXT",
            duration: "3 weeks",
            team_size: "1 person",
            description: "A sentiment analysis project that classifies user emotions from textual input using a machine learning model trained on the Twitter Emotion Dataset.",
            role: "Individual",
            technologies: "Python, Scikit-learn, Pandas, NLTK, Streamlit"
        }
    ];

    const fallbackContact = {
        phone: "+91 6352732968",
        email: "dhararuparel16@gmail.com",
        location: "Gandhinagar"
    };

    renderProjects(fallbackProjects);
    renderContact(fallbackContact);
    updateStats(fallbackProjects, [], []);
}