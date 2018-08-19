from django.db import models
from django.contrib.postgres.fields import JSONField
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField
from imagekit.processors import Transpose

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=45)
    date = models.DateTimeField('date of post')
    

class Comment(models.Model):
    author = models.CharField(max_length=45)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class EmbeddedImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='uploads/')
    image_spec = ImageSpecField(processors=[Transpose(Transpose.AUTO)], source='image', format='JPEG')