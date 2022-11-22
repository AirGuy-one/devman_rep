from django.contrib import admin
from .models import Post, Images


class ImagesAdmin(admin.ModelAdmin):
    model = Images
    extra = 0
    ordering = ('-id',)


admin.site.register(Post)
admin.site.register(Images, ImagesAdmin)






