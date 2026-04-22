from django.contrib import admin
from .models import Recorrido, PreInscripcion


class AdministrarRecorrido(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('nombre', 'fecha', 'estado', 'ciudad', 'costo')
    search_fields = ('nombre', 'ciudad', 'estado', 'descripcion')
    date_hierarchy = 'created'
    list_filter = ('estado',)


admin.site.register(Recorrido, AdministrarRecorrido)


class AdministrarPreInscripcion(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('nombre', 'correo', 'recorrido', 'created')
    search_fields = ('nombre', 'correo')
    date_hierarchy = 'created'
    list_filter = ('estado',)


admin.site.register(PreInscripcion, AdministrarPreInscripcion)