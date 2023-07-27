class NotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.notifications = request.user.notification_set.filter(read=False).order_by('-date')
        response = self.get_response(request)
        return response
