# Django Student Dashboard

## 📌 Project Overview

This project is a simple **Django-based Student Dashboard** developed during my Week 6 internship tasks.

The project started with a basic Django setup and gradually developed into a dashboard that combines:

* Django project and app structure
* MVT (Model-View-Template) architecture
* Django Models
* SQLite database
* Django Admin Panel
* Views and URLs
* HTML Templates
* Student Dashboard
* CSV data
* Pandas DataFrame operations
* Displaying processed data on a Django webpage

The purpose of the project was to understand how Django works from the basic project setup to displaying dynamically processed data on a webpage.

---

# 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML**
* **Pandas**
* **CSV**
* **Django Admin Panel**

---

# 📁 Project Structure

The final project contains the following main structure:

```text
myproject/
│
├── manage.py
├── db.sqlite3
│
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    │
    ├── read_csv.py
    ├── students.csv
    │
    ├── migrations/
    │   ├── __init__.py
    │   ├── 0001_initial.py
    │   ├── 0002_task_delete_myapp.py
    │   └── 0003_remove_task_completed_remove_task_created_at.py
    │
    └── templates/
        └── myapp/
            └── dashboard.html
```

The project also contains automatically generated `__pycache__` files.

---

# 🚀 Project Development

## Day 1 — Django Setup and First App

The project was initially created using Django.

The basic Django project structure was generated with:

```bash
django-admin startproject myproject
```

After creating the project, the application was created:

```bash
python manage.py startapp myapp
```

The application was then connected to the Django project through `settings.py`.

The project introduced the basic **MVT architecture**:

```text
Model
  ↓
View
  ↓
Template
```

I also worked with Django URLs to connect browser requests to views.

The main purpose of this stage was to understand the difference between a Django **project** and a Django **app**, and how Django handles a request from the browser.

---

# 🗄️ Day 2 — Models, SQLite and Django Admin

The second stage introduced database functionality.

A Django model was created in:

```text
myapp/models.py
```

The model acted as a blueprint for storing application data.

Django's built-in **SQLite database** was used for the project:

```text
db.sqlite3
```

The database structure was created and updated using migrations:

```bash
python manage.py makemigrations
```

and:

```bash
python manage.py migrate
```

The project also used Django's Admin Panel to manage database records.

A superuser was created using:

```bash
python manage.py createsuperuser
```

The model was registered in:

```text
myapp/admin.py
```

This allowed records to be added, edited and viewed through:

```text
http://127.0.0.1:8000/admin/
```

### Main concepts covered

* Django Models
* ORM
* Migrations
* SQLite
* Superuser
* Django Admin Panel
* Database records

---

# 🌐 Day 3 — Views, Templates and Dashboard

The third stage focused on connecting Python logic with an HTML webpage.

The main view was created in:

```text
myapp/views.py
```

The application URLs were defined in:

```text
myapp/urls.py
```

The HTML template was placed inside:

```text
myapp/templates/myapp/dashboard.html
```

The view renders the dashboard template and passes information to it.

The dashboard contains student-related information such as:

```text
Name
Course
Semester
Tasks
```

Django template variables were used to display information dynamically.

For example:

```html
<p><strong>Name:</strong> {{ name }}</p>
```

This demonstrated how information from a Django view can be displayed inside an HTML template.

---

# 📊 CSV and Pandas Integration

The project was later extended to work with student data stored in a CSV file.

The CSV file is:

```text
myapp/students.csv
```

The project also contains:

```text
myapp/read_csv.py
```

which was used for reading and processing CSV data with Pandas.

The basic Pandas process was:

```python
import pandas as pd

df = pd.read_csv("students.csv")
```

The CSV data was loaded into a Pandas **DataFrame**.

Basic DataFrame operations were used to inspect and process the student data.

Examples include:

```python
df.head()
```

```python
df.tail()
```

```python
df.shape
```

```python
df.columns
```

The processed records could then be converted into a format that Django templates could display.

---

# 📋 Student CSV Data

The project uses student information containing fields such as:

```text
Name
Course
Marks
Semester
```

Example:

| Name  | Course | Marks | Semester |
| ----- | ------ | ----: | -------: |
| Addan | BSCS   |    85 |        1 |
| Ali   | BSCS   |    78 |        1 |
| Ahmed | BSCS   |    92 |        1 |
| Usman | BSCS   |    74 |        1 |
| Hamza | BSCS   |    88 |        1 |

