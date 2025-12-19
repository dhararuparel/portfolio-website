"""
Create index.html in root directory for GitHub Pages
"""
import shutil
import os

def create_root_index():
    # Create the static HTML content
    html_content = """<!DOCTYPE html>
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
                            <h3>3</h3>
                            <p>Projects Completed</p>
                        </div>
                        <div class="stat">
                            <h3>0</h3>
                            <p>Internships</p>
                        </div>
                        <div class="stat">
                            <h3>5</h3>
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
                <div class="project-card">
                    <div class="project-header">
                        <h3>CAMERA MOTION SENSING PROJECT</h3>
                        <div class="project-meta">
                            <span class="duration">6 months</span>
                            <span class="team-size">Team: 4 persons</span>
                        </div>
                    </div>
                    <div class="project-content">
                        <p class="project-description">A smart surveillance system that detects and responds to motion using real-time camera sensing and Python-based automation.</p>
                        <div class="project-role">
                            <strong>Role:</strong> Member
                        </div>
                        <div class="project-tech">
                            <h4>Technologies Used:</h4>
                            <div class="tech-tags">
                                <span class="tech-tag">HTML</span>
                                <span class="tech-tag">CSS</span>
                                <span class="tech-tag">Flask</span>
                                <span class="tech-tag">Python</span>
                                <span class="tech-tag">PostgreSQL</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-header">
                        <h3>HAND GESTURE RECOGNITION SYSTEM</h3>
                        <div class="project-meta">
                            <span class="duration">1 Month</span>
                            <span class="team-size">Team: 1 person</span>
                        </div>
                    </div>
                    <div class="project-content">
                        <p class="project-description">A real-time hand gesture recognition system that detects and classifies 5 distinct hand gestures using computer vision and Media Pipe.</p>
                        <div class="project-role">
                            <strong>Role:</strong> Individual
                        </div>
                        <div class="project-tech">
                            <h4>Technologies Used:</h4>
                            <div class="tech-tags">
                                <span class="tech-tag">Python</span>
                                <span class="tech-tag">OpenCV</span>
                                <span class="tech-tag">Media Pipe</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-header">
                        <h3>EMOTION DETECTION FROM TEXT</h3>
                        <div class="project-meta">
                            <span class="duration">3 weeks</span>
                            <span class="team-size">Team: 1 person</span>
                        </div>
                    </div>
                    <div class="project-content">
                        <p class="project-description">A sentiment analysis project that classifies user emotions from textual input using a machine learning model trained on the Twitter Emotion Dataset.</p>
                        <div class="project-role">
                            <strong>Role:</strong> Individual
                        </div>
                        <div class="project-tech">
                            <h4>Technologies Used:</h4>
                            <div class="tech-tags">
                                <span class="tech-tag">Python</span>
                                <span class="tech-tag">Scikit-learn</span>
                                <span class="tech-tag">Pandas</span>
                                <span class="tech-tag">NLTK</span>
                                <span class="tech-tag">Streamlit</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills">
        <div class="container">
            <h2 class="section-title">Skills & Technologies</h2>
            <div class="skills-container">
                <div class="skill-category">
                    <h3>Programming Languages</h3>
                    <div class="skills-list">
                        <div class="skill-item"><span class="skill-name">Python</span></div>
                        <div class="skill-item"><span class="skill-name">Machine Learning</span></div>
                        <div class="skill-item"><span class="skill-name">AI</span></div>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3>Databases</h3>
                    <div class="skills-list">
                        <div class="skill-item"><span class="skill-name">PostgreSQL</span></div>
                        <div class="skill-item"><span class="skill-name">SQL</span></div>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3>Web Technologies</h3>
                    <div class="skills-list">
                        <div class="skill-item"><span class="skill-name">HTML</span></div>
                        <div class="skill-item"><span class="skill-name">CSS</span></div>
                        <div class="skill-item"><span class="skill-name">JavaScript</span></div>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3>Web Frameworks</h3>
                    <div class="skills-list">
                        <div class="skill-item"><span class="skill-name">Flask</span></div>
                        <div class="skill-item"><span class="skill-name">Django</span></div>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3>Libraries & Frameworks</h3>
                    <div class="skills-list">
                        <div class="skill-item"><span class="skill-name">OpenCV</span></div>
                        <div class="skill-item"><span class="skill-name">MediaPipe</span></div>
                        <div class="skill-item"><span class="skill-name">Scikit-learn</span></div>
                        <div class="skill-item"><span class="skill-name">Pandas</span></div>
                        <div class="skill-item"><span class="skill-name">NLTK</span></div>
                        <div class="skill-item"><span class="skill-name">Streamlit</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="education">
        <div class="container">
            <h2 class="section-title">Education</h2>
            <div class="education-timeline">
                <div class="education-item">
                    <div class="education-year">2022-2026</div>
                    <div class="education-content">
                        <h3>B.E.(COMPUTER) - KSV</h3>
                        <p class="institution">KSV University</p>
                        <div class="percentage">8.44</div>
                    </div>
                </div>
                
                <div class="education-item">
                    <div class="education-year">2020-2022</div>
                    <div class="education-content">
                        <h3>H.S.C - C.B.S.E</h3>
                        <p class="institution">CBSE Board</p>
                        <div class="percentage">87%</div>
                    </div>
                </div>
                
                <div class="education-item">
                    <div class="education-year">2020</div>
                    <div class="education-content">
                        <h3>S.S.C - C.B.S.E</h3>
                        <p class="institution">CBSE Board</p>
                        <div class="percentage">94.2%</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Certifications Section -->
    <section id="certifications" class="certifications">
        <div class="container">
            <h2 class="section-title">Certifications</h2>
            <div class="certifications-grid">
                <div class="certification-card">
                    <div class="cert-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <div class="cert-content">
                        <h3>NPTEL Certification on "Enhancing Soft Skills and Personality"</h3>
                        <p class="cert-issuer">NPTEL</p>
                        <div class="cert-score">Score: 77%</div>
                    </div>
                </div>
                
                <div class="certification-card">
                    <div class="cert-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <div class="cert-content">
                        <h3>NPTEL Certification on "Python for Data Science"</h3>
                        <p class="cert-issuer">NPTEL</p>
                        <div class="cert-score">Score: 68%</div>
                    </div>
                </div>
                
                <div class="certification-card">
                    <div class="cert-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <div class="cert-content">
                        <h3>5 Days Hands-on Series on Laravel Framework and Wordpress CMS</h3>
                        <p class="cert-issuer">LDRP ITR</p>
                        <div class="cert-date">20/01/2025 to 24/01/2025</div>
                    </div>
                </div>
                
                <div class="certification-card">
                    <div class="cert-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <div class="cert-content">
                        <h3>Institute of Plasma Research Project Completion Certificate</h3>
                        <p class="cert-issuer">Institute of Plasma Research</p>
                    </div>
                </div>
                
                <div class="certification-card">
                    <div class="cert-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <div class="cert-content">
                        <h3>TCS iON Career Edge - Young Professional Program</h3>
                        <p class="cert-issuer">TCS iON</p>
                    </div>
                </div>
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
                            <span>+91 6352732968</span>
                        </div>
                        <div class="contact-item">
                            <i class="fas fa-envelope"></i>
                            <span>dhararuparel16@gmail.com</span>
                        </div>
                        <div class="contact-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>Gandhinagar</span>
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
    
    # Write index.html to root directory
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Created index.html in root directory")
    print("🚀 Ready for GitHub Pages deployment!")

if __name__ == '__main__':
    create_root_index()