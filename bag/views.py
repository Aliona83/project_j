from django.shortcuts import render, redirect, reverse,  HttpResponse, get_object_or_404
from django.contrib import messages
from jewelleries.models import Jewellery

# Create your views here.
def view_bag(request):
    """ A view that render the bag content page"""

    return render(request, 'bag/bag.html')
    
def add_to_bag(request, item_id):
    """
    A view to allow the users to add items to the bag
    with a quantity of their choosing
    """

    jewellery = get_object_or_404(Jewellery, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    current_item_count = sum(bag.values())

    # Check if adding the new item would exceed the limit
    if current_item_count + quantity > 2:
        messages.error(request, 'You are allowed to buy only 2 items at the same time.')
        return redirect(redirect_url, status=400)

    if item_id in bag:
        bag[item_id] += quantity
        messages.success(request, f'Updated {jewellery.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {jewellery.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {jewellery.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {jewellery.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    A view to allow the users the change the quantity of the product
    to a specified amount.
    """

    jewellery = get_object_or_404(Jewellery, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {jewellery.name} {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {jewellery.name}')

    request.session['bag'] = bag
    return redirect(reverse('bag:view_bag'))


def remove_from_bag(request, item_id):
    """
    A view to allow the users to remove an item from the bag
    irrespective of the quantity.
    """

    try:
        jewellery  = get_object_or_404(Jewellery, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {jewellery.name}')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)