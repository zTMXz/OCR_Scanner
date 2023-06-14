from django.urls import path, include
from scanner.views import ImageUpload, ImageUploadDetail


app_name = 'scanner'
urlpatterns = [
    path("", ImageUpload.as_view(), name='image_upload'),
    path("<int:id>/", ImageUploadDetail.as_view(), name='image_upload_success'),
]