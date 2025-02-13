from django.http import HttpResponse, JsonResponse
# importamos de models los modelos Project y Task
from .models import Project, Task
# Este es el import para el 404 not found
from django.shortcuts import get_object_or_404
# Importamos el render para las paginas html
from django.shortcuts import render, redirect
from .forms import CreateNewTask,CreateNewProject  # Importamos el formulario


def index(request):
    # return HttpResponse("¡Hola, bienvenido a mi sitio esta es la seccion de inicio!")
    return render(request, 'home.html')
    # Pagina About


def about(request):
    author = "Ivan Sanchez"
    # return HttpResponse("Esta es la página 'About'.")
    return render(request, 'about.html', {
        'author': author
    })

    # Saludo inicial


def hello(request, username):
    return HttpResponse(f"¡Hola, {username}!")

    # Muestra todos los proyectos


def showProjects(request):
    # return JsonResponse(list(Project.objects.values()), safe=False)
    # return JsonResponse(list(ModeloInicial.Objects.values()), safe = False) para que me muestre los valores que contiene en forma de Lista
    projects = Project.objects.all()
    return render(request, './projects/projects.html', {
        'projects': projects
    })

    # Muestra un proyecto basado en su ID


def showSpecificProject(request, identifier):
    # specific_project = Project.objects.get(id = identifier) metodo sin usar get_object_or_404
    specific_project = get_object_or_404(Project, id=identifier)
    return HttpResponse('<h2>Proyecto : '+specific_project.name+' </h2>'+'Numero proyecto: '+str(specific_project.id)+'<br>Description: '+specific_project.description)

    # Muestra todas las tareas


def showTasks(request):
    # return JsonResponse(list(Task.objects.values()), safe=False)
    projects = Project.objects.all()
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'projects': projects,
        'tasks': tasks
    })

    # Muestra una tarea basado en su ID


def showSpecificTasks(request, identifier):
    # specific_task =  Task.objects.get(id = identifier) #Aqui obtenemos con el ID el registro que esta en Task sin usar el get_object_or_404
    specific_task = get_object_or_404(Task, id=identifier)
    return HttpResponse('<h2>Lista de Tareas</h2>'+'<br>Title: ' + specific_task.title+"<br>Description: "+specific_task.description+"<br>Asigned to: "+specific_task.asigned_to
                        + "<br>Project: "+specific_task.project.name)


def create_task(request):
    # En caso que se desee mostrar al usuario la pantalla de carga es esta:
    if request.method == 'GET':
        return render(request, './tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        # En caso que se ejecute un post
        form = CreateNewTask(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                asigned_to=request.POST['asigned_to'],
                project_id=1
            )
            return redirect('task/')
        else:
            return render(request, 'tasks/create_task.html', {
                'form': form,
                'error': 'Formulario inválido'
            })
            
 #Para la creacion de proyectos           
def create_project(request):
    # En caso que se desee mostrar al usuario la pantalla de carga es esta:
    if request.method == 'GET':
        return render(request, './projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        # En caso que se ejecute un post
        form = CreateNewProject(request.POST)
        if form.is_valid():
            Project.objects.create(
                name=request.POST['name'],
                description=request.POST['description'],
            )
            return redirect('projects/')
        else:
            return render(request, 'projects/create_projects.html', {
                'form': form,
                'error': 'Formulario inválido'
            })
