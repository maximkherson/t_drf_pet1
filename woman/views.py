from rest_framework.viewsets import ModelViewSet
from woman.models import Woman
from woman.serializers import WomanSerializer


class WomanModelViewSet(ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
