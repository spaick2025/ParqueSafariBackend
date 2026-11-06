from rest_framework import serializers
from .models import JornadaVenta, Venta, DetalleVenta, Comanda

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True)

    class Meta:
        model = Venta
        fields = '__all__'

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        venta = Venta.objects.create(**validated_data)
        for detalle_data in detalles_data:
            DetalleVenta.objects.create(venta=venta, **detalle_data)
        return venta

class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = '__all__'

class JornadaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = JornadaVenta
        fields = '__all__'