from django.shortcuts import render,HttpResponse
from post.models import Post 
from .models import User
# Create your views here.

def profile(request,id):
    #render 2 valores, primero el request que le pasamso a la función y segundo el template que queremos devolver
    #path relativo no el completo, ya busca en la carpeta templates

    #posts = Post.objects.filter(user_id = id) 
    posts = Post.objects.all()
    return render(request,'user/index.html', {'posts':posts, 'id':id})

def seguidos(request,id):
    #seguidos = User.Seguidores.objects.filter(user_id = id)
    seguidos = User.objects.select_related('user_id')

    return render(request,'user/seguidos.html', {'seguidos':seguidos, 'id':id})

def seguidores(request,id):
    #seguidos = User.Seguidores.objects.filter(user_id = id)
    seguidos = User.objects.select_related('id', 'user_id')

    return render(request,'user/seguidos.html', {'seguidos':seguidos},id)
