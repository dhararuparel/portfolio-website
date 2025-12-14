from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dhara16@localhost/portfolio_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    team_size = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    proficiency = db.Column(db.Integer, default=80)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(200), nullable=False)
    institution = db.Column(db.String(200), nullable=False)
    year = db.Column(db.String(20), nullable=False)
    percentage = db.Column(db.String(10))

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    issuer = db.Column(db.String(200), nullable=False)
    percentage = db.Column(db.String(10))
    date_range = db.Column(db.String(100))

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    linkedin = db.Column(db.String(200))

# Routes
@app.route('/')
def index():
    projects = Project.query.all()
    skills = Skill.query.all()
    education = Education.query.all()
    certifications = Certification.query.all()
    internships = Internship.query.all()
    contact = Contact.query.first()
    return render_template('index.html', 
                         projects=projects, 
                         skills=skills, 
                         education=education, 
                         certifications=certifications,
                         internships=internships,
                         contact=contact)

@app.route('/admin')
def admin_login():
    if 'admin_logged_in' in session:
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    username = request.form['username']
    password = request.form['password']
    
    admin = Admin.query.filter_by(username=username).first()
    if admin and check_password_hash(admin.password_hash, password):
        session['admin_logged_in'] = True
        return redirect(url_for('admin_dashboard'))
    
    flash('Invalid credentials')
    return redirect(url_for('admin_login'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
    
    projects = Project.query.all()
    skills = Skill.query.all()
    education = Education.query.all()
    certifications = Certification.query.all()
    internships = Internship.query.all()
    contact = Contact.query.first()
    
    return render_template('admin_dashboard.html',
                         projects=projects,
                         skills=skills,
                         education=education,
                         certifications=certifications,
                         internships=internships,
                         contact=contact)

# API Routes for CRUD operations
@app.route('/api/projects', methods=['GET', 'POST'])
def api_projects():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.json
        project = Project(
            title=data['title'],
            description=data['description'],
            technologies=data['technologies'],
            duration=data['duration'],
            team_size=data['team_size'],
            role=data['role']
        )
        db.session.add(project)
        db.session.commit()
        return jsonify({'message': 'Project added successfully', 'id': project.id})
    
    projects = Project.query.all()
    return jsonify([{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'technologies': p.technologies,
        'duration': p.duration,
        'team_size': p.team_size,
        'role': p.role
    } for p in projects])

@app.route('/api/projects/<int:project_id>', methods=['GET', 'PUT', 'DELETE'])
def api_project(project_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    project = Project.query.get_or_404(project_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'technologies': project.technologies,
            'duration': project.duration,
            'team_size': project.team_size,
            'role': project.role
        })
    
    elif request.method == 'PUT':
        data = request.json
        project.title = data['title']
        project.description = data['description']
        project.technologies = data['technologies']
        project.duration = data['duration']
        project.team_size = data['team_size']
        project.role = data['role']
        db.session.commit()
        return jsonify({'message': 'Project updated successfully'})
    
    elif request.method == 'DELETE':
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully'})

@app.route('/api/skills', methods=['GET', 'POST'])
def api_skills():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.json
        skill = Skill(
            name=data['name'],
            category=data['category'],
            proficiency=80  # Default proficiency, not used in display
        )
        db.session.add(skill)
        db.session.commit()
        return jsonify({'message': 'Skill added successfully', 'id': skill.id})
    
    skills = Skill.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'category': s.category,
        'proficiency': s.proficiency
    } for s in skills])

@app.route('/api/skills/<int:skill_id>', methods=['GET', 'PUT', 'DELETE'])
def api_skill(skill_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    skill = Skill.query.get_or_404(skill_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': skill.id,
            'name': skill.name,
            'category': skill.category,
            'proficiency': skill.proficiency
        })
    
    elif request.method == 'PUT':
        data = request.json
        skill.name = data['name']
        skill.category = data['category']
        # Keep existing proficiency or set default, not used in display
        skill.proficiency = skill.proficiency or 80
        db.session.commit()
        return jsonify({'message': 'Skill updated successfully'})
    
    elif request.method == 'DELETE':
        db.session.delete(skill)
        db.session.commit()
        return jsonify({'message': 'Skill deleted successfully'})

@app.route('/api/education', methods=['GET', 'POST'])
def api_education():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.json
        education = Education(
            degree=data['degree'],
            institution=data['institution'],
            year=data['year'],
            percentage=data.get('percentage')
        )
        db.session.add(education)
        db.session.commit()
        return jsonify({'message': 'Education added successfully', 'id': education.id})
    
    education = Education.query.all()
    return jsonify([{
        'id': e.id,
        'degree': e.degree,
        'institution': e.institution,
        'year': e.year,
        'percentage': e.percentage
    } for e in education])

