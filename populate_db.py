from app import app, db, Project, Skill, Education, Certification, Contact, Admin
from werkzeug.security import generate_password_hash

def populate_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create admin user
        admin = Admin(
            username='admin',
            password_hash=generate_password_hash('admin123')
        )
        db.session.add(admin)
        
        # Add Projects from resume
        projects = [
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
                'description': 'A real-time hand gesture recognition system that detects and classifies 5 distinct hand gestures — open palm, thumbs up, OK sign, closed fist, and peace sign — using computer vision and Media Pipe, enabling intuitive and hands-free control of basic computer interactions.',
                'technologies': 'Python, OpenCV, Media Pipe',
                'duration': '1 Month',
                'team_size': '1 person',
                'role': 'Individual'
            },
            {
                'title': 'EMOTION DETECTION FROM TEXT',
                'description': 'A sentiment analysis project that classifies user emotions from textual input using a machine learning model trained on the Twitter Emotion Dataset, deployed through an interactive web interface.',
                'technologies': 'Python, Scikit-learn, Pandas, NLTK, Streamlit',
                'duration': '3 weeks',
                'team_size': '1 person',
                'role': 'Individual'
            }
        ]
        
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)
        
        # Add Skills from resume
        skills = [
            {'name': 'Python', 'category': 'Programming Languages', 'proficiency': 90},
            {'name': 'Machine Learning', 'category': 'Programming Languages', 'proficiency': 85},
            {'name': 'AI', 'category': 'Programming Languages', 'proficiency': 80},
            {'name': 'PostgreSQL', 'category': 'Databases', 'proficiency': 85},
            {'name': 'OpenCV', 'category': 'Libraries & Frameworks', 'proficiency': 80},
            {'name': 'MediaPipe', 'category': 'Libraries & Frameworks', 'proficiency': 75},
            {'name': 'Flask', 'category': 'Web Frameworks', 'proficiency': 85},
            {'name': 'Django', 'category': 'Web Frameworks', 'proficiency': 75},
            {'name': 'HTML', 'category': 'Web Technologies', 'proficiency': 90},
            {'name': 'CSS', 'category': 'Web Technologies', 'proficiency': 85},
            {'name': 'JavaScript', 'category': 'Web Technologies', 'proficiency': 80},
            {'name': 'Scikit-learn', 'category': 'Libraries & Frameworks', 'proficiency': 85},
            {'name': 'Pandas', 'category': 'Libraries & Frameworks', 'proficiency': 90},
            {'name': 'NLTK', 'category': 'Libraries & Frameworks', 'proficiency': 80},
            {'name': 'Streamlit', 'category': 'Libraries & Frameworks', 'proficiency': 75}
        ]
        
        for skill_data in skills:
            skill = Skill(**skill_data)
            db.session.add(skill)
        
        # Add Education from resume
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
        
        for edu_data in education_data:
            education = Education(**edu_data)
            db.session.add(education)
        
        # Add Certifications from resume
        certifications_data = [
            {
                'title': 'NPTEL Certification on "Enhancing Soft Skills and Personality"',
                'issuer': 'NPTEL',
                'percentage': '77%',
                'date_range': None
            },
            {
                'title': 'NPTEL Certification on "Python for Data Science"',
                'issuer': 'NPTEL',
                'percentage': '68%',
                'date_range': None
            },
            {
                'title': '5 Days Hands-on Series on Laravel Framework and Wordpress CMS',
                'issuer': 'LDRP ITR',
                'percentage': None,
                'date_range': '20/01/2025 to 24/01/2025'
            },
            {
                'title': 'Institute of Plasma Research Project Completion Certificate',
                'issuer': 'Institute of Plasma Research',
                'percentage': None,
                'date_range': None
            },
            {
                'title': 'TCS iON Career Edge - Young Professional Program',
                'issuer': 'TCS iON',
                'percentage': None,
                'date_range': None
            }
        ]
        
        for cert_data in certifications_data:
            certification = Certification(**cert_data)
            db.session.add(certification)
        
        # Add Contact Information from resume
        contact = Contact(
            phone='+91 6352732968',
            email='dhara.ruparel16@gmail.com',
            location='Gandhinagar',
            linkedin='https://www.linkedin.com/in/dhara-ruparel/'
        )
        db.session.add(contact)
        
        # Commit all changes
        db.session.commit()
        print("Database populated successfully!")
        print("Admin credentials: username='admin', password='admin123'")

if __name__ == '__main__':
    populate_database()