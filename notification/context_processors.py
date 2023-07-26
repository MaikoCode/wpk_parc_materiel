
def notifications(request):
    unread_notifications_count = 0
    if request.user.is_authenticated:
        unread_notifications_count = request.user.notification_set.filter(read=False).count()
    return {'unread_notifications_count': unread_notifications_count}
