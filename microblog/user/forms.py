from cProfile import label
from django import forms
import django
from post import models
from post.models import Post
from user.models import User

class FormBlog(forms.ModelForm):
    class Meta:
        #con esta clase django infiere un formulario que satisfaga a lo que encuentre en publicar model
        model = Post
        #limita los campos que se infieren para el form
        fields = ['body','user_id']
        widgets = {'user_id':forms.HiddenInput()}

    
#class LoginForm(forms.Form):
#    email = forms.EmailField(label="Correo electronico", max_length=100, required=True)
#    password = forms.CharField(label="Clave",widget=forms.PasswordInput, min_length=8, max_length=15 , required=True)

class RegistroForm(forms.ModelForm):
    nombre=forms.CharField(label="Nombre", min_length=4 , max_length=50, required=True)
    apellido=forms.CharField(label="Apellido", min_length=4 , max_length=50, required=True)
    email = forms.EmailField(label="Correo electronico", max_length=100, required=True)
    password = forms.CharField(label="Clave",widget=forms.PasswordInput, min_length=6, max_length=15 , required=True)
    class Meta:
        model = User
        fields = ['nombre','apellido','password','email']
        