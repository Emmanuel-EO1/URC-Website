from django.urls import path
from . import views

urlpatterns= [
    path('', views.service_index, name='services')
]