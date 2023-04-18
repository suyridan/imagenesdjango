from rest_framework import routers
from .api import AcervoViewSet

router = routers.DefaultRouter()

router.register('api/acervos', AcervoViewSet, 'acervos')

urlpatterns = router.urls