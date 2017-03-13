from django.contrib import admin

from .models import article
from django.conf import settings
# Register your models here.
from django import forms
from pagedown.widgets import AdminPagedownWidget


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(article, ArticleAdmin)
# admin.site.register(article)