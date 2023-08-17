from django.shortcuts import render, reverse, redirect
from .models import Jewellery, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .forms import ProductForm

# Import Pagination Stuff
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def all_jewelleries(request):
    """  A view to show all jewelleries, including sorting and search queries """
    jewelleries = Jewellery.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

# Set up Pagination
    p = Paginator(jewelleries, 16)
    page = request.GET.get('page', 1)

    try:
        all_jewellery = p.page(page)
    except (EmptyPage, PageNotAnInteger):
        all_jewellery = p.page(1)
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                jewelleries = jewelleries.annotate(lower_name=Lower('name'))
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
        'all_jewellery': all_jewellery,
    }
    return render(request, 'jewelleries/jewelleries.html', context)


def jewelleries_details(request, jewellery_id):
    """  A view to show individual product details """
    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)

    context = {
        'jewellery': jewellery,
    }
    return render(request, 'jewelleries/jewelleries_details.html', context)

@login_required
def add_jewellery(request):
    """ Add a product to the store """
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
    """ Edit a product in the store """
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
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)
    jewellery.delete()
    messages.success(request, 'Jewellery was successful  deleted!')
    return redirect(reverse('jewelleries:jewelleries'))       
