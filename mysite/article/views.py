from django.shortcuts import render
from django.http import HttpResponse
from article.models import article
from django.http import Http404

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