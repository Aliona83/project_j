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
    """ A view to show all products, including sorting and search queries """
    
    query = None
    categories = None
    sort = None

    category_filter = request.GET.get('category')
    sort = request.GET.get('sort')
    direction = request.GET.get('direction')

    # Get all jewellery items
    jewelleries = Jewellery.objects.all()

    # Apply category filter if present
    if category_filter:
        jewelleries = jewelleries.filter(category__name=category_filter)

    # Apply sorting
    if sort and direction:
        if direction == 'asc':
            jewelleries = jewelleries.order_by(sort)
        elif direction == 'desc':
            jewelleries = jewelleries.order_by(f'-{sort}')

    # Pagination
    paginator = Paginator(jewelleries, 12)  # Show 12 items per page
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)
        

    context = {
        'jewelleries': page_obj,
        'current_categories': Jewellery.objects.all(),
        'current_sorting': f'{sort}_{direction}' if sort and direction else 'None_None',
        'search_term': category_filter,
        'page_obj': page_obj,
    }

    return render(request, 'jewelleries/jewelleries.html', context)
    # direction = None
    
    # jewelleries = Jewellery.objects.all()

    # paginator = Paginator(jewelleries, 16)  # Show 25 contacts per page.

    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # # return render(request, "jewelleries/jewelleries.html", {"page_obj": page_obj})
    # categories = request.GET.getlist('category')
   

    # if request.GET:
    #     if 'sort' in request.GET:
    #         sortkey = request.GET['sort']
    #         sort = sortkey
    #         if sortkey == 'name':
    #             sortkey = 'lower_name'
    #             jewelleries= jewelleries.annotate(lower_name=Lower('name'))
    #         if sortkey == 'category':
    #             sortkey = 'category__name'
    #         if 'direction' in request.GET:
    #             direction = request.GET['direction']
    #             if direction == 'desc':
    #                 sortkey = f'-{sortkey}'
    #         jewelleries = jewelleries.order_by(sortkey)
            
    #     if 'category' in request.GET:
            
    #         categories = request.GET['category'].split(',')
    #         jewelleries = jewelleries.filter(category__name__in=categories)
    #         categories = Category.objects.filter(name__in=categories)

    #     if 'q' in request.GET:
    #         query = request.GET['q']
    #         if not query:

    #             messages.error(request, "You didn't enter any search criteria!")
    #             return redirect(reverse('products'))
            
    #         queries = Q(name__icontains=query) | Q(description__icontains=query)
    #         jewelleries = jewelleries.filter(queries)

            

    # current_sorting = f'{sort}_{direction}'



    # context = {
    #     'jewelleries': jewelleries,
    #     'search_term': query,
    #     'current_categories': categories,
    #     'current_sorting': current_sorting,
    #     'page_obj': page_obj
         
        
       
    # }

    # return render(request, 'jewelleries/jewelleries.html', context)

# def load_more_products(request):
#     # Get the page number from the 'load_more' parameter in the request's GET data
#     page_number = request.GET.get('load_more')
    
#     # Calculate the range of products to load based on the page number
#     items_per_page = 12
#     start_index = (int(page_number) - 1) * items_per_page
#     end_index = start_index + items_per_page

#     # Query the database to retrieve the products for the current page
#     products = Jewellery.objects.all()[start_index:end_index]
#     # print(products)
#     # Render the products as HTML
#     product_html = render(request, 'jewelleries/jewelleries_list.html', {'jewelleries': products})

#     return JsonResponse({'jewelleries.html': all_jewelleries.content.decode('utf-8')})


def jewelleries_details(request, jewellery_id):
    """ A view to show individual product details """

    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)

    context = {
        'jewellery': jewellery,
    }

    return render(request, 'jewelleries/jewelleries_details.html', context)

# def jewelleries_details(request, product_id):
#     """ A view to show individual product details """

#     jewellery = get_object_or_404(Jewellery, pk=jewellery_id)

#     context = {
#         'jewellery': jewellery,
#     }

#     return render(request, 'jewelleries/jewelleries_detail.html', context)
   

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
