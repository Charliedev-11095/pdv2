# Generated by Django 3.2.22 on 2023-10-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vistadatosusuarios',
            fields=[
                ('usuario_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_collation='utf8mb4_general_ci', db_column='Nombre', max_length=100)),
                ('apellido_paterno', models.CharField(db_collation='utf8mb4_general_ci', db_column='Apellido Paterno', max_length=100)),
                ('apellido_materno', models.CharField(db_collation='utf8mb4_general_ci', db_column='Apellido Materno', max_length=100)),
                ('género', models.CharField(db_collation='utf8mb4_general_ci', db_column='Género', max_length=9)),
                ('fecha_de_nacimiento', models.DateField(db_column='Fecha de Nacimiento')),
                ('rol', models.CharField(db_collation='utf8mb4_general_ci', db_column='Rol', max_length=13)),
                ('calle', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='Calle', max_length=100, null=True)),
                ('ciudad', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='Ciudad', max_length=100, null=True)),
                ('estado', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='Estado', max_length=100, null=True)),
                ('país', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='País', max_length=100, null=True)),
                ('teléfono', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='Teléfono', max_length=10, null=True)),
                ('celular', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='Celular', max_length=10, null=True)),
                ('correo_electrónico', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='Correo Electrónico', max_length=250, null=True)),
                ('rfc', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='RFC', max_length=13, null=True)),
                ('razón_social', models.CharField(blank=True, db_collation='utf8mb4_general_ci', db_column='Razón Social', max_length=50, null=True)),
            ],
            options={
                'db_table': 'VistaDatosUsuarios',
                'managed': False,
            },
        ),
    ]