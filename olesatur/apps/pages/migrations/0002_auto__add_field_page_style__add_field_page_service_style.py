# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.style'
        db.add_column('pages_page', 'style',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='page', null=True, to=orm['styles.PageStyle']),
                      keep_default=False)

        # Adding field 'Page.service_style'
        db.add_column('pages_page', 'service_style',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='service', null=True, to=orm['styles.ServiceStyle']),
                      keep_default=False)

        # Adding M2M table for field styles on 'Page'
        db.create_table('pages_page_styles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['pages.page'], null=False)),
            ('pagestyle', models.ForeignKey(orm['styles.pagestyle'], null=False))
        ))
        db.create_unique('pages_page_styles', ['page_id', 'pagestyle_id'])


    def backwards(self, orm):
        # Deleting field 'Page.style'
        db.delete_column('pages_page', 'style_id')

        # Deleting field 'Page.service_style'
        db.delete_column('pages_page', 'service_style_id')

        # Removing M2M table for field styles on 'Page'
        db.delete_table('pages_page_styles')


    models = {
        'pages.infoblock': {
            'Meta': {'ordering': "('title',)", 'object_name': 'InfoBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pages.page': {
            'Meta': {'ordering': "('tree_id', 'lft')", 'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pages.Page']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'service_style': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'service'", 'null': 'True', 'to': "orm['styles.ServiceStyle']"}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'page'", 'null': 'True', 'to': "orm['styles.PageStyle']"}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'pages'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['styles.PageStyle']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'styles.pagestyle': {
            'Meta': {'object_name': 'PageStyle'},
            'cap_color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'head_color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'styles.servicestyle': {
            'Meta': {'object_name': 'ServiceStyle'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['pages']