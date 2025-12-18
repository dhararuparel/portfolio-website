"""
Generate static HTML version for GitHub Pages deployment
This creates a static portfolio without Flask backend
"""

import os
import shutil
from datetime import datetime

def create_static_portfolio():
    """Generate static HTML with current data"""
    
    # Sample data (replace with your actual data)
    projects_data = [
        {
            'title': 'CAMERA MOTION SENSING PROJECT',
            'description': 'A smart surveillance system that detects and responds to motion using real-time camera sensing and Python-based automation.',
            'technologies': 'HTML, CSS, Flask, Python, PostgreSQL',
            'duration': '6 months',
            'team_size': '4 persons',
            'role': 'Member'
        },
        {
            'title': 'HAND GESTURE RECOGNITION SYSTEM',
            'description': 'A real-time hand gesture recognition system that detects and classifies 5 distinct hand gestures using computer vision and Media Pipe.',
            'technologies': 'Python, OpenCV, Media Pipe',
            'duration': '1 Month',
            'team_size': '1 person',
            'role': 'Individual'
        },
        {
            'title': 'EMOTION DETECTION FROM TEXT',
            'description': 'A sentiment analysis project that classifies user emotions from textual input using a machine learning model trained on the Twitter Emotion Dataset.',
            'technologies': 'Python, Scikit-learn, Pandas, NLTK, Streamlit',
            'duration': '3 weeks',
            'team_size': '1 person',
            'role': 'Individual'
        }
    ]
    
    skills_data = {
        'Programming Languages': ['Python', 'Machine Learning', 'AI'],
        'Databases': ['PostgreSQL', 'SQL'],
        'Web Technologies': ['HTML', 'CSS', 'JavaScript'],
        'Web Frameworks': ['Flask', 'Django'],
        'Libraries & Frameworks': ['OpenCV', 'MediaPipe', 'Scikit-learn', 'Pandas', 'NLTK', 'Streamlit']
    }
    
    education_data = [
        {
            'degree': 'B.E.(COMPUTER) - KSV',
            'institution': 'KSV University',
            'year': '2022-2026',
            'percentage': '8.44'
        },
        {
            'degree': 'H.S.C - C.B.S.E',
            'institution': 'CBSE Board',
            'year': '2020-2022',
            'percentage': '87%'
        },
        {
            'degree': 'S.S.C - C.B.S.E',
            'institution': 'CBSE Board',
            'year': '2020',
            'percentage': '94.2%'
        }
    ]
    
    certifications_data = [
        {
            'title': 'NPTEL Certification on "Enhancing Soft Skills and Personality"',
            'issuer': 'NPTEL',
            'percentage': '77%'
        },
        {
            'title': 'NPTEL Certification on "Python for Data Science"',
            'issuer': 'NPTEL',
            'percentage': '68%'
        },
        {
            'title': '5 Days Hands-on Series on Laravel Framework and Wordpress CMS',
            'issuer': 'LDRP ITR',
            'date_range': '20/01/2025 to 24/01/2025'
        },
        {
            'title': 'Institute of Plasma Research Project Completion Certificate',
            'issuer': 'Institute of Plasma Research'
        },
        {
            'title': 'TCS iON Career Edge - Young Professional Program',
            'issuer': 'TCS iON'
        }
    ]
    
    contact_data = {
        'phone': '+91 6352732968',
        'email': 'dhararuparel16@gmail.com',
        'location': 'Gandhinagar'
    }
    
    # Generate HTML content
    html_content = generate_html(projects_data, skills_data, education_data, certifications_data, contact_data)
    
    # Create docs directory (GitHub Pages uses this)
    os.makedirs('docs', exist_ok=True)
    
    # Write index.html
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Copy static assets
    if os.path.exists('docs/static'):
        shutil.rmtree('docs/static')
    shutil.copytree('static', 'docs/static')
    
    print("✅ Static site generated in 'docs' folder")
    print("🚀 Ready for GitHub Pages deployment!")
    print("📁 Upload 'docs' folder contents or enable GitHub Pages from 'docs' folder")

def generate_html(projects, skills, education, certifications, contact):
    """Generate complete HTML with data"""
    
    return f"""<!DOCTYPE html>
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
                            <h3>0</h3>
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
                {generate_projects_html(projects)}
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills">
        <div class="container">
            <h2 class="section-title">Skills & Technologies</h2>
            <div class="skills-container">
                {generate_skills_html(skills)}
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="education">
        <div class="container">
            <h2 class="section-title">Education</h2>
            <div class="education-timeline">
                {generate_education_html(education)}
            </div>
        </div>
    </section>

    <!-- Certifications Section -->
    <section id="certifications" class="certifications">
        <div class="container">
            <h2 class="section-title">Certifications</h2>
            <div class="certifications-grid">
                {generate_certifications_html(certifications)}
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
                    
                    <div class="contact-details">
                        <div class="contact-item">
                            <i class="fas fa-phone"></i>
                            <span>{contact['phone']}</span>
                        </div>
                        <div class="contact-item">
                            <i class="fas fa-envelope"></i>
                            <span>{contact['email']}</span>
                        </div>
                        <div class="contact-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>{contact['location']}</span>
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
                    </div>
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

def generate_projects_html(projects):
    html = ""
    for project in projects:
        tech_tags = ""
        for tech in project['technologies'].split(', '):
            tech_tags += f'<span class="tech-tag">{tech}</span>'
        
        html += f"""
        <div class="project-card">
            <div class="project-header">
                <h3>{project['title']}</h3>
                <div class="project-meta">
                    <span class="duration">{project['duration']}</span>
                    <span class="team-size">Team: {project['team_size']}</span>
                </div>
            </div>
            <div class="project-content">
                <p class="project-description">{project['description']}</p>
                <div class="project-role">
                    <strong>Role:</strong> {project['role']}
                </div>
                <div class="project-tech">
                    <h4>Technologies Used:</h4>
                    <div class="tech-tags">
                        {tech_tags}
                    </div>
                </div>
            </div>
        </div>"""
    return html

def generate_skills_html(skills):
    html = ""
    for category, skill_list in skills.items():
        skill_items = ""
        for skill in skill_list:
            skill_items += f'<div class="skill-item"><span class="skill-name">{skill}</span></div>'
        
        html += f"""
        <div class="skill-category">
            <h3>{category}</h3>
            <div class="skills-list">
                {skill_items}
            </div>
        </div>"""
    return html

def generate_education_html(education):
    html = ""
    for edu in education:
        percentage_html = f'<div class="percentage">{edu["percentage"]}</div>' if edu.get("percentage") else ""
        html += f"""
        <div class="education-item">
            <div class="education-year">{edu['year']}</div>
            <div class="education-content">
                <h3>{edu['degree']}</h3>
                <p class="institution">{edu['institution']}</p>
                {percentage_html}
            </div>
        </div>"""
    return html

def generate_certifications_html(certifications):
    html = ""
    for cert in certifications:
        score_html = f'<div class="cert-score">Score: {cert["percentage"]}</div>' if cert.get("percentage") else ""
        date_html = f'<div class="cert-date">{cert["date_range"]}</div>' if cert.get("date_range") else ""
        
        html += f"""
        <div class="certification-card">
            <div class="cert-icon">
                <i class="fas fa-certificate"></i>
            </div>
            <div class="cert-content">
                <h3>{cert['title']}</h3>
                <p class="cert-issuer">{cert['issuer']}</p>
                {score_html}
                {date_html}
            </div>
        </div>"""
    return html

if __name__ == '__main__':
    create_static_portfolio()