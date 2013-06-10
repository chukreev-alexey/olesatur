# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible')
    list_editable = ('visible', )
admin.site.register(News, NewsAdmin)