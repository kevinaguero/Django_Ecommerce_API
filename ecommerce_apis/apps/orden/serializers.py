from rest_framework import serializers
from .models import Orden, DetalleOrden

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ('fecha_hora')

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
