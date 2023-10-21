from django.contrib import admin
from .models import DetallesUsuario, Domicilio

admin.register(DetallesUsuario, Domicilio)(admin.ModelAdmin)