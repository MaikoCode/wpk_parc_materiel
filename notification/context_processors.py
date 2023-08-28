from .models import Notification

def notifications(request):
    unread_notifications_count = 0  # Initialisation
    if request.user.is_authenticated:
        if request.user.role == 'ADMIN':
            unread_notifications_count = Notification.objects.filter(read=False, role_target='ADMIN').count()
        elif request.user.role == 'USER':
            unread_notifications_count = Notification.objects.filter(read=False,role_target='USER',user=request.user).count()
    return {'unread_notifications_count': unread_notifications_count}
