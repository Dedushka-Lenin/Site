from django.db import models

# Create your models here.


class lots(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.IntegerField(blank=False)
    Description = models.TextField(blank=False)
    ing = models.ImageField()

    def __str__(self):
        return self.name