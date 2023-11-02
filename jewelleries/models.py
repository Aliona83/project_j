from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Jewellery(models.Model):

    class Meta:
        verbose_name_plural = 'Jewelleries'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_featured = models.BooleanField(
        default=True, verbose_name="Feature on Home Page")
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    gold_karats = models.PositiveIntegerField(default=24)
    diamond_carats = models.FloatField(null=True, blank=True)
    diamond_shape = models.CharField(
        max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ReviewRating(models.Model):
    jewellery = models.ForeignKey(Jewellery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=False)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.jewellery.name} by {self.user.username}"
