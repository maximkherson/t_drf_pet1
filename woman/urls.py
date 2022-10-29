from django.urls import path
from woman.views import WomenAPIView

urlpatterns = [
    path('', WomenAPIView.as_view(), name='women'),
]
