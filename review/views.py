
from django.shortcuts import redirect, get_object_or_404, render
from jewelleries.models import Jewellery 
from .models import Review

def add_review(request, id):
    if request.user.is_authenticated:
       jewellery = Jewellery.objects.get(id=id)
       if request.method == "POST":
           form = ReviewForm(requests.POST or None)
           if form.is_valid():
                data = form.save(commit = False)
                data.comment = request.POST('comment')
                data.rate = request.POST('rate')
                data.user = request.user
                data.jewellery = jewellery
                data.save()
                return redirect("jewelleries:jewelleries_details", id)
           else:
                form = ReviewForm()
           return render(request, 'jewelleries_details.html', {"form":form})
       else: 
            return redirect("accounts:login")   

# def submit_review(request, jewellery_id):
#     print("Submit Review View Called!") 
#     jewellery = get_object_or_404(Jewellery, pk=jewellery_id)
#     reviews = Review.objects.filter(jewellery=jewellery)
       
#     if request.method == 'POST':
#         comment = request.POST.get('comment')
#         rate = request.POST.get('rate')
#         user = request.user  # Assuming you're using authentication

#         # Create a new review
#         review = Review.objects.create(
#             user=user,
#             jewellery=jewellery,
#             comment=comment,
#             rate=rate
#         )
#          # Print debug information
#         print(f"Comment: {comment}")
#         print(f"Rate: {rate}")
#         print(f"User: {user}")
#         print(f"Jewellery ID: {jewellery_id}")
#         print(f"Review ID: {review.id}")
#         template = 'jewelleries/jewelleries_details.html'
#         # Redirect back to the product details page
#         context = {
#         'jewellery': jewellery,
#         'review' : submit_review
       
#     }
#         return render(request, template,context)
#     else:
#         # Handle non-POST requests (if necessary)
#         pass


