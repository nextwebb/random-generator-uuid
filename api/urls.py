from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UUIDViewSet
# register api routes
router = routers.DefaultRouter()

router.register('generate-uuid', UUIDViewSet, basename='randomuuidmodel')


urlpatterns = [
    path('', include(router.urls)),
]
