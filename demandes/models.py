from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from employe.models import Employe

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('open', 'open'),
        ('in_progress', 'In Progress'),
        ('completed', 'completed'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='low')
    request_by = models.ForeignKey(Employe, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=timezone.now)
    files = models.ManyToManyField('FileUpload', blank=True)

    def _str_(self):
        return self.title


class FileUpload(models.Model):
    file = models.FileField(upload_to='ticket_files/')
    def _str_(self):
        return self.file.name


class Response(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='responses', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employe, on_delete=models.CASCADE)
    response_text = models.TextField()
    response_date = models.DateTimeField(default=timezone.now)

    def str(self):
        return f'Response by {self.employee} on {self.response_date}'