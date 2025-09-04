# Django Project Setup Guide

## Steps to run locally:

### 1. Clone the repo

```bash
git clone <repository-url>
```

---

### 2. Navigate inside the `djangodemo` folder and create a virtual environment

```bash
cd djangodemo
python -m venv venv
```

---

### 3. Activate the virtual environment

- On **Windows**:

```bash
venv\Scripts\activate
```

- On **macOS/Linux**:

```bash
source venv/bin/activate
```

---

### 4. Install all dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Navigate again into the `djangodemo` folder

```bash
cd djangodemo
```

---

### 6. Run the Django development server

```bash
python manage.py runserver
```

The server will start at:

```
http://127.0.0.1:8000/
```

## Notes on Project Components

1. [Create a Django Project](#1-create-a-django-project)
2. [Start the Django Server](#2-start-the-django-server)
3. [Install DB Browser for SQLite](#3-install-db-browser-for-sqlite)
4. [Project Folder Structure](#4-project-folder-structure)
5. [Create an App Folder](#5-create-an-app-folder)
6. [App Folder Structure](#6-app-folder-structure)
7. [Admin Panel Setup](#7-admin-panel-setup)

---

## 1. Create a Django Project

### Steps:

- Create a new Django project using:

```bash
django-admin startproject <project-folder-name>
```

**Example:**

```bash
django-admin startproject mysite
```

---

## 2. Start the Django Server

### Steps:

- Navigate inside the project folder:

```bash
cd mysite
```

- The `mysite` folder will contain another sub-folder named `mysite` along with `manage.py`.
  Folder structure:

```plaintext
mysite/
├── mysite/
└── manage.py
```

- Run the Django development server:

```bash
python manage.py runserver
```

- The Django server starts on:

```
http://127.0.0.1:8000/
```

After running the server, the project folder structure becomes:

```plaintext
mysite/
├── mysite/    # Project folder
├── manage.py
└── db.sqlite3
```

---

## 3. Install DB Browser for SQLite

### Steps:

- Download from:

```
https://sqlitebrowser.org/dl/
```

- Choose the Standard Installer for 64-bit.

---

## 4. Project Folder Structure

Inside the `mysite/mysite` sub-folder, you will find:

```plaintext
|--- __init__.py   # Initializes mysite as a package
|--- asgi.py       # Asynchronous Server Gateway Interface (used for async hosting)
|--- wsgi.py       # Web Server Gateway Interface (used for deployment)
|--- settings.py   # All settings (Database configs, Installed apps, etc.)
|--- urls.py       # Contains all URL routes (routing for the application)
```

---

## 5. Create an App Folder

### Steps:

- Create an app folder inside your Django project:

```bash
python manage.py startapp <app-folder-name>
```

**Example:**

```bash
python manage.py startapp demo
```

- If you run the server now:

```bash
python manage.py runserver
```

You might see this warning:

```plaintext
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
```

✅ Fix this by running:

```bash
python manage.py migrate
```

By default, 11 tables will be created in the database.

---

## 6. App Folder Structure

The `demo` folder contains these files:

```plaintext
|--- __init__.py  # Initializes app folder
|--- admin.py     # Register models for admin panel
|--- apps.py
|--- models.py    # Define database models
|--- tests.py
|--- views.py
```

---

## 7. Admin Panel Setup

### Steps:

- Django runs on:

```
http://127.0.0.1:8000/
```

- For the admin panel, go to:

```
http://127.0.0.1:8000/admin
```

- It will ask for username and password → You need to create a superuser:

```bash
python manage.py createsuperuser
```

When prompted, enter:

- Username
- Email
- Password (You can bypass validation locally by pressing `y`)

**Example Output:**

```plaintext
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
```

✅ Superuser created successfully.

After this, run the server again and log in with your username and password.

Lecture 2:

HttpResponse is used to display a single message only

To render an entire HTML Page we use render method

Lecture 1 Sept:
Restart Django server if image changes do not apply