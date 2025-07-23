from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('', include(router.urls)),
]
