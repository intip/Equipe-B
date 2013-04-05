# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Visitante.avatar'
        db.add_column(u'core_visitante', 'avatar',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Evento.image'
        db.delete_column(u'core_evento', 'image')

        # Adding field 'Evento.imagem'
        db.add_column(u'core_evento', 'imagem',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Visitante.avatar'
        db.delete_column(u'core_visitante', 'avatar')

        # Adding field 'Evento.image'
        db.add_column(u'core_evento', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Evento.imagem'
        db.delete_column(u'core_evento', 'imagem')


    models = {
        u'core.evento': {
            'Meta': {'object_name': 'Evento'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'core.palestra': {
            'Meta': {'object_name': 'Palestra'},
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Evento']"}),
            'hora_fim': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palestrante': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Palestrante']", 'unique': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'core.palestrante': {
            'Meta': {'object_name': 'Palestrante'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'core.visitante': {
            'Meta': {'object_name': 'Visitante'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'palestra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Palestra']"})
        }
    }

    complete_apps = ['core']