from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase
from .models import Post, Images


class ImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Images
    extra = 0
    list_display = ('number', 'id', 'display_image_field', 'post')
    ordering = ('number',)

    def display_image_field(self, obj):
        new_width = 200 * obj.image.width / obj.image.height

        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=new_width,
                height=200,
            )
        )


class ImagesInline(SortableTabularInline):
    model = Images

    readonly_fields = ["display_image_field", ]

    def display_image_field(self, obj):
        new_width = 200 * obj.image.width / obj.image.height

        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=new_width,
                height=200,
            )
        )


class PostAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (
        ImagesInline,
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Images, ImagesAdmin)
