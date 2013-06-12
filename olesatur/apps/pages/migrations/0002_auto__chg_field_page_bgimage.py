# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.bgimage'
        db.alter_column(u'pages_page', 'bgimage', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Page.bgimage'
        db.alter_column(u'pages_page', 'bgimage', self.gf('filebrowser.fields.FileBrowseField')(default='', max_length=200))

    models = {
        u'pages.infoblock': {
            'Meta': {'ordering': "('title',)", 'object_name': 'InfoBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'html_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'pages.page': {
            'Meta': {'ordering': "('tree_id', 'lft')", 'object_name': 'Page'},
            'bgimage': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'redirect_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'redirected'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'seo_meta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['pages']