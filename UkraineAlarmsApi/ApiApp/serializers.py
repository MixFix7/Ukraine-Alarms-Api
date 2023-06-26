from rest_framework import serializers
from .models import UkraineRegions


class UkraineSerializer(serializers.ModelSerializer):
    class Meta:
        model = UkraineRegions
        fields = ['id', 'Region', 'Region_en', 'Alarm', 'datetime']


