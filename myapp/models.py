from django.db import models

# Create your models here.
class ImageResult(models.Model):
    image = models.ImageField(upload_to='images/')
    result = models.TextField()