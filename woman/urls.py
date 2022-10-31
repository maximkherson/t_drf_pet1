from django.urls import path
from woman.views import WomanListCreateAPIView, WomanUpdateAPIView

urlpatterns = [
    path('', WomanListCreateAPIView.as_view(), name='women'),
    path('<int:pk>', WomanUpdateAPIView.as_view())
]
