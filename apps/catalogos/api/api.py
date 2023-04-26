from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UbicacionSerializer

from apps.catalogos.models import Ubicacion

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UbicacionSerializer
    
class UbicacionAPIVIEW(APIView):
    
    def get(self, request):
        ubicaciones = Ubicacion.objects.all()
        ubicacion_serializer = UbicacionSerializer(ubicaciones, many=True)
        return Response(ubicacion_serializer.data)