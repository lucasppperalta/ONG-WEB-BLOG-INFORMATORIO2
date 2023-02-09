
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Recursos
from .forms import RecursosForm


def recursos(request):
    recursos=Recursos.objects.all()
    return render(request, 'recursos.html', {'recursos':recursos})


def crear(request):
    formulario=RecursosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('recursos')
    return render(request, 'crear.html', {'formulario':formulario})


def editar(request, id):
    recursos=Recursos.objects.get(id=id)
    formulario=RecursosForm(request.POST or None, request.FILES or None, instance=recursos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('recursos')

    return render(request, 'editar.html', {'formulario':formulario})


def eliminar(request, id):
    recursos=Recursos.objects.get(id=id)
    recursos.delete()
    return redirect('recursos')

    