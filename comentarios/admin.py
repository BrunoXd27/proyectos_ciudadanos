from django.contrib import admin

from .models import Comentario
# Register your models here.

class ComentarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text", {"fields": ["contenido", "usuario"]}),
    ]

    list_display = ('contenido', 'fecha_creacion', 'usuario')
    search_fields = ('contenido', 'usuario')
    list_filter = ('usuario', 'fecha_creacion')


admin.site.register(Comentario, ComentarioAdmin)