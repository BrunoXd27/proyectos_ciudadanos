from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('crear/propuesta/<int:propuesta_id>/', views.Crear_Comentario.as_view(), name='crear_comentario_propuesta'),
    path('crear/version/<int:version_id>/', views.Crear_Comentario.as_view(), name='crear_comentario_version'),
    path('responder/<int:parent_id>/', views.Crear_Comentario.as_view(), name='responder_comentario'), 
]