# Taofick Portfolio

A personal portfolio website built with **Python and Django** to showcase projects, technical skills, education, research, experience, resume, and technical blog posts.

The portfolio uses **Django Admin as a content management system**, allowing the website content to be updated dynamically without modifying the source code.

---

## ✨ Features

- Professional personal portfolio
- Responsive design for desktop, tablet, and mobile
- Fixed sidebar navigation on desktop
- Slide-out navigation on mobile
- Dynamic portfolio content
- Django Admin CMS
- Profile management
- Profile image management
- Availability status
- Social media links
- Skills and skill categories
- Custom skill icons
- Project showcase
- Project detail pages
- Project technologies
- Project features
- Project image gallery
- Live Demo links
- GitHub repository links
- Featured projects
- Education section
- Research section
- Experience section
- Dedicated resume page
- Resume PDF viewer
- Resume PDF download
- Blog section
- Blog detail pages
- Markdown-supported blog content
- Contact information
- Contact message management
- Site settings
- PostgreSQL support
- SQLite support for local development

---

## 🛠️ Technology Stack

### Backend

- Python
- Django
- Django ORM
- Django Admin

### Database

- PostgreSQL
- SQLite

### Frontend

- HTML5
- CSS3
- JavaScript
- CSS Grid
- CSS Flexbox
- SVG Icons

### Development Tools

- Git
- GitHub
- Postman
- Linux

### Additional Technologies

The portfolio also showcases experience with:

- Django REST Framework
- RESTful APIs
- PostgreSQL
- Redis
- Celery
- Docker
- Docker Compose
- JWT Authentication
- Swagger / OpenAPI

---

# 📂 Project Structure

```text
Portfolio/
│
├── blog/
│   ├── migrations/
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── blog_extras.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── contact/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── core/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── portfolio/
│   ├── management/
│   │   └── commands/
│   │       └── seed_portfolio.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   └── models.py
│
├── projects/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   └── site.css
│   ├── js/
│   │   └── site.js
│   └── pdfjs/
│       └── build/
│           ├── pdf.mjs
│           └── pdf.worker.mjs
│
├── templates/
│   ├── base.html
│   ├── blog/
│   │   ├── list.html
│   │   └── detail.html
│   ├── contact/
│   ├── core/
│   │   ├── home.html
│   │   └── resume.html
│   └── projects/
│
├── media/
│
├── .env
├── .env.example
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt