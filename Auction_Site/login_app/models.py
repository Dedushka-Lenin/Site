from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Users_info(models.Model):
    # name = models.CharField(max_length=20, blank=False)
    # mail = models.CharField(max_length=50, blank=False)
    # password = models.CharField(max_length=30, blank=False)
    # subscription = models.CharField(default='Non', max_length=6, blank=False)
    # balance = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.name
    
class Users(AbstractUser):
    email = models.EmailField(
        _("email address"), 
        blank=True,
        unique=True)
    
    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]