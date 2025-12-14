# 🛠️ Portfolio Website Setup Guide

## 📋 Prerequisites

Before setting up your portfolio website, ensure you have:

- ✅ **Python 3.8+** installed
- ✅ **PostgreSQL** database server
- ✅ **Git** (optional, for version control)
- ✅ **Web browser** (Chrome, Firefox, Safari, Edge)

---

## 🚀 Step-by-Step Setup

### **Step 1: Database Setup**
1. **Install PostgreSQL** (if not already installed)
2. **Start PostgreSQL service**
3. **Create database:**
   ```sql
   CREATE DATABASE portfolio_db;
   ```
4. **Note your credentials:**
   - Username: `postgres`
   - Password: `dhara16` (or your PostgreSQL password)

### **Step 2: Install Dependencies**
```bash
# Install required Python packages
pip install -r requirements.txt
```

**Required packages:**
- Flask==2.3.3
- Flask-SQLAlchemy==3.0.5
- psycopg2-binary==2.9.7
- Werkzeug==2.3.7
- python-dotenv==1.0.0

### **Step 3: Initialize Database**
```bash
# Populate database with initial data
python populate_db.py
```

This will create:
- All database tables
- Sample data from your resume
- Admin user account

### **Step 4: Start the Application**
```bash
# Start the Flask development server
python app.py
```

**Or use the Windows batch file:**
```bash
# Double-click or run
run.bat
```

### **Step 5: Verify Setup**
1. **Open browser** and go to: `http://localhost:5000`
2. **Check portfolio** displays correctly
3. **Test admin panel:** `http://localhost:5000/admin`
4. **Login with:** `admin` / `admin123`

---

## 🔧 Configuration

### **Database Configuration**
If you need to change database settings, edit `app.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
```

### **Admin Credentials**
To change admin password, edit `app.py`:
```python
# Find this section and update password
admin = Admin(username='admin', password_hash=generate_password_hash('your_new_password'))
```

### **Profile Image**
Replace your profile image:
1. **Add your photo** to `static/images/`
2. **Name it:** `DHARA.jpg` (or update HTML reference)
3. **Recommended:** Square aspect ratio, high resolution

---

## 📁 Project Structure

```
portfolio-website/
├── 📄 app.py                    # Main Flask application
├── 📄 populate_db.py            # Database initialization
├── 📄 requirements.txt          # Python dependencies
├── 📄 run.bat                   # Windows startup script
├── 📄 setup.bat                 # Setup automation script
├── 📁 static/
│   ├── 📁 css/
│   │   └── 📄 style.css         # Main stylesheet
│   ├── 📁 js/
│   │   ├── 📄 script.js         # Frontend JavaScript
│   │   └── 📄 admin.js          # Admin panel JavaScript
│   └── 📁 images/
│       └── 📄 DHARA.jpg         # Profile image
├── 📁 templates/
│   ├── 📄 base.html             # Base template
│   ├── 📄 index.html            # Main portfolio page
│   ├── 📄 admin_login.html      # Admin login page
│   └── 📄 admin_dashboard.html  # Admin dashboard
├── 📄 README.md                 # Technical documentation
├── 📄 USER_GUIDE.md             # Comprehensive user guide
├── 📄 QUICK_REFERENCE.md        # Quick reference card
└── 📄 SETUP_GUIDE.md            # This setup guide
```

---

## 🎯 Initial Content Setup

### **After successful setup, add your content:**

1. **Update Profile Image:**
   - Replace `static/images/DHARA.jpg` with your photo

2. **Add Your Projects:**
   - Admin Panel → Projects → Add Project
   - Include all your significant work

3. **Update Skills:**
   - Admin Panel → Skills → Add Skill
   - Organize by categories

4. **Add Internships:**
   - Admin Panel → Internships → Add Internship
   - Include professional experience

5. **Update Education:**
   - Admin Panel → Education → Add Education
   - Add your academic background

6. **Add Certifications:**
   - Admin Panel → Certifications → Add Certification
   - Include professional certifications

7. **Update Contact Info:**
   - Admin Panel → Contact → Edit Contact Info
   - Add your current contact details

---

## 🚨 Troubleshooting Setup Issues

### **Common Problems & Solutions:**

#### **Database Connection Error:**
```
Error: could not connect to server
```
**Solution:**
- Ensure PostgreSQL is running
- Check database name: `portfolio_db`
- Verify credentials in `app.py`

#### **Module Not Found Error:**
```
ModuleNotFoundError: No module named 'flask'
```
**Solution:**
```bash
pip install -r requirements.txt
```

#### **Port Already in Use:**
```
Address already in use
```
**Solution:**
- Stop other Flask applications
- Or change port in `app.py`: `app.run(port=5001)`

#### **Permission Denied:**
```
Permission denied
```
**Solution:**
- Run terminal as administrator (Windows)
- Check file permissions
- Ensure PostgreSQL has proper permissions

#### **Profile Image Not Loading:**
**Solution:**
- Check file exists: `static/images/DHARA.jpg`
- Verify file format (JPG, PNG)
- Check file permissions

---

## 🔒 Security Setup (Production)

### **For Production Deployment:**

1. **Change Secret Key:**
   ```python
   app.config['SECRET_KEY'] = 'your-secure-random-key-here'
   ```

2. **Update Admin Password:**
   - Use strong, unique password
   - Consider adding more admin users

3. **Database Security:**
   - Use environment variables for credentials
   - Enable SSL connections
   - Regular backups

4. **Web Server:**
   - Use Gunicorn or uWSGI
   - Configure HTTPS/SSL
   - Set up reverse proxy (Nginx)

---

## ✅ Setup Verification Checklist

- [ ] PostgreSQL installed and running
- [ ] Python dependencies installed
- [ ] Database created and populated
- [ ] Flask application starts without errors
- [ ] Portfolio loads at `http://localhost:5000`
- [ ] Admin panel accessible at `http://localhost:5000/admin`
- [ ] Can login with `admin` / `admin123`
- [ ] Profile image displays correctly
- [ ] All sections show sample data
- [ ] Admin CRUD operations work
- [ ] Responsive design works on mobile

---

## 🎉 Next Steps

After successful setup:

1. **Customize Content** - Add your personal information
2. **Update Styling** - Modify colors and design if needed
3. **Test Thoroughly** - Check all features work correctly
4. **Deploy** - Consider hosting options for production
5. **Maintain** - Keep content updated regularly

---

## 📞 Getting Help

If you encounter issues during setup:

1. **Check Error Messages** - Read terminal output carefully
2. **Verify Prerequisites** - Ensure all requirements are met
3. **Review File Paths** - Check all files are in correct locations
4. **Test Database** - Verify PostgreSQL connection
5. **Browser Console** - Check for JavaScript errors

---

*Your portfolio website is now ready to showcase your professional journey!*

**Happy coding! 🚀**