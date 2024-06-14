from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Lots_are_over(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.IntegerField(blank=False)
    Description = models.TextField(blank=False)
    ing = models.ImageField(upload_to='static/lots_img/', null=False, blank=False)

    sent = models.BooleanField(default=False)

    recipient = models.EmailField(
        _("email address"), 
        blank=True,
        default='',)

    def __str__(self):
        return self.name


class Lots(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.IntegerField(blank=False)
    auction_step = models.IntegerField(blank=False)
    Description = models.TextField(blank=False)
    ing = models.ImageField(upload_to='static/lots_img/', null=False, blank=False)

    end = models.BooleanField(default=False)
    end_time = models.CharField(max_length=20, blank=False)

    recipient = models.EmailField(
        _("email address"), 
        blank=True,
        default='',)

    def __str__(self):
        return self.name
    