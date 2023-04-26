from rest_framework import serializers
from apps.catalogos.models import Ubicacion

class UbicacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ubicacion
        fields = ('id','nombre','estatus','created_at')
        read_only_fields = ('created_at', )