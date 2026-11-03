"""
Generate static HTML version for GitHub Pages deployment
This renders the templates dynamically from the Flask app database
"""

import os
import shutil
import re
from datetime import datetime
from app import app, db, ResumeFile, sync_static_files

def create_static_portfolio():
    """Generate static HTML with current data from database"""
    print("Generating static site from local database and templates...")
    
    with app.app_context():
        # Ensure static resume is up to date
        resume = ResumeFile.query.order_by(ResumeFile.updated_at.desc(), ResumeFile.id.desc()).first()
        if resume and resume.data:
            os.makedirs('static', exist_ok=True)
            resume_path = os.path.join('static', 'Dhara_Ruparel_Resume.pdf')
            with open(resume_path, 'wb') as f:
                f.write(resume.data)
            print(f"Saved resume PDF from database to {resume_path}")

        # Synchronize root index.html and docs/index.html
        sync_static_files()

        # Copy static folder to docs/static
        os.makedirs('docs', exist_ok=True)
        if os.path.exists('docs/static'):
            shutil.rmtree('docs/static')
        shutil.copytree('static', 'docs/static')
        print("Successfully synchronized docs/static assets.")

if __name__ == '__main__':
    create_static_portfolio()
