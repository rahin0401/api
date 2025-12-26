install python version 3.17+ (and install it )
then in cmd 
  python -m venv env
  env\scripts\activate
  pip install django djangorestframework pillow
  cd project
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  
