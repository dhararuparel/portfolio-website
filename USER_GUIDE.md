# 📚 Portfolio Website User Guide

## 🎯 Overview

This is a comprehensive guide for understanding and managing your personal portfolio website. The website showcases your professional profile with a modern dark theme and includes a powerful admin panel for content management.

---

## 🌐 Website Structure

### **Frontend Portfolio Sections:**

#### 1. **Hero Section**
- **Your Profile Photo** - Professional circular image with gradient border
- **Introduction** - "Hii, I'm Dhara Ruparel"
- **Subtitle** - "Computer Science Student & AI Enthusiast"
- **Description** - Brief professional summary
- **Action Buttons** - "View My Work" and "Get In Touch"

#### 2. **About Me Section**
- **Left Side:** Professional description and background
- **Right Side:** 
  - **Statistics:** Projects Completed | Internships | Certifications
  - **Languages:** English, Hindi, Gujarati (as tags)

#### 3. **Projects Section**
- **Project Cards** showing:
  - Project title and description
  - Duration and team size
  - Your role in the project
  - Technologies used (as tags)
  - Hover animations and effects

#### 4. **Skills Section**
- **Tag-based Layout** - Skills displayed as modern pills/badges
- **Categories:** Programming Languages, Web Technologies, Databases, etc.
- **Hover Effects** - Tags lift and change color on hover
- **No Percentages** - Clean, simple skill names only

#### 5. **Internships Section**
- **Internship Cards** displaying:
  - Position and company name
  - Duration and location
  - Detailed description
  - Technologies used (if applicable)
  - Professional card design with animations

#### 6. **Education Section**
- **Timeline Layout** - Chronological education history
- **Information Shown:**
  - Degree and institution
  - Year of completion
  - Percentage/grades achieved
  - Alternating left-right layout

#### 7. **Certifications Section**
- **Grid Layout** - Professional certification cards
- **Details Include:**
  - Certification title and issuer
  - Scores/percentages (if applicable)
  - Date ranges
  - Certificate icons

#### 8. **Contact Section**
- **Left Side:** Contact information and social links
- **Right Side:** Contact form for visitors
- **Social Media Icons:** Instagram, LinkedIn, GitHub, Email
- **Contact Details:** Phone, email, location

---

## 🔧 Admin Panel Guide

### **Accessing Admin Panel:**
```
URL: http://localhost:5000/admin
Username: admin
Password: admin123
```

### **Admin Dashboard Sections:**

#### 1. **Projects Management**
- **Add New Projects:** Click "Add Project" button
- **Required Fields:**
  - Title (e.g., "Camera Motion Sensing Project")
  - Description (detailed project overview)
  - Technologies (comma-separated: "Python, OpenCV, Flask")
  - Duration (e.g., "6 months")
  - Team Size (e.g., "4 persons")
  - Role (e.g., "Team Member" or "Individual")
- **Actions:** Edit existing projects or delete them

#### 2. **Skills Management**
- **Add New Skills:** Click "Add Skill" button
- **Required Fields:**
  - Skill Name (e.g., "Python", "Machine Learning")
  - Category (dropdown selection):
    - Programming Languages
    - Web Technologies
    - Web Frameworks
    - Databases
    - Libraries & Frameworks
    - Tools & Technologies
- **Note:** No proficiency percentages needed (simplified design)

#### 3. **Internships Management**
- **Add New Internships:** Click "Add Internship" button
- **Required Fields:**
  - Position (e.g., "Software Development Intern")
  - Company (e.g., "Tech Solutions Inc.")
  - Duration (e.g., "3 months")
  - Location (e.g., "Mumbai, India")
  - Description (detailed internship experience)
  - Technologies (optional, comma-separated)

#### 4. **Education Management**
- **Add Education Entries:** Click "Add Education" button
- **Required Fields:**
  - Degree (e.g., "B.E.(COMPUTER) - KSV")
  - Institution (e.g., "KSV University")
  - Year (e.g., "2022-2026")
  - Percentage/Grade (optional, e.g., "8.44" or "87%")

#### 5. **Certifications Management**
- **Add Certifications:** Click "Add Certification" button
- **Required Fields:**
  - Title (full certification name)
  - Issuer (e.g., "NPTEL", "TCS iON")
  - Percentage/Score (optional)
  - Date Range (optional, e.g., "20/01/2025 to 24/01/2025")

#### 6. **Contact Information**
- **Update Contact Details:**
  - Phone number
  - Email address
  - Location
  - LinkedIn URL (optional)
- **Note:** Only one contact record exists - edit to update

---

## 🚀 Getting Started

### **First Time Setup:**

1. **Run the Application:**
   ```bash
   python app.py
   ```
   Or double-click `run.bat`

2. **Access Your Portfolio:**
   - Open browser: `http://localhost:5000`
   - View your live portfolio

3. **Access Admin Panel:**
   - Go to: `http://localhost:5000/admin`
   - Login with: `admin` / `admin123`

### **Adding Your First Content:**

1. **Add a New Project:**
   - Go to Admin → Projects → Add Project
   - Fill in your project details
   - Save and view on portfolio

