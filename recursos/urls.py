from urllib import request
from django.urls import path, include
from .views import *
from . import views
from recursos import views





urlpatterns=[
    path('recursos', views.recursos, name='recursos'),
    path('recursos/crear', views.crear, name= 'crear'),
    path('recursos/editar', views.crear, name= 'editar'),
    path('eliminar/<int:id>', views.eliminar, name= 'eliminar'),
    path('recursos/editar/<int:id>', views.editar, name= 'editar'),
]
 
 
 