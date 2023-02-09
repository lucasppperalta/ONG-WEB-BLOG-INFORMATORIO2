from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    telefono=models.CharField(max_length=255, null=True, blank=True)
    #imagen_perfil=models.ImageField(upload_to='imagen-perfil', null=True, blank=True)