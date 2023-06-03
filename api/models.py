from django.db import models


class Request(models.Model):
    photo = models.ImageField()
    user = models.CharField(max_length=123)