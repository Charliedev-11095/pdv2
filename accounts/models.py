from django.db import models
from django.contrib.auth.models import User


class DetallesUsuario(models.Model):
    GENDER_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ]
    ROLE_CHOICES = [
        ('administrador', 'Administrador'),
        ('vendedor', 'Vendedor'),
        ('cliente', 'Cliente'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(("nombre completo"),max_length=100, blank=True)
    phone = models.CharField(("teléfono"),max_length=10, blank=True)
    gender = models.CharField(("género"),max_length=9, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField()
    role = models.CharField(("rol"),max_length=13, choices=ROLE_CHOICES, blank=True)
    domicilio =models.ForeignKey('Domicilio', on_delete=models.CASCADE, null=False, blank=True)
    
    def __str__(self):
        return self.full_name
    
class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    
    def __str__(self):
        return self.calle
    


