from django.urls import path
from scanner.views import ImageUpload, ImageUploadDetail, ImagePrint


app_name = 'scanner'
urlpatterns = [
    path("", ImageUpload.as_view(), name='image_upload'),
    path("print/<int:id>/", ImagePrint.as_view(), name='image_print'),
    path("<int:id>/", ImageUploadDetail.as_view(), name='image_upload_success'),
]