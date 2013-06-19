# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (Banner, BgImage, Direction, IndexBlock, Partner, Settings,
                     Tour)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_editable = ('image',)
admin.site.register(Banner, BannerAdmin)

class BgImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_editable = ('image', )
admin.site.register(BgImage, BgImageAdmin)

admin.site.register(Settings)

class DirectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [('title', 'visible'), 'slug', 'content'], 'classes': ['wide']
        }),
        (u'SEO', {
            'fields': ['seo_title', 'seo_meta'], 'classes': ['grp-collapse grp-closed']
        }),
    ]
    list_display = ('title', 'slug', 'visible')
    list_editable = ('visible', )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    
    """
    class Media:
        css = {
            "all": ('/static/core/tinymce_setup/tiny_styles.css',)
        }
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/core/tinymce_setup/content.js',
            '/static/core/tinymce_setup/tinymce_setup.js',
        ]
    """
admin.site.register(Direction, DirectionAdmin)

class IndexBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort', 'visible')
    list_editable = ('sort', 'visible')
admin.site.register(IndexBlock, IndexBlockAdmin)

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'sort', 'visible')
    list_editable = ('href', 'sort', 'visible')
admin.site.register(Partner, PartnerAdmin)

class TourAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [('title', 'in_bottom_block', 'visible'), 'slug', 'image'], 'classes': ['wide']
        }),
        (u'Информация о туре', {
            'fields': [('start_date', 'nights'), ('direction', 'hotel'), ('price', 'adult_amount', 'child_amount')], 'classes': ['wide']
        }),
        (u'Описание', {
            'fields': ['description', 'content'], 'classes': ['wide']
        }),
    ]
    list_display = ('__unicode__', 'start_date', 'nights',
        'adult_amount', 'direction', 'hotel', 'price', 'in_bottom_block',
        'visible')
    list_editable = ('start_date', 'nights', 'adult_amount', 'hotel',
                     'price', 'in_bottom_block','visible')
    list_filter = ('start_date', 'direction', 'in_bottom_block')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('id', 'title', 'description', 'content')
admin.site.register(Tour, TourAdmin)
