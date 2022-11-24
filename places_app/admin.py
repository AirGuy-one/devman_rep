from django.contrib import admin
from .models import Post, Images


class ImagesAdmin(admin.ModelAdmin):
    model = Images
    extra = 0
    ordering = ('-id',)


class ImagesInline(admin.TabularInline):
    model = Images


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Images, ImagesAdmin)






