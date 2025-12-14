# 🌟 Dhara Ruparel - Portfolio Website

A modern, fully functional portfolio website with a sleek dark theme and powerful admin panel for content management. Built with Flask, PostgreSQL, HTML, CSS, and JavaScript.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

## 🚀 Live Demo

- **Portfolio:** [View Live Portfolio](http://localhost:5000) *(when running locally)*
- **Admin Panel:** [Admin Dashboard](http://localhost:5000/admin) *(Login: admin/admin123)*

## 📸 Screenshots

### Portfolio Homepage
![Portfolio Homepage](https://via.placeholder.com/800x400/1a1a2e/ffffff?text=Portfolio+Homepage)

### Admin Dashboard
![Admin Dashboard](https://via.placeholder.com/800x400/1a1a2e/ffffff?text=Admin+Dashboard)

## ✨ Features

### 🎨 Frontend
- **Modern Dark Theme** with purple accent colors
- **Fully Responsive Design** - works on all devices
- **Smooth Animations** and hover effects
- **Interactive Elements** with professional styling
- **Tag-based Skills** display (no percentage bars)
- **Social Media Integration** (Instagram, LinkedIn, GitHub)
- **Contact Form** with validation

### ⚙️ Backend
- **Flask Framework** with Python 3.8+
- **PostgreSQL Database** for reliable data storage
- **RESTful API** with full CRUD operations
- **Secure Session Management**
- **Admin Authentication System**

### 🛠️ Admin Panel
- **Secure Login System** (admin/admin123)
- **Complete Content Management**:
  - ✅ Projects Management
  - ✅ Skills Organization by Categories
  - ✅ Internships Tracking
  - ✅ Education Timeline
  - ✅ Certifications Display
  - ✅ Contact Information Updates
- **Real-time Updates** - changes reflect immediately
- **User-friendly Interface** with modern design

## Content Management

The admin panel allows you to manage:
- **Projects**: Work experience and personal projects
- **Skills**: Technical skills with proficiency levels
- **Education**: Academic background
- **Certifications**: Professional certifications
- **Contact Information**: Personal contact details

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- Git

### 1. Clone the Repository
```bash
git clone <repository-url>
cd portfolio-website
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. Make sure PostgreSQL is running
2. Create a database named `portfolio_db`
3. Update database credentials in `app.py` if needed:
   - Username: `postgres`
   - Password: `dhara16`
   - Database: `portfolio_db`

### 5. Initialize Database
```bash
python populate_db.py
```

This will create all tables and populate them with initial data from the resume.

### 6. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Admin Access

- **URL**: `http://localhost:5000/admin`
- **Username**: `admin`
- **Password**: `admin123`

## Project Structure

```
portfolio-website/
├── app.py                 # Main Flask application
├── populate_db.py         # Database initialization script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       ├── script.js     # Frontend JavaScript
│       └── admin.js      # Admin panel JavaScript
└── templates/
    ├── base.html         # Base template
    ├── index.html        # Main portfolio page
    ├── admin_login.html  # Admin login page
    └── admin_dashboard.html # Admin dashboard
```

## Database Schema

### Tables
- **Admin**: Admin user credentials
- **Project**: Work experience and projects
- **Skill**: Technical skills with categories and proficiency
- **Education**: Academic background
- **Certification**: Professional certifications
- **Contact**: Personal contact information

## API Endpoints

### Projects
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Create new project
- `GET /api/projects/<id>` - Get specific project
- `PUT /api/projects/<id>` - Update project
- `DELETE /api/projects/<id>` - Delete project

### Skills
- `GET /api/skills` - Get all skills
- `POST /api/skills` - Create new skill
- `GET /api/skills/<id>` - Get specific skill
- `PUT /api/skills/<id>` - Update skill
- `DELETE /api/skills/<id>` - Delete skill

### Education
- `GET /api/education` - Get all education entries
- `POST /api/education` - Create new education entry
- `GET /api/education/<id>` - Get specific education entry
- `PUT /api/education/<id>` - Update education entry
- `DELETE /api/education/<id>` - Delete education entry

### Certifications
- `GET /api/certifications` - Get all certifications
- `POST /api/certifications` - Create new certification
- `GET /api/certifications/<id>` - Get specific certification
- `PUT /api/certifications/<id>` - Update certification
- `DELETE /api/certifications/<id>` - Delete certification

### Contact
- `GET /api/contact` - Get contact information
- `POST /api/contact` - Create contact information
- `PUT /api/contact` - Update contact information

## Customization

### Changing Colors
Edit the CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #6c5ce7;
    --secondary-color: #a29bfe;
    --background-color: #0a0a0a;
}
```

### Adding New Sections
1. Create database model in `app.py`
2. Add API endpoints
3. Update admin dashboard template
4. Add JavaScript functions for CRUD operations

## Security Notes

- Change the default admin password in production
- Update the Flask secret key
- Use environment variables for sensitive data
- Enable HTTPS in production

## Deployment

For production deployment:
1. Set `debug=False` in `app.py`
2. Use a production WSGI server (e.g., Gunicorn)
3. Configure environment variables
4. Set up SSL/HTTPS
5. Use a production database

## License

This project is open source and available under the MIT License.

## Contact

For questions or support, contact Dhara Ruparel at dhara.ruparel16@gmail.com