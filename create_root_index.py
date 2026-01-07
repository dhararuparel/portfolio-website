"""
Create index.html in root directory for GitHub Pages with actual database data
"""
import shutil
import os
from app import app, Project, Skill, Education, Certification, Internship, Contact

def create_root_index():
    # Get data from database
    with app.app_context():
        projects = Project.query.all()
        skills = Skill.query.all()
        education = Education.query.all()
        certifications = Certification.query.all()
        internships = Internship.query.all()
        contact = Contact.query.first()
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)
    
    # Generate projects HTML
    projects_html = ""
    for project in projects:
        tech_tags = ""
        for tech in project.technologies.split(', '):
            tech_tags += f'<span class="tech-tag">{tech}</span>\n                                '
        
        projects_html += f"""
                <div class="project-card">
                    <div class="project-header">
                        <h3>{project.title}</h3>
                        <div class="project-meta">
                            <span class="duration">{project.duration}</span>
                            <span class="team-size">Team: {project.team_size}</span>
                        </div>
                    </div>
                    <div class="project-content">
                        <p class="project-description">{project.description}</p>
                        <div class="project-role">
                            <strong>Role:</strong> {project.role}
                        </div>
                        <div class="project-tech">
                            <h4>Technologies Used:</h4>
                            <div class="tech-tags">
                                {tech_tags}
                            </div>
                        </div>
                    </div>
                </div>
                """
    
    # Generate skills HTML
    skills_html = ""
    for category, category_skills in skill_categories.items():
        skill_items = ""
        for skill in category_skills:
            skill_items += f'<div class="skill-item"><span class="skill-name">{skill.name}</span></div>\n                        '
        
        skills_html += f"""
            <div class="skill-category">
                <h3>{category}</h3>
                <div class="skills-list">
                    {skill_items}
                </div>
            </div>
            """
    
    # Generate education HTML
    education_html = ""
    for edu in education:
        percentage_html = f'<div class="percentage">{edu.percentage}</div>' if edu.percentage else ''
        education_html += f"""
                <div class="education-item">
                    <div class="education-year">{edu.year}</div>
                    <div class="education-content">
                        <h3>{edu.degree}</h3>
                        <p class="institution">{edu.institution}</p>
                        {percentage_html}
                    </div>
                </div>
                """
    
    # Generate certifications HTML
    certifications_html = ""
    for cert in certifications:
        score_html = f'<div class="cert-score">Score: {cert.percentage}</div>' if cert.percentage else ''
        date_html = f'<div class="cert-date">{cert.date_range}</div>' if cert.date_range else ''
        
        certifications_html += f"""
                <div class="certification-card">
                    <div class="cert-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <div class="cert-content">
                        <h3>{cert.title}</h3>
                        <p class="cert-issuer">{cert.issuer}</p>
                        {score_html}
                        {date_html}
                    </div>
                </div>
                """
    
    # Generate internships HTML
    internships_html = ""
    for internship in internships:
        tech_html = ""
        if internship.technologies:
            tech_tags = ""
            for tech in internship.technologies.split(', '):
                tech_tags += f'<span class="tech-tag">{tech}</span>\n                            '
            tech_html = f"""
                    <div class="internship-tech">
                        <h4>Technologies Used:</h4>
                        <div class="tech-tags">
                            {tech_tags}
                        </div>
                    </div>"""
        
        internships_html += f"""
                <div class="internship-card">
                    <div class="internship-header">
                        <h3>{internship.position}</h3>
                        <div class="company-info">
                            <span class="company">{internship.company}</span>
                            <span class="location">{internship.location}</span>
                        </div>
                        <div class="duration">{internship.duration}</div>
                    </div>
                    <div class="internship-content">
                        <p class="internship-description">{internship.description}</p>
                        {tech_html}
                    </div>
                </div>
                """
    
    # Generate contact HTML
    contact_html = ""
    if contact:
        contact_html = f"""
                    <div class="contact-details">
                        <div class="contact-item">
                            <i class="fas fa-phone"></i>
                            <span>{contact.phone}</span>
                        </div>
                        <div class="contact-item">
                            <i class="fas fa-envelope"></i>
                            <span>{contact.email}</span>
                        </div>
                        <div class="contact-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>{contact.location}</span>
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
                    </div>"""
    
    # Create the static HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dhara Ruparel - Portfolio</title>
    <link rel="stylesheet" href="static/css/style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h2>DHARA RUPAREL</h2>
            </div>
            <div class="nav-menu">
                <a href="#home" class="nav-link">Home</a>
                <a href="#about" class="nav-link">About</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#skills" class="nav-link">Skills</a>
                <a href="#internships" class="nav-link">Internships</a>
                <a href="#education" class="nav-link">Education</a>
                <a href="#certifications" class="nav-link">Certifications</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-container">
            <div class="hero-content">
                <h1 class="hero-title">
                    Hii, I'm <span class="highlight">Dhara Ruparel</span>
                </h1>
                <p class="hero-subtitle">Computer Science Student & AI Enthusiast</p>
                <p class="hero-description">
                    Passionate about Python, Machine Learning, and creating innovative solutions 
                    through technology. Currently pursuing B.E. in Computer Science.
                </p>
                <div class="hero-buttons">
                    <a href="#projects" class="btn btn-primary">View My Work</a>
                    <a href="#contact" class="btn btn-secondary">Get In Touch</a>
                </div>
            </div>
            <div class="hero-image">
                <div class="profile-card">
                    <div class="profile-avatar">
                        <img src="static/images/DHARA.jpg" alt="Dhara Ruparel" class="profile-image">
                    </div>
                    <div class="floating-elements">
                        <div class="floating-icon python"><i class="fab fa-python"></i></div>
                        <div class="floating-icon js"><i class="fab fa-js-square"></i></div>
                        <div class="floating-icon react"><i class="fab fa-react"></i></div>
                        <div class="floating-icon database"><i class="fas fa-database"></i></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-text">
                    <p>
                        I'm a dedicated Computer Science student with a passion for artificial intelligence, 
                        machine learning, and web development. My journey in technology has led me to work 
                        on various projects involving motion sensing, gesture recognition, and emotion detection.
                    </p>
                    <p>
                        With experience in Python, Flask, PostgreSQL, and modern web technologies, I enjoy 
                        creating solutions that bridge the gap between complex algorithms and user-friendly interfaces.
                    </p>
                </div>
                <div class="about-image">
                    <div class="about-stats">
                        <div class="stat">
                            <h3>{len(projects)}</h3>
                            <p>Projects Completed</p>
                        </div>
                        <div class="stat">
                            <h3>{len(internships)}</h3>
                            <p>Internships</p>
                        </div>
                        <div class="stat">
                            <h3>{len(certifications)}</h3>
                            <p>Certifications</p>
                        </div>
                    </div>
                    <div class="about-card">
                        <div class="languages">
                            <h4>Languages</h4>
                            <div class="language-list">
                                <span class="language-tag">English</span>
                                <span class="language-tag">Hindi</span>
                                <span class="language-tag">Gujarati</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <div class="container">
            <h2 class="section-title">Work Experience & Projects</h2>
            <div class="projects-grid">
            {projects_html}
        </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills">
        <div class="container">
            <h2 class="section-title">Skills & Technologies</h2>
            <div class="skills-container">
                {skills_html}
            </div>
        </div>
    </section>

    <!-- Internships Section -->
    <section id="internships" class="internships">
        <div class="container">
            <h2 class="section-title">Internships</h2>
            <div class="internships-grid">
                {internships_html}
            </div>
            {f'<div class="empty-state"><i class="fas fa-briefcase"></i><p>No internships added yet.</p></div>' if not internships else ''}
        </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="education">
        <div class="container">
            <h2 class="section-title">Education</h2>
            <div class="education-timeline">
                {education_html}
            </div>
        </div>
    </section>

    <!-- Certifications Section -->
    <section id="certifications" class="certifications">
        <div class="container">
            <h2 class="section-title">Certifications</h2>
            <div class="certifications-grid">
                {certifications_html}
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2 class="section-title">Get In Touch</h2>
            <div class="contact-content">
                <div class="contact-info">
                    <h3>Let's Connect</h3>
                    <p>I'm always open to discussing new opportunities, interesting projects, or just having a chat about technology.</p>
                    
                    {contact_html}
                </div>
                
                <div class="contact-form">
                    <form id="contactForm">
                        <div class="form-group">
                            <input type="text" id="name" name="name" placeholder="Your Name" required>
                        </div>
                        <div class="form-group">
                            <input type="email" id="email" name="email" placeholder="Your Email" required>
                        </div>
                        <div class="form-group">
                            <input type="text" id="subject" name="subject" placeholder="Subject" required>
                        </div>
                        <div class="form-group">
                            <textarea id="message" name="message" placeholder="Your Message" rows="5" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p>&copy; 2025 Dhara Ruparel. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="static/js/script.js"></script>
</body>
</html>"""
    
    # Write index.html to root directory
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Created index.html in root directory")
    print("🚀 Ready for GitHub Pages deployment!")

if __name__ == '__main__':
    create_root_index()