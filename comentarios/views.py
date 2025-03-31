from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.views import generic, View

from .models import Comentario
from propuestas.models import Propuesta
from versiones.models import Version
from .forms import Comentario_Form

# Create your views here.

# Crear un comentario para una propuesta
class Crear_Comentario(View):
    '''
    Crea un nuevo comentario para una propuesta o una versión.
    '''
    def post(self, request, *args, **kwargs):
        form = Comentario_Form(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Propuesta if 'propuesta_id' in kwargs else Version)
            object_id = kwargs.get('propuesta_id') or kwargs.get('version_id')
            parent_id = kwargs.get('parent_id')

            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.content_type = content_type
            comentario.object_id = object_id
            if parent_id:
                comentario.parent = get_object_or_404(Comentario, pk=parent_id)
            comentario.save()
                        # Redirigir al detalle correspondiente
            if 'propuesta_id' in kwargs:
                return redirect('propuestas:propuesta_detalle', pk=object_id)
            elif 'version_id' in kwargs:
                return redirect('versiones:version_detalle', pk=object_id)
        return redirect('propuestas:propuesta_detalle', pk=object_id)  # Redirige al detalle
