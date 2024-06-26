from rest_framework import serializers
from .models import Factura, Presupuesto




class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'


class PresupuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presupuesto
        fields = '__all__'


class ExtraerMontoSerializer(serializers.Serializer):
    presupuesto = serializers.IntegerField()
    presupuesto2 = serializers.IntegerField()
    cantidad = serializers.FloatField()

