from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db.models import F ##F es para hacer queries atomicas, como "UPDATE table SET column = column + 1"

from .models import Voto_Propuesta, Voto_Version
from propuestas.models import Propuesta
from versiones.models import Version

# Create your views here.
def voto_propuesta(request, pk):
    if not request.user.is_authenticated:
        return redirect('home:login')
    
    propuesta = get_object_or_404(Propuesta, pk=pk)

    voto, created = Voto_Propuesta.objects.get_or_create(usuario=request.user, propuesta=propuesta)
    #el created es True si el voto no existia, y False si ya existia de acuerdo al usuario y la propuesta

    if created:
        propuesta.votos = F('votos') + 1
        propuesta.save()
        return redirect('propuestas:propuesta_detalle', pk=pk)
    else:
        return redirect('propuestas:propuesta_detalle', pk=pk)
    
def voto_version(request, pk):
    if not request.user.is_authenticated:
        return redirect('home:login')
    
    version = get_object_or_404(Version, pk=pk)

    voto, created = Voto_Version.objects.get_or_create(usuario=request.user, version=version)
    #el created es True si el voto no existia, y False si ya existia de acuerdo al usuario y la propuesta

    if created:
        version.votos = F('votos') + 1
        version.save()
        return redirect('versiones:version_detalle', pk=pk)
    else:
        return redirect('versiones:version_detalle', pk=pk)