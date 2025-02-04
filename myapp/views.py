from django.http import HttpResponse

def hello(request):
    return HttpResponse("¡Hola, bienvenido a mi sitio!")

def about(request):
    return HttpResponse("Esta es la página 'About'.")
