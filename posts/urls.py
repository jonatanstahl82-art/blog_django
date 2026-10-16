from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('acerca/', views.acerca, name='acerca'),
    path('crear/', views.post_form, name='post_form'),
    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('eliminar/<int:post_id>/', views.post_confirm_delete, name='post_confirm_delete'),
    path('detalle/<int:post_id>/', views.detalle_post, name='detalle_post'),

]