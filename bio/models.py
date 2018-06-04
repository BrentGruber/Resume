from django.db import models
from django.contrib.postgres.fields import JSONField
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):

    name = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=45)
    #TODO: find a better naming convention for media uploads, can't go by prof name, don't have it yet
    image = models.ImageField(blank=True, upload_to='uploads/')
    resume = models.FileField(blank=True, upload_to='uploads/')
    about = HTMLField()
    links = JSONField()
    skills = JSONField()

    @property
    def get_skill(self):
        return json.dumps(self.skills)

    def __str__(self):
        return self.name 