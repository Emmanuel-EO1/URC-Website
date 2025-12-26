from django.shortcuts import render
from . models import Service
# Create your views here.

def service_index(request):
    all_services= Service.objects.all().order_by('title') 

    context= {
        'services': all_services,
    }

    return render(request, 'services/service_index.html', context)