from django.shortcuts import render
from .forms import CustomJewelleryDesignForm

def create_custom_jewellery(request):
    if request.method == 'POST':
        form = CustomJewelleryDesignForm(request.POST, request.FILES)
        if form.is_valid():
            custom_design = form.save()
    else:
        form = CustomJewelleryDesignForm()

    context = {'form': form}
    return render(request, 'CustomOrder/design_jewellery.html', context)


def view_submitted_forms(request):
    user_submissions = CustomJewelleryDesign.objects.filter(user=request.user)  # Filter submissions by the current user
    context = {'user_submissions': user_submissions}
    return render(request, 'submitted_forms.html', context)

