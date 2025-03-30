from django.contrib import admin

from .models import Propuesta, Categoria

# Register your models here.

# class VersionesInLine(admin.TabularInline): ##TabularInline es para mostrar los objetos en forma de tabla, es decir, uno al lado del otro
#     model = Version

# class VersionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Text", {"fields": ["cambioPropuesta", "contenido", "usuario", "propuesta"]}),
#     ]

#     list_display = ('cambioPropuesta', 'contenido', 'fechaCreacion', 'usuario', 'propuesta')
#     search_fields = ('cambioPropuesta', 'contenido', 'usuario', 'propuesta')
#     list_filter = ('usuario', 'propuesta', 'fechaCreacion')

# class ComentariosInLine(admin.TabularInline):
#     model = Comentario

# class ComentarioAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Text", {"fields": ["contenido", "usuario", "propuesta"]}),
#     ]

#     list_display = ('contenido', 'fechaCreacion', 'usuario', 'propuesta')
#     search_fields = ('contenido', 'usuario', 'propuesta')
#     list_filter = ('usuario', 'propuesta', 'fechaCreacion')

class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text", {"fields": ["nombre", "descripcion"]}),
    ]

class PropuestaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text", {"fields": ["titulo", "descripcion", "usuario", "categoria"]}),
        ("Status", {"fields": ["estado"]}),
    ]

    # inlines = [VersionesInLine]
    # inlines = [ComentariosInLine, VersionesInLine]
    list_display = ('titulo', 'fechaCreacion', 'estado', 'usuario')
    search_fields = ('titulo', 'descripcion', 'usuario')
    list_filter = ('estado', 'categoria', 'usuario', 'fechaCreacion')

admin.site.register(Propuesta, PropuestaAdmin)

admin.site.register(Categoria, CategoriaAdmin)

# admin.site.register(Comentario, ComentarioAdmin)

# admin.site.register(Version, VersionAdmin)