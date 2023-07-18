from django.shortcuts import render
from .models import Jewellery, Category
from django.shortcuts import get_object_or_404


# Create your views here.
def all_jewelleries(request):
   """  A view to show all jewelleries, including sorting and search queries """
    
   jewelleries = Jewellery.objects.all()

   context = {
        'jewelleries': jewelleries,
    }
   return render(request, 'jewelleries/jewelleries.html', context)


def jewelleries_details(request, jewellery_id):
   """  A view to show individual product details """
    
   jewellery = get_object_or_404(Jewellery, pk=jewellery_id)

   context = {
        'jewellery': jewellery,
    }
   return render(request, 'jewelleries/jewelleries_details.html', context)