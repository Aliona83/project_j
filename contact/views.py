from django.shortcuts import render

# Create your views here.from django.shortcuts import render, redirect
from .forms import ContactForm
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required

from django.contrib import messages

@login_required
def contact(request):
     
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your enquiry was sent successfully. \
                Please allow up to 2 working days for a response.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'There was an error sending your enquiry. \
            Please ensure all fields are valid and try again.')
            return redirect('contact')

    else:
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'contact_name': user.user,
                    'contact_email': user.user.email,
                    'contact_phone_number': user.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()

    template = 'contact/contact.html'
    user = request.user

    context = {
        'contact_name': user.get_full_name(),
        'form': contact_form,
    }

    return render(request, template, context)