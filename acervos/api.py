from .models import Acervo
from rest_framework import viewsets, permissions
from .serializers import AcervoSerializer

class AcervoViewSet(viewsets.ModelViewSet):
    queryset = Acervo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AcervoSerializer