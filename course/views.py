#   course/views.py

from rest_framework import viewsets
from .models import Course, CourseApplication, FeedbackForm, Topic, Lesson
from .serializers import CourseSerializer, CourseApplicationSerializer, FeedbackFormSerializer, TopicSerializer, LessonSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseApplicationViewSet(viewsets.ModelViewSet):
    queryset = CourseApplication.objects.all()
    serializer_class = CourseApplicationSerializer

class FeedbackFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all()
    serializer_class = FeedbackFormSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
