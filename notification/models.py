from django.db import models
from django.conf import settings

class Notification(models.Model):
    ADMIN = 'ADMIN'
    USER = 'USER'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'user'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    role_target = models.CharField(max_length=30, choices=ROLE_CHOICES, default=ADMIN)
    theme = models.CharField(max_length=100, default='pannes')

    def __str__(self):
        return f"{self.user} | {self.message}"

def create_notification(user, message, role_target='ADMIN', theme=''):
    Notification.objects.create(user=user, message=message, role_target=role_target, theme=theme)




