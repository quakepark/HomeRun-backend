from rest_framework import viewsets

from HomeRun.models import Registration
from HomeRun.serializers import RegSerializer


class RegViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegSerializer
