from rest_framework import viewsets

from malls.models import Mall
from malls.serializers import MallSerializer


class MallViewSet(viewsets.ModelViewSet):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer
