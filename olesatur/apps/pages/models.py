# -*- coding: utf-8 -*-
import random
from django.db import models
from django.core.cache import cache
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from mptt.models import MPTTModel

from f_heads.apps.styles.models import PageStyle, ServiceStyle

class InfoBlock(models.Model):
    title = models.CharField(u'Название', max_length=255)
    name = models.CharField(u'Имя для обращения', max_length=255, unique=True,
        validators=[RegexValidator(
            regex=r'^[0-9a-zA-Z_]+$',
            message=u"Имя может содержать только латинские буквы, цифры и _"
        )],
        help_text=u'request.infoblock.<<Имя по по латински>>')
    content = models.TextField(u'Содержимое блока текст', blank=True, null=True,
        help_text=u'''Содержимое блока берется сначала из текстового поля, но если оно пустое, то из HTML''')
    html_content = models.TextField(u'Содержимое блока HTML', blank=True, null=True)
            
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)
        verbose_name = u'блок'
        verbose_name_plural = u'информационные блоки'
        
@receiver(post_save, sender=InfoBlock)
@receiver(post_delete, sender=InfoBlock)
def clear_infoblock_cache(sender, **kwargs):
    cache.delete('infoblock')


class VisibleManager(models.Manager):
    def get_query_set(self):
        return super(VisibleManager, self).get_query_set().filter(visible=True)
    
class Page(MPTTModel):
    name = models.CharField(u'Страница', max_length=255)
    title = models.CharField(u'Заголовок (title)', max_length=255, blank=True)
    meta = models.TextField(u'Мета теги (meta)', blank=True, null=True,
        help_text=u'''В данное поле вводится не просто текст, а meta теги целиком.
        Например:<br />
        &lt;meta name="keywords" content="Ключевые слова" /&gt;<br />
        &lt;meta name="description" content="Описание" /&gt;<br />
        &lt;meta name="yandex-verification" content="61409bea27eedabb" /&gt;
        ''')
    path = models.CharField(u'Путь на сайте', max_length=255, blank=True, null=True,
            editable=False, unique=True)
    url = models.CharField(u'Путь к ресурсу URL', max_length=100, help_text=u'''
            Если первым символом указать "/", то путь страницы будет считаться
            от корня сайта, иначе будет прибавлен к пути родителя.
            Примеры:<br />1) /about => http://mysite.ru/about/
            <br />2) contacts (является дочерней страницей страницы about) =>
            http://mysite.ru/about/contacts ''', blank=True, default=u'')
    content = models.TextField(u'Содержимое страницы', blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True,
            related_name='children', verbose_name=u'Родительский элемент')
    redirect_to = models.ForeignKey('self', null=True, blank=True,
            related_name='redirected', verbose_name=u'Перенаправить на страницу')
    style = models.ForeignKey(PageStyle, verbose_name=u'Стиль страницы',
                              related_name='page', blank=True, null=True)
    styles = models.ManyToManyField(PageStyle, verbose_name=u'Стили для рэндома',
                                    related_name='pages', blank=True, null=True)
    service_style = models.ForeignKey(ServiceStyle, verbose_name=u'Стиль услуги',
                                      related_name='service', blank=True, null=True)
    visible = models.BooleanField(u'Показывать?', default=False)
    
    allobjects = models.Manager()
    objects = VisibleManager()
    
    @property
    def is_service(self):
        try:
            return (
                self.is_descendant_of(Page.objects.get(path='services')) \
                or \
                self.is_descendant_of(Page.objects.get(path='solutions'))
            )
        except Page.DoesNotExist:
            return False
    
    @property
    def get_style(self):
        if self.style:
            return self.style
        if self.styles.count() > 0:
            return random.choice(self.styles.all())
        return random.choice(PageStyle.objects.all())
    
    @property
    def get_service_style(self):
        return self.service_style or random.choice(ServiceStyle.objects.all())
    
    def get_absolute_url(self):
        return u'/%s/' % self.path if self.path else '/'
    
    def save(self, *args, **kwargs):
        self.url = self.url.strip()
        if not self.title:
            self.title = self.name
        super(Page, self).save(*args, **kwargs)
        if not self.url and self.parent:
            self.url = str(self.id)
        if self.url and self.url[0] == '/':
            self.path = self.url[1:] # absolute path
        else:
            ancestors = filter(lambda x: bool(x),
                map(lambda x: x.url, self.get_ancestors()))
            ancestors.append(self.url)
            self.path = "/".join(ancestors)
            del(ancestors)
        descendants = self.get_children() # Go throw all children
        for descendant in descendants:
            descendant.save()
        super(Page, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.id == 1: # Index page cannot be deleted 
            return
        super(Page, self).delete(*args, **kwargs)
    
    def __unicode__(self):
        #if self.level > 0:
        #    return  u"%s %s" % (u"".join([u"___" for i in xrange(self.level)]), self.name)
        return self.name
    
    class Meta:
        ordering = ('tree_id', 'lft')
        verbose_name = u'страница'
        verbose_name_plural = u'Страницы сайта'
