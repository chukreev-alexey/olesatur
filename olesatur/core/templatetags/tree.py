# -*- coding: utf-8 -*-
from django import template

register = template.Library()


class TreeNode(template.Node):
    def __init__(self, tree, node_list):
        self.tree = tree
        self.node_list = node_list

    def render(self, context):
        tree = self.tree.resolve(context)
        br = getattr(context.get('request'), 'ancestors', [])
        breadcrumbs = [i.path for i in getattr(context.get('request'), 'ancestors', [])]
        #breadcrumbs = [i['path'] for i in context.get('breadcrumbs', [])]

        # выводит элемент списка с подсписком
        # для подсписка рекурсивно вызывается render_items
        def render_item(item, sub_items, level):
            context.update({'item': item, 'level': level})
            if item['path'].strip('/') in breadcrumbs:
                ul_pattern = '<ul class="b-menu-list">%s</ul>'
                return ''.join([
                    '<li class="b-menu__item active">',
                    item and self.node_list.render(context) or '',
                    sub_items and ul_pattern % ''.join(render_items(sub_items, level + 1)) or '',
                    '</li>',
                ])
            else:
                return ''.join([
                    '<li class="b-menu__item">',
                    item and self.node_list.render(context) or '',
                    '</li>',
                ])

        # вывод списка элементов
        def render_items(items, level):
            return ''.join(render_item(item, item['children'], level) for item in items)

        return render_items(tree, 0)

@register.tag
def tree(parser, token):
    bits = token.split_contents()
    if len(bits) not in (2, 3):
        raise template.TemplateSyntaxError('"%s" takes one argument: tree-structured list' % bits[0])
    node_list = parser.parse('end' + bits[0])
    parser.delete_first_token()
    return TreeNode(parser.compile_filter(bits[1]), node_list)

#{% tree category_list %}
#    <a href="{{ item.path }}">{{ item.name }}</a>
#{% endtree %}