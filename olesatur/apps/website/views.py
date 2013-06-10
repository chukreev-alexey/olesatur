# -*- coding: utf-8 -*-
from django.shortcuts import render
from f_heads.apps.pages.models import Page
from f_heads.apps.website.models import News

def index(request):
    news_list = News.objects.all()[:2]
    return render(request, 'website/index.html', {'news_list': news_list})

def service_list(request, kind):
    service_page = Page.objects.get(path=kind)
    object_list = service_page.children.all()
    return render(request, 'website/service_list.html', {
        'object_list': object_list
    })

def service_detail(request, kind):
    return render(request, 'website/service_detail.html')

def page(request, path):
    return render(request, 'website/page.html')
