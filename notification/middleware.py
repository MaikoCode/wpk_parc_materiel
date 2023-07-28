from .models import Notification

class NotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.role == 'ADMIN':
                request.notifications = Notification.objects.filter(read=False, role_target='ADMIN').order_by('-date')
            elif request.user.role == 'USER':
                request.notifications = Notification.objects.filter(read=False,role_target='USER',user=request.user).order_by('-date')
        response = self.get_response(request)
        return response
