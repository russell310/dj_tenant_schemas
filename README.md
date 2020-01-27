# Django 2 project boilerplate

## Follow the steps below

1. Create your virtual environment and activate
2. Install latest version of django using `pip install django`
3. create new project using command below

`django-admin startproject --template=https://github.com/russell310/myproject/archive/master.zip project_name`

4. Install requirements `pip install -r requirements.txt`
5. rename `.env.example` to `.env` with your own setup details 
6. `python manage.py migrate`
7. `python manage.py runserver`

* For strong SECRET_KEY: https://www.miniwebtool.com/django-secret-key-generator/
* For Postgresql replace in .env DATABASE_URL = postgres://username:password@localhost:5432/database_name 
