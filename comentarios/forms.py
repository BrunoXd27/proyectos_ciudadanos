from django import forms
from .models import Comentario

class Comentario_Form(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']