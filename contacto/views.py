from http.client import HTTPResponse
from django.shortcuts import render
from .models import Contacto
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def contacto(request):
    next=request.POST.get('next', '/')
    if request.method == 'POST':
        contacto = Contacto()
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        mensaje=request.POST.get('mensaje')
        contacto.nombre=nombre
        contacto.email=email
        contacto.mensaje=mensaje
        contacto.save()
        messages.success(request, 'Recibimos tu mensaje, te responderemos en breve!')
        
        return HttpResponseRedirect(next)
    
    return render(request,'contacto.html')
