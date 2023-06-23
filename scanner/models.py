from django.db import models
from django.urls import reverse
from users.models import User

from pytils import translit
from django.utils.text import slugify

# Create your models here.
class Scanner(models.Model):
    def get_image_path(self, filename):
        path = ''.join(["users/scans/", translit.slugify(filename)])
        return path


    description = models.TextField(blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to=get_image_path)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recognition = models.TextField(blank=True)
    # recognition_extended = models.TextField(blank=True)

    def __str__(self):
        return ' '.join([self.user.username, self.description[:11]])

    def get_absolute_url(self):
        return reverse('scanner:image_upload_success', kwargs={'id': self.id})


