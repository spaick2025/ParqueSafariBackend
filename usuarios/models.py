from django.db import models

class Persona(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.rut} - {self.nombre_completo}"

class UserProfile(Persona):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('CAJERO', 'Cajero'),
        ('GARZON', 'Garzón'),
    ]
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.nombre_completo} ({self.get_role_display()})"

class Trabajador(Persona):
    saldo_acumulado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    activo_para_fiado = models.BooleanField(default=True)

    def __str__(self):
        return f"Trabajador: {self.nombre_completo} [Saldo: ${self.saldo_acumulado}]"
