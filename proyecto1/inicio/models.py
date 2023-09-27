from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    psw = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Publicacion(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    compartidos = models.IntegerField()
    