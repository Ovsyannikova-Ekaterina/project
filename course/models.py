#   course/models.py

from django.db import models
from django.core.mail import send_mail
from users.models import Parent, Teacher, Student

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in hours")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CourseApplication(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent_phone = models.CharField(max_length=15)
    parent_email = models.EmailField()

    def __str__(self):
        return f"{self.parent.user.username} - {self.course.name}"
class FeedbackForm(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Feedback on {self.date} at {self.time}"

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    material_links = models.TextField(blank=True, help_text="Comma separated links")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    materials = models.FileField(upload_to='materials/', blank=True, null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.topic.name} - {self.date}"
