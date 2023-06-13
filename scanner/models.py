from django.db import models
from users.models import User

# Create your models here.
class Scanner(models.Model):
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ScanHistory(models.Model):
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    recognition = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

