from .models import UkraineAlarmsStatus
from rest_framework import viewsets, permissions
from .serializers import UkraineSerializer
from .ukraine_alarms import get_alarms


class UkraineViewSet(viewsets.ModelViewSet):
    queryset = UkraineAlarmsStatus.objects.all()
    get_alarms()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UkraineSerializer
