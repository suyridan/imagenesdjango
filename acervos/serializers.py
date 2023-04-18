from rest_framework import serializers
from .models import Acervo, VisualImagen, FisicaImagen


class AcervoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acervo
        fields = ('id','nombre','estatus','created_at')
        read_only_fields = ('created_at', )
        
        
class VisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualImagen
        fields = ('id','nombre','estatus','created_at')
        read_only_fields = ('created_at', )
        
class VisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = FisicaImagen
        fields = ('id','nombre','estatus','created_at')
        read_only_fields = ('created_at', )