from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404, render
from jewelleries.models import Jewellery 
from .models import Review
from django import forms
from .forms import ReviewForm

def add_review(request, jewellery_id):
    if request.user.is_authenticated:
       jewellery = get_object_or_404(Jewellery, pk=jewellery_id)
       jewellery = Jewellery.objects.get(id=jewellery_id)
       if request.method == "POST":
           form = ReviewForm(request.POST or None)
           
           if form.is_valid():
                data = form.save(commit = False)
                data.comment = request.POST['comment']
                data.rate = request.POST['rate']
                data.user = request.user
                data.jewellery = jewellery
                data.save()
                return redirect("jewelleries:jewelleries_details", jewellery_id=jewellery_id)
           else:
                form = ReviewForm()
           return render(request, 'jewelleries/jewelleries_details.html', {"form":form})
       else: 
            return redirect("accounts:login")   


