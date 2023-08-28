from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomJewelleryDesign
from .forms import CustomJewelleryDesignForm

def custom_jewellery_list(request):
    designs = CustomJewelleryDesign.objects.all()
    return render(request, 'customjewellery/design_list.html', {'designs': designs})

def custom_jewellery_detail(request, design_id):
    design = get_object_or_404(CustomJewelleryDesign, pk=design_id)
    return render(request, 'customjewellery/design_detail.html', {'design': design})

def create_custom_jewellery(request):
    if request.method == 'POST':
        form = CustomJewelleryDesignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customjewellery:design_list')
    else:
        form = CustomJewelleryDesignForm()
    return render(request, 'customjewellery/create_design.html', {'form': form})
