from django.shortcuts import render
from .models import CalcSqrt

def index(request):
    # Obtém todos os objetos do modelo CalcSqrt
    calc_sqrt_objects = CalcSqrt.objects.all()

    # Cria listas para armazenar os valores de cada coeficiente
    coef_a = [obj.coeficiente_a for obj in calc_sqrt_objects]
    coef_b = [obj.coeficiente_b for obj in calc_sqrt_objects]
    coef_c = [obj.coeficiente_c for obj in calc_sqrt_objects]

    context = {
        'coef_a': coef_a,
        'coef_b': coef_b,
        'coef_c': coef_c,
    }

    return render(request, 'index.html', context)