from django.contrib.auth.models import User 
from django.db import models

# Create your models here.

class Perfil(models.Model): # Modelo para almacenar información adicional del usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField(max_length=700, blank=True)
    avatar = models.ImageField(
        upload_to='avatars/', 
        null=True, 
        blank=True,
        default='media/def_avatar/avatar_def.svg')

    def __str__(self):
        return self.user.username
