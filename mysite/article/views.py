from django.shortcuts import render
from django.http import HttpResponse
from article.models import article
from django.http import Http404
from django.db.models import Q

# Create your views here.


def index(request):

    article_list = article.objects.all()

    category_list = article.objects.order_by('category').values_list('category', flat=True).distinct()

    context = {'article_list': article_list, 'category_list': category_list}

    return render(request, 'index.html', context)


def article_detail(request, id):

    category_list = article.objects.order_by('category').values_list('category', flat=True).distinct()

    try:
        a = article.objects.get(id=id)
        a.visit += 1
        a.save()
    except article.DoesNotExist:
        raise Http404('This article does not exist')

    return render(request, 'article_detail.html', {
       'article' : a, 'category_list': category_list
    })


def article_category(request, category):
    category_list = article.objects.order_by('category').values_list('category', flat=True).distinct()
    try:
        a = article.objects.filter(category=category)
    except article.DoesNotExist:
        raise Http404('This category does not exist')
    return render(request, 'index.html', {
       'article_list': a, 'category_list': category_list
    })

def article_search(request, search):
    category_list = article.objects.order_by('category').values_list('category', flat=True).distinct()
    try:
        a = article.objects.filter(Q(title__contains=search) | Q(content__contains=search))
    except article.DoesNotExist:
        raise Http404('This category does not exist')
    return render(request, 'index.html', {
       'article_list': a, 'category_list': category_list
    })