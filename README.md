# Student Entry Application

## Overview

This project is a fully functional CRUD application designed for managing student records. The application features AJAX integration for seamless data retrieval and manipulation, and a user authentication module allowing registration, login, and logout functionalities. It is built using Django for the backend and Bootstrap for the frontend.

## Features

- **CRUD Functionality:**
  - Create: Allow staff users to add new student details.
  - Read: Enable staff users to view a list of existing student records and individual student details.
  - Update: Provide the ability to edit and update student information.
  - Delete: Allow staff users to remove student records from the database.

- **AJAX Integration:**
  - Seamless data retrieval and manipulation without reloading the entire web page.
  
- **User Authentication:**
  - Custom registration model for staff users.
  - Registration: Staff users can register, but need to be activated by a super admin.
  - Login: Only active staff users can log in.
  - Logout: Secure logout functionality.

- **Admin Dashboard:**
  - Super admin can activate/deactivate staff users from the admin dashboard.

- **Frontend:**
  - Designed with Bootstrap for a responsive and user-friendly interface.

## Application Structure

- **Backend:**
  - Python with Django framework.
  - Database: SQLite3 (default Django database).
  - Models: Custom user model for staff registration, Student model for student data.

- **Frontend:**
  - HTML, CSS, JavaScript.
  - AJAX with jQuery for asynchronous operations.
  - Bootstrap for styling.

## How to Run the Application Locally

### Prerequisites

- Python
- Django
- pip (Python package installer)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DanishIrfan1/CRUD-Operations-with-AJAX-Custom-Authentication.git
   cd CRUD-Operations-with-AJAX-Custom-Authentication
   ```
2. **Create and Activate a Virtual Environment:**
```bash
python -m venv .venv
.venv\Scripts\activate  # On Mac use `source venv/bin/activate`
```
3. **Install the Required Packages:**
```bash
pip install -r requirements.txt
```
4. **Apply Migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```
5. **Create a Superuser:**
```bash
python manage.py createsuperuser
```
6. **Run the Development Server:**
```bash
python manage.py runserver
```
7. **Access the Application:**
- Open a web browser and go to http://127.0.0.1:8000/.
- Log in to the admin dashboard at http://127.0.0.1:8000/admin/ to activate staff users.
