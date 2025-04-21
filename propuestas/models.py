from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Propuesta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Aprobada', 'Aprobada'), ('Rechazada', 'Rechazada')], default='Pendiente')
    votos = models.IntegerField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='propuestas')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='propuestas')

    def __str__(self):
        return self.titulo
