from dronezonia.models import Path
from rest_framework import serializers


class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ['id', 'path']
