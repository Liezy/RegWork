from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={
                'placeholder': 'Digite o conteúdo do registro aqui...',
                'rows': 4,
                'class': 'w-full p-4 border rounded shadow-sm',
            })
        }