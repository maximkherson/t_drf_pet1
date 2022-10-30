from rest_framework.response import Response
from rest_framework.views import APIView
from woman.models import Woman
from woman.serializers import WomanSerializer


class WomanAPIView(APIView):
    def get(self, request):
        print('XXX', request.data)
        return Response({'posts': WomanSerializer(Woman.objects.all(), many=True).data})

    def post(self, request):
        WomanSerializer(data=request.data).is_valid(raise_exception=True)

        new_post = Woman.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': WomanSerializer(new_post).data})
