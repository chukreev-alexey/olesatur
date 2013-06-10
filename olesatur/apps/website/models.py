# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, post_delete

from filebrowser.fields import FileBrowseField

from olesatur.core.models import BaseSettings, BaseModelWithVisible


class Settings(BaseSettings):
    pass

@receiver(post_save, sender=Settings)
@receiver(post_delete, sender=Settings)
def clear_settings_cache(sender, **kwargs):
    cache.delete('settings')
    

class IndexBlock(BaseModelWithVisible):
    name = models.CharField(u'Название', max_length=255)
    content = models.TextField(u'Содержимое', blank=True, null=True)
    sort = models.IntegerField(u'Порядок', default=0)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('sort', )
        verbose_name = u'блок'
        verbose_name_plural = u'блоки на главной странице'

class Direction(BaseModelWithVisible):
    name = models.CharField(u'Название', max_length=255)
    url = models.SlugField(u'Адрес', max_length=255)
    title = models.CharField(u'Заголовок (title)', max_length=255, blank=True)
    meta = models.TextField(u'Мета дескрипторы (meta)', blank=True, null=True)
    content = models.TextField(u'Содержимое', blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        verbose_name = u'направление'
        verbose_name_plural = u'направления'


class TourManager(models.Manager):
    def get_query_set(self):
        return super(TourManager, self).get_query_set().\
            filter(start_date__gte=datetime.date.today(), visible=True)

class Tour(models.Model):
    name = models.CharField(u'Название', max_length=255)
    url = models.SlugField(u'Адрес', max_length=255)
    image = FileBrowseField(u'Картинка', format='image', max_length=200, directory="tours/")
    start_date = models.DateField(u'Дата заезда', default=datetime.date.today)
    nights = models.IntegerField(u'Ночей', default=0)
    adult_amount = models.IntegerField(u'Взрослых', default=2)
    child_amount = models.IntegerField(u'Детей', default=0)
    hotel = models.CharField(u'Отель', max_length=255, blank=True, null=True)
    price = models.IntegerField(u'Стоимость', default=0)
    description = models.TextField(u'Краткое описание (в списке)', blank=True,
                                   null=True)
    content = models.TextField(u'Полное описание (в карточке)', blank=True,
                               null=True)
    visible = models.BooleanField(u'Показывать?', default=False)
    
    allobjects = models.Manager()
    objects = TourManager()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('start_date', 'name')
        verbose_name = u'тур'
        verbose_name_plural = u'туры'


class Partner(models.Model):
    name = models.CharField(u'Название', max_length=255)
    image = FileBrowseField(u'Картинка', format='image', max_length=200, directory="partners/")
    href = models.URLField(u'Ссылка на партнера', blank=True, null=True)
    sort = models.IntegerField(u'Порядок', default=0)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('sort', 'name')
        verbose_name = u'партнер'
        verbose_name_plural = u'партнеры'
        

class Banner(models.Model):
    name = models.CharField(u'Название', max_length=255)
    image = FileBrowseField(u'Картинка', format='image', max_length=200, directory="banners/")
    href = models.URLField(u'Ссылка', blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
        verbose_name = u'баннер'
        verbose_name_plural = u'баннеры'
