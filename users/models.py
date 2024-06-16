#   users/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .validators import validate_username

class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_username],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    USER_TYPE_CHOICES = (
        (1, 'parent'),
        (2, 'student'),
        (3, 'teacher'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set_permissions')

    def __str__(self):
        return self.username

class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    relation_to_child = models.CharField(max_length=50)

    def __str__(self):
        return self.user.get_full_name()


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField()
    email = models.EmailField(blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.get_full_name()
