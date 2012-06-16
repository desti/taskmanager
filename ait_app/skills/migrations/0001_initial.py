# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Skill'
        db.create_table('skills_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
        ))
        db.send_create_signal('skills', ['Skill'])

        # Adding model 'Level'
        db.create_table('skills_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
        ))
        db.send_create_signal('skills', ['Level'])

        # Adding model 'SkillLevel'
        db.create_table('skills_skilllevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skills.Skill'])),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skills.Level'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('skills', ['SkillLevel'])

        # Adding unique constraint on 'SkillLevel', fields ['skill', 'level']
        db.create_unique('skills_skilllevel', ['skill_id', 'level_id'])

        # Adding unique constraint on 'SkillLevel', fields ['skill', 'order']
        db.create_unique('skills_skilllevel', ['skill_id', 'order'])


    def backwards(self, orm):
        # Removing unique constraint on 'SkillLevel', fields ['skill', 'order']
        db.delete_unique('skills_skilllevel', ['skill_id', 'order'])

        # Removing unique constraint on 'SkillLevel', fields ['skill', 'level']
        db.delete_unique('skills_skilllevel', ['skill_id', 'level_id'])

        # Deleting model 'Skill'
        db.delete_table('skills_skill')

        # Deleting model 'Level'
        db.delete_table('skills_level')

        # Deleting model 'SkillLevel'
        db.delete_table('skills_skilllevel')


    models = {
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
        }
    }

    complete_apps = ['skills']