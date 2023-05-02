from rest_framework import routers
from .api import UbicacionViewSet

router = routers.DefaultRouter()

router.register('ubicaciones', UbicacionViewSet, 'ubicaciones')