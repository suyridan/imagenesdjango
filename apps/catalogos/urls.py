from rest_framework import routers
from .api import UbicacionViewSet

router = routers.DefaultRouter()

router.register('api/ubicaciones', UbicacionViewSet, 'ubicaciones')

urlpatterns = router.urls