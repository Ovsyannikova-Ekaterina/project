# Generated by Django 5.0.6 on 2024-06-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='materials',
            field=models.FileField(blank=True, null=True, upload_to='materials/'),
        ),
    ]
