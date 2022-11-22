from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


def show_phones(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_phones),
]


urlpatterns += [
     path('catalog/', include('places.urls')),
]


urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
