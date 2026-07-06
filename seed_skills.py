"""Seed skills into the portfolio database."""
import os
from dotenv import load_dotenv
load_dotenv()

from app import app, db, Skill

SKILLS = [
    # Programming Languages
    ("Python",          "Programming Languages"),
    ("JavaScript",      "Programming Languages"),
    ("SQL",             "Programming Languages"),

    # AI & Machine Learning
    ("Machine Learning",    "AI & Machine Learning"),
    ("NLP",                 "AI & Machine Learning"),
    ("RAG",                 "AI & Machine Learning"),
    ("LLM Applications",    "AI & Machine Learning"),
    ("Computer Vision",     "AI & Machine Learning"),

    # Libraries & Frameworks
    ("Scikit-learn", "Libraries & Frameworks"),
    ("Pandas",       "Libraries & Frameworks"),
    ("OpenCV",       "Libraries & Frameworks"),
    ("MediaPipe",    "Libraries & Frameworks"),
    ("NLTK",         "Libraries & Frameworks"),
    ("Streamlit",    "Libraries & Frameworks"),

    # Web Frameworks
    ("Flask",  "Web Frameworks"),
    ("Django", "Web Frameworks"),

    # Databases & Backend Services
    ("PostgreSQL", "Databases & Backend Services"),
    ("MySQL",      "Databases & Backend Services"),
    ("Supabase",   "Databases & Backend Services"),

    # Web Technologies
    ("HTML",       "Web Technologies"),
    ("CSS",        "Web Technologies"),

    # Developer & AI Tools
    ("Git",           "Developer & AI Tools"),
    ("GitHub",        "Developer & AI Tools"),
    ("Cursor",        "Developer & AI Tools"),
    ("GitHub Copilot","Developer & AI Tools"),
    ("Gemini",        "Developer & AI Tools"),
    ("ChatGPT",       "Developer & AI Tools"),
]

with app.app_context():
    added = 0
    skipped = 0
    for order, (name, category) in enumerate(SKILLS):
        exists = Skill.query.filter_by(name=name, category=category).first()
        if exists:
            print(f"  SKIP  {name} ({category})")
            skipped += 1
        else:
            skill = Skill(name=name, category=category, proficiency=80, display_order=order)
            db.session.add(skill)
            print(f"  ADD   {name} ({category})")
            added += 1
    db.session.commit()
    print(f"\nDone! Added {added} skills, skipped {skipped} duplicates.")
