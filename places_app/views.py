from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Post, Images
import json
import pathlib


def index(request):
    images = Images.objects.all()
    posts = Post.objects.all()

    places_info = {
        "type": "FeatureCollection",
        "features": []
    }

    for post in posts:
        """ Here we writing json to html template """
        features_info = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [post.longitude, post.latitude]
            },
            "properties": {
                "title": post.title,
                "placeId": post.id,
                "detailsUrl": "static/places/" + f"{post.id}" + "_json_data.json"
            }
        }

        places_info['features'].append(features_info)

    context = {
        'posts': posts,
        'images': images,
        'json_final': places_info,
    }

    return render(request, 'index.html', context=context)


def api(request, pk):

    desired_dir = str(pathlib.Path(__file__).parent.parent.resolve())

    post = Post.objects.get(pk=pk)

    desired_dir = desired_dir + f'/static/places/{post.id}_json_data.json'
    with open(desired_dir) as f:
        response_data = json.load(f)


    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False, 'indent': 2})
