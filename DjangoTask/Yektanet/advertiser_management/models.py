from django.db import models
from PIL import Image
from django.urls import reverse
from django.db.models.functions import Trunc


class Advertiser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_approved_ads(self):
        return self.ads.filter(approved=True)

    def get_total_clicks(self):
        ads = self.ads.all()
        clicks_count = sum(ad.total_clicks() for ad in ads)
        return clicks_count

    def get_total_views(self):
        ads = self.ads.all()
        views_count = sum(ad.total_views() for ad in ads)
        return views_count

    get_total_views.short_description = 'Total views'
    get_total_clicks.short_description = 'Total clicks'


class Ad(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='ad_pics')
    link = models.URLField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def inc_clicks(self, ip_addr):
        Click.objects.create(ad=self, ip=ip_addr)

    def inc_views(self, ip_addr):
        View.objects.create(ad=self, ip=ip_addr)

    def save(self, **kwargs):
        super().save(**kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def total_clicks(self):
        return self.clicks.count()

    def total_views(self):
        return self.views.count()

    def get_absolute_url(self):
        return reverse('ad-detail', kwargs={'pk': self.pk})

    @property
    def ctr(self):
        return round(self.total_clicks() / self.total_views(), 2)


class Click(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='clicks')
    created_on = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return f'{self.ad.title} clicked by {self.ip} in {self.created_on}'


class View(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='views')
    created_on = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return f'{self.ad.title} viewed by {self.ip} in {self.created_on.strftime("%m/%d/%Y, %H:%M")}'
