from rest_framework import serializers
from .models import Plot


class PlotListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)

    class Meta:
        model = Plot
        fields = ('id', 'contour', 'farmer', 'culture', 'season')
        read_only_fields = ('contour',)