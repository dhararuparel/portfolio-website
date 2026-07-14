from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from dotenv import load_dotenv
import requests
import os
import io

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB (allows video uploads)

# Render uses 'postgres://' but SQLAlchemy requires 'postgresql://'
db_url = os.getenv('DATABASE_URL', 'postgresql://postgres:dhara16@localhost/portfolio_db')
if db_url.startswith('postgres://'):
    db_url = db_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask-Mail configuration (Gmail SMTP)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')       # your Gmail address
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')       # Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

db = SQLAlchemy(app)
mail = Mail(app)

# Database Models
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    team_size = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    link_url = db.Column(db.String(500))
    link_label = db.Column(db.String(100))
    display_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    proficiency = db.Column(db.Integer, default=80)
    display_order = db.Column(db.Integer, default=0)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(200), nullable=False)
    institution = db.Column(db.String(200), nullable=False)
    year = db.Column(db.String(20), nullable=False)
    percentage = db.Column(db.String(10))
    display_order = db.Column(db.Integer, default=0)

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    issuer = db.Column(db.String(200), nullable=False)
    percentage = db.Column(db.String(10))
    date_range = db.Column(db.String(100))
    display_order = db.Column(db.Integer, default=0)

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(500))
    display_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    linkedin = db.Column(db.String(200))

class ResumeFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False, default='Dhara_Ruparel_Resume.pdf')
    content_type = db.Column(db.String(100), nullable=False, default='application/pdf')
    data = db.Column(db.LargeBinary, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class IntroVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False, default='intro_video.mp4')
    content_type = db.Column(db.String(100), nullable=False, default='video/mp4')
    data = db.Column(db.LargeBinary, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Routes
@app.route('/')
def index():
    projects = Project.query.order_by(Project.display_order, Project.id).all()
    skills = Skill.query.order_by(Skill.display_order, Skill.id).all()
    education = Education.query.order_by(Education.display_order, Education.id).all()
    certifications = Certification.query.order_by(Certification.display_order, Certification.id).all()
    internships = Internship.query.order_by(Internship.display_order, Internship.id).all()
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
    
    projects = Project.query.order_by(Project.display_order, Project.id).all()
    skills = Skill.query.order_by(Skill.display_order, Skill.id).all()
    education = Education.query.order_by(Education.display_order, Education.id).all()
    certifications = Certification.query.order_by(Certification.display_order, Certification.id).all()
    internships = Internship.query.order_by(Internship.display_order, Internship.id).all()
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
            duration=data.get('duration', ''),
            team_size=data.get('team_size', ''),
            role=data.get('role', ''),
            link_url=data.get('link_url', ''),
            link_label=data.get('link_label', '')
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
        'role': p.role,
        'link_url': p.link_url or '',
        'link_label': p.link_label or ''
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
            'role': project.role,
            'link_url': project.link_url or '',
            'link_label': project.link_label or ''
        })
    
    elif request.method == 'PUT':
        data = request.json
        project.title = data['title']
        project.description = data['description']
        project.technologies = data['technologies']
        project.duration = data.get('duration', project.duration or '')
        project.team_size = data.get('team_size', project.team_size or '')
        project.role = data.get('role', project.role or '')
        project.link_url = data.get('link_url', '')
        project.link_label = data.get('link_label', '')
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


# ── Reorder routes ────────────────────────────────────────────────────────────
def _reorder(model, items):
    """Generic helper: items = [{id, order}, ...]"""
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    for item in items:
        row = model.query.get(item['id'])
        if row:
            row.display_order = item['order']
    db.session.commit()
    return jsonify({'message': 'Order saved'})

@app.route('/api/projects/reorder', methods=['POST'])
def reorder_projects():
    return _reorder(Project, request.json)

@app.route('/api/skills/reorder', methods=['POST'])
def reorder_skills():
    return _reorder(Skill, request.json)

@app.route('/api/education/reorder', methods=['POST'])
def reorder_education():
    return _reorder(Education, request.json)

@app.route('/api/certifications/reorder', methods=['POST'])
def reorder_certifications():
    return _reorder(Certification, request.json)

