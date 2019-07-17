# Django from Scratch
This is a step by step process of creating a basic website using Django framework. As you might know Django is a very powerfull web framework and it allows you to create perfect websites in minimum steps. Here I will be describing each and every aspect of installing, setup and modelling the project for creating your Django based website.

## Prerequisite
You will need 
1. python 3.x (very simple to install on most OS, readily availble in linux and mac. Windows users you can try using Chocolatey Package manager to install python or download the exe from the website.)
2. pip (is a package manager for python)
3. virtualenv (not a must but helps a lot in mentaining all packages in one place)
```
python -m pip install virtualenv
```
* Create virtualenv (please cd to your project before running this)
```
virtualenv env
```
* Activate virtualenv
    * For Linux and Mac
    ```source env/bin/activate```
    * For windows
    ```.\env\Scripts\activate.bat```

## Install and setup Django project
* Install django framework (reminder to activate your env and be inside your project folder before running this).
```
python -m pip install django
```
* Run following command to create a django project.
```
django-admin startproject firstproject .
```
* Start web server
```python manage.py runserver```
Now you can visit your browser at http://localhost:8000/ to check out your first Django project.

Please note that the page you are seeing now is showing because you have ```DEBUG = true``` setup at setting.py file.

## Create a basic blog site
Here we will try to utilze django admin to create a blog site. Each product we add to Django project is know as an APP.

### Creating Django App
#### Step1
Our first step is to create blog app.
```
python manage.py startapp blog
```
#### Step2
Now to inform the project we have an app edit settings.py and add your appname to the INSTALLED_APPS list:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```
#### Step3
Run migration to create database structure for admin page
```
python manage.py migrate
```
#### Step4
To create Django admin (follow the input request to create new super admin)
```
python manage.py createsuperuser
```
This will create Django Admin where you can manage backend related stuffs.
We will come back to this section for doing some more interesting stuffs.
#### Step5
Lets create a view for our blog app. To do that first we need to edit views.py under blog folder.
```
from django.http import HttpResponse
def index(request):
    return HttpResponse("This is a custom response")
```
1. You can include this view on the url pattern of the project folder in urls.py as:
```
from django.contrib import admin
from django.urls import include, path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index")),
]
```
2. Best practice is to create a custom urls.py file in the app folder and add the route as:
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")
]
```
and then add this to the path pattern in the urls.py of the project folder
```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
]
```
* Now if you runserver then you could see custom message set at the blog page.
Notice we have left the first argument of the path function of the urlpatterns as blank.
It means that any request coming on the root page of the application will be redirected to blog views index function.

##### Understanding Url matching
To match or get argument from http url you can create the routes using either path converters (<int:postid>) or regex base url match explained below.

Check the example below:
```
from django.urls import path, re_path

urlpatterns = [
    path('post/<int:postid>', view.post),
    re_path(r'blog/post/(\d+)', view.blogpost),
]
```
```<int:postid>``` is format matching process in path function which evaluates expression inside arrow. Where int, str, uuid, slug some of the accepted data types. The characters after colon (postid in this example) is the name of the variable that will be passed to the function.

```r'^blog/post/(\d+)'``` is a regex based matching where the expression is under parenthesis. This requires including re_path module.


#### Understanding Model and Migration



