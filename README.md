# Blog Django
Proyecto base de un blog web desarrollado con Django.
## Descripción
Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.  
Incluye la configuración base del proyecto y una aplicación llamada `posts`.
## Instalación
Clonar el repositorio:
```bash
git clone https://github.com/jonatanstahl82-art/blog_django.git
```
Entrar a la carpeta del proyecto:
```
cd blog_django
```
Crear entorno virtual:
python -m venv venv
Activar entorno virtual:
En Windows PowerShell:
```
.\venv\Scripts\Activate.ps1
```
En Linux o macOS:
```
source venv/bin/activate
```
Instalar dependencias:
```
pip install -r requirements.txt
```
Ejecutar el servidor:
```
python manage.py runserver
```
Abrir en el navegador:
http://127.0.0.1:8000/
Aplicaciones
- posts: aplicación inicial para manejar las publicaciones del blog.

# Actualizacion del blog!
se agregaron estilos con css y la navegacion por urls

# Actualización  Preentrega 10: CRUD de Posts con Imágenes en Django

## Cambios en la estructura
    se afgregaron archivos necesarios para las funciones CRUD
        posts/templates/posts/detalle_post.html
        posts/templates/posts/post_form.html
        posts/templates/posts/post_confirm_delete.html
        posts/forms.py

## Cómo Probar la Carga de Imágenes y el CRUD Completo

1. Crear un Post con Imagen:
   - Navega a la sección Crear Post.
   - Completa los campos obligatorios y adjunta un archivo de imagen en el campo correspondiente.
   - Presiona Publicar. Serás redirigido a la lista general donde podrás visualizar la tarjeta del post con su imagen renderizada.

2. Editar un Post y Modificar su Imagen:
   - En la lista de posts, haz clic en el botón Editar de cualquier publicación.
   - Selecciona una nueva imagen o modifica los datos del formulario y guarda los cambios.

3. Ver Detalle del Post:
   - Haz clic en Ver Detalle para corroborar la vista individual de la publicación junto a su imagen en tamaño completo.

4. Eliminar un Post:
   - Haz clic en el botón Eliminar y confirma la acción en la pantalla de confirmación.

## Configuración de Archivos Multimedia (Media)

Para permitir que los usuarios puedan subir y visualizar imágenes en las publicaciones, se realizaron las siguientes configuraciones:

1. Ajustes en settings.py:
   Se definieron las constantes para la gestión de archivos cargados por el usuario:
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'

2. Configuración de URLs para Entorno de Desarrollo:
   En blog_project/urls.py se habilitó el servicio de archivos estáticos y multimedia durante la fase de desarrollo (DEBUG = True):
   from django.conf import settings
   from django.conf.urls.static import static

   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Actualización Preentrega 11: Autenticación, Usuarios y Perfiles en Django

## Cambios en la estructura
    se agregaron archivos necesarios para las funciones CRUD
        posts/templates/posts/detalle_post.html
        posts/templates/posts/post_form.html
        posts/templates/posts/post_confirm_delete.html
        posts/forms.py


En esta preentrega se implementó el sistema de cuentas de usuario, separando la lógica en una nueva aplicación llamada `cuentas_usuarios` para mantener el proyecto ordenado y escalable.

## 🚀 Nuevas Funcionalidades

1. **Gestión de Usuarios (App `cuentas_usuarios`):**
   * **Registro:** Los usuarios nuevos pueden crearse una cuenta desde la página de registro.
   * **Login / Logout:** Sistema seguro de inicio y cierre de sesión.
   * **Perfil de Usuario:** Cada usuario tiene su propia página de perfil donde puede ver sus datos y una lista de los posts que publicó.
   
2. **Modelo de Perfil Extendido:**
   * Se creó el modelo `Perfil` vinculado al usuario de Django (OneToOneField).
   * Permite agregar una **Biografía** y subir un **Avatar** (imagen de perfil).
   * Si el usuario no sube una foto, el sistema asigna automáticamente un avatar `.svg` por defecto.

3. **Edición y Eliminación de Cuentas:**
   * Los usuarios logueados pueden editar su biografía y cambiar su avatar.
   * Implementación de borrado de cuenta con pantalla de confirmación por seguridad.

## 🛡️ Seguridad y Protección de Rutas

Se implementaron restricciones para proteger el contenido:
* Se utilizó `@login_required` para que solo los usuarios registrados puedan crear posts o acceder a su perfil.
* **Validación de Autores:** Si un usuario intenta editar o eliminar un post que no le pertenece, el sistema bloquea la acción, muestra una pantalla de "Acceso Denegado" con diseño personalizado y lo redirige automáticamente a la lista de posts en 3 segundos.

## 🧪 Cómo probar el panel de administración

Se incluye la base de datos `db.sqlite3` para facilitar la corrección. 
Para ingresar al panel de administración (`/admin`) y verificar los modelos registrados, pueden utilizar el siguiente superusuario de prueba:

* **Usuario:** jonatanstahl
* **Contraseña:** asqw12zx

