from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# URLS DE CUENTAS DE USUARIO
urlpatterns = [
    # Rutas de autenticación
    path('login/', LoginView.as_view(template_name='cuentas_usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='cuentas_usuarios/logout.html'), name='logout'),

    # Rutas de usuario y perfil
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<int:user_id>/', views.perfil, name='ver_perfil_admin'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/eliminar/', views.eliminar_perfil, name='eliminar_perfil'),
    
    # Rutas de administración de usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:user_id>/eliminar/', views.eliminar_usuario_admin, name='eliminar_usuario_admin'),
]