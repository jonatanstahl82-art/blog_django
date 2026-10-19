from django.contrib import admin
from posts.models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'estado')
    list_display_links = ('titulo', 'autor')
    list_filter = ('estado', 'fecha_creacion', 'autor')
    search_fields = ('titulo', 'autor__username')
    ordering = ('fecha_creacion',)
    readonly_fields = ('fecha_creacion',)
