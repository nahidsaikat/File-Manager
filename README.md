# File-Manager
A django app to store and manage directory and files.

# Dependencies
#### Main
* Python == 3.7.3
* Django == 2.2.2
#### Test
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
#
* `pytest` for running test

# Screen Shots
* Folder Create Interface
![Folder Create](https://raw.githubusercontent.com/nahidsaikat/File-Manager/master/docs/images/create_folder.png)


* File Create Interface
![File Create](https://raw.githubusercontent.com/nahidsaikat/File-Manager/master/docs/images/create_file.png)


* Folder View Interface 1
![Folder View](https://raw.githubusercontent.com/nahidsaikat/File-Manager/master/docs/images/view_folder_1.png)


* Folder View Interface 2
![Folder View](https://raw.githubusercontent.com/nahidsaikat/File-Manager/master/docs/images/view_folder_2.png)


# License
[MIT](https://github.com/nahidsaikat/File-Manager/blob/master/LICENSE)

Copyright (c) 2020 [MD. Nahidur Rahman](https://nahidsaikat.com/)
