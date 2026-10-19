from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registro, perfil, editar_perfil, eliminar_perfil

urlpatterns = [
    # Rutas de autenticación usando las vistas genéricas de Django
    path('login/', LoginView.as_view(template_name='cuentas_usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='cuentas_usuarios/logout.html'), name='logout'),

    # Rutas propias de tu aplicación
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/eliminar/', eliminar_perfil, name='eliminar_perfil'),
]