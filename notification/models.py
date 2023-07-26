from django.db import models
# from .models import Notification
# from employe.models import Employe
from django.conf import settings



class Notification(models.Model):


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} | {self.message}"

def create_notification(user, message):
    print(user, message)
    Notification.objects.create(user=user, message=message)



