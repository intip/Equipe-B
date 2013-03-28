# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Palestra.palestrante'
        db.add_column(u'core_palestra', 'palestrante',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['core.Pessoa'], unique=True),
                      keep_default=False)


        # Changing field 'Pessoa.tipo'
        db.alter_column(u'core_pessoa', 'tipo', self.gf('django.db.models.fields.CharField')(max_length=1))

    def backwards(self, orm):
        # Deleting field 'Palestra.palestrante'
        db.delete_column(u'core_palestra', 'palestrante_id')


        # Changing field 'Pessoa.tipo'
        db.alter_column(u'core_pessoa', 'tipo', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'core.evento': {
            'Meta': {'object_name': 'Evento'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'core.palestra': {
            'Meta': {'object_name': 'Palestra'},
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Evento']"}),
            'hora_fim': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palestrante': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Pessoa']", 'unique': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'core.pessoa': {
            'Meta': {'object_name': 'Pessoa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        }
    }

    complete_apps = ['core']