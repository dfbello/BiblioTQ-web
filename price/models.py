from django.db import models

class Cotizacion1(models.Model):
    usuario = models.ForeignKey('SimpleUsuario', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    alto = models.DecimalField(max_digits=10, decimal_places=2)
    ancho = models.DecimalField(max_digits=10, decimal_places=2)
    fondo = models.DecimalField(max_digits=10, decimal_places=2)
    n_cajones_der = models.IntegerField()
    n_cajones_izq = models.IntegerField()
    status = models.BooleanField(default=False)  # False = pendiente, True = completado

class Cotizacion2(models.Model):
    usuario = models.ForeignKey('SimpleUsuario', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    alto = models.DecimalField(max_digits=10, decimal_places=2)
    ancho = models.DecimalField(max_digits=10, decimal_places=2)
    fondo = models.DecimalField(max_digits=10, decimal_places=2)
    alturarepisa = models.DecimalField(max_digits=10, decimal_places=2)
    Nrepisas = models.IntegerField()
    puerta = models.BooleanField(default=False)
    status = models.BooleanField(default=False)  # False = pendiente, True = completado

class Cotizacion3(models.Model):
    usuario = models.ForeignKey('SimpleUsuario', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    alto = models.DecimalField(max_digits=10, decimal_places=2)
    ancho = models.DecimalField(max_digits=10, decimal_places=2)
    fondo = models.DecimalField(max_digits=10, decimal_places=2)
    altura_1 = models.DecimalField(max_digits=10, decimal_places=2)
    altura_2 = models.DecimalField(max_digits=10, decimal_places=2)
    N_repisas_p = models.IntegerField()
    cajon = models.BooleanField(default=False)
    status = models.BooleanField(default=False)  # False = pendiente, True = completado

class insumo(models.Model):
    model = models.CharField(max_length=100)
    clase = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)


class SimpleUsuario(models.Model):
    email = models.EmailField(unique=True)

