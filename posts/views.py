from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from posts.forms import PostForm


def inicio(request):    # Vista para la página de inicio
    return render(request, 'posts/inicio.html')

def lista_posts(request): # Vista para la lista de posts
    posts = Post.objects.filter(estado="publicado").order_by("fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)

def acerca(request): # Vista para la página "Acerca de"
    return render(request, 'posts/acerca.html')

def post_form(request): # Vista para crear un nuevo post
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'posts/inicio.html')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', post_id=post.id)  # Redirección tras guardado exitoso
    else:
        form = PostForm(instance=post)
        
    # Renderizado para mostrar el formulario (GET o POST con errores)
    return render(request, 'posts/post_form.html', {'form': form, 'es_edicion': True})

def post_confirm_delete(request, post_id): # Vista para eliminar un post existente
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        post.delete()
        return redirect('lista_posts')  # Redirección tras eliminación exitosa
    else:
        return render(request, 'posts/post_confirm_delete.html', {'post': post})

def detalle_post(request, post_id): # Vista para ver los detalles de un post
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detalle_post.html', {'post': post})
