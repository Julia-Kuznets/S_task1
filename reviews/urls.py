from .views import ReviewViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls))
]