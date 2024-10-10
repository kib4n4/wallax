from django.db import models

# Create your models here.

class Listings(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField()
    address = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

    def __str__(self):
        return self.title

                             