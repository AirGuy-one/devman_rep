from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Images


def index(request):
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
        'json_final': places_info,
    }

    return render(request, 'index.html', context=context)


def get_post_json(request, pk):

    post = get_object_or_404(Post, pk=pk)

    post_info = {'title': post.title,
                 'imgs': [i.image.url for i in Post.objects.get(pk=pk).images.all()],
                 'description_short': post.description_short,
                 'description_long': post.description_long,
                 'coordinates': {
                     "lng": post.longitude,
                     "lat": post.latitude
                 }
                 }

    return JsonResponse(post_info, json_dumps_params={'ensure_ascii': False, 'indent': 2})
