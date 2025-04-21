from django.urls import path
from . import views

app_name = 'votos'
urlpatterns = [
    path('propuesta/<int:pk>/', views.voto_propuesta, name='voto_propuesta'),
    path('version/<int:pk>/', views.voto_version, name='voto_version'),
]