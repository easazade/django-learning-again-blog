The path() function is passed four arguments, two required: route and view,
and two optional: kwargs, and name. At this point, read the docs to know more
####################################################################################################
to create a virtual environment in a python project
1- make sure virtualenv module is installed
$ python3 -m pip install --user virtualenv

2- go to project root directory and create a virtual env
$ python3 -m venv env

3- exclude env/ from .gitignore

4- to activate virtual environment 
$ source env/bin/activate

5- to deactivate 
$ deactivate

6- to freeze dependencies 
$ python3 -m pip freeze

7- to install dependencies from requirements.txt file 
python3 -m pip install -r requirements.txt

////also 
pip allows you to specify which version of a package to install using version specifiers. For example, to install a specific version of requests:
$ python3 -m pip install requests==2.18.4

To install the latest 2.x release of requests:
$ python3 -m pip install requests>=2.0.0,<3.0.0

To install pre-release versions of packages, use the --pre flag:
$ python3 -m pip install --pre requests

####################################################################################################
information about settings.py

SECRET_KEY is used for deployment on server

set DEBUG to False when you are deploying your project to server  

####################################################################################################
DTL is the name for django template language - there are other options like jinja
####################################################################################################
to add static files like css, images, js 
- create a static directory in project directory 
- in settings.py add 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

 if you are using images in your model add the MEDIA_ROOT path as well you need to add media path checkout notes for models

- the run command 
$ python manage.py collectstatic

- then to use it in templates you will first load the static tag 
{% load static %}

- then you can access static files like this
<link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}"> 

-extra : we can load static folders as variables in case we needed to use them in templates like this
{% static "icons" as  iconsUrl %}
then we can use them in jinja syntx like in moments like this :
src="{{iconsUrl}}/{{product.icon}}"
in above example product is an object fetched from database
####################################################################################################
to create models in your app first :

- install postgresql using brew 
- install pgadmin using brew 
- run pip install psycopg2
- run pip install pillow. this is needed for working with images in django
- add your databse config in the settings.py like below 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_tut',
        'USER': 'postgres',
        'PASSWORD': '1321',
        'HOST': 'localhost'
    }
} 


- create your model - don't add id by default your will get an id for models in django
- before creating and running migrations make sure you have added your app to INSTALLED_APPS or you will get an error
- run python manage.py makemigrations 
- run python manage.py migrate 

- if you want to see what sql command will run when we apply the migrations run below command 
$ python manage.py sqlmigrate app_label 0001 
0001 is the migration file name 

- if you went to pgadmin and nothing changed try (right click > refresh) the table

- to add your model to django admin panel go to your admin.py of your app and type below code

```python
from .models import Destination
# Register your models here.
admin.site.register(Destination)
```

if you're using images in your model you need to define the MEDIA_ROOT path for your django project in order to upload files 

```python
# if you are using images in your model add the MEDIA_ROOT path as well

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- then change your project  urls.py file to something like this 

```python
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('polls/', include('polls.urls')),
    path('travel/', include('travel.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_RROT)
```
####################################################################################################
to create a superuser for your database 
- python manage.py createsuperuser
####################################################################################################
- to change label of models in admin panel override __str__ method
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################