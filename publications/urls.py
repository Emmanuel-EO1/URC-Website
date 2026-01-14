from django.urls import path
from . import views

app_name = 'publications'

urlpatterns= [
    path('', views.article_list, name='articles'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]