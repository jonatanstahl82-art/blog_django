from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages


from .forms import FormularioRegistro, PerfilForm
from .models import Perfil
from posts.models import Post


def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioRegistro()
    return render(request, 'cuentas_usuarios/registro.html', {'form': form})

#A PARTIR DE ACA ESTAN LAS FUNCIONES QUE REQUIEREN AUTENTICACION
@login_required
def perfil(request, user_id=None):  
    if user_id and request.user.is_superuser:
        usuario_ver = get_object_or_404(User, id=user_id)
    else:
        usuario_ver = request.user

    perfil_usuario, created = Perfil.objects.get_or_create(user=usuario_ver)
    posts_usuario = Post.objects.filter(autor=usuario_ver)

    context = {
        'perfil': perfil_usuario,
        'perfil_user': usuario_ver,
        'posts': posts_usuario,
        'es_propio_perfil': (usuario_ver == request.user),
    }

    if request.user.is_superuser:
        context['todos_los_usuarios'] = User.objects.all().order_by('username')

    return render(request, 'cuentas_usuarios/perfil.html', context)


@login_required
def editar_perfil(request):
    perfil_usuario, created = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil_usuario)
    return render(request, 'cuentas_usuarios/editar_perfil.html', {'form': form}) 


@login_required
def eliminar_perfil(request):
    perfil_usuario, created = Perfil.objects.get_or_create(user=request.user)  

    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('inicio')
        
    return render(request, 'cuentas_usuarios/eliminar_perfil.html', {'perfil': perfil_usuario})

# A PARTIR DE ACA ESTAN LAS FUNCIONES ADMIN
def es_admin(user):
    return user.is_authenticated and user.is_superuser


@login_required
@user_passes_test(es_admin)
def lista_usuarios(request):
    usuarios = User.objects.all().order_by('-date_joined')
    return render(request, 'cuentas_usuarios/lista_usuarios.html', {'usuarios': usuarios})


@login_required
@user_passes_test(es_admin)
def eliminar_usuario_admin(request, user_id): 
    usuario = get_object_or_404(User, id=user_id)
    
    if usuario == request.user:
        messages.error(request, "No podés eliminar tu propia cuenta desde este panel.")
        return redirect('lista_usuarios')

    if request.method == 'POST':
        usuario.delete()
        messages.success(request, f"El usuario '{usuario.username}' fue eliminado correctamente.")
        return redirect('lista_usuarios')

    return render(request, 'cuentas_usuarios/usuario_confirm_delete.html', {'usuario_borrar': usuario})