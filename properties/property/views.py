from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f"New message from {name}"
        body = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(subject, body, email, ['wallezhomes.p@gmail.com'], fail_silently=False)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect back to the contact page
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'contact.html')

# Properties List View
def properties(request, pk=None):
    slide = get_object_or_404(Listings, pk=pk) if pk else None
    listings = Listings.objects.all()
    context = {'listings': listings, 'slide': slide}
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
