from django import forms
from .models import CalcSqrt

class CalcSqrtForm(forms.ModelForm):
    class Meta:
        model = CalcSqrt
        fields = ('coeficiente_a', 'coeficiente_b', 'coeficiente_c')