from django.db import models

class Mesa(models.Model):
    ESTADOS = [
        ('LIBRE', 'Libre'),
        ('OCUPADA', 'Ocupada'),
        ('RESERVADA', 'Reservada'),
    ]
    codigo = models.CharField(max_length=5, unique=True) # Ej: A1, H7
    estado = models.CharField(max_length=15, choices=ESTADOS, default='LIBRE')
    tiempo_inicio = models.DateTimeField(blank=True, null=True)
    tiempo_entrega = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Mesa {self.codigo} - {self.estado}"