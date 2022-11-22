from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()

    def __str__(self):
        return f'{self.id} {self.title}'


class Images(models.Model):
    image_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Image {self.id} - {self.image_title}'











