from django.db import models


# Create your models here.
class FileUpload(models.Model):
    image = models.ImageField(upload_to='images/')
    transformation = models.CharField(max_length=4, default='')
