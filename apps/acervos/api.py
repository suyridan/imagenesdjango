from .models import Acervo, VisualImagen
from rest_framework import viewsets, permissions
from .serializers import AcervoSerializer, VisualImagenSerializer

class AcervoViewSet(viewsets.ModelViewSet):
    queryset = Acervo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AcervoSerializer
    
class VisualImagenViewSet(viewsets.ModelViewSet):
    queryset = VisualImagen.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VisualImagenSerializer