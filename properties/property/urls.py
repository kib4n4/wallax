from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page

    # Properties: Optional pk for a specific listing in the carousel
    path('properties/<int:pk>/', views.properties, name='property_detail'),  # View specific property in carousel
    path('properties/', views.properties, {'pk': None}, name='properties_list'),  # View all properties

    # Listings
    path('listing/<int:pk>/', views.listing_retrieve, name='listing_retrieve'),  # View listing details
    path('listing/create/', views.listing_create, name='listing_create'),  # Create a new listing
    path('listing/update/<int:pk>/', views.listing_update, name='listing_update'),  # Update an existing listing
    path('listing/delete/<int:pk>/', views.listing_delete, name='listing_delete'),  # Delete a listing
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
