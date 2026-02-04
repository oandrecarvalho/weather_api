from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from weather_app.views import UserViewSet
from weather_app import urls as weather_urls

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(weather_urls)),
    path('', include(weather_urls)),
]
