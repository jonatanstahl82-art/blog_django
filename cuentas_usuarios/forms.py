from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cuentas_usuarios.models import Perfil

class FormularioRegistro(UserCreationForm): # Formulario de registro personalizado que hereda de UserCreationForm
    email = forms.EmailField(required=True) # Campo de correo electrónico obligatorio
    biografia = forms.CharField(widget=forms.Textarea, required=False) # Campo de biografía opcional con un área de texto

    class Meta: # Especifica el modelo y los campos para el formulario
        model = User
        fields = ('username', 'email')

    def clean_email(self): # Validación para asegurarse de que el correo electrónico sea único
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

    def save(self, commit=True): # Sobrescribe el método save para crear un perfil de usuario al registrar un nuevo usuario
        user = super().save(commit=False) # Crea una instancia del usuario sin guardarla en la base de datos aún  
        user.email = self.cleaned_data['email'] # Asigna el correo electrónico al usuario
        if commit:
            user.save()
            biografia_creada = self.cleaned_data.get('biografia', '') # Obtiene la biografía del formulario, si está presente
            Perfil.objects.create(user=user, biografia=biografia_creada) # Crea un perfil asociado al usuario
            
        return user

class PerfilForm(forms.ModelForm): # Formulario para editar el perfil del usuario
    class Meta:
        model = Perfil
        fields = ['biografia', 'avatar',] # Campos del perfil que se pueden editar