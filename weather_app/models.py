from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default='', unique=True)
    email = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='', blank=True, null=True)

def __str__(self):
    return self.username + ' ' + self.location
