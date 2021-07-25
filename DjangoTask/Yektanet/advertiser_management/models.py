from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=50)
    clicks = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)


class Ad(models.Model):
    title = models.CharField(max_length=50)
    img_url = models.URLField()
    link = models.URLField()
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)

