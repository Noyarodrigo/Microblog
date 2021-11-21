from django import forms
from post.models import Post

class PublicarBlog(forms.ModelForm):
    class Meta:
        #con esta clase django infiere un formulario que satisfaga a lo que encuentre en publicar model
        model = Post
        #limita los campos que se infieren para el form
        fields = ['body','user_id']
        widgets = {'user_id':forms.HiddenInput()}

