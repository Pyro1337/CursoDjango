from django.db import models

# Create your models here.
#Procedemos a crear el primer modelo y recordar dentro del class llamar a Models

class Project(models.Model): #Le estamos dando charField como campo texto y longitud de 200, al segundo le damos TextField
    name = models.CharField(max_length=200)
    description = models.TextField()
    #definimos la funcion str
    def __str__(self):
        return self.name

#Creamos ahora la tabla Task para posteriormente relacionarla junto con Project
class Task (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() #le damos textfield con mas longitud
    asigned_to = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField( default = False)
    #models.ForeignKey(Tabla a relacionar, on_delete=models.CASCADE)
    #Para la parte de project utilizamos el modelo ForeignKey para hacer la relacion con la tabla principal "Project"
    #Tener en cuenta que como segundo parametro se utiliza on_delete=models.CASCADE para que al borrar un project se borren sus tareas.

    def __str__(self):
        return self.title