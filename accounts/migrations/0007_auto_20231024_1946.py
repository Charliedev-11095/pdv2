# Generated by Django 3.2.22 on 2023-10-24 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20231024_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empleado', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(blank=True, max_length=100, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(blank=True, max_length=100, verbose_name='Apellido Materno')),
                ('genero', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], max_length=9, verbose_name='género')),
                ('birth_date', models.DateField()),
                ('role', models.CharField(blank=True, choices=[('administrador', 'Administrador'), ('vendedor', 'Vendedor'), ('cliente', 'Cliente')], max_length=13, verbose_name='rol')),
                ('datos_contacto', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.datoscontacto')),
                ('datos_fiscales', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.datosfiscales')),
                ('domicilio', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.domicilio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dato Personal',
                'verbose_name_plural': 'Datos Personales',
            },
        ),
        migrations.RemoveField(
            model_name='usuariosacceso',
            name='datos_contacto',
        ),
        migrations.RemoveField(
            model_name='usuariosacceso',
            name='datos_personales',
        ),
        migrations.RemoveField(
            model_name='usuariosacceso',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='datos_contacto',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='datos_fiscales',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='datos_personales',
        ),
        migrations.AddField(
            model_name='clientes',
            name='id_cliente',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='DatosPersonales',
        ),
        migrations.AddField(
            model_name='empleados',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.usuario'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.usuario'),
        ),
        migrations.AlterField(
            model_name='movimientoscaja',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.empleados'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.empleados'),
        ),
        migrations.DeleteModel(
            name='UsuariosAcceso',
        ),
    ]
