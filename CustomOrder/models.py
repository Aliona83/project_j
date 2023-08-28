from django.db import models
from jewelleries.models import Jewellery  # Import the Jewellery model from your existing app
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from profiles.models import UserProfile  # Import the UserProfile model from your existing app

class CustomJewelleryDesign(models.Model):
    JEWELLERY_TYPE_CHOICES = (
        ('ring', 'Ring'),
        ('necklace', 'Necklace'),
        ('earrings', 'Earrings'),
    )
    
    METAL_TYPE_CHOICES = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
    )
    
    STONE_TYPE_CHOICES = (
        ('diamond', 'Diamond'),
        ('emerald', 'Emerald'),
        ('ruby', 'Ruby'),
        ('sapphire', 'Sapphire'),
        ('other', 'Other'),
    )

    design_name = models.CharField(max_length=100)
    jewellery_type = models.CharField(max_length=20, choices=JEWELLERY_TYPE_CHOICES)
    metal_type = models.CharField(max_length=20, choices=METAL_TYPE_CHOICES)
    stone_type = models.CharField(max_length=20, choices=STONE_TYPE_CHOICES)
    description = models.TextField()
    design_image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.design_name

    
    def __str__(self):
        return self.design_name


class CustomerDetails(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='customer_details')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    
    # Add any other fields you need for customer details
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"

