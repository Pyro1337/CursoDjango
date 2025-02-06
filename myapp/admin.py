from django.contrib import admin
from .models import Project, Task #importamos los modelos[Tablas] Project y Task

# Register your models here.
#Aqui enlazamos al panel admin de la siguiente forma
admin.site.register(Project)
admin.site.register(Task)