from django.urls import path
from . import views

app_name = 'versiones'
urlpatterns = [
    path('crear/propuesta/<int:pk>/', views.Crear_Version_Desde_Propuesta.as_view(), name='crear_version_desde_propuesta'),
    path('crear/version/<int:pk>/', views.Crear_Version_Desde_Version.as_view(), name='crear_version_desde_version'),
    path('<int:pk>/', views.Version_Detalle.as_view(), name='version_detalle'),
]