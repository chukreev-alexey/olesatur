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

urlpatterns += patterns('f_heads.apps.website.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<kind>services|solutions)/$', 'service_list', name='service_list'),
    url(r'^(?P<kind>services|solutions)/', 'service_detail', name='service_detail'),
)


# Serving media
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    url(r'^(?P<path>.*?)[/]?$', 'f_heads.apps.website.views.page', name="page"),
)