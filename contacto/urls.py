from django.urls import path,include
from . import views

urlpatterns=[
    path('contacto/',views.contacto, name='contacto')

]