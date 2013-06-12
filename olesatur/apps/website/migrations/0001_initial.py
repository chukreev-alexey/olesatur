# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Settings'
        db.create_table(u'website_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emails', self.gf('olesatur.core.fields.MultiEmailField')(max_length=255)),
        ))
        db.send_create_signal(u'website', ['Settings'])

        # Adding model 'IndexBlock'
        db.create_table(u'website_indexblock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'website', ['IndexBlock'])

        # Adding model 'Direction'
        db.create_table(u'website_direction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('seo_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('seo_meta', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['Direction'])

        # Adding model 'Tour'
        db.create_table(u'website_tour', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('direction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Direction'], null=True, blank=True)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('nights', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('adult_amount', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('child_amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hotel', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'website', ['Tour'])

        # Adding model 'Partner'
        db.create_table(u'website_partner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'website', ['Partner'])

        # Adding model 'Banner'
        db.create_table(u'website_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['Banner'])

        # Adding model 'BgImage'
        db.create_table(u'website_bgimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
        ))
        db.send_create_signal(u'website', ['BgImage'])


    def backwards(self, orm):
        # Deleting model 'Settings'
        db.delete_table(u'website_settings')

        # Deleting model 'IndexBlock'
        db.delete_table(u'website_indexblock')

        # Deleting model 'Direction'
        db.delete_table(u'website_direction')

        # Deleting model 'Tour'
        db.delete_table(u'website_tour')

        # Deleting model 'Partner'
        db.delete_table(u'website_partner')

        # Deleting model 'Banner'
        db.delete_table(u'website_banner')

        # Deleting model 'BgImage'
        db.delete_table(u'website_bgimage')


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
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Direction']", 'null': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'nights': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['website']