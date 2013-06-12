# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InfoBlock'
        db.create_table(u'pages_infoblock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('html_content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['InfoBlock'])

        # Adding model 'Page'
        db.create_table(u'pages_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('seo_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('seo_meta', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=100, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('bgimage', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pages.Page'])),
            ('redirect_to', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='redirected', null=True, to=orm['pages.Page'])),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'pages', ['Page'])


    def backwards(self, orm):
        # Deleting model 'InfoBlock'
        db.delete_table(u'pages_infoblock')

        # Deleting model 'Page'
        db.delete_table(u'pages_page')


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
            'bgimage': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
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