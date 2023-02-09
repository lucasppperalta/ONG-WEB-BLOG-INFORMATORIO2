from django.urls import path, include
from .views import *
from . import views

app_name='usuario'

urlpatterns = [
    path('registro/', CrearUsuario.as_view(), name='registro-usuario'),
    
]