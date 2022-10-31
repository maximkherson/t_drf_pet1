from django.urls import path
from woman.views import WomanListCreateAPIView

urlpatterns = [
    path('', WomanListCreateAPIView.as_view(), name='women')
]
