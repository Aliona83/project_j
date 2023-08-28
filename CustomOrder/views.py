from django.shortcuts import render, redirect, reverse
from .forms import CustomJewelleryDesignForm
from .models import CustomJewelleryDesign 
from django.contrib import messages

def create_custom_jewellery(request):
    if request.method == 'POST':
        form = CustomJewelleryDesignForm(request.POST, request.FILES)
        if form.is_valid():
            custom_design = form.save(commit=False)
            custom_design.user = request.user  # Assign the logged-in user
            custom_design.save()

            messages.success(request, 'Successfully submit your form!')
            return redirect(reverse('jewelleries:jewelleries'))
        else:
            messages.error(request, 'Failed to submit form. Please ensure the form is valid.')
            return redirect(reverse('CustomOrder:submitted_success', args=[user.id]))
    else:
        form = CustomJewelleryDesignForm()

    context = {'form': form}
    return render(request, 'CustomOrder/design_jewellery.html', context)

def submitted_success(request):
    return render(request, 'CustomOrder/submitted_success.html')

def view_submitted_forms(request):
    user_submissions = CustomJewelleryDesign.objects.filter(user=request.user)  
    context = {'user_submissions': user_submissions}
    return render(request, 'CustomOrder/submitted_forms.html', context)

