from django.shortcuts import render

# Create your views here.

def profile(request):
    #render 2 valores, primero el request que le pasamso a la función y segundo el template que queremos devolver
    #path relativo no el completo, ya busca en la carpeta templates
    return render(request,'user/index.html')
