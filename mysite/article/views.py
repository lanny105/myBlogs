#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404

from article.models import article
from django.http import Http404
from django.db.models import Q
from .form import PostForm

from django.contrib.auth.decorators import login_required
import time

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import os
import json

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
       'article': a, 'category_list': category_list
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


@login_required
def post_new(request):
    category_list = article.objects.order_by('category').values_list('category', flat=True).distinct()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=True)
            a.author = request.user
            a.publish()
            print a.image
            return redirect('article_detail', id=a.id)
        else:
            print "invalid form!!"
    else:
        form = PostForm()
    return render(request, 'new_article.html', {'form': form, 'category_list': category_list})


@login_required
def post_edit(request, id):
    a = get_object_or_404(article, id=id)
    category_list = article.objects.order_by('category').values_list('category', flat=True).distinct()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=a)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.save()
            print a.image
            return redirect('article_detail', id=a.id)
        else:
            print "invalid form!!"
    else:
        form = PostForm(instance=a)
    return render(request, 'new_article.html', {'form': form, 'category_list': category_list})



@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        file_obj = open("log.txt","w+")
        buf = request.FILES.get('imgFile', None)
        print >> file_obj,str(buf)
        file_buff = buf.read()
        time_format=str(time.strftime("%Y-%m-%d-%H%M%S",time.localtime()))
        try:
            file_name = "img_"+time_format+".jpg"
            save_file("media/upload/image/content_img", file_name, file_buff)
            dict_tmp = {}
            dict_tmp["error"] = 0
            dict_tmp["url"] = "/media/upload/image/content_img/"+file_name
            return HttpResponse(json.dumps(dict_tmp))
        except Exception,e:
            dict_tmp = {}
            dict_tmp["error"] = 1
            print >> file_obj,e
            return HttpResponse(json.dumps(dict_tmp))
#对path进行处理
def mkdir(path):
    # 去除左右两边的空格
    path=path.strip()
    # 去除尾部 \符号
    path=path.rstrip("\\")

    if not os.path.exists(path):
        os.makedirs(path)
    return path
#保存相关的文件
def save_file(path, file_name, data):
    if data == None:
        return

    mkdir(path)
    if(not path.endswith("/")):
        path=path+"/"
    file=open(path+file_name, "wb")
    file.write(data)
    file.flush()
    file.close()