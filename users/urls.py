from django.urls import path, include
from users.views import Register, Profile, delete_all, delete_one

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("register/", Register.as_view(), name='register'),
    path("profile/", Profile.as_view(), name='profile'),
    path("profile/delete/<int:scan_id>", delete_one, name='delete_one'),
    path("profile/delete_all/", delete_all, name='delete_all'),
]