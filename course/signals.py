# course/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import FeedbackForm

@receiver(post_save, sender=FeedbackForm)
def send_feedback_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='New Feedback Received',
            message=f"New feedback received:\n\n{instance.description}",
            from_email='ovs1ano4ka@yandex.ru',
            recipient_list=['ovs1ano4ka@yandex.ru'],
            fail_silently=False,
        )
