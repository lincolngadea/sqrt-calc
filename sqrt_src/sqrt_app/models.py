from django.db import models
from decimal import Decimal, getcontext

# Configura a precisão global para cálculos com Decimal
getcontext().prec = 10


class CalcSqrt(models.Model):
    coeficiente_a = models.DecimalField('Coeficiente A', max_digits=10, decimal_places=2)
    coeficiente_b = models.DecimalField('Coeficiente B', max_digits=10, decimal_places=2)
    coeficiente_c = models.DecimalField('Coeficiente C', max_digits=10, decimal_places=2)
    result_sqrt = models.CharField('Resultado', max_length=255, editable=False)

    def clean(self):
        # Valida que coeficiente_a não seja zero
        if self.coeficiente_a == 0:
            raise ValueError("O coeficiente 'a' não pode ser zero.")

    def calculate_roots(self):
        """Calcula as raízes da equação quadrática."""
        discriminant = (self.coeficiente_b ** 2) - (Decimal(4) * self.coeficiente_a * self.coeficiente_c)

        if discriminant > 0:
            # Duas raízes reais
            root1 = (-self.coeficiente_b + discriminant.sqrt()) / (2 * self.coeficiente_a)
            root2 = (-self.coeficiente_b - discriminant.sqrt()) / (2 * self.coeficiente_a)
            return f"duas raízes reais, {root1:.1f} e {root2:.1f}"
        elif discriminant == 0:
            # Uma raiz real
            root = -self.coeficiente_b / (2 * self.coeficiente_a)
            return f"uma raiz real, {root:.1f}"
        else:
            # Sem raízes reais
            return "sem raízes reais"

    def save(self, *args, **kwargs):
        # Calcula o resultado antes de salvar
        self.result_sqrt = self.calculate_roots()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"a: {self.coeficiente_a}, b: {self.coeficiente_b}, c: {self.coeficiente_c}, resultado: {self.result_sqrt}"