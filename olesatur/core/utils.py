# -*- coding: utf-8 -*-

from collections import defaultdict

from django.core.paginator import Paginator, InvalidPage, EmptyPage

def get_paginator(request, queryset, rows_on_page=30, pages_forward=5):
    paginator = Paginator(queryset, rows_on_page, orphans=0)
    try:
        page = int(request.REQUEST.get('page', '1'))
    except ValueError:
        page = 1
    try:
        objects = paginator.page(page)
    except (EmptyPage, InvalidPage):
        objects = paginator.page(paginator.num_pages)
    
    start_index = page - (pages_forward+1)
    if start_index < 0:
       start_index = 0
    objects.paginator.slice = "%d:%d" % (start_index, page+pages_forward)
    return objects


def mptt_as_dict(items, path_prefix=None, none_level=None):
    
    def build_parent_map(items):
        parent_map = defaultdict(list)
        for item in items:
            parent_map[getattr(item, 'parent_id')].append(item.id)
        if none_level:
            parent_map[None] = none_level
        return parent_map

    def get_children(node):
        if node:
            node = node.id
        if node in parent_map:
            return [item for item in items if item.id in parent_map[node]]
        return []

    def tree_level(parent):
        for item in get_children(parent):
            name, path = item.name, item.path
            if item.path:
                path = '/%s/' % item.path.strip('/')
            else:
                path = '/'
            if path_prefix:
                path = '/%s%s' % (path_prefix.strip('/'), path)
            sub_items = list(tree_level(item))
            yield dict(name=name, path=path, children=sub_items)
    
    parent_map = build_parent_map(items)
    return list(tree_level(None))