from rest_framework import viewsets
from .models import JornadaVenta, Venta, DetalleVenta, Comanda
from .serializers import JornadaVentaSerializer, VentaSerializer, DetalleVentaSerializer, ComandaSerializer

class JornadaVentaViewSet(viewsets.ModelViewSet):
    queryset = JornadaVenta.objects.all()
    serializer_class = JornadaVentaSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer

class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer