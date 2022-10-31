from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from woman.models import Woman, Category
from woman.serializers import WomanSerializer


class WomanModelViewSet(ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        wo = self.get_object()
        category = Category.objects.get(pk=wo.cat.id)
        return Response({'category': category.name})
