from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class DatosPersonales(models.Model):
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
    last_name = models.CharField(("Apellido Materno"),max_length=100, blank=True)
    phone = models.CharField(("teléfono"),max_length=10, blank=True)
    gender = models.CharField(("género"),max_length=9, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField()
    role = models.CharField(("rol"),max_length=13, choices=ROLE_CHOICES, blank=True)
    domicilio =models.ForeignKey('Domicilio', on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return self.last_name
    
class Meta:
    verbose_name = 'Dato Personal'
    verbose_name_plural = 'Datos Personales'
    
class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    
    def __str__(self):
        return self.calle

class Marca(models.Model):
    nombre_de_la_marca = models.CharField(max_length=50,null=False)
    descripcion_marca = models.CharField(max_length=50,null=False)
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    def __str__(self):
        return self.nombre_de_la_marca
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class DatosContacto(models.Model):
    telefono = models.CharField(max_length=10, null=True)
    celular = models.CharField(max_length=10,null=False)
    correo_electronico = models.EmailField(max_length=250, null=True)
    url_social = models.URLField(max_length=250,null=True)

    def __str__(self):
        return self.celular + ' ' + self.correo_electronico

    class Meta:
        verbose_name = 'Dato de Contacto'
        verbose_name_plural = 'Datos de Contacto'


class DatosFiscales(models.Model):
    rfc = models.CharField(max_length=13, null=True)
    razon_social = models.CharField(max_length=50, null=True)
    direccion = models.ForeignKey(Domicilio, null=False, blank=False,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rfc + ' ' + self.razon_social + ' ' 

    class Meta:
        verbose_name = 'Dato Fiscal'
        verbose_name_plural = 'Datos Fiscales'

class UsuariosAcceso(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales,null=False,on_delete=models.CASCADE)
    datos_contacto = models.ForeignKey(DatosContacto,null=False,on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=50,null=False)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1)

    def __str__(self):
        return self.datos_personales.nombre + ' ' + self.datos_personales.apellidos

    class Meta:
        verbose_name = 'Usuario de Acceso'
        verbose_name_plural = 'Usuarios de Acceso'


#Tabla de clientes
class Clientes(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales,null=False,on_delete=models.CASCADE)
    datos_contacto = models.ForeignKey(DatosContacto,null=False,blank=False,on_delete=models.CASCADE)
    datos_fiscales = models.ForeignKey(DatosFiscales,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.datos_personales.nombre + ' ' + self.datos_personales.apellidos
   
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Negocio(models.Model):
    contacto = models.ForeignKey(DatosContacto, null=False, blank=False,on_delete=models.CASCADE)
    datos_fiscales = models.ForeignKey(DatosFiscales, null=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.datos_fiscales.razon_social

    class Meta:
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

class DepartamentoProducto(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Departamento de Producto'
        verbose_name_plural = 'Departamentos de Productos'


class UnidadesMedidaProducto(models.Model):
    descripcion = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = 'Unidad de Medida de Producto'
        verbose_name_plural = 'Unidades de Medida de Productos'

class Productos(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    descripcion = models.CharField(max_length=300,null=True)
    marca = models.ForeignKey(Marca,null=True,blank=False,on_delete=models.SET_NULL)
    existencia = models.DecimalField(max_digits=5,decimal_places=2,null=False,blank=False)
    deparamento_producto = models.ForeignKey(DepartamentoProducto,null=True,blank=False,on_delete=models.SET_NULL)
    precio_venta = models.DecimalField(max_digits=5,decimal_places=2,null=False)
    existencia_minima = models.DecimalField(max_digits=5,decimal_places=2,null=False)
    
    def __str__(self):
        return self.nombre + ' ' + self.marca.nombre_de_la_marca + ' ' + self.deparamento_producto.nombre + ' ' + str(self.precio_venta)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


#Tabla de cajas
class Cajas(models.Model):
    clave = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.clave + ' ' + self.nombre

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'
OPCIONMOVIMIENTO = (
    ('a','abrir'),
    ('c','cerrar'),)

class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'

class MovimientosCaja(models.Model):
    caja = models.ForeignKey(Cajas,null=True,blank=False, on_delete=models.SET_NULL)
    fecha_apertura = models.DateTimeField()
    fecha_cierre = models.DateTimeField()
    tipo_movimiento = models.CharField(max_length=1,choices=OPCIONMOVIMIENTO)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(UsuariosAcceso,null=True,blank=False,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.caja.nombre + ' ' + self.tipo_movimiento + ' ' + str(self.saldo_inicial) + ' ' + str(self.saldo_final)

    class Meta:
        verbose_name = 'Movimiento de Caja'
        verbose_name_plural = 'Movimientos de Caja'

#tabla ventas 
METODOPAGOS = (
    ('a','transferencia'),
    ('b','efectivo'),
    ('c','tarjeta de credito'),
    ('d','tarjeta de debito'),
)

class Ventas(models.Model):
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Clientes,null=True,blank=False, on_delete=models.SET_NULL)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Cajas,null=True,blank=False, on_delete=models.SET_NULL)
    metodo_pago = models.CharField(max_length=1, choices=METODOPAGOS)
    importe_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    vuelto = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(UsuariosAcceso,null=True,blank=False, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.cliente.datos_personales.nombre + ' ' + self.cliente.datos_personales.apellidos + ' ' + str(self.total) + ' ' + str(self.total_descuento) + ' ' + str(self.total_impuesto) + ' ' + self.caja.nombre + ' ' + self.metodo_pago + ' ' + str(self.importe_pagado) + ' ' + str(self.vuelto) + ' ' + self.empleado.datos_personales.nombre + ' ' + self.empleado.datos_personales.apellidos

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class DetalleVentas(models.Model):
    producto = models.ForeignKey(Productos,null=True,blank=False,on_delete=models.SET_NULL)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2)
    venta = models.ForeignKey(Ventas,null=True,blank=False,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.producto.nombre + ' ' + str(self.descuento) + ' ' + str(self.porcentaje_descuento) + ' ' + str(self.cantidad) + ' ' + str(self.valor_unitario) + ' ' + str(self.importe) + ' ' + str(self.impuesto) + ' ' + self.venta.cliente.datos_personales.nombre + ' ' + self.venta.cliente.datos_personales.apellidos + ' ' + str(self.venta.total) + ' ' + str(self.venta.total_descuento) + ' ' + str(self.venta.total_impuesto) + ' ' + self.venta.caja.nombre + ' ' + self.venta.metodo_pago + ' ' + str(self.venta.importe_pagado) + ' ' + str(self.venta.vuelto) + ' ' + self.venta.empleado.datos_personales.nombre + ' ' + self.venta.empleado.datos_personales.apellidos
    
    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'