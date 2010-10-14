# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table('addressbook_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('addressbook', ['Contact'])

        # Adding model 'Address'
        db.create_table('addressbook_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
            ('addressType', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('street3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('addressbook', ['Address'])

        # Adding model 'TelephoneNumber'
        db.create_table('addressbook_telephonenumber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('extension', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('numberType', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('addressbook', ['TelephoneNumber'])

        # Adding model 'Email'
        db.create_table('addressbook_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('addressbook', ['Email'])


    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table('addressbook_contact')

        # Deleting model 'Address'
        db.delete_table('addressbook_address')

        # Deleting model 'TelephoneNumber'
        db.delete_table('addressbook_telephonenumber')

        # Deleting model 'Email'
        db.delete_table('addressbook_email')


    models = {
        'addressbook.address': {
            'Meta': {'object_name': 'Address'},
            'addressType': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isDefault': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'postalCode': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'street3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'addressbook.contact': {
            'Meta': {'object_name': 'Contact'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'addressbook.email': {
            'Meta': {'object_name': 'Email'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isDefault': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'addressbook.telephonenumber': {
            'Meta': {'object_name': 'TelephoneNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isDefault': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numberType': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['addressbook']
