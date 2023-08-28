from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ticket, Response
from notification.models import create_notification

@receiver(post_save, sender=Ticket)
def send_notification_after_save_ticket(sender, instance, created, **kwargs):
    if created:
        create_notification(instance.request_by.user, f'{instance.request_by.user} vient de creer un ticket', theme='detail_ticket_admin/' + str(instance.id) + '/')
    elif instance.status != 'open':
        create_notification(instance.request_by.user, f'{instance.request_by.user} vient de changer le statut du ticket', role_target='USER', theme='ticket_description/' + str(instance.id) + '/')


@receiver(post_save, sender=Response)
def send_notification_after_save_response(sender, instance, created, **kwargs):
    if created:
        user = instance.employee.user
        if user.role == 'ADMIN':
            create_notification(instance.ticket.request_by.user, f'{user} vient de laisser une reponse', role_target='USER', theme='ticket_description/' + str(instance.ticket.id) + '/')
           
            
        elif user.role == 'USER':
            create_notification(user, 
                                f'{user} vient de laisser une reponse',
                                role_target='ADMIN', 
                                theme='detail_ticket_admin/' + str(instance.ticket.id) + '/')
            
            
            

