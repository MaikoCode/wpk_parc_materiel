from django.shortcuts import redirect
from .models import Notification

def read_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.read = True
    notification.save()

    if notification.theme == 'pannes':
        return redirect('pannes')

    # On va ajouter le reste des themes en fonction des pages


    return redirect('home')
