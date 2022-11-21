from django.contrib import admin
from django.shortcuts import render
from django.urls import path


def show_phones(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_phones),
]
