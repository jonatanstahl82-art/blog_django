from django import forms
from posts.models import Post

class PostForm(forms.ModelForm): # FORMULARIO DE POST
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'estado', 'imagen']
        