2. **Add Skills:**
   - Go to Admin → Skills → Add Skill
   - Choose appropriate category
   - Add all your technical skills

3. **Add Internship Experience:**
   - Go to Admin → Internships → Add Internship
   - Include company, role, and experience details

---

## 🎨 Customization Guide

### **Changing Colors:**
Edit `static/css/style.css` and modify these CSS variables:
```css
/* Primary purple color */
#6c5ce7 → Your preferred color

/* Secondary purple */
#a29bfe → Lighter shade of your color

/* Background */
#0a0a0a → Your background color
```

### **Updating Profile Image:**
1. Replace `static/images/DHARA.jpg` with your photo
2. Keep the same filename or update the HTML reference
3. Recommended: Square image, high resolution

### **Modifying Content:**
- **Static Text:** Edit `templates/index.html`
- **Dynamic Content:** Use Admin Panel
- **Styling:** Modify `static/css/style.css`

---

## 📱 Responsive Design

### **Device Compatibility:**
- ✅ **Desktop** - Full layout with all features
- ✅ **Tablet** - Adapted grid layouts
- ✅ **Mobile** - Stacked sections, hamburger menu
- ✅ **All Screen Sizes** - Flexible and responsive

### **Mobile Features:**
- Hamburger navigation menu
- Touch-friendly buttons
- Optimized image sizes
- Readable text scaling

---

## 🔒 Security & Maintenance

### **Admin Security:**
- **Change Default Password:** Update in `app.py`
- **Use Strong Passwords:** For production deployment
- **Secure Database:** Use environment variables for credentials

### **Regular Maintenance:**
- **Update Content:** Keep projects and skills current
- **Backup Database:** Regular PostgreSQL backups
- **Monitor Performance:** Check loading speeds

### **Production Deployment:**
1. Set `debug=False` in `app.py`
2. Use production WSGI server (Gunicorn)
3. Configure HTTPS/SSL
4. Use environment variables for secrets
5. Set up proper database hosting

---

## 🛠️ Troubleshooting

### **Common Issues:**

#### **Website Not Loading:**
- Check if Flask app is running: `python app.py`
- Verify URL: `http://localhost:5000`
- Check terminal for error messages

#### **Admin Panel Not Working:**
- Verify credentials: `admin` / `admin123`
- Check database connection
- Ensure PostgreSQL is running

#### **Database Errors:**
- Restart PostgreSQL service
- Check database name: `portfolio_db`
- Verify credentials: `postgres` / `dhara16`

#### **Images Not Displaying:**
- Check file path: `static/images/DHARA.jpg`
- Verify image file exists
- Check file permissions

### **Getting Help:**
- Check browser console for JavaScript errors
- Review Flask terminal output for backend errors
- Verify all required files are present

---

## 📊 Analytics & Performance

### **Monitoring Your Portfolio:**
- **Page Load Speed:** Use browser dev tools
- **Mobile Responsiveness:** Test on different devices
- **Content Updates:** Regular admin panel usage
- **User Engagement:** Monitor contact form submissions

### **Performance Tips:**
- **Optimize Images:** Compress profile photos
- **Minimize CSS/JS:** For production deployment
- **Database Indexing:** For large datasets
- **Caching:** Implement for better performance

---

## 🎯 Best Practices

### **Content Management:**
- **Keep Projects Updated:** Add new work regularly
- **Skill Relevance:** Focus on current technologies
- **Professional Tone:** Maintain consistent voice
- **Regular Updates:** Keep information current

### **Design Consistency:**
- **Color Scheme:** Stick to the purple theme
- **Typography:** Maintain font consistency
- **Spacing:** Keep uniform margins and padding
- **Animation:** Subtle, professional effects

### **SEO & Accessibility:**
- **Alt Text:** Add for all images
- **Semantic HTML:** Use proper heading structure
- **Meta Tags:** Add for better search visibility
- **Keyboard Navigation:** Ensure accessibility

---

## 📞 Support & Resources

### **Technical Stack:**
- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python Flask
- **Database:** PostgreSQL
- **Styling:** Custom CSS with animations
- **Icons:** Font Awesome

### **File Structure:**
```
portfolio-website/
├── app.py                 # Main Flask application
├── static/
│   ├── css/style.css     # Main stylesheet
│   ├── js/script.js      # Frontend JavaScript
│   ├── js/admin.js       # Admin panel JavaScript
│   └── images/           # Profile images
├── templates/
│   ├── index.html        # Main portfolio page
│   ├── admin_dashboard.html # Admin interface
│   └── admin_login.html  # Admin login page
├── run.bat               # Windows startup script
└── README.md            # Technical documentation
```

### **Quick Commands:**
```bash
# Start the application
python app.py

# Access portfolio
http://localhost:5000

# Access admin
http://localhost:5000/admin

# Stop the application
Ctrl+C in terminal
```

---

## 🎉 Conclusion

Your portfolio website is now ready to showcase your professional journey! Use the admin panel to keep your content updated, and don't forget to regularly add new projects, skills, and experiences as you grow in your career.

**Remember:** This is your digital presence - keep it current, professional, and reflective of your best work!

---

*Last Updated: December 2024*
*Version: 1.0*