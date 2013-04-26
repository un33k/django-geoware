# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Altname'
        db.create_table('geoware-altname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_altname_language', null=True, to=orm['geoware.Language'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('is_preferred', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_short', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('geoname_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('geoware', ['Altname'])

        # Adding model 'City'
        db.create_table('geoware-city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('name_std', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('population', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('elevation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('geoname_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('bbw', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('bbn', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('bbe', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('bbs', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(default='POINT(0.0 0.0)')),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_city_country', null=True, to=orm['geoware.Country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_city_region', null=True, to=orm['geoware.Region'])),
            ('subregion', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_city_subregion', null=True, to=orm['geoware.Subregion'])),
            ('timezone', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_city_timezone', null=True, to=orm['geoware.Timezone'])),
            ('sister', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geoware.City'], null=True, blank=True)),
        ))
        db.send_create_signal('geoware', ['City'])

        # Adding M2M table for field altnames on 'City'
        db.create_table('geoware-city_altnames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('city', models.ForeignKey(orm['geoware.city'], null=False)),
            ('altname', models.ForeignKey(orm['geoware.altname'], null=False))
        ))
        db.create_unique('geoware-city_altnames', ['city_id', 'altname_id'])

        # Adding model 'Continent'
        db.create_table('geoware-continent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('name_std', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('population', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('elevation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('geoname_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2, db_index=True)),
        ))
        db.send_create_signal('geoware', ['Continent'])

        # Adding unique constraint on 'Continent', fields ['name', 'code']
        db.create_unique('geoware-continent', ['name', 'code'])

        # Adding M2M table for field altnames on 'Continent'
        db.create_table('geoware-continent_altnames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('continent', models.ForeignKey(orm['geoware.continent'], null=False)),
            ('altname', models.ForeignKey(orm['geoware.altname'], null=False))
        ))
        db.create_unique('geoware-continent_altnames', ['continent_id', 'altname_id'])

        # Adding model 'Country'
        db.create_table('geoware-country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('name_std', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('population', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('elevation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('geoname_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('continent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_country_continent', null=True, to=orm['geoware.Continent'])),
            ('jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_country_jurisdiction', null=True, to=orm['geoware.Country'])),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_country_currency', null=True, to=orm['geoware.Currency'])),
            ('capital', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_country_capital', null=True, to=orm['geoware.City'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2, db_index=True)),
            ('iso_3', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('iso_n', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('fips', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('idc', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('tld', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal('geoware', ['Country'])

        # Adding M2M table for field altnames on 'Country'
        db.create_table('geoware-country_altnames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('country', models.ForeignKey(orm['geoware.country'], null=False)),
            ('altname', models.ForeignKey(orm['geoware.altname'], null=False))
        ))
        db.create_unique('geoware-country_altnames', ['country_id', 'altname_id'])

        # Adding M2M table for field neighbours on 'Country'
        db.create_table('geoware-country_neighbours', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_country', models.ForeignKey(orm['geoware.country'], null=False)),
            ('to_country', models.ForeignKey(orm['geoware.country'], null=False))
        ))
        db.create_unique('geoware-country_neighbours', ['from_country_id', 'to_country_id'])

        # Adding M2M table for field languages on 'Country'
        db.create_table('geoware-country_languages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('country', models.ForeignKey(orm['geoware.country'], null=False)),
            ('language', models.ForeignKey(orm['geoware.language'], null=False))
        ))
        db.create_unique('geoware-country_languages', ['country_id', 'language_id'])

        # Adding model 'Currency'
        db.create_table('geoware-currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=40, db_index=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('fractional_unit', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('fractional_ratio', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('geoware', ['Currency'])

        # Adding unique constraint on 'Currency', fields ['name', 'code']
        db.create_unique('geoware-currency', ['name', 'code'])

        # Adding model 'District'
        db.create_table('geoware-district', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('name_std', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('population', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('elevation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('geoname_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('bbw', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('bbn', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('bbe', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('bbs', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(default='POINT(0.0 0.0)')),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_district_city', null=True, to=orm['geoware.City'])),
        ))
        db.send_create_signal('geoware', ['District'])

        # Adding unique constraint on 'District', fields ['name', 'city']
        db.create_unique('geoware-district', ['name', 'city_id'])

        # Adding M2M table for field altnames on 'District'
        db.create_table('geoware-district_altnames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('district', models.ForeignKey(orm['geoware.district'], null=False)),
            ('altname', models.ForeignKey(orm['geoware.altname'], null=False))
        ))
        db.create_unique('geoware-district_altnames', ['district_id', 'altname_id'])

        # Adding model 'Language'
        db.create_table('geoware-language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=40, db_index=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dialect', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('geoware', ['Language'])

        # Adding model 'Ocean'
        db.create_table('geoware-ocean', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('name_std', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('population', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('elevation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('geoname_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('depth_name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
        ))
        db.send_create_signal('geoware', ['Ocean'])

        # Adding M2M table for field altnames on 'Ocean'
        db.create_table('geoware-ocean_altnames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ocean', models.ForeignKey(orm['geoware.ocean'], null=False)),
            ('altname', models.ForeignKey(orm['geoware.altname'], null=False))
        ))
        db.create_unique('geoware-ocean_altnames', ['ocean_id', 'altname_id'])

        # Adding model 'Region'
        db.create_table('geoware-region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('name_std', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('population', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('elevation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('geoname_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_region_country', null=True, to=orm['geoware.Country'])),
            ('capital', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_region_capital', null=True, to=orm['geoware.City'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('fips', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal('geoware', ['Region'])

        # Adding unique constraint on 'Region', fields ['name', 'country']
        db.create_unique('geoware-region', ['name', 'country_id'])

        # Adding M2M table for field altnames on 'Region'
        db.create_table('geoware-region_altnames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('region', models.ForeignKey(orm['geoware.region'], null=False)),
            ('altname', models.ForeignKey(orm['geoware.altname'], null=False))
        ))
        db.create_unique('geoware-region_altnames', ['region_id', 'altname_id'])

        # Adding model 'Subregion'
        db.create_table('geoware-subregion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('name_std', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('population', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('elevation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('geoname_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_subregion_region', null=True, to=orm['geoware.Region'])),
            ('capital', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_subregion_capital', null=True, to=orm['geoware.City'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('fips', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal('geoware', ['Subregion'])

        # Adding unique constraint on 'Subregion', fields ['name', 'region']
        db.create_unique('geoware-subregion', ['name', 'region_id'])

        # Adding M2M table for field altnames on 'Subregion'
        db.create_table('geoware-subregion_altnames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subregion', models.ForeignKey(orm['geoware.subregion'], null=False)),
            ('altname', models.ForeignKey(orm['geoware.altname'], null=False))
        ))
        db.create_unique('geoware-subregion_altnames', ['subregion_id', 'altname_id'])

        # Adding model 'Timezone'
        db.create_table('geoware-timezone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name_id', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('gmt_offset', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dst_offset', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('raw_offset', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geoware_timezone_country', null=True, to=orm['geoware.Country'])),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=254, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('geoware', ['Timezone'])


    def backwards(self, orm):
        # Removing unique constraint on 'Subregion', fields ['name', 'region']
        db.delete_unique('geoware-subregion', ['name', 'region_id'])

        # Removing unique constraint on 'Region', fields ['name', 'country']
        db.delete_unique('geoware-region', ['name', 'country_id'])

        # Removing unique constraint on 'District', fields ['name', 'city']
        db.delete_unique('geoware-district', ['name', 'city_id'])

        # Removing unique constraint on 'Currency', fields ['name', 'code']
        db.delete_unique('geoware-currency', ['name', 'code'])

        # Removing unique constraint on 'Continent', fields ['name', 'code']
        db.delete_unique('geoware-continent', ['name', 'code'])

        # Deleting model 'Altname'
        db.delete_table('geoware-altname')

        # Deleting model 'City'
        db.delete_table('geoware-city')

        # Removing M2M table for field altnames on 'City'
        db.delete_table('geoware-city_altnames')

        # Deleting model 'Continent'
        db.delete_table('geoware-continent')

        # Removing M2M table for field altnames on 'Continent'
        db.delete_table('geoware-continent_altnames')

        # Deleting model 'Country'
        db.delete_table('geoware-country')

        # Removing M2M table for field altnames on 'Country'
        db.delete_table('geoware-country_altnames')

        # Removing M2M table for field neighbours on 'Country'
        db.delete_table('geoware-country_neighbours')

        # Removing M2M table for field languages on 'Country'
        db.delete_table('geoware-country_languages')

        # Deleting model 'Currency'
        db.delete_table('geoware-currency')

        # Deleting model 'District'
        db.delete_table('geoware-district')

        # Removing M2M table for field altnames on 'District'
        db.delete_table('geoware-district_altnames')

        # Deleting model 'Language'
        db.delete_table('geoware-language')

        # Deleting model 'Ocean'
        db.delete_table('geoware-ocean')

        # Removing M2M table for field altnames on 'Ocean'
        db.delete_table('geoware-ocean_altnames')

        # Deleting model 'Region'
        db.delete_table('geoware-region')

        # Removing M2M table for field altnames on 'Region'
        db.delete_table('geoware-region_altnames')

        # Deleting model 'Subregion'
        db.delete_table('geoware-subregion')

        # Removing M2M table for field altnames on 'Subregion'
        db.delete_table('geoware-subregion_altnames')

        # Deleting model 'Timezone'
        db.delete_table('geoware-timezone')


    models = {
        'geoware.altname': {
            'Meta': {'object_name': 'Altname', 'db_table': "'geoware-altname'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_preferred': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_short': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_altname_language'", 'null': 'True', 'to': "orm['geoware.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'geoware.city': {
            'Meta': {'object_name': 'City', 'db_table': "'geoware-city'"},
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_city_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bbe': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbn': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbs': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbw': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_city_country'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT(0.0 0.0)'"}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_city_region'", 'null': 'True', 'to': "orm['geoware.Region']"}),
            'sister': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geoware.City']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'subregion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_city_subregion'", 'null': 'True', 'to': "orm['geoware.Subregion']"}),
            'timezone': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_city_timezone'", 'null': 'True', 'to': "orm['geoware.Timezone']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.continent': {
            'Meta': {'unique_together': "[('name', 'code')]", 'object_name': 'Continent', 'db_table': "'geoware-continent'"},
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_continent_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.country': {
            'Meta': {'object_name': 'Country', 'db_table': "'geoware-country'"},
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_country_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'capital': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_country_capital'", 'null': 'True', 'to': "orm['geoware.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_country_continent'", 'null': 'True', 'to': "orm['geoware.Continent']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_country_currency'", 'null': 'True', 'to': "orm['geoware.Currency']"}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'iso_3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'iso_n': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_country_jurisdiction'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_country_languagues'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'neighbours': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'neighbours_rel_+'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'tld': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.currency': {
            'Meta': {'unique_together': "(('name', 'code'),)", 'object_name': 'Currency', 'db_table': "'geoware-currency'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fractional_ratio': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fractional_unit': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.district': {
            'Meta': {'unique_together': "[('name', 'city')]", 'object_name': 'District', 'db_table': "'geoware-district'"},
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_district_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bbe': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbn': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbs': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbw': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_district_city'", 'null': 'True', 'to': "orm['geoware.City']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT(0.0 0.0)'"}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.language': {
            'Meta': {'object_name': 'Language', 'db_table': "'geoware-language'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dialect': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.ocean': {
            'Meta': {'object_name': 'Ocean', 'db_table': "'geoware-ocean'"},
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_ocean_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'depth_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.region': {
            'Meta': {'unique_together': "[('name', 'country')]", 'object_name': 'Region', 'db_table': "'geoware-region'"},
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_region_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'capital': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_region_capital'", 'null': 'True', 'to': "orm['geoware.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_region_country'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.subregion': {
            'Meta': {'unique_together': "[('name', 'region')]", 'object_name': 'Subregion', 'db_table': "'geoware-subregion'"},
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_subregion_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'capital': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_subregion_capital'", 'null': 'True', 'to': "orm['geoware.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_subregion_region'", 'null': 'True', 'to': "orm['geoware.Region']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.timezone': {
            'Meta': {'object_name': 'Timezone', 'db_table': "'geoware-timezone'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_timezone_country'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dst_offset': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'gmt_offset': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name_id': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'raw_offset': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['geoware']