from rest_framework import routers
from woman.views import WomanModelViewSet

women_router = routers.SimpleRouter()
women_router.register('', WomanModelViewSet)
print(women_router.urls)
