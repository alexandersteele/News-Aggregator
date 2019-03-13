from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Author (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class NewsStory (models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=64)
    category = models.CharField(max_length=50)
    region = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    details = models.CharField(max_length=512)

    def __str__(self):
        return self.headline
