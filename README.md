# University ERP System

This project is a Django-based University Enterprise Resource Planning (ERP) system designed to manage core academic aspects such as Programs, Courses, Subjects, Semesters, Syllabus, and potentially more functionalities in the future.

## Technologies Used

* Backend: Django
* Frontend: Django Templates
* Styling: Tailwind CSS (planned)
* API: Django Rest Framework (potential future integration)
* Authentication: Django Built-in Authentication with custom User model (email and phone number fields)
* Data Validation: Django Forms
* Database: (Specify your chosen database - e.g., PostgreSQL, SQLite)
* Deployment: Render Free Account (planned)
* Version Control: Git
* Project Management: GitHub Projects (Free)
* Documentation: This README file

## Project Structure
university/
├── university/
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/  # Your main app
│   ├── init.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/core/  # Frontend templates
│       ├── ...
│   └── ...  # Other app-related files
├── users/  # Potential app for user management (optional)
│   ├── init.py
│   ├── ...
├── static/  # Static files (CSS, JS, images)
│   ├── ...
├── templates/  # Base template and others
│   ├── base.html
│   ├── ...
└── README.md


## Installation

1. **Prerequisites:**
   - Python 3.x (https://www.python.org/downloads/)
   - pip (usually comes with Python)

2. **Clone the repository:**

   ```bash
   git clone [https://github.com/](https://github.com/)manishgupta248/university.git

python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate  # Windows

