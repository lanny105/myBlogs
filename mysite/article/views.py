from django.shortcuts import render
from django.http import HttpResponse
from article.models import article
from django.http import Http404
from django.db.models import Q

# Create your views here.


def index(request):

    article_list = article.objects.all()

    context = {'article_list': article_list}

    return render(request, 'index.html', context)



def article_detail(request, id):


    # print article
    try:
        a = article.objects.get(id=id)
    except article.DoesNotExist:
        raise Http404('This article does not exist')
    return render(request, 'article_detail.html', {
       'article' : a
    })


def article_category(request, category):

    try:
        a = article.objects.filter(category=category)
    except article.DoesNotExist:
        raise Http404('This category does not exist')
    return render(request, 'index.html', {
       'article_list': a
    })

def article_search(request, search):

    try:
        a = article.objects.filter(Q(title__contains=search) | Q(content__contains=search))
    except article.DoesNotExist:
        raise Http404('This category does not exist')
    return render(request, 'index.html', {
       'article_list': a
    })