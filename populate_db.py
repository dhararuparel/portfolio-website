from app import app, db, Project, Skill, Education, Certification, Contact, Admin, EngineeringSnapshot, ResumeFile, Internship
from werkzeug.security import generate_password_hash
import os

def populate_database():
    with app.app_context():
        # Create tables if they don't exist (don't drop existing data)
        db.create_all()
        
        # Create admin user (only if it doesn't exist)
        if not Admin.query.filter_by(username='admin').first():
            admin = Admin(
                username='admin',
                password_hash=generate_password_hash('admin123')
            )
            db.session.add(admin)
            print("Created admin user")
        else:
            print("Admin user already exists")
        
        # Check if data already exists
        existing_projects_count = Project.query.count()
        print(f"Existing projects in database: {existing_projects_count}")
        
        # Add Projects from resume (only if they don't exist)
        projects = [
            {
                'title': 'LEXARA AI - LLM-POWERED RAG PLATFORM',
                'description': 'Developed an advanced RAG platform enabling conversational knowledge retrieval from documents and web sources using hybrid semantic search, AI-powered responses, multi-format content ingestion, team collaboration features, and analytics.',
                'technologies': 'Python, Flask, FAISS, Gemini 2.5 Flash, Supabase, Render',
                'duration': '3 months',
                'team_size': '1 person',
                'role': 'Lead Developer',
                'link_url': 'https://lexara-ai.onrender.com/',
                'link_label': 'Live Demo'
            },
            {
                'title': 'CAMERA MOTION SENSING SYSTEM',
                'description': 'A smart surveillance system that detects and responds to motion using real-time camera sensing and Python-based automation.',
                'technologies': 'HTML, CSS, Flask, Python, PostgreSQL',
                'duration': '6 months',
                'team_size': '4 persons',
                'role': 'Member',
                'link_url': 'https://github.com/dhararuparel/Camera-Motion-Sensing-Project.git',
                'link_label': 'GitHub'
            },
            {
                'title': 'EMOTION DETECTION FROM TEXT',
                'description': 'A sentiment analysis project that classifies user emotions from textual input using a machine learning model trained on the Twitter Emotion Dataset, deployed through an interactive web interface.',
                'technologies': 'Python, Scikit-learn, Pandas, NLTK, Streamlit',
                'duration': '3 weeks',
                'team_size': '1 person',
                'role': 'Individual',
                'link_url': 'https://github.com/dhararuparel/emo_sense',
                'link_label': 'GitHub'
            },
            {
                'title': 'AI CONTENT FACTORY',
                'description': 'Developed an AI-powered workflow to generate content ideas and automate storage and notifications.',
                'technologies': 'n8n, Google Gemini, Google Sheets API, Gmail API, Automation, Low-Code',
                'duration': '2 weeks',
                'team_size': '1 person',
                'role': 'Individual',
                'link_url': '',
                'link_label': ''
            },
            {
                'title': 'HAND GESTURE RECOGNITION SYSTEM',
                'description': 'A real-time hand gesture recognition system that detects and classifies 5 distinct hand gestures — open palm, thumbs up, OK sign, closed fist, and peace sign — using computer vision and Media Pipe, enabling intuitive and hands-free control of basic computer interactions.',
                'technologies': 'Python, OpenCV, Media Pipe',
                'duration': '1 Month',
                'team_size': '1 person',
                'role': 'Individual',
                'link_url': 'https://github.com/dhararuparel/Hand-Gesture-Project.git',
                'link_label': 'GitHub'
            },
            {
                'title': 'HOUSE PRICE PREDICTION SYSTEM',
                'description': 'ML-powered real estate platform for predicting property prices across major Indian cities (Mumbai, Delhi, Bangalore, Chennai, Hyderabad, Kolkata) with interactive web interface.',
                'technologies': 'Python, Machine Learning, Scikit-learn, Flask, HTML, CSS, JavaScript, PostgreSQL, REST APIs, Pickle',
                'duration': '1 month',
                'team_size': '1 person',
                'role': 'Individual',
                'link_url': 'https://github.com/dhararuparel/house-price-prediction.git',
                'link_label': 'GitHub'
            }
        ]
        
        # Only add projects if they don't already exist; sync order
        for i, project_data in enumerate(projects, 1):
            existing = Project.query.filter_by(title=project_data['title']).first()
            if not existing:
                project = Project(display_order=i, **project_data)
                db.session.add(project)
                print(f"Added project: {project_data['title']}")
            else:
                existing.display_order = i
                print(f"Project already exists: {project_data['title']}")
        
        # Add Skills from resume
        skills = [
            {'name': 'Python', 'category': 'Programming Languages', 'proficiency': 90},
            {'name': 'Machine Learning', 'category': 'AI & Machine Learning', 'proficiency': 85},
            {'name': 'AI', 'category': 'AI & Machine Learning', 'proficiency': 85},
            {'name': 'PostgreSQL', 'category': 'Databases & Backend Services', 'proficiency': 80},
            {'name': 'OpenCV', 'category': 'Libraries & Frameworks', 'proficiency': 80},
            {'name': 'MediaPipe', 'category': 'Libraries & Frameworks', 'proficiency': 75},
            {'name': 'Flask', 'category': 'Web Frameworks', 'proficiency': 85},
            {'name': 'Django', 'category': 'Web Frameworks', 'proficiency': 75},
            {'name': 'HTML', 'category': 'Web Technologies', 'proficiency': 90},
            {'name': 'CSS', 'category': 'Web Technologies', 'proficiency': 85},
            {'name': 'JavaScript', 'category': 'Web Technologies', 'proficiency': 75},
            {'name': 'Scikit-learn', 'category': 'Libraries & Frameworks', 'proficiency': 80},
            {'name': 'Pandas', 'category': 'Libraries & Frameworks', 'proficiency': 85},
            {'name': 'NLTK', 'category': 'Libraries & Frameworks', 'proficiency': 75},
            {'name': 'Streamlit', 'category': 'Libraries & Frameworks', 'proficiency': 80},
            {'name': 'MySQL', 'category': 'Databases & Backend Services', 'proficiency': 75},
            {'name': 'SQL Server', 'category': 'Databases', 'proficiency': 70},
            {'name': 'PyTorch', 'category': 'Libraries & Frameworks', 'proficiency': 75},
            {'name': 'n8n', 'category': 'AI Tools', 'proficiency': 80},
            {'name': 'Supabase', 'category': 'Databases & Backend Services', 'proficiency': 80},
            {'name': 'ChatGPT', 'category': 'Developer & AI Tools', 'proficiency': 90},
            {'name': 'GitHub Copilot', 'category': 'Developer & AI Tools', 'proficiency': 85},
            {'name': 'Kiro', 'category': 'Developer & AI Tools', 'proficiency': 75},
            {'name': 'Gemini', 'category': 'Developer & AI Tools', 'proficiency': 85},
            {'name': 'Midjourney', 'category': 'Developer & AI Tools', 'proficiency': 75},
            {'name': 'Cursor', 'category': 'Developer & AI Tools', 'proficiency': 85},
            {'name': 'Git', 'category': 'Version Control & Deployment', 'proficiency': 85},
            {'name': 'GitHub', 'category': 'Version Control & Deployment', 'proficiency': 85}
        ]
        
        for i, skill_data in enumerate(skills, 1):
            existing = Skill.query.filter_by(name=skill_data['name']).first()
            if not existing:
                skill = Skill(display_order=i, **skill_data)
                db.session.add(skill)
                print(f"Added skill: {skill_data['name']}")
            else:
                existing.display_order = i
                print(f"Skill already exists: {skill_data['name']}")
        
        # Add Education from resume
        education = [
            {
                'degree': 'Bachelor of Engineering in Computer Engineering',
                'institution': 'LDRP Institute of Technology and Research, Gandhinagar',
                'year': '2022 - 2026',
                'percentage': '8.55 CGPA'
            },
            {
                'degree': 'Higher Secondary Certificate (HSC)',
                'institution': 'St. Xavier\'s High School, Jamnagar',
                'year': '2020 - 2022',
                'percentage': '78%'
            },
            {
                'degree': 'Secondary School Certificate (SSC)',
                'institution': 'St. Xavier\'s High School, Jamnagar',
                'year': '2019 - 2020',
                'percentage': '73%'
            }
        ]
        
        for i, edu_data in enumerate(education, 1):
            existing = Education.query.filter_by(degree=edu_data['degree']).first()
            if not existing:
                edu = Education(display_order=i, **edu_data)
                db.session.add(edu)
                print(f"Added education: {edu_data['degree']}")
            else:
                existing.display_order = i
                print(f"Education already exists: {edu_data['degree']}")
        
        # Add Certifications from resume
        certifications = [
            {
                'title': 'Python for Data Science',
                'issuer': 'NPTEL (IIT Madras)',
                'percentage': '70% (Elite Certificate)',
                'date_range': 'Jan 2024 - Feb 2024'
            },
            {
                'title': 'TCS iON Career Edge - Young Professional',
                'issuer': 'TCS',
                'percentage': 'Completed',
                'date_range': 'Dec 2024 - Jan 2025'
            }
        ]
        
        for i, cert_data in enumerate(certifications, 1):
            existing = Certification.query.filter_by(title=cert_data['title']).first()
            if not existing:
                cert = Certification(display_order=i, **cert_data)
                db.session.add(cert)
                print(f"Added certification: {cert_data['title']}")
            else:
                existing.display_order = i
                print(f"Certification already exists: {cert_data['title']}")
        
        # Add Internships (only if they don't exist)
        internships_data = [
            {
                'company': 'AirDawg Labs (Caudal AI Labs Pvt. Ltd.)',
                'position': 'AI Systems Evaluation Intern',
                'duration': '07/2026 - 10/2026',
                'location': 'Remote',
                'description': 'Developed and refined benchmark tasks for Terminal-Bench and Sentinel to evaluate AI agents on complex, real-world problem-solving scenarios. Designed and validated test cases, verification scripts, and evaluation criteria.',
                'technologies': 'Python, Terminal-Bench, Sentinel, AI Evaluation, LLM Benchmarking'
            },
            {
                'company': 'iTechbrains Pvt. Ltd.',
                'position': 'Python With Django',
                'duration': '1 Month',
                'location': 'Virtual',
                'description': 'Developed backend modules using Python and Django. Implemented CRUD operations and REST API functionality.',
                'technologies': 'Python, Django, PostgreSQL'
            },
            {
                'company': 'TatvaSoft Pvt. Ltd.',
                'position': 'Summer Internship',
                'duration': '15 Days',
                'location': 'Virtual',
                'description': 'Worked with database management and full-stack integration.',
                'technologies': 'PostgreSQL, .NET, Angular'
            }
        ]
        for i, intern_data in enumerate(internships_data, 1):
            existing = Internship.query.filter_by(company=intern_data['company'], position=intern_data['position']).first()
            if not existing:
                internship = Internship(display_order=i, **intern_data)
                db.session.add(internship)
                print(f"Added internship: {intern_data['position']} at {intern_data['company']}")
            else:
                existing.display_order = i
                print(f"Internship already exists: {intern_data['position']}")

        # Add Contact Information from resume (only if it doesn't exist)
        existing_contact = Contact.query.first()
        if not existing_contact:
            contact = Contact(
                phone='+91 6352732968',
                email='dhararuparel16@gmail.com',
                location='Gandhinagar',
                linkedin='https://www.linkedin.com/in/dhara-ruparel/'
            )
            db.session.add(contact)
            print("Added contact information")
        else:
            print("Contact information already exists")
        
        # Add Engineering Snapshot (only if it doesn't exist)
        existing_snapshot = EngineeringSnapshot.query.first()
        if not existing_snapshot:
            snapshot = EngineeringSnapshot(
                public_repos=15,
                ai_projects=6,
                apis_integrated=10,
                technologies_used=15,
                years_of_coding=3,
                total_commits=500,
                currently_building='GitScope AI',
                learning='Go + System Design',
                available_for='AI Engineer &amp; Backend Engineer',
                last_updated='Jul 2025'
            )
            db.session.add(snapshot)
            print("Added engineering snapshot")
        else:
            print("Engineering snapshot already exists")
        
        # Add or update ResumeFile from static file
        existing_resume = ResumeFile.query.first()
        resume_path = os.path.join(app.root_path, 'static', 'Dhara_Ruparel_Resume.pdf')
        if os.path.isfile(resume_path):
            with open(resume_path, 'rb') as f:
                resume_data = f.read()
            if resume_data:
                if not existing_resume:
                    db.session.add(ResumeFile(
                        filename='Dhara_Ruparel_Resume.pdf',
                        content_type='application/pdf',
                        data=resume_data
                    ))
                    print("Added resume from static file")
                elif existing_resume.data != resume_data and len(existing_resume.data) == 93252:
                    existing_resume.data = resume_data
                    print("Updated resume from latest static file")

        # Commit all changes
        db.session.commit()
        print("Database populated successfully!")
        print("Admin credentials: username='admin', password='admin123'")

        try:
            from app import sync_static_files
            sync_static_files()
            print("Static files automatically synchronized.")
        except Exception as sync_err:
            print(f"Static sync notice: {sync_err}")

if __name__ == '__main__':
    populate_database()
