from django.shortcuts import render, get_object_or_404, redirect
from .models import Listings
from .forms import ListingForm


# Home View
def home(request):
    listings = Listings.objects.all()
    context = {'listings': listings}
    return render(request, 'home.html', context)

# About Page View
def about(request):
    return render(request, 'about.html')

# Contact Page View
def contact(request):
    return render(request, 'contact.html')

# Properties List View
def properties(request,pk=None):
    slide =get_object_or_404(Listings,pk=pk) if pk else None
    listings = Listings.objects.all()
    context = {'listings': listings,
               'slide' : slide,
               }
    return render(request, 'properties.html', context)

# Retrieve Listing Detail
def listing_retrieve(request, pk):
    listing = get_object_or_404(Listings, id=pk)
    context = {'listing': listing}
    return render(request, 'listing_detail.html', context)

# Create Listing
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListingForm()
    context = {"form": form}
    return render(request, 'listing_create.html', context)

# Update Listing
def listing_update(request, pk):
    listing = get_object_or_404(Listings, id=pk)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListingForm(instance=listing)
    context = {"form": form, "listing": listing}
    return render(request, 'listing_update.html', context)

# Delete Listing
def listing_delete(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.delete()
    return redirect('home')

