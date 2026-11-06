# en ventas/models.py
from django.db import models
from usuarios.models import UserProfile, Trabajador
from mesas.models import Mesa
from productos.models import Producto

class JornadaVenta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    usuario_abre = models.ForeignKey(UserProfile, on_delete=models.PROTECT)

class Venta(models.Model):
    TIPO_VENTA = [
        ('DIRECTA', 'Caja Directa'),
        ('SALON', 'Atención Salón'),
        ('FIADO', 'Consumo Interno Trabajador'),
    ]
    tipo_venta = models.CharField(max_length=20, choices=TIPO_VENTA)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    jornada = models.ForeignKey(JornadaVenta, on_delete=models.PROTECT)
    usuario = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, blank=True, null=True)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.SET_NULL, blank=True, null=True)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.CharField(max_length=255, blank=True, null=True)

class Comanda(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    destino = models.CharField(max_length=50) # Cocina o Barra
    estado = models.CharField(max_length=20, default='PENDIENTE')
    timestamp_creacion = models.DateTimeField(auto_now_add=True)
    timestamp_entrega = models.DateTimeField(blank=True, null=True)