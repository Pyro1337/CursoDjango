from django.http import HttpResponse, JsonResponse
from .models import Project,Task #importamos de models los modelos Project y Task
from django.shortcuts import get_object_or_404 #Este es el import para el 404 not found
from django.shortcuts import render #Importamos el render para las paginas html
def index(request):
    return HttpResponse("¡Hola, bienvenido a mi sitio esta es la seccion de inicio!")
    #Pagina About
def about(request):
    author = "Ivan Sanchez"
    #return HttpResponse("Esta es la página 'About'.")
    return render(request,'about.html',{
        'author' : author
    })

    #Saludo inicial
def hello(request,username):
    return HttpResponse(f"¡Hola, {username}!")

    #Muestra todos los proyectos
def showProjects(request):
    #return JsonResponse(list(Project.objects.values()), safe=False)
    #return JsonResponse(list(ModeloInicial.Objects.values()), safe = False) para que me muestre los valores que contiene en forma de Lista
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects' : projects
    })

    #Muestra un proyecto basado en su ID
def showSpecificProject(request, identifier):
    #specific_project = Project.objects.get(id = identifier) metodo sin usar get_object_or_404
    specific_project = get_object_or_404(Project, id = identifier)
    return HttpResponse('<h2>Proyecto : '+specific_project.name+' </h2>'+'Numero proyecto: '+str(specific_project.id)+'<br>Description: '+specific_project.description)  

    #Muestra todas las tareas
def showTasks(request):
    #return JsonResponse(list(Task.objects.values()), safe=False)
    projects = Project.objects.all()
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{
        'projects' : projects,
        'tasks' : tasks
    })

    #Muestra una tarea basado en su ID
def showSpecificTasks(request,identifier):
    #specific_task =  Task.objects.get(id = identifier) #Aqui obtenemos con el ID el registro que esta en Task sin usar el get_object_or_404
    specific_task = get_object_or_404(Task, id = identifier)
    return HttpResponse('<h2>Lista de Tareas</h2>'+'<br>Title: ' +specific_task.title+"<br>Description: "+specific_task.description+"<br>Asigned to: "+specific_task.asigned_to
                        +"<br>Project: "+specific_task.project.name)


