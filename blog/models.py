from django.db import models

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