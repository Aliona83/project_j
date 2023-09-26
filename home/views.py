from django.shortcuts import render
from jewelleries.models import Jewellery, Category
import random


def index(request):
    """ A view to return the index page """

    try:
        new_arrivals_category = Category.objects.get(name='new_arrivals')
    except Category.DoesNotExist:
        new_arrivals_category = None

    featured_jewellery = []
    if new_arrivals_category:
        featured_jewellery = list(
            Jewellery.objects.filter(
                category=new_arrivals_category, is_featured=True))
        random.shuffle(featured_jewellery)
        num_products_to_display = min(3, len(featured_jewellery))
        random_featured_jewellery = random.sample(
            featured_jewellery, num_products_to_display)

    else:
        random_featured_jewellery = []

    context = {
        'featured_jewellery': random_featured_jewellery,
    }
    return render(request, 'home/index.html', context)
