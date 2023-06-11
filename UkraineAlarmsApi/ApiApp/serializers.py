from rest_framework import serializers
from .models import UkraineAlarmsStatus


class UkraineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
