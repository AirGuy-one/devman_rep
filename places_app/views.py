from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post


def index(request):
    places_info = {
        "type": "FeatureCollection",
        "features": []
    }

    for post in Post.objects.all():
        # Here we're writing json to html template
        features_info = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [post.longitude, post.latitude]
            },
            "properties": {
                "title": post.title,
                "placeId": post.id,
                "detailsUrl": reverse(get_post_json, args=[post.id])
            }
        }

        places_info['features'].append(features_info)

    context = {
        'places_info': places_info,
    }

    return render(request, 'index.html', context=context)


def get_post_json(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post_info = {
        'title': post.title,
        'imgs': [
            image.image.url for image in post.images.all()
        ],
        'description_short': post.description_short,
        'description_long': post.description_long,
        'coordinates': {
            "lng": post.longitude,
            "lat": post.latitude
        }
    }

    return JsonResponse(
        post_info,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
