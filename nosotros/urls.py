from django.urls import path, include
from . import views
from .views import *


urlpatterns = [

    path('quienes-somos/',views.quienesSomos, name='quienes-somos-puestos'),
]


"""path('quienes-somos/',QuienesSomosPuestos.as_view(), name='quienes-somos-puestos'),
path('quienes-somos/',QuienesSomosIntegrantes.as_view(), name='quienes-somos-integrantes'),
path('quienes-somos/',QuienesSomosMisionVision.as_view(), name='quienes-mision-vision'),"""
    
