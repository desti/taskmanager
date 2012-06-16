# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table('users_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('users', ['Company'])

        # Adding model 'User'
        db.create_table('users_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('login_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Company'])),
        ))
        db.send_create_signal('users', ['User'])

        # Adding model 'UserSkill'
        db.create_table('users_userskill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('skill_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skills.SkillLevel'])),
            ('current_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('users', ['UserSkill'])

        # Adding unique constraint on 'UserSkill', fields ['user', 'skill_level']
        db.create_unique('users_userskill', ['user_id', 'skill_level_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserSkill', fields ['user', 'skill_level']
        db.delete_unique('users_userskill', ['user_id', 'skill_level_id'])

        # Deleting model 'Company'
        db.delete_table('users_company')

        # Deleting model 'User'
        db.delete_table('users_user')

        # Deleting model 'UserSkill'
        db.delete_table('users_userskill')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'skills.level': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        'skills.skill': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        'skills.skilllevel': {
            'Meta': {'ordering': "('skill', 'order')", 'unique_together': "(('skill', 'level'), ('skill', 'order'))", 'object_name': 'SkillLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skills.Level']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skills.Skill']"})
        },
        'users.company': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Company'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'users.user': {
            'Meta': {'object_name': 'User'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'users.userskill': {
            'Meta': {'unique_together': "(('user', 'skill_level'),)", 'object_name': 'UserSkill'},
            'current_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill_level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skills.SkillLevel']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"})
        }
    }

    complete_apps = ['users']