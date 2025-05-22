
from django.db import models

# Create your models here.
class Captcha(models.Model):
    image = models.ImageField(upload_to='captcha_images')
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer

