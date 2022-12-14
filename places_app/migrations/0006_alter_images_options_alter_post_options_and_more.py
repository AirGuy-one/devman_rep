# Generated by Django 4.1.2 on 2022-11-24 22:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0005_remove_images_image_title_alter_images_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['id'], 'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id'], 'verbose_name': 'Локация', 'verbose_name_plural': 'Локации'},
        ),
        migrations.AlterField(
            model_name='post',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
    ]
