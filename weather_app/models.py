from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='', unique=True)
    password = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='', blank=True, null=True)
    state = models.CharField(max_length=100, default='', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city}/{self.state}"
