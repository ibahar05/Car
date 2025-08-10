from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import *
from users.forms import *

def main(request):
    return render(request,"views/main.html")

@login_required
def home(request):
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(request, "views/home.html",context )


@login_required
def list_view(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()

    return render(request, 'views/list.html', {"listing_form":listing_form,"location_from": location_form})