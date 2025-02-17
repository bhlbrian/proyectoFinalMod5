# Generated by Django 5.0.7 on 2024-07-25 13:44

import django.db.models.deletion
import gestionBiblioteca.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBiblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, validators=[gestionBiblioteca.validators.validar_nombre]),
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prestatario', models.CharField(max_length=100, validators=[gestionBiblioteca.validators.validar_nombre])),
                ('fecha_prestamo', models.DateTimeField()),
                ('fecha_devolucion', models.DateTimeField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionBiblioteca.libro')),
            ],
        ),
    ]
