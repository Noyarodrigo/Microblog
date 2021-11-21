from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Seguidores(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    followerid = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.IntegerField()
    createdat = models.DateTimeField(auto_now_add=True)
