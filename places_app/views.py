from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Post, Images
from django.shortcuts import get_object_or_404
import json
import pathlib
from environs import Env

class PlacesJsonResponse(JsonResponse):
    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        json_dumps_params = dict(ensure_ascii=False)
        json_dumps_params['indent'] = 2
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)


def index(request):
    images = Images.objects.all()
    posts = Post.objects.all()

    json_convert_file = {}

    json_for_html = {
        "type": "FeatureCollection",
        "features": []
    }

    for post in posts:
        """Here we writing json to html template"""
        adding = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(post.longitude), float(post.latitude)]
            },
            "properties": {
                "title": f'{post.title}',
                "placeId": f'id_is_{post.id}',
                "detailsUrl": "static/places/" + f"{post.id}" + "_json_data.json"
            }
        }

        json_for_html['features'].append(adding)

    # json_final = json.dumps(json_for_html, indent=4)
    json_final = json_for_html

    last = Post.objects.last()

    context = {
        'posts': posts,
        'images': images,
        'last': last,
        'json_final': json_final,
    }

    return render(request, 'index.html', context=context)


def api(request, pk):

    desired_dir = str(pathlib.Path(__file__).parent.parent.resolve())

    post = Post.objects.get(pk=pk)

    desired_dir = desired_dir + f'/static/places/{post.id}_json_data.json'
    with open(desired_dir) as f:
        response_data = json.load(f)

    return PlacesJsonResponse(response_data)
