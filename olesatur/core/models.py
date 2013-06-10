# -*- coding: utf-8 -*-
from django.db import models
from .fields import MultiEmailField
from .managers import VisibleObjectsManager

class BaseModelWithVisible(models.Model):
    visible = models.BooleanField(u'Показывать?', default=False)
    
    allobjects = models.Manager()
    objects = VisibleObjectsManager()
    
    class Meta:
        abstract = True

class BaseSettings(models.Model):
    emails = MultiEmailField(u'Email для писем', max_length=255,
        help_text=u'''Можете вставить несколько email, разделив их запятой''')
    
    def __unicode__(self):
        return u'настройки'
            
    class Meta:
        abstract = True
        verbose_name = u'настройки'
        verbose_name_plural = u'настройки'
