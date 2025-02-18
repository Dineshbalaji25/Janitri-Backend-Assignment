# Heart Rate Monitoring System (HRM)

## Overview

The HRM project is a Django-based RESTful API application that manages user accounts, patient records, and heart rate data. It includes endpoints for user registration and login, managing patient information, and recording/retrieving heart rate details. This project leverages Django and Django REST Framework (DRF) for backend development.

## Features

- **User Registration & Login**: Endpoints for creating user accounts and authenticating using email and password.
- **Patient Management**: Endpoints to add patients and retrieve patient details.
- **Heart Rate Data**: Endpoints to record and retrieve heart rate data for patients.
- **RESTful API**: Designed to be consumed by any frontend (web/mobile) or API testing tools (Postman, cURL).

## Prerequisites

- Python 3.x
- Git

## Setup Instructions

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Dineshbalaji25/Janitri-Backend-Assignment.git
cd Janitri-Backend-Assignment


2. Create a Virtual Environment
On Windows:
python -m venv env
env\Scripts\activate

On macOS/Linux:
python3 -m venv env
source env/bin/activate

3. Install Dependencies
If a requirements.txt file already exists, install the dependencies:
pip install -r requirements.txt

4. Apply Migrations
Run the following commands to create the database schema:
python manage.py makemigrations
python manage.py migrate


5. Create a Superuser (Optional)
To access the Django admin panel, create a superuser:
python manage.py createsuperuser
Follow the prompts to enter your email, username, and password.


6. Running the Development Server
Start the server with:
python manage.py runserver
Your application will be available at http://127.0.0.1:8000/.


Project Structure

Janitri-Backend-Assignment/
├── heart_rate/              # Heart rate app (models, views, serializers, urls)
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── hrm/                     # Project settings and urls
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── patients/                # Patients app (models, views, serializers, urls)
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── users/                   # Users app (custom user model, registration, login, etc.)
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py                # Django management script
└── requirements.txt         # List of project dependencies

URL Endpoints
The following API endpoints are available:

Users
Registration: POST /users/register/
Login: POST /users/login/

Patients
Add Patient: POST /patients/add/
Get Patient Details: GET /patients/<patient_id>/

Heart Rate Data
Record Heart Rate Data: POST /heart_rate/add/<patient_id>/
Retrieve Heart Rate Data: GET /heart_rate/<patient_id>/

Running Tests
If you have unit tests, run them using:
python manage.py test


Troubleshooting
ModuleNotFoundError: Ensure all dependencies are installed (check requirements.txt).
Database Issues: Run python manage.py makemigrations and python manage.py migrate if you make model changes.
Authentication Problems: Verify that you are using the correct email and password for login.
