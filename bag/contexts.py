from decimal import Decimal
from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from jewelleries.models import Jewellery

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

   # Calculate the total amount in the bag_items list
    for item_id, quantity in bag.items():
        product = get_object_or_404(Jewellery, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Check if the total is greater than or equal to 1000 euros to apply the discount
    discount = 0

    if total >= 1000:
        discount = (total // 1000 ) * settings.DISCOUNT_PER_1000_EURO

    # Calculate the grand total after applying the discount
    grand_total = total - discount
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'discount_amount': settings.DISCOUNT_PER_1000_EURO
    }

    return context