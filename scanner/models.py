from django.db import models
from django.urls import reverse
from users.models import User

from pytils import translit


class Scanner(models.Model):
    choices = [
        ('en', 'English'),
        ('ru', 'Russian')
    ]

    def get_image_path(self, filename):
        path = ''.join(["users/scans/", translit.slugify(filename)])
        return path

    description = models.TextField(blank=True)
    image = models.ImageField(verbose_name='Image', upload_to=get_image_path)
    image_denoised = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recognition = models.TextField(blank=True)
    lang = models.CharField(max_length=24, choices=choices, default='English')

    def __str__(self):
        return ' '.join([self.user.username, self.description[:11]])

    def get_absolute_url(self):
        return reverse('scanner:image_upload_success', kwargs={'id': self.id})
