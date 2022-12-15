import json
import os
import requests
import shutil

from pathlib import Path
from django.core.management.base import BaseCommand
from places_app.models import Post, Images


class Command(BaseCommand):
    help = 'Display the args'

    def add_arguments(self, parser):
        parser.add_argument('json_file_address', type=str)

    def handle(self, *args, **kwargs):
        url_address = kwargs['json_file_address']

        response = requests.get(url_address)
        response.raise_for_status()
        response_place = response.json()

        # Here we add the post to Post model
        post = Post.objects.create(
            title=response_place['title'],
            description_short=response_place['description_short'],
            description_long=response_place['description_long'],
            longitude=response_place['coordinates']['lng'],
            latitude=response_place['coordinates']['lat']
        )

        # Here we add the photos to Image model
        for i in response_place['imgs']:
            url = i
            title_of_image = f'{url[-10:-4]}_img_data.jpg'
            response = requests.get(url, stream=True)
            with open(f'media/images/{title_of_image}', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            Images.objects.create(image=f'images/{title_of_image}', post=post)
