# from django.shortcuts import render, redirect, reverse
# from .forms import CustomJewelleryDesignForm
 
# from django.contrib import messages

# def create_custom_jewellery(request):
#     if request.method == 'POST':
#         form = CustomJewelleryDesignForm(request.POST, request.FILES)
#         if form.is_valid():
#             custom_design = form.save(commit=False)
#             custom_design.user = request.user  # Assign the logged-in user
#             custom_design.save()

#             customer_details = CustomerDetails(
#                 user_profile=request.user.userprofile,
#                 full_name=form.cleaned_data['full_name'],
#                 email=form.cleaned_data['email'],
#                 phone_number=form.cleaned_data['phone_number'],
#                 county=form.cleaned_data['county'],
#                 postcode=form.cleaned_data['postcode'],
#                 town_or_city=form.cleaned_data['town_or_city'],
#                 street_address1=form.cleaned_data['street_address1'],
#                 street_address2=form.cleaned_data['street_address2'],
#             )
#             customer_details.save()

#             messages.success(request, 'Successfully submit your form!')
#             return redirect(reverse('CustomOrder:submitted_success'))
#         else:
#             messages.error(request, 'Failed to submit form. Please ensure the form is valid.')
#             return redirect(reverse('CustomOrder:submitted_success', args=[user.id]))
#     else:
#         form = CustomJewelleryDesignForm()

#     context = {'form': form}
#     return render(request, 'CustomOrder/design_jewellery.html', context)

# def submitted_success(request):
#     return render(request, 'CustomOrder/submitted_success.html')

# def view_submitted_forms(request):
#     user_submissions = CustomJewelleryDesign.objects.filter(user=request.user)  
#     context = {'user_submissions': user_submissions}
#     return render(request, 'CustomOrder/submitted_forms.html', context)

from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import CustomJewelleryDesignForm
from .models import CustomJewelleryDesign
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from profiles.forms import UserProfileForm


def create_custom_jewellery(request):
    if request.method == 'POST':
        form = CustomJewelleryDesignForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.save(commit=False)
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                design.user_profile = user_profile
                design.save()
            messages.success(request, 'Successfully submit your form!')
            return redirect(reverse('CustomOrder:submitted_success'))
        else:
            messages.error(request, 'Failed to submit form. Please ensure the form is valid.')
            return redirect('CustomOrder:submitted_success')  
    else:
        form = CustomJewelleryDesignForm()
    
    context = {'form': form}
    return render(request, 'CustomOrder/design_jewellery.html', context)

def submitted_success(request):
     return render(request, 'CustomOrder/submitted_success.html')



def view_submitted_forms(request):
    custom_orders = CustomJewelleryDesign.objects.all()
    context = {'custom_orders': custom_orders}
    return render(request, 'CustomOrder/submitted_forms.html', context)
