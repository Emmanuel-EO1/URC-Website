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
    team_members= TeamMember.objects.filter(is_featured=True).order_by('position')

    for idx, prop in enumerate(team_members):
        prop.aos_delay= (idx + 1) * 200

    context= {
        'team_members': team_members,
    }

    return render(request, 'pages/about.html', context)