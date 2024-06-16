# course/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CourseApplicationViewSet, FeedbackFormViewSet, TopicViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course-applications', CourseApplicationViewSet)
router.register(r'feedback-forms', FeedbackFormViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
