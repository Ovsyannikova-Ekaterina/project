#   course/admin.py

from django.contrib import admin
from .models import Course, CourseApplication, FeedbackForm, Topic, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'duration', 'cost')
    search_fields = ('name', 'level')

@admin.register(CourseApplication)
class CourseApplicationAdmin(admin.ModelAdmin):
    list_display = ('parent', 'course', 'date', 'status')
    search_fields = ('parent__user__username', 'course__name')
    list_filter = ('status', 'date')

@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'time')
    search_fields = ('description',)
    list_filter = ('date',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'description')
    search_fields = ('name', 'course__name')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'teacher', 'date', 'start_time', 'end_time')
    search_fields = ('topic__name', 'teacher__user__username')
    list_filter = ('date',)
