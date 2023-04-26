from rest_framework import viewsets, permissions
from rest_framework.views import View

from apps.acervos.models import Acervo, VisualImagen
from apps.acervos.api.serializers import AcervoSerializer, VisualImagenSerializer

class AcervoViewSet(viewsets.ModelViewSet):
    queryset = Acervo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AcervoSerializer
    
class VisualImagenViewSet(viewsets.ModelViewSet):
    queryset = VisualImagen.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VisualImagenSerializer