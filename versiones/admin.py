from django.contrib import admin

from .models import Version
# Register your models here.

class VersionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text", {"fields": ["cambioPropuesta", "contenido", "usuario", "propuesta", 'parent_version']}),
    ]

    list_display = ('cambioPropuesta', 'fechaCreacion', 'usuario', 'propuesta', 'parent_version')
    search_fields = ('cambioPropuesta', 'contenido', 'usuario', 'propuesta')
    list_filter = ('usuario', 'propuesta', 'fechaCreacion')


admin.site.register(Version, VersionAdmin)