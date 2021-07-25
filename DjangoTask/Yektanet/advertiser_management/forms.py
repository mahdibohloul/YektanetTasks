from django import forms

from .models import Ad, Advertiser


class CreateAdvertiserForm(forms.ModelForm):
    class Meta:
        model = Advertiser
        fields = ['name']


class CreateAdForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Ad
        fields = ['advertiser', 'image', 'title', 'link']
