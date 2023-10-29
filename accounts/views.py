from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Usuario
import json

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def dashboard(request):
    return render(request, "dashboard.html")


from django.http import JsonResponse
from .models import Vistadatosusuarios

def listaUsuarios(request):
    # Consulta la vista de datos de usuarios
    datos_usuarios = Vistadatosusuarios.objects.all()

    # Convierte los datos en una lista de diccionarios
    data = [{'usuario_id': item.usuario_id,
             'Nombre': item.nombre,
             'Apellido Paterno': item.apellido_paterno,
             'Apellido Materno': item.apellido_materno,
             'Género': item.género,
             'Fecha de Nacimiento': item.fecha_de_nacimiento.strftime('%Y-%m-%d'),
             'Status': '<div class="badge bg-success text-white rounded-pill">Activo</div>' if item.status else '<div class="badge bg-danger text-white rounded-pill">Inactivo</div>',
             'Rol': item.rol,
             'Calle': item.calle,
             'Ciudad': item.ciudad,
             'Estado': item.estado,
             'País': item.país,
             'Teléfono': item.teléfono,
             'Celular': item.celular,
             'Correo Electrónico': item.correo_electrónico,
             'RFC': item.rfc,
             'Razón Social': item.razón_social}
            for item in datos_usuarios]

    return JsonResponse(data, safe=False)


