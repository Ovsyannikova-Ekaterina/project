# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ParentViewSet, StudentViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
