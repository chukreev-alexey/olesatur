# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.contrib import admin
from .models import Page, InfoBlock
from olesatur.apps.treeadmin import TreeAdmin

class PageAdmin(TreeAdmin):
    fieldsets = [
        (None, {
            'fields': [('name','visible'), 'url', ('parent', 'redirect_to'), 'bgimage' ], 'classes': ['wide']
        }),
        (u'Содержимое страницы', {
            'fields': ['content'], 'classes': ['grp-collapse grp-closed']
        }),
        (u'SEO', {
            'fields': ['seo_title', 'seo_meta'], 'classes': ['grp-collapse grp-closed']
        }),
    ]
    tree_title_field = 'name'
    tree_display = ('name', 'path',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }

    class Meta:
        model = Page
    
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/core/tinymce_setup/content.js',
            '/static/core/tinymce_setup/tinymce_setup.js',
        ]
admin.site.register(Page, PageAdmin)

class InfoBlockAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('title', 'name')
    search_fields = ('title', 'name')
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/pages/tinymce_setup/html_content.js',
            '/static/core/tinymce_setup/tinymce_setup.js',
        ]
admin.site.register(InfoBlock, InfoBlockAdmin)
