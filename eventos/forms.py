import django_filters
from .models import Evento, Categoria
from django import forms
#from pyexpat import model

class EventoForm(forms.ModelForm):
    class Meta:
        model=Evento
        managed = True
        fields=['autor_evento','titulo_evento','fecha_inicio_evento','fecha_fin_evento','hora_evento','modalidad_evento','descripcion_evento','foto','id_categoria','asistencias']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        managed = True
        fields=['nombre_categoria',]
        
    

class EventoFilter(django_filters.FilterSet):

    class Meta:
        model = Evento
        fields = ['id_categoria']