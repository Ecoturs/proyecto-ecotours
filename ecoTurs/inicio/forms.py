from django import forms
from .models import Recorrido, PreInscripcion


class RecorridoForm(forms.ModelForm):
    class Meta:
        model = Recorrido
        fields = ['nombre', 'fecha', 'estado', 'ciudad', 'costo', 'imagen', 'descripcion']


class PreInscripcionForm(forms.ModelForm):
    class Meta:
        model = PreInscripcion
        fields = ['nombre', 'correo', 'telefono', 'ciudad', 'estado']