@app.route('/api/internships/reorder', methods=['POST'])
def reorder_internships():
    return _reorder(Internship, request.json)
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/resume/download')
def download_resume():
    """Serve the resume PDF with forced download headers."""
    resume_blob = ResumeFile.query.order_by(ResumeFile.updated_at.desc(), ResumeFile.id.desc()).first()
    if resume_blob and resume_blob.data:
        return send_file(
            io.BytesIO(resume_blob.data),
            mimetype=resume_blob.content_type or 'application/pdf',
            as_attachment=True,
            download_name='Dhara_Ruparel_Resume.pdf'
        )

    # Backward compatibility for previously disk-based deployments.
    resume_path = os.path.join(app.root_path, 'static', 'Dhara_Ruparel_Resume.pdf')
    if not os.path.isfile(resume_path):
        return "Resume not found. Please upload it via the admin panel.", 404
    return send_file(
        resume_path,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='Dhara_Ruparel_Resume.pdf'
    )


@app.route('/resume/view')
def view_resume():
    """Serve the resume PDF inline for viewing in the browser."""
    resume_blob = ResumeFile.query.order_by(ResumeFile.updated_at.desc(), ResumeFile.id.desc()).first()
    if resume_blob and resume_blob.data:
        return send_file(
            io.BytesIO(resume_blob.data),
            mimetype=resume_blob.content_type or 'application/pdf',
            as_attachment=False
        )

    resume_path = os.path.join(app.root_path, 'static', 'Dhara_Ruparel_Resume.pdf')
    if not os.path.isfile(resume_path):
        return "Resume not found. Please upload it via the admin panel.", 404
    return send_file(
        resume_path,
        mimetype='application/pdf',
        as_attachment=False
    )


@app.route('/api/resume/upload', methods=['POST'])
def upload_resume():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    if 'resume' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Only allow PDF
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are allowed'}), 400

    try:
        pdf_bytes = file.read()
        if not pdf_bytes:
            return jsonify({'error': 'Uploaded file is empty'}), 400

        resume_blob = ResumeFile.query.first()
        if not resume_blob:
            resume_blob = ResumeFile(
                filename='Dhara_Ruparel_Resume.pdf',
                content_type='application/pdf',
                data=pdf_bytes
            )
            db.session.add(resume_blob)
        else:
            resume_blob.filename = 'Dhara_Ruparel_Resume.pdf'
            resume_blob.content_type = 'application/pdf'
            resume_blob.data = pdf_bytes
            resume_blob.updated_at = datetime.utcnow()

        db.session.commit()
        return jsonify({'message': 'Resume uploaded successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Could not save file: {str(e)}'}), 500


@app.errorhandler(413)
def file_too_large(_error):
    if request.path.startswith('/api/'):
        return jsonify({'error': 'File is too large. Maximum size is 100 MB.'}), 413
    return 'File is too large. Maximum size is 100 MB.', 413


# ── Intro Video Routes ────────────────────────────────────────────────────────

@app.route('/intro-video/stream')
def stream_intro_video():
    """Stream the intro video from DB; falls back to the static file."""
    import mimetypes
    video_blob = IntroVideo.query.order_by(IntroVideo.updated_at.desc(), IntroVideo.id.desc()).first()
    if video_blob and video_blob.data:
        return send_file(
            io.BytesIO(video_blob.data),
            mimetype=video_blob.content_type or 'video/mp4',
            as_attachment=False,
            download_name=video_blob.filename or 'intro_video.mp4'
        )
    # Fallback: serve from static folder
    static_path = os.path.join(app.root_path, 'static', 'videos', 'intro_video.mp4')
    if os.path.isfile(static_path):
        return send_file(static_path, mimetype='video/mp4')
    return 'Intro video not found. Please upload one via the admin panel.', 404


@app.route('/api/intro-video/upload', methods=['POST'])
def upload_intro_video():
    """Upload a new intro video from the admin panel."""
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    if 'intro_video' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['intro_video']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    allowed_extensions = ('.mp4', '.webm', '.ogg', '.mov')
    if not file.filename.lower().endswith(allowed_extensions):
        return jsonify({'error': 'Only video files (.mp4, .webm, .ogg, .mov) are allowed'}), 400

    try:
        video_bytes = file.read()
        if not video_bytes:
            return jsonify({'error': 'Uploaded file is empty'}), 400

        ext = file.filename.lower().rsplit('.', 1)[-1]
        mime_map = {'mp4': 'video/mp4', 'webm': 'video/webm', 'ogg': 'video/ogg', 'mov': 'video/quicktime'}
        content_type = mime_map.get(ext, 'video/mp4')

        video_blob = IntroVideo.query.first()
        if not video_blob:
            video_blob = IntroVideo(
                filename='intro_video.' + ext,
                content_type=content_type,
                data=video_bytes
            )
            db.session.add(video_blob)
        else:
            video_blob.filename = 'intro_video.' + ext
            video_blob.content_type = content_type
            video_blob.data = video_bytes
            video_blob.updated_at = datetime.utcnow()

        db.session.commit()
        return jsonify({'message': 'Intro video uploaded successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Could not save video: {str(e)}'}), 500


