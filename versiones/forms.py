from django import forms
from .models import Version

class Version_Form(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['cambioPropuesta', 'contenido']