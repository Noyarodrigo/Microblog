from django.shortcuts import render,HttpResponse
from post.models import Post 
from .models import User, Seguidores
from .forms import PublicarBlog

def profile(request,id):
    #render 2 valores, primero el request que le pasamso a la función y segundo el template que queremos devolver
    #path relativo no el completo, ya busca en la carpeta templates
    posts = Post.objects.filter(user_id = id).order_by('-created_at')
    return render(request,'user/index.html', {'posts':posts, 'id':id})

def seguidores(request,id):
    seguidores = Seguidores.objects.filter(user=id).select_related('followerid').all().order_by('createdat')
    return render(request,'user/seguidores.html', {'seguidores':seguidores, 'id':id})

def publicar(request,id):
    if request.method == 'GET':
        publicar_form = PublicarBlog()
        return render(request, 'user/publicar.html', {'form':publicar_form, 'id':id})
    else:
        publicar_form = PublicarBlog(data = request.POST)
        if publicar_form.is_valid:
            if len(request.POST.get('body')) < 144 and len(request.POST.get('body')) > 0:
                publicar_form.save()
                status = 'True'
            else:
                status = 'False' 
        return render(request, 'user/confirmar_publicacion.html', {'status':status, 'id':id})

