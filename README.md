Django mysite

Django mysite: A very simple Task Management web app written with Django Admin.
Features

    Simple task manager that allows to define a tasks with title, description, responsible of the task, priority...
    Each task may have items: sub-tasks to be done.
    The built-in Django Authentication and Authorization system to manage users and groups, login, etc.

    Requirements

    Python 3.5+ (tested with Python 3.6).
    Django 2.1 and other dependencies declared in the requirements.txt file (use virtual environments!).
    A Django compatible database like PostgreSQL (by default uses the Python's built-in SQLite database for development purpose).

Install and Run

(Optional) Create a virtual environment and activate it with:

$ python3 -m venv .venv && source .venv/bin/activate

Install dependencies with:

$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt       # For DEV environments

Create the database with:

$ python3 manage.py makemigrations
$ python3 manage.py makemigrations mtasks
$ python3 manage.py migrate

To create an admin user:

$ python3 manage.py createsuperuser

Then run in development mode with:

$ python3 manage.py runserver

Or use the script to startup in the same mode:

$ ./run.sh dev

Some settings can be overwritten with environment variables. For example to overwrite the language translations of the application and set debug options to false:

$ DEBUG=False LANGUAGE_CODE=es-ar python3 manage.py runserver

Available settings to override are:

    DEBUG: set the Django DEBUG option. Default True.
    TIME_ZONE: default UTC. Other example: America/Buenos_Aires.
    LANGUAGE_CODE: default en-us. Other example: es-ar.
    SITE_HEADER: Header title of the app. Default to "Django mysite - A Simple Task Manager".
    DATABASE_URL: Database string connection. Default uses SQLite database. Other example: postgresql://dmysite:postgres@localhost/dmysite_dev.

To run in a production environment, check the README-production.rst notes, or see the official Django documentation.
Access the application

Like any Django app developed with Django Admin, enter with: http://localhost:8000/admin
Development

Some tips if you are improving this application.
Translations

After add to the source code new texts to be translated, execute from the root folder (replace LANG by a valid language code like es):

$ django-admin makemessages -l LANG

Then go to the .po file and add the translations. Finally execute to compile the locales:

$ django-admin compilemessages

Oldest Django versions

The master branch works with Django 2.1. The are two more branches:

    django/2.0
    django/1.11

With the source code that works for each version of Django, and maybe tweaking some configurations can works with oldest versions too.
