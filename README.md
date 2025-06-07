# ToDo_project
A full-stack ToDo List web application built with **Django (Backend)** and **HTML, CSS, Bootstrap (Frontend)**. 
Includes user authentication, task management with CRUD operations, and is designed with a clean, responsive UI.

## Features

- User Registration & Login (with JWT tokens)
- Create, View, Update, and Delete tasks
- Group tasks by **due date** and **completion status**
- Responsive UI using Bootstrap
- Role-based authentication & secure 

## Setup Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Apply Migrations & Run Server
python manage.py migrate
python manage.py runserver
