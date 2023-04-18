from rest_framework import serializers
from .models import Acervo


class AcervoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acervo
        fields = ('id','nombre','estatus','created_at')
        read_only_fields = ('created_at', )