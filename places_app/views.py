from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Images
from django.shortcuts import get_object_or_404
import json


def index(request):
    images = Images.objects.all()
    posts = Post.objects.all()

    json_convert_file = {}

    for post in posts:
        """Here we add json files to folder places"""
        json_convert_file['title'] = str(post.title)

        json_convert_file['imgs'] = []
        for i in Images.objects.filter(post=Post.objects.get(pk=post.id)):
            json_convert_file['imgs'].append("media/" + str(i.image))

        json_convert_file['description_short'] = str(post.description_short)
        json_convert_file['description_long'] = str(post.description_long)
        json_convert_file['coordinates'] = {
            "lng": float(post.x),
            "lat": float(post.y)
        }

        json_tmp = json.dumps(json_convert_file, indent=4)

        with open(f'static/places/{post.id}_json_data.json', 'w') as f:
            f.write(json_tmp)

    last = Post.objects.last()

    context = {
        'posts': posts,
        'images': images,
        'last': last
    }

    return render(request, 'index.html', context=context)


def api(request, pk):
    title_of_post = get_object_or_404(Post, pk=pk)

    return HttpResponse(f'{title_of_post}')







