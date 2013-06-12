# -*- coding: utf-8 -*-
import math

from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404

from .models import IndexBlock, Direction, Tour, Banner

def get_bottom_block_context():
    return {
        'direction_list': Direction.objects.all(),
        'direction_count': math.ceil(float(Tour.objects.filter(in_bottom_block=True).count()) / 3),
        'tour_list': Tour.objects.filter(in_bottom_block=True)[:2],
    }

def index(request):
    try:
        banner = Banner.objects.all().order_by('?')[0]
    except IndexError:
        banner = None
    context = {
        'block_list': IndexBlock.objects.all(),
        'banner': banner
    }
    context.update(get_bottom_block_context())
    return render(request, 'website/index.html', context)

def direction_detail(request, slug):
    request.page = get_object_or_404(Direction, slug=slug)
    print request.page
    return render(request, 'core/base.html')

def page(request, path):
    return render(request, 'core/base.html')
