from django.shortcuts import render, redirect
from .forms import CustomJewelleryDesignForm

def create_custom_jewellery(request):
    if request.method == 'POST':
        form = CustomJewelleryDesignForm(request.POST, request.FILES)
        if form.is_valid():
            custom_design = form.save()
            return redirect('CustomOrder:submitted_success', design_name=custom_design.design_name)
    else:
        form = CustomJewelleryDesignForm()

    context = {'form': form}
    return render(request, 'CustomOrder/design_jewellery.html', context)

def submitted_success(request):
    return render(request, 'CustomOrder/submitted_success.html', context)

def view_submitted_forms(request):
    user_submissions = CustomJewelleryDesign.objects.filter(user=request.user)  
    context = {'user_submissions': user_submissions}
    return render(request, 'CustomOrder/submitted_forms.html', context)

