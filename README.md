# 🚀 Placement Preparation Portal

A full-stack web application designed to help students prepare for placements through mock tests, coding practice, and resume guidance.

🔗 **Live Demo:** https://placement-preparation-portal.onrender.com  
🔗 **GitHub Repository:** https://github.com/indranath0612/placement-preparation-portal

---

## 📌 Features

### 👤 Authentication
- Secure login system
- Admin-controlled access for managing content

### 📝 Mock Tests
- 100+ MCQ questions stored in database
- Randomized selection of 10 questions per attempt
- Auto-evaluation with score calculation
- Highlight correct and incorrect answers
- Session-based test handling

### 💻 Coding Practice
- Collection of commonly asked coding interview questions
- Categorized and stored in database
- Easy-to-read interface for practice

### 🛠 Admin Panel
- Admin login
- Add new mock test questions
- Add coding practice questions
- Database-driven content management

### 🌐 Deployment
- Live deployment using Render
- Gunicorn as production WSGI server
- GitHub-based CI/CD workflow

---

## 🧰 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask
- Jinja2 (templating)

### Database
- SQLite

### Deployment & Tools
- Git & GitHub
- Render
- Gunicorn

---

## 📂 Project Structure


placement_preparation_portal/
│
├── app.py
├── database.db
├── requirements.txt
│
├── static/
│ └── style.css
│
├── templates/
│ ├── login.html
│ ├── admin.html
│ ├── mocktest.html
│ ├── coding.html
│ └── add_question.html
│
└── README.md
