from django.shortcuts import render,HttpResponse
from post.models import Post 
from .models import User, Seguidores
# Create your views here.

def profile(request,id):
    #render 2 valores, primero el request que le pasamso a la función y segundo el template que queremos devolver
    #path relativo no el completo, ya busca en la carpeta templates

    #posts = Post.objects.filter(user_id = id) 
    posts = Post.objects.all()
    return render(request,'user/index.html', {'posts':posts, 'id':id})

def seguidos(request, id):
    seguidos = Seguidores.objects.filter(followerid=id).select_related('followerid').get().order_by('createdat')
    print(seguidostmp)
    for seguido in seguidos:
        print(seguido.followerid.nombre)
    return render(request,'user/seguidos.html', {'seguidos':seguidos, 'id':id})

def seguidores(request,id):
    seguidores = Seguidores.objects.filter(user=id).select_related('followerid').all().order_by('createdat')
    return render(request,'user/seguidos.html', {'seguidos':seguidores, 'id':id})
