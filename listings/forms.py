from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'name',
            'description',
            'brand',
            'milage',
            'price',
            'image'
        ]
