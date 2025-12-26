from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from contacts.forms import ContactForm
from .models import Property
from django.core.paginator import Paginator
from listings.models import Agent


# Create your views here.

def listing_index(request):
    queryset_list= Property.objects.order_by('list_date').filter(is_published=True)

    if 'property_type' in request.GET:
        property_type= request.GET['property_type']
        if property_type:
            queryset_list= queryset_list.filter(property_type__iexact=property_type)

    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            queryset_list= queryset_list.filter(city__iexact=city)

    if 'price' in request.GET:
        price= request.GET['price']
        if price:
            queryset_list= queryset_list.filter(price__lte=price)

    if 'agent' in request.GET:
        agent_id= request.GET['agent']
        if agent_id:
            queryset_list= queryset_list.filter(agent__id=agent_id)

    paginator= Paginator(queryset_list, 6)
    page= request.GET.get('page')
    paged_listings= paginator.get_page(page)

    context= {
        'listings': paged_listings,
        'is_paginated': paged_listings.has_other_pages(),
        'search_values':{
            'city': Property.objects.values_list('city', flat=True).distinct(),
            'type': Property.PROPERTY_TYPE_CHOICES,
        },
        'agents': Agent.objects.all(),
    }

    return render(request, 'listings/listing_index.html', context)


def listing_detail(request, property_slug):
    property = get_object_or_404(Property.objects.filter(is_published=True), slug=property_slug)


    if request.method == 'POST':
       
        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, f'Inquiry about "{property.title}" successfully sent! We will respond shortly.')

            return redirect('listing_detail', property_slug=property_slug)
        else:
            messages.error(request, 'Submission failed. Please check the required fields.')

    else:
        # Set the initial 'property' value to the ID of the current property being viewed
        initial_data = {'property': property.id}
        form = ContactForm(initial=initial_data)

    context = {
        'property': property,
        'form': form,
    }

    return render(request, 'listings/listing_detail.html', context)