@app.route('/api/education/<int:education_id>', methods=['GET', 'PUT', 'DELETE'])
def api_education_item(education_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    education = Education.query.get_or_404(education_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': education.id,
            'degree': education.degree,
            'institution': education.institution,
            'year': education.year,
            'percentage': education.percentage
        })
    
    elif request.method == 'PUT':
        data = request.json
        education.degree = data['degree']
        education.institution = data['institution']
        education.year = data['year']
        education.percentage = data.get('percentage')
        db.session.commit()
        return jsonify({'message': 'Education updated successfully'})
    
    elif request.method == 'DELETE':
        db.session.delete(education)
        db.session.commit()
        return jsonify({'message': 'Education deleted successfully'})

@app.route('/api/certifications', methods=['GET', 'POST'])
def api_certifications():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.json
        certification = Certification(
            title=data['title'],
            issuer=data['issuer'],
            percentage=data.get('percentage'),
            date_range=data.get('date_range')
        )
        db.session.add(certification)
        db.session.commit()
        return jsonify({'message': 'Certification added successfully', 'id': certification.id})
    
    certifications = Certification.query.all()
    return jsonify([{
        'id': c.id,
        'title': c.title,
        'issuer': c.issuer,
        'percentage': c.percentage,
        'date_range': c.date_range
    } for c in certifications])

@app.route('/api/certifications/<int:cert_id>', methods=['GET', 'PUT', 'DELETE'])
def api_certification(cert_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    certification = Certification.query.get_or_404(cert_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': certification.id,
            'title': certification.title,
            'issuer': certification.issuer,
            'percentage': certification.percentage,
            'date_range': certification.date_range
        })
    
    elif request.method == 'PUT':
        data = request.json
        certification.title = data['title']
        certification.issuer = data['issuer']
        certification.percentage = data.get('percentage')
        certification.date_range = data.get('date_range')
        db.session.commit()
        return jsonify({'message': 'Certification updated successfully'})
    
    elif request.method == 'DELETE':
        db.session.delete(certification)
        db.session.commit()
        return jsonify({'message': 'Certification deleted successfully'})

@app.route('/api/contact', methods=['GET', 'POST', 'PUT'])
def api_contact():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.json
        contact = Contact(
            phone=data['phone'],
            email=data['email'],
            location=data['location'],
            linkedin=data.get('linkedin')
        )
        db.session.add(contact)
        db.session.commit()
        return jsonify({'message': 'Contact info added successfully', 'id': contact.id})
    
    elif request.method == 'PUT':
        contact = Contact.query.first()
        if not contact:
            return jsonify({'error': 'Contact info not found'}), 404
        
        data = request.json
        contact.phone = data['phone']
        contact.email = data['email']
        contact.location = data['location']
        contact.linkedin = data.get('linkedin')
        db.session.commit()
        return jsonify({'message': 'Contact info updated successfully'})
    
    contact = Contact.query.first()
    if contact:
        return jsonify({
            'id': contact.id,
            'phone': contact.phone,
            'email': contact.email,
            'location': contact.location,
            'linkedin': contact.linkedin
        })
    return jsonify({'message': 'No contact info found'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create default admin if not exists
        if not Admin.query.filter_by(username='admin').first():
            admin = Admin(username='admin', password_hash=generate_password_hash('admin123'))
            db.session.add(admin)
            db.session.commit()
    
    app.run(debug=True)

@app.route('/api/internships', methods=['GET', 'POST'])
def api_internships():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.json
        internship = Internship(
            company=data['company'],
            position=data['position'],
            duration=data['duration'],
            location=data['location'],
            description=data.get('description', ''),
            technologies=data.get('technologies', '')
        )
        db.session.add(internship)
        db.session.commit()
        return jsonify({'message': 'Internship added successfully', 'id': internship.id})
    
    internships = Internship.query.all()
    return jsonify([{
        'id': i.id,
        'company': i.company,
        'position': i.position,
        'duration': i.duration,
        'location': i.location,
        'description': i.description,
        'technologies': i.technologies
    } for i in internships])

@app.route('/api/internships/<int:internship_id>', methods=['GET', 'PUT', 'DELETE'])
def api_internship(internship_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    internship = Internship.query.get_or_404(internship_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': internship.id,
            'company': internship.company,
            'position': internship.position,
            'duration': internship.duration,
            'location': internship.location,
            'description': internship.description,
            'technologies': internship.technologies
        })
    
    elif request.method == 'PUT':
        data = request.json
        internship.company = data['company']
        internship.position = data['position']
        internship.duration = data['duration']
        internship.location = data['location']
        internship.description = data.get('description', '')
        internship.technologies = data.get('technologies', '')
        db.session.commit()
        return jsonify({'message': 'Internship updated successfully'})
    
    elif request.method == 'DELETE':
        db.session.delete(internship)
        db.session.commit()
        return jsonify({'message': 'Internship deleted successfully'})