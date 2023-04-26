from rest_framework import serializers
from .models import Acervo, VisualImagen, FisicaImagen


class AcervoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acervo
        fields = ('id','name','estatus','created_at')
        read_only_fields = ('created_at', )
        
        
class VisualImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualImagen
        fields = ('id','titulo','estatus','created_at')
        read_only_fields = ('created_at', )
        
class FisicaImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FisicaImagen
        fields = ('id','nombre','estatus','created_at')
        read_only_fields = ('created_at', )