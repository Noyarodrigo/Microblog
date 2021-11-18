from django.db import models
from user.models import User 

# Create your models here.

class Post(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=144)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
