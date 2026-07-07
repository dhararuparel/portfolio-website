<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=DHARA%20RUPAREL&fontSize=60&fontColor=fff&animation=twinkling&fontAlignY=35&desc=AI%20Engineer%20%7C%20Machine%20Learning%20%7C%20LLM%20Applications&descAlignY=55&descSize=18" width="100%"/>

<br/>

[![Portfolio](https://img.shields.io/badge/🌐_Live_Portfolio-View_Now-6c5ce7?style=for-the-badge&logoColor=white)](https://dhararuparel.github.io/portfolio-website)
[![Admin Panel](https://img.shields.io/badge/🔐_Admin_Panel-/admin-a29bfe?style=for-the-badge)](https://dhararuparel.github.io/portfolio-website/admin)
[![GitHub](https://img.shields.io/badge/GitHub-dhararuparel-181717?style=for-the-badge&logo=github)](https://github.com/dhararuparel)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/dhara-ruparel/)

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white)

</div>

---

<div align="center">

## ⚡ A living, breathing portfolio — fully manageable from a sleek admin panel. No code edits. Ever.

</div>

---

## 🎯 What Makes This Special

> This isn't just a static portfolio. Every single piece of content — from projects to the hero intro video — is dynamically managed through a secure admin dashboard. Upload a new resume? Done in seconds. New intro video? Drag, drop, upload. It just works.

```
🎬  Hero intro video     → upload from admin panel, streamed live to visitors
📄  Resume PDF           → replace anytime, served from database
🗂️  All content sections → full CRUD with drag-and-drop reordering
📧  Contact form         → emails delivered via Gmail SMTP
🌗  Dark / Light theme   → toggle with smooth transitions
📱  Fully responsive     → pixel-perfect on every screen size
```

---

## 🚀 Live Demo

<div align="center">

| | |
|:---:|:---:|
| 🌐 **Portfolio** | [dhararuparel.github.io/portfolio-website](https://dhararuparel.github.io/portfolio-website) |
| 🔐 **Admin Panel** | `/admin` → `admin` / `admin123` |

</div>

---

## 🧠 Tech Stack

<table>
<tr>
<td valign="top" width="50%">

### Backend
- **Python 3** + **Flask 2.3** — lightweight & fast web framework
- **Flask-SQLAlchemy** — ORM for clean database interactions
- **PostgreSQL** — robust relational database (hosted on Supabase)
- **Gunicorn** — production WSGI server
- **Flask-Mail** — Gmail SMTP integration for contact form
- **Werkzeug** — secure password hashing for admin auth

</td>
<td valign="top" width="50%">

### Frontend
- **HTML5** — semantic, accessible markup
- **Vanilla CSS** — custom design system with glassmorphism, gradients, animations
- **Vanilla JavaScript** — zero framework bloat, pure performance
- **Font Awesome** — icon library
- **Google Fonts** — premium typography

</td>
</tr>
<tr>
<td valign="top">

### Database & Storage
- **PostgreSQL** on **Supabase** (cloud)
- Video & Resume stored as **binary blobs** — survives redeployments
- Auto-migration on startup — zero manual DB setup

</td>
<td valign="top">

### Deployment
- **Render** — primary hosting (Gunicorn + PostgreSQL)
- **Vercel** — alternate serverless deployment
- **GitHub Pages** — static export via `generate_static.py`

</td>
</tr>
</table>

---

## 📁 Project Structure

```
📦 portfolio-website/
│
├── 🐍 app.py                     # Flask app — all routes, models, API endpoints
├── 📋 requirements.txt           # Python dependencies
├── ⚙️  Procfile                  # Gunicorn start command for Render
├── 🔧 vercel.json                # Vercel serverless config
├── 🔐 .env                       # Environment variables (never committed)
│
├── 📂 templates/
│   ├── base.html                 # Base layout (fonts, icons, meta tags)
│   ├── index.html                # Portfolio homepage (hero, projects, skills...)
│   ├── admin_login.html          # Admin authentication page
│   └── admin_dashboard.html     # Full content management dashboard
│
├── 📂 static/
│   ├── css/
│   │   ├── style.css             # Portfolio design system
│   │   └── admin.css             # Admin dashboard styles
│   ├── js/
│   │   ├── script.js             # Portfolio animations & interactions
│   │   └── admin.js              # CRUD operations + drag-and-drop reordering
│   └── videos/
│       └── intro_video.mp4       # Fallback hero video (if none in DB)
│
├── 📂 docs/                      # GitHub Pages static export
├── 🌱 populate_db.py             # Initial database seed script
└── ⚡ generate_static.py         # Generates static build for GitHub Pages
```

---

## 🛠️ Local Setup

### Prerequisites
- Python 3.9+
- PostgreSQL (local) or a [Supabase](https://supabase.com) project (free tier works)
- A Gmail account with [App Password](https://myaccount.google.com/apppasswords) enabled

### 1️⃣ Clone & Enter

```bash
git clone https://github.com/dhararuparel/portfolio-website.git
cd portfolio-website
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment

Create a `.env` file at the project root:

```env
# App
SECRET_KEY=your-super-secret-random-key-here

# Database (PostgreSQL)
DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db

# Gmail SMTP (for contact form)
MAIL_USERNAME=your-gmail@gmail.com
MAIL_PASSWORD=your-16-char-app-password

# Contact form recipient (optional — defaults to MAIL_USERNAME)
CONTACT_RECEIVER_EMAIL=your-gmail@gmail.com
```

> 💡 **Gmail App Password**: Google Account → Security → 2-Step Verification → App Passwords → Generate for "Mail"

### 5️⃣ Run

```bash
python app.py
```

✅ Tables are auto-created. Admin account `admin / admin123` is seeded on first run.

Open → `http://127.0.0.1:5000`

---

## 🔐 Admin Panel Guide

Navigate to `/admin` and log in.

<table>
<thead>
<tr><th>Section</th><th>Capabilities</th></tr>
</thead>
<tbody>
<tr><td>🗂️ <b>Projects</b></td><td>Add, edit, delete, reorder — with optional GitHub / demo links</td></tr>
<tr><td>⚙️ <b>Skills</b></td><td>Add by category (AI, Languages, Frameworks, Tools…), reorder</td></tr>
<tr><td>💼 <b>Internships</b></td><td>Full work experience entries with company, role, duration, tech stack</td></tr>
<tr><td>🎓 <b>Education</b></td><td>Degree, institution, year, percentage — drag to reorder</td></tr>
<tr><td>🏅 <b>Certifications</b></td><td>Title, issuer, score, date range — drag to reorder</td></tr>
<tr><td>📬 <b>Contact</b></td><td>Phone, email, location, LinkedIn URL</td></tr>
<tr><td>📄 <b>Resume</b></td><td>Drag & drop PDF upload → stored in DB → always served fresh</td></tr>
<tr><td>🎬 <b>Intro Video</b></td><td>Drag & drop MP4/WebM upload → stored in DB → live preview before upload</td></tr>
</tbody>
</table>

---

## 🌐 Deployment

### ▶ Render (Recommended)

1. Push to GitHub
2. New **Web Service** on [render.com](https://render.com)
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Add all `.env` variables in the Render dashboard
6. Link a **PostgreSQL** database (or use Supabase via `DATABASE_URL`)

> 🚀 The app auto-creates all tables and admin on first boot — zero manual DB setup.

### ▲ Vercel (Alternate)

```bash
vercel deploy
```

> ⚠️ Vercel's serverless functions have a 10s timeout — large video uploads may fail. Use Render for full functionality.

### 📄 GitHub Pages (Static Export)

```bash
python generate_static.py
git add docs/ && git commit -m "chore: rebuild static site" && git push
```

Enable GitHub Pages from the `docs/` folder in repository settings.

---

## 🔑 Environment Variables

| Variable | Required | Description |
|---|:---:|---|
| `SECRET_KEY` | ✅ | Flask session secret — long random string |
| `DATABASE_URL` | ✅ | PostgreSQL connection URI |
| `MAIL_USERNAME` | ✅ | Gmail address used to send emails |
| `MAIL_PASSWORD` | ✅ | Gmail App Password (16-char, not your login password) |
| `CONTACT_RECEIVER_EMAIL` | ⬜ | Email to receive contact form submissions |

---

## 📡 API Reference

> All routes below require admin session. Unauthenticated requests return `401`.

<details>
<summary><b>📁 Projects</b></summary>

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/projects` | List all projects |
| `POST` | `/api/projects` | Create project |
| `GET` | `/api/projects/<id>` | Get single project |
| `PUT` | `/api/projects/<id>` | Update project |
| `DELETE` | `/api/projects/<id>` | Delete project |
| `POST` | `/api/projects/reorder` | Save display order |

</details>

<details>
<summary><b>⚙️ Skills, 💼 Internships, 🎓 Education, 🏅 Certifications</b></summary>

Same pattern as Projects: `GET/POST /api/<resource>` and `GET/PUT/DELETE /api/<resource>/<id>` and `POST /api/<resource>/reorder`

Resources: `skills` · `internships` · `education` · `certifications`

</details>

<details>
<summary><b>📄 Resume & 🎬 Intro Video</b></summary>

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/resume/upload` | Upload PDF resume |
| `GET` | `/api/resume/status` | Check resume status |
| `GET` | `/resume/download` | Download current resume |
| `POST` | `/api/intro-video/upload` | Upload intro video |
| `GET` | `/api/intro-video/status` | Check video status |
| `GET` | `/intro-video/stream` | Stream video to browser |

</details>

<details>
<summary><b>📬 Contact</b></summary>

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/contact` | Get contact info |
| `POST` | `/api/contact` | Create contact info |
| `PUT` | `/api/contact` | Update contact info |
| `POST` | `/api/contact/send` | Send contact form email (public) |

</details>

---

## 🗄️ Database Models

```
Admin          → id, username, password_hash
Project        → id, title, description, technologies, duration, team_size, role, link_url, link_label, display_order
Skill          → id, name, category, proficiency, display_order
Internship     → id, company, position, duration, location, description, technologies, display_order
Education      → id, degree, institution, year, percentage, display_order
Certification  → id, title, issuer, percentage, date_range, display_order
Contact        → id, phone, email, location, linkedin
ResumeFile     → id, filename, content_type, data (BLOB), updated_at
IntroVideo     → id, filename, content_type, data (BLOB), updated_at
```

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
