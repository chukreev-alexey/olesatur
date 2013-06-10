# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter
def split(value, sep=None):
    sep = sep or ','
    return value.split(sep)