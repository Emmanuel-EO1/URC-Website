import email
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .tasks import send_async_email

# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)

        if form.is_valid():
            form.save()

            name = request.POST.get('name')
            email = request.POST.get('email')
            
            send_async_email(email, name)
            
            messages.success(request, 'Your inquiry has been successfully submitted! We will respond within 24 hours.')
            return redirect('contact_us')
        
        else:
            messages.error(request, 'Submission failed. Please check the fields and try again.')
    else:
        form= ContactForm()

    context= {
        'form': form,
    }
    return render(request, 'contacts/contact_us.html', context)
