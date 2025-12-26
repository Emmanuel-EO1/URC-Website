from django.urls import path
from . import views

urlpatterns= [
    path('', views.article_index, name='articles'),
    path('<slug:artice_slug>/', views.article_detail, name='article_detail'),
]