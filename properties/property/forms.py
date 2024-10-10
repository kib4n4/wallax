from django.forms import ModelForm
from .models import Listings


class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = '__all__'  # Include all fields from the model