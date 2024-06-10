from django.db import models

# Create your models here.


class Lots(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.IntegerField(blank=False)
    Description = models.TextField(blank=False)
    ing = models.ImageField(upload_to='static/lots_img/', null=False, blank=False)

    def __str__(self):
        return self.name