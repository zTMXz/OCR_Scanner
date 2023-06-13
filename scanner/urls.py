from django.urls import path, include
from scanner.views import image_upload


urlpatterns = [
    path("", image_upload, name='image_upload'),
]