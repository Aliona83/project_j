from django.shortcuts import render, reverse, redirect
from .models import Jewellery, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q 
from django.contrib import messages
from django.db.models.functions import Lower


# Create your views here.
def all_jewelleries(request):
   """  A view to show all jewelleries, including sorting and search queries """
    
   jewelleries = Jewellery.objects.all()
   query = None
   categories = None
   sort = None
   direction = None

   if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                jewelleries= jewelleries.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            jewelleries = jewelleries.order_by(sortkey)


   if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            jewelleries = jewelleries.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

   if request.GET:
       if 'q' in request.GET:
           query = request.GET['q']
           if not query:
               messages.error(request, 'You didnt enter search criteria !')
               return redirect(reverse('jewelleries:jewelleries'))
            
           queries = Q(name__icontains=query) | Q(description__icontains=query)
           jewelleries = jewelleries.filter(queries)

   current_sorting = f'{sort}_{direction}'
   context = {
        'jewelleries': jewelleries,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
   return render(request, 'jewelleries/jewelleries.html', context)


def jewelleries_details(request, jewellery_id):
   """  A view to show individual product details """
    
   jewellery = get_object_or_404(Jewellery, pk=jewellery_id)

   context = {
        'jewellery': jewellery,
    }
   return render(request, 'jewelleries/jewelleries_details.html', context)