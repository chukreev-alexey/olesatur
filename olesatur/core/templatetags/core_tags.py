# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter
def split(value, sep=None):
    sep = sep or ','
    return value.split(sep)


@register.inclusion_tag('core/templatetags/base_paginator.html')
def base_paginator(objects, request=None):
    if request:
        query = request.GET.copy()
        query.update(request.POST.copy())
        try:
            del query['page']
        except:
            pass
    return {'objects': objects, 'query': '&'+query.urlencode()}