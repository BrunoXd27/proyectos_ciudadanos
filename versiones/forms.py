from django import forms
from .models import Version

class Version_Form(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['cambioPropuesta', 'contenido']
        labels = {
            'cambioPropuesta': 'Descripción del cambio',
            'contenido': 'Contenido',
        }
        widgets = {
            'cambioPropuesta': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe el cambio propuesto...'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Escribe el contenido aquí...'
            }),
        }