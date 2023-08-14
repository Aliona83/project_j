from django.shortcuts import render
from jewelleries.models import Jewellery



def index(request):
    """ A view to return the index page """
    featured_jewellery = Jewellery.objects.filter(is_featured=True)
    print("Number of featured jewellery items:", featured_jewellery.count())
    context = {
        'featured_jewellery': featured_jewellery,
}
    return render(request, 'home/index.html', context)


