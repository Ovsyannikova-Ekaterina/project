# Generated by Django 5.0.6 on 2024-06-16 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_topic_materials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackform',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='feedbackform',
            name='student',
        ),
        migrations.RemoveField(
            model_name='feedbackform',
            name='teacher',
        ),
    ]
