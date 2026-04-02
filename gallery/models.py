from django.db import models


# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=100, name = "tag")

    def __str__(self):
        return self.tag

class Image(models.Model):
    image = models.ImageField()
    session = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
   


class Comment(models.Model):
    comment = models.CharField(max_length = 200)
    image = models.ForeignKey(Image)