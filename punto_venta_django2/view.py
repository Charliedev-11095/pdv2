from django.shortcuts import render

def usuarios(request):
    usuario = request.user
    nombre_usuario = usuario.username
    correo_electronico = usuario.email
    nombre = usuario.first_name
    apellido = usuario.last_name

    return render(request, 'mi_template.html', {'usuario': usuario})