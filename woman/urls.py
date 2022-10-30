from django.urls import path
from woman.views import WomanAPIView

urlpatterns = [
    path('', WomanAPIView.as_view(), name='women'),
]
