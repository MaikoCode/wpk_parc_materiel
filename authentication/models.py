from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from employe.models import Employe


class User(AbstractUser):
    ADMIN = 'ADMIN'
    USER = 'USER'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'user'),
    )
    employe = models.OneToOneField(Employe, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    