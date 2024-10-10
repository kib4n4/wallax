from django.shortcuts import render, get_object_or_404, redirect  # Added redirect import
from .models import Listings
from .forms import ListingForm

def home(request):
    listings = Listings.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'home.html', context)

def listing_retrieve(request, pk):
    listing = get_object_or_404(Listings, id=pk)  # Use get_object_or_404 for safety
    context = {
        'listing': listing
    }
    return render(request, 'listing_detail.html', context)  # Create a separate template for listing details

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after creating a new listing
    else:
        form = ListingForm()  # Only create a new form if the request is not POST
    context = {
        "form": form
    }
    return render(request, 'listing_create.html', context)

def listing_update(request, pk):
    listing = get_object_or_404(Listings, id=pk)  # Use get_object_or_404 for safety
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)  # Bind the form to the existing listing
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after updating the listing
    else:
        form = ListingForm(instance=listing)  # Populate the form with the existing listing data
    context = {
        "form": form,
        "listing": listing
    }
    return render(request, 'listing_update.html', context)
def listing_delete(request, pk):
    listing= Listings.objects.get(id=pk)
    listing.delete()
    return redirect('home')  # Redirect to the home page after deleting the listing