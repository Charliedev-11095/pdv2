$(document).ready(function() {
    $('#example').DataTable({
        "ajax": {
            "url": "/accounts/listaUsuarios/",
            "dataSrc": ""  // Deja esto en blanco para que los datos se tomen directamente del JSON
        },
        "columns": [
            { "data": "usuario_id" },
            { "data": "Nombre" },
            { "data": "Apellido Paterno" },
            { "data": "Apellido Materno" },
            { "data": "Género" },
            { "data": "Fecha de Nacimiento" },
            { "data": "Status" },
            { "data": "Rol" },
            { "data": "Calle" },
            { "data": "Ciudad" },
            { "data": "Estado" },
            { "data": "País" },
            { "data": "Teléfono" },
            { "data": "Celular" },
            { "data": "Correo Electrónico" },
            { "data": "RFC" },
            { "data": "Razón Social" },
            {
                "data": null,
                "defaultContent": "<button class='btn btn-primary mr-2'>Editar</button> <button class='btn btn-danger'>Borrar</button>"
            }
        ]
    });
});