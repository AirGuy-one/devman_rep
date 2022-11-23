from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    x = models.DecimalField(max_digits=20, decimal_places=14, null=True)
    y = models.DecimalField(max_digits=20, decimal_places=14, null=True)

    def __str__(self):
        return f'{self.id} {self.title}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Image {self.id} - {self.image.name}'

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'




















