# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Pessoa'
        db.delete_table(u'core_pessoa')

        # Adding model 'Visitante'
        db.create_table(u'core_visitante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('palestra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Palestra'])),
        ))
        db.send_create_signal(u'core', ['Visitante'])

        # Adding model 'Palestrante'
        db.create_table(u'core_palestrante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'core', ['Palestrante'])


        # Changing field 'Palestra.palestrante'
        db.alter_column(u'core_palestra', 'palestrante_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Palestrante'], unique=True))

    def backwards(self, orm):
        # Adding model 'Pessoa'
        db.create_table(u'core_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='P', max_length=1)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'core', ['Pessoa'])

        # Deleting model 'Visitante'
        db.delete_table(u'core_visitante')

        # Deleting model 'Palestrante'
        db.delete_table(u'core_palestrante')


        # Changing field 'Palestra.palestrante'
        db.alter_column(u'core_palestra', 'palestrante_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Pessoa'], unique=True))

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'palestra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Palestra']"})
        }
    }

    complete_apps = ['core']