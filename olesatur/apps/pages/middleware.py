# -*- coding: utf-8 -*-
import os
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.conf import settings

from olesatur.core.utils import mptt_as_dict
from olesatur.apps.website.models import Partner, BgImage, Settings, Tour
from .models import Page, InfoBlock


class PageMiddleware(object):
    """
    Add page object to request object
    """
    def __init__(self):
        pass
    
    def common_actions(self, request):
        request.settings = cache.get('settings')
        if not request.settings:
            try:
                request.settings = Settings.objects.all()[0]
                cache.set('settings', request.settings, 60*60*24)
            except IndexError:
                pass
            
        request.infoblock = cache.get('infoblock')
        if not request.infoblock:
            try:
                request.infoblock = dict(
                    [(item.name, item.content or item.html_content) \
                     for item in InfoBlock.objects.all()]) 
                cache.set('infoblock', request.infoblock, 60*60*24)
            except:
                pass
        return request
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        #request.PROJECT_TITLE = settings.PROJECT_TITLE
        """
        Abort if:
        1) Ajax request
        2) Request for static serve via django mechanism
        """
        if request.path.startswith('/static/') or \
            request.path.startswith('/media/') or \
            request.path.startswith('/admin/') or \
            request.path.startswith('/grappelli/'):
            
            return None
        request.TITLE = settings.GRAPPELLI_ADMIN_TITLE
        path = request.path.strip('/')
        request = self.common_actions(request)
        
        request.top_menu = Page.objects.filter(level=1)
        request.partner_list = Partner.objects.all()[:20]
        request.tour_slider = Tour.objects.filter(in_slider=True)[:5]
        
        
        try:
            request.page = Page.objects.get(path=path)
        except Page.DoesNotExist:
            if view_func.__name__ == 'page':
                raise Http404
            else:
                #request.page = Page()
                request.page  = None
        
        #none_level = request.top_menu.values_list('id', flat=True)
        #request.tree = mptt_as_dict(Page.objects.filter(level__gte=1), none_level=none_level)
        if request.page and request.page.bgimage:
            request.background_image = os.path.join(settings.MEDIA_URL,
                                                    request.page.bgimage.path)
        else:
            try:
                request.background_image = os.path.join(settings.MEDIA_URL,
                    BgImage.objects.all().order_by('?')[0].image.path)
            except IndexError:
                request.background_image = os.path.join(settings.STATIC_URL,
                                                        'img/bbb.png')
                
        if request.page:
            request.ancestors = list(request.page.get_ancestors()) + [request.page]
            if request.page.redirect_to and not request.page.redirect_to.redirect_to:
                return HttpResponseRedirect(request.page.redirect_to.get_absolute_url() or '/')
        
        
        return None
