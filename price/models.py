from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)

class Peticion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada')
    ], default='pendiente')

class Inventario(models.Model):
    nombre_mueble = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField()

class PedidoInventario(models.Model):
    mueble = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado')
    ], default='pendiente')

class Cotizacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.TextField()
    ancho = models.DecimalField(max_digits=10, decimal_places=2)
    alto = models.DecimalField(max_digits=10, decimal_places=2)
    profundidad = models.DecimalField(max_digits=10, decimal_places=2)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)

class CorreoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)