from django.db import models


# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to="")
    good = models.IntegerField(null=True, blank=True)
    read = models.IntegerField(null=True, blank=True)
    readtext = models.TextField(null=True, blank=True)
