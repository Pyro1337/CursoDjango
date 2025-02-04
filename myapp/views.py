from django.http import HttpResponse, JsonResponse
from .models import Project,Task #importamos de models los modelos Project y Task
def index(request):
    return HttpResponse("¡Hola, bienvenido a mi sitio esta es la seccion de inicio!")

def about(request):
    return HttpResponse("Esta es la página 'About'.")

def hello(request,username):
    return HttpResponse(f"¡Hola, {username}!")

def showProject(request):
    return JsonResponse(list(Project.objects.values()), safe=False)
    #return JsonResponse(list(ModeloInicial.Objects.values()), safe = False) para que me muestre los valores que contiene en forma de Lista

def showTasks(request,identifier):
    specific_task =  Task.objects.get(id = identifier) #Aqui obtenemos con el ID el registro que esta en Task
    return HttpResponse('<h2>Lista de Tareas</h2>'+'<br>Title: ' +specific_task.title+"<br>Description: "+specific_task.description+"<br>Asigned to: "+specific_task.asigned_to
                        +"<br>Project: "+specific_task.project.name)    

