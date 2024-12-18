from django.db import models

class Listings(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

    def __str__(self):
        return self.title
