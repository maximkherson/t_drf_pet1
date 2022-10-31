from django.contrib import admin
from django.urls import path, include
from woman.urls import women_router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('women/', include('woman.urls'))
    path('women/', include(women_router.urls))
]