@app.route('/api/intro-video/status', methods=['GET'])
def intro_video_status():
    """Return upload status for the admin panel."""
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    video_blob = IntroVideo.query.order_by(IntroVideo.updated_at.desc(), IntroVideo.id.desc()).first()
    if video_blob and video_blob.data:
        last_updated = video_blob.updated_at.strftime('%d %b %Y, %H:%M') if video_blob.updated_at else None
        return jsonify({'exists': True, 'last_updated': last_updated, 'filename': video_blob.filename})

    # Check static fallback
    static_path = os.path.join(app.root_path, 'static', 'videos', 'intro_video.mp4')
    if os.path.isfile(static_path):
        return jsonify({'exists': True, 'last_updated': 'static file (no DB record)', 'filename': 'intro_video.mp4'})

    return jsonify({'exists': False, 'last_updated': None})
# ─────────────────────────────────────────────────────────────────────────────


@app.route('/api/resume/status', methods=['GET'])
def resume_status():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    resume_blob = ResumeFile.query.order_by(ResumeFile.updated_at.desc(), ResumeFile.id.desc()).first()
    if resume_blob and resume_blob.data:
        last_updated = resume_blob.updated_at.strftime('%d %b %Y, %H:%M') if resume_blob.updated_at else None
        return jsonify({'exists': True, 'last_updated': last_updated})

    # Backward compatibility for previously disk-based deployments.
    path = os.path.join(app.root_path, 'static', 'Dhara_Ruparel_Resume.pdf')
    exists = os.path.isfile(path)
    mtime = None
    if exists:
        import time
        mtime = time.strftime('%d %b %Y, %H:%M', time.localtime(os.path.getmtime(path)))
    return jsonify({'exists': exists, 'last_updated': mtime})


@app.route('/api/contact/send', methods=['POST'])
def send_contact_email():
    data = request.json
    name    = data.get('name', '').strip()
    sender  = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    body    = data.get('message', '').strip()

    if not all([name, sender, subject, body]):
        return jsonify({'error': 'All fields are required.'}), 400

    try:
        recipient = os.getenv('CONTACT_RECEIVER_EMAIL', os.getenv('MAIL_USERNAME'))
        msg = Message(
            subject=f"Portfolio Contact: {subject}",
            recipients=[recipient],
            reply_to=sender,
            body=f"Name: {name}\nEmail: {sender}\n\n{body}"
        )
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Admin.query.filter_by(username='admin').first():
            admin = Admin(username='admin', password_hash=generate_password_hash('Dhara1625'))
            db.session.add(admin)
            db.session.commit()
    app.run(debug=True)


# Auto-run on gunicorn startup (Render) - just create tables and admin
with app.app_context():
    try:
        db.create_all()
        if not Admin.query.filter_by(username='admin').first():
            db.session.add(Admin(username='admin', password_hash=generate_password_hash('Dhara1625')))
            db.session.commit()

        # Migrate: add display_order column if missing (SQLite / Postgres safe)
        from sqlalchemy import text, inspect as sa_inspect
        inspector = sa_inspect(db.engine)

        # Add link_url / link_label to project FIRST (before any model queries)
        proj_cols = [c['name'] for c in inspector.get_columns('project')]
        if 'link_url' not in proj_cols:
            db.session.execute(text("ALTER TABLE project ADD COLUMN link_url VARCHAR(500)"))
            db.session.commit()
        if 'link_label' not in proj_cols:
            db.session.execute(text("ALTER TABLE project ADD COLUMN link_label VARCHAR(100)"))
            db.session.commit()

        # Ensure IntroVideo table exists
        db.create_all()

        for model, table in [
            (Project, 'project'), (Skill, 'skill'),
            (Education, 'education'), (Certification, 'certification'),
            (Internship, 'internship'),
        ]:
            cols = [c['name'] for c in inspector.get_columns(table)]
            if 'display_order' not in cols:
                db.session.execute(text(f'ALTER TABLE "{table}" ADD COLUMN display_order INTEGER DEFAULT 0'))
                db.session.commit()
            # Back-fill zeros with sequential values so existing rows have a stable order
            rows = model.query.filter(model.display_order == 0).order_by(model.id).all()
            for i, row in enumerate(rows, start=1):
                row.display_order = i
        db.session.commit()
    except Exception as e:
        print(f"Startup DB init error: {e}")