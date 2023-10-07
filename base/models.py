from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)

class Post(models.Model):
    name = models.CharField(max_length = 200)
    topic = models.ForeignKey(Topic, null = True, on_delete=models.SET_NULL)
    url = models.CharField(null = True, blank = True, max_length=50)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to="base/static/base/images", default="")
    body1 = models.TextField(null = True, blank = True)
    body2 = models.TextField(null = True, blank = True)
    body3 = models.TextField(null = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return str(self.name)