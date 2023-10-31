from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Usuario(models.Model):
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
    nombre = models.CharField(("Nombre"),max_length=100, blank=True)
    apellido_paterno = models.CharField(("Apellido Paterno"),max_length=100, blank=True)
    apellido_materno = models.CharField(("Apellido Materno"),max_length=100, blank=True)
    genero = models.CharField(("género"),max_length=9, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField()
    status = models.BooleanField(("status"), default=True)
    role = models.CharField(("rol"),max_length=13, choices=ROLE_CHOICES, blank=True)
    domicilio =models.ForeignKey('Domicilio', on_delete=models.CASCADE, null=False, blank=True)
    datos_contacto = models.ForeignKey('DatosContacto', on_delete=models.CASCADE, null=False, blank=True)
    datos_fiscales= models.ForeignKey('DatosFiscales', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Dato Personal'
        verbose_name_plural = 'Datos Personales'

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
    
class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
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

#Tabla de clientes
class Clientes(models.Model):
    usuario=models.ForeignKey(Usuario,null=True,blank=False,on_delete=models.SET_NULL)
    id_cliente = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.datos_personales.nombre + ' ' + self.datos_personales.apellidos
   
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Empleados(models.Model):
    usuario=models.ForeignKey(Usuario,null=True,blank=False,on_delete=models.SET_NULL)
    id_empleado = models.CharField(max_length=50, null=False)
    puesto = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.datos_personales.nombre + ' ' + self.datos_personales.apellidos

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

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
    empleado = models.ForeignKey(Empleados,null=True,blank=False,on_delete=models.SET_NULL)
    
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
    empleado = models.ForeignKey(Empleados,null=True,blank=False, on_delete=models.SET_NULL)
    
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

# -------------------------------------VISTAS SQL -------------------------------------

from django.db import models


class Vistadatosusuarios(models.Model):
    usuario_id = models.BigIntegerField(primary_key=True, db_column='usuario_id')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    apellido_paterno = models.CharField(db_column='Apellido Paterno', max_length=100, db_collation='utf8mb4_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    apellido_materno = models.CharField(db_column='Apellido Materno', max_length=100, db_collation='utf8mb4_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    género = models.CharField(db_column='Género', max_length=9, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    fecha_de_nacimiento = models.DateField(db_column='Fecha de Nacimiento')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.BooleanField(db_column='Status')  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=13, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    calle = models.CharField(db_column='Calle', max_length=100, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=100, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=100, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    país = models.CharField(db_column='País', max_length=100, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    teléfono = models.CharField(db_column='Teléfono', max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    correo_electrónico = models.CharField(db_column='Correo Electrónico', max_length=250, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rfc = models.CharField(db_column='RFC', max_length=13, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    razón_social = models.CharField(db_column='Razón Social', max_length=50, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'VistaDatosUsuarios'