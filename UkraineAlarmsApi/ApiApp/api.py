from .models import UkraineAlarmsStatus
from rest_framework import viewsets, permissions
from .serializers import UkraineSerializer


class UkraineViewSet(viewsets.ModelViewSet):
    queryset = UkraineAlarmsStatus.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UkraineSerializer
