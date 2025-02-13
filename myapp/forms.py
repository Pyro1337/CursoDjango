from django import forms

class CreateNewTask(forms.Form) :
    title =  forms.CharField(label="Titulo de la tarea", max_length=200)
    description = forms.CharField(label= "Descripcion de la tarea",
                                  widget = forms.Textarea)
    asigned_to = forms.CharField(label="Asignado a", max_length=200)
    
#Crear Proyecto
class CreateNewProject(forms.Form):
    name = forms.CharField(label= "Nombre del proyecto: ",max_length= 150)
    description = forms.CharField(label= "Descripción del proyecto: ", widget = forms.Textarea)