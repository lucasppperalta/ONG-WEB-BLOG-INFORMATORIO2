from django.db import models


# Create your models here.

class Puesto(models.Model):
    puestos=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.puestos}: '
    

class Integrante(models.Model):
    puesto_integrante=models.OneToOneField(Puesto,verbose_name='Puesto', on_delete=models.CASCADE)
    nombre_integrante=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.puesto_integrante} {self.nombre_integrante}'

class MisionVision(models.Model):
    mision=models.TextField()
    vision=models.TextField()

    def __str__(self):
        return f'{self.mision} {self.vision}'
