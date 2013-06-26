# -*- coding: utf-8 -*-
import json
import math

from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages

from olesatur.core.utils import get_paginator
from olesatur.apps.pages.models import Page

from .models import IndexBlock, Direction, Tour, Banner

def get_bottom_block_context():
    return {
        'direction_list': Direction.objects.all(),
        'direction_count': math.ceil(float(Direction.objects.all().count()) / 3),
    }

def build_ancestors(obj, url):
    try:
        obj_page = get_object_or_404(Page, url=url)
    except:
        obj_page = None
    if obj_page:
        return list(obj_page.get_ancestors()) + [obj_page, obj]

def index(request):
    try:
        banner = Banner.objects.all().order_by('?')[0]
    except IndexError:
        banner = None
    context = {
        'block_list': IndexBlock.objects.all(),
        'banner': banner,
        'tour_list': Tour.objects.filter(in_bottom_block=True)[:5],
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

def callback(request):
    from .forms import CallbackForm
    from olesatur.core.fields import emails_list
    form = CallbackForm(request.POST or None)
    if form.is_valid():
        subject = u'Заказ звонка с сайта'
        recipients = []
        recipients.extend(emails_list(request.settings.emails))
        email_context = form.cleaned_data
        email_content = render_to_string('website/emails/callback_email.txt', email_context)
        send_mail(subject, email_content,
                  email_context.get('email') or recipients[0], recipients)
        messages.add_message(request, messages.SUCCESS, u"Наши менеджеры обязательно вам перезвонят в ближайшее время.")
        return redirect(reverse('callback'))
    return render(request, 'website/callback.html', {'form': form})

def direction_list(request):
    context = get_bottom_block_context()
    return render(request, 'website/directions.html', context)

def tour_list(request):
    context = {'object_list': get_paginator(request, Tour.objects.all(), rows_on_page=10)}
    context.update(get_bottom_block_context())
    return render(request, 'website/tour_list.html', context)

def tour_detail(request, slug):
    obj = get_object_or_404(Tour, slug=slug)
    request.ancestors = build_ancestors(obj, 'tours')
    context = {'object_list': get_paginator(request, [obj], rows_on_page=1)}
    context.update(get_bottom_block_context())
    return render(request, 'website/tour_list.html', context)

def direction_detail(request, slug):
    object_detail = get_object_or_404(Direction, slug=slug)
    request.ancestors = build_ancestors(object_detail, 'directions')
    context = get_bottom_block_context()
    context.update({'object_detail': object_detail})
    return render(request, 'website/direction_detail.html', context)

def page(request, path):
    context = get_bottom_block_context()
    return render(request, 'core/base.html', context)
