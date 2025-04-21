from django import forms

from .models import Propuesta

class PropuestaForm(forms.ModelForm):

    class Meta:
        model = Propuesta
        fields = ['titulo', 'descripcion', 'categoria']