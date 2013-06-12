# -*- coding: utf-8 -*-
import pytils

from django.db import models, IntegrityError, transaction
from .fields import MultiEmailField
from .managers import VisibleObjectsManager

class BaseModelWithVisible(models.Model):
    visible = models.BooleanField(u'Показывать?', default=False)
    
    allobjects = models.Manager()
    objects = VisibleObjectsManager()
    
    class Meta:
        abstract = True

class TitleSlugModel(models.Model):
    title = models.CharField(u'Название', max_length=255)
    slug = models.SlugField(u'Адрес', max_length=255, unique=True)
    
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        slug = pytils.translit.slugify(self.title)
        i = 0
        while True:
            try:
                savepoint = transaction.savepoint()
                res = super(TitleSlugModel, self).save(*args, **kwargs)
                transaction.savepoint_commit(savepoint)
                return res
            except IntegrityError:
                transaction.savepoint_rollback(savepoint)
                i += 1
                self.slug = '%s_%d' % (slug, i)

class BaseSettings(models.Model):
    emails = MultiEmailField(u'Email для писем', max_length=255,
        help_text=u'''Можете вставить несколько email, разделив их запятой''')
    
    def __unicode__(self):
        return u'настройки'
            
    class Meta:
        abstract = True
        verbose_name = u'настройки'
        verbose_name_plural = u'настройки'
