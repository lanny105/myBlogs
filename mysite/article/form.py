from django import forms

from .models import article

class PostForm(forms.ModelForm):

    class Meta:
        model = article
        fields = ('title', 'category', 'content', 'image', 'is_draft')