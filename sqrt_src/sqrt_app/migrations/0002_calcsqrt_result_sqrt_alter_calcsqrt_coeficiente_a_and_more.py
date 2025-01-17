# Generated by Django 5.1.4 on 2025-01-16 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqrt_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcsqrt',
            name='result_sqrt',
            field=models.CharField(default=0, editable=False, max_length=255, verbose_name='Resultado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calcsqrt',
            name='coeficiente_a',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Coeficiente A'),
        ),
        migrations.AlterField(
            model_name='calcsqrt',
            name='coeficiente_b',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Coeficiente B'),
        ),
        migrations.AlterField(
            model_name='calcsqrt',
            name='coeficiente_c',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Coeficiente C'),
        ),
    ]
