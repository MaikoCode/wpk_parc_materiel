from django.shortcuts import redirect
from .models import Notification

def read_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.read = True
    notification.save()

    if notification.theme == 'pannes':
        return redirect('pannes')

    if notification.theme == 'demander_materiel' and request.user.role == 'ADMIN':
        return redirect('Gestion_Demande')

    if notification.theme == 'demander_materiel' and request.user.role == 'USER':
        return redirect('materiels_user')

    return redirect('home')
