from django.urls import path

from rest_framework import routers
from .api import AcervoViewSet, VisualImagenViewSet

router = routers.DefaultRouter()

router.register('acervos', AcervoViewSet, 'acervos')
router.register('visualImagenes', VisualImagenViewSet, 'visualImagenes')
