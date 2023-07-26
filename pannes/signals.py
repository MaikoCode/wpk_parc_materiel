from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Panne
from notification.models import create_notification

@receiver(post_save, sender=Panne)
def send_notification_after_save(sender, instance, created, **kwargs):
    if created:
        create_notification(instance.user, f'Une nouvelle instance de {instance} a été créée')
