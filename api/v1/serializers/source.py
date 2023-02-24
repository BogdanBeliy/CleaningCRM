from rest_framework.serializers import ModelSerializer

from core.models import Source


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = ['name']

