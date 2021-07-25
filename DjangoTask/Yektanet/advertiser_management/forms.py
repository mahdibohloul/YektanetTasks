from django import forms

from .models import Ad


class CreateAdForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Ad
        fields = ['advertiser', 'image', 'title', 'link']
