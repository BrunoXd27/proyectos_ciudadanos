from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que realiza el comentario
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Tipo de contenido (Propuesta o Version)
    object_id = models.PositiveIntegerField(null=True)  # ID del objeto relacionado (Propuesta o Version)
    content_object = GenericForeignKey('content_type', 'object_id')  # Relación genérica
    contenido = models.TextField()  # Contenido del comentario
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del comentario
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')  # Comentario padre (para respuestas)

    class Meta:
        ordering = ['-fecha_creacion']  # Ordenar por fecha de creación (más reciente primero)

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.content_object} \n {self.contenido}"