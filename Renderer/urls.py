from .views import *
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

app_name = 'Renderer'
urlpatterns = [
    path('', index, name=''),
    path('info', index),
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)