import csv
import math

from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .models import Post, Images


class ImagesAdmin(admin.ModelAdmin):
    model = Images
    extra = 0
    ordering = ('-id', )


class ImagesInline(admin.TabularInline):
    model = Images

    readonly_fields = ["display_image_field", ]

    def display_image_field(self, obj):
        new_width = 200 * obj.image.width / obj.image.height

        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=new_width,
            height=200,
        )
        )


class PostAdmin(admin.ModelAdmin):

    inlines = [
        ImagesInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Images, ImagesAdmin)






