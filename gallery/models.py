from django.db import models


# Create your models here.

class Image(models.Model):
    image = models.ImageField()
    session = models.CharField(max_length=100)