# Generated by Django 3.2.22 on 2023-10-23 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetallesUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], max_length=9, verbose_name='género')),
                ('birth_date', models.DateField()),
                ('role', models.CharField(max_length=100)),
                ('domicilio', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.domicilio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]