from rest_framework import generics
from woman.models import Woman
from woman.serializers import WomanSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
