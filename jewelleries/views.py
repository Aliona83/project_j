from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Jewellery, Category, ReviewRating
from .forms import ProductForm, ReviewForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse





def all_jewelleries(request):
    """ A view to show all jewelleries, '
    'including sorting and search queries """
    jewelleries = Jewellery.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    sort_key = 'name'  
    direction = 'asc'  


    if request.GET:
        valid_sort_keys = ['price', 'rating', 'name', 'category']
        default_sort = 'name'
        default_direction = 'asc'
        sort = request.GET.get('sort', 'name')
        direction = request.GET.get('direction', 'asc')
        if sort not in valid_sort_keys:
            sort = default_sort

        sort_key_mapping = {
            'name': 'name',
            'category': 'category__name',
            'price': 'price',
            'rating': 'rating',
        }

        model_sort_field = sort_key_mapping.get(sort, default_sort)

        if direction == 'desc':
            jewelleries = jewelleries.order_by(model_sort_field)
            model_sort_field = f'-{model_sort_field}'
        elif direction == 'asc' and sort == 'price':
            jewelleries = jewelleries.order_by('price')

        if 'category' in request.GET:
            categories = request.GET.get('category').split(",")
            if categories:
                category_query = Q()
                for category in categories:
                    category_query |= Q(category__name=category)
            jewelleries = jewelleries.filter(category_query)

        if 'q' in request.GET:
            query = request.GET['q']
            if query:
                if ',' in query:
                    category_names = query.split(',')
                    queries = (
                        Q(name__icontains=query) |
                        Q(description__icontains=query) |
                        Q(category__name__in=category_names)
                    )
                    jewelleries = jewelleries.filter(queries)
                else:
                    queries = (
                        Q(name__icontains=query) |
                        Q(description__icontains=query) |
                        Q(category__name__iexact=query)
                    )
                    jewelleries = jewelleries.filter(queries)
            else:
                messages.error(request,
                               "You didn't enter any search criteria!")
        sort_key = 'name' 
    if sort:
        sort_key = sort

    if direction == 'desc':
        sort_key = f'-{sort_key}'

    jewelleries = jewelleries.order_by(sort_key)



    items_per_page = 15
    paginator = Paginator(jewelleries, items_per_page)
    page_number = request.GET.get('page')

    try:
        jewelleries = paginator.page(page_number)
    except PageNotAnInteger:
        jewelleries = paginator.page(1)
    except EmptyPage:
        jewelleries = paginator.page(paginator.num_pages)
    current_sorting = f'{sort}_{direction}'
    sort, direction = current_sorting.split('_')

    context = {
        'jewelleries': jewelleries,
        'search_term': query,
        'current_categories': categories,
        'sort': sort,
        'direction': direction,
       
    }

    if categories:
        category_param = '&'.join(
          [f'category={category}' for category in categories]
        )
        context['category_param'] = category_param

    return render(request, 'jewelleries/jewelleries.html', context)

def jewelleries_details(request, jewellery_id):
    """ A view to show individual product details """

    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)
    reviews = ReviewRating.objects.filter(jewellery=jewellery)
     
    context = {
        'jewellery': jewellery,
        'reviews': reviews,
    }

    return render(request, 'jewelleries/jewelleries_details.html', context)


@login_required
def submit_review(request, jewellery_id):
    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        print(request)
        try:
            review = ReviewRating.objects.get(user=request.user, jewellery_id=jewellery_id)
            print(review)
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.jewellery = jewellery
                review.user = request.user
                review.ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
                review.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
    return redirect(url)





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
            messages.error(request,
                           'Failed to add product. '
                           'Please ensure the form is valid.')
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
            return redirect(reverse(
                    'jewelleries:jewelleries_details', args=[jewellery.id]))
        else:
            messages.error(request,
                           'Failed to update product. '
                           'Please ensure the form is valid.')
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

