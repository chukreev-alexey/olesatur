# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tour.in_bottom_block'
        db.add_column(u'website_tour', 'in_bottom_block',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tour.in_bottom_block'
        db.delete_column(u'website_tour', 'in_bottom_block')


    models = {
        u'website.banner': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Banner'},
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'website.bgimage': {
            'Meta': {'ordering': "('title',)", 'object_name': 'BgImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'website.direction': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Direction'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seo_meta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'website.indexblock': {
            'Meta': {'ordering': "('sort',)", 'object_name': 'IndexBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'website.partner': {
            'Meta': {'ordering': "('sort', 'title')", 'object_name': 'Partner'},
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'website.settings': {
            'Meta': {'object_name': 'Settings'},
            'emails': ('olesatur.core.fields.MultiEmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'website.tour': {
            'Meta': {'ordering': "('start_date',)", 'object_name': 'Tour'},
            'adult_amount': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'child_amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Direction']", 'null': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'in_bottom_block': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nights': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['website']