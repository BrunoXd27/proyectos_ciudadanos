from django.urls import path, include
from . import views

app_name = 'propuestas'

urlpatterns = [
    path('', views.Propuestas_Listado.as_view(), name='propuestas_listado'),
    path('crear/', views.Propuesta_Crear.as_view(), name='crear_propuesta'),
    path('<int:pk>/', views.Propuesta_Detalle.as_view(), name='propuesta_detalle'),
]