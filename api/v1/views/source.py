from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from uuid import uuid4
from api.v1.serializers.source import SourceSerializer
from core.models import Source


@extend_schema(tags=['source'])
class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(
            token=uuid4().hex[:50]
        )
