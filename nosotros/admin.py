from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Puesto)

class PuestosAdmin(admin.ModelAdmin):
    list_display= ('id', 'puestos')

@admin.register(MisionVision)

class MisionVisionAdmin(admin.ModelAdmin):
    list_display= ('id', 'mision', 'vision')

@admin.register(Integrante)

class IntegrantesAdmin(admin.ModelAdmin):
    list_display= ('id', 'puesto_integrante', 'nombre_integrante')
