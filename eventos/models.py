from django.db import models
from usuario.models import Usuario

#Creamos la tabla de caterías a parte para poder filtrar después.
class Categoria(models.Model):
    nombre_categoria=models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre_categoria}'


# Creamos la tabla de eventos con sus respectivos campos.
class Evento(models.Model):
    autor_evento=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo_evento=models.CharField(max_length=50)
    fecha_inicio_evento=models.DateField()
    fecha_fin_evento=models.DateField()
    hora_evento=models.CharField(max_length=5)
    modalidad_evento=models.CharField(max_length=50)
    descripcion_evento=models.TextField()
    foto=models.ImageField(null=True,blank=True, upload_to='fotos-eventos')
    id_categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    asistencias=models.ManyToManyField(Usuario, blank=True, related_name='asistencias')
    
    

    def __str__(self):
        return f'{self.titulo_evento} {self.fecha_inicio_evento} {self.fecha_fin_evento} {self.hora_evento} {self.modalidad_evento} {self.descripcion_evento}'
