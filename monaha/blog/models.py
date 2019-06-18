from django.db import models

class BlogPhoto(models.Model):
    photo = models.ImageField()
    post = models.ForeignKey('Blog', null=True, on_delete=models.SET_NULL)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.CharField(max_length=15)
