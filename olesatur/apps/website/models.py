# -*- coding: utf-8 -*-
import datetime
import pytils

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from filebrowser.fields import FileBrowseField

from olesatur.core.models import (BaseSettings, BaseModelWithVisible,
                                  TitleSlugModel)


class Settings(BaseSettings):
    pass

@receiver(post_save, sender=Settings)
@receiver(post_delete, sender=Settings)
def clear_settings_cache(sender, **kwargs):
    cache.delete('settings')
    

class IndexBlock(BaseModelWithVisible):
    title = models.CharField(u'Название', max_length=255)
    content = models.TextField(u'Содержимое', blank=True, null=True)
    sort = models.IntegerField(u'Порядок', default=0)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('sort', )
        verbose_name = u'блок'
        verbose_name_plural = u'блоки на главной странице'

class Direction(TitleSlugModel, BaseModelWithVisible):
    seo_title = models.CharField(u'Заголовок (title)', max_length=255, blank=True)
    seo_meta = models.TextField(u'Мета дескрипторы (meta)', blank=True, null=True)
    content = models.TextField(u'Содержимое', blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('direction_detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('title', )
        verbose_name = u'направление'
        verbose_name_plural = u'направления'


class TourManager(models.Manager):
    def get_query_set(self):
        return super(TourManager, self).get_query_set().\
            filter(start_date__gte=datetime.date.today(), visible=True)

class Tour(TitleSlugModel):
    direction = models.ForeignKey(Direction, verbose_name=u'Направление',
                                  blank=True, null=True)
    image = FileBrowseField(u'Картинка', format='image', max_length=200,
                            directory="tours/", blank=True, null=True)
    start_date = models.DateField(u'Дата заезда', default=datetime.date.today)
    nights = models.IntegerField(u'Ночей', default=0)
    adult_amount = models.IntegerField(u'Взрослых', default=2)
    child_amount = models.IntegerField(u'Детей', default=0)
    hotel = models.CharField(u'Отель', max_length=255, blank=True, null=True)
    price = models.IntegerField(u'Стоимость', default=0)
    description = models.TextField(u'Краткое описание (в нижнем блоке)', blank=True,
                                   null=True)
    content = models.TextField(u'Полное описание (в списке туров)', blank=True,
                               null=True)
    in_bottom_block = models.BooleanField(u'Спецпредложение', default=False)
    visible = models.BooleanField(u'Показывать?', default=False)
    
    allobjects = models.Manager()
    objects = TourManager()
    
    def get_text(self):
        return u'%s %s на %d %s' % (
            self.hotel or '',
            self.start_date.strftime('%d.%m.%Y'),
            self.nights,
            pytils.numeral.choose_plural(self.nights, (u"ночь", u"ночи", u"ночей"))
        )
    
    def __unicode__(self):
        return u'%s (№%d)' % (self.title, self.id)
    
    class Meta:
        ordering = ('start_date',)
        verbose_name = u'тур'
        verbose_name_plural = u'туры'


class Partner(BaseModelWithVisible):
    title = models.CharField(u'Название', max_length=255)
    image = FileBrowseField(u'Картинка', format='image', max_length=200,
                            directory="partners/")
    href = models.URLField(u'Ссылка на партнера', blank=True, null=True,
        help_text=u'''Если ссылка указана, то картинка партнера становится
        кликабельной. Указывать в формате http://somesite.ru/page_adreess''')
    sort = models.IntegerField(u'Порядок', default=0)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('sort', 'title')
        verbose_name = u'партнер'
        verbose_name_plural = u'партнеры'
        

class Banner(models.Model):
    title = models.CharField(u'Название', max_length=255)
    image = FileBrowseField(u'Картинка', format='image', max_length=200,
                            directory="banners/")
    href = models.URLField(u'Ссылка', blank=True, null=True, help_text=u'''Если
        ссылка указана, то баннер становится кликабельным. Указывать в формате
        http://somesite.ru/page_adreess/page.html''')
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('title', )
        verbose_name = u'баннер'
        verbose_name_plural = u'баннеры на главной странице'

class BgImage(models.Model):
    title = models.CharField(u'Название', max_length=255)
    image = FileBrowseField(u'Картинка', format='image', max_length=200,
                            directory='backgrounds/')
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('title', )
        verbose_name = u'картинка'
        verbose_name_plural = u'фоновые картинки'
