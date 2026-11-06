# en productos/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50) # Ej: Comida, Bebida, Snack
    impresora_destino = models.CharField(max_length=50) # Ej: Cocina, Barra

    def __str__(self):
        return f"{self.nombre} (${self.precio})"