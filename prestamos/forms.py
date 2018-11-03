from dal import autocomplete

from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ('__all__')
        widgets = {
            'persona': autocomplete.ModelSelect2(url='lector-autocomplete'),
            'libro': autocomplete.ModelSelect2(url='libro-autocomplete')
        }