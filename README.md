# File-Manager
A django app to store and manage directory and files.

# Dependencies
* Python == 3.7.3
* Django == 2.2.2
* Pytest == 4.6.4
* Pytest-Django == 3.5.0

# Setup Step
* `git clone https://github.com/nahidsaikat/File-Manager.git`
* `cd File-Manager`
* (run if pipenv is not available) `pip install pipenv`
* `export PIPENV_VENV_IN_PROJECT="enabled"`
* `pipenv install` 
* `pipenv shell`
* `python manage.py migrate`
* `python manage.py createsuperuser`
* `python manage.py runserver 0.0.0.0:8000`
