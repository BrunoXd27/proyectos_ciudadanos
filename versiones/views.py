from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Version
from propuestas.models import Propuesta
from votos.models import Voto_Version
from .forms import Version_Form

# Create your views here.
    
class Crear_Version_Desde_Propuesta(generic.CreateView):
    '''
    Vista para crear una nueva versión a partir de una propuesta.
    Se utiliza una vista genérica para manejar la creación de la versión.
    Se utiliza el modelo Version y la plantilla version_crear.html.
    '''
    model = Version
    template_name = 'versiones/version_crear.html'
    form_class = Version_Form

    def get_success_url(self):
        return reverse('versiones:version_detalle', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Retrieve the propuesta using the pk from the URL
        propuesta_id = self.kwargs['pk']
        propuesta = get_object_or_404(Propuesta, pk=propuesta_id)
        # Save the version with the associated propuesta and user
        version = form.save(commit=False)
        version.propuesta = propuesta
        version.usuario = self.request.user
        version.save()
        return super().form_valid(form)
    
class Crear_Version_Desde_Version(generic.CreateView):
    '''
    Vista para crear una nueva versión a partir de una version.
    Se utiliza una vista genérica para manejar la creación de la versión.
    Se utiliza el modelo Version y la plantilla version_crear.html.
    '''
    model = Version
    template_name = 'versiones/version_crear.html'
    form_class = Version_Form

    def get_success_url(self):
        return reverse('versiones:version_detalle', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Retrieve the propuesta using the pk from the URL
        version_id = self.kwargs['pk']
        parent_version = get_object_or_404(Version, pk=version_id)
        # Save the version with the associated propuesta and user
        version = form.save(commit=False)
        version.parent_version = parent_version
        version.usuario = self.request.user
        version.save()
        return super().form_valid(form)
    
class Version_Detalle(generic.DetailView):
    model = Version
    template_name = 'versiones/version_detalle.html'
    context_object_name = 'version'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        version = self.get_object()
        user = self.request.user
        # Check if the version has a parent version or comes from a propuesta
        if version.parent_version:
            context['origen'] = version.parent_version  # Add the parent version as the origin
            context['origen_tipo'] = 'version'
        else:
            context['origen'] = version.propuesta  # Add the propuesta as the origin
            context['origen_tipo'] = 'propuesta'

        # Verificar si el usuario ya votó por esta propuesta
        ya_voto = Voto_Version.objects.filter(version=version, usuario=user).exists()
        context['ya_voto'] = ya_voto  # Agregar al contexto

        return context
    