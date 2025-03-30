from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from django.urls import reverse
from django.db.models import F ##F es para hacer queries atomicas, como "UPDATE table SET column = column + 1"

from .models import Propuesta
from votos.models import Voto_Propuesta
from .forms import PropuestaForm
# Create your views here.

class Propuestas_Listado(generic.ListView):
    model = Propuesta
    template_name = 'propuestas/propuestas.html'
    context_object_name = 'propuestas'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:login')  # Redirect to login if not authenticated
        return super().dispatch(request, *args, **kwargs)

class Propuesta_Crear(generic.CreateView):
    model = Propuesta
    form_class = PropuestaForm
    template_name = 'propuestas/propuesta_crear.html'

    def get_success_url(self):
        return reverse('propuestas:propuesta_detalle', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        propuesta = form.save(commit=False)
        propuesta.usuario = self.request.user
        propuesta.save()
        return super().form_valid(form)

class Propuesta_Detalle(generic.DetailView):
    model = Propuesta
    template_name = 'propuestas/propuesta_detalle.html'
    context_object_name = 'propuesta'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        propuesta = self.get_object()  # Obtén la propuesta actual
        user = self.request.user

        # Verificar si el usuario ya votó por esta propuesta
        ya_voto = Voto_Propuesta.objects.filter(propuesta=propuesta, usuario=user).exists()
        context['ya_voto'] = ya_voto  # Agregar al contexto

        return context