<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=DHARA%20RUPAREL&fontSize=60&fontColor=fff&animation=twinkling&fontAlignY=35&desc=AI%20Engineer%20%7C%20Machine%20Learning%20%7C%20LLM%20Applications&descAlignY=55&descSize=18" width="100%"/>

<br/>

[![Portfolio](https://img.shields.io/badge/🌐_Live_Portfolio-View_Now-6c5ce7?style=for-the-badge&logoColor=white)](https://dhara-ruparel.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-dhararuparel-181717?style=for-the-badge&logo=github)](https://github.com/dhararuparel)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/dhara-ruparel/)

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)

</div>

---

<div align="center">

## ⚡ A full-stack portfolio — every section managed from a secure admin panel. No code edits. Ever.

</div>

---

## 🚀 Live Demo

<div align="center">

| | |
|:---:|:---:|
| 🌐 **Portfolio** | [dhara-ruparel.vercel.app](https://dhara-ruparel.vercel.app/) |
| 🔐 **Admin Panel** | [dhara-ruparel.vercel.app/admin](https://dhara-ruparel.vercel.app/admin) |

</div>

---

## ✨ Features

```
🎬  Hero intro video     → upload from admin panel, streamed live to visitors
📄  Resume PDF           → replace anytime, served from database
🗂️  All content sections → full CRUD with drag-and-drop reordering
📧  Contact form         → emails delivered via Gmail SMTP
🌗  Dark / Light theme   → toggle with smooth transitions
📱  Fully responsive     → pixel-perfect on every screen size
```

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3, Flask 2.3, Flask-SQLAlchemy, Werkzeug |
| **Database** | PostgreSQL hosted on Supabase |
| **Email** | Flask-Mail (Gmail SMTP) |
| **Server** | Gunicorn |
| **Frontend** | HTML5, Vanilla CSS, Vanilla JavaScript |
| **Deployment** | Vercel |

---

## 📁 Project Structure

```
📦 portfolio-website/
│
├── 🐍 app.py                    # Flask app — routes, models, API
├── 📋 requirements.txt          # Python dependencies
├── ⚙️  Procfile                 # Gunicorn entry point
├── 🔧 vercel.json               # Vercel deployment config
├── 🔐 .env                      # Environment variables (not committed)
│
├── 📂 templates/
│   ├── base.html                # Base layout
│   ├── index.html               # Portfolio homepage
│   ├── admin_login.html         # Admin login
│   └── admin_dashboard.html    # Content management dashboard
│
└── 📂 static/
    ├── css/  style.css, admin.css
    ├── js/   script.js, admin.js
    └── videos/ intro_video.mp4  # Fallback hero video
```

---

## 🛠️ Local Setup

```bash
# 1. Clone
git clone https://github.com/dhararuparel/portfolio-website.git
cd portfolio-website

# 2. Virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file (see below)

# 5. Run
python app.py
```

### `.env` Configuration

```env
SECRET_KEY=your-random-secret-key
DATABASE_URL=postgresql://user:password@host:5432/dbname
MAIL_USERNAME=your-gmail@gmail.com
MAIL_PASSWORD=your-16-char-app-password
CONTACT_RECEIVER_EMAIL=your-gmail@gmail.com
```

> 💡 **Gmail App Password**: Google Account → Security → 2-Step Verification → App Passwords

Open → `http://127.0.0.1:5000`  
Admin → `http://127.0.0.1:5000/admin`

---

## 🔐 Admin Panel

| Section | What you can do |
|---|---|
| 🗂️ **Projects** | Add, edit, delete, reorder — with optional GitHub/demo links |
| ⚙️ **Skills** | Manage by category, reorder |
| 💼 **Internships** | Full work experience with tech stack |
| 🎓 **Education** | Degree, institution, year, grade |
| 🏅 **Certifications** | Title, issuer, score, date range |
| 📬 **Contact** | Phone, email, location, LinkedIn |
| 📄 **Resume** | Drag & drop PDF upload — stored in DB |
| 🎬 **Intro Video** | Drag & drop MP4 upload — live preview before upload |

---

## 🌐 Deployment on Vercel

```bash
vercel deploy
```

Set these environment variables in the Vercel dashboard:

| Variable | Required |
|---|:---:|
| `SECRET_KEY` | ✅ |
| `DATABASE_URL` | ✅ |
| `MAIL_USERNAME` | ✅ |
| `MAIL_PASSWORD` | ✅ |
| `CONTACT_RECEIVER_EMAIL` | ⬜ |

> The app auto-creates all database tables and the admin account on first boot.

---

<div align="center">

## 🤝 Connect

[![Email](https://img.shields.io/badge/Email-dhararuparel16%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dhararuparel16@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Dhara_Ruparel-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dhara-ruparel/)
[![GitHub](https://img.shields.io/badge/GitHub-dhararuparel-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dhararuparel)
[![Instagram](https://img.shields.io/badge/Instagram-@dhara__ruparel16-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/dhara_ruparel16)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer&animation=twinkling" width="100%"/>

*Built with ❤️ by Dhara Ruparel — AI Engineer*

</div>
