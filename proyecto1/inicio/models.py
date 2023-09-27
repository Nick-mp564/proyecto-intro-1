from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    psw = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Publicacion(models.Model):
    title = models.CharField(max_length=50)
    shared = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)