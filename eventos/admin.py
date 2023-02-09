from django.contrib import admin
from  . models import Categoria, Evento

# Register your models here.
@admin.register(Evento)

class EventoAdmin(admin.ModelAdmin):
    list_display=('id','titulo_evento','fecha_inicio_evento','fecha_fin_evento')
    search_fields=('titulo_evento','fecha_inicio_evento','fecha_fin_evento')
    list_editable=('titulo_evento',)
    list_filter=('fecha_inicio_evento','fecha_fin_evento')
    exclude=('asistencias',)

@admin.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('id','nombre_categoria')
    list_editable=('nombre_categoria',)
