from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DemandeMateriel
from notification.models import create_notification

@receiver(post_save, sender=DemandeMateriel)
def send_notification_after_save(sender, instance, created, **kwargs):
    if created:
        create_notification(instance.demandeur.user, f'{instance.demandeur.user} vient de faire une demande.', role_target='ADMIN', theme='demander_materiel')
    elif instance.status:
        create_notification(instance.demandeur.user, f'Votre demande de matériel a été validée.', role_target='USER', theme='demander_materiel')

