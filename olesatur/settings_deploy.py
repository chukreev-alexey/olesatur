# -*- coding: utf-8 -*-

from settings_base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u30658',
        'USER': 'u30658',
        'PASSWORD': 'mcrnucsn2d',
        'HOST': 'localhost',
        'PORT': '',
    }
}
