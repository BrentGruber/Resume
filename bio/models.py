from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=45)
    image = models.ImageField(blank=True)
    resume = models.FileField(blank=True)
    about = models.TextField()
    links = JSONField()
    skills = JSONField()

    @property
    def get_skill(self):
        return json.dumps(self.skills)

    def __str__(self):
        return self.name