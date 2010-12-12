# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Email'
        db.delete_table('addressbook_email')

        # Deleting model 'Address'
        db.delete_table('addressbook_address')

        # Deleting model 'TelephoneNumber'
        db.delete_table('addressbook_telephonenumber')

        # Adding model 'CompanyTelephone'
        db.create_table('addressbook_companytelephone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('extension', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('numberType', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Company'])),
        ))
        db.send_create_signal('addressbook', ['CompanyTelephone'])

        # Adding model 'Company'
        db.create_table('addressbook_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('addressbook', ['Company'])

        # Adding model 'ContactEmail'
        db.create_table('addressbook_contactemail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
        ))
        db.send_create_signal('addressbook', ['ContactEmail'])

        # Adding model 'CompanyAddress'
        db.create_table('addressbook_companyaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('addressType', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('street3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Company'])),
        ))
        db.send_create_signal('addressbook', ['CompanyAddress'])

        # Adding model 'CompanyEmail'
        db.create_table('addressbook_companyemail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Company'])),
        ))
        db.send_create_signal('addressbook', ['CompanyEmail'])

        # Adding model 'ContactTelephone'
        db.create_table('addressbook_contacttelephone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('extension', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('numberType', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
        ))
        db.send_create_signal('addressbook', ['ContactTelephone'])

        # Adding model 'ContactAddress'
        db.create_table('addressbook_contactaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('addressType', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('street3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
        ))
        db.send_create_signal('addressbook', ['ContactAddress'])

        # Adding field 'Contact.company'
        db.add_column('addressbook_contact', 'company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Company'], null=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Email'
        db.create_table('addressbook_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
        ))
        db.send_create_signal('addressbook', ['Email'])

        # Adding model 'Address'
        db.create_table('addressbook_address', (
            ('addressType', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('street3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('addressbook', ['Address'])

        # Adding model 'TelephoneNumber'
        db.create_table('addressbook_telephonenumber', (
            ('extension', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('numberType', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isDefault', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('addressbook', ['TelephoneNumber'])

        # Deleting model 'CompanyTelephone'
        db.delete_table('addressbook_companytelephone')

        # Deleting model 'Company'
        db.delete_table('addressbook_company')

        # Deleting model 'ContactEmail'
        db.delete_table('addressbook_contactemail')

        # Deleting model 'CompanyAddress'
        db.delete_table('addressbook_companyaddress')

        # Deleting model 'CompanyEmail'
        db.delete_table('addressbook_companyemail')

        # Deleting model 'ContactTelephone'
        db.delete_table('addressbook_contacttelephone')

        # Deleting model 'ContactAddress'
        db.delete_table('addressbook_contactaddress')

        # Deleting field 'Contact.company'
        db.delete_column('addressbook_contact', 'company_id')


    models = {
        'addressbook.company': {
            'Meta': {'object_name': 'Company'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'addressbook.companyaddress': {
            'Meta': {'object_name': 'CompanyAddress'},
            'addressType': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Company']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isDefault': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'postalCode': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'street3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'addressbook.companyemail': {
            'Meta': {'object_name': 'CompanyEmail'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Company']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isDefault': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'addressbook.companytelephone': {
            'Meta': {'object_name': 'CompanyTelephone'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Company']"}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isDefault': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numberType': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'addressbook.contact': {
            'Meta': {'object_name': 'Contact'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Company']", 'null': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'addressbook.contactaddress': {
            'Meta': {'object_name': 'ContactAddress'},
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
        'addressbook.contactemail': {
            'Meta': {'object_name': 'ContactEmail'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isDefault': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'addressbook.contacttelephone': {
            'Meta': {'object_name': 'ContactTelephone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isDefault': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numberType': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['addressbook']
