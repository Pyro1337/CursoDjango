"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import hello,about,index,showProjects,showTasks,showSpecificProject,showSpecificTasks,create_task,create_project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('about/',about,name='about'),
    path('projects/',showProjects,name='projects'),
    path('task/',showTasks,name='tasks'),
    path('create_new_task',create_task,name='create_task'),
    path('create_new_project',create_project,name='create_project'),
    #path('projects/<int:identifier>',showSpecificProject),
    #path('hello/<str:username>',hello,name='hello'),
    #path('task/<int:identifier>',showSpecificTasks),
]
