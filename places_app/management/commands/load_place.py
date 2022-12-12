import json
import urllib.request
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

        """ Here we create auxiliary folders """
        if not os.path.isdir('static'):
            base_dir = Path(__file__).resolve().parent.parent.parent.parent
            os.chdir(base_dir)
            os.mkdir('static')
            os.mkdir('media')
            os.chdir(os.path.join(base_dir, 'media'))
            os.mkdir('images')
            os.chdir(os.path.join(base_dir, 'load_static'))
            os.mkdir('places')
            os.chdir('..')

        r = requests.get(url_address)
        data = r.json()

        """ Here we add the post to Post model """
        post = Post.objects.create(title=data['title'], description_short=data['description_short'],
                                   description_long=data['description_long'], longitude=data['coordinates']['lng'],
                                   latitude=data['coordinates']['lat'])

        """ Here we add the photos to Image model """
        for i in data['imgs']:
            url = i
            title_of_image = f'{url[-10:-4]}_img_data.jpg'
            response = requests.get(url, stream=True)
            with open(f'media/images/{title_of_image}', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            Images.objects.create(image=f'images/{title_of_image}', post=post)

        """ Here we create json file in server folder """
        json_convert_file = {'title': str(post.title), 'imgs': []}

        for i in Images.objects.filter(post=Post.objects.get(pk=post.id)):
            json_convert_file['imgs'].append("media/" + str(i.image))

        json_convert_file['description_short'] = str(post.description_short)
        json_convert_file['description_long'] = str(post.description_long)
        json_convert_file['coordinates'] = {
            "lng": float(post.longitude),
            "lat": float(post.latitude)
        }

        json_tmp = json.dumps(json_convert_file, indent=4, ensure_ascii=False)

        with open(f'load_static/places/{post.id}_json_data.json', 'w') as f:
            f.write(json_tmp)