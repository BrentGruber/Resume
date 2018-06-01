from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=45)
    about = models.TextField()
    links = JSONField()
    skills = JSONField()