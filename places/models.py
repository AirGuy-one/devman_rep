from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()





