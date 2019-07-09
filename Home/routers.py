from rest_framework import routers
from HomeRun.viewsets import RegViewSet

router = routers.DefaultRouter()
router.register(r'registration', RegViewSet)
