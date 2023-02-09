from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

def quienesSomos(request):
    template_name='quienes-somos.html'
    ctx = {}

    ctx['puestos']=Puesto.objects.all()
    ctx['integrantes']=Integrante.objects.all()
    ctx['misionvision']=MisionVision.objects.all()

    return render(request, template_name, context=ctx)

"""class QuienesSomosPuestos(ListView):
    template_name='quienes-somos.html'
    model=Puesto

    def get_queryset(self):
        queryset=self.model.objects.all()
        return queryset
    
class QuienesSomosIntegrantes(ListView):
    template_name='quienes-somos.html'
    model=Integrante

    def get_queryset(self):
        queryset=self.model.object.all()
        return queryset
    


class QuienesSomosMisionVision(ListView):
    template_name='quienes-somos.html'
    model=MisionVision

    def get_queryset(self):
        queryset=self.model.object.all()
        return queryset"""
    

    

