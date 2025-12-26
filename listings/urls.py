from django.urls import path 
from . import views

urlpatterns = [
    path('', views.listing_index, name='listings'),
    path('<slug:property_slug>/', views.listing_detail, name='listing_detail'),
]