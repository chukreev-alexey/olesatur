# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^$', 'olesatur.apps.website.views.index'),
    url(r'^direction/(?P<slug>[\w-]+)/$', 'olesatur.apps.website.views.direction_detail', name="direction_detail"),
)

# Serving media
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    url(r'^(?P<path>.*?)[/]?$', 'olesatur.apps.website.views.page', name="page"),
)