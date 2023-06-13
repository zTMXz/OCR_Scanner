from django.db import models
from django.urls import reverse
from users.models import User

# Create your models here.
class Scanner(models.Model):
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recognition = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('scanner:image_upload_success', kwargs={'id': self.id})

