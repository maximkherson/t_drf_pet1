from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from woman.models import Woman
from woman.serializers import WomanSerializer


class WomanListCreateAPIView(ListCreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class WomanUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
