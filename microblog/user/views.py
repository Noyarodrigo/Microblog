import email
from email import message
import logging
from multiprocessing import context
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse
from post.models import Post 
from .models import User, Seguidores
from .forms import PublicarBlog, RegistroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.core.mail import send_mail
from django.conf import settings

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

def loginPage(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')
        #user = User(email=e, password=p)
        if User.objects.filter(email=e,password=p):
            #return HttpResponse(User.objects.filter(email=e,password=p))
            #ACA DERIAMOS REDIRECCIONAR AL FEED O AL PERFIL DEL USUARIO
            return HttpResponseRedirect('feed')
    context={}
    return render(request,'user/login.html',context)

def feed(request):
    mensaje="mostrar feed"
    return HttpResponse(mensaje)

def regitroPage(request):
    form=RegistroForm()
    context = {'form':form}
    
    if request.method == 'POST':
         form=RegistroForm(request.POST)
         if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            email_enviador=settings.EMAIL_HOST_USER
            recipient_list=[email]
            subject="Confirmacion de cuenta microblog"
            message="Su cuenta fue confirmada exitosamente!"
            send_mail(subject,message,email_enviador,recipient_list)
            
            messages.success(request, 'Enviamos un mail a ' + email + ", confirma tu cuenta antes de ingresar") 
            return HttpResponseRedirect('login')

            
    return render(request, 'user/registro.html', context)
