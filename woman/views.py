from rest_framework.response import Response
from rest_framework.views import APIView
from woman.models import Woman
from woman.serializers import WomanSerializer


class WomanAPIView(APIView):
    def get(self, request):
        return Response({'posts': WomanSerializer(Woman.objects.all(), many=True).data})

    def post(self, request):
        serializer = WomanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = WomanSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Woman.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response({"post": "delete post " + str(pk)})
