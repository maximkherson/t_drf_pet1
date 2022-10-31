from django.urls import path
from woman.views import WomanModelViewSet

urlpatterns = [
    path('', WomanModelViewSet.as_view({'get': 'list'}), name='women'),
    path('<int:pk>', WomanModelViewSet.as_view({'get': 'retrieve', 'put': 'update'}))
]
