from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UbicacionSerializer

from apps.catalogos.models import Ubicacion

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UbicacionSerializer
    
# class ZoneSerializer(ModelSerializer):
#     parent = SerializerMethodField()

#     class Meta:
#         model = Zone
#         fields = ('id', 'name', 'project', 'parent',)

#     def get_parent(self, obj):
#         if obj.parent is not None:
#             return ZoneSerializer(obj.parent).data
#         else:
#             return None
class UbicacionAPIVIEW(APIView):
    
    def get(self, request):
        ubicaciones = Ubicacion.objects.all()
        ubicacion_serializer = UbicacionSerializer(ubicaciones, many=True)
        return Response(ubicacion_serializer.data)
    
# @api_view
# def ubicacion_api_view(request):
#     if request.method == 'GET':
#         ubicaciones = Ubicacion.objects.all()
#         ubicacion_serializer = UbicacionSerializer(ubicaciones, many=True)
#         return Response(ubicacion_serializer.data)