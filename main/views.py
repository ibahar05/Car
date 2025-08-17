from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import *
from users.forms import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from importlib import reload


def main(request):
    return render(request,"views/main.html")
from django.shortcuts import render
from .models import Listing
from .filters import *


@login_required
def home(request):
    # همیشه در ابتدای تابع مقداردهی می‌کنیم
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset = listings)

    context = {
        'listing_filter': listing_filter,
    }
    return render(request, "views/home.html", context)



@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('main:home')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()

    return render(request, 'views/list.html', {"listing_form":listing_form,"location_form": location_form})



@login_required
def listing_view(request,id):
    try:
        listing = Listing.objects.get(id=id)
        return render(request,'views/listing.html', {'listing': listing, })
    except ObjectDoesNotExist:
        messages.error(request, f'Invalid UID {id} was provided for listing.')
        return redirect('main:home')
    
@login_required
def edit_view(request,id):
    try:
        listing = Listing.objects.get (id = id)

        if listing is None:
            raise Exception()
        
        if request.method == "POST":
            listing_form = ListingForm(request.POST, request.FILES,instance =listing)
            location_form = LocationForm(request.POST,instance=listing.location)
            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.info(request, f" listing {id} updated succesfully")
                return redirect ("main:home")
            else:
                messages.error(request, "An error occured while trying update the listing.")
                return reload()
        else:
            listing_form = ListingForm(instance =listing)
            location_form = LocationForm(instance=listing.location)
            context= {
                "listing_form":listing_form,
                "location_form":location_form,
            }
        return render(request, "views/edit.html", context)
    
    except Exception as e:
        messages.error(request, "An error occured while trying update the listing.")
        return redirect("home:main")
