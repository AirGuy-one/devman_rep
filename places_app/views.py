from django.http import JsonResponse
from django.shortcuts import render
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

    post = Post.objects.get(pk=pk)

    post_info = {'title': str(post.title), 'imgs': []}

    for i in Images.objects.filter(post=Post.objects.get(pk=post.id)):
        post_info['imgs'].append("media/" + str(i.image))

    post_info['description_short'] = str(post.description_short)
    post_info['description_long'] = str(post.description_long)
    post_info['coordinates'] = {
        "lng": float(post.longitude),
        "lat": float(post.latitude)
    }

    return JsonResponse(post_info, json_dumps_params={'ensure_ascii': False, 'indent': 2})
