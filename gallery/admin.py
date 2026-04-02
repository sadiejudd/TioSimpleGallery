from django.contrib import admin
from .models import Image, Tag, Comment

# Register your models here.

admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Comment)
