# -*- coding: utf-8 -*-
import json
import math

from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import send_mail

from olesatur.core.utils import get_paginator

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

def order_form(request, tour):
    from .forms import OrderForm
    from olesatur.core.fields import emails_list
    tour = get_object_or_404(Tour, pk=tour)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = u'Заказ с сайта'
        recipients = []
        recipients.extend(emails_list(request.settings.emails))
        email_context = form.cleaned_data
        email_context['tour'] = tour
        email_content = render_to_string('website/emails/order_email.txt', email_context)
        send_mail(subject, email_content,
                  email_context.get('email') or recipients[0], recipients)
        return HttpResponse('success')
    return render(request, 'website/include/order_form.html', {'form': form, 'tour': tour})

def direction_list(request):
    context = get_bottom_block_context()
    return render(request, 'website/directions.html', context)

def tour_list(request):
    context = {'object_list': get_paginator(request, Tour.objects.all(), rows_on_page=10)}
    context.update(get_bottom_block_context())
    return render(request, 'website/tour_list.html', context)

def direction_detail(request, slug):
    request.page = get_object_or_404(Direction, slug=slug)
    print request.page
    return render(request, 'core/base.html')

def page(request, path):
    return render(request, 'core/base.html')
