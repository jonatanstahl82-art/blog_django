# Blog Django 📝

Proyecto final de aplicación web desarrollada con **Django**. Permite a los usuarios registrarse, gestionar sus publicaciones con soporte multimedia, personalizar su perfil y administrar la plataforma.


## 🚀 Funcionalidades Principales

### 📰 Gestión de Publicaciones (App `posts`)
* **CRUD Completo:** Creación, lectura (listado general y detalle individual), edición y eliminación de publicaciones.
* **Soporte Multimedia:** Carga y renderizado de imágenes asociadas a cada post.
* **Validación de Autoría:** Solo el autor de la publicación (o un superusuario) tiene permisos para editarla o eliminarla.

### 👤 Cuentas y Perfiles (App `cuentas_usuarios`)
* **Autenticación Completa:** Registro de usuarios, inicio (`LoginView`) y cierre de sesión (`LogoutView`).
* **Perfil Extendido (`Perfil` model):**
  * Vinculación `OneToOneField` con la cuenta de usuario.
  * Campos para **Biografía**, **Página Web** y **Avatar**.
  * Asignación automática de avatar por defecto (`.svg`) cuando el usuario no adjunta foto.
* **Edición y Eliminación de Cuenta:** Gestión de datos personales y borrado de cuenta con confirmación previa.
* **Administración de Usuarios:** Vistas exclusivas para que los administradores puedan inspeccionar perfiles ajenos y gestionar cuentas desde el frontend.

### 🛡️ Seguridad y Permisos
* Protección de rutas mediante decoradores `@login_required` (auetenticación requerida) y `@user_passes_test`. (usuario administrador requerido)
* Pantalla de **Acceso Denegado** (`error_permisos.html`) con redirección automática si un usuario intenta modificar contenido no autorizado.

---

## 📁 Estructura del Proyecto

blog_project/
│
├── blog_project/                      # Configuración principal del proyecto (settings, urls, etc.)
├── posts/                             # App para publicaciones (modelos, vistas, formularios, templates)
│   └── templates/posts/               # Plantillas: detalle_post, post_form, post_confirm_delete, error_permisos
├── cuentas_usuarios/                  # App para autenticación y perfiles
│   └── templates/cuentas_usuarios/    # Plantillas: login, registro, perfil, editar_perfil, etc.
├── media/                             # Archivos multimedia subidos por usuarios (avatares e imágenes)
├── static/                            # Estilos CSS generales y recursos estáticos
├── db.sqlite3                         # Base de datos local
├── manage.py
└── requirements.txt

🛠️ Instalación y Configuración
Clonar el repositorio:


git clone [https://github.com/jonatanstahl82-art/blog_django.git](https://github.com/jonatanstahl82-art/blog_django.git)
cd blog_django
Crear y activar el entorno virtual:

Windows (PowerShell):


python -m venv venv
.\venv\Scripts\Activate.ps1
Linux / macOS:


python -m venv venv
source venv/bin/activate
Instalar dependencias:


pip install -r requirements.txt
Aplicar migraciones:


python manage.py migrate
Ejecutar el servidor de desarrollo:


python manage.py runserver
Abrir en el navegador:
Ingresar a http://127.0.0.1:8000/

⚙️ Configuración de Archivos Multimedia (Media)
Para permitir el manejo de imágenes en entorno de desarrollo (DEBUG = True), se configuraron los siguientes parámetros:

settings.py:

Python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
blog_project/urls.py:

Python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


