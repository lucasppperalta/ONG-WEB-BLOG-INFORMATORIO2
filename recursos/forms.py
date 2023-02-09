from dataclasses import field
from pyexpat import model
from django import forms
from .models import Recursos

class RecursosForm(forms.ModelForm):
    class Meta:
        model=Recursos
        fields= '__all__'