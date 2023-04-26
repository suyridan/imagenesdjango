from rest_framework import routers
from .api.api import AcervoViewSet, VisualImagenViewSet

router = routers.DefaultRouter()

router.register('api/acervos', AcervoViewSet, 'acervos')
router.register('api/visualImagenes', VisualImagenViewSet, 'visualImagenes')

urlpatterns = router.urls