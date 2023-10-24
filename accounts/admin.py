from django.contrib import admin


from .models import DatosPersonales, Domicilio, Marca, DatosContacto ,DatosFiscales, UsuariosAcceso, Clientes, Negocio, DepartamentoProducto, UnidadesMedidaProducto, Productos, Cajas, MovimientosCaja, Ventas, DetalleVentas
admin.site.register(DatosPersonales)
admin.site.register(Domicilio)
admin.site.register(Marca)
admin.site.register(DatosContacto)
admin.site.register(DatosFiscales)
admin.site.register(UsuariosAcceso)
admin.site.register(Clientes)
admin.site.register(Negocio)
admin.site.register(DepartamentoProducto)
admin.site.register(UnidadesMedidaProducto)
admin.site.register(Productos)
admin.site.register(Cajas)
admin.site.register(MovimientosCaja)
admin.site.register(Ventas)
admin.site.register(DetalleVentas)

(admin.ModelAdmin)