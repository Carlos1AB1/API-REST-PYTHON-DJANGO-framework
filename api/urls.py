from django.urls import include, path
from rest_framework import routers
from api import views
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