This data is loaded from the CSV and displayed on the Django dashboard.

---

# 🔗 Django + Pandas Integration

The final part of the project combines Django and Pandas.

The overall flow is:

```text
students.csv
     ↓
   Pandas
     ↓
  DataFrame
     ↓
Data Processing
     ↓
Django View
     ↓
HTML Template
     ↓
Student Dashboard
```

The Pandas records are passed from the Django view to the template.

The template then uses a Django loop to display each student.

For example:

```html
{% for student in students %}

<tr>
    <td>{{ student.name }}</td>
    <td>{{ student.course }}</td>
    <td>{{ student.marks }}</td>
    <td>{{ student.semester }}</td>
</tr>

{% endfor %}
```

This allows the dashboard to display multiple student records without manually writing every row in HTML.

---

# 📈 Dashboard

The final dashboard combines the information developed during the different stages of the project.

It contains:

### Student Information

* Name
* Course
* Semester

### Student Data

* Student name
* Course
* Marks
* Semester

### Dashboard Statistics

The dashboard can also display processed information such as:

* Total number of students
* Average marks
* Highest marks

The dashboard therefore demonstrates how raw CSV data can be processed and presented through a Django webpage.

---

# 🔄 Overall Application Flow

The complete project can be understood through this flow:

```text
User opens website
       ↓
Django URL
       ↓
Django View
       ↓
       ├── Student information
       │
       ├── SQLite database
       │
       └── CSV → Pandas → DataFrame
                    ↓
              Processed data
                    ↓
              Django Context
                    ↓
             HTML Template
                    ↓
             Student Dashboard
```

---

# 📚 What I Practiced

During the development of this project, I practiced:

1. Creating a Django project
2. Creating a Django application
3. Understanding MVT architecture
4. Working with `manage.py`
5. Configuring Django settings
6. Creating URLs
7. Creating views
8. Creating HTML templates
9. Passing data from views to templates
10. Creating Django models
11. Creating migrations
12. Working with SQLite
13. Creating a Django superuser
14. Using the Django Admin Panel
15. Managing database records
16. Reading CSV files
17. Using Pandas
18. Working with DataFrames
19. Processing student data
20. Passing processed data to Django templates
21. Creating a basic student dashboard

---

# 🐛 Debugging and Problems Faced

Several practical errors occurred while developing the project.

### `manage.py` Not Found

This occurred when Django commands were executed from a directory that did not contain `manage.py`.

The solution was to move to the correct project directory before running commands.

---

### `django-admin` Not Recognized

The `django-admin` command was initially not recognized in PowerShell.

The Django/Python environment and command setup had to be checked before continuing with project creation.

---

### `ModuleNotFoundError`

A project-name mismatch caused Django to search for a module that did not exist.

The project configuration was corrected so that the configured project package matched the actual project folder.

---

### `TemplateDoesNotExist`

Django displayed:

```text
TemplateDoesNotExist
```

when the template could not be found.

The problem was solved by placing the template in the correct application template directory and making sure the path used by `render()` matched the actual file location.

---

### `ValueError: Empty module name`

This occurred because of an incorrect application configuration in `INSTALLED_APPS`.

The Django settings were checked and corrected.

---

### Dashboard Data Disappearing

When new Pandas/CSV functionality was added, some previously existing dashboard content disappeared.

The problem was caused by replacing the previous dashboard structure instead of combining the old and new data.

The solution was to pass all required information together through the Django context.

---

# 🎯 Final Outcome

The project progressed from a basic Django installation to a functional student dashboard.

The final application demonstrates how different technologies can work together:

```text
Python
   +
Django
   +
SQLite
   +
HTML
   +
CSV
   +
Pandas
   ↓
Student Dashboard
```

The project gave me practical experience with Django's MVT architecture, database management, the Django Admin Panel, templates, views, CSV files, Pandas DataFrames and displaying processed data through a web application.

---

# ▶️ How to Run the Project

Open the terminal in the directory containing `manage.py`.

Run:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

For the Django Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

# 👨‍💻 Project Status

**Status:** Completed

**Project:** Django Student Dashboard

**Main Purpose:** Learning Django development and integrating Pandas/CSV data into a Django webpage.

**Week:** Week 6 Internship

**Days Covered:** Day 1, Day 2, Day 3 and Day 5

**Main Technologies:** Python, Django, SQLite, HTML, Pandas and CSV.
