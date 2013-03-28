# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Evento'
        db.create_table(u'core_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('data', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'core', ['Evento'])


    def backwards(self, orm):
        # Deleting model 'Evento'
        db.delete_table(u'core_evento')


    models = {
        u'core.evento': {
            'Meta': {'object_name': 'Evento'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['core']