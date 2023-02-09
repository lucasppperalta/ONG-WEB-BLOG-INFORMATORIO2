from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth import login, logout
from eventos.models import *

class Inicio(TemplateView):
    template_name='index.html'

class Recursos(TemplateView):
    template_name='recursos.html'

class Contacto(TemplateView):
    template_name='contacto.html'

class MisEventos(TemplateView):
    template_name='mis_eventos.html'

