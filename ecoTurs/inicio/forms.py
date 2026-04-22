from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recorrido, PreInscripcion, Opinion


class RecorridoForm(forms.ModelForm):
    class Meta:
        model = Recorrido
        fields = ['nombre', 'fecha', 'estado', 'ciudad', 'costo', 'imagen', 'descripcion']


class PreInscripcionForm(forms.ModelForm):
    class Meta:
        model = PreInscripcion
        fields = ['nombre', 'correo', 'telefono', 'ciudad', 'estado']


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OpinionForm(forms.ModelForm):
    calificacion = forms.ChoiceField(
        choices=[(i, f'{"★" * i}') for i in range(1, 6)],
        label="Calificación"
    )

    class Meta:
        model = Opinion
        fields = ['comentario', 'calificacion']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escribe tu opinión aquí...'
            }),
        }
        labels = {
            'comentario': 'Comentario',
        }