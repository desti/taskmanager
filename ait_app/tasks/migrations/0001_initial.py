# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table('tasks_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_tasks', to=orm['users.User'])),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='worker_tasks', null=True, to=orm['users.User'])),
            ('finished_percentage', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_set', null=True, to=orm['tasks.Task'])),
        ))
        db.send_create_signal('tasks', ['Task'])

        # Adding M2M table for field required_skills on 'Task'
        db.create_table('tasks_task_required_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm['tasks.task'], null=False)),
            ('skilllevel', models.ForeignKey(orm['skills.skilllevel'], null=False))
        ))
        db.create_unique('tasks_task_required_skills', ['task_id', 'skilllevel_id'])

        # Adding model 'Candidate'
        db.create_table('tasks_candidate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Task'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('has_accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tasks', ['Candidate'])

        # Adding unique constraint on 'Candidate', fields ['task', 'user']
        db.create_unique('tasks_candidate', ['task_id', 'user_id'])

        # Adding model 'Status'
        db.create_table('tasks_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('tasks', ['Status'])

        # Adding model 'StatusRule'
        db.create_table('tasks_statusrule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_rules', to=orm['tasks.Status'])),
            ('to_status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_rules', to=orm['tasks.Status'])),
        ))
        db.send_create_signal('tasks', ['StatusRule'])

        # Adding unique constraint on 'StatusRule', fields ['from_status', 'to_status']
        db.create_unique('tasks_statusrule', ['from_status_id', 'to_status_id'])

        # Adding model 'StatusLog'
        db.create_table('tasks_statuslog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Task'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Status'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('tasks', ['StatusLog'])


    def backwards(self, orm):
        # Removing unique constraint on 'StatusRule', fields ['from_status', 'to_status']
        db.delete_unique('tasks_statusrule', ['from_status_id', 'to_status_id'])

        # Removing unique constraint on 'Candidate', fields ['task', 'user']
        db.delete_unique('tasks_candidate', ['task_id', 'user_id'])

        # Deleting model 'Task'
        db.delete_table('tasks_task')

        # Removing M2M table for field required_skills on 'Task'
        db.delete_table('tasks_task_required_skills')

        # Deleting model 'Candidate'
        db.delete_table('tasks_candidate')

        # Deleting model 'Status'
        db.delete_table('tasks_status')

        # Deleting model 'StatusRule'
        db.delete_table('tasks_statusrule')

        # Deleting model 'StatusLog'
        db.delete_table('tasks_statuslog')


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
        'tasks.candidate': {
            'Meta': {'unique_together': "(('task', 'user'),)", 'object_name': 'Candidate'},
            'has_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Task']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"})
        },
        'tasks.status': {
            'Meta': {'object_name': 'Status'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'tasks.statuslog': {
            'Meta': {'ordering': "('-created_on',)", 'object_name': 'StatusLog'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Status']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Task']"})
        },
        'tasks.statusrule': {
            'Meta': {'unique_together': "(('from_status', 'to_status'),)", 'object_name': 'StatusRule'},
            'from_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_rules'", 'to': "orm['tasks.Status']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_rules'", 'to': "orm['tasks.Status']"})
        },
        'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'candidates': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['users.User']", 'through': "orm['tasks.Candidate']", 'symmetrical': 'False'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_tasks'", 'to': "orm['users.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'finished_percentage': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['tasks.Task']"}),
            'required_skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['skills.SkillLevel']", 'symmetrical': 'False', 'blank': 'True'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'worker_tasks'", 'null': 'True', 'to': "orm['users.User']"})
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
        }
    }

    complete_apps = ['tasks']