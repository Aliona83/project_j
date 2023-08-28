from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomJewelleryDesign(models.Model):
    JEWELLERY_TYPES = (
        ('ring', 'Ring'),
        ('necklace', 'Necklace'),
        ('earring', 'Earring'),
    )

    METAL_TYPES = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jewellery_type = models.CharField(max_length=20, choices=JEWELLERY_TYPES)
    stone_type = models.CharField(max_length=50)
    metal_type = models.CharField(max_length=20, choices=METAL_TYPES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Contact Information
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=20)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Custom {self.jewellery_type.capitalize()} Design by {self.name} {self.surname}"