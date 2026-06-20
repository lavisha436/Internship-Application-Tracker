# Internship Application Tracker

A Django-based web application that helps users manage and track their internship applications in one place. The application provides authentication, application management, dashboard analytics, and search functionality.

---

## Features

### User Authentication

* User Registration
* User Login
* User Logout
* Secure user-specific data access

### Application Management

* Add new internship applications
* Edit existing applications
* Delete applications
* View all applications

### Dashboard

* Total Applications Count
* Applied Applications Count
* Interview Applications Count
* Offered Applications Count
* Rejected Applications Count
* Recent Applications Section

### Search

* Search applications by company name

### User Interface

* Responsive Bootstrap 5 UI
* Dashboard Cards
* Landing Page for Guest Users
* Navigation Bar

---

## Tech Stack

### Backend

* Django
* Python

### Database

* SQLite

### Frontend

* HTML
* CSS
* Bootstrap 5

---

## Project Structure

```text
InternshipTracker/
│
├── applications/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── admin.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/lavisha436/Internship-Application-Tracker.git
```

```bash
cd Internship-Application-Tracker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Screenshots

### Landing Page

(Add screenshot here)

### Dashboard

(Add screenshot here)

### Applications Page

(Add screenshot here)

---

## Future Improvements

* Status Filters
* Email Notifications
* Application Notes
* Interview Scheduling
* Pagination
* REST API using Django REST Framework (DRF)

---

## Learning Outcomes

Through this project, I learned:

* Django Models
* Django ORM
* Migrations
* ModelForms
* Authentication System
* CRUD Operations
* Template Rendering
* Bootstrap Integration
* Search Functionality
* Git & GitHub Workflow

---

## Author

**Lavisha Arora**

GitHub: https://github.com/lavisha436
