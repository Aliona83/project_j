from django.shortcuts import render
from .models import Jewellery, Category


# Create your views here.
def all_jewelleries(request):
   """  A view to show all jewelleries, including sorting and search queries """
    
   jewelleries = Jewellery.objects.all()

   context = {
        'jewelleries': jewelleries,
    }
   return render(request, 'jewelleries/jewelleries.html', context)