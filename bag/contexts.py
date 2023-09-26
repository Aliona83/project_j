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
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Jewellery, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Jewellery, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                })
    discount = 0
    if total > 1000:
        discount = 100

    # Calculate the grand total after applying the discount
    grand_total = total - discount
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'discount': discount
    }

    return context
