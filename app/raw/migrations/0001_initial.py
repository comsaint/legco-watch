# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RawCouncilAgenda'
        db.create_table(u'raw_rawcouncilagenda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('paper_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('language', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('local_filename', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('raw', ['RawCouncilAgenda'])

        # Adding model 'RawCouncilHansard'
        db.create_table(u'raw_rawcouncilhansard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('raw_date', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('language', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created_by_parts', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('local_filename', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('raw', ['RawCouncilHansard'])

        # Adding model 'RawCouncilVoteResult'
        db.create_table(u'raw_rawcouncilvoteresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('raw_date', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('xml_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('xml_filename', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pdf_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('pdf_filename', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('raw', ['RawCouncilVoteResult'])

        # Adding model 'RawMember'
        db.create_table(u'raw_rawmember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('name_e', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('name_c', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('title_e', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('title_c', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('honours_e', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('honours_c', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('year_of_birth', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('place_of_birth', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('homepage', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('photo_file', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('service_e', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('service_c', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('education_e', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('education_c', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('occupation_e', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('occupation_c', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('raw', ['RawMember'])

        # Adding model 'RawCouncilQuestion'
        db.create_table(u'raw_rawcouncilquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('raw_date', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('number_and_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('raw_asker', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('asker', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='raw_questions', null=True, to=orm['raw.RawMember'])),
            ('subject', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('subject_link', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('reply_link', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('local_filename', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('raw', ['RawCouncilQuestion'])

        # Adding model 'RawScheduleMember'
        db.create_table(u'raw_rawschedulemember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('last_name_c', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('first_name_c', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('last_name_e', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('first_name_e', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('english_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('raw', ['RawScheduleMember'])

        # Adding model 'RawCommittee'
        db.create_table(u'raw_rawcommittee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('name_e', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('name_c', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url_e', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url_c', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('raw', ['RawCommittee'])

        # Adding model 'RawCommitteeMembership'
        db.create_table(u'raw_rawcommitteemembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('membership_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('_member_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='memberships', null=True, to=orm['raw.RawScheduleMember'])),
            ('_committee_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('committee', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='memberships', null=True, to=orm['raw.RawCommittee'])),
            ('post_e', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('post_c', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('raw', ['RawCommitteeMembership'])

        # Adding model 'RawMeeting'
        db.create_table(u'raw_rawmeeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meeting_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slot_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('subject_e', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('subject_c', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('agenda_url_e', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('agenda_url_c', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('venue_code', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('meeting_type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('raw', ['RawMeeting'])

        # Adding M2M table for field committees on 'RawMeeting'
        m2m_table_name = db.shorten_name(u'raw_rawmeeting_committees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rawmeeting', models.ForeignKey(orm['raw.rawmeeting'], null=False)),
            ('rawcommittee', models.ForeignKey(orm['raw.rawcommittee'], null=False))
        ))
        db.create_unique(m2m_table_name, ['rawmeeting_id', 'rawcommittee_id'])

        # Adding model 'RawMeetingCommittee'
        db.create_table(u'raw_rawmeetingcommittee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_crawled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_parsed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('crawled_from', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slot_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('_committee_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('committee', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='meeting_committees', null=True, to=orm['raw.RawCommittee'])),
        ))
        db.send_create_signal('raw', ['RawMeetingCommittee'])

        # Adding model 'ScrapeJob'
        db.create_table(u'raw_scrapejob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spider', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('scheduled', self.gf('django.db.models.fields.DateTimeField')()),
            ('job_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('raw_response', self.gf('django.db.models.fields.TextField')()),
            ('completed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_fetched', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('raw', ['ScrapeJob'])

        # Adding model 'Override'
        db.create_table(u'raw_override', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ref_model', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ref_uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('data', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('raw', ['Override'])

        # Adding model 'ParsedPerson'
        db.create_table(u'raw_parsedperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deactivate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name_e', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title_e', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title_c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('honours_e', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('honours_c', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('education_e', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('education_c', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('occupation_e', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('occupation_c', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('gender', self.gf('django.db.models.fields.IntegerField')()),
            ('year_of_birth', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('place_of_birth', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('homepage', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('photo_file', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('raw', ['ParsedPerson'])

        # Adding model 'ParsedMembership'
        db.create_table(u'raw_parsedmembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deactivate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='memberships', to=orm['raw.ParsedPerson'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('method_obtained', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('note', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('raw', ['ParsedMembership'])

        # Adding model 'ParsedCommittee'
        db.create_table(u'raw_parsedcommittee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deactivate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('name_e', self.gf('django.db.models.fields.TextField')()),
            ('name_c', self.gf('django.db.models.fields.TextField')()),
            ('url_e', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('url_c', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('raw', ['ParsedCommittee'])

        # Adding model 'ParsedCommitteeMembership'
        db.create_table(u'raw_parsedcommitteemembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deactivate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('committee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='memberships', to=orm['raw.ParsedCommittee'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='committee_memberships', to=orm['raw.ParsedPerson'])),
            ('post_e', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('post_c', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('raw', ['ParsedCommitteeMembership'])

        # Adding model 'ParsedCouncilMeeting'
        db.create_table(u'raw_parsedcouncilmeeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deactivate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('raw', ['ParsedCouncilMeeting'])

        # Adding model 'ParsedQuestion'
        db.create_table(u'raw_parsedquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deactivate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('meeting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['raw.ParsedCouncilMeeting'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('urgent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('question_type', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True)),
            ('asker', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='questions', blank=True, to=orm['raw.ParsedPerson'])),
            ('repliers_e', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('repliers_c', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('ask_subject_e', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('ask_subject_c', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('body_e', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('body_c', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('reply_subject_e', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('reply_subject_c', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('reply_e', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('reply_c', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('raw', ['ParsedQuestion'])


    def backwards(self, orm):
        # Deleting model 'RawCouncilAgenda'
        db.delete_table(u'raw_rawcouncilagenda')

        # Deleting model 'RawCouncilHansard'
        db.delete_table(u'raw_rawcouncilhansard')

        # Deleting model 'RawCouncilVoteResult'
        db.delete_table(u'raw_rawcouncilvoteresult')

        # Deleting model 'RawMember'
        db.delete_table(u'raw_rawmember')

        # Deleting model 'RawCouncilQuestion'
        db.delete_table(u'raw_rawcouncilquestion')

        # Deleting model 'RawScheduleMember'
        db.delete_table(u'raw_rawschedulemember')

        # Deleting model 'RawCommittee'
        db.delete_table(u'raw_rawcommittee')

        # Deleting model 'RawCommitteeMembership'
        db.delete_table(u'raw_rawcommitteemembership')

        # Deleting model 'RawMeeting'
        db.delete_table(u'raw_rawmeeting')

        # Removing M2M table for field committees on 'RawMeeting'
        db.delete_table(db.shorten_name(u'raw_rawmeeting_committees'))

        # Deleting model 'RawMeetingCommittee'
        db.delete_table(u'raw_rawmeetingcommittee')

        # Deleting model 'ScrapeJob'
        db.delete_table(u'raw_scrapejob')

        # Deleting model 'Override'
        db.delete_table(u'raw_override')

        # Deleting model 'ParsedPerson'
        db.delete_table(u'raw_parsedperson')

        # Deleting model 'ParsedMembership'
        db.delete_table(u'raw_parsedmembership')

        # Deleting model 'ParsedCommittee'
        db.delete_table(u'raw_parsedcommittee')

        # Deleting model 'ParsedCommitteeMembership'
        db.delete_table(u'raw_parsedcommitteemembership')

        # Deleting model 'ParsedCouncilMeeting'
        db.delete_table(u'raw_parsedcouncilmeeting')

        # Deleting model 'ParsedQuestion'
        db.delete_table(u'raw_parsedquestion')


    models = {
        'raw.override': {
            'Meta': {'object_name': 'Override'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ref_model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ref_uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'raw.parsedcommittee': {
            'Meta': {'ordering': "['name_e']", 'object_name': 'ParsedCommittee'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'deactivate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['raw.ParsedPerson']", 'through': "orm['raw.ParsedCommitteeMembership']", 'symmetrical': 'False'}),
            'name_c': ('django.db.models.fields.TextField', [], {}),
            'name_e': ('django.db.models.fields.TextField', [], {}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_c': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'url_e': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        'raw.parsedcommitteemembership': {
            'Meta': {'object_name': 'ParsedCommitteeMembership'},
            'committee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': "orm['raw.ParsedCommittee']"}),
            'deactivate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'committee_memberships'", 'to': "orm['raw.ParsedPerson']"}),
            'post_c': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'post_e': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'raw.parsedcouncilmeeting': {
            'Meta': {'object_name': 'ParsedCouncilMeeting'},
            'deactivate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'raw.parsedmembership': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'ParsedMembership'},
            'deactivate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method_obtained': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'note': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': "orm['raw.ParsedPerson']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'raw.parsedperson': {
            'Meta': {'object_name': 'ParsedPerson'},
            'committees': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['raw.ParsedCommittee']", 'through': "orm['raw.ParsedCommitteeMembership']", 'symmetrical': 'False'}),
            'deactivate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'education_c': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'education_e': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {}),
            'homepage': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'honours_c': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'honours_e': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_e': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'occupation_c': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'occupation_e': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'photo_file': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'title_c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_e': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year_of_birth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'raw.parsedquestion': {
            'Meta': {'ordering': "['meeting']", 'object_name': 'ParsedQuestion'},
            'ask_subject_c': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'ask_subject_e': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'asker': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'questions'", 'blank': 'True', 'to': "orm['raw.ParsedPerson']"}),
            'body_c': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'body_e': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'deactivate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['raw.ParsedCouncilMeeting']"}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'question_type': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True'}),
            'repliers_c': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'repliers_e': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'reply_c': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'reply_e': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'reply_subject_c': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'reply_subject_e': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'urgent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'raw.rawcommittee': {
            'Meta': {'object_name': 'RawCommittee'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name_c': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name_e': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url_c': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url_e': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'raw.rawcommitteemembership': {
            'Meta': {'object_name': 'RawCommitteeMembership'},
            '_committee_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_member_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'committee': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'memberships'", 'null': 'True', 'to': "orm['raw.RawCommittee']"}),
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'memberships'", 'null': 'True', 'to': "orm['raw.RawScheduleMember']"}),
            'membership_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'post_c': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'post_e': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'raw.rawcouncilagenda': {
            'Meta': {'ordering': "['-uid']", 'object_name': 'RawCouncilAgenda'},
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'local_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'paper_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'raw.rawcouncilhansard': {
            'Meta': {'ordering': "['-uid']", 'object_name': 'RawCouncilHansard'},
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_by_parts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'local_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'raw_date': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'raw.rawcouncilquestion': {
            'Meta': {'ordering': "['-uid']", 'object_name': 'RawCouncilQuestion'},
            'asker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'raw_questions'", 'null': 'True', 'to': "orm['raw.RawMember']"}),
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'local_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number_and_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'raw_asker': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'raw_date': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'reply_link': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subject': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subject_link': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'raw.rawcouncilvoteresult': {
            'Meta': {'object_name': 'RawCouncilVoteResult'},
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pdf_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pdf_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'raw_date': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'xml_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'xml_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'raw.rawmeeting': {
            'Meta': {'object_name': 'RawMeeting'},
            'agenda_url_c': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'agenda_url_e': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'committees': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'meetings'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['raw.RawCommittee']"}),
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'meeting_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meeting_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slot_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'subject_c': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subject_e': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'venue_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'raw.rawmeetingcommittee': {
            'Meta': {'object_name': 'RawMeetingCommittee'},
            '_committee_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'committee': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'meeting_committees'", 'null': 'True', 'to': "orm['raw.RawCommittee']"}),
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slot_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'raw.rawmember': {
            'Meta': {'ordering': "['uid']", 'object_name': 'RawMember'},
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'education_c': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'education_e': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'honours_c': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'honours_e': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name_c': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name_e': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'occupation_c': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'occupation_e': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo_file': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'service_c': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'service_e': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title_c': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title_e': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'year_of_birth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'raw.rawschedulemember': {
            'Meta': {'object_name': 'RawScheduleMember'},
            'crawled_from': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'english_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'first_name_c': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'first_name_e': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_crawled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_name_c': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'last_name_e': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'raw.scrapejob': {
            'Meta': {'object_name': 'ScrapeJob'},
            'completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'raw_response': ('django.db.models.fields.TextField', [], {}),
            'scheduled': ('django.db.models.fields.DateTimeField', [], {}),
            'spider': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['raw']
