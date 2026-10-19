from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Importaciones de tu propia app (nota el punto antes de forms y models)
from .forms import FormularioRegistro, PerfilForm
from .models import Perfil

from posts.models import Post  # Asegúrate de que la ruta sea correcta según tu estructura de proyecto

def registro(request): # Vista para manejar el registro de nuevos usuarios
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('login')  # Redirige al usuario a la página de login después del registro
    else:
        form = FormularioRegistro()
    return render(request, 'cuentas_usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    perfil_usuario, created = Perfil.objects.get_or_create(user=request.user)  # Obtiene o crea un perfil para el usuario actual
    posts_usuario = Post.objects.filter(autor=request.user)
    return render(request, 'cuentas_usuarios/perfil.html', {'perfil': perfil_usuario, 'posts': posts_usuario})

@login_required
def editar_perfil(request):
    perfil_usuario, created = Perfil.objects.get_or_create(user=request.user)  # Obtiene o crea un perfil para el usuario actual
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirige al usuario a su perfil después de guardar los cambios
    else:
        form = PerfilForm(instance=perfil_usuario)  # Crea un formulario con los datos actuales del perfil
    return render(request, 'cuentas_usuarios/editar_perfil.html', {'form': form}) 

@login_required
def eliminar_perfil(request):
    # Obtenemos el perfil de forma segura para pasarlo al HTML
    perfil_usuario, created = Perfil.objects.get_or_create(user=request.user)  

    if request.method == 'POST':
        user = request.user
        user.delete()  # Esto borra al usuario y en cascada a su perfil
        return redirect('inicio')  # Asegurate de tener una ruta 'home' o cambiala por la que uses
        
    # Le pasamos el perfil al contexto para que lo puedas usar en eliminar_perfil.html
    return render(request, 'cuentas_usuarios/eliminar_perfil.html', {'perfil': perfil_usuario})