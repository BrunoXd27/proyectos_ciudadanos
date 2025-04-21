from django.db import models
from django.contrib.auth.models import User
from versiones.models import Version
from propuestas.models import Propuesta

# Create your models here.

class Voto_Propuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votos_propuesta')
    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE, related_name='votos_propuesta', null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class Voto_Version(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votos_version')
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='votos_version', null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
