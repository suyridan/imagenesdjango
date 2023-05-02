from django.urls import path, include
from .api.routers import *

urlpatterns = [
    path('api/', include((router.urls, 'api')), name="catalogos_api")
]