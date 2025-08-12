import django_filters # type: ignore

from .models import Listing

class ListingFilter(django_filters.FilterSet):
    
    class Meta:
        model = Listing
        fields = {"brand":{"exact"},"transmisson": {"exact"},"mileage": {"lt"}, }
