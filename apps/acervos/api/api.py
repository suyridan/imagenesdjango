from rest_framework import viewsets, permissions
from rest_framework.views import APIView

from apps.acervos.models import Acervo, VisualImagen
from apps.acervos.api.serializers import AcervoSerializer, VisualImagenSerializer

class AcervoViewSet(viewsets.ModelViewSet): #toda la api GET(list), GET id, delete, post (create)
    queryset = Acervo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AcervoSerializer
    
class VisualImagenViewSet(viewsets.ModelViewSet):
    queryset = VisualImagen.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VisualImagenSerializer