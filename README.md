# Django Task List Application

This is a simple task list application built with Django that allows users to add, filter, and sort tasks by priority and due date.

## Features

- Create tasks with a title, description, due date, priority, and status.
- Filter tasks by status and sort by priority or due date.

## Prerequisites

- Python
- Django

## Installation and Setup without Docker

1. **Clone the repository:**

   ```bash
    git clone https://github.com/zeddkhan03/django-tasklist.git
    cd django-tasklist

2. **Create a virtual environment:**

   ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install the required dependencies:**

   ```bash
    pip install -r requirements.txt
   
4. **Apply database migrations:**

   ```bash
    python3 manage.py migrate

5. **Run the application:**

   ```bash
    python3 manage.py runserver

6. **Access the app:**

    Open your browser and go to `http://127.0.0.1:8000/tasks/` to view the application.

7. **To run the unit tests, use:**

   ```bash
    python3 manage.py test

## License
  This project is licensed under the MIT License. Feel free to modify and use it for your own purposes.


