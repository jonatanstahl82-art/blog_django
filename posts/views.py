from django.shortcuts import render



def inicio(request):
    return render(request, 'posts/inicio.html')

def lista_posts(request):
    return render(request, 'posts/lista_posts.html')

def acerca(request):
    return render(request, 'posts/acerca.html')