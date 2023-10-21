from django.db import models
from django.contrib.auth.models import User


class DetallesUsuario(models.Model):
    GENDER_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ]
    nickname = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(("género"),max_length=9, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField()
    role = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    accion=models.CharField(max_length=100)
    domicilio =models.ForeignKey('Domicilio', on_delete=models.CASCADE, null=False, blank=True)
    
    def __str__(self):
        return self.full_name
    
class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.calle

