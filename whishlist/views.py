from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jewelleries.models import Jewellery
from .models import WishList


@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    wishlist = None
    try:
        wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'whishlist/whishlist.html', context)


@login_required
def add_to_wishlist(request, jewellery_id):
    """
    Add a jewellery product from the store to the
    wishlist for the logged in user
    """
    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)
    wishlist, _ = WishList.objects.get_or_create(user=request.user)
    if jewellery not in wishlist.jewelleries.all():
        wishlist.jewelleries.add(jewellery)
        messages.info(request, "A new jewellery was added to your wishlist")
    else:
        messages.info(request, "This jewellery is already in your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, jewellery_id):
    """
    Add a product from the store to the
    wishlist for the logged in user
    """
    wishlist = WishList.objects.get(user=request.user)
    jewellery = get_object_or_404(Jewellery, pk=jewellery_id)

    wishlist.jewelleries.remove(jewellery)
    messages.info(request, "A jewellery was removed from your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))
