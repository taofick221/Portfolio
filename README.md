# Taofick Portfolio — Recruiter-Ready Premium Edition

Professional Django portfolio with a colorful, light visual system and Django Admin as the CMS.

## Design
- Professional colorful light UI; no dark/light toggle.
- Soft neutral page background and white elevated surfaces.
- Purple, blue, cyan, green and orange accents used with restraint.
- Compact spacing to reduce empty areas.
- Subtle shadows, hover elevation and image zoom.
- Fixed desktop sidebar and mobile slide-out navigation.
- Inline SVG icons for social/project/resume links; no external icon dependency.

## Content managed from Django Admin
- Profile, photo, availability and resume PDF
- Social links
- Skill categories and skills
- Optional custom skill icons; built-in local SVG defaults are used when no upload exists
- Projects, thumbnails, Live Demo, GitHub, technologies
- Project features and gallery via inline admin
- Education
- Research
- Experience
- Contact information and contact messages
- Blog posts
- Site settings

## Resume
Upload the PDF from Admin -> Profile. The uploaded resume is available through View/Download actions in the sidebar and homepage hero. The separate resume promotional section has intentionally been removed.

## Academic section
Education and Research are compact cards displayed side-by-side on desktop and stacked on mobile.

## Project detail
Each project can have:
- Category
- Date
- Status
- Overview
- Features
- Technologies
- Gallery
- Live Demo
- GitHub

## Installation

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    python manage.py migrate
    python manage.py seed_portfolio
    python manage.py createsuperuser
    python manage.py runserver

Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

## Database
SQLite is included as the easy local fallback. PostgreSQL is supported through `.env`:

    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=portfolio_db
    DB_USER=postgres
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=5432

Do not commit production secrets.


## Resume page
- Sidebar and homepage use a dedicated `/resume/` page.
- Clicking View Resume opens the portfolio resume viewer page.
- The page embeds the latest Admin-uploaded PDF.
- Download PDF is available on the resume page.
- Upload/change the PDF from Django Admin → Profile → Resume.
