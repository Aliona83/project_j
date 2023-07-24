from decimal import Decimal
from django.conf import settings
from decimal import Decimal

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

   # Calculate the total amount in the bag_items list
    for item in bag_items:
        total += item['quantity'] * item['price']
        product_count += item['quantity']
    
    # Check if the total is greater than or equal to 1000 euros to apply the discount
    discount = 0

    if total >= 1000:
        discount = settings.DISCOUNT_AMOUNT

    # Calculate the grand total after applying the discount
    grand_total = total - discount
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'discount_amount': settings.DISCOUNT_AMOUNT
    }

    return context