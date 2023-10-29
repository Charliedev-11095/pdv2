
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
                        { "data": "Correo Electrónico" },
                        { "data": "Teléfono" },
                        { "data": "Celular" },
                        { "data": "Rol" },
                        { "data": "RFC" },
                        { "data": "Razón Social" },
                        { "data": "Calle" },
                        { "data": "Ciudad" },
                        { "data": "Estado" },
                        { "data": "País" },
                        {
                            "data": null,
                            "defaultContent": "<button>Edit</button> <button>Delete</button>"
                        }
                    ]
                });
            });
