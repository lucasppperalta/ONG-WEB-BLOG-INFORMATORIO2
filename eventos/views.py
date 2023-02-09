from django.shortcuts import render
from .models import Evento, Categoria
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.urls.base import reverse_lazy
from django.urls import reverse
from django.views.generic.detail import DetailView
from .forms import EventoFilter
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import *

# Create your views here.

class Calendario(ListView):
    model= Evento
    template_name='calendario-dinamico.html'
    
    

    def get_queryset(self):
        queryset= self.model.objects.all()
        return queryset
    



# Create your views here.
class MostrarEvento(ListView):
    template_name='eventos/detalle-evento.html'
    model=Evento
    paginate_by=3

    def get_queryset(self):
        queryset=self.model.objects.all()
        return queryset

#=================================================================================================
#=================================================================================================

class ConfirmarAsistencia(LoginRequiredMixin, View):

    template_name='eventos/detalle-evento.html'
    model=Evento

    
    def post(self, request, pk, *args, **kwargs):
        post=Evento.objects.get(pk=pk)

        if request.user in post.asistencias.all():
            post.asistencias.remove(request.user)
        
        else:
            post.asistencias.add(request.user)

        
        next =request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class RedirigirEvento(DetailView):
    template_name='evento-seleccionado.html'
    model=Evento


#=================================================================================================
#=================================================================================================

def mostrar_panel(request):
    eventos = Evento.objects.all()
    categorias = Categoria.objects.all()

    template_name='panel/panel.html'

    ctx = {
        'eventos':eventos,
        'categorias':categorias
    }
    return render(request, template_name, context=ctx)


class CrearEvento(CreateView):
    model= Evento
    form_class= EventoForm
    template_name='panel/panel-de-control-eventos.html'

    def get_success_url(self, **kwargs):
        return reverse('evento:panel')



class EventoUpdateView(UpdateView):
    template_name="panel/panel-actualizar-eventos.html"
    model=Evento
    form_class = EventoForm


    def get_success_url(self, **kwargs):
        return reverse('eventos:panel')

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = "panel/panel-borrar.html"

    def get_success_url(self, **kwargs):
        return reverse('eventos:panel')



class CrearCategoria(CreateView):
    model= Categoria
    form_class= CategoriaForm
    template_name='panel/panel-de-control-categorias.html'

    def get_success_url(self, **kwargs):
        return reverse('evento:panel-categorias')


class CategoriaUpdateView(UpdateView):
    template_name="panel/panel-actualizar-categorias.html"
    model=Categoria
    form_class = CategoriaForm

    def get_success_url(self, **kwargs):
        return reverse('eventos:panel')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "panel/panel-borrar.html"

    def get_success_url(self, **kwargs):
        return reverse('eventos:panel')



def lista_eventos(request):
    f = EventoFilter(request.GET, queryset=Evento.objects.all())
    return render(request, 'filtrado.html', {'filter': f})




    
    
    



    
        
