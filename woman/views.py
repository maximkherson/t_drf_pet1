from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from woman.models import Woman


class WomanAPIView(APIView):
    def get(self, request):
        return Response({'posts': Woman.objects.all().values()})

    def post(self, request):
        new_post = Woman.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(new_post)})
