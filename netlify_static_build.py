"""
Script to generate static HTML version for Netlify deployment
This creates a static version without Flask backend or admin panel
"""

from app import app, db, Project, Skill, Education, Certification, Contact
from flask import render_template
import os

def generate_static_site():
    with app.app_context():
        # Get all data from database
        projects = Project.query.all()
        skills = Skill.query.all()
        education = Education.query.all()
        certifications = Certification.query.all()
        internships = []  # Empty since we can't query without running server
        contact = Contact.query.first()
        
        # Render the template with data
        html_content = render_template('index.html',
                                     projects=projects,
                                     skills=skills,
                                     education=education,
                                     certifications=certifications,
                                     internships=internships,
                                     contact=contact)
        
        # Create dist directory for Netlify
        os.makedirs('dist', exist_ok=True)
        
        # Write static HTML file
        with open('dist/index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Copy static assets
        import shutil
        if os.path.exists('dist/static'):
            shutil.rmtree('dist/static')
        shutil.copytree('static', 'dist/static')
        
        print("Static site generated in 'dist' folder")
        print("Upload 'dist' folder contents to Netlify")

if __name__ == '__main__':
    generate_static_site()