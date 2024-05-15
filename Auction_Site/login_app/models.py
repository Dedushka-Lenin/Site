from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20, blank=False)
    mail = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=30, blank=False)
    subscription = models.CharField(max_length=6, blank=False)
    balance = models.IntegerField(default=0)
