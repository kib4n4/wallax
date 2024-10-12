from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about', views.about, name='about'), # About page
    path('contact', views.contact, name='contact'),  # Contact page
    path('properties', views.properties, name='properties'),  # Properties page (list all listings)
    path('listing/<int:pk>/', views.listing_retrieve, name='listing_retrieve'),  # Retrieve a specific listing
    path('listing/create/',views.listing_create, name='listing_create'), # Create a new listing
    path('listing/update/<int:pk>/',views.listing_update, name='listing_update'), # Update a specific listing
    path('listing/delete/<int:pk>/', views.listing_delete, name='listing_delete'), # Delete a specific listing
]
