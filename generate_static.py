"""
Generate static HTML version for GitHub Pages deployment
This renders the templates dynamically from the Flask app database
"""

import os
import shutil
import io
from app import app, db, Project, Skill, Education, Certification, Internship, Contact, ResumeFile

def create_static_portfolio():
    """Generate static HTML with current data from database"""
    print("Generating static site from local database and templates...")
    
    with app.app_context():
        # 1. Fetch resume from database and save to static/Dhara_Ruparel_Resume.pdf
        resume = ResumeFile.query.order_by(ResumeFile.updated_at.desc(), ResumeFile.id.desc()).first()
        if resume and resume.data:
            os.makedirs('static', exist_ok=True)
            resume_path = os.path.join('static', 'Dhara_Ruparel_Resume.pdf')
            with open(resume_path, 'wb') as f:
                f.write(resume.data)
            print(f"Saved resume PDF from database to {resume_path}")
        else:
            print("Warning: No resume found in database.")

        # 2. Use test client to render home page
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code != 200:
                print(f"Error rendering homepage: {response.status_code}")
                return
            html = response.get_data(as_text=True)

            # Post-process paths to make them relative for GitHub Pages
            html = html.replace('href="/static/', 'href="static/')
            html = html.replace('src="/static/', 'src="static/')
            html = html.replace("href='/static/", "href='static/")
            html = html.replace("src='/static/", "src='static/")
            html = html.replace('href="/resume/download"', 'href="static/Dhara_Ruparel_Resume.pdf"')
            html = html.replace("href='/resume/download'", "href='static/Dhara_Ruparel_Resume.pdf'")
            html = html.replace('href="/resume/view"', 'href="static/Dhara_Ruparel_Resume.pdf"')
            html = html.replace("href='/resume/view'", "href='static/Dhara_Ruparel_Resume.pdf'")
            
            # Ensure docs folder exists
            os.makedirs('docs', exist_ok=True)
            
            # Write to docs/index.html and index.html at root
            with open('docs/index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print("Successfully wrote docs/index.html and index.html")

        # 3. Copy static folder to docs/static
        if os.path.exists('docs/static'):
            shutil.rmtree('docs/static')
        shutil.copytree('static', 'docs/static')
        print("Successfully copied static assets to docs/static")

if __name__ == '__main__':
    create_static_portfolio()