# Pacific Hotel Booking System

This is a Django-based web application for managing hotel bookings. Users can book rooms, view their bookings, and contact the hotel for inquiries. Admins can manage the system via Django's admin interface.

---

## Prerequisites

Ensure the following are installed on your system:
- Python 3.7 or above
- pip (Python package manager)
- Virtualenv (optional but recommended)
- PostgreSQL or any database supported by Django (optional, defaults to SQLite)

---

## Directory structure:

HELLO/
├── Hello/
├── home/
├── login/
├── static/
├── templates/
├── db.sqlite3
├── manage.py
├── README.md

---

## Installation
- For Windows

1. **Clone the Repository**:
   Download the ZIP folder and extract its contents.

2. **Install Django**
Open Terminal on your Device and run the following command to install django:
    pip install django
Verify using:
    django-admin --version

3. **Make migrations**:
    Run the following commands in your code editor terminal or navigate to this folder in the cmd terminal to create DB models used in this project:

    python manage.py makemigrations
    python manage.py migrate

4. **Run Live Server**
    Run this command on the same terminal. Make sure to keep the root directory as outer 'HELLO'- project folder which contains apps,static folder,manage.py and templates folder.

    python manage.py runserver

5. **Open server on port**

    Ctrl+Click on the port link given in the terminal which shows up after the above steps are successfully executed.

---

## Post Server Execution:

1. A Super User is already created with username and passwords both as 'admin'.
2. Register as new user when the server starts running.
3. Login using the credentials and start using the services.
4. Ctrl+C on the running terminal to stop the live server execution.
---
## Testing

- Run tests written for views and models of this project using:
    python manage.py test
- Run individual test for each app using:
    python manage.py test home
    python manage.py test login
---