from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^article/(?P<id>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^category/(?P<category>\w+)/$', views.article_category),
    url(r'^search/(?P<search>\w+)/$', views.article_search),
    url(r'^new_article/$', views.post_new),
    url(r'^edit_article/(?P<id>\d+)/$', views.post_edit, name='edit_article'),
]