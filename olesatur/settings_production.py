# -*- coding: utf-8 -*-
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Chukreyev Alexey', 'chukreev.alexey@gmail.com'),
)

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']

# RBD Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(PROJECT_ROOT, 'db', '%s.sqlite' % PROJECT_NAME),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Yekaterinburg'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_ROOT + MEDIA_URL

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_ROOT + STATIC_URL

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '3ujzn63)r#=4*rgiteaq8or(7y29(u4tymn*$!4a*f9p#pfyz('

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'olesatur.apps.pages.middleware.PageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 3-rd party apps
    'south',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    
    # Project apps
    'olesatur.apps.pages',
    'olesatur.apps.treeadmin',
    'olesatur.core',
    'django.contrib.admin',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Project settings
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},

}
GRAPPELLI_ADMIN_TITLE = u'Панель администрирования сайта'
GRAPPELLI_INDEX_DASHBOARD = '%s.dashboard.CustomIndexDashboard' % PROJECT_NAME
PAGINATOR_PER_PAGE = 20
