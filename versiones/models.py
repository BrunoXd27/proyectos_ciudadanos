from django.db import models
from django.contrib.auth.models import User
from propuestas.models import Propuesta

# Create your models here.
class Version(models.Model):
    cambioPropuesta = models.TextField(default='')
    contenido = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Aprobada', 'Aprobada'), ('Rechazada', 'Rechazada')], default='Pendiente', null=True)
    votos = models.IntegerField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='versiones')
    #la version viene de una propuesta
    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE, related_name='versiones', null=True, blank=True)
    # o la version viene de otra version
    parent_version = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_versions')

    def __str__(self):
        return f"{self.cambioPropuesta} (ID: {self.id})"