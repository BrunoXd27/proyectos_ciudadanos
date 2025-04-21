from django.contrib import admin

from .models import Propuesta, Categoria
from versiones.models import Version

# Register your models here.

class VersionesInLine(admin.TabularInline): ##TabularInline es para mostrar los objetos en forma de tabla, es decir, uno al lado del otro
    model = Version

class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text", {"fields": ["nombre", "descripcion"]}),
    ]

class PropuestaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text", {"fields": ["titulo", "descripcion", "usuario", "categoria"]}),
        ("Status", {"fields": ["estado"]}),
        ("Votes", {"fields": ["votos"]}),
    ]

    inlines = [VersionesInLine]
    list_display = ('titulo', 'fechaCreacion', 'estado', 'usuario', 'categoria', 'votos')
    search_fields = ('titulo', 'descripcion', 'usuario')
    list_filter = ('estado', 'categoria', 'usuario', 'fechaCreacion')

admin.site.register(Propuesta, PropuestaAdmin)

admin.site.register(Categoria, CategoriaAdmin)

# admin.site.register(Comentario, ComentarioAdmin)

# admin.site.register(Version, VersionAdmin)