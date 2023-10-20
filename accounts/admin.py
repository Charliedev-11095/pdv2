from django.contrib import admin
from .models import User, DetallesUsuario, Domicilio

admin.register(User, DetallesUsuario, Domicilio)(admin.ModelAdmin)