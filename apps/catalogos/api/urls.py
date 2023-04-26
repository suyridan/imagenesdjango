from django.urls import path
from apps.catalogos.api.api import UbicacionAPIVIEW

urlpatterns = [
    path('ubicacion/', UbicacionAPIVIEW.as_view(), name = 'ubicacion_api')
]
