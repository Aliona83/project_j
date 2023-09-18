from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Jewellery, Category
from .forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
# from django.core.paginator import Paginator


def all_jewelleries(request):
    """ A view to show all jewelleries, including sorting and search queries """
    jewelleries = Jewellery.objects.all()
  

    query = None
    categories = None
    sort = None
    direction = None
    
    sort = request.GET.get('sort')
    direction = request.GET.get('direction')

    # Define a default sorting option and direction if not provided
    default_sort = 'name'  # Default to sorting by name
    default_direction = 'asc'  # Default to ascending order

    # Define a mapping of sorting options to model fields
    sorting_options = {
        'price_asc': 'price',
        'price_desc': '-price',
        'rating_asc': 'rating',
        'rating_desc': '-rating',
        'name_asc': 'name',
        'name_desc': '-name',
        'category_asc': 'category__name',
        'category_desc': '-category__name',
    }

    # Use the selected sorting option or default to 'name' if not provided
    sortkey = sorting_options.get(sort, default_sort)

    # Update the sortkey based on the sorting direction
    if direction == 'desc':
        sortkey = f'-{sortkey}'

    # Update the queryset to order by the selected sorting option and direction
    jewelleries = jewelleries.order_by(sortkey)
 

 
    # if request.GET:
    #     if 'sort' in request.GET:
    #         sortkey = request.GET['sort']
    #         sort = sortkey
    #         if sortkey == 'name':
    #             sortkey = 'lower_name'
    #             jewelleries = jewelleries.annotate(lower_name=Lower('name'))
    #         if sortkey == 'category':
    #             sortkey = 'category__name'
    #         if 'direction' in request.GET:
    #             direction = request.GET['direction']
    #             if direction == 'desc':
    #                 sortkey = f'-{sortkey}'
    #         jewelleries = jewelleries.order_by(sortkey)
            
    if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            jewelleries = jewelleries.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            print(categories)

    if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('jewelleries'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            jewelleries = jewelleries.filter(queries)
            
    # all_jewellery_param = request.GET.get('all_jewellery')
    # page = request.GET.get('page', 1)
    # paginator = Paginator(jewelleries, 15)  # Show 15 jewelleries per page
    
    # if all_jewellery_param == 'true':
    #     paginator = Paginator(jewelleries, 12)  # Define your desired number of items per page
    #     page_number = request.GET.get('page')
    #     jewelleries = paginator.get_page(page_number)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(jewelleries, 15)  # Show 15 jewelleries per page

    try:
        jewelleries = paginator.page(page_number)
    except PageNotAnInteger:
        # If the 'page' parameter is not an integer, default to page 1
        jewelleries = paginator.page(1)
    except EmptyPage:
        # If the 'page' parameter is out of range, display the last page
        jewelleries = paginator.page(paginator.num_pages)

    
    current_sorting = f'{sort}_{direction}'
    

    context = {
        'jewelleries': jewelleries,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        # 'all_jewellery_param': all_jewellery_param,
    }

    return render(request, 'jewelleries/jewelleries.html', context)

def jewelleries_details(request, jewellery_id):
    """ A view to show individual product details """

    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)

    context = {
        'jewellery': jewellery,
    }

    return render(request, 'jewelleries/jewelleries_details.html', context)
   
@login_required
def add_jewellery(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('jewelleries:add_jewellery'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'jewelleries/add_jewellery.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def edit_jewellery(request, jewellery_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=jewellery)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('jewelleries:jewelleries_details', args=[jewellery.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=jewellery)
        messages.info(request, f'You are editing {jewellery.name}')

    template = 'jewelleries/edit_jewellery.html'
    context = {
        'form': form,
        'jewellery': jewellery,
    }
    return render(request, template, context)

@login_required
def delete_jewellery(request, jewellery_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)
    jewellery.delete()
    messages.success(request, 'Jewellery was successfully deleted!')
    return redirect(reverse('jewelleries:jewelleries'))
