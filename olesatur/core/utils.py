# -*- coding: utf-8 -*-

from collections import defaultdict

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