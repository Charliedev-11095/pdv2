# Generated by Django 3.2.22 on 2023-10-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20231024_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datospersonales',
            name='full_name',
        ),
        migrations.AddField(
            model_name='datospersonales',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Apellido Materno'),
        ),
    ]