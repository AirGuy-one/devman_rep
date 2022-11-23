from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from places_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
]


urlpatterns += [
     path('', include('places_app.urls')),
]


# urlpatterns += [
#     path('', RedirectView.as_view(url='', permanent=True)),
# ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
