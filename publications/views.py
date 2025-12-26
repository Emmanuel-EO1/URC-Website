from django.shortcuts import render, get_object_or_404
from . models import Article
from django.core.paginator import Paginator

# Create your views here.

def article_index(request):
    all_articles= Article.objects.order_by('publish_date').filter(is_published=True)
    paginator= Paginator(all_articles, 9)
    page= request.GET.get('page')
    paged_articles= paginator.get_page(page)

    context= {
        'articles': paged_articles,
        'is_paginated': paged_articles.has_other_pages(),
    }

    return render(request, 'publications/article_index.html', context)

def article_detail(request, article_slug):
    article= get_object_or_404(Article.objects.filter(is_published=True), slug=article_slug)
    recent_articles= Article.objects.exclude(pk=article.pk).order_by('publish_date')[:3]

    context= {
        'article': article,
        'recent_articles': recent_articles,
    }

    return render(request, 'publications/article_detail.html', context)