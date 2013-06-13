# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag('website/templatetags/paginator.html')
def paginator(object_list, request=None):
    if request:
        query = request.GET.copy()
        query.update(request.POST.copy())
        try:
            del query['page']
        except:
            pass
    return {'object_list': object_list, 'query': '&'+query.urlencode()}