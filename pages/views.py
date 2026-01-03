from django.shortcuts import render
from listings.models import Property, Agent
from .models import TeamMember
# Create your views here.

def home(request):
    featured_properties= Property.objects.order_by('list_date').filter(is_published=True, is_featured=True)[:3]

    for idx, prop in enumerate(featured_properties):
        prop.aos_delay= (idx + 1) * 200

    context={
        'properties': featured_properties,
        'agents': Agent.objects.all(),
    }

    return render(request, 'pages/home.html', context)

def about(request):
    executives= TeamMember.objects.filter(role_type='Executive', is_featured=True).order_by('id')

    management= TeamMember.objects.filter(role_type='Management', is_featured=True).order_by('id')

    for idx, prop in enumerate(executives):
        prop.aos_delay= (idx + 1) * 200

    for idx, prop in enumerate(management):
        prop.aos_delay= (idx + 1) * 200

    context= {
        'executives': executives,
        'management': management,
    }

    return render(request, 'pages/about.html', context)