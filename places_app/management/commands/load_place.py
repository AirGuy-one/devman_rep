import requests

from hashlib import md5
from django.core.management.base import BaseCommand
from places_app.models import Post, Images
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Display the args'

    def add_arguments(self, parser):
        parser.add_argument('json_file_address', type=str)

    def handle(self, *args, **kwargs):
        url_address = kwargs['json_file_address']

        response = requests.get(url_address)
        response.raise_for_status()
        place_content = response.json()

        # Here we add the place to Post model
        place, created = Post.objects.get_or_create(
            title=place_content['title'],
            defaults={
                'description_short': place_content['description_short'],
                'description_long': place_content['description_long'],
                'lat': place_content['coordinates']['lat'],
                'lng': place_content['coordinates']['lng'],
            })

        # Here we add the photos to Image model
        for url in place_content.get('imgs', []):
            response = requests.get(url, stream=True)

            content_file = ContentFile(
                response.content,
                name=md5(response.content).hexdigest()
            )
            Images.objects.get_or_create(image=content_file, post=place)
