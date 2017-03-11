#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()  #自定义filter时必须加上


@register.filter(is_safe=True)  #注册template filter
@stringfilter  #希望字符串作为参数
def custom_markdown(value):
    return mark_safe(markdown.markdown(force_text(value),
        extensions = ['markdown.extensions.fenced_code'],
                                       safe_mode=False,
                                       enable_attributes=False))
# def custom_markdown(value):
#     return mark_safe(markdown2.markdown(force_text(value), extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